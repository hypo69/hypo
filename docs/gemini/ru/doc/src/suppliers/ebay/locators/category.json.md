# Документация для `category.json`

## Обзор

Файл `category.json` содержит JSON-объект, который определяет локаторы для извлечения ссылок на товары на страницах категорий eBay.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [product_links](#product_links)
    
## Структура JSON

### `product_links`
**Описание**:  Словарь, содержащий информацию о локаторах для извлечения ссылок на товары.

**Структура**:
  - **`attribute`** (str): Атрибут, из которого нужно извлечь данные (в данном случае 'href').
  - **`by`** (str): Метод поиска элемента (в данном случае 'XPATH').
  - **`selector`** (str): Строка XPATH-селектора, определяющая местоположение элемента.
  - **`if_list`** (str): Указывает, как обрабатывать список элементов (в данном случае 'first', выбирается первый элемент).
  - **`use_mouse`** (bool):  Указывает, нужно ли использовать мышь для взаимодействия (в данном случае `false`).
  - **`mandatory`** (bool): Указывает, является ли извлечение этого элемента обязательным (в данном случае `true`).
  - **`timeout`** (int): Время ожидания при поиске элемента (в данном случае `0`).
  - **`timeout_for_event`** (str): Тип события для ожидания (в данном случае 'presence_of_element_located').
  - **`event`** (None): Событие для ожидания (в данном случае `null`).
  
  
   
**Пример:**
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