# Модуль aliexpress

## Обзор

Модуль `aliexpress` предоставляет класс `Aliexpress`, который объединяет функциональность классов `Supplier`, `AliRequests` и `AliApi` для работы с AliExpress. Он позволяет взаимодействовать с AliExpress как через requests, так и через webdriver.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации взаимодействия с платформой AliExpress. Он предоставляет инструменты для выполнения запросов к API AliExpress, обработки ответов и выполнения других задач, связанных с этим поставщиком. Модуль позволяет работать с AliExpress в различных режимах, включая использование веб-драйвера для эмуляции действий пользователя и режим запросов напрямую к API.

## Классы

### `Aliexpress`

**Описание**: Базовый класс для работы с AliExpress.

**Наследует**:
- `Supplier`: Предоставляет общую функциональность для работы с поставщиками.
- `AliRequests`: Отвечает за выполнение HTTP-запросов к AliExpress.
- `AliApi`: Предоставляет методы для взаимодействия с API AliExpress.

**Аттрибуты**:
- Отсутствуют, класс объединяет функциональность родительских классов.

**Методы**:
- `__init__`: Инициализирует класс `Aliexpress`.

### `Aliexpress.__init__`

```python
def __init__(self, 
             webdriver: bool | str = False, 
             locale: str | dict = {'EN': 'USD'},
             *args, **kwargs):
    """
    Initialize the Aliexpress class.

    :param webdriver: Webdriver mode. Supported values are:
        - `False` (default): No webdriver.
        - `'chrome'`: Use the Chrome webdriver.
        - `'mozilla'`: Use the Mozilla webdriver.
        - `'edge'`: Use the Edge webdriver.
        - `'default'`: Use the system's default webdriver.
    :type webdriver: bool | str

    :param locale: The language and currency settings for the script.
    :type locale: str | dict

    :param args: Additional positional arguments.
    :param kwargs: Additional keyword arguments.

    **Examples**:

    .. code-block:: python

        # Run without a webdriver
        a = Aliexpress()

        # Webdriver `Chrome`
        a = Aliexpress('chrome')

    """
    ...
    super().__init__(supplier_prefix = 'aliexpress', 
                     locale = locale, 
                     webdriver = webdriver, 
                     *args, **kwargs)
```

**Назначение**: Инициализирует экземпляр класса `Aliexpress`, настраивая режим работы (с веб-драйвером или без), локаль и другие параметры.

**Параметры**:
- `webdriver` (bool | str): Определяет режим работы с веб-драйвером. Возможные значения:
    - `False` (по умолчанию): Без веб-драйвера.
    - `'chrome'`: Использовать Chrome webdriver.
    - `'mozilla'`: Использовать Mozilla webdriver.
    - `'edge'`: Использовать Edge webdriver.
    - `'default'`: Использовать системный веб-драйвер по умолчанию.
- `locale` (str | dict): Языковые и валютные настройки для скрипта.
- `*args`: Дополнительные позиционные аргументы.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- None

**Вызывает исключения**:
- Нет информации об исключениях в предоставленном коде.

**Как работает функция**:

1.  Инициализация класса `Aliexpress`: Функция `__init__` инициализирует объект класса `Aliexpress`.
2.  Настройка режима веб-драйвера: В зависимости от значения параметра `webdriver`, класс настраивается на работу с использованием веб-драйвера (Chrome, Mozilla, Edge или системный по умолчанию) или без него.
3.  Установка локали: Устанавливаются языковые и валютные настройки на основе параметра `locale`.
4.  Вызов конструктора родительского класса: Вызывается конструктор класса `Supplier` с параметрами `supplier_prefix`, `locale` и `webdriver`, а также с дополнительными позиционными и именованными аргументами.

```
Инициализация Aliexpress
↓
Определение режима веб-драйвера
↓
Установка локали
↓
Вызов конструктора Supplier
```

**Примеры**:

```python
# Run without a webdriver
a = Aliexpress()

# Webdriver `Chrome`
a = Aliexpress('chrome')