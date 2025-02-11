from bs4 import BeautifulSoup
import requests
import telebot
import asyncio
from pathlib import Path
from typing import Optional, List

import header
from src import gs
from src.endpoints.kazarinov.report_generator.report_generator import ReportGenerator
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.utils.jjson import j_dumps
from src.logger.logger import logger

##############################################################

ENDPOINT = "kazarinov"

#############################################################


def fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | bool:
    """
    Функция паресит целевые URL из полученного OneTab.

    Args:
        one_tab_url (str): URL страницы OneTab.

    Returns:
        price, mexiron_name, urls (tuple):
            price (str): Цена.
            mexiron_name (str): Имя Mexiron.
            urls (list): Список целевых URL.

    """
    try:
        response = requests.get(one_tab_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # Извлечение ссылок
        urls = [a["href"] for a in soup.find_all("a", class_="tabLink")]

        # Извлечение данных из div с классом 'tabGroupLabel'
        element = soup.find("div", class_="tabGroupLabel")
        data = element.get_text() if element else None

        if not data:
            price = ""
            mexiron_name = gs.now
        else:
            # Разбивка данных на цену и имя
            parts = data.split(maxsplit=1)
            price = int(parts[0]) if parts[0].isdigit() else ""
            mexiron_name = parts[1] if len(parts) > 1 else gs.now

        return price, mexiron_name, urls

    except requests.exceptions.RequestException as ex:
        logger.error(f"Ошибка при выполнении запроса: {one_tab_url=}", ex)
        ...
        return False, False, False


class Scenario(QuotationBuilder):
    """Исполнитель сценария для Казаринова
    one-tab.com -> telegram -> ai  -> pdf(docx,html)
    """

    def __init__(self, mexiron_name: Optional[str] = gs.now):
        """Сценарий сбора информации. Результат уходит в конструктор ценового предложения `QuotationBuilder`
        Сценарий возвращает боту ответы о процессе исполненения
        """
        self.mexiron_name = mexiron_name
        super().__init__(self.mexiron_name)

    def run_scenario(
        self,
        bot: telebot.TeleBot,
        chat_id: int,
        urls: list[str,str],
        price: Optional[str] = '',
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

        lang_index: int = 2  # <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEV. индекс, указывающий ID языка в магазине Prstashop
        for url in urls:
            graber: 'Graber' = get_graber_by_supplier_url(self.driver, url, lang_index)

            if not graber:
                logger.debug(f"Нет грабера для: {url}")
                continue

            f: ProductFields = None
            bot.send_message(chat_id, f"Process: {url}")
            try:
                f = graber.grab_page(*self.required_fields)
            except Exception as ex:
                logger.error(f"Failed... Ошибка получения полей товара {url}:", ex)
                continue

            if not f:
                logger.error(f"Failed to parse product fields for URL: {url}")
                bot.send_message(chat_id, f"Failed to parse product fields for URL: {url}")
                continue

            product_data = self.convert_product_fields(f)
            if not product_data:
                logger.error(f"Failed to convert product fields: {product_data}")
                bot.send_message(chat_id, f"Failed to convert product fields {url}")
                continue

            asyncio.run( self.save_product_data(product_data))
            products_list.append(product_data)

        # -----------------------------------------------------
        # 2. AI processing

        """ список компонентов сборки компьютера уходит в обработку моделью (`gemini`) ->
        модель парсит данные, делает перевод на `ru`, `he` и возвращает кортеж словарей по языкам.
        Внимание! модель может ошибаться"""

        langs_list: list = ["he", "ru"]

        for lang in langs_list:            
            bot.send_message(
                chat_id,
                f"""AI processing {lang=}""",
            )
            data: dict = self.process_ai(products_list, lang)
            if not data:
                bot.send_message(chat_id, f"Ошибка модели для {lang=}")
                continue


            # -----------------------------------------------------------------
            # 3. Report creating

            bot.send_message(chat_id, f"Создаю файл")
            data = data[lang]
            data["price"] = price
            data["currency"] = getattr(self.translations.currency, lang, "ש''ח")

            j_dumps(data, self.export_path / f'{self.mexiron_name}_{lang}.json')

            reporter = ReportGenerator(if_need_docx=False)
            reporter.create_reports(bot = bot,
                                chat_id = chat_id,
                                data = data, 
                                lang = lang,
                                mexiron_name = self.mexiron_name
                                    )
                
        ...


