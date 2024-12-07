# Модуль hypotez/src/suppliers/kualastyle/login.py

## Обзор

Этот модуль содержит функции для авторизации поставщика Kualastyle.  Он включает в себя логику входа и закрытия всплывающих окон.

## Оглавление

* [Функции](#функции)


## Функции

### `login`

**Описание**: Функция для входа поставщика.

**Параметры**:

- `s` (Supplier): Объект, представляющий поставщика.

**Возвращает**:

- `bool`: `True`, если вход успешен, `False` иначе.

**Вызывает исключения**:
- Нет


### `close_pop_up`

**Описание**: Функция для закрытия всплывающих окон.

**Параметры**:

- `s` (Supplier): Объект, представляющий поставщика.

**Возвращает**:

- `bool`: `True`, если окно закрыто, `False` иначе.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке выполнения действия по закрытию всплывающего окна.  В лог записывается сообщение об ошибке.

```
```python
from src.logger import logger

def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
    close_pop_up(s)
    return True 

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