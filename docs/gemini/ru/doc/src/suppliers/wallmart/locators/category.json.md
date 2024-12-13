# Документация для `hypotez/src/suppliers/wallmart/locators/category.json`

## Обзор

Данный файл содержит JSON-конфигурацию для локаторов элементов на странице категории товаров Walmart. Он определяет, как находить ссылки на товары, используя XPath и атрибуты элементов.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
    - [`product_links`](#product_links)

## Структура JSON

### `product_links`

**Описание**: Конфигурация локатора для извлечения ссылок на товары на странице категории.

**Структура**:
   - `attribute` (str): Атрибут, из которого извлекается значение (в данном случае, "href").
   - `by` (str): Метод поиска элемента (в данном случае, "XPATH").
   - `selector` (str): XPath-выражение для поиска элементов.
   - `if_list` (str): Указывает, что нужно извлечь первый элемент из списка найденных (значение "first").
   - `use_mouse` (bool): Указывает, нужно ли использовать мышь для взаимодействия с элементом (в данном случае, `false`).
   - `mandatory` (bool): Указывает, является ли наличие элемента обязательным (в данном случае, `true`).
   - `timeout` (int): Максимальное время ожидания в секундах.
   - `timeout_for_event` (str): Тип события ожидания.
   - `event` (Optional[str]): Название события.
    
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