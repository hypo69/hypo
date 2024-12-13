# Документация для `category.json`

## Обзор

Файл `category.json` содержит JSON-конфигурацию для извлечения ссылок на товары на странице категории.

## Содержание

1.  [Обзор](#обзор)
2.  [Структура JSON](#структура-json)
    -   [product_links](#product_links)

## Структура JSON

### `product_links`

**Описание**: Объект `product_links` содержит конфигурацию для извлечения ссылок на товары.

**Параметры**:

-   `attribute` (str): Атрибут, который нужно извлечь из элемента. В данном случае это `"href"`.
-   `by` (str): Метод поиска элемента. В данном случае это `"XPATH"`.
-   `selector` (str): XPath-селектор для поиска элементов. В данном случае это `//span[@data-component-type ='s-product-image']//a`.
-   `if_list` (str): Определяет, как обрабатывать список элементов. В данном случае берется первый элемент `"first"`.
-   `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом. В данном случае `false`.
-   `mandatory` (bool): Указывает, является ли элемент обязательным для поиска. В данном случае `true`.
-  `timeout` (int): Таймаут ожидания элемента, по умолчанию 0.
-   `timeout_for_event` (str): Таймаут ожидания события, `"presence_of_element_located"`
-   `event` (str | None): Событие, которое нужно ожидать (не используется, `null`).

**Пример**:

```json
{
  "product_links": {
    "attribute": "href",
    "by": "XPATH",
    "selector": "//span[@data-component-type ='s-product-image']//a",
    "if_list":"first",
     "use_mouse": false, 
     "mandatory": true,
     "timeout":0,
     "timeout_for_event":"presence_of_element_located",
     "event": null
  }
}
```