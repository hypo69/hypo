# Модуль для работы с JavaScript в Selenium WebDriver
## Обзор

Модуль `src.webdriver.js` предназначен для расширения возможностей Selenium WebDriver путем добавления функций JavaScript для взаимодействия с веб-страницами. Он включает в себя функции для управления видимостью элементов DOM, получения информации о странице и управления фокусом браузера.

## Подробнее

Этот модуль предоставляет класс `JavaScript`, который содержит методы для выполнения JavaScript-кода в контексте текущей веб-страницы, управляемой Selenium WebDriver. Это позволяет автоматизировать задачи, которые сложно выполнить стандартными средствами Selenium.

## Классы

### `JavaScript`

**Описание**: Предоставляет набор утилит JavaScript для взаимодействия с веб-страницей.

**Принцип работы**: Класс инициализируется экземпляром Selenium WebDriver. Методы класса позволяют выполнять JavaScript-код для управления видимостью элементов, получения информации о состоянии документа и управления фокусом окна браузера.

**Методы**:
- `__init__`: Инициализирует класс `JavaScript` экземпляром WebDriver.
- `unhide_DOM_element`: Делает невидимый DOM-элемент видимым.
- `ready_state`: Возвращает статус загрузки документа.
- `window_focus`: Устанавливает фокус на окно браузера.
- `get_referrer`: Возвращает URL-адрес реферера текущего документа.
- `get_page_lang`: Возвращает язык текущей страницы.

### `__init__`
```python
    def __init__(self, driver: WebDriver):
        """Initializes the JavaScript helper with a Selenium WebDriver instance.

        Args:
            driver (WebDriver): Selenium WebDriver instance to execute JavaScript.
        """
        self.driver = driver
```
**Назначение**: Инициализирует экземпляр класса `JavaScript` с использованием переданного экземпляра `WebDriver`.

**Параметры**:
- `driver` (WebDriver): Экземпляр `WebDriver`, который будет использоваться для выполнения JavaScript-кода.

**Как работает функция**:
1. Функция принимает экземпляр `WebDriver` в качестве аргумента.
2. Сохраняет переданный экземпляр `WebDriver` в атрибуте `self.driver` для дальнейшего использования в методах класса.

```
A[Принимает экземпляр WebDriver]
|
B[Сохраняет экземпляр WebDriver в атрибуте self.driver]
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

# Пример использования с Chrome
driver = webdriver.Chrome()
js_utils = JavaScript(driver)

# Пример использования с Firefox
driver = webdriver.Firefox()
js_utils = JavaScript(driver)
```

### `unhide_DOM_element`
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
- `element` (WebElement): Объект `WebElement`, который нужно сделать видимым.

**Возвращает**:
- `bool`: `True`, если скрипт выполнен успешно, `False` в противном случае.

**Как работает функция**:
1. Функция принимает объект `WebElement` в качестве аргумента.
2. Определяет JavaScript-код, который изменяет свойства стиля элемента, чтобы сделать его видимым (opacity = 1, transform = 'translate(0px, 0px) scale(1)').
3. Пытается выполнить JavaScript-код с помощью метода `execute_script` объекта `self.driver`, передавая элемент в качестве аргумента скрипта.
4. Если выполнение скрипта проходит успешно, возвращает `True`.
5. Если во время выполнения скрипта возникает исключение, логирует ошибку и возвращает `False`.

```
A[Принимает объект WebElement]
|
B[Определяет JavaScript-код для изменения свойств стиля элемента]
|
C[Пытается выполнить JavaScript-код]
|
D[Если успешно: возвращает True, иначе: логирует ошибку и возвращает False]
```

**Примеры**:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)

# Находим невидимый элемент (например, с opacity: 0)
element = driver.find_element(By.ID, "hiddenElement")

# Делаем элемент видимым
if js_utils.unhide_DOM_element(element):
    print("Элемент успешно сделан видимым")
else:
    print("Не удалось сделать элемент видимым")
```

### `ready_state`
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
1. Функция пытается выполнить JavaScript-код `return document.readyState;` с помощью метода `execute_script` объекта `self.driver`.
2. Возвращает результат выполнения скрипта, который представляет собой строку, указывающую статус загрузки документа.
3. Если во время выполнения скрипта возникает исключение, логирует ошибку и возвращает пустую строку.

```
A[Пытается выполнить JavaScript-код для получения статуса загрузки документа]
|
B[Если успешно: возвращает статус, иначе: логирует ошибку и возвращает пустую строку]
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)

# Получаем статус загрузки документа
ready_state = js_utils.ready_state
print(f"Статус загрузки документа: {ready_state}")
```

### `window_focus`
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
**Назначение**: Устанавливает фокус на окно браузера с помощью JavaScript.

**Как работает функция**:
1. Функция пытается выполнить JavaScript-код `window.focus();` с помощью метода `execute_script` объекта `self.driver`.
2. Если во время выполнения скрипта возникает исключение, логирует ошибку.

```
A[Пытается выполнить JavaScript-код для установки фокуса на окно браузера]
|
B[Если возникает исключение: логирует ошибку]
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)

# Устанавливаем фокус на окно браузера
js_utils.window_focus()
```

### `get_referrer`
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
**Назначение**: Извлекает URL-адрес реферера текущего документа.

**Возвращает**:
- `str`: URL-адрес реферера или пустую строку, если он недоступен.

**Как работает функция**:
1. Функция пытается выполнить JavaScript-код `return document.referrer;` с помощью метода `execute_script` объекта `self.driver`.
2. Возвращает результат выполнения скрипта, который представляет собой URL-адрес реферера. Если реферер отсутствует, возвращает пустую строку.
3. Если во время выполнения скрипта возникает исключение, логирует ошибку и возвращает пустую строку.

```
A[Пытается выполнить JavaScript-код для получения URL-адреса реферера]
|
B[Если успешно: возвращает URL-адрес реферера, иначе: логирует ошибку и возвращает пустую строку]
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)

# Получаем URL-адрес реферера
referrer = js_utils.get_referrer()
print(f"URL-адрес реферера: {referrer}")
```

### `get_page_lang`
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
1. Функция пытается выполнить JavaScript-код `return document.documentElement.lang;` с помощью метода `execute_script` объекта `self.driver`.
2. Возвращает результат выполнения скрипта, который представляет собой код языка страницы. Если язык не определен, возвращает пустую строку.
3. Если во время выполнения скрипта возникает исключение, логирует ошибку и возвращает пустую строку.

```
A[Пытается выполнить JavaScript-код для получения языка страницы]
|
B[Если успешно: возвращает код языка, иначе: логирует ошибку и возвращает пустую строку]
```

**Примеры**:
```python
from selenium import webdriver
from src.webdriver.js import JavaScript

driver = webdriver.Chrome()
driver.get("https://example.com")
js_utils = JavaScript(driver)

# Получаем язык страницы
page_lang = js_utils.get_page_lang()
print(f"Язык страницы: {page_lang}")