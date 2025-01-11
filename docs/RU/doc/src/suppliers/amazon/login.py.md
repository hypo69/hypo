# Модуль `login` для Amazon

## Обзор

Модуль `login.py` содержит реализацию функции авторизации для поставщика Amazon с использованием веб-драйвера. Он обрабатывает вход на сайт Amazon, заполняет поля ввода электронной почты и пароля, а также нажимает необходимые кнопки для завершения процесса авторизации.

## Содержание

- [Функции](#Функции)
    - [`login`](#login)

## Функции

### `login`

**Описание**: Функция выполняет авторизацию на сайте Amazon.

**Параметры**:
- `s` (object): Объект поставщика (`Supplier`), содержащий данные для авторизации, такие как локаторы и драйвер.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, в противном случае - `None`.

**Вызывает исключения**:
- Нет явных исключений, но при некорректной работе драйвера могут возникнуть исключения.

```python
def login(s) -> bool:
    """ Функция логин. 
    Args:
        s (object): Supplier.
    Returns:
        bool: True if login else False
    """
    _l : dict = s.locators_store['login']
    _d = s.driver
    _d.window_focus()
    _d.get_url('https://amazon.com/')
    if not _d.click(_l['open_login_inputs']):
        _d.refresh()
        _d.window_focus()
        if not _d.click(_l['open_login_inputs']):
            logger.debug(' Тут надо искать логин кнопку в другом месте ')
        ...
    if not _d.execute_locator(_l['email_input']): 
        return
        ... # TODO логика обработки False

    _d.wait(.7)
    if not _d.execute_locator(_l['continue_button']):
       ... # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['password_input']): 
        ... # TODO логика обработки False
    _d.wait(.7)
    if not _d.execute_locator(_l['keep_signed_in_checkbox']):
        ...
    _d.wait(.7)
    if not _d.execute_locator(_l['success_login_button']):
       ... # TODO логика обработки False
    if _d.current_url == "https://www.amazon.com/ap/signin":
        logger.error(f' Неудачный логин ')
        ...
        return
    _d.wait(1.7)
    _d.maximize_window()
    logger.info(f'Залогинился ... ')
    return True
```