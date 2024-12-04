# Модуль `hypotez/src/suppliers/kualastyle/via_webdriver.py`

## Обзор

Модуль `via_webdriver.py` предоставляет функции для работы с веб-драйвером для парсинга данных поставщика `kualastyle`.  Он содержит функции для получения списка ссылок на продукты в категории.

## Функции

### `get_list_products_in_category`

**Описание**: Функция возвращает список ссылок на продукты, находящиеся на странице категории.

**Параметры**:

- `s` (объект): Объект, представляющий поставщика (`Supplier`), содержащий драйвер браузера и локаторы элементов.

**Возвращает**:

- `list[str, str, None]`: Список кортежей, содержащий ссылки на продукты. Каждый кортеж имеет вид `(ссылка, название продукта, None)`. Возвращает `None` в случае ошибки.

**Обработка исключений**:

В функции не указаны потенциальные исключения. Добавьте обработку исключений, если они могут возникнуть при работе с веб-драйвером (например, `NoSuchElementException`, `TimeoutException`).
```python
def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    d = s.driver
    l: dict = s.locators.get('category')
    d.scroll(scroll_count = 10, direction = "forward")

    _ = d.execute_locator
    list_products_in_category = _(l['product_links'])
    #pprint(list_products_in_category)
    return list_products_in_category
```

**Примечания**:

- Код содержит неиспользуемый импорт `pprint`. Убедитесь, что он нужен, если вы его используете.
- Необходимо добавить обработку исключений (try...except), чтобы обработать потенциальные ошибки, возникающие при работе с веб-драйвером (например, `NoSuchElementException`).
- Необходимо определить тип возвращаемого значения (`list[str, str, None]`) как кортеж из трех элементов.  В текущей реализации это некорректно.
- Не хватает описания параметров `scroll_count` и `direction` в вызове `d.scroll()`.
- Необходимо указать, что функция `d.execute_locator` возвращает.  Возвращаемый тип должен быть уточнен.
- В коде есть `list_products_in_categoryy`, которая, по всей видимости, должна быть `list_products_in_category`.