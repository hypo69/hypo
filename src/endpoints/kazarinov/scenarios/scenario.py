from bs4 import BeautifulSoup
import requests
import telebot
import asyncio
from pathlib import Path
from typing import Optional, List

import header
from src import gs
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.utils.jjson import j_dumps
from src.logger.logger import logger


def fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | bool:
    """
    Извлечение целевых URL с указанного URL OneTab.

    Args:
        one_tab_url (str): URL страницы OneTab.

    Returns:
        list[str] | bool: Список целевых URL или False при ошибке.
    """
    try:
        response = requests.get(one_tab_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Извлечение ссылок
        urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

        # Извлечение данных из div с классом 'tabGroupLabel'
        element = soup.find('div', class_='tabGroupLabel')
        data = element.get_text() if element else None

        if not data:
            price = ''
            mexiron_name = gs.now
        else:
            # Разбивка данных на цену и имя
            parts = data.split(maxsplit=1)
            price = int(parts[0]) if parts[0].isdigit() else ''
            mexiron_name = parts[1] if len(parts) > 1 else gs.now

        return price, mexiron_name, urls

    except requests.exceptions.RequestException as ex:
        logger.error('Ошибка при выполнении запроса: %s', ex)
        return False


class Scenario(QuotationBuilder):

    def __init__(self):
        """Сценарий сбора информации. Результат уходит в конструктор ценового предложения `QuotationBuilder`
        Сценарий возвращает боту ответы о процессе исполненения
        """
        super().__init__()

    async def run_scenario(
        self,
        bot:telebot.TeleBot,
        chat_id:int,
        urls: list[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = '',
    ) -> bool:
        """
        Executes the scenario: parses products, processes them via AI, and stores data.

        Args:
            system_instruction (Optional[str]): System instructions for the AI model.
            price (Optional[str]): Price to process.
            mexiron_name (Optional[str]): Custom Mexiron name.
            urls (Optional[str | List[str]]): Product page URLs.

        Returns:
            bool: True if the scenario executes successfully, False otherwise.

        .. todo:
            сделать логер перед отрицательным выходом из функции.
            Важно! модель ошибается.

        """

        products_list = []

        # -------------------------------------------------
        # 1. Сбор товаров

        lang_index:int = 3 # индекс, указывающий ID языка в магазине Prstashop
        for url in urls:
            graber: 'Graber' = get_graber_by_supplier_url(self.driver, url, lang_index)

            if not graber:
                logger.debug(f"Нет грабера для: {url}")
                continue

            try:
                bot.send_message(chat_id, f"Process: {url}")
                f:ProductFields = await graber.grab_page(*self.required_fields)
            except Exception as ex:
                logger.error(f"Ошибка получения полей товара {url}: {ex}")
                continue

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}')
                continue

            product_data = self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Failed to convert product fields: {product_data}')
                continue

            await self.save_product_data(product_data)
            products_list.append(product_data)

        # -----------------------------------------------------
        # 2. AI processing
        """ список компонентов сборки компьютера уходит в обработку моделью (`gemini`) ->
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться"""

        langs_list: list = ['he', 'ru']
        for lang in langs_list:
            bot.send_message(chat_id, f"""AI processing lang = {lang}.
           Это может занять время. Зависит от загрузки модели""")
            data: dict = await self.process_ai(products_list, lang)
            if not data:
                bot.send_message(chat_id, "Ошибка модели")
                continue

            # -----------------------------------------------------------------
            # 3. Report creating

            data[lang]['price'] = price
            data[lang]['currency'] = getattr(self.translations.currency, lang, "ש''ח")

            if not j_dumps(data, self.export_path / f'{self.mexiron_name}_{lang}.json'):
                logger.error("Ошибка JSON")

            html_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.html')
            pdf_file = Path(self.export_path / f'{self.mexiron_name}_{lang}.pdf')

            await self.create_report(data[lang], lang, html_file, pdf_file)

            try:
                with open(pdf_file, 'rb') as f:
                    bot.send_document(chat_id, f)
            except Exception as ex:
                logger.error(f'Ошибка при отправке PDF-файла: {ex}')
                bot.send_message(chat_id, 'Произошла ошибка при отправке PDF-файла. ')
