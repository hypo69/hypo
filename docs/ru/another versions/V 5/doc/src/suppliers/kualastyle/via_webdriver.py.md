# Модуль `via_webdriver.py`

## Обзор

Модуль `via_webdriver.py` предназначен для парсинга данных с сайта Kualastyle с использованием Selenium WebDriver. Он содержит функции для извлечения списка URL продуктов из категорий.

## Подробней

Этот модуль является частью пакета `src.suppliers.kualastyle` и используется для автоматизации сбора информации о продуктах с сайта Kualastyle. Он использует Selenium WebDriver для взаимодействия с веб-страницами, прокрутки страниц и извлечения ссылок на продукты.

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

**Описание**: Извлекает список URL продуктов со страницы категории.

**Как работает функция**:
1. Получает объект `driver` из объекта поставщика `s`.
2. Получает локаторы для страницы категории из `s.locators.get('category')`.
3. Выполняет прокрутку страницы вниз для загрузки всех продуктов.
4. Извлекает список ссылок на продукты, используя локатор `product_links`.
5. Возвращает список URL продуктов.

**Параметры**:
- `s`: Объект поставщика (Suplier), содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list[str, str, None]`: Список URL продуктов или `None` в случае ошибки.

**Примеры**:

```python
# Пример вызова функции
# products = get_list_products_in_category(supplier_object)
# if products:
#     print(f"Найдено {len(products)} продуктов")
# else:
#     print("Продукты не найдены")
```