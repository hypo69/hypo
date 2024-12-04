# Локаторы полей на HTML-странице

## Обзор

Данный файл содержит описание локаторов для поиска веб-элементов на HTML-странице. Локаторы определяют способ нахождения элементов с помощью различных стратегий (XPATH, CSS-селекторы и т.д.) и параметров, таких как атрибуты, события и обязательность поиска.  Формат описания локаторов - JSON.

## Примеры локаторов

### Пример локатора:

```json
"close_banner": {
    "attribute": null, 
    "by": "XPATH",
    "selector": "//button[@id = 'closeXButton']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": false,
    "event": "click()",
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`)."
  },
  "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
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
    "event": null,
    "locator_description": "SKU Morlevi."
  },
  "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`)."
  }
```

## Детали

Имя словаря соответствует имени поля класса `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).


### Параметры локатора

- **`attribute` (строка или список строк):** Атрибут, который нужно получить от веб-элемента. Например: `innerText`, `src`, `id`, `href` и т.д. Если `null` или `false`, WebDriver возвращает весь веб-элемент (`WebElement`).

- **`by` (строка или список строк):** Стратегия поиска элемента.  Возможные значения: `ID`, `NAME`, `CLASS_NAME`, `TAG_NAME`, `LINK_TEXT`, `PARTIAL_LINK_TEXT`, `CSS_SELECTOR`, `XPATH`.

- **`selector` (строка или список строк):** Селектор, определяющий способ нахождения веб-элемента. Примеры: `(//li[@class = 'slide selected previous'])[1]//img`, `//a[@id = 'mainpic']//img`, `//span[@class = 'ltr sku-copy']`.

- **`if_list` (строка):**  Определяет, как обработать список найденных элементов.  Возможные значения: `first`, `all`, `last`, `even`, `odd` или список номеров элементов (например, `[1,3,5]`).

- **`use_mouse` (булево или список булевых значений):**  Используется для выполнения действий с помощью мыши.

- **`event` (строка или список строк):** Действие, которое должно быть выполнено с веб-элементом до получения значения атрибута.  Примеры: `click()`, `screenshot()`, `scroll()`.  `send_message()`: отправляет сообщение веб-элементу (рекомендуется использование `%EXTERNAL_MESSAGE%`).

- **`mandatory` (булево или список булевых значений):**  Обязательность локатора. Если `true`, и элемент не найден, вызывается исключение.

- **`locator_description` (строка или список строк):**  Описание локатора.


### Сложные локаторы

В ключи локатора можно передавать списки, кортежи или словари, позволяя создавать сложные правила поиска.

#### Пример локатора со списками:

```json
"sample_locator": {
    "attribute": [
      null,
      "href"
    ],
    "by": [
      "XPATH",
      "XPATH"
    ],
    "selector": [
      "//a[contains(@href, '#tab-description')]",
      "//div[@id = 'tab-description']//p"
    ],
    "event": [
      "click()",
      null
    ],
    "if_list": "first",
    "use_mouse": [
      false,
      false
    ],
    "mandatory": [
      true,
      true
    ],
    "locator_description": [
      "Нажимаю на вкладку для открытия поля description.",
      "Читаю данные из div."
    ]
  }
```


#### Пример локатора со словарем:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```
```