# Анализ кода модуля `locator.md`

**Качество кода**
8
-  Плюсы
    - Документ содержит подробное описание структуры JSON-объектов, используемых для локаторов элементов на веб-странице.
    - Описаны все ключевые поля локаторов, их типы и возможные значения.
    - Приведены примеры использования локаторов в различных сценариях.
    - Объясняется порядок выполнения действий при использовании события (`event`).
    - Документ предоставляет рекомендации по организации файлов с локаторами для разных версий сайта.
-  Минусы
    - Документ представляет собой описание структуры данных в Markdown, а не Python код, поэтому рекомендации по форматированию кода не применимы напрямую.
    - Отсутствует явное указание на использование `src.utils.jjson` для загрузки JSON, поскольку это не Python код.
    - Не хватает явного упоминания о логировании ошибок при использовании локаторов в коде (хотя это подразумевается контекстом).

**Рекомендации по улучшению**
1.  **Добавить примеры кода на Python**:
    - Включить примеры загрузки JSON с локаторами с использованием `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Показать, как использовать локаторы для поиска элементов на странице.
2.  **Уточнить использование `timeout_for_event`**:
    -  Добавить пояснение, что значения для `timeout_for_event` берутся из `selenium.webdriver.support.expected_conditions`.
    -  Перечислить все возможные варианты, такие как `"presence_of_element_located"`, `"element_to_be_clickable"`, `"visibility_of_element_located"` и т.д.
3.  **Логирование**:
    -  Явно указать в тексте, что при обработке локаторов следует использовать `logger.error` для фиксации ошибок.
4.  **Добавить примеры сложных локаторов**:
    -  Показать примеры использования вложенных структур в селекторах.
5.  **Формат reStructuredText**:
    -  Хотя это не Python код, было бы полезно предоставить примеры форматирования описаний для `locator_description` в формате RST, чтобы разработчики понимали, как документировать локаторы.

**Оптимизированный код**
```markdown
# Полевые локаторы на `HTML` странице

### Пример локатора:

```json
{
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
}
```

### Детали:

Имя словаря соответствует имени поля в классе `ProductFields` ([подробнее о `ProductFields`](../product/product_fields)).

- **`attribute`**: Атрибут, который нужно получить из веб-элемента. Примеры: `innerText`, `src`, `id`, `href` и т.д.
  Если `attribute` установлен в `none/false`, WebDriver вернет весь веб-элемент (`WebElement`).

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
  - Конкретные числа, например, `1,2,...` или `[1,3,5]`: вернуть элементы с указанными номерами.

  Также можно указать номер элемента непосредственно в селекторе, например:
  `(//div[contains(@class, 'description')])[2]//p`

- **`use_mouse`**: `true` | `false`
  Определяет, использовать ли мышь для взаимодействия с элементом.

- **`event`**: WebDriver может выполнить действие над веб-элементом, такое как `click()`, `screenshot()`, `scroll()` и т.д.
  **Важно**: Если указано `event`, оно будет выполнено **до** получения значения из `attribute`.
  Пример:
  ```json
  {
      "...": "...",
      "attribute": "href",
      "...": "...",
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()",
      "...": "..."
  }
  ```
  В этом случае драйвер сначала выполнит `click()` на веб-элементе, а затем получит его атрибут `href`.
  Последовательность работает так: **действие -> атрибут**.
  Другие примеры событий:
    - `screenshot()` возвращает веб-элемент в виде скриншота. Полезно, когда сервер `CDN` не возвращает изображение через `URL`.
    - `send_message()` отправляет сообщение веб-элементу.
      Рекомендуется отправлять сообщение через переменную `%EXTERNAL_MESSAGE%`, как показано ниже:
      - `{"timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click();backspace(10);%EXTERNAL_MESSAGE%"}`
        Это выполнит последовательность:
        <ol type="1">
          <li><code>click()</code> - кликает веб-элемент (фокусируется на поле ввода) <code>&lt;textbox&gt;</code>.</li>
          <li><code>backspace(10)</code> - перемещает каретку на 10 символов влево (очищает текст в поле ввода).</li>
          <li><code>%EXTERNAL_MESSAGE%</code> - отправляет сообщение в поле ввода.</li>
        </ol>

- **`mandatory`**: Является ли локатор обязательным.
  Если `{mandatory: true}` и взаимодействие с элементом невозможно, будет выброшена ошибка. Если `mandatory: false`, элемент будет пропущен.

- **`locator_description`**: Описание локатора.

---

### Сложные локаторы:

Можно передавать списки, кортежи или словари в ключах локатора.

#### Пример локатора со списками:

```json
{
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
}
```
В этом примере будет найден первый элемент `//a[contains(@href, '#tab-description')]`.
Драйвер выполнит `click()`, а затем получит атрибут `href` элемента `//a[contains(@href, '#tab-description')]`.

#### Пример локатора со словарем:

```json
{
  "sample_locator": {
    "attribute": {"href": "name"},
      "...": "..."
    }
}
```

---

### Описание ключей для локаторов:

1. **`attribute`**:
   Этот ключ указывает атрибут, который будет использоваться для получения данных из элемента. `null` означает, что атрибут не используется для поиска элемента.

2. **`by`**:
   Указывает метод для определения элемента на странице. В данном случае это `'XPATH'`, что означает использование XPath для определения элемента.

3. **`selector`**:
   Строка локатора, которая будет использоваться для поиска веб-элемента. В данном случае это XPath-выражение `"//a[@id = 'mainpic']//img"`, которое находит изображение внутри тега `a` с `id='mainpic'`.

4. **`if_list`**:
   Определяет правило для обработки списка элементов. В данном случае `'first'` означает возврат первого элемента из списка.

5. **`use_mouse`**:
   Логическое значение, указывающее, следует ли использовать мышь для взаимодействия с элементом. Установлено в `false`, что означает отсутствие необходимости во взаимодействии с мышью.

6.  **`timeout`**:
    Время ожидания (в секундах) для поиска элемента. Значение `0` означает отсутствие ожидания; элемент будет найден немедленно.

7.  **`timeout_for_event`**:
   Время ожидания (в секундах) для события. `"presence_of_element_located"` означает, что WebDriver будет ждать, пока элемент не появится, прежде чем выполнять событие. Дополнительные возможные значения: `"element_to_be_clickable"`, `"visibility_of_element_located"` и другие из `selenium.webdriver.support.expected_conditions`.

8. **`event`**:
   Действие, которое будет выполнено над веб-элементом, например `click()`, `screenshot()`, `scroll()` и т.д. Событие будет выполнено перед получением значения из `attribute`.

9. **`mandatory`**:
   Указывает, является ли локатор обязательным. Если установлено значение `true`, возникнет ошибка, если элемент не может быть найден или с ним нельзя взаимодействовать.

10. **`locator_description`**:
   Описание локатора, предоставляющее больше контекста о том, что он делает.

---------------
-  Макет страницы может варьироваться, например, между настольной и мобильной версиями. В таких случаях рекомендуется вести отдельные файлы локаторов для каждой версии.
    Пример: `product.json`, `product_mobile_site.json`.

#### Пример загрузки и использования локаторов в Python:

```python
from src.utils.jjson import j_loads
from src.logger.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element(driver, locator_data):
    """
    Находит элемент на странице, используя предоставленные данные локатора.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param locator_data: Словарь с данными локатора.
    :return: Найденный веб-элемент или None, если элемент не найден.
    """
    try:
        by_strategy = getattr(By, locator_data['by'])
        wait = WebDriverWait(driver, locator_data.get('timeout', 0))
        element = wait.until(EC.presence_of_element_located((by_strategy, locator_data['selector'])))

        if 'event' in locator_data and locator_data['event']:
            if 'timeout_for_event' in locator_data:
                 wait_event = WebDriverWait(driver, locator_data['timeout_for_event'])
                 wait_event.until(EC.presence_of_element_located((by_strategy, locator_data['selector'])))
            
            event = locator_data['event']
            if event == "click()":
                element.click()
            elif event == "screenshot()":
                # TODO: добавить обработку скриншота
                 ...
            elif event.startswith("send_message()"):
                # TODO: добавить обработку отправки сообщения
                ...

        if locator_data['attribute']:
            return element.get_attribute(locator_data['attribute'])
        else:
            return element
    except Exception as ex:
        logger.error(f"Ошибка при поиске элемента: {locator_data=}", exc_info=True)
        if locator_data.get('mandatory', False):
           raise
        return None


if __name__ == '__main__':
   
    # Пример использования
    
    # TODO: здесь нужно создать инстанс драйвера, зайти на страницу
    driver = ...

    locator_file = 'suppliers/locator.json'
    try:
      locators = j_loads(locator_file)
    except Exception as ex:
      logger.error(f"Не удалось загрузить файл с локаторами: {locator_file}", exc_info=True)
      ...
      
    # Предположим, что у вас есть словарь с локаторами "close_banner"
    locator = locators.get("close_banner")
    if locator:
        close_button = get_element(driver, locator)
        if close_button:
          # TODO: действия с элементом
          ...
        else:
          logger.debug("Кнопка 'close_banner' не найдена")

    # Пример использования для получения списка элементов
    locator_images = locators.get("additional_images_urls")
    if locator_images:
      images = get_element(driver, locator_images)
      if images:
        # TODO: действия со списком элементов
        ...
      else:
          logger.debug("Изображения 'additional_images_urls' не найдены")
```
```