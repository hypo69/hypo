# Документация для разработчика: Локаторы элементов на HTML-странице

## Обзор

Этот документ описывает структуру и использование локаторов элементов на HTML-страницах в проекте `hypotez`. Локаторы используются для поиска и взаимодействия с элементами на веб-странице с помощью WebDriver. Они определяют, как находить элементы, какие атрибуты извлекать и какие действия выполнять над ними.

## Подробнее

В этом разделе представлено подробное описание структуры локаторов, их параметров и примеры использования. Локаторы позволяют гибко настраивать взаимодействие с веб-страницами, адаптируясь к различным структурам и изменениям в разметке.

## Пример локатора

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
    "locator_description": "Закрываю pop-up окно. Если оно не появилось — не страшно (`mandatory`: `false`)."
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
    "locator_description": "Внимание! В Morlevi картинка получается через screenshot и возвращается как PNG (`bytes`)."
  }
```

### Детали

Имя словаря соответствует имени поля класса `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

Например, локатор `name {}` будет использоваться для получения имени продукта, локатор `price {}` — для получения цены продукта и т.д.

```python
f = ProductFields(
    name = d.execute_locator('name'),
    price = d.execute_locator('price'),
    ...
)
```

Кроме того, можно создать свои локаторы для дополнительных действий на странице.
Например, `close_banner {}` будет использоваться для закрытия баннера на странице.

Словарь локатора содержит следующие ключи:

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
  **Важно❗**: Если указан `event`, он будет выполнен **до** получения значения из `attribute`.  
  Например:  
  ```json
  {
      ...
      "attribute": "href",
      ...
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()",
      ...
  }
  ```  
  В этом случае сначала драйвер выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.  
  Принцип работы: **действие -> атрибут**.  
  Еще примеры эвентов:\
   - `screenshot()` возвращает вебэлемент как снимок экрана. Удобно, когда `CDN` сервер не возвращает изображение через `URL`.\
   - `send_message()` - отправляет сообщение вебэлементу.  
     Я рекомендую отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:  
     ```json
     {"timeout": 0, 
     "timeout_for_event": "presence_of_element_located", 
     "event": "click();backspace(10);%EXTERNAL_MESSAGE%"
     }```
     
       
       ```
       исполняет последовательность:  
       <ol type="1">\
         <li><code>click()</code> - нажимает на вебэлемент (переводит фокус в поле ввода) <code>&lt;textbox&gt;</code>.</li>\
         <li><code>backspace(10)</code> - сдвигает каретку на 10 символов влево (очищает текст в поле ввода).</li>\
         <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>\
       </ol>

       ```

- **`mandatory`**: Является ли локатор обязательным.  
  Если `{mandatory: true}` и взаимодействие с веб-элементом невозможно, код выбросит ошибку. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Сложные локаторы

В ключи локатора можно передавать списки, кортежи или словари.

#### Пример локатора со списками

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
    "timeout": 0,
    "timeout_for_event": "presence_of_element_located",
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

#### Пример локатора со словарём

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```

---

### Описание ключей локатора

1. **`attribute`**:  
   Этот ключ указывает на атрибут, который будет использован для поиска элемента. В данном случае значение `null`, что означает, что атрибут не используется для поиска.

2. **`by`**:  
   Указывает на метод поиска элемента на странице. В данном случае это `'XPATH'`, что означает использование XPath для нахождения элемента.

3. **`selector`**:  
   Это строка, представляющая локатор, который будет использоваться для нахождения элемента. В данном случае это XPath выражение `"//a[@id = 'mainpic']//img"`, что означает поиск изображения внутри тега `a` с `id='mainpic'` .

4. **`if_list`**:  
   Указывает правило обработки списка элементов. В данном случае указано `'first'`, что означает, что если элементов несколько, то будет возвращен первый элемент из найденного списка.

5. **`use_mouse`**:  
   Булевое значение, которое указывает, нужно ли использовать мышь для взаимодействия с элементом. В данном случае установлено `false`, что значит, что мышь не используется.

6. **`timeout`**:  
   Время ожидания (в секундах) для нахождения элемента. В данном случае установлено значение `0`, что означает, что поиск элемента будет выполнен немедленно без ожидания.

7. **`timeout_for_event`**:  
   Время ожидания (в секундах) для события. В данном случае указано `"presence_of_element_located"`, что означает, что WebDriver будет ожидать появления элемента перед выполнением события.

8. **`event`**:  
   Указывает, какое событие должно быть выполнено с найденным элементом. Например, это может быть `click()`, чтобы кликнуть на элемент, или `screenshot()`, чтобы сделать скриншот элемента.

9. **`mandatory`**:  
   Указывает, является ли локатор обязательным. Если установлено значение `true`, то если элемент не будет найден или не удастся с ним взаимодействовать, будет вызвана ошибка.

10. **`locator_description`**:  
    Описание того, что делает локатор, чтобы помочь в понимании его цели.

-----------------

- Разметка страницы может меняться. Например десктопная/мобильная версии. В Таком случае я рекомендую держать несколько файлов локторов для каждой из версий.
Например: `product.json`,`product_mobile_site.json`

По умолчанию локаторы читаются из файла `product.json`. Вот как можно это изменить:
В файле грабера страницы поставщика делается проверка на `url`

```python
    async def grab_page(self) -> ProductFields:
        ...
         = driver  
        if 'ksp.co.il/mob' in d.current_url: # <- бывет, что подключается к мобильной версии сайта
            self.locator = j_loads_ns(gs.path.src / 'suppliers' / 'ksp' / 'locators' / 'product_mobile_site.json')
        ...