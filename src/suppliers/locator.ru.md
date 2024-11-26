# Локаторы полей на `HTML` странице
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
    "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
  },
    "additional_images_urls": {
    "attribute": "src",
    "by": "XPATH",
    "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
    "if_list": "all",
    "use_mouse": false,
    "mandatory": false,
    "event": null
    "locator_description": "получает список `url` дополнительных изображений"
  },
    "id_supplier": {
    "attribute": "innerText",
    "by": "XPATH",
    "selector": "//span[@class = 'ltr sku-copy']",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null,
    "locator_description": "SKU morlevi"
  },
    "default_image_url": {
    "attribute": null,
    "by": "XPATH",
    "selector": "//a[@id = 'mainpic']//img",
    "if_list": "first",
    "use_mouse": false,
    "event": "screenshot()",
    "mandatory": true,
    "locator_description": "Внимание! в морлеви картинка получается через screenshot и возвращается как png (`bytes`)"
  },
```
где:
имя словаря - это имя поля класса `ProductFields` ([подробно о `ProductFields`](../product/product_fileds))

- `attribute`: аттрибут, который мы хотим получить от вебэемента. Напринер: `innerText`,`src`,`id`,`href`,... Если установить значение аттрибута в `none/false`, то ведрайвер вернет весь вебеэлемент (`WebElement`) 

- `by`: стратегия захвата элемента:
 
    `ID` соответствует `By.ID`  
    `NAME` соответствует `By.NAME`  
    `CLASS_NAME`  соответствует `By.CLASS_NAME`  
    `TAG_NAME` соответствует `By.TAG_NAME`  
    `LINK_TEXT` соответствует `By.LINK_TEXT`  
    `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`  
    `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`  
    `XPATH` соответствует `By.XPATH`

- `selector`: селектор, определяющий как найти вебэлемент. Примеры селекторов:
    `(//li[@class = 'slide selected previous'])[1]//img`,`//a[@id = 'mainpic']//img`,`//span[@class = 'ltr sku-copy']`

- `if_list`: определяет, что делать со списком полученных вебэлементов. Значения, которые можно установить:
    `first` - брать первый из списка 
    `all` - забрать весь список вебэлементов со страницы 
    `last` - забрать последний вебэлемент из списка 
    `even`, `odd` - забрать чётные/нечётные вебэелементы 

- use_mouse`: `true` | `false`

`event`: вебдрайвер может выполнить дейаствие над вебэлементом. Например, `click()`, `screenshot()`, `scroll()`, ...
Важно! Если указан `event`, то он будет выполнен, до он будет выполнен, до того, как драйвер получит значение в `attribute`.
Например, если 
```json
{"attribute":"href",
....
"event":"click()"
}
```
то вначале драйвер передаст вебэлементу комманду, а потом получит его аттрибут.
принцип такой: действие -> аттрибут.

- `mandatory`: является ли локатор обязательным. Если да {`mandatory`:`True`}, то при невозможности взаимодейтвия с вебэлементом код выдаст ошибку, если нет - пропустит обработку вебэлемента

- `locator_description`: Заметка о локатoре

Более сложные локаторы:
В ключи локатора можно передавать списки/коретжи и словари.
Пример локатора со списками:
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
      "Нажимаю на таб для отркытия поля description",
      "читаю данные из div"
    ]
  },
}
```
В данном примере вначале будет найден элемент  "//a[contains(@href, '#tab-description')]", драйвер пошлет ему комаду `click()` и после этого получит значение `href` элемента "//a[contains(@href, '#tab-description')]",

Пример словаря в локаторе:
```json
"sample_locator":
{
"attribute":{"href":"name"},
...
}
```
[chatgpt](https://chatgpt.com/share/674617f1-ebb8-800d-b62b-a3ab2ab39d14)