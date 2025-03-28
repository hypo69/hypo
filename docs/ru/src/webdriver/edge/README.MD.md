# Модуль Edge WebDriver для Selenium

## Обзор

Модуль предоставляет пользовательскую реализацию Edge WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определенные в файле `edge.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкое и автоматизированное взаимодействие с браузером.

## Основные характеристики

- **Централизованная конфигурация**: Управление конфигурацией осуществляется через файл `edge.json`.
- **Множественные профили браузера**: Поддерживает несколько профилей браузера, что позволяет настраивать различные параметры для тестирования.
- **Улучшенное ведение журнала и обработка ошибок**: Предоставляет подробные журналы для инициализации, проблем с конфигурацией и ошибок WebDriver.
- **Возможность передачи пользовательских параметров**: Поддерживает передачу пользовательских параметров во время инициализации WebDriver.

## Требования

Перед использованием этого WebDriver убедитесь, что установлены следующие зависимости:

- Python 3.x
- Selenium
- Fake User Agent
- Бинарный файл Edge WebDriver (например, `msedgedriver`)

Установите необходимые зависимости Python:

```bash
pip install selenium fake_useragent
```

Кроме того, убедитесь, что бинарный файл `msedgedriver` доступен в `PATH` вашей системы, или укажите его путь в конфигурации.

## Конфигурация

Конфигурация для Edge WebDriver хранится в файле `edge.json`. Ниже приведен пример структуры файла конфигурации и его описание:

### Пример конфигурации (`edge.json`)

```json
{
  "options": [
    "--disable-dev-shm-usage",
    "--remote-debugging-port=0"
  ],
  "profiles": {
    "os": "%LOCALAPPDATA%\\\\Microsoft\\\\Edge\\\\User Data\\\\Default",
    "internal": "webdriver\\\\edge\\\\profiles\\\\default"
  },
  "executable_path": {
    "default": "webdrivers\\\\edge\\\\123.0.2420.97\\\\msedgedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
}
```

### Описание полей конфигурации

#### 1. `options`
Список аргументов командной строки, передаваемых в Edge. Примеры:
- `--disable-dev-shm-usage`: Отключает использование `/dev/shm` в контейнерах Docker (полезно для предотвращения ошибок в контейнерных средах).
- `--remote-debugging-port=0`: Устанавливает порт для удаленной отладки в Edge. Значение `0` означает, что будет назначен случайный порт.

#### 2. `profiles`
Пути к каталогам пользовательских данных Edge для различных сред:
- **os**: Путь к каталогу пользовательских данных по умолчанию (обычно для систем Windows).
- **internal**: Внутренний путь для профиля WebDriver по умолчанию.

#### 3. `executable_path`
Путь к бинарному файлу Edge WebDriver:
- **default**: Путь к бинарному файлу `msedgedriver.exe`.

#### 4. `headers`
Пользовательские HTTP-заголовки, используемые в запросах браузера:
- **User-Agent**: Устанавливает строку user-agent для браузера.
- **Accept**: Устанавливает типы данных, которые браузер готов принимать.
- **Accept-Charset**: Устанавливает кодировку символов, поддерживаемую браузером.
- **Accept-Encoding**: Устанавливает поддерживаемые методы кодирования (установите `none`, чтобы отключить).
- **Accept-Language**: Устанавливает предпочитаемые языки.
- **Connection**: Устанавливает тип соединения, который должен использовать браузер (например, `keep-alive`).

## Использование

Чтобы использовать `Edge` WebDriver в своем проекте, просто импортируйте и инициализируйте его:

```python
from src.webdriver.edge import Edge

# Инициализация Edge WebDriver с настройками user-agent и пользовательскими параметрами
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Открытие веб-сайта
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()
```

Класс `Edge` автоматически загружает настройки из файла `edge.json` и использует их для настройки WebDriver. Вы также можете указать пользовательский user-agent и передать дополнительные параметры во время инициализации WebDriver.

### Паттерн Singleton

`Edge` WebDriver использует паттерн Singleton. Это означает, что будет создан только один экземпляр WebDriver. Если экземпляр уже существует, будет повторно использован тот же экземпляр, и будет открыто новое окно.

## Ведение журнала и отладка

Класс WebDriver использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, конфигурации или выполнения, будут зарегистрированы для облегчения отладки.

### Пример журналов

- **Ошибка во время инициализации WebDriver**: `Error initializing Edge WebDriver: <детали ошибки>`
- **Проблемы конфигурации**: `Error in edge.json file: <детали проблемы>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности смотрите в файле [LICENSE](../../LICENSE).