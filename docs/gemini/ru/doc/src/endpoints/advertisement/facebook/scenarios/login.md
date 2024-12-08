# Модуль hypotez/src/endpoints/advertisement/facebook/scenarios/login.py

## Обзор

Данный модуль содержит сценарий для входа на Facebook.  Он предоставляет функцию `login`, которая использует экземпляр `Driver` для взаимодействия с веб-элементами и авторизации пользователя.

## Локаторы

Локаторы для элементов страницы Facebook загружаются из файла `login.json` в папке `locators`.  Если файл не найден или произошла ошибка при его загрузке, выводится соответствующее сообщение в лог.

## Функции

### `login`

**Описание**:  Выполняет вход на Facebook.  Функция использует переданный `Driver` для выполнения авторизации, заполняя поля логина и пароля, а затем нажимает кнопку входа.

**Параметры**:

- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

**Возвращает**:

- `bool`: `True`, если авторизация прошла успешно, иначе `False`.

**Возможные исключения**:

- `Exception`: Возникает при ошибках при вводе логина, пароля или нажатии кнопки входа.  Подробная информация о причине ошибки логгируется с помощью `logger`.


```
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