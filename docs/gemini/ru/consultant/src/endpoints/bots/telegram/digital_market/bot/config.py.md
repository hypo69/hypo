# Анализ кода модуля `config`

**Качество кода**:
   - **Соответствие стандартам**: 7
   - **Плюсы**:
     - Использование `pydantic_settings` для управления настройками, что упрощает работу с переменными окружения.
     - Применение `aiogram` для создания Telegram-бота.
     - Использование `MemoryStorage` для хранения состояния бота.
     - Применение `@property` для динамического формирования URL вебхуков.
     - Наличие комментариев в коде.
   - **Минусы**:
     - Использование `loguru` вместо `src.logger`.
     - Использование двойных кавычек в строковых литералах, что противоречит стандартам кодирования.
     - Отсутствие документации в формате RST для класса `Settings` и его методов.
     - Смешивание логики настройки с объявлением переменных и инициализацией объектов.

**Рекомендации по улучшению**:

   - Заменить `from loguru import logger` на `from src.logger import logger`.
   - Использовать одинарные кавычки для строковых литералов в коде, за исключением вывода и логгирования.
   - Добавить документацию в формате RST для класса `Settings` и его методов.
   - Перенести инициализацию логгера в отдельную функцию или блок, чтобы отделить логику настройки от основной части кода.
   - Проверить использование всех импортов и выровнять их по алфавиту.
   - Добавить проверку на корректность переменных окружения.
   - Избегать множественной инициализации объектов.
   - Добавить комментарии в формате RST для функций, методов и классов.
   - Заменить явное использование `os.path.join` на pathlib для более читаемого и кроссплатформенного кода.
   - Удалить неиспользуемые переменные.

**Оптимизированный код**:

```python
import os
from pathlib import Path
from typing import List

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.logger import logger #  Импорт логгера из src.logger


class Settings(BaseSettings):
    """
    Настройки для Telegram-бота.

    :ivar BOT_TOKEN: Токен Telegram-бота.
    :vartype BOT_TOKEN: str
    :ivar ADMIN_IDS: Список ID администраторов.
    :vartype ADMIN_IDS: List[int]
    :ivar PROVIDER_TOKEN: Токен платежного провайдера.
    :vartype PROVIDER_TOKEN: str
    :ivar FORMAT_LOG: Формат логирования.
    :vartype FORMAT_LOG: str
    :ivar LOG_ROTATION: Размер ротации логов.
    :vartype LOG_ROTATION: str
    :ivar DB_URL: URL базы данных.
    :vartype DB_URL: str
    :ivar SITE_URL: URL сайта.
    :vartype SITE_URL: str
    :ivar SITE_HOST: Хост сайта.
    :vartype SITE_HOST: str
    :ivar SITE_PORT: Порт сайта.
    :vartype SITE_PORT: int
    :ivar MRH_LOGIN: Логин для MRH.
    :vartype MRH_LOGIN: str
    :ivar MRH_PASS_1: Пароль 1 для MRH.
    :vartype MRH_PASS_1: str
    :ivar MRH_PASS_2: Пароль 2 для MRH.
    :vartype MRH_PASS_2: str
    :ivar IN_TEST: Флаг тестового режима.
    :vartype IN_TEST: int
    """
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    PROVIDER_TOKEN: str
    FORMAT_LOG: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}' #  Используем одинарные кавычки
    LOG_ROTATION: str = '10 MB' #  Используем одинарные кавычки
    DB_URL: str = 'sqlite+aiosqlite:///data/db.sqlite3' #  Используем одинарные кавычки
    SITE_URL: str
    SITE_HOST: str
    SITE_PORT: int
    MRH_LOGIN: str
    MRH_PASS_1: str
    MRH_PASS_2: str
    IN_TEST: int
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / '.env' #  Используем Path для создания пути к файлу
    )

    @property
    def get_webhook_url(self) -> str:
        """
        Формирует URL для вебхука бота.

        :return: URL вебхука бота.
        :rtype: str

        Пример:
            >>> settings = Settings(SITE_URL='https://example.com', BOT_TOKEN='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
            >>> settings.get_webhook_url
            'https://example.com/123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
        """
        return f"{self.SITE_URL}/{self.BOT_TOKEN}"

    @property
    def get_provider_hook_url(self) -> str:
        """
        Формирует URL для вебхука платежного провайдера.

        :return: URL вебхука платежного провайдера.
        :rtype: str

        Пример:
            >>> settings = Settings(SITE_URL='https://example.com')
            >>> settings.get_provider_hook_url
            'https://example.com/robokassa'
        """
        return f"{self.SITE_URL}/robokassa"


# Получаем параметры для загрузки переменных среды
settings = Settings() # Инициализация настроек

# Инициализируем бота и диспетчер
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) # Инициализация бота
dp = Dispatcher(storage=MemoryStorage()) # Инициализация диспетчера
admins = settings.ADMIN_IDS #  Получение списка администраторов

log_file_path = Path(__file__).parent / 'log.txt' #  Используем Path для создания пути к файлу
logger.add(str(log_file_path), format=settings.FORMAT_LOG, level='INFO', rotation=settings.LOG_ROTATION) # Настройка логгера
database_url = settings.DB_URL #  Получение URL базы данных
```