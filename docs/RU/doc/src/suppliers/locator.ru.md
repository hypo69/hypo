# Локаторы полей на HTML-странице

## Обзор

Этот файл содержит определения локаторов для элементов на веб-страницах, используемых для извлечения данных о продуктах.  Локаторы задаются в формате JSON и описывают способ нахождения элементов на странице, включая атрибуты, стратегии поиска (например, XPath), обработку списков элементов и дополнительные действия (например, клик, скриншот).

## Словари локаторов

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

### Детали локаторов

**Ключи словаря локатора:**

* **`attribute` (str | list | dict):**  Атрибут для извлечения, `null`/`false` - для получения всего элемента. Может быть списком или словарем.  Список - для множественных атрибутов. Словарь - для привязки атрибутов к именам. Пример использования словаря - `{"href": "name"}`
* **`by` (str | list):**  Стратегия поиска элемента (`XPATH`, `CSS_SELECTOR`, etc.). Может быть списком, если нужны несколько стратегий.
* **`selector` (str | list):** Локатор (XPath/CSS селектор). Может быть списком для множественных селекторов.
* **`if_list` (str):** Обработка списка элементов (`first`, `all`, `last`, числа).
* **`use_mouse` (bool | list):** Использование мыши. `true` или `false`, списки допустимы для множественных селекторов.
* **`mandatory` (bool | list):** Обязательность локатора. `true` - локатор необходим, `false` - локатор не обязателен.
* **`timeout` (int):** Время ожидания (в секундах) поиска элемента.
* **`timeout_for_event` (str):** Тип ожидания для события (например, `presence_of_element_located`).
* **`event` (str | list):** Действие, которое должно быть выполнено над элементом (`click()`, `screenshot()`, `send_message()`).
* **`locator_description` (str | list):** Описание локатора.


## Сложные локаторы

Локаторы могут содержать списки, кортежи или словари для более гибкого управления.


## Описание ключей локаторов (подробно)

Подробное описание каждого ключа для более глубокого понимания.


## Обработка мобильных локаторов

Описание способа загрузки локаторов для мобильных версий сайтов.


```