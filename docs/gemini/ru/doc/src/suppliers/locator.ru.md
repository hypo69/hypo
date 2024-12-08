# Локаторы полей на HTML-странице

## Обзор

Данный файл содержит JSON-локаторы для элементов на HTML-странице, используемые для взаимодействия с веб-драйвером.  Каждый локатор описывает способ нахождения элемента на странице и возможные действия с ним.

## Локаторы

### Пример локатора:

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
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`).",
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
    "event": null,
    "locator_description": "Получает список `url` дополнительных изображений."
  },
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
    "locator_description": "SKU Morlevi."
  },
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
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`).",
  }
```

### Детали:

**Описание ключей локатора:**

* **`attribute`**: Атрибут для извлечения данных. `null` означает извлечение всего элемента.
* **`by`**: Стратегия поиска (XPATH, ID, NAME, CSS_SELECTOR, etc.).  Соответствие с `By` из `Selenium`.
* **`selector`**: XPath или CSS селектор для поиска элемента.
* **`if_list`**: Обработка списка найденных элементов (`first`, `all`, `last`).
* **`use_mouse`**:  Используется ли мышь (`true`/`false`).
* **`mandatory`**:  Обязателен ли локатор (`true`/`false`).
* **`timeout`**: Время ожидания поиска (в секундах). `0` означает поиск без ожидания.
* **`timeout_for_event`**: Время ожидания события, например `presence_of_element_located`.
* **`event`**: Действие, выполняемое с элементом (click(), screenshot(), scroll(), etc.).
* **`locator_description`**:  Описание цели и назначения локатора.


### Сложные локаторы

Локаторы могут содержать списки, кортежи или словари для более сложных сценариев поиска и обработки.  При этом, структура описания параметров повторяется для каждого значения внутри списка.


### Описание параметров в примере

Раздел описывает детально назначение каждого параметра локатора, позволяя легко разобраться в формате данных.


### Важные замечания

* Разметка страниц может изменяться (разные версии сайта), поэтому рекомендуется использовать отдельные файлы локаторов для различных версий.
* Локаторы по умолчанию берутся из `product.json`.  В коде можно загружать локаторы из альтернативных файлов (например, `product_mobile_site.json`) в зависимости от контекста страницы.

```
```