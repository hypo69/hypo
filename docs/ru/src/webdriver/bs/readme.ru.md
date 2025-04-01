# Модуль парсера BeautifulSoup и XPath

## Обзор

Этот модуль предоставляет пользовательскую реализацию для парсинга HTML-контента с использованием библиотек BeautifulSoup и XPath. Он обеспечивает возможность загрузки HTML-контента из файлов или URL-адресов, его последующий парсинг и извлечение элементов с помощью XPath-локаторов. Модуль предназначен для упрощения и стандартизации процесса парсинга HTML в проекте `hypotez`.

## Подробнее

Модуль `src.webdriver.bs` предоставляет класс `BS` для парсинга HTML-контента. Он позволяет загружать HTML из различных источников, таких как файлы или URL-адреса, и извлекать необходимые элементы с использованием XPath-локаторов. Конфигурация модуля осуществляется через файл `bs.json`, что позволяет централизованно управлять параметрами парсинга.

## Функциональность и особенности

-   **Парсинг HTML**: Использует BeautifulSoup и XPath для эффективного парсинга HTML.
-   **Поддержка файлов и URL**: Загружает HTML-контент из локальных файлов или веб-адресов.
-   **Пользовательские локаторы**: Позволяет определять пользовательские XPath-локаторы для извлечения элементов.
-   **Логирование и обработка ошибок**: Предоставляет подробные логи для отладки и отслеживания ошибок.
-   **Поддержка конфигурации**: Централизованная конфигурация через файл `bs.json`.

## Использование

### Установка зависимостей

Перед использованием модуля необходимо установить следующие зависимости:

```bash
pip install beautifulsoup4 lxml requests
```

### Конфигурация (`bs.json`)

Пример конфигурационного файла:

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

Описание полей конфигурации:

1.  `default_url`: URL по умолчанию для загрузки HTML-контента.
2.  `default_file_path`: Путь к файлу по умолчанию для загрузки HTML-контента.
3.  `default_locator`: Локатор по умолчанию для извлечения элементов:

    *   `by`: Тип локатора (например, `ID`, `CSS`, `TEXT`).
    *   `attribute`: Атрибут для поиска (например, `element_id`).
    *   `selector`: XPath-селектор для извлечения элементов.
4.  `logging`: Настройки логирования:

    *   `level`: Уровень логирования (например, `INFO`, `DEBUG`, `ERROR`).
    *   `file`: Путь к файлу, куда будут записываться логи.
5.  `proxy`: Настройки прокси-сервера:

    *   `enabled`: Булевое значение, указывающее, следует ли использовать прокси.
    *   `server`: Адрес прокси-сервера.
    *   `username`: Имя пользователя для аутентификации на прокси-сервере.
    *   `password`: Пароль для аутентификации на прокси-сервере.
6.  `timeout`: Максимальное время ожидания для запросов (в секундах).
7.  `encoding`: Кодировка, используемая при чтении файлов или запросах.

### Примеры использования

#### Инициализация парсера `BS` с URL по умолчанию

```python
from src.webdriver.bs import BS
from types import SimpleNamespace
from src.utils.jjson import j_loads_ns
from pathlib import Path

# Загрузка настроек из конфигурационного файла
settings_path = Path('path/to/bs.json')
settings = j_loads_ns(settings_path)

# Инициализация парсера BS с URL по умолчанию
parser = BS(url=settings.default_url)

# Использование локатора по умолчанию из конфигурации
locator = SimpleNamespace(**settings.default_locator)
elements = parser.execute_locator(locator)
print(elements)
```

#### Загрузка HTML из файла

```python
parser = BS()
parser.get_url('file://path/to/your/file.html')
locator = SimpleNamespace(by='ID', attribute='element_id', selector='//*[@id="element_id"]')
elements = parser.execute_locator(locator)
print(elements)
```

#### Загрузка HTML из URL

```python
parser = BS()
parser.get_url('https://example.com')
locator = SimpleNamespace(by='CSS', attribute='class_name', selector='//*[contains(@class, "class_name")]')
elements = parser.execute_locator(locator)
print(elements)
```

## Логирование и отладка

Парсер `BS` использует `logger` из `src.logger` для логирования ошибок, предупреждений и общей информации. Все проблемы, возникающие при инициализации, конфигурации или выполнении, будут записываться в логи для удобства отладки.

### Примеры логов

*   **Ошибка при инициализации**: `Ошибка при инициализации парсера BS: <детали ошибки>`
*   **Проблемы с конфигурацией**: `Ошибка в файле bs.json: <детали проблемы>`

## Лицензия

Этот проект лицензирован на условиях MIT License. Подробности см. в файле [LICENSE](../../LICENSE).