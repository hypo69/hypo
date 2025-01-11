# Модуль `scenario.py` для Amazon

## Обзор

Модуль `scenario.py` предназначен для сбора данных о товарах с сайта Amazon, используя веб-драйвер. Он включает в себя функциональность для извлечения списка категорий и товаров, а также обработки страниц товаров.

## Оглавление

1.  [Обзор](#обзор)
2.  [Функции](#функции)
    -   [`get_list_products_in_category`](#get_list_products_in_category)

## Функции

### `get_list_products_in_category`

**Описание**:
Возвращает список URL-адресов товаров со страницы категории. Если необходимо пролистывание страниц категорий, то пролистывает их.

**Параметры**:
- `s` (Supplier): Экземпляр поставщика (Supplier instance).

**Возвращает**:
- `list[str, str, None]`: Список URL-адресов товаров или `None`, если список не найден.

**Пример:**
```python
    list_products_in_category = get_list_products_in_category(supplier_instance)
    if list_products_in_category:
        for product_url in list_products_in_category:
            print(product_url)
```
**Обработка исключений:**
- `logger.error`: Если локаторы не найдены, выводится ошибка в лог.
- `logger.warning`: Если не найдены ссылки на товары, выводится предупреждение в лог.
```python
def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Если надо пролистстать - страницы категорий - листаю ??????

    Attrs:
    @param s: Supplier - Supplier intstance
    @returns list or one of products urls or None
    """
    d = s.driver
    l: dict = s.locators['category']
    if not l:
        """ Много проверок, потому, что код можно запускать от лица разных ихполнителей: Supplier, Product, Scenario """
        logger.error(f"А где локаторы? {l}")
        return
    d.scroll()

    #TODO: Нет листалки

    list_products_in_category = d.execute_locator(l['product_links'])
    """ Собираю ссылки на товары.  """
    if not list_products_in_category:
        logger.warning('Нет ссылок на товары')
        return
    
    list_products_in_category = [list_products_in_category] if isinstance(list_products_in_category, str) else list_products_in_category


    logger.info(f""" Найдено {len(list_products_in_category)} товаров """)
    
    #""" Проверяю наличие товара в базе данных магазина """
    #for asin in list_products_in_category:
    #    _asin = asin.split(f'''/''')[-2]
    #    _sku = f'''{s.supplier_id}_{_asin}''' 
    #    if PrestaShopProduct.check(_sku) == False:
    #        """ Синтаксис для того, чтобы помнить,
    #        что я проверяю ОТСУТСТВИЕ товара в базе данных
    #        """
    #        continue
    #    else:
    #        """ Товар в базе данных """
    #        continue
            #TODO: Логику 


    return list_products_in_category
```