# Firefox WebDriver

## Обзор

Этот код определяет подкласс `webdriver.Firefox` под названием `Firefox`. Он предоставляет дополнительные возможности, такие как запуск Firefox в режиме киоска и настройку профиля Firefox для веб-драйвера.

## Класс: Firefox

### Атрибуты

- `driver_name`: Классовый атрибут, установленный в `'firefox'`.

### Методы

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Инициализирует веб-драйвер Firefox со специфицированными параметрами запуска и профилем.

- **Параметры:**
    - `user_agent` (`dict`, необязательно): Словарь, содержащий настройки пользовательского агента. Если не указан, генерируется случайный пользовательский агент.


#### `_set_options(self, settings: SimpleNamespace) -> Options`

Устанавливает параметры запуска для веб-драйвера Firefox.

- **Параметры:**
    - `settings` (`SimpleNamespace`): Настройки параметров запуска Firefox.

- **Возвращает:**
    - `Options`: Объект `Options` с указанными параметрами запуска.


#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Настраивает профиль Firefox для веб-драйвера.

- **Параметры:**
    - `profile` (`SimpleNamespace`): Объект `SimpleNamespace`, содержащий настройки профиля.

- **Возвращает:**
    - `FirefoxProfile`: Объект `FirefoxProfile`, представляющий профиль.


## Использование

### Создание профиля с пользовательским агентом

```python
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "user-agent-string")
```

### Отключение изображений

```python
profile = FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
```

### Блокировка всплывающих окон

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

### Установка пути для скачиваемых файлов

```python
profile = FirefoxProfile()
profile.set_preference("browser.download.dir", "/path/to/download/folder")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
```

### Отключение уведомлений браузера

```python
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
```

## Примеры настроек запуска (`Options`)

### Запуск в бескамерном режиме (headless)

```python
options = Options()
options.headless = True
```

### Установка языка браузера

```python
options = Options()
options.add_argument('-lang=es')
```

### Настройка пользовательских параметров командной строки

```python
options = Options()
options.add_argument('--some-option=value')
```

### Управление сообщениями отладки

```python
options = Options()
options.add_argument('-vv')
```

### Запуск в полноэкранном режиме (kiosk)

```python
options = Options()
options.add_argument('--kiosk')
```


## Обработка исключений

Обратите внимание на блок `try...except WebDriverException as ex:` для правильной обработки возможных ошибок при запуске драйвера.

## Ссылки

- [Документация по настройкам профиля Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Документация по параметрам запуска Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)