# Примеры использования драйвера

## Обзор

Данный файл содержит примеры использования классов `Driver` и `Chrome` для управления веб-драйвером. Он демонстрирует различные методы, включая навигацию по URL, извлечение домена, сохранение cookies, обновление страницы, прокрутку, получение языка страницы, установку пользовательского агента, поиск элементов, получение текущего URL и фокусировку окна.

## Оглавление

* [Примеры использования драйвера](#примеры-использования-драйвера)
* [Примечания](#примечания)

## Примеры использования драйвера

### `main` функция

**Описание**: Основная функция, демонстрирующая примеры использования классов `Driver` и `Chrome`.

**Подробности**: Функция `main` содержит примеры использования различных методов класса `Driver`.

**Примеры**:


#### Создание экземпляра Chrome драйвера и навигация по URL

```python
chrome_driver = Driver(Chrome)
if chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL")
```

**Описание**: Создает экземпляр драйвера Chrome и переходит на указанный URL.


#### Извлечение домена из URL

```python
domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")
print(f"Extracted domain: {domain}")
```

**Описание**: Извлекает доменную часть из предоставленного URL.


#### Сохранение cookies в локальный файл

```python
success = chrome_driver._save_cookies_localy()
if success:
    print("Cookies were saved successfully")
```

**Описание**: Сохраняет cookies в локальный файл.


#### Обновление текущей страницы

```python
if chrome_driver.page_refresh():
    print("Page was refreshed successfully")
```

**Описание**: Обновляет текущую страницу.


#### Прокрутка страницы вниз

```python
if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):
    print("Successfully scrolled the page down")
```

**Описание**: Прокручивает страницу вниз на заданное количество скроллов.


#### Получение языка текущей страницы

```python
page_language = chrome_driver.locale
print(f"Page language: {page_language}")
```

**Описание**: Получает язык текущей страницы.


#### Установка кастомного User-Agent для Chrome драйвера

```python
user_agent = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
custom_chrome_driver = Driver(Chrome, user_agent=user_agent)
if custom_chrome_driver.get_url("https://www.example.com"):
    print("Successfully navigated to the URL with custom user agent")
```

**Описание**: Устанавливает пользовательский агент для драйвера Chrome.


#### Поиск элемента по CSS селектору

```python
element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
if element:
    print(f"Found element with text: {element.text}")
```

**Описание**: Ищет элемент на странице по CSS селектору.


#### Получение текущего URL

```python
current_url = chrome_driver.current_url
print(f"Current URL: {current_url}")
```

**Описание**: Получает текущий URL страницы.


#### Фокусировка окна

```python
chrome_driver.window_focus()
print("Focused the window")
```

**Описание**: Фокусирует окно драйвера.


## Примечания

* Убедитесь, что у вас установлены необходимые зависимости, такие как `selenium`, `fake_useragent`, и модули, указанные в импортах.
* Параметры `scrolls`, `direction`, `frame_size` и `delay` в методе `scroll` должны быть корректными для вашей задачи.
* Пути к файлам настроек и другим ресурсам должны быть нанесены в глобальные настройки (`gs`).