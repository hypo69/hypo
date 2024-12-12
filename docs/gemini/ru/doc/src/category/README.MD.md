# Модуль `src.category`

## Обзор

Модуль `Category` предоставляет функциональность для работы с категориями товаров, в основном для PrestaShop. Он предлагает инструменты для взаимодействия с данными категорий, включая сканирование страниц категорий и управление иерархическими структурами категорий.

## Оглавление

- [Класс: `Category`](#класс-category)
  - [Конструктор: `__init__`](#конструктор-__init__)
  - [Метод: `get_parents`](#метод-get_parents)
  - [Метод: `crawl_categories_async`](#метод-crawl_categories_async)
  - [Метод: `crawl_categories`](#метод-crawl_categories)
  - [Метод: `_is_duplicate_url`](#метод-_is_duplicate_url)
- [Функция: `compare_and_print_missing_keys`](#функция-compare_and_print_missing_keys)
- [Пример использования](#пример-использования)
- [Зависимости](#зависимости)

## Класс: `Category`

Класс `Category` наследуется от `PrestaCategory` и отвечает за обработку категорий продуктов, получение родительских категорий и рекурсивное сканирование страниц категорий.

### Конструктор: `__init__`

**Описание**: Инициализирует объект `Category`.

**Параметры**:
- `api_credentials` (dict): API-ключи для доступа к данным категорий.
- `args`: Переменное количество позиционных аргументов (не используется).
- `kwargs`: Переменное количество ключевых аргументов (не используется).

### Метод: `get_parents`

**Описание**: Извлекает список родительских категорий.

**Параметры**:
- `id_category` (int): ID категории, для которой нужно извлечь родителей.
- `dept` (int): Глубина уровня категории.

**Возвращает**:
- `list`: Список родительских категорий.

### Метод: `crawl_categories_async`

**Описание**: Асинхронно сканирует категории, строя иерархический словарь.

**Параметры**:
- `url` (str): URL страницы категории.
- `depth` (int): Глубина рекурсии сканирования.
- `driver` (selenium.webdriver.remote.webdriver.WebDriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath-локатор для ссылок категорий.
- `dump_file` (str): Путь к JSON-файлу для сохранения результатов.
- `default_category_id` (int): ID категории по умолчанию.
- `category` (Optional[dict], optional): Существующий словарь категорий (по умолчанию `None`).

**Возвращает**:
- `dict`: Обновленный или новый словарь категорий.

### Метод: `crawl_categories`

**Описание**: Рекурсивно сканирует категории и строит иерархический словарь.

**Параметры**:
- `url` (str): URL страницы для сканирования.
- `depth` (int): Глубина рекурсии.
- `driver` (selenium.webdriver.remote.webdriver.WebDriver): Экземпляр Selenium WebDriver.
- `locator` (str): XPath-локатор для поиска ссылок на категории.
- `dump_file` (str): Файл для сохранения иерархического словаря.
- `id_category_default` (int): ID категории по умолчанию.
- `category` (dict, optional): Словарь категорий (по умолчанию пустой).

**Возвращает**:
- `dict`: Иерархический словарь категорий и их URL-адресов.

### Метод: `_is_duplicate_url`

**Описание**: Проверяет, существует ли URL-адрес уже в словаре категорий.

**Параметры**:
- `category` (dict): Словарь категорий.
- `url` (str): URL-адрес для проверки.

**Возвращает**:
- `bool`: `True`, если URL является дубликатом, `False` в противном случае.

## Функция: `compare_and_print_missing_keys`

**Описание**: Сравнивает текущий словарь с данными из файла и выводит любые отсутствующие ключи.

**Параметры**:
- `current_dict` (dict): Словарь для сравнения.
- `file_path` (str): Путь к файлу, содержащему данные для сравнения.

## Пример использования

```python
from src.category import Category
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


async def main():
    # Инициализация WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    driver = webdriver.Chrome(options=chrome_options)


    # Инициализируем Category с ключами API
    category = Category(api_credentials={'api_key': 'your_api_key'})

    # Получаем родительские категории
    parents = category.get_parents(id_category=123, dept=2)

    # Асинхронное сканирование категорий
    category_data = await category.crawl_categories_async(
        url='https://example.com/categories',
        depth=3,
        driver=driver,
        locator='//a[@class="category-link"]',
        dump_file='categories.json',
        default_category_id=123
    )

    # Сравниваем текущие данные категорий с файлом и выводим отсутствующие ключи
    compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')

    driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
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