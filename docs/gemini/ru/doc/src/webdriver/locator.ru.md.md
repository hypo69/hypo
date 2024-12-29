# Локаторы и их взаимодействие с `executor`

## Обзор

Этот документ описывает структуру и использование локаторов для взаимодействия с веб-элементами в контексте автоматизации веб-тестов. Локаторы представляют собой конфигурационные объекты, определяющие, как находить и взаимодействовать с элементами на веб-странице. Они используются вместе с классом `ExecuteLocator` для выполнения различных действий, таких как клики, ввод текста, извлечение атрибутов и т.д.

## Содержание

- [Обзор](#обзор)
- [Примеры локаторов](#примеры-локаторов)
    - [1. `close_banner`](#1-close_banner)
    - [2. `id_manufacturer`](#2-id_manufacturer)
    - [3. `additional_images_urls`](#3-additional_images_urls)
    - [4. `default_image_url`](#4-default_image_url)
    - [5. `id_supplier`](#5-id_supplier)
- [Взаимодействие с `executor`](#взаимодействие-с-executor)

## Примеры локаторов

### 1. `close_banner`

```json
"close_banner": {
  "attribute": null,
  "by": "XPATH",
  "selector": "//button[@id = 'closeXButton']",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "click()",
  "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
}
```

**Описание**: Локатор для закрытия всплывающего окна (баннера).

**Ключи**:

- `attribute`: Не используется в данном случае (`null`).
- `by`: Тип локатора (`XPATH`).
- `selector`:  Выражение для поиска элемента `//button[@id = 'closeXButton']`.
- `if_list`:  Указывает, что если найдено несколько элементов, то использовать первый из них (`first`).
- `use_mouse`: Указывает, что не нужно использовать мышь (`false`).
- `mandatory`: Указывает, что действие не является обязательным (`false`).
- `timeout`: Тайм-аут для поиска элемента (`0`).
- `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
- `event`: Событие, которое нужно выполнить (`click()`).
- `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:
- `executor` находит элемент по XPATH.
- `executor` выполняет клик по найденному элементу.
- Если элемент не найден, `executor` продолжит выполнение, так как `mandatory` установлен в `false`.

### 2. `id_manufacturer`

```json
"id_manufacturer": {
  "attribute": 11290,
  "by": "VALUE",
  "selector": null,
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": null,
  "locator_description": "id_manufacturer"
}
```

**Описание**: Локатор для получения значения идентификатора производителя.

**Ключи**:

- `attribute`: Значение атрибута (`11290`).
- `by`: Тип локатора (`VALUE`).
- `selector`: Не используется в данном случае (`null`).
- `if_list`: Указывает, что если найдено несколько элементов, то использовать первый из них (`first`).
- `use_mouse`: Указывает, что не нужно использовать мышь (`false`).
- `mandatory`: Указывает, что действие является обязательным (`true`).
- `timeout`: Тайм-аут для поиска элемента (`0`).
- `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
- `event`: Нет события (`null`).
- `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:
- `executor` вернет значение, установленное в `attribute` (`11290`).
- Так как `by` установлен в `VALUE`, `executor` не будет искать элемент на странице.

### 3. `additional_images_urls`

```json
"additional_images_urls": {
  "attribute": "src",
  "by": "XPATH",
  "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": null
}
```

**Описание**: Локатор для извлечения URL-адресов дополнительных изображений.

**Ключи**:

- `attribute`: Атрибут, который нужно извлечь (`src`).
- `by`: Тип локатора (`XPATH`).
- `selector`: Выражение для поиска элемента `//ol[contains(@class, 'flex-control-thumbs')]//img`.
- `if_list`: Указывает, что если найдено несколько элементов, то использовать первый из них (`first`).
- `use_mouse`: Указывает, что не нужно использовать мышь (`false`).
- `mandatory`: Указывает, что действие не является обязательным (`false`).
- `timeout`: Тайм-аут для поиска элемента (`0`).
- `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
- `event`: Нет события (`null`).

**Взаимодействие с `executor`**:
- `executor` находит все элементы по XPATH.
- `executor` извлекает атрибут `src` для каждого найденного элемента.
- Если элементы не найдены, `executor` продолжит выполнение, так как `mandatory` установлен в `false`.

### 4. `default_image_url`

```json
"default_image_url": {
  "attribute": null,
  "by": "XPATH",
  "selector": "//a[@id = 'mainpic']//img",
  "if_list": "first",
  "use_mouse": false,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": "screenshot()",
  "mandatory": true,
  "locator_description": "Внимание! в морлеви картинка получается через screenshot и возвращается как png (`bytes`)"
}
```

**Описание**: Локатор для создания скриншота изображения по умолчанию.

**Ключи**:

- `attribute`: Не используется в данном случае (`null`).
- `by`: Тип локатора (`XPATH`).
- `selector`: Выражение для поиска элемента `//a[@id = 'mainpic']//img`.
- `if_list`: Указывает, что если найдено несколько элементов, то использовать первый из них (`first`).
- `use_mouse`: Указывает, что не нужно использовать мышь (`false`).
- `timeout`: Тайм-аут для поиска элемента (`0`).
- `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
- `event`: Событие, которое нужно выполнить (`screenshot()`).
- `mandatory`: Указывает, что действие является обязательным (`true`).
- `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:
- `executor` находит элемент по XPATH.
- `executor` создает скриншот найденного элемента и возвращает его как байтовую строку (`bytes`).
- Если элемент не найден, `executor` выдаст ошибку, так как `mandatory` установлен в `true`.

### 5. `id_supplier`

```json
"id_supplier": {
  "attribute": "innerText",
  "by": "XPATH",
  "selector": "//span[@class = 'ltr sku-copy']",
  "if_list": "first",
  "use_mouse": false,
  "mandatory": true,
  "timeout": 0,
  "timeout_for_event": "presence_of_element_located",
  "event": null,
  "locator_description": "SKU morlevi"
}
```

**Описание**: Локатор для извлечения текста внутри элемента, содержащего SKU.

**Ключи**:

- `attribute`: Атрибут, который нужно извлечь (`innerText`).
- `by`: Тип локатора (`XPATH`).
- `selector`: Выражение для поиска элемента `//span[@class = 'ltr sku-copy']`.
- `if_list`: Указывает, что если найдено несколько элементов, то использовать первый из них (`first`).
- `use_mouse`: Указывает, что не нужно использовать мышь (`false`).
- `mandatory`: Указывает, что действие является обязательным (`true`).
- `timeout`: Тайм-аут для поиска элемента (`0`).
- `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
- `event`: Нет события (`null`).
- `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:
- `executor` находит элемент по XPATH.
- `executor` извлекает текст внутри найденного элемента (`innerText`).
- Если элемент не найден, `executor` выдаст ошибку, так как `mandatory` установлен в `true`.

## Взаимодействие с `executor`

`executor` использует локаторы для выполнения различных действий на веб-странице. Основные шаги взаимодействия:

1.  **Парсинг локатора**: Преобразует локатор в объект `SimpleNamespace`, если это необходимо.
2.  **Поиск элемента**: Использует тип локатора (`by`) и селектор (`selector`) для поиска элемента на странице.
3.  **Выполнение события**: Если указан ключ `event`, выполняет соответствующее действие (например, клик, скриншот).
4.  **Извлечение атрибута**: Если указан ключ `attribute`, извлекает значение атрибута из найденного элемента.
5.  **Обработка ошибок**: Если элемент не найден и действие не обязательно (`mandatory: false`), продолжает выполнение. Если действие обязательно, выдает ошибку.