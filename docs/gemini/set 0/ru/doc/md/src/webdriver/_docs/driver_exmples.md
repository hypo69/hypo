# Примеры использования драйвера

## Обзор

Этот файл предоставляет примеры использования классов `Driver` и `Chrome` для управления веб-драйвером.  Он демонстрирует различные функции, включая навигацию по URL, извлечение домена, сохранение куки, обновление страницы, прокрутку, получение языка страницы, настройку User-Agent, поиск элементов и получение текущего URL.

## Оглавление

* [Примеры использования драйвера](#примеры-использования-драйвера)
* [Функции](#функции)
* [Примечания](#примечания)


## Примеры использования драйвера

Эти примеры показывают практическое применение методов класса `Driver` и `Chrome`.

### Создание экземпляра Chrome драйвера и навигация по URL

```python
from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By

chrome_driver = Driver(Chrome)
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")
```

**Описание:** Создает экземпляр драйвера Chrome и пытается перейти по указанному URL. Выводит сообщение об успехе или отсутствии.

**Возвращает:** `True` если навигация успешна, `False` в противном случае.


### Извлечение домена из URL

```python
domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
print(f"Extracted domain: {domain}")
```

**Описание:** Извлекает доменное имя из предоставленного URL.

**Параметры:**
- `url` (str): URL для извлечения домена.


**Возвращает:**
- `str`: Доменное имя.

**Возможные исключения:**  Никаких, предполагается, что входной `url` валиден.


### Сохранение cookies в локальный файл

```python
success = chrome_driver._save_cookies_localy()
if success:
    print("Cookies were saved successfully")
```

**Описание:** Сохраняет cookies в локальный файл.

**Возвращает:** `True` если сохранение прошло успешно, `False` в противном случае.

**Примечание:** Подробности о формате файла и пути к нему должны быть описаны в global settings (`gs`).


### Обновление текущей страницы

```python
if chrome_driver.page_refresh():
    print("Page was refreshed successfully")
```

**Описание:** Обновляет текущую страницу в браузере.

**Возвращает:** `True` если обновление прошло успешно, `False` в противном случае.


### Прокрутка страницы вниз

```python
if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
    print("Successfully scrolled the page down")
```

**Описание:** Прокручивает страницу вниз на заданное количество раз.

**Параметры:**
- `scrolls` (int): Количество прокруток.
- `direction` (str): Направление прокрутки ('forward' или 'backward').
- `frame_size` (int): Размер кадра прокрутки.
- `delay` (int): Задержка между прокрутками.

**Возвращает:** `True` если прокрутка прошла успешно, `False` в противном случае.


### Получение языка текущей страницы

```python
page_language = chrome_driver.locale
print(f"Page language: {page_language}")
```

**Описание:** Возвращает язык текущей страницы.

**Возвращает:** `str`: Язык страницы.


### Установка кастомного User-Agent для Chrome драйвера

```python
user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
if custom_chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL with custom user agent")
```

**Описание:** Создает экземпляр драйвера Chrome с заданным User-Agent.

**Параметры:**
- `user_agent` (dict): Словарь с пользовательским User-Agent.

**Возвращает:** `True` если навигация прошла успешно, `False` в противном случае.


### Поиск элемента по CSS селектору

```python
element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
if element:
    print(f"Found element with text: {element.text}")
```

**Описание:** Ищет элемент по заданному CSS селектору.

**Параметры:**
- `by` (By): Тип селектора (By.CSS_SELECTOR).
- `selector` (str): CSS селектор.


**Возвращает:** `WebElement` если элемент найден, `None` в противном случае.

**Возможные исключения:** `NoSuchElementException` если элемент не найден.


### Получение текущего URL

```python
current_url = chrome_driver.current_url
print(f"Current URL: {current_url}")
```

**Описание:** Возвращает текущий URL.

**Возвращает:** `str`: Текущий URL.


### Фокусировка окна

```python
chrome_driver.window_focus()
print("Focused the window")
```

**Описание:** Переводит фокус на окно драйвера.


## Функции

Этот раздел описывает функции, используемые в примерах.

### `main`

**Описание:** Основная функция для демонстрации примеров использования классов `Driver` и `Chrome`.

**Возвращает:** `None`



## Примечания

- Убедитесь, что установлены все необходимые зависимости, включая `selenium`, `fake_useragent` и модули, используемые в примерах.
- Конфигурация файла настроек (`gs`) должна содержать необходимые пути к файлам и ресурсам.


```