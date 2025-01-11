# Документация для `category.json`

## Обзор

Данный JSON-файл содержит конфигурацию локаторов для парсинга категорий, ссылок на продукты и пагинации на веб-сайте поставщика Etzmaleh.

## Оглавление

1. [Структура JSON](#структура-json)
2. [Параметр `pager`](#параметр-pager)
3. [Параметр `product_links`](#параметр-product_links)
4. [Параметр `categories_links`](#параметр-categories_links)

## Структура JSON

Файл состоит из трех основных разделов, каждый из которых описывает локаторы для конкретных элементов на странице:

-   `pager`: Описывает параметры для пагинации (переключения страниц).
-   `product_links`: Описывает локаторы для извлечения ссылок на продукты.
-   `categories_links`: Описывает локаторы для извлечения ссылок на категории.

## Параметр `pager`

### Описание

Параметр `pager` содержит настройки для определения способа пагинации на странице.

### Структура

```json
{
  "attribute": null,
  "by": "event",
  "selector": null,
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "scroll(5,'both')"
}
```

### Параметры

-   `attribute` (null): Атрибут не используется.
-   `by` (str): Метод определения локатора. В данном случае "event".
-   `selector` (null): Селектор не используется, так как используется `event`.
-   `if_list` (str): Указывает как обрабатывать список элементов - берется первый элемент.
-   `use_mouse` (bool): Указывает, нужно ли использовать мышь - не используется.
-   `mandatory` (bool): Указывает, является ли этот локатор обязательным - да.
-   `timeout` (int): Время ожидания (в секундах) - 0.
-  `timeout_for_event`(str): Тип ожидания события - `presence_of_element_located`.
-   `event` (str): Событие для пагинации, в данном случае прокрутка страницы на 5 пикселей по вертикали и горизонтали - `scroll(5,'both')`.

## Параметр `product_links`

### Описание

Параметр `product_links` содержит настройки для извлечения ссылок на продукты.

### Структура

```json
{
  "attribute": "href",
  "by": "XPATH",
  "selector": "//span[@data-component-type ='s-product-image']//a",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "timeout": 0,
   "timeout_for_event": "presence_of_element_located",
  "event": null
}
```

### Параметры

-   `attribute` (str): Атрибут, значение которого нужно извлечь - `"href"`.
-   `by` (str): Метод определения локатора - `"XPATH"`.
-   `selector` (str):  XPATH селектор для ссылок на продукты.
-   `if_list` (str): Указывает как обрабатывать список элементов - берется первый элемент.
-   `use_mouse` (bool): Указывает, нужно ли использовать мышь - не используется.
-   `mandatory` (bool): Указывает, является ли этот локатор обязательным - да.
-   `timeout` (int): Время ожидания (в секундах) - 0.
-   `timeout_for_event` (str): Тип ожидания события - `presence_of_element_located`.
-   `event` (null): Событие не используется.

## Параметр `categories_links`

### Описание

Параметр `categories_links` содержит настройки для извлечения ссылок на категории.

### Структура

```json
{
  "attribute": { "text": "href" },
  "by": "XPATH",
  "selector": "//a[contains(@class, 'menu-item')]",
  "timeout": 0,
   "timeout_for_event": "presence_of_element_located",
  "event": false,
  "mandatory": false,
  "locator_description": ""
}
```

### Параметры

-   `attribute` (dict): Атрибут, значение которого нужно извлечь, в данном случае текст ссылки и `href`.
-   `by` (str): Метод определения локатора - `"XPATH"`.
-   `selector` (str): XPATH селектор для ссылок на категории.
-   `timeout` (int): Время ожидания (в секундах) - 0.
-   `timeout_for_event` (str): Тип ожидания события - `presence_of_element_located`.
-   `event` (bool): Событие не используется - `false`.
-   `mandatory` (bool): Указывает, является ли этот локатор обязательным - нет.
-   `locator_description` (str): Описание локатора. В данном случае пустое.