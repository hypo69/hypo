# Модуль hypotez/src/suppliers/hb/login.py

## Обзор

Этот модуль содержит функции для авторизации поставщика (HB).

## Функции

### `login`

**Описание**: Функция логина поставщика.

**Параметры**:

- `s` (Supplier): Объект поставщика.

**Возвращает**:

- `bool`: `True`, если логин успешен, `False` - иначе.

**Вызывает исключения**:

- Нет описанных исключений.


```python
from src.logger.logger import logger

def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
    return True
```