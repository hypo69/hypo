```markdown
# Модуль `hypotez/src/endpoints/advertisement/facebook/scenarios/login.py`

## Обзор

Этот модуль содержит сценарий для входа на Facebook. Он использует `Driver` для взаимодействия с веб-элементами, ввода логина и пароля, а затем нажатия кнопки входа.

## Оглавление

* [Функции](#функции)
    * [login](#login)


## Функции

### `login`

**Описание**: Выполняет вход на Facebook. Функция использует переданный `Driver` для выполнения авторизации на Facebook, заполняя логин и пароль, а затем нажимает кнопку входа.

**Параметры**:
- `d` (Driver): Экземпляр драйвера для взаимодействия с веб-элементами.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при вводе логина, пароля или нажатии кнопки.

**Детали**:

Эта функция использует локаторы из файла `login.json` для взаимодействия с веб-элементами Facebook. Если файл локаторов не загружен или содержит ошибки, функция логирует сообщение об ошибке и возвращает `False`.  В случае ошибки на любой из этапов (ввод логина, пароля, нажатие кнопки), функция логирует ошибку, используя `logger.error` и возвращает `False`.  Функция `d.wait` используется для ожидания загрузки элементов. Функция `credentials` получает данные для входа из глобального хранилища `gs.facebook_credentials`.

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
```