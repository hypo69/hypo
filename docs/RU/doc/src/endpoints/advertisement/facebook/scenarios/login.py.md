# Модуль `login.py`

## Обзор

Модуль `login.py` содержит функциональность для выполнения авторизации на Facebook с использованием Selenium WebDriver. Он загружает локаторы веб-элементов из JSON-файла и использует их для взаимодействия с элементами на странице входа.

## Содержание

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Локаторы](#локаторы)
4. [Функции](#функции)
    - [`login`](#login)

## Импорты

Модуль импортирует следующие библиотеки:

- `pathlib.Path`: Для работы с путями к файлам.
- `typing.Dict`: Для аннотации типов.
- `src.gs`: Глобальные настройки проекта.
- `src.webdriver.driver.Driver`: Класс драйвера для управления веб-браузером.
- `src.utils.jjson.j_loads, j_loads_ns, j_dumps`: Функции для работы с JSON.
- `src.logger.logger.logger`: Объект логгера.

## Локаторы

Локаторы веб-элементов для страницы входа в Facebook загружаются из файла `login.json` и хранятся в переменной `locators`.

## Функции

### `login`

**Описание**:
Выполняет вход на Facebook.

Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя логин и пароль, а затем нажимает кнопку входа.

**Параметры**:
- `d` (`Driver`): Экземпляр драйвера для взаимодействия с веб-элементами.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.
```python
def login(d: Driver) -> bool:
    """ Выполняет вход на Facebook.

    Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя
    логин и пароль, а затем нажимает кнопку входа.

    Args:
        d (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

    Returns:
        bool: `True`, если авторизация прошла успешно, иначе `False`.

    Raises:
        Exception: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.
    """
    credentials = gs.facebook_credentials[0]
    try:
        # Ввод логина
        d.send_key_to_webelement(locators.email, credentials.username)
    except Exception as ex:
        logger.error("Invalid login", ex)
        return False

    d.wait(1.3)
    try:
        # Ввод пароля
        d.send_key_to_webelement(locators['password'], credentials['password'])
    except Exception as ex:
        logger.error("Invalid login", ex)
        return False

    d.wait(0.5)
    try:
        # Нажатие кнопки входа
        d.execute_locator(locators['button'])
    except Exception as ex:
        logger.error("Invalid login", ex)
        return False

    return True
```