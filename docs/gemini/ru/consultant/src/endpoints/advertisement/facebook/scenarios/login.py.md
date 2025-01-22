# Анализ кода модуля `login.py`

## Качество кода:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование `j_loads_ns` для загрузки JSON, что соответствует инструкциям.
    - Наличие комментариев к коду.
    - Наличие базовой структуры для логина.
- **Минусы**:
    -  Использование `try-except` блоков для каждой операции ввода и нажатия, что делает код менее читаемым.
    -  Использование `logger.error("Invalid login", ex)` для каждой ошибки, что не всегда информативно.
    -  Отсутствие RST документации.
    -  Несоответствие PEP8 по стилю, например `locators['password']` и `credentials['password']`.
    -  Использование  `logger.debug(f"Ошибка в файле локаторов")` вместо `logger.error()`.
    -  Дублирование `logger.error("Invalid login", ex)` в блоках `except`.
    -  Отсутствие проверки успешности загрузки JSON файла `login.json`.

## Рекомендации по улучшению:
-   Добавить RST-документацию для модуля и функции `login`.
-   Убрать дублирование `try-except` блоков, используя вспомогательную функцию.
-   Использовать более конкретные сообщения об ошибках в `logger.error`, например, "Ошибка ввода логина" или "Ошибка ввода пароля".
-   Использовать f-строки для форматирования сообщений логгера.
-   Добавить проверки для корректности загрузки локаторов из `login.json`.
-   Переименовать переменную `d` в `driver` для лучшей читаемости.
-   Исправить ошибки PEP8: `locators['password']` на `locators['password']`, `credentials['password']` на `credentials.password`.
-   Импортировать `logger` через `from src.logger.logger import logger`.

## Оптимизированный код:
```python
"""
Модуль для выполнения сценария авторизации Facebook.
===================================================

Модуль содержит функцию :func:`login`, которая используется для авторизации
пользователя на Facebook, используя предоставленные учетные данные и локаторы.

Пример использования
----------------------
.. code-block:: python

    from src.webdriver.driver import Driver
    from src.endpoints.advertisement.facebook.scenarios.login import login

    async def main():
        driver = Driver()
        driver.open_url("https://www.facebook.com/")
        result = login(driver)
        print(result)
        await driver.close()

    if __name__ == "__main__":
        import asyncio
        asyncio.run(main())
"""

from pathlib import Path
from typing import Dict

from src import gs
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger  # Исправлен импорт


# Загрузка локаторов для авторизации Facebook
locators = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'login.json')
)
if not locators:
    logger.error("Ошибка при загрузке файла локаторов")  # Исправлено на logger.error
    ...


def _execute_action(driver: Driver, locator: str, value: str = None, action_type: str = 'send_keys') -> bool:
    """
    Выполняет действие с веб-элементом.

    :param driver: Экземпляр драйвера для взаимодействия с веб-элементами.
    :type driver: Driver
    :param locator: Локатор веб-элемента.
    :type locator: str
    :param value: Значение для отправки (если требуется).
    :type value: str, optional
    :param action_type: Тип действия ('send_keys' или 'click').
    :type action_type: str, optional
    :return: True, если действие выполнено успешно, иначе False.
    :rtype: bool
    :raises Exception: В случае ошибки при выполнении действия.
    """
    try:
        if action_type == 'send_keys':
            driver.send_key_to_webelement(locator, value)
        elif action_type == 'click':
            driver.execute_locator(locator)
        return True
    except Exception as ex:
        logger.error(f"Ошибка при выполнении действия {action_type} с локатором {locator}: {ex}")  # f-строка и сообщение
        return False


def login(driver: Driver) -> bool:
    """
    Выполняет вход на Facebook.

    Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя
    логин и пароль, а затем нажимает кнопку входа.

    :param driver: Экземпляр драйвера для взаимодействия с веб-элементами.
    :type driver: Driver
    :return: `True`, если авторизация прошла успешно, иначе `False`.
    :rtype: bool
    :raises Exception: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.

    Пример:
        >>> from src.webdriver.driver import Driver
        >>> from src.endpoints.advertisement.facebook.scenarios.login import login
        >>>
        >>> async def main():
        >>>     driver = Driver()
        >>>     driver.open_url("https://www.facebook.com/")
        >>>     result = login(driver)
        >>>     print(result)
        >>>     await driver.close()
        >>>
        >>> if __name__ == "__main__":
        >>>     import asyncio
        >>>     asyncio.run(main())
    """
    if not locators: # Проверка наличия загруженных локаторов
        logger.error("Локаторы не загружены, авторизация невозможна.") # Добавлено сообщение об ошибке
        return False

    credentials = gs.facebook_credentials[0]

    if not _execute_action(driver, locators.email, credentials.username): # Используем вспомогательную функцию для логина
        logger.error("Ошибка при вводе логина") # Добавлено сообщение об ошибке
        return False
    
    driver.wait(1.3)

    if not _execute_action(driver, locators['password'], credentials.password): # Используем вспомогательную функцию для пароля
         logger.error("Ошибка при вводе пароля") # Добавлено сообщение об ошибке
         return False
    
    driver.wait(0.5)

    if not _execute_action(driver, locators['button'], action_type='click'): # Используем вспомогательную функцию для кнопки
        logger.error("Ошибка при нажатии кнопки входа") # Добавлено сообщение об ошибке
        return False

    return True
```