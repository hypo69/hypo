# Модуль `login` для Amazon

## Обзор

Модуль `login.py` предназначен для автоматизации процесса авторизации на сайте Amazon с использованием веб-драйвера. Он содержит функцию `login`, которая принимает объект поставщика (`Supplier`) в качестве аргумента и выполняет шаги, необходимые для входа в систему.

## Подробней

Этот модуль является частью системы автоматизации для взаимодействия с Amazon. Он использует локаторы, хранящиеся в объекте поставщика, для определения элементов на веб-странице и выполнения действий, таких как ввод данных в поля и нажатие кнопок. Модуль также включает обработку ошибок и логирование для обеспечения стабильности и информативности процесса авторизации.

## Функции

### `login`

```python
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
```

**Описание**:
Функция `login` выполняет процесс авторизации на сайте Amazon.

**Как работает функция**:

1.  Извлекает локаторы для элементов страницы входа из `s.locators_store['login']`.
2.  Получает доступ к веб-драйверу через `s.driver`.
3.  Устанавливает фокус на окне браузера.
4.  Переходит по URL-адресу `https://amazon.com/`.
5.  Кликает на кнопку открытия полей ввода логина. Если не удается, обновляет страницу и пробует еще раз.
6.  Вводит email, пароль, устанавливает чекбокс "keep signed in" и нажимает кнопку подтверждения.
7.  Проверяет текущий URL, чтобы убедиться, что вход выполнен успешно.
8.  Логирует информацию об успешном или неудачном входе.

**Параметры**:

*   `s` (Supplier): Объект поставщика, содержащий информацию о драйвере и локаторах.

**Возвращает**:

*   `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Примеры**:

```python
# Пример вызова функции login
supplier = Supplier(...)  # инициализация объекта Supplier с необходимыми параметрами
success = login(supplier)
if success:
    print("Login successful")
else:
    print("Login failed")
```
```python
    _l : dict = s.locators_store[\'login\']
    _d = s.driver
    _d.window_focus()\n
```
*   `_l`: Локаторы для элементов страницы входа.
*   `_d`:  Веб-драйвер.
*  `_d.window_focus()`:  Устанавливает фокус на окне браузера.
```python
    _d.get_url(\'https://amazon.com/\')
```
*   `_d.get_url`:  Переходит по URL-адресу `https://amazon.com/`.
```python
   if not _d.click(_l[\'open_login_inputs\']):\n
        _d.refresh()\n
        _d.window_focus()\n
        if not _d.click(_l[\'open_login_inputs\']):\n
            \'\'\' Тут надо искать логин кнопку в другом месте \'\'\'\n
            logger.debug(\'\'\' Тут надо искать логин кнопку в другом месте \'\'\')
```
*   `_d.click(_l['open_login_inputs'])`: Кликает на кнопку открытия полей ввода логина. 
*   `_d.refresh()`: Обновляет страницу
*   `logger.debug`: Если клик не удался, то выводит сообщение в лог, что надо искать кнопку в другом месте

```python
   if not _d.execute_locator(_l[\'email_input\']): \n
        return
        ... # TODO логика обработки False
```
*   `_d.execute_locator(_l['email_input'])`: Вводит email
*   `return`: если не удалось ввести email, то завершает функцию
```python
  if not _d.execute_locator(_l[\'continue_button\']):\n
       ... # TODO логика обработки False
```
*   `_d.execute_locator(_l['continue_button'])`: Нажимает на кнопку `continue`
```python
   if not _d.execute_locator(_l[\'password_input\']): \n
        ... # TODO логика обработки False
```
*   `_d.execute_locator(_l['password_input'])`:  Вводит пароль
```python
    if not _d.execute_locator(_l[\'keep_signed_in_checkbox\']):\n
        ...
```
*   `_d.execute_locator(_l['keep_signed_in_checkbox'])`: Устанавливает чекбокс `keep signed in`
```python
  if not _d.execute_locator(_l[\'success_login_button\']):\n
       ... # TODO логика обработки False
```
*   `_d.execute_locator(_l['success_login_button'])`: Нажимает на кнопку `success_login_button`
```python
   if _d.current_url == "https://www.amazon.com/ap/signin":\n
        logger.error(f\'\'\' Неудачный логин \'\'\')\n
        ...\n
        return
```
*   `_d.current_url`:  Текущий URL страницы
*   `logger.error`:  Если текущий URL `https://www.amazon.com/ap/signin`, то выводит сообщение в лог, что логин не удался, и завершает функцию

```python
 _d.maximize_window()\n
    #_d.dump_cookies_to_file()\n
    logger.info(f\'\'\'Залогинился ... \'\'\')\n
    return True
```
*   `_d.maximize_window()`:  Разворачивает окно браузера
*   `logger.info`: Выводит сообщение в лог, что вход выполнен успешно, и возвращает `True`.
```python