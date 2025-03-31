# Локаторы полей на `HTML` странице

## Обзор

Этот документ описывает структуру и использование локаторов для извлечения данных с HTML-страницы. Локаторы определяют, как находить и взаимодействовать с веб-элементами, такими как кнопки, изображения и текстовые поля.

## Оглавление

- [Пример локатора](#пример-локатора)
- [Детали](#детали)
- [Сложные локаторы](#сложные-локаторы)
    - [Пример локатора со списками](#пример-локатора-со-списками)
    - [Пример локатора со словарем](#пример-локатора-со-словарем)
- [Описание ключей локаторов](#описание-ключей-локаторов)

## Пример локатора:

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
    "locator_description": "Закрыть всплывающее окно. Если оно не появляется — не проблема (`mandatory`: `false`)."
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
    "locator_description": "Получить список `urls` для дополнительных изображений."
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
    "locator_description": "Внимание! В Morlevi изображение получается через скриншот и возвращается как PNG (`bytes`)."
  }
```

## Детали

Имя словаря соответствует имени поля в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить из веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.  
Если `attribute` установлено в `none/false`, WebDriver вернет весь веб-элемент (`WebElement`).

- **`by`**: Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`

- **`selector`**: Селектор, определяющий, как найти веб-элемент. Примеры:  
  `(//li[@class = 'slide selected previous'])[1]//img`,  
  `//a[@id = 'mainpic']//img`,  
  `//span[@class = 'ltr sku-copy']`.

- **`if_list`**: Определяет, что делать со списком найденных веб-элементов (`web_element`). Возможные значения:
    - `first`: вернуть первый элемент из списка.
    - `all`: вернуть все элементы.
    - `last`: вернуть последний элемент.
    - `even`, `odd`: вернуть четные/нечетные элементы.
    - Конкретные номера, например, `1,2,...` или `[1,3,5]`: вернуть элементы с указанными номерами.

   Альтернативно, можно указать номер элемента непосредственно в селекторе, например:  
   `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`  
  Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**: WebDriver может выполнить действие с веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д.  
  **Важно**: Если `event` указано, оно будет выполнено **перед** получением значения из `attribute`.  
  Пример:
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
  В этом случае драйвер сначала выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.  
  Последовательность работает так: **действие -> атрибут**.  
  Другие примеры событий:
    - `screenshot()` возвращает веб-элемент в виде скриншота. Полезно, когда `CDN` сервер не возвращает изображение по `URL`.
    - `send_message()` отправляет сообщение веб-элементу.  
      Рекомендуется отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:  
      - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`  
        Это выполнит следующую последовательность:
          <ol type="1">
            <li><code>click()</code> - кликает по веб-элементу (фокусируется на поле ввода) <code>&lt;textbox&gt;</code>.</li>
            <li><code>backspace(10)</code> - перемещает курсор на 10 символов влево (очищает текст в поле ввода).</li>
            <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
          </ol>

- **`mandatory`**: Является ли локатор обязательным.  
  Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшена ошибка. Если `mandatory: false`, элемент будет пропущен.

-   **`timeout`**: Тайм-аут (в секундах) для поиска элемента. Значение `0` означает отсутствие ожидания; элемент будет найден немедленно.

- **`timeout_for_event`**: Тайм-аут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ждать, пока элемент не появится, прежде чем выполнить событие.

- **`locator_description`**: Описание локатора.

## Сложные локаторы

Можно передавать списки, кортежи или словари в ключах локатора.

### Пример локатора со списками:

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
      "Клик по вкладке, чтобы открыть поле описания.",
      "Чтение данных из div."
    ]
  }
```
В этом примере будет найден первый элемент `//a[contains(@href, '#tab-description')]`.  
Драйвер выполнит `click()`, а затем получит атрибут `href` элемента `//a[contains(@href, '#tab-description')]`.

### Пример локатора со словарем:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```

## Описание ключей локаторов:

1. **`attribute`**:
    - Этот ключ указывает атрибут, который будет использоваться для получения данных из элемента. `null` означает, что атрибут не используется для поиска элемента.

2. **`by`**:
    - Определяет метод для поиска элемента на странице. В этом случае это `'XPATH'`, что означает использование XPath для поиска элемента.

3.  **`selector`**:
    - Строка локатора, которая будет использоваться для поиска веб-элемента. В этом случае это XPath выражение `"//a[@id = 'mainpic']//img"`, которое находит изображение внутри тега `a` с `id='mainpic'`.

4.  **`if_list`**:
    - Указывает правило для обработки списка элементов. В этом случае `'first'` означает возвращение первого элемента из списка.

5.  **`use_mouse`**:
    - Логическое значение, указывающее, использовать ли мышь для взаимодействия с элементом. Установлено значение `false`, что означает, что взаимодействие с мышью не требуется.

6.  **`timeout`**:
    - Тайм-аут (в секундах) для поиска элемента. Значение `0` означает отсутствие ожидания; элемент будет найден немедленно.

7.  **`timeout_for_event`**:
    - Тайм-аут (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ждать, пока элемент не появится, прежде чем выполнить событие.

8.  **`event`**:
    - Действие, которое будет выполнено с веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д. Событие будет выполнено перед получением значения из `attribute`.

9. **`mandatory`**:
    - Указывает, является ли локатор обязательным. Если установлено значение `true`, будет выдана ошибка, если элемент не может быть найден или с ним нельзя взаимодействовать.

10. **`locator_description`**:
    - Описание локатора, предоставляющее больше контекста о том, что он делает.

---
- Макет страницы может меняться, например, между настольной и мобильной версиями. В таких случаях я рекомендую вести отдельные файлы локаторов для каждой версии.
Пример: `product.json`, `product_mobile_site.json`.