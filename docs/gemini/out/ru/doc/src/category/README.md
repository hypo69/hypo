# Модуль: Category

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями продуктов, в основном для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая сканирование страниц категорий и управление иерархической структурой категорий.


## Класс: `Category`

Класс `Category` наследуется от `PrestaCategory` и отвечает за обработку категорий продуктов, получение родительских категорий и рекурсивное сканирование страниц категорий.


### Конструктор: `__init__(self, api_credentials, *args, **kwargs)`

Инициализирует объект `Category`.

#### Аргументы:
- `api_credentials`: Данные для доступа к данным о категориях.
- `args`: Список аргументов переменной длины (не используется).
- `kwargs`: Словарь ключевых аргументов (не используется).


### Метод: `get_parents(self, id_category, dept)`

Возвращает список родительских категорий.

#### Аргументы:
- `id_category`: ID категории, для которой нужно получить родителей.
- `dept`: Уровень глубины категории.

#### Возвращает:
- Список родительских категорий.


### Метод: `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`

Асинхронно сканирует категории, создавая иерархический словарь.

#### Аргументы:
- `url`: URL страницы категории.
- `depth`: Глубина рекурсии сканирования.
- `driver`: Экземпляр Selenium WebDriver.
- `locator`: XPath локатор для ссылок на категории.
- `dump_file`: Путь к файлу JSON для сохранения результатов.
- `default_category_id`: ID по умолчанию для категории.
- `category`: (Необязательно) Существующий словарь категории (по умолчанию `None`).

#### Возвращает:
- Обновленный или новый словарь категории.


### Метод: `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`

Рекурсивно сканирует категории и создаёт иерархический словарь.

#### Аргументы:
- `url`: URL страницы для сканирования.
- `depth`: Глубина рекурсии.
- `driver`: Экземпляр Selenium WebDriver.
- `locator`: XPath локатор для нахождения ссылок на категории.
- `dump_file`: Файл для сохранения иерархического словаря.
- `id_category_default`: ID категории по умолчанию.
- `category`: Словарь категории (по умолчанию пустой).

#### Возвращает:
- Иерархический словарь категорий и их URL.


### Метод: `_is_duplicate_url(self, category, url)`

Проверяет, существует ли URL уже в словаре категории.

#### Аргументы:
- `category`: Словарь категории.
- `url`: URL для проверки.

#### Возвращает:
- `True`, если URL дублируется, `False` в противном случае.


## Функция: `compare_and_print_missing_keys(current_dict, file_path)`

Сравнивает текущий словарь с данными из файла и выводит отсутствующие ключи.

### Аргументы:
- `current_dict`: Словарь для сравнения.
- `file_path`: Путь к файлу с данными для сравнения.


## Пример использования

```python
from src.category import Category

# Инициализация Category с данными API
category = Category(api_credentials={'api_key': 'your_api_key'})

# Получение родителей категории
parents = category.get_parents(id_category=123, dept=2)

# Асинхронное сканирование категорий
category_data = await category.crawl_categories_async(
    url='https://example.com/categories',
    depth=3,
    driver=driver_instance,
    locator='//a[@class="category-link"]',
    dump_file='categories.json',
    default_category_id=123
)

# Сравнение текущих данных категории с файлом и вывод отсутствующих ключей
compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
```

## Зависимости

- `requests`
- `lxml`
- `asyncio`
- `selenium`
- `src.endpoints.prestashop.PrestaShop`
- `src.endpoints.prestashop.PrestaCategory`
- `src.utils.jjson.j_loads`
- `src.utils.jjson.j_dumps`
- `src.logger.logger`