# Firefox WebDriver

## Обзор

Этот код определяет подкласс `webdriver.Firefox` под названием `Firefox`. Он предоставляет дополнительные функции, такие как возможность запуска Firefox в режиме киоска и возможность настройки профиля Firefox для веб-драйвера.

## Класс: Firefox

### Атрибуты

- `driver_name`: Атрибут класса, установленный в значение `'firefox'`.

### Методы

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Инициализирует веб-драйвер Firefox с указанными параметрами запуска и профилем.

- **Параметры:**
  - `user_agent` (`dict`, optional): Словарь, содержащий настройки user agent. Если не указан, генерируется случайный user agent.

#### `_set_options(self, settings: SimpleNamespace) -> Options`

Устанавливает параметры запуска для веб-драйвера Firefox.

- **Параметры:**
  - `settings` (`SimpleNamespace`): Настройки для параметров Firefox.

- **Возвращает:**
  - `Options`: Объект Options с указанными параметрами запуска.

#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Настраивает профиль Firefox для веб-драйвера.

- **Параметры:**
  - `profile` (`SimpleNamespace`): Объект SimpleNamespace, содержащий настройки профиля.

- **Возвращает:**
  - `FirefoxProfile`: Объект FirefoxProfile, представляющий профиль.

## Использование

### Создание профиля с User Agent

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

### Настройка пути для загрузки файлов

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

## Примеры параметров

### Запуск в безголовом режиме

```python
options = Options()
options.headless = True
```

### Установка языка браузера

```python
options = Options()
options.add_argument('-lang=es')
```

### Пользовательские параметры командной строки

```python
options = Options()
options.add_argument('--some-option=value')
```

### Управление отладочными сообщениями

```python
options = Options()
options.add_argument('-vv')
```

### Запуск в полноэкранном режиме

```python
options = Options()
options.add_argument('--kiosk')
```

## Ссылки

- [Документация по настройкам профиля Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Документация по параметрам Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)