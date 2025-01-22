# Модуль BeautifulSoup и XPath парсера

## Обзор

Модуль предоставляет пользовательскую реализацию для разбора HTML-контента с использованием BeautifulSoup и XPath. Он позволяет получать HTML-контент из файлов или URL-адресов, анализировать его и извлекать элементы с помощью локаторов XPath.

## Основные особенности

-   **Разбор HTML**: Использует BeautifulSoup и XPath для эффективного разбора HTML.
-   **Поддержка файлов и URL-адресов**: Получает HTML-контент из локальных файлов или веб-URL-адресов.
-   **Пользовательские локаторы**: Позволяет определять пользовательские локаторы XPath для извлечения элементов.
-   **Логирование и обработка ошибок**: Предоставляет подробные журналы для отладки и отслеживания ошибок.
-   **Поддержка конфигурации**: Централизованная конфигурация через файл `bs.json`.

## Требования

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

-   Python 3.x
-   BeautifulSoup
-   lxml
-   requests

Установите необходимые зависимости Python:

```bash
pip install beautifulsoup4 lxml requests
```

## Конфигурация

Конфигурация для парсера `BS` хранится в файле `bs.json`. Ниже приведена примерная структура файла конфигурации и его описание:

### Пример конфигурации (`bs.json`)

```json
{
  "default_url": "https://example.com",
  "default_file_path": "file://path/to/your/file.html",
  "default_locator": {
    "by": "ID",
    "attribute": "element_id",
    "selector": "//*[@id='element_id']"
  },
  "logging": {
    "level": "INFO",
    "file": "logs/bs.log"
  },
  "proxy": {
    "enabled": false,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "timeout": 10,
  "encoding": "utf-8"
}
```

### Описание полей конфигурации

#### 1. `default_url`

URL-адрес по умолчанию для получения HTML-контента.

#### 2. `default_file_path`

Путь к файлу по умолчанию для получения HTML-контента.

#### 3. `default_locator`

Локатор по умолчанию для извлечения элементов:

-   **by**: Тип локатора (например, `ID`, `CSS`, `TEXT`).
-   **attribute**: Атрибут для поиска (например, `element_id`).
-   **selector**: Селектор XPath для извлечения элемента.

#### 4. `logging`

Настройки логирования:

-   **level**: Уровень логирования (например, `INFO`, `DEBUG`, `ERROR`).
-   **file**: Путь к файлу журнала.

#### 5. `proxy`

Настройки прокси-сервера:

-   **enabled**: Логическое значение, указывающее, следует ли использовать прокси.
-   **server**: Адрес прокси-сервера.
-   **username**: Имя пользователя для аутентификации прокси.
-   **password**: Пароль для аутентификации прокси.

#### 6. `timeout`

Максимальное время ожидания для запросов (в секундах).

#### 7. `encoding`

Кодировка, используемая при чтении файлов или выполнении запросов.

## Использование

Чтобы использовать парсер `BS` в своем проекте, просто импортируйте и инициализируйте его:

```python
from src.webdriver.bs import BS
from types import SimpleNamespace
from src.utils.jjson import j_loads_ns
from pathlib import Path

# Загрузка настроек из файла конфигурации
settings_path = Path('path/to/bs.json')
settings = j_loads_ns(settings_path)

# Инициализация парсера BS с URL-адресом по умолчанию
parser = BS(url=settings.default_url)

# Использование локатора по умолчанию из конфигурации
locator = SimpleNamespace(**settings.default_locator)
elements = parser.execute_locator(locator)
print(elements)
```

### Пример: Получение HTML из файла

```python
parser = BS()
parser.get_url('file://path/to/your/file.html')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
print(elements)
```

### Пример: Получение HTML из URL

```python
parser = BS()
parser.get_url('https://example.com')
locator = SimpleNamespace(by='CSS', attribute='class_name', selector='//*[contains(@class, "class_name")]')
elements = parser.execute_locator(locator)
print(elements)
```

## Логирование и отладка

Парсер `BS` использует `logger` из `src.logger` для регистрации ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, настройки или выполнения, будут регистрироваться для облегчения отладки.

### Примеры логов

-   **Ошибка при инициализации**: `Error initializing BS parser: <детали ошибки>`
-   **Проблемы с конфигурацией**: `Error in bs.json file: <детали проблемы>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](../../LICENSE).