# Модуль `get_graber_by_supplier`

## Обзор

Модуль `get_graber_by_supplier.py` предназначен для получения объекта граббера на основе URL-адреса поставщика.
Каждый поставщик имеет свой собственный граббер, который извлекает значения полей из целевой HTML-страницы.

## Оглавление
1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`get_graber_by_supplier_url`](#get_graber_by_supplier_url)

## Функции

### `get_graber_by_supplier_url`

**Описание**: Функция возвращает соответствующий граббер для заданного URL-адреса поставщика.

**Параметры**:
- `self`: Экземпляр класса, в котором вызывается функция.
- `url` (str): URL-адрес страницы поставщика.

**Возвращает**:
- `Graber | None`: Экземпляр граббера, если соответствие найдено, иначе `None`.

**Пример использования:**
```python
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.webdriver import WebDriver

driver = WebDriver()
url = 'https://www.example.com'
graber = get_graber_by_supplier_url(driver, url)

if graber:
    # Использовать граббер для извлечения данных
    pass
else:
    # Обработать ситуацию, когда граббер не найден
    pass
```