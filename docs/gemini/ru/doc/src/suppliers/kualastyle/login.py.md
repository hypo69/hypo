# Модуль для авторизации поставщика Kualastyle

## Обзор

Модуль `login.py` предназначен для автоматизации процесса авторизации поставщика на сайте Kualastyle. Он содержит функции для входа в систему и закрытия всплывающих окон.

## Подробней

Этот модуль является частью проекта `hypotez` и отвечает за автоматизацию входа в систему поставщика Kualastyle. Он использует драйвер веб-браузера для взаимодействия с веб-сайтом, выполняет необходимые действия для авторизации и обрабатывает возможные всплывающие окна.

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

**Назначение**: Осуществляет вход в систему поставщика.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий необходимую информацию для входа в систему, такую как драйвер веб-браузера и локаторы элементов.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, иначе `False`.

**Как работает функция**:

1. Вызывает функцию `close_pop_up(s)` для закрытия возможных всплывающих окон.
2. Возвращает `True`, предполагая, что вход выполнен успешно.

```
login
|
-- close_pop_up(s)
|
return True
```

**Примеры**:

```python
# Пример вызова функции login
# from src.suppliers.kualastyle.login import login
# from src.suppliers.supplier import Supplier
# supplier = Supplier()
# result = login(supplier)
# print(f"Вход выполнен: {result}")
```

### `close_pop_up`

```python
def close_pop_up(s) -> bool:
    """ Функция логин
   @param
        s - Supplier
    @returns
        True if login else False

   """
```

**Назначение**: Закрывает всплывающее окно на сайте Kualastyle.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий драйвер веб-браузера и локаторы элементов.

**Возвращает**:
- `bool`: `True`, если всплывающее окно закрыто успешно, иначе `False`.

**Как работает функция**:

1. Извлекает драйвер веб-браузера (`_d`) из объекта поставщика (`s`).
2. Извлекает локатор (`_l`) для кнопки закрытия всплывающего окна из локаторов поставщика.
3. Переходит по URL-адресу `https://www.kualastyle.com` с помощью `_d.get_url`.
4. Переводит фокус в окно браузера.
5. Ожидает 5 секунд.
6. Пытается выполнить локатор (`_l`) для закрытия всплывающего окна с помощью `_d.execute_locator(_l)`.
7. Если возникает исключение, регистрирует предупреждение с помощью `logger.warning(f"Не закрыл попап")`.

```
close_pop_up
|
-- _d = s.driver
|
-- _l : dict = s.locators['close_pop_up_locator']
|
-- _d.get_url('https://www.kualastyle.com')
|
-- _d.window_focus(_d)
|
-- _d.wait(5)
|
-- try: _d.execute_locator(_l)
|
-- except Exception as e: logger.warning(f"Не закрыл попап")
|
...
```

**Примеры**:

```python
# Пример вызова функции close_pop_up
# from src.suppliers.kualastyle.login import close_pop_up
# from src.suppliers.supplier import Supplier
# supplier = Supplier()
# result = close_pop_up(supplier)
# print(f"Попап закрыт: {result}")