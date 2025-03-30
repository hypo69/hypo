# Модуль `crawlee_python`

## Обзор

Модуль `crawlee_python` предоставляет интеграцию с библиотекой Crawlee для Python. Он содержит класс `CrawleePython`, который упрощает использование Crawlee в проекте `hypotez` для задач веб-скрапинга и автоматизации.

## Подробней

Этот модуль предназначен для упрощения работы с Crawlee, предоставляя готовый к использованию класс `CrawleePython`. Это позволяет стандартизировать и упростить процесс сбора данных с веб-страниц, а также автоматизировать взаимодействие с веб-сайтами.

## Классы

### `CrawleePython`

**Описание**:
Класс `CrawleePython` предоставляет методы для настройки и запуска Crawlee-пауков.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `CrawleePython`.

**Параметры**:
- Нет явных параметров, но класс может принимать параметры конфигурации через методы.

**Примеры**:
```python
from src.webdriver.crawlee_python import CrawleePython

crawler = CrawleePython()
# crawler.run()  # Пример запуска (требуется дополнительная реализация)
```

## Функции

### `CrawleePython`

```python
from .crawlee_python import CrawleePython
```

**Описание**: Функция импортирует класс `CrawleePython` из модуля `.crawlee_python`.

**Параметры**: Нет параметров.

**Возвращает**:  `None`.

**Вызывает исключения**:  `None`.

**Примеры**:
```python
from .crawlee_python import CrawleePython

crawler = CrawleePython()