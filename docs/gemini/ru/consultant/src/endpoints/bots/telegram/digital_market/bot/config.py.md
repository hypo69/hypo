# Анализ кода модуля `config.py`

**Качество кода**
8
-  Плюсы
    - Код использует `pydantic_settings` для управления настройками, что обеспечивает валидацию и удобство доступа к переменным окружения.
    - Используется `aiogram` для работы с Telegram ботом, что является стандартом для подобных приложений.
    - Настройки логирования вынесены в переменные окружения и применяются через `loguru`.
    - Конфигурация вебхуков динамически формируется на основе токена и URL сайта.
-  Минусы
    - Отсутствует документация в формате RST.
    - Используются двойные кавычки в константах, хотя по инструкции должны использоваться одинарные.
    - Есть импорт `loguru`, хотя должен быть `from src.logger.logger import logger`.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов, хотя это указано в требованиях.
    - Некоторые переменные, такие как `SITE_URL`, `SITE_HOST`, `SITE_PORT`, `MRH_LOGIN`, `MRH_PASS_1`, `MRH_PASS_2`, `IN_TEST`, не имеют подробного описания.
    - Не хватает обработки ошибок для случая, когда переменные окружения не установлены.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Заменить все двойные кавычки на одинарные в константах, кроме операций вывода.
3.  Использовать `from src.logger.logger import logger` для логирования.
4.  Добавить RST-документацию для класса `Settings`, его методов и переменных.
5.  Обеспечить обработку ошибок при загрузке переменных окружения.
6.  Добавить более подробные комментарии к коду.
7.  Уточнить назначение и использование переменных `SITE_URL`, `SITE_HOST`, `SITE_PORT`, `MRH_LOGIN`, `MRH_PASS_1`, `MRH_PASS_2`, `IN_TEST`.

**Оптимизированный код**

```python
"""
Модуль конфигурации для Telegram бота цифрового рынка.
=========================================================================================

Этот модуль содержит класс :class:`Settings`, который загружает и управляет настройками
для Telegram бота, включая токен, идентификаторы администраторов, настройки логирования,
и параметры подключения к базе данных.

Пример использования
--------------------

Пример использования класса `Settings`:

.. code-block:: python

    settings = Settings()
    bot = Bot(token=settings.BOT_TOKEN)

"""
import os
from typing import List
# from loguru import logger #  заменил на  from src.logger.logger import logger
from src.logger.logger import logger
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс для хранения настроек бота.

    :cvar BOT_TOKEN: Токен Telegram бота.
    :vartype BOT_TOKEN: str
    :cvar ADMIN_IDS: Список идентификаторов администраторов бота.
    :vartype ADMIN_IDS: List[int]
    :cvar PROVIDER_TOKEN: Токен провайдера платежей.
    :vartype PROVIDER_TOKEN: str
    :cvar FORMAT_LOG: Формат логов.
    :vartype FORMAT_LOG: str
    :cvar LOG_ROTATION: Размер ротации логов.
    :vartype LOG_ROTATION: str
    :cvar DB_URL: URL базы данных.
    :vartype DB_URL: str
    :cvar SITE_URL: URL сайта.
    :vartype SITE_URL: str
    :cvar SITE_HOST: Хост сайта.
    :vartype SITE_HOST: str
    :cvar SITE_PORT: Порт сайта.
    :vartype SITE_PORT: int
    :cvar MRH_LOGIN: Логин для MRH.
    :vartype MRH_LOGIN: str
    :cvar MRH_PASS_1: Первый пароль для MRH.
    :vartype MRH_PASS_1: str
    :cvar MRH_PASS_2: Второй пароль для MRH.
    :vartype MRH_PASS_2: str
    :cvar IN_TEST: Флаг тестового режима.
    :vartype IN_TEST: int
    """
    BOT_TOKEN: str
    ADMIN_IDS: List[int]
    PROVIDER_TOKEN: str
    FORMAT_LOG: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}' # Изменил на одинарные ковычки
    LOG_ROTATION: str = '10 MB' # Изменил на одинарные ковычки
    DB_URL: str = 'sqlite+aiosqlite:///data/db.sqlite3' # Изменил на одинарные ковычки
    SITE_URL: str
    SITE_HOST: str
    SITE_PORT: int
    MRH_LOGIN: str
    MRH_PASS_1: str
    MRH_PASS_2: str
    IN_TEST: int
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env') # Изменил на одинарные ковычки
    )

    @property
    def get_webhook_url(self) -> str:
        """
        Динамически формирует путь для вебхука на основе токена и URL сайта.

        :return: URL вебхука.
        :rtype: str
        """
        return f'{self.SITE_URL}/{self.BOT_TOKEN}' # Изменил на одинарные ковычки

    @property
    def get_provider_hook_url(self) -> str:
        """
        Динамически формирует путь для вебхука провайдера на основе URL сайта.

        :return: URL вебхука провайдера.
        :rtype: str
        """
        return f'{self.SITE_URL}/robokassa' # Изменил на одинарные ковычки


# Получаем параметры для загрузки переменных среды
try:
    settings = Settings()
except Exception as e:
    logger.error(f'Не удалось загрузить настройки из переменных окружения: {e}') #  Логирование ошибки при загрузке настроек
    raise  # Пробрасываем исключение для прерывания работы.
# Инициализируем бота и диспетчер
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
admins = settings.ADMIN_IDS

# Настраиваем логирование
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.txt') # Изменил на одинарные ковычки
logger.add(log_file_path, format=settings.FORMAT_LOG, level='INFO', rotation=settings.LOG_ROTATION) # Изменил на одинарные ковычки
database_url = settings.DB_URL
```