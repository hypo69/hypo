# Модуль `js`

## Обзор

Модуль `js` предоставляет JavaScript утилиты для взаимодействия с веб-страницей. Он разработан для расширения возможностей Selenium WebDriver путем добавления функций на основе JavaScript для взаимодействия с веб-страницами, включая манипуляции видимостью, получение информации о странице и управление фокусом браузера.

## Подробней

Модуль содержит класс `JavaScript`, который инкапсулирует методы для выполнения JavaScript-кода в контексте веб-страницы, управляемой Selenium WebDriver. Это позволяет автоматизировать задачи, которые сложно или невозможно выполнить стандартными средствами Selenium.

## Классы

### `JavaScript`

**Описание**: Предоставляет JavaScript утилиты для взаимодействия с веб-страницей.

**Принцип работы**:
Класс инициализируется экземпляром `WebDriver` и предоставляет методы для выполнения JavaScript-кода в контексте текущей веб-страницы. Это позволяет изменять свойства элементов DOM, получать информацию о странице и управлять поведением браузера.

**Аттрибуты**:
- `driver` (WebDriver): Экземпляр Selenium WebDriver, используемый для выполнения JavaScript.

**Методы**:
- `unhide_DOM_element`: Делает невидимый DOM-элемент видимым.
- `ready_state`: Получает статус загрузки документа.
- `window_focus`: Устанавливает фокус на окно браузера.
- `get_referrer`: Получает URL-адрес referrer текущего документа.
- `get_page_lang`: Получает язык текущей страницы.

## Функции

### `JavaScript.__init__`

```python
def __init__(self, driver: WebDriver):
    """Initializes the JavaScript helper with a Selenium WebDriver instance.

    Args:
        driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
    """
    self.driver = driver
```

**Назначение**: Инициализирует класс `JavaScript` с экземпляром `WebDriver`.

**Параметры**:
- `driver` (WebDriver): Экземпляр Selenium WebDriver, который будет использоваться для выполнения JavaScript-кода.

**Как работает функция**:
1. Функция принимает экземпляр `WebDriver` в качестве аргумента.
2. Сохраняет переданный экземпляр `WebDriver` в атрибуте `self.driver` класса `JavaScript`.

```
A [Инициализация JavaScript]
|
B [Сохранение драйвера]
|
C [Конец]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)
```

### `JavaScript.unhide_DOM_element`

```python
def unhide_DOM_element(self, element: WebElement) -> bool:
    """Makes an invisible DOM element visible by modifying its style properties.

    Args:
        element (WebElement): The WebElement object to make visible.

    Returns:
        bool: True if the script executes successfully, False otherwise.
    """
    script = """
    arguments[0].style.opacity = 1;
    arguments[0].style.transform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.MozTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.WebkitTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.msTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].style.OTransform = 'translate(0px, 0px) scale(1)';
    arguments[0].scrollIntoView(true);
    return true;
    """
    try:
        self.driver.execute_script(script, element)
        return True
    except Exception as ex:
        logger.error('Error in unhide_DOM_element: %s', ex)
        return False
```

**Назначение**: Делает невидимый DOM-элемент видимым, изменяя его свойства стиля.

**Параметры**:
- `element` (WebElement): Объект WebElement, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

**Как работает функция**:
1. Определяет JavaScript-скрипт, который изменяет свойства стиля элемента, чтобы сделать его видимым.
2. Выполняет JavaScript-скрипт с помощью `driver.execute_script`, передавая элемент в качестве аргумента.
3. Перехватывает возможные исключения, логирует ошибку и возвращает `False` в случае неудачи.

```
A [Unhide DOM element]
|
B [Execute script: change element style]
|
C [Check result]
|
D [Return status]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)

# Поиск невидимого элемента (пример)
invisible_element = driver.find_element("id", "invisible_element")

# Сделать элемент видимым
success = js_helper.unhide_DOM_element(invisible_element)
if success:
    print("Элемент успешно сделан видимым")
else:
    print("Не удалось сделать элемент видимым")
```

### `JavaScript.ready_state`

```python
@property
def ready_state(self) -> str:
    """Retrieves the document loading status.

    Returns:
        str: 'loading' if the document is still loading, 'complete' if loading is finished.
    """
    try:
        return self.driver.execute_script('return document.readyState;')
    except Exception as ex:
        logger.error('Error retrieving document.readyState: %s', ex)
        return ''
```

**Назначение**: Извлекает статус загрузки документа.

**Возвращает**:
- `str`: `'loading'`, если документ все еще загружается, `'complete'`, если загрузка завершена.

**Как работает функция**:
1. Выполняет JavaScript-скрипт `return document.readyState;`, чтобы получить текущий статус загрузки документа.
2. Перехватывает возможные исключения, логирует ошибку и возвращает пустую строку в случае неудачи.

```
A [Ready state request]
|
B [Execute script: get document.readyState]
|
C [Check result]
|
D [Return status]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)

# Получение статуса загрузки документа
ready_state = js_helper.ready_state
print(f"Статус загрузки документа: {ready_state}")
```

### `JavaScript.window_focus`

```python
def window_focus(self) -> None:
    """Sets focus to the browser window using JavaScript.

    Attempts to bring the browser window to the foreground.
    """
    try:
        self.driver.execute_script('window.focus();')
    except Exception as ex:
        logger.error('Error executing window.focus(): %s', ex)
```

**Назначение**: Устанавливает фокус на окно браузера, используя JavaScript.

**Как работает функция**:
1. Выполняет JavaScript-скрипт `window.focus();`, чтобы установить фокус на текущее окно браузера.
2. Перехватывает возможные исключения и логирует ошибку.

```
A [Window focus request]
|
B [Execute script: window.focus()]
|
C [Check result]
|
D [Return]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)

# Установка фокуса на окно браузера
js_helper.window_focus()
print("Фокус установлен на окно браузера")
```

### `JavaScript.get_referrer`

```python
def get_referrer(self) -> str:
    """Retrieves the referrer URL of the current document.

    Returns:
        str: The referrer URL, or an empty string if unavailable.
    """
    try:
        return self.driver.execute_script('return document.referrer;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.referrer: %s', ex)
        return ''
```

**Назначение**: Извлекает URL-адрес referrer текущего документа.

**Возвращает**:
- `str`: URL-адрес referrer или пустую строку, если он недоступен.

**Как работает функция**:
1. Выполняет JavaScript-скрипт `return document.referrer;`, чтобы получить URL-адрес referrer.
2. Возвращает полученный URL-адрес или пустую строку, если referrer не установлен.
3. Перехватывает возможные исключения, логирует ошибку и возвращает пустую строку в случае неудачи.

```
A [Get referrer request]
|
B [Execute script: get document.referrer]
|
C [Check result]
|
D [Return referrer url]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)

# Получение URL-адреса referrer
referrer = js_helper.get_referrer()
print(f"URL-адрес referrer: {referrer}")
```

### `JavaScript.get_page_lang`

```python
def get_page_lang(self) -> str:
    """Retrieves the language of the current page.

    Returns:
        str: The language code of the page, or an empty string if unavailable.
    """
    try:
        return self.driver.execute_script('return document.documentElement.lang;') or ''
    except Exception as ex:
        logger.error('Error retrieving document.documentElement.lang: %s', ex)
        return ''
```

**Назначение**: Извлекает язык текущей страницы.

**Возвращает**:
- `str`: Код языка страницы или пустую строку, если он недоступен.

**Как работает функция**:
1. Выполняет JavaScript-скрипт `return document.documentElement.lang;`, чтобы получить код языка страницы.
2. Возвращает полученный код языка или пустую строку, если он не установлен.
3. Перехватывает возможные исключения, логирует ошибку и возвращает пустую строку в случае неудачи.

```
A [Get page language request]
|
B [Execute script: get document.documentElement.lang]
|
C [Check result]
|
D [Return page language]
```

**Примеры**:

```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Создание экземпляра WebDriver (пример с Chrome)
driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Создание экземпляра JavaScript helper
js_helper = JavaScript(driver)

# Получение языка страницы
page_lang = js_helper.get_page_lang()
print(f"Язык страницы: {page_lang}")