# Модуль `get_graber_by_supplier`

## Обзор

Этот модуль предоставляет функциональность для получения объекта граббера на основе URL-адреса поставщика. Каждый поставщик имеет свой собственный граббер, который извлекает значения полей из целевой HTML-страницы.

## Оглавление

- [Функции](#функции)
    - [`get_graber_by_supplier_url`](#get_graber_by_supplier_url)

## Функции

### `get_graber_by_supplier_url`

**Описание**: Функция, которая возвращает соответствующий граббер для заданного URL-адреса поставщика.

**Параметры**:
- `self`: Экземпляр класса, содержащий `driver`.
- `url` (str): URL-адрес страницы поставщика.

**Возвращает**:
- `Graber | None`: Экземпляр граббера, если найдено совпадение, иначе `None`.

**Пример использования**:

```python
from src.suppliers.get_graber_by_supplier import get_graber_by_supplier_url
from src.webdriver import WebDriver

driver = WebDriver()
url = 'https://www.example.com'
graber = get_graber_by_supplier_url(driver, url)

if graber:
    # Используйте граббер для извлечения данных
    pass
else:
    # Обработайте случай, когда граббер не найден
    pass
```