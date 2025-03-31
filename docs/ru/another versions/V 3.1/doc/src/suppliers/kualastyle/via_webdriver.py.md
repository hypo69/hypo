# Модуль `via_webdriver`

## Обзор

Модуль `via_webdriver` предназначен для парсинга данных с сайта Kualastyle с использованием Selenium WebDriver. Он содержит функции для получения списка URL продуктов из заданной категории.

## Подробней

Этот модуль является частью пакета `src.suppliers.kualastyle` и используется для автоматизированного сбора данных о продуктах с сайта Kualastyle. Он использует WebDriver для навигации по сайту и извлечения необходимых данных.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str,str,None]:
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
```

**Описание**: Возвращает список URL продуктов со страницы категории.

**Параметры**:
- `s`: Объект поставщика (Supplier), содержащий драйвер WebDriver и локаторы элементов.

**Возвращает**:
- `list[str,str,None]`: Список URL продуктов или `None`, если список пуст.

**Примеры**:

```python
# Пример вызова функции
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from src.suppliers.kualastyle.kualastyle import Kualastyle
# supplier = Kualastyle()
# product_urls = get_list_products_in_category(supplier)
# if product_urls:
#     print(product_urls)
# else:
#     print("No products found in the category.")