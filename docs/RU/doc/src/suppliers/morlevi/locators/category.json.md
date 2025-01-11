# Локаторы категорий Morlevi

## Обзор

Данный файл содержит JSON-конфигурацию локаторов для извлечения ссылок на товары из категорий на сайте Morlevi.

## Содержание

- [Локаторы](#locators)
    - [`product_links`](#product_links)

## Локаторы

### `product_links`

**Описание**: Локатор для извлечения ссылок на товары.

**Параметры**:
- `attribute` (str): Атрибут элемента, содержащий ссылку на товар.
- `by` (str): Метод поиска элемента.
- `selector` (str): CSS селектор для поиска элемента.
- `if_list` (str): Определение как обрабатывать список результатов.
- `use_mouse` (bool): Использовать ли мышь для поиска элемента.
- `mandatory` (bool): Является ли элемент обязательным для поиска.
- `timeout` (int): Время ожидания элемента в секундах.
- `timeout_for_event` (str): Событие для ожидания.
- `event` (str | None): Событие.

**Значение**
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