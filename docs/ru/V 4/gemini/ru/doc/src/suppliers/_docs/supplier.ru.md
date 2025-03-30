# Модуль Supplier

## Обзор

Модуль `Supplier` предоставляет базовый класс для работы с поставщиками данных в приложении `hypotez`. Этот класс служит основой для создания специализированных классов, взаимодействующих с различными поставщиками, такими как Amazon, AliExpress и Walmart. Он содержит общие методы и атрибуты, которые могут быть переопределены в дочерних классах для реализации специфической логики взаимодействия с каждым поставщиком.

## Подробней

Класс `Supplier` предназначен для унификации процесса получения данных от различных поставщиков. Он обеспечивает загрузку конфигураций, инициализацию веб-драйвера, выполнение сценариев и парсинг данных. Это позволяет упростить и стандартизировать процесс интеграции с новыми поставщиками, а также повысить переиспользуемость кода.

## Классы

### `Supplier`

**Описание**:
Базовый класс для работы с поставщиками данных.

**Методы**:
- `__init__`: Конструктор класса, инициализирующий атрибуты на основе префикса поставщика и других параметров.
- `_payload`: Загружает настройки поставщика, конфигурационные файлы и инициализирует веб-драйвер.
- `login`: Метод для выполнения входа на сайт поставщика (если требуется).
- `run_scenario_files`: Запускает выполнение файлов сценариев.
- `run_scenarios`: Запускает один или несколько сценариев.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика, например, `'aliexpress'` или `'amazon'`.
- `locale` (str, optional): Код локализации, например, `'en'` для английского или `'ru'` для русского. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой `'default'`, экземпляром `Driver` или булевым значением. По умолчанию `'default'`.
- `*attrs`: Дополнительные атрибуты.
- `**kwargs`: Дополнительные именованные аргументы.

**Примеры**

```python
# Создаем объект для поставщика 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполняем вход на сайт поставщика
supplier.login()

# Запускаем сценарии из файлов
supplier.run_scenario_files(['example_scenario.json'])

# Или запускаем сценарии по определенным условиям
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Функции

### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """
    Args:
        supplier_prefix (str): Префикс поставщика, например, `'aliexpress'` или `'amazon'`.
        locale (str, optional): Код локализации, например, `'en'` для английского или `'ru'` для русского. По умолчанию `'en'`.
        webdriver (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой `'default'`, экземпляром `Driver` или булевым значением. По умолчанию `'default'`.
        *attrs: Дополнительные атрибуты.
        **kwargs: Дополнительные именованные аргументы.
    """
```

**Описание**:
Конструктор класса `Supplier`, инициализирует атрибуты на основе префикса поставщика, локали и веб-драйвера.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика, например, `'aliexpress'` или `'amazon'`.
- `locale` (str, optional): Код локализации, например, `'en'` для английского или `'ru'` для русского. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой `'default'`, экземпляром `Driver` или булевым значением. По умолчанию `'default'`.
- `*attrs`: Дополнительные атрибуты.
- `**kwargs`: Дополнительные именованные аргументы.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
```

### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """
    Args:
        webdriver (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой `'default'`, экземпляром `Driver` или булевым значением.
        *attrs: Дополнительные атрибуты.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        bool: Возвращает `True` в случае успешной загрузки конфигурации и инициализации веб-драйвера, `False` в противном случае.
    """
```

**Описание**:
Загружает настройки поставщика, конфигурационные файлы и инициализирует веб-драйвер.

**Параметры**:
- `webdriver` (str | Driver | bool): Веб-драйвер для взаимодействия с сайтом поставщика. Может быть строкой `'default'`, экземпляром `Driver` или булевым значением.
- `*attrs`: Дополнительные атрибуты.
- `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешной загрузки конфигурации и инициализации веб-драйвера, `False` в противном случае.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en')
result = supplier._payload(webdriver='chrome')
print(result)  # Вывод: True или False
```

### `login`

```python
def login(self) -> bool:
    """
    Returns:
        bool: Возвращает `True`, если вход на сайт выполнен успешно, `False` в противном случае.
    """
```

**Описание**:
Метод для выполнения входа на сайт поставщика (если требуется).

**Возвращает**:
- `bool`: Возвращает `True`, если вход на сайт выполнен успешно, `False` в противном случае.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en')
result = supplier.login()
print(result)  # Вывод: True или False
```

### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """
    Args:
        scenario_files (str | List[str], optional): Список файлов сценариев для выполнения. По умолчанию `None`.

    Returns:
        bool: Возвращает `True`, если выполнение сценариев из файлов завершено успешно, `False` в противном случае.
    """
```

**Описание**:
Запускает выполнение сценариев из указанных файлов.

**Параметры**:
- `scenario_files` (str | List[str], optional): Список файлов сценариев для выполнения. По умолчанию `None`.

**Возвращает**:
- `bool`: Возвращает `True`, если выполнение сценариев из файлов завершено успешно, `False` в противном случае.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en')
result = supplier.run_scenario_files(['example_scenario.json'])
print(result)  # Вывод: True или False
```

### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """
    Args:
        scenarios (dict | list[dict]): Список сценариев для выполнения.

    Returns:
        bool: Возвращает `True`, если выполнение сценариев завершено успешно, `False` в противном случае.
    """
```

**Описание**:
Запускает выполнение заданных сценариев.

**Параметры**:
- `scenarios` (dict | list[dict]): Список сценариев для выполнения.

**Возвращает**:
- `bool`: Возвращает `True`, если выполнение сценариев завершено успешно, `False` в противном случае.

**Примеры**:

```python
supplier = Supplier(supplier_prefix='aliexpress', locale='en')
result = supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
print(result)  # Вывод: True или False
```