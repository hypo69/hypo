## Анализ кода модуля `scenario.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Четкая структура классов и функций.
  - Использование асинхронности для неблокирующих операций.
  - Логирование ошибок с использованием `logger.error`.
  - Использование `BeautifulSoup` и `requests` для парсинга данных.
  - Использование `j_dumps` для записи JSON.
- **Минусы**:
  - Не все функции и методы имеют docstring.
  - Не везде используются аннотации типов.
  - Некоторые комментарии отсутствуют или не полные.
  - Жестко заданы некоторые параметры, такие как `lang_index: int = 2`.
  - Дублирование кода при отправке сообщений в `bot`.
  - Не все переменные и параметры имеют аннотацию типов.

**Рекомендации по улучшению:**

1.  **Документирование кода**:
    *   Добавить docstring к функциям `run_sample_scenario` и `__init__` класса `Scenario`.
    *   Улучшить описание для функции `fetch_target_urls_onetab`.
2.  **Аннотации типов**:
    *   Добавить аннотации типов для всех переменных и параметров функций, где это необходимо.
3.  **Улучшение обработки ошибок**:
    *   Улучшить обработку ошибок в функции `fetch_target_urls_onetab`, чтобы возвращать более информативные значения при возникновении исключений.
4.  **Рефакторинг**:
    *   Удалить закомментированный код, который больше не используется (`# if 'window_mode' not in kwards:`).
    *   Избегать дублирования кода при отправке сообщений в `bot`. Создать отдельную функцию для отправки сообщений.
    *   Использовать `j_loads` или `j_loads_ns` для чтения конфигурационных файлов, если они используются.
5.  **Стандартизация**:
    *   Привести код в соответствие со стандартами PEP8.
    *   Убедиться, что все импорты организованы и соответствуют рекомендациям.
6.  **Использовать `logger`**:
    *   Убедиться, что все ошибки логируются с использованием `logger.error` с указанием `exc_info=True` для вывода трассировки стека.

**Оптимизированный код:**

```python
## \file /src/endpoints/kazarinov/scenarios/scenario.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
.. module:: src.endpoints.kazarinov.scenarios.scenario
	:platform: Windows, Unix
	:synopsis: Сценарий для Казаринова

"""

from bs4 import BeautifulSoup
import requests
import telebot
import asyncio
from pathlib import Path
from typing import Optional, List, Tuple

import header
from src import gs
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.webdriver.playwright import Playwrid
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.kazarinov.report_generator.report_generator import ReportGenerator
from src.endpoints.kazarinov.scenarios.quotation_builder import QuotationBuilder
from src.endpoints.prestashop.product_fields.product_fields import ProductFields
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.utils.jjson import j_dumps
from src.logger.logger import logger

##############################################################

ENDPOINT = 'kazarinov'

#############################################################


def fetch_target_urls_onetab(one_tab_url: str) -> tuple[str, str, list[str]] | tuple[bool, bool, bool]:
    """
    Извлекает целевые URL из OneTab URL.

    Args:
        one_tab_url (str): URL OneTab страницы.

    Returns:
        tuple[str, str, list[str]] | tuple[bool, bool, bool]: Кортеж, содержащий цену, имя Mexiron и список URL,
        или (False, False, False) в случае ошибки.
    
    Raises:
        requests.exceptions.RequestException: При ошибке выполнения HTTP запроса.

    Example:
        >>> url = 'http://example.com/onetab_url'
        >>> price, mexiron_name, urls = fetch_target_urls_onetab(url)
        >>> if price and mexiron_name and urls:
        ...     print(f'Price: {price}, Name: {mexiron_name}, URLs: {urls}')
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
        logger.error(f'Ошибка при выполнении запроса: {one_tab_url=}', ex, exc_info=True)
        return False, False, False


class Scenario(QuotationBuilder):
    """Исполнитель сценария для Казаринова"""

    def __init__(self, mexiron_name: Optional[str] = gs.now, driver: Optional[Firefox | Playwrid | str] = None, **kwards):
        """
        Инициализирует сценарий сбора информации.

        Args:
            mexiron_name (Optional[str]): Имя Mexiron. По умолчанию gs.now.
            driver (Optional[Firefox | Playwrid | str]): Драйвер для управления браузером. По умолчанию None.
            **kwards: Дополнительные параметры.
        """
        kwards['window_mode'] = 'normal'
        self.driver = Driver(Firefox, **kwards) if not driver else driver

        super().__init__(mexiron_name=mexiron_name, driver=self.driver, **kwards)

    async def run_scenario_async(
        self,
        urls: List[str],
        price: Optional[str] = '',
        mexiron_name: Optional[str] = gs.now,
        bot: Optional[telebot.TeleBot] = None,
        chat_id: Optional[int] = 0,
        attempts: int = 3,
    ) -> bool:
        """
        Выполняет сценарий: парсит продукты, обрабатывает их через AI и сохраняет данные.

        Args:
            urls (List[str]): Список URL для парсинга.
            price (Optional[str]): Цена. По умолчанию ''.
            mexiron_name (Optional[str]): Имя Mexiron. По умолчанию gs.now.
            bot (Optional[telebot.TeleBot]): Telegram бот для отправки сообщений. По умолчанию None.
            chat_id (Optional[int]): ID чата для отправки сообщений. По умолчанию 0.
            attempts (int): Количество попыток выполнения. По умолчанию 3.

        Returns:
            bool: True, если выполнение успешно, иначе False.
        """

        products_list = []

        # -------------------------------------------------
        # 1. Сбор товаров

        lang_index: int = 2
        for url in urls:
            kwards: dict = {}
            graber: 'Graber' = get_graber_by_supplier_url(self.driver, url, lang_index, **kwards)

            if not graber:
                logger.error(f'Нет грабера для: {url}')
                await self._send_message(bot, chat_id, f'Нет грабера для: {url}') # Отправка сообщения об ошибке
                continue

            f: ProductFields = None
            if bot: await self._send_message(bot, chat_id, f'Process: {url}') # Отправка сообщения о начале обработки
            try:
                f = await graber.grab_page_async(*self.required_fields)
            except Exception as ex:
                logger.error(f'Failed... Ошибка получения полей товара {url}:', ex, exc_info=True)
                await self._send_message(bot, chat_id, f'Failed... Ошибка получения полей товара {url}\\n{ex}') # Отправка сообщения об ошибке
                continue

            if not f:
                logger.error(f'Failed to parse product fields for URL: {url}')
                await self._send_message(bot, chat_id, f'Failed to parse product fields for URL: {url}') # Отправка сообщения об ошибке
                continue

            product_data = self.convert_product_fields(f)
            if not product_data:
                logger.error(f'Failed to convert product fields: {product_data}')
                await self._send_message(bot, chat_id, f'Failed to convert product fields {url} \\n {product_data}') # Отправка сообщения об ошибке
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
            if bot:
                await self._send_message(
                    bot,
                    chat_id,
                    f'AI processing {lang=}',
                )
            try:
                data: dict = await self.process_ai_async(products_list, lang)
                if not data:
                    await self._send_message(bot, chat_id, f'Ошибка модели для {lang=}') # Отправка сообщения об ошибке
                    # Альтернатива рекурсии: просто пропустить этот язык
                    continue
            except Exception as ex:
                logger.error(f'AI processing failed for {lang=}', exc_info=True)
                await self._send_message(bot, chat_id, f'AI processing failed for {lang=}: {ex}') # Отправка сообщения об ошибке
                continue

            # -----------------------------------------------------------------
            # 3. Report creating

            if bot: await self._send_message(bot, chat_id, f'Создаю файл') # Отправка сообщения о создании файла
            data = data[lang]
            data['price'] = price
            data['currency'] = getattr(self.translations.currency, lang, 'ש\'\'ח')

            j_dumps(data, self.export_path / f'{self.mexiron_name}_{lang}.json')

            reporter = ReportGenerator(if_need_docx=False)
            await reporter.create_reports_async(
                bot=bot,
                chat_id=chat_id,
                data=data,
                lang=lang,
                mexiron_name=self.mexiron_name,
            )

        return True  # Возвращаем True в конце

    async def _send_message(self, bot: telebot.TeleBot, chat_id: int, text: str) -> None:
        """
        Отправляет сообщение в Telegram, если бот и chat_id предоставлены.

        Args:
            bot (telebot.TeleBot): Экземпляр бота Telegram.
            chat_id (int): ID чата для отправки сообщения.
            text (str): Текст сообщения для отправки.
        """
        if bot:
            try:
                await bot.send_message(chat_id, text)
            except Exception as ex:
                logger.error(f'Failed to send message to Telegram: {text}', ex, exc_info=True)

def run_sample_scenario():
    """
    Запускает пример сценария.
    """
    ...
    urls_list: list[str] = ['https://www.morlevi.co.il/product/21039',
                           'https://www.morlevi.co.il/product/21018',
                           'https://www.ivory.co.il/catalog.php?id=85473',
                           'https://grandadvance.co.il/eng/?go=products&action=view&ties_ids=801&product_id=28457--SAMSUNG-SSD-1TB-990-EVO-PCle-4.0-x4--5.0-x2-NVMe',
                           'https://www.ivory.co.il/catalog.php?id=85473',
                           'https://www.morlevi.co.il/product/21018']

    s = Scenario(window_mode='headless')
    asyncio.run(s.run_scenario_async(urls=urls_list, mexiron_name='test price quotation', ))


if __name__ == '__main__':
    run_sample_scenario()