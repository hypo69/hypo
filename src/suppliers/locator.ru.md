
# Локаторы полей на `HTML`-странице

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

### Детали:
Имя словаря соответствует имени поля класса `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить от веб-элемента. Например: `innerText`, `src`, `id`, `href` и т.д.  
  Если установить значение `attribute` в `none/false`, то WebDriver вернёт весь веб-элемент (`WebElement`).

- **`by`**: Стратегия для поиска элемента:  
  - `ID` соответствует `By.ID`  
  - `NAME` соответствует `By.NAME`  
  - `CLASS_NAME` соответствует `By.CLASS_NAME`  
  - `TAG_NAME` соответствует `By.TAG_NAME`  
  - `LINK_TEXT` соответствует `By.LINK_TEXT`  
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`  
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`  
  - `XPATH` соответствует `By.XPATH`

- **`selector`**: Селектор, определяющий способ нахождения веб-элемента. Примеры:  
  `(//li[@class = 'slide selected previous'])[1]//img`,  
  `//a[@id = 'mainpic']//img`,  
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Определяет, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:  
  - `first`: выбрать первый элемент из списка.  
  - `all`: выбрать все элементы.  
  - `last`: выбрать последний элемент.  
  - `even`, `odd`: выбрать чётные/нечётные элементы.  
  - Указание конкретных номеров, например, `1,2,...` или `[1,3,5]`: выбрать элементы с указанными номерами.  

  Альтернативный способ — указать номер элемента прямо в селекторе, например:  
  `(//div[contains(@class, 'description')])[2]//p`  

- **`use_mouse`**: `true` | `false`  
  Используется для выполнения действий с помощью мыши.

- **`event`**: WebDriver может выполнить действие с веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д.  
  **Важно**: Если указан `event`, он будет выполнен **до** получения значения из `attribute`.  
  Например:  
  ```json
  {"attribute": "href",
  ...
  "event": "click()"
  }
  ```
  В этом случае сначала драйвер выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.  
  Принцип работы: **действие -> атрибут**.  
  Еще примеры эвентов:
   - `screenshot()` возвращает вебэлемент как снимок экрана. Удобно, когда `CDN` сервер не возвращает изображение через `URL`.
   - `send_message()` - отправляет сообщение вебэлементу.  
     Я рекомендую отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:  
     - `{"event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`  
       исполняет последовательность:  
       <ol type="1">
         <li><code>click()</code> - нажимает на вебэлемент (переводит фокус в поле ввода) <code>&lt;textbox&gt;</code>.</li>
         <li><code>backspace(10)</code> - сдвигает каретку на 10 символов влево (очищает текст в поле ввода).</li>
         <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
       </ol>

- **`mandatory`**: Является ли локатор обязательным.  
  Если `{mandatory: true}` и взаимодействие с веб-элементом невозможно, код выбросит ошибку. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Сложные локаторы:
В ключи локатора можно передавать списки, кортежи или словари.

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
В этом примере сначала будет найден элемент `//a[contains(@href, '#tab-description')]`.  
Драйвер выполнит команду `click()`, затем получит значение атрибута `href` элемента `//a[contains(@href, '#tab-description')]`.

#### Пример локатора со словарём:
```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```
