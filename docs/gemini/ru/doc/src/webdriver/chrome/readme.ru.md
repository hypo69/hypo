# Chrome WebDriver для Selenium

## Обзор

Этот модуль предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определенные в файле `chrome.json`, такие как user-agent и настройки профиля браузера, для гибких и автоматизированных взаимодействий с браузером.

## Ключевые особенности

- Централизованная конфигурация: Конфигурация управляется через файл `chrome.json`.
- Множественные профили браузера: Поддерживает несколько профилей браузера для настройки различных параметров тестирования.
- Улучшенное логирование и обработка ошибок: Предоставляет подробные логи для инициализации, проблем с конфигурацией и ошибок WebDriver.

## Требования

Перед использованием убедитесь в установке следующих зависимостей:

- Python 3.x
- Selenium
- Fake User Agent
- Бинарник ChromeDriver (например, `chromedriver`)

Установите необходимые Python пакеты:

```bash
pip install selenium fake_useragent
```

Убедитесь, что бинарник `chromedriver` доступен в `PATH` или укажите его путь в конфигурации.

## Конфигурация

Конфигурация для Chrome WebDriver хранится в файле `chrome.json`.

### Пример конфигурации (`chrome.json`)

```json
{
  "options": {
    "log-level": "5",
    "disable-dev-shm-usage": "",
    "remote-debugging-port": "0",
    "arguments": [ "--kiosk", "--disable-gpu" ]
  },
  "disabled_options": { "headless": "" },
  "profile_directory": {
    "os": "%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data",
    "internal": "webdriver\\\\chrome\\\\profiles\\\\default",
    "testing": "%LOCALAPPDATA%\\\\Google\\\\Chrome for Testing\\\\User Data"
  },
  "binary_location": {
    "os": "C:\\\\Program Files\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
    "exe": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\chromedriver.exe",
    "binary": "bin\\\\webdrivers\\\\chrome\\\\125.0.6422.14\\\\win64-125.0.6422.14\\\\chrome-win64\\\\chrome.exe",
    "chromium": "bin\\\\webdrivers\\\\chromium\\\\chrome-win\\\\chrome.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "proxy_enabled": false
}
```

### Описание полей конфигурации

#### 1. `options`

Словарь параметров Chrome для изменения поведения браузера:

- **log-level**: Уровень логирования (5 - самый подробный).
- **disable-dev-shm-usage**: Отключает использование `/dev/shm` (Docker).
- **remote-debugging-port**: Порт для удаленной отладки. 0 - случайный порт.
- **arguments**: Аргументы командной строки для Chrome.

#### 2. `disabled_options`

Опции, явно отключенные. В данном примере отключен `headless` режим.

#### 3. `profile_directory`

Пути к директориям пользовательских данных Chrome.

#### 4. `binary_location`

Пути к бинарникам Chrome и ChromeDriver.

#### 5. `headers`

Пользовательские HTTP-заголовки.

#### 6. `proxy_enabled`

Включить/выключить прокси.

## Классы

### `Chrome`

**Описание**: Класс для управления Chrome WebDriver.  Использует паттерн Singleton для единственного экземпляра.

**Методы**:

- `__init__(self, user_agent=None)`: Инициализирует WebDriver. Если экземпляр уже существует, возвращает имеющийся.
- `get(self, url: str)`: Открывает веб-страницу.
- `quit(self)`: Закрывает браузер.


**Параметры**:

- `user_agent` (Optional[str], optional): Пользовательский User-Agent. По умолчанию `None`.

**Возвращает**:

-  (None):


**Вызывает исключения**:

- `Exception`: При возникновении любых ошибок.



## Использование

```python
from src.webdriver.chrome import Chrome

# Инициализация Chrome WebDriver с пользовательским user-agent
browser = Chrome(user_agent="Мой пользовательский User-Agent")

# Открытие веб-страницы
browser.get("https://www.example.com")

# Закрытие браузера
browser.quit()
```

## Логирование и отладка

Модуль использует `logger` из `src.logger` для логирования.


## Лицензия

Этот проект лицензирован на условиях MIT License.  См. файл [LICENSE](LICENSE).