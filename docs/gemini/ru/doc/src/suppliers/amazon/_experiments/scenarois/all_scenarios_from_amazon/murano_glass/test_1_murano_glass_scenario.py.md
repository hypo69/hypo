# Модуль `test_1_murano_glass_scenario.py`

## Обзор

Модуль предназначен для автоматизации процесса сбора данных о товарах с сайта Amazon (в частности, о муранском стекле) и загрузки этих данных в базу данных PrestaShop. Он включает в себя функции для извлечения информации о товаре, проверки наличия товара в базе данных, загрузки изображений и создания/обновления информации о товаре в PrestaShop.

## Подробнее

Модуль является частью более крупного проекта `hypotez` и используется для автоматизации процесса обновления каталога товаров в интернет-магазине PrestaShop на основе данных, полученных с Amazon. Он предназначен для работы с товарами категории "муранское стекло". 

Модуль выполняет следующие основные шаги:

1.  Инициализация поставщика (Amazon).
2.  Переход на страницу товара на Amazon.
3.  Извлечение основных данных о товаре, таких как ASIN, название, изображения и т.д.
4.  Проверка наличия товара в базе данных PrestaShop по артикулу.
5.  Если товар уже существует в базе данных, обновление информации о товаре и загрузка новых изображений.
6.  Если товар отсутствует в базе данных, создание новой записи о товаре в PrestaShop.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str) -> Supplier:
    """
    Инициализирует поставщика.

    Args:
        supplier_prefix (str): Префикс поставщика.

    Returns:
        Supplier: Объект поставщика.
    """
```

**Назначение**: Инициализирует поставщика на основе переданного префикса. В данном коде префикс поставщика - `amazon`.

**Параметры**:

*   `supplier_prefix` (str): Префикс поставщика, указывающий на конкретного поставщика (в данном случае, 'amazon').

**Возвращает**:

*   `Supplier`: Объект поставщика, созданный на основе префикса.

**Как работает функция**:

1.  Функция `start_supplier` принимает строковый аргумент `supplier_prefix`.
2.  Она использует этот префикс для инициализации и возврата объекта класса `Supplier`.
3.  В данном контексте `s = start_supplier(supplier_prefix)` создает экземпляр класса `Supplier` для работы с Amazon.

**ASCII flowchart**:

```
    start_supplier(supplier_prefix)
    ↓
    Инициализация объекта Supplier с префиксом
    ↓
    Возврат объекта Supplier
```

**Примеры**:

```python
supplier_prefix = 'amazon'
s = start_supplier(supplier_prefix)
print(type(s))  # Вывод: <class 'header.Supplier'>
```

## Переменные

### `supplier_prefix`

```python
supplier_prefix = 'amazon'
```

**Описание**: Префикс поставщика, используемый для инициализации объекта `Supplier`. В данном случае, указывает на Amazon.

### `s`

```python
s = start_supplier(supplier_prefix)
```

**Описание**: Экземпляр класса `Supplier`, представляющий поставщика Amazon.

### `s.current_scenario`

```python
s.current_scenario: dict = {
  "url": "https://amzn.to/3OhRz2g",
  "condition": "new",
  "presta_categories": {
    "default_category": { "11209": "MURANO GLASS" },
    "additional_categories": [ "" ]
  },
  "price_rule": 1
}
```

**Описание**: Словарь, содержащий информацию о текущем сценарии, включая URL товара, состояние (новое), категории PrestaShop и правило цены.

### `l`

```python
l = s.locators.get('product')
```

**Описание**: Локаторы элементов страницы товара, полученные из объекта `Supplier`. Используются для поиска элементов на странице Amazon.

### `d`

```python
d = s.driver
```

**Описание**: Драйвер веб-браузера, используемый для взаимодействия с веб-страницей.

### `_`

```python
_ = d.execute_locator
```

**Описание**: Сокращенная ссылка на метод `execute_locator` драйвера, используемая для упрощения вызова локаторов.

### `ASIN`

```python
ASIN = _(l['ASIN'])
```

**Описание**: Идентификатор ASIN товара, извлеченный с помощью локатора 'ASIN'.

### `product_reference`

```python
product_reference = f"{s.supplier_id}-{ASIN}"
```

**Описание**: Уникальный артикул товара, сформированный на основе идентификатора поставщика и ASIN товара.

### `product_id`

```python
product_id = Product.check_if_product_in_presta_db(product_reference)
```

**Описание**: Идентификатор товара в базе данных PrestaShop, полученный путем проверки наличия товара по артикулу. Если товар отсутствует, значение будет `False`.

### `default_image_url`

```python
default_image_url = _(l['additional_images_urls'])[0]
```

**Описание**: URL первого изображения товара, извлеченного с помощью локатора 'additional\_images\_urls'.

### `product_fields`

```python
product_fields: ProductFields = Product.grab_product_page(s)
```

**Описание**: Объект `ProductFields`, содержащий извлеченные данные о товаре со страницы товара.

### `product_dict`

```python
product_dict: dict = {}
product_dict['product']: dict = dict(product_fields.fields)
```

**Описание**: Словарь, содержащий информацию о товаре, подготовленную для загрузки в PrestaShop.

### `product_name`

```python
product_name = _(l['name'])[0]
```

**Описание**: Название товара, извлеченное с помощью локатора 'name'.

### `res_product_name`

```python
res_product_name = ''
for n in product_name:
    res_product_name += n
product_dict['product']['name'] = res_product_name.strip("\'").strip('\"').strip('\\n')
```

**Описание**: Очищенное название товара, полученное путем удаления лишних символов (кавычек и переносов строк).