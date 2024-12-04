# Firefox WebDriver

## Overview

Этот код определяет подкласс `webdriver.Firefox`, называемый `Firefox`. Он предоставляет дополнительную функциональность, такую как возможность запуска Firefox в режиме киоска и настройку профиля Firefox для вебдрайвера.

## Классы

### `Firefox`

**Описание**: Подкласс `webdriver.Firefox`, предоставляющий расширенные возможности.

**Атрибуты**:

- `driver_name`: Классовый атрибут, установленный в `'firefox'`.


**Методы**:

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

Инициализирует вебдрайвер Firefox со заданными параметрами запуска и профилем.

- **Параметры**:
    - `user_agent` (`dict`, необязательно): Словарь, содержащий настройки пользовательского агента. Если не указан, генерируется случайный пользовательский агент.

#### `_set_options(self, settings: SimpleNamespace) -> Options`

Настраивает параметры запуска для вебдрайвера Firefox.

- **Параметры**:
    - `settings` (`SimpleNamespace`): Настройки параметров запуска Firefox.

- **Возвращает**:
    - `Options`: Объект `Options` с заданными параметрами запуска.


#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

Настраивает профиль Firefox для вебдрайвера.

- **Параметры**:
    - `profile` (`SimpleNamespace`): Объект `SimpleNamespace`, содержащий настройки профиля.

- **Возвращает**:
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

### Блокирование всплывающих окон

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

### Установка пути для загрузки файлов

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

## Примеры параметров запуска

### Запуск в бестелесном режиме (headless)

```python
options = Options()
options.headless = True
```

### Установка языка браузера

```python
options = Options()
options.add_argument('-lang=ru') # или другой язык
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

### Запуск в полноэкранном режиме

```python
options = Options()
options.add_argument('--kiosk')
```


## Обработка исключений

Обратите внимание на обработку исключений `WebDriverException` и `Exception`.  Этот код корректно ловит исключения и выводит соответствующие сообщения в лог.

## Ссылки

- [Документация по настройкам профиля Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Документация по параметрам запуска Firefox](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)