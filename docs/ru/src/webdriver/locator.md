# Описание локаторов и их взаимодействие с `executor`

## Обзор

Этот документ содержит объяснение локаторов и их взаимодействие с `executor`. Локаторы - это объекты конфигурации, которые описывают, как найти веб-элементы на странице и взаимодействовать с ними. Они передаются классу `ExecuteLocator` для выполнения различных действий, таких как клики, отправка сообщений, извлечение атрибутов и т. д.

## Подробнее

Локаторы используются для автоматизации взаимодействия с веб-элементами. `executor` обеспечивает их выполнение с учетом всех параметров и условий. Основные шаги взаимодействия:

1.  **Разбор локатора**: Преобразует локатор в объект `SimpleNamespace`, если это необходимо.
2.  **Поиск элемента**: Использует тип локатора (`by`) и селектор (`selector`) для поиска элемента на странице.
3.  **Выполнение события**: Если указан ключ `event`, выполняет соответствующее действие (например, клик, скриншот).
4.  **Извлечение атрибута**: Если указан ключ `attribute`, извлекает значение атрибута из найденного элемента.
5.  **Обработка ошибок**: Если элемент не найден и действие не является обязательным (`mandatory: false`), продолжает выполнение. Если действие является обязательным, вызывает ошибку.

## Примеры локаторов

### `close_banner`

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
  "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
}
```

**Назначение локатора**: Закрыть баннер (всплывающее окно), если он появляется на странице.

**Ключи**:

*   `attribute`: Не используется в данном случае.
*   `by`: Тип локатора (`XPATH`).
*   `selector`: Выражение для поиска элемента (`//button[@id = 'closeXButton']`).
*   `if_list`: Если найдено несколько элементов, использовать первый (`first`).
*   `use_mouse`: Не использовать мышь (`false`).
*   `mandatory`: Необязательное действие (`false`).
*   `timeout`: Время ожидания для поиска элемента (`0`).
*   `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
*   `event`: Событие для выполнения (`click()`).
*   `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:

*   `executor` найдет элемент по XPATH и выполнит клик по нему.
*   Если элемент не найден, `executor` продолжит выполнение, так как действие не является обязательным (`mandatory: false`).

### `id_manufacturer`

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

**Назначение локатора**: Вернуть значение, установленное в `attribute`.

**Ключи**:

*   `attribute`: Значение атрибута (`11290`).
*   `by`: Тип локатора (`VALUE`).
*   `selector`: Не используется в данном случае.
*   `if_list`: Если найдено несколько элементов, использовать первый (`first`).
*   `use_mouse`: Не использовать мышь (`false`).
*   `mandatory`: Обязательное действие (`true`).
*   `timeout`: Время ожидания для поиска элемента (`0`).
*   `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
*   `event`: Нет события (`null`).
*   `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:

*   `executor` вернет значение, установленное в `attribute` (`11290`).
*   Поскольку `by` установлено в `VALUE`, `executor` не будет искать элемент на странице.

### `additional_images_urls`

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

**Назначение локатора**: Извлечь URL-адреса дополнительных изображений.

**Ключи**:

*   `attribute`: Атрибут для извлечения (`src`).
*   `by`: Тип локатора (`XPATH`).
*   `selector`: Выражение для поиска элементов (`//ol[contains(@class, 'flex-control-thumbs')]//img`).
*   `if_list`: Если найдено несколько элементов, использовать первый (`first`).
*   `use_mouse`: Не использовать мышь (`false`).
*   `mandatory`: Необязательное действие (`false`).
*   `timeout`: Время ожидания для поиска элемента (`0`).
*   `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
*   `event`: Нет события (`null`).

**Взаимодействие с `executor`**:

*   `executor` найдет элементы по XPATH и извлечет значение атрибута `src` для каждого элемента.
*   Если элементы не найдены, `executor` продолжит выполнение, так как действие не является обязательным (`mandatory: false`).

### `default_image_url`

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
  "locator_description": "Attention! In Morlevi, the image is obtained via screenshot and returned as png (`bytes`)"
}
```

**Назначение локатора**: Сделать скриншот изображения по умолчанию.

**Ключи**:

*   `attribute`: Не используется в данном случае.
*   `by`: Тип локатора (`XPATH`).
*   `selector`: Выражение для поиска элемента (`//a[@id = 'mainpic']//img`).
*   `if_list`: Если найдено несколько элементов, использовать первый (`first`).
*   `use_mouse`: Не использовать мышь (`false`).
*   `timeout`: Время ожидания для поиска элемента (`0`).
*   `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
*   `event`: Событие для выполнения (`screenshot()`).
*   `mandatory`: Обязательное действие (`true`).
*   `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:

*   `executor` найдет элемент по XPATH и сделает скриншот элемента.
*   Если элемент не найден, `executor` вызовет ошибку, так как действие является обязательным (`mandatory: true`).

### `id_supplier`

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

**Назначение локатора**: Извлечь текст внутри элемента, содержащего SKU.

**Ключи**:

*   `attribute`: Атрибут для извлечения (`innerText`).
*   `by`: Тип локатора (`XPATH`).
*   `selector`: Выражение для поиска элемента (`//span[@class = 'ltr sku-copy']`).
*   `if_list`: Если найдено несколько элементов, использовать первый (`first`).
*   `use_mouse`: Не использовать мышь (`false`).
*   `mandatory`: Обязательное действие (`true`).
*   `timeout`: Время ожидания для поиска элемента (`0`).
*   `timeout_for_event`: Условие ожидания (`presence_of_element_located`).
*   `event`: Нет события (`null`).
*   `locator_description`: Описание локатора.

**Взаимодействие с `executor`**:

*   `executor` найдет элемент по XPATH и извлечет текст внутри элемента (`innerText`).
*   Если элемент не найден, `executor` вызовет ошибку, так как действие является обязательным (`mandatory: true`).