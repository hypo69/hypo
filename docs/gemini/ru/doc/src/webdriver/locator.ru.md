# Локаторы и их взаимодействие с `executor`

## Обзор

В этом документе описываются локаторы, их структура и взаимодействие с классом `executor` для автоматизации взаимодействия с веб-элементами. Локаторы используются для определения того, как находить и взаимодействовать с элементами на веб-странице.

## Содержание

1.  [Обзор](#обзор)
2.  [Примеры локаторов](#примеры-локаторов)
    - [1. `close_banner`](#1-close_banner)
    - [2. `id_manufacturer`](#2-id_manufacturer)
    - [3. `additional_images_urls`](#3-additional_images_urls)
    - [4. `default_image_url`](#4-default_image_url)
    - [5. `id_supplier`](#5-id_supplier)
3.  [Взаимодействие с `executor`](#взаимодействие-с-executor)

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

**Описание**:
Локатор для закрытия pop-up окна (баннера) на странице.

**Ключи**:

-   `attribute` (Optional[str]): Атрибут элемента, который нужно извлечь. В данном случае не используется.
-   `by` (str): Тип локатора (`XPATH`).
-   `selector` (str): Выражение для поиска элемента (`//button[@id = 'closeXButton']`).
-   `if_list` (str): Указывает, какой элемент из списка использовать (`first`).
-   `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия (`false`).
-   `mandatory` (bool): Указывает, является ли действие обязательным (`false`).
-   `timeout` (int): Время ожидания для поиска элемента (`0`).
-   `timeout_for_event` (str): Условие ожидания перед выполнением действия (`presence_of_element_located`).
-   `event` (str): Событие для выполнения (`click()`).
-    `locator_description` (str): Описание локатора.

**Взаимодействие с `executor`**:
`executor` найдет элемент по XPATH и выполнит клик на нем. Если элемент не найден, выполнение продолжится, так как действие не является обязательным.

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

**Описание**:
Локатор для возврата значения, установленного в `attribute`.

**Ключи**:

-   `attribute` (int): Значение атрибута (`11290`).
-   `by` (str): Тип локатора (`VALUE`).
-   `selector` (Optional[str]): Селектор не используется.
-   `if_list` (str): Указывает, какой элемент из списка использовать (`first`).
-   `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия (`false`).
-   `mandatory` (bool): Указывает, является ли действие обязательным (`true`).
-   `timeout` (int): Время ожидания для поиска элемента (`0`).
-   `timeout_for_event` (str): Условие ожидания перед выполнением действия (`presence_of_element_located`).
-   `event` (Optional[str]): Событие не используется (`null`).
-   `locator_description` (str): Описание локатора.

**Взаимодействие с `executor`**:
`executor` вернет значение, установленное в `attribute` (`11290`). Так как `by` установлен в `VALUE`, поиск элемента на странице не производится.

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

**Описание**:
Локатор для извлечения URL дополнительных изображений.

**Ключи**:

-   `attribute` (str): Атрибут элемента, который нужно извлечь (`src`).
-   `by` (str): Тип локатора (`XPATH`).
-   `selector` (str): Выражение для поиска элементов (`//ol[contains(@class, 'flex-control-thumbs')]//img`).
-   `if_list` (str): Указывает, какой элемент из списка использовать (`first`).
-   `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия (`false`).
-   `mandatory` (bool): Указывает, является ли действие обязательным (`false`).
-   `timeout` (int): Время ожидания для поиска элемента (`0`).
-   `timeout_for_event` (str): Условие ожидания перед выполнением действия (`presence_of_element_located`).
-   `event` (Optional[str]): Событие не используется (`null`).

**Взаимодействие с `executor`**:
`executor` найдет элементы по XPATH и извлечет значение атрибута `src` для каждого найденного элемента. Если элементы не найдены, выполнение продолжится, так как действие не является обязательным.

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

**Описание**:
Локатор для создания скриншота изображения по умолчанию.

**Ключи**:

-   `attribute` (Optional[str]): Атрибут элемента не используется.
-   `by` (str): Тип локатора (`XPATH`).
-   `selector` (str): Выражение для поиска элемента (`//a[@id = 'mainpic']//img`).
-   `if_list` (str): Указывает, какой элемент из списка использовать (`first`).
-   `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия (`false`).
-   `mandatory` (bool): Указывает, является ли действие обязательным (`true`).
-   `timeout` (int): Время ожидания для поиска элемента (`0`).
-   `timeout_for_event` (str): Условие ожидания перед выполнением действия (`presence_of_element_located`).
-   `event` (str): Событие для выполнения (`screenshot()`).
-   `locator_description` (str): Описание локатора.

**Взаимодействие с `executor`**:
`executor` найдет элемент по XPATH и сделает скриншот этого элемента. Если элемент не найден, будет выброшена ошибка, так как действие является обязательным.

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

**Описание**:
Локатор для извлечения текста внутри элемента, содержащего SKU.

**Ключи**:

-   `attribute` (str): Атрибут элемента, который нужно извлечь (`innerText`).
-   `by` (str): Тип локатора (`XPATH`).
-   `selector` (str): Выражение для поиска элемента (`//span[@class = 'ltr sku-copy']`).
-   `if_list` (str): Указывает, какой элемент из списка использовать (`first`).
-   `use_mouse` (bool): Указывает, использовать ли мышь для взаимодействия (`false`).
-   `mandatory` (bool): Указывает, является ли действие обязательным (`true`).
-   `timeout` (int): Время ожидания для поиска элемента (`0`).
-   `timeout_for_event` (str): Условие ожидания перед выполнением действия (`presence_of_element_located`).
-   `event` (Optional[str]): Событие не используется (`null`).
-   `locator_description` (str): Описание локатора.

**Взаимодействие с `executor`**:
`executor` найдет элемент по XPATH и извлечет текст внутри элемента (`innerText`). Если элемент не найден, будет выброшена ошибка, так как действие является обязательным.

## Взаимодействие с `executor`

`executor` использует локаторы для выполнения различных действий на веб-странице. Процесс взаимодействия состоит из следующих шагов:

1.  **Парсинг локатора**: Преобразует локатор в объект `SimpleNamespace`, если это необходимо.
2.  **Поиск элемента**: Использует тип локатора (`by`) и селектор (`selector`) для поиска элемента на странице.
3.  **Выполнение события**: Если указан ключ `event`, выполняет соответствующее действие (например, клик, скриншот).
4.  **Извлечение атрибута**: Если указан ключ `attribute`, извлекает значение атрибута из найденного элемента.
5.  **Обработка ошибок**: Если элемент не найден и действие не обязательно (`mandatory: false`), выполнение продолжается. Если действие обязательно, выдается ошибка.