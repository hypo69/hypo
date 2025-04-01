# Модуль `login` для поставщика `kualastyle`

## Обзор

Модуль `login` содержит функции для авторизации поставщика `kualastyle` на веб-сайте. Он предоставляет функции для входа в систему и закрытия всплывающих окон, которые могут появляться на сайте.

## Подробней

Этот модуль предназначен для автоматизации процесса входа в систему на веб-сайте `kualastyle.com`. Он использует Selenium WebDriver для управления браузером и выполнения действий, необходимых для входа в систему. Модуль включает функции для обработки всплывающих окон, которые могут мешать процессу входа в систему.

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
    close_pop_up(s)
    return True
```

**Описание**:
Функция `login` выполняет вход пользователя в систему. В текущей реализации она вызывает функцию `close_pop_up` и возвращает `True`.

**Как работает функция**:

1.  Вызывает функцию `close_pop_up(s)` для закрытия всплывающих окон.
2.  Возвращает `True`, что означает успешное выполнение входа в систему (в текущей реализации).

**Параметры**:

*   `s`: Объект `Supplier`, содержащий информацию о поставщике и драйвер Selenium.

**Возвращает**:

*   `bool`: `True`, если вход выполнен успешно (в текущей реализации).

**Примеры**:

```python
# Пример вызова функции login
# from src.suppliers.kualastyle.login import login
# from src.suppliers.kualastyle.supplier import Supplier
# supplier = Supplier(driver=webdriver.Chrome(), locators={})  # Инициализация объекта Supplier (упрощенно)
# result = login(supplier)
# print(result)  # Вывод: True
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
    _d = s.driver
    _l : dict = s.locators['close_pop_up_locator']
    
    _d.get_url('https://www.kualastyle.com')
    _d.window_focus(_d)
    _d.wait(5)
    #_d.page_refresh()
    try:
        _d.execute_locator(_l)
    except Exception as ex:
        logger.warning(f"Не закрыл попап")
    
    ...
```

**Описание**:
Функция `close_pop_up` пытается закрыть всплывающее окно на веб-сайте.

**Как работает функция**:

1.  Извлекает драйвер Selenium (`_d`) и локаторы (`_l`) из объекта `Supplier`.
2.  Переходит на главную страницу веб-сайта `kualastyle.com`.
3.  Устанавливает фокус на текущее окно браузера.
4.  Ожидает 5 секунд.
5.  Пытается выполнить локатор для закрытия всплывающего окна.
6.  Если возникает исключение, регистрирует предупреждение в лог.

**Параметры**:

*   `s`: Объект `Supplier`, содержащий информацию о поставщике, драйвер Selenium и локаторы.

**Возвращает**:

*   `bool`: `True`, если вход выполнен успешно (в текущей реализации).

**Вызывает исключения**:

*   `Exception`: Если возникает ошибка при закрытии всплывающего окна, исключение перехватывается и логируется.

**Примеры**:

```python
# from src.suppliers.kualastyle.login import close_pop_up
# from src.suppliers.kualastyle.supplier import Supplier
# from selenium import webdriver
# # Инициализация объекта Supplier (упрощенно)
# supplier = Supplier(driver=webdriver.Chrome(), locators={'close_pop_up_locator': 'locator'})
# result = close_pop_up(supplier)