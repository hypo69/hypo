# Модуль `hypotez/src/suppliers/kualastyle/login.py`

## Обзор

Этот модуль содержит функции для авторизации поставщика `Kualastyle`.  Он включает в себя функции `login` и `close_pop_up` для обработки процесса входа и закрытия всплывающих окон.

## Оглавление

* [Функции](#функции)


## Функции

### `login`

**Описание**: Функция осуществляет вход в систему поставщика `Kualastyle`.

**Параметры**:

- `s` (объект): Объект, представляющий поставщика (`Supplier`).

**Возвращает**:

- `bool`: `True`, если вход успешен, `False` - в противном случае.

**Вызывает исключения**:

-  (Возможные исключения, если таковые есть).


### `close_pop_up`

**Описание**: Функция закрывает всплывающие окна при входе.

**Параметры**:

- `s` (объект): Объект, представляющий поставщика (`Supplier`).

**Возвращает**:

- `bool`: `True`, если окно закрыто, `False` - в противном случае.

**Вызывает исключения**:

- `Exception`:  В случае возникновения ошибки при взаимодействии с браузером.  В лог записывается сообщение о том, что попап не закрыт.


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
    except Exception as e:
        logger.warning(f"Не закрыл попап")
    
    ...