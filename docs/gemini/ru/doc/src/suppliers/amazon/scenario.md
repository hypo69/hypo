# Модуль `hypotez/src/suppliers/amazon/scenario.py`

## Обзор

Этот модуль предоставляет сценарий обработки категорий товаров для поставщика Amazon. Он отвечает за сбор списка категорий, товаров в категории и извлечение данных о товарах.

## Константы

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev', 'prod').

**Значение**: 'dev' по умолчанию.


## Функции

### `get_list_products_in_category`

**Описание**: Функция собирает список ссылок на товары на странице категории.

**Параметры**:

- `s` (Supplier): Экземпляр класса `Supplier` (предполагается, что `Supplier` содержит необходимые данные и драйвер).

**Возвращает**:

- `list[str,str,None]`: Список ссылок на товары. Возвращает `None` в случае ошибки.

**Вызывает исключения**:

- Возможные исключения, связанные с взаимодействием с веб-драйвером (например, `NoSuchElementException`, `TimeoutException`).

**Детали**:
Функция получает веб-драйвер и локаторы из экземпляра `s`.  Производит скроллинг страницы для загрузки всех товаров. Извлекает ссылки на товары из локаторов. Возвращает список ссылок на товары или `None`, если ссылки не найдены или произошла ошибка.  В текущем виде функция не обрабатывает случаи пагинации страниц категорий. Также отсутствует логика проверки наличия товара в базе данных.
```
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
    #    _asin = asin.split(f'//')[-2]
    #    _sku = f'{s.supplier_id}_{_asin}'
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
## Заметки

- Необходимо реализовать обработку пагинации страниц категорий.
- Необходимо добавить проверку на изменение категорий на страницах продавца.
- Требуется реализовать логику проверки наличия товара в базе данных.
- Необходимо учесть различные типы возвращаемых значений и добавить проверки типов.