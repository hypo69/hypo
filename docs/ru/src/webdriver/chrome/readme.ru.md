# Документация для модуля `src.webdriver.chrome`

## Обзор

Модуль предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он интегрирует настройки конфигурации, определённые в файле `chrome.json`, такие как user-agent и настройки профиля браузера, чтобы обеспечить гибкие и автоматизированные взаимодействия с браузером.

## Подробнее

Модуль `src.webdriver.chrome` предоставляет возможность централизованного управления конфигурацией Chrome WebDriver через файл `chrome.json`. Это позволяет легко настраивать различные параметры, такие как user-agent, опции запуска браузера и пути к бинарным файлам. Интеграция с системой логирования `src.logger` обеспечивает удобный мониторинг и отладку процесса инициализации и работы драйвера.

## Классы

### `Chrome`

**Описание**: Класс `Chrome` предоставляет кастомную реализацию Chrome WebDriver с использованием Selenium. Он управляет конфигурацией WebDriver на основе файла `chrome.json` и предоставляет возможность передачи пользовательских опций.

**Принцип работы**: Класс использует паттерн Singleton, чтобы гарантировать создание только одного экземпляра WebDriver. Он загружает конфигурацию из файла `chrome.json`, применяет её для настройки WebDriver и предоставляет методы для управления браузером.

**Методы**:
- `__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None)`: Инициализирует экземпляр класса `Chrome`.
- `__new__(cls, *args, **kwargs)`: Реализует паттерн Singleton для класса `Chrome`.

#### `__init__`

```python
def __init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None):
    """Инициализирует экземпляр класса Chrome.

    Args:
        user_agent (Optional[str], optional): User-Agent, который будет использоваться в браузере. Defaults to None.
        options (Optional[List[str]], optional): Список дополнительных опций для запуска Chrome. Defaults to None.
    """
    ...
```

**Назначение**: Инициализирует экземпляр класса `Chrome`, загружает конфигурацию из `chrome.json`, настраивает опции Chrome и создает экземпляр WebDriver.

**Параметры**:
- `user_agent` (Optional[str]): User-Agent, который будет использоваться в браузере. По умолчанию `None`.
- `options` (Optional[List[str]]): Список дополнительных опций для запуска Chrome. По умолчанию `None`.

**Как работает функция**:
1. Загружает конфигурацию из файла `chrome.json`, используя функцию `j_loads` из модуля `src.config_reader`.
2. Инициализирует логгер из модуля `src.logger.logger`.
3. Определяет путь к профилю Chrome на основе операционной системы.
4. Создает объект опций Chrome (`webdriver.ChromeOptions`).
5. Добавляет аргументы из конфигурации (`chrome.json`) к опциям Chrome.
6. Устанавливает местоположение бинарного файла Chrome.
7. Если указан `user_agent`, устанавливает его в опциях Chrome. Если `user_agent` не указан, пытается получить его из конфигурации.
8. Добавляет пользовательские опции, если они указаны.
9. Создает экземпляр Chrome WebDriver с заданными опциями.
10. Настраивает размер окна браузера.
11. Логирует информацию об успешной инициализации WebDriver.
12. Если возникают исключения в процессе инициализации, логирует ошибку.

```
Загрузка конфигурации из chrome.json  -->  Инициализация логгера  -->  Определение пути к профилю  -->  Создание объекта опций Chrome  -->  Добавление аргументов из конфигурации  -->  Установка местоположения бинарного файла Chrome  -->  Установка User-Agent  -->  Добавление пользовательских опций  -->  Создание экземпляра Chrome WebDriver  -->  Настройка размера окна браузера  -->  Логирование информации об успешной инициализации/ошибках
```

#### `__new__`

```python
def __new__(cls, *args, **kwargs):
    """Реализует паттерн Singleton для класса Chrome."""
    ...
```

**Назначение**: Реализует паттерн Singleton, чтобы гарантировать, что у класса `Chrome` будет только один экземпляр.

**Параметры**:
- `cls`: Ссылка на класс.
- `*args`: Произвольные позиционные аргументы.
- `**kwargs`: Произвольные именованные аргументы.

**Возвращает**:
- Единственный экземпляр класса `Chrome`.

**Как работает функция**:
1. Проверяет, существует ли уже экземпляр класса (`cls._instance`).
2. Если экземпляр не существует, создает новый экземпляр и сохраняет его в `cls._instance`.
3. Возвращает существующий экземпляр, если он уже был создан.

```
Проверка существования экземпляра класса  -->  Создание нового экземпляра (если не существует)  -->  Возврат существующего экземпляра
```

## Функции

В данном модуле функции отсутствуют.