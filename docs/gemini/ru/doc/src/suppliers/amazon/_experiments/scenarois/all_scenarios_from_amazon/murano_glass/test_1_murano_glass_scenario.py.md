# Модуль для тестирования сценария Murano Glass на Amazon

## Обзор

Модуль `test_1_murano_glass_scenario.py` предназначен для тестирования сценария приобретения муранского стекла (Murano Glass) на платформе Amazon. Он включает в себя функциональность для извлечения информации о продукте, проверки наличия товара в базе данных PrestaShop и загрузки изображений.

## Подробней

Этот модуль является частью более крупного проекта `hypotez` и служит для автоматизации процесса тестирования и сбора данных о товарах на Amazon. Он использует различные вспомогательные модули и классы, такие как `header`, `Product`, `Supplier` и `Driver`, для выполнения своих задач. Расположение модуля в структуре проекта указывает на его принадлежность к экспериментальным сценариям для Amazon, в частности, к категории муранского стекла.

## Функции

### `default_image_url`

**Назначение**: Получает URL первого дополнительного изображения товара.

```python
default_image_url = _(l['additional_images_urls'])[0]
```

**Как работает функция**:

1.  Извлекает список URL дополнительных изображений из локатора `l['additional_images_urls']` с помощью функции `_`.
2.  Берет первый URL из списка.

```
Извлечение URL дополнительных изображений из локатора
↓
Получение первого URL из списка
↓
default_image_url
```

**Примеры**:

```python
# Допустим, l['additional_images_urls'] содержит список URL: ['url1', 'url2', 'url3']
# Тогда default_image_url будет равен 'url1'
```

## Переменные

-   `supplier_prefix (str)`: Префикс поставщика, устанавливается как `'amazon'`.
-   `s (Supplier)`: Объект класса `Supplier`, инициализированный с использованием `start_supplier(supplier_prefix)`. Представляет поставщика Amazon.
-   `s.current_scenario (dict)`: Словарь, содержащий текущий сценарий для тестирования, включая URL, условие товара, категории PrestaShop и правило цены.
-   `l (dict)`: Локаторы элементов страницы продукта, полученные из `s.locators.get('product')`.
-   `d (Driver)`: Объект драйвера, используемый для управления браузером, `s.driver`.
-   `_ (Callable)`: Функция для выполнения локаторов через драйвер, `d.execute_locator`.
-   `ASIN (str)`: Идентификатор ASIN продукта, полученный с использованием локатора `l['ASIN']`.
-   `product_reference (str)`: Уникальная ссылка на продукт, формируется как `f"{s.supplier_id}-{ASIN}"`.
-   `product_id (Union[int, bool])`: ID продукта в базе данных PrestaShop, полученный через `Product.check_if_product_in_presta_db(product_reference)`. Если продукта нет в БД, то `False`.
-   `default_image_url (str)`: URL первого изображения продукта, полученный из `_(l['additional_images_urls'])[0]`.
-   `product_fields (ProductFields)`: Объект типа `ProductFields`, содержащий информацию о товаре, полученную с помощью `Product.grab_product_page(s)`.
-   `product_dict (dict)`: Словарь, содержащий информацию о продукте для добавления или обновления в PrestaShop.
-   `product_name (List[str])`: Имя продукта, полученное с помощью локатора `l['name']`.
-   `res_product_name (str)`: Отформатированное имя продукта, полученное путем объединения элементов из `product_name`.

## Код

```python
s.current_scenario: dict = {
    "url": "https://amzn.to/3OhRz2g",
    "condition": "new",
    "presta_categories": {
        "default_category": {"11209": "MURANO GLASS"},
        "additional_categories": [""]
    },
    "price_rule": 1
}
l = s.locators.get('product')
d = s.driver
_ = d.execute_locator

d.get_url(s.current_scenario['url'])

ASIN = _(l['ASIN'])

product_reference = f"{s.supplier_id}-{ASIN}"
product_id = Product.check_if_product_in_presta_db(product_reference)

default_image_url = _(l['additional_images_urls'])[0]

if not isinstance(product_id, bool):
    Product.upload_image2presta(image_url=default_image_url, product_id=product_id)
    ...
else:
    product_fields: ProductFields = Product.grab_product_page(s)

    product_dict: dict = {}
    product_dict['product']: dict = dict(product_fields.fields)
    product_name = _(l['name'])[0]

    res_product_name = ''
    for n in product_name:
        res_product_name += n
    product_dict['product']['name'] = res_product_name.strip("'").strip('"').strip('\n')
    pprint(product_dict)