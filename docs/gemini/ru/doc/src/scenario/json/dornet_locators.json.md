# Локаторы Dornet

## Обзор

Этот JSON-файл содержит определения локаторов для веб-элементов на сайте dornet.ru. Локаторы используются для автоматизации взаимодействия с веб-страницами, включая навигацию по категориям, извлечение информации о продуктах и проверку наличия товаров.

## Оглавление

- [Категории](#категории)
- [Продукты](#продукты)
- [Поля продукта](#поля-продукта)
- [Наличие на складе](#наличие-на-складе)
- [Статус "Нет в наличии"](#статус-нет-в-наличии)

## Категории

### `pages_listing_locator`
**Описание**: Локатор для кнопки или ссылки "следующая страница" при просмотре списка товаров в категории.

**Параметры**:
 - `attribute` (str): Атрибут, который нужно получить (`href`).
 - `by` (str): Метод поиска (`css selector`).
 - `selector` (str): CSS-селектор для поиска элемента (`li.next-page a`).
 - `timeout` (int): Тайм-аут ожидания элемента.
 - `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
 - `event` (None): Событие, которое нужно отслеживать.

## Продукты

### `product_block_locator`
**Описание**: Локатор для блока, содержащего информацию о продукте.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div.boxItem-wrap`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `link_to_product_locator`
**Описание**: Локатор для ссылки, ведущей на страницу продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`href`).
- `by` (str): Метод поиска (`XPATH`).
- `selector` (str): XPATH-селектор для поиска элемента (`//a[@class='str-item-card__property-title']`).
-   `timeout` (int): Тайм-аут ожидания элемента.
-   `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

## Поля продукта

### `product_name_locator`
**Описание**: Локатор для названия продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div[class=product-name] h1[itemprop='name']`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `brand_locator`
**Описание**: Локатор для названия бренда продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`.brands`).
-   `timeout` (int): Тайм-аут ожидания элемента.
-   `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `sku_locator`
**Описание**: Локатор для артикула продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div[class=sku] span[itemprop='sku']`).
-   `timeout` (int): Тайм-аут ожидания элемента.
-   `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.
### `brand_sku_locator`
**Описание**: Локатор для артикула бренда.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div[class=sku] span[itemprop='sku']`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `summary_locator`
**Описание**: Локатор для краткого описания продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div[class=product-name] h1[itemprop='name']`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `description_locator`
**Описание**: Локатор для полного описания продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`.data-table[role='presentation']`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `images_locator`
**Описание**: Локатор для изображений продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`src`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`.cloudzoom`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

### `price_locator`
**Описание**: Локатор для цены продукта.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`div span[itemprop='price']`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

## Наличие на складе

### `stock_locator`
**Описание**: Локатор для статуса наличия товара на складе.
**Параметры**:
- `attribute` (str): Атрибут, который нужно получить (`innerHTML`).
- `by` (str): Метод поиска (`css selector`).
- `selector` (str): CSS-селектор для поиска элемента (`.value.stock_staus`).
-  `timeout` (int): Тайм-аут ожидания элемента.
-  `timeout_for_event` (str): Событие для ожидания (`presence_of_element_located`).
- `event` (None): Событие, которое нужно отслеживать.

## Статус "Нет в наличии"

### `not in stock`
**Описание**: Список значений, которые указывают, что товара нет в наличии.
**Значения**:
- `color:red`: CSS цвет для определения статуса "нет в наличии".
- `color:#d19b00`: CSS цвет для определения статуса "нет в наличии".