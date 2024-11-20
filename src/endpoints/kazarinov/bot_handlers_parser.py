## \file hypotez/src/endpoints/kazarinov/bot_handlers_parser.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.kazarinov """
MODE = 'development'
import header

import asyncio
from src import gs
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
from src.ai.gemini import GoogleGenerativeAI

from src.endpoints.kazarinov.scenarios.scenario_pricelist import Mexiron
from src.utils.string.url import is_url
from src.logger import logger
from typing import Optional, Any

class HandlersParser():
    """Исполнитель команд, полученных ботом."""
    mexiron:Mexiron
    def __init__(self, webdriver_name:Optional[str] = 'firefox'):
        """"""
        logger.info('handler started')
        self.mexiron: Mexiron = Mexiron(Driver(Firefox  if  webdriver_name.lower() == 'firefox' else Chrome))

    async def handle_url(self, update: Update, context: CallbackContext) -> Any:
        """"""
        ...
        price, mexiron_name, urls = self.handle_onetab_url(update.message.text)
        if price or mexiron_name or urls:
            if await self.mexiron.run_scenario(price=price, mexiron_name=mexiron_name, urls=urls):
                await update.message.reply_text('Готово!\nСсылку я вышлю на WhatsApp')
                return True

        else:
            await update.message.reply_text('Ошибка. Попробуй ещё раз.')
            return False

    def handle_supplier_url(self, update: Update) -> Optional[bool]:
        """Map URLs to specific handlers."""
        if any(response.startswith(url) for url in self.config.url_handlers.suppliers):
            # Здесь будет код для обработки ссылок поставщиков
            pass
        return False, False, False

    async def handle_onetab_url(self, update: Update, response: str) -> list[int | float, str, list] | bool:
        """Handle OneTab URLs."""
        if not response.startswith(('https://onetab.com', 'http://onetab.com')):
            return False, False, False

        price, mexiron_name, urls = fetch_target_urls_onetab(response)

        if not all([price, mexiron_name, urls]):
            await update.message.reply_text('Ошибка на сервере OneTab. Попробуй ещё раз через часок.')
            return False, False, False

        return price, mexiron_name, urls




    async def handle_next_command(self, update: Update) -> None:
        """Handle '--next' and related commands."""
        try:
            question = random.choice(self.questions_list)
            answer = self.model.ask(question)
            await asyncio.gather(
                update.message.reply_text(question),
                update.message.reply_text(answer)
            )
        except Exception as ex:
            logger.debug("Ошибка чтения вопросов: %s", ex)
            await update.message.reply_text('Произошла ошибка при чтении вопросов.')


    def fetch_target_urls_onetab(self, target_page_url: str) -> list[str] | bool:
        """Извлекает целевые URL с указанного URL OneTab.

        Выполняет GET-запрос к указанному URL, парсит HTML-контент
        и извлекает все ссылки из тегов 'a' с классом 'tabLink'.

        Args:
            target_page_url (str): URL страницы OneTab для извлечения целевых URL.

        Returns:
            Tuple[int, str, List[str]] | bool: Кортеж из цены, имени и списка URL 
            или `False`, если произошла ошибка.

        Raises:
            requests.exceptions.RequestException: При ошибке запроса.
        """
        try:
            response = requests.get(target_page_url, timeout=10)
            response.raise_for_status()

            if response.status_code != 200:
                logger.debug(f'Ошибка response\n{pprint(response)}')
                return False

            soup = BeautifulSoup(response.content, 'html.parser')

            # Извлечение ссылок
            urls = [a['href'] for a in soup.find_all('a', class_='tabLink')]

            # Извлечение данных из div с классом 'tabGroupLabel'
            element = soup.find('div', class_='tabGroupLabel')
            data = element.get_text() if element else None

            if not data:
                return False

            # Разбивка данных на цену и имя
            parts = data.split(maxsplit=1)
            try:
                price = int(parts[0])
            except ValueError as ex:
                logger.error(f'Ошибка при преобразовании цены: {ex}')
                return False

            mexiron_name = parts[1] if len(parts) > 1 else gs.now

            return price, mexiron_name, urls

        except requests.exceptions.RequestException as ex:
            logger.error(f'Ошибка при выполнении запроса: {ex}')
            return False