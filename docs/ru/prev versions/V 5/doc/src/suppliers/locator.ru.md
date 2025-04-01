# Локаторы полей на `HTML`-странице

## Обзор

Этот файл содержит описание структуры и принципов работы с локаторами элементов на веб-странице. Локаторы используются для поиска и взаимодействия с элементами на странице с помощью WebDriver. Описание предназначено для разработчиков, работающих с проектом `hypotez`, и содержит подробную информацию о формате и использовании локаторов.

## Содержание

- [Пример локатора](#пример-локатора)
- [Детали](#детали)
- [Описание ключей локатора](#описание-ключей-локатора)
- [Сложные локаторы](#сложные-локаторы)

## Пример локатора

Здесь представлен пример структуры локатора, используемого для определения элементов на `HTML`-странице:

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

## Детали

Имя каждого словаря должно соответствовать имени поля класса `ProductFields`.

Пример использования локаторов для заполнения полей класса `ProductFields`:

```python
f = ProductFields(
    name = d.execute_locator('name'),
    price = d.execute_locator('price'),
    ...
)
```

Также можно создавать локаторы для выполнения дополнительных действий на странице, например, для закрытия баннеров.

### Ключи словаря локатора

- **`attribute`**: Атрибут веб-элемента, который необходимо получить (например, `innerText`, `src`, `id`, `href`). Если значение установлено в `none/false`, WebDriver вернет весь `WebElement`.
- **`by`**: Стратегия поиска элемента:
  - `ID` соответствует `By.ID`
  - `NAME` соответствует `By.NAME`
  - `CLASS_NAME` соответствует `By.CLASS_NAME`
  - `TAG_NAME` соответствует `By.TAG_NAME`
  - `LINK_TEXT` соответствует `By.LINK_TEXT`
  - `PARTIAL_LINK_TEXT` соответствует `By.PARTIAL_LINK_TEXT`
  - `CSS_SELECTOR` соответствует `By.CSS_SELECTOR`
  - `XPATH` соответствует `By.XPATH`
- **`selector`**: Селектор для определения местоположения веб-элемента. Примеры:
  - `(//li[@class = 'slide selected previous'])[1]//img`
  - `//a[@id = 'mainpic']//img`
  - `//span[@class = 'ltr sku-copy']`
- **`if_list`**: Определяет, что делать со списком найденных элементов:
  - `first`: выбрать первый элемент.
  - `all`: выбрать все элементы.
  - `last`: выбрать последний элемент.
  - `even`, `odd`: выбрать четные/нечетные элементы.
  - Указание конкретных номеров, например, `1,2,...` или `[1,3,5]`: выбрать элементы с указанными номерами.
  - Альтернативный способ — указать номер элемента прямо в селекторе, например: `(//div[contains(@class, 'description')])[2]//p`
- **`use_mouse`**: `true` | `false`. Указывает, следует ли использовать мышь для выполнения действий.
- **`event`**: Действие, которое WebDriver может выполнить с веб-элементом, например, `click()`, `screenshot()`, `scroll()` и т.д. Важно: Если указан `event`, он будет выполнен **до** получения значения из `attribute`.
  Пример:
  ```json
  {
      ...,
      "attribute": "href",
      ...,
      "timeout": 0,
      "timeout_for_event": "presence_of_element_located",
      "event": "click()",
      ...
  }
  ```
  В этом случае сначала драйвер выполнит `click()` на веб-элементе, а затем получит его атрибут `href`. Принцип работы: **действие -> атрибут**.  Другие примеры событий:
    - `screenshot()`: возвращает веб-элемент в виде снимка экрана (PNG в формате `bytes`).
    - `send_message()`: отправляет сообщение веб-элементу. Рекомендуется использовать переменную `%EXTERNAL_MESSAGE%`.
    Пример:
    ```json
    {"timeout": 0, 
    "timeout_for_event": "presence_of_element_located", 
    "event": "click();backspace(10);%EXTERNAL_MESSAGE%"
    }
    ```
    Эта последовательность выполняет:
    1. `click()` - нажимает на веб-элемент.
    2. `backspace(10)` - сдвигает каретку на 10 символов влево (очищает текст в поле ввода).
    3. `%EXTERNAL_MESSAGE%` - отправляет сообщение в поле ввода.
- **`mandatory`**: Указывает, является ли локатор обязательным. Если `true`, и взаимодействие с элементом невозможно, код вызовет ошибку. Если `false`, элемент будет пропущен.
- **`locator_description`**: Описание локатора.

## Сложные локаторы

В ключи локатора можно передавать списки, кортежи или словари для более гибкой настройки поиска элементов.

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
      "true",
      "true"
    ],
    "locator_description": [
      "Нажимаю на вкладку для открытия поля description.",
      "Читаю данные из div."
    ]
  }
```

В этом примере сначала будет найден элемент `//a[contains(@href, '#tab-description')]`. Драйвер выполнит команду `click()`, затем получит значение атрибута `href` элемента `//a[contains(@href, '#tab-description')]`.

### Пример локатора со словарём:

```json
"sample_locator": {
  "attribute": {"href": "name"},
  ...
}
```

## Описание ключей локатора

1. **`attribute`**:
   Указывает атрибут элемента для поиска. Если значение `null`, атрибут не используется для поиска.

2. **`by`**:
   Указывает метод поиска элемента на странице. В данном случае `'XPATH'`, что означает использование XPath.

3. **`selector`**:
   Строка, представляющая локатор (XPath выражение) для поиска элемента. Например, `"//a[@id = 'mainpic']//img"` ищет изображение внутри тега `a` с `id='mainpic'`.

4. **`if_list`**:
   Правило обработки списка элементов. `'first'` означает, что будет возвращен первый элемент из списка.

5. **`use_mouse`**:
   Булевое значение, указывающее, нужно ли использовать мышь для взаимодействия с элементом. `false` означает, что мышь не используется.

6. **`timeout`**:
   Время ожидания (в секундах) для нахождения элемента. `0` означает, что поиск будет выполнен немедленно.

7. **`timeout_for_event`**:
   Время ожидания для события. `"presence_of_element_located"` означает, что WebDriver будет ожидать появления элемента перед выполнением события.

8. **`event`**:
   Действие, которое должно быть выполнено с найденным элементом. Например, `click()` для клика или `screenshot()` для создания скриншота.

9. **`mandatory`**:
   Указывает, является ли локатор обязательным. Если `true`, и элемент не найден, будет вызвана ошибка.

10. **`locator_description`**:
    Описание того, что делает локатор, чтобы помочь в понимании его цели.

## Полезные советы

Разметка страницы может меняться в зависимости от версии (например, десктопная/мобильная). Рекомендуется хранить несколько файлов локаторов для каждой версии. Например: `product.json`, `product_mobile_site.json`.

По умолчанию локаторы читаются из файла `product.json`. Вот как можно это изменить:

В файле грабера страницы поставщика делается проверка на `url`:

```python
async def grab_page(self) -> ProductFields:
    ...
    d = driver
    if 'ksp.co.il/mob' in d.current_url:  # <- бывает, что подключается к мобильной версии сайта
        self.locator = j_loads_ns(gs.path.src / 'suppliers' / 'ksp' / 'locators' / 'product_mobile_site.json')
    ...
```