# Модуль BeautifulSoup и XPath Parser

## Обзор

Этот модуль предоставляет пользовательскую реализацию для парсинга HTML-контента с использованием BeautifulSoup и XPath. Он позволяет получать HTML-контент из файлов или URL, парсить его и извлекать элементы с использованием XPath-локаторов.

## Подробнее

Модуль `src.webdriver.bs` предназначен для парсинга HTML-контента с использованием библиотек BeautifulSoup и XPath. Он обеспечивает возможность получения данных как из локальных файлов, так и из веб-ресурсов, а также позволяет извлекать элементы, используя XPath-локаторы. Централизованная конфигурация осуществляется через файл `bs.json`. Модуль включает функции для обработки ошибок и ведения детального логирования для облегчения отладки.

## Содержание

1.  [Основные характеристики](#основные-характеристики)
2.  [Требования](#требования)
3.  [Конфигурация](#конфигурация)
4.  [Использование](#использование)
5.  [Логирование и отладка](#логирование-и-отладка)
6.  [Лицензия](#лицензия)

## Основные характеристики

*   **HTML Parsing**: Использует BeautifulSoup и XPath для эффективного парсинга HTML.
*   **File and URL Support**: Поддерживает получение HTML-контента из локальных файлов или веб-URL.
*   **Custom Locators**: Позволяет определять пользовательские XPath-локаторы для извлечения элементов.
*   **Logging and Error Handling**: Предоставляет детальные логи для отладки и отслеживания ошибок.
*   **Configuration Support**: Централизованная конфигурация через файл `bs.json`.

## Требования

Перед использованием этого модуля убедитесь, что установлены следующие зависимости:

*   Python 3.x
*   BeautifulSoup
*   lxml
*   requests

Установите необходимые Python-зависимости:

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

URL по умолчанию для получения HTML-контента.

#### 2. `default_file_path`

Путь к файлу по умолчанию для получения HTML-контента.

#### 3. `default_locator`

Локатор по умолчанию для извлечения элементов:

*   **by**: Тип локатора (например, `ID`, `CSS`, `TEXT`).
*   **attribute**: Атрибут для поиска (например, `element_id`).
*   **selector**: XPath-селектор для извлечения элементов.

#### 4. `logging`

Настройки логирования:

*   **level**: Уровень логирования (например, `INFO`, `DEBUG`, `ERROR`).
*   **file**: Путь к файлу журнала.

#### 5. `proxy`

Настройки прокси-сервера:

*   **enabled**: Логическое значение, указывающее, следует ли использовать прокси.
*   **server**: Адрес прокси-сервера.
*   **username**: Имя пользователя для аутентификации прокси.
*   **password**: Пароль для аутентификации прокси.

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

# Инициализация парсера BS с URL по умолчанию
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

Парсер `BS` использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации. Все проблемы, возникающие во время инициализации, конфигурации или выполнения, будут залогированы для облегчения отладки.

### Примеры логов

*   **Ошибка во время инициализации**: `Error initializing BS parser: <error details>`
*   **Проблемы с конфигурацией**: `Error in bs.json file: <issue details>`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT. Подробности см. в файле [LICENSE](../../LICENSE).