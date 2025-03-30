# Модуль `bangood`

## Обзор

Модуль `bangood` предназначен для взаимодействия с сайтом Banggood, включая сбор данных о категориях и товарах. Он содержит классы и функции для выполнения задач парсинга и извлечения информации с сайта Banggood.

## Подробней

Этот модуль предоставляет функциональность для автоматизированного сбора данных с сайта Banggood. Он включает в себя граббер (`Graber`) для обработки веб-страниц и сценарии (`get_list_categories_from_site`, `get_list_products_in_category`) для извлечения списков категорий и товаров. Модуль позволяет автоматизировать процесс мониторинга и анализа данных о товарах, доступных на Banggood.

## Функции

### `get_list_categories_from_site`

```python
def get_list_categories_from_site(url: str, grabber: Graber) -> list[str]:
    """
    Извлекает список категорий с сайта Banggood.

    Args:
        url (str): URL сайта Banggood.
        grabber (Graber): Экземпляр класса Graber для выполнения HTTP-запросов.

    Returns:
        list[str]: Список URL категорий.
    """
```

**Описание**: Извлекает список URL категорий с сайта Banggood, используя предоставленный URL и граббер.

**Параметры**:
- `url` (str): URL сайта Banggood.
- `grabber` (Graber): Экземпляр класса `Graber` для выполнения HTTP-запросов.

**Возвращает**:
- `list[str]`: Список URL категорий.

**Примеры**:
```python
from src.suppliers.bangood import get_list_categories_from_site, Graber
url = 'https://www.banggood.com'
grabber = Graber()
categories = get_list_categories_from_site(url, grabber)
print(categories)
```

### `get_list_products_in_category`

```python
def get_list_products_in_category(url: str, grabber: Graber) -> list[str]:
    """
    Извлекает список товаров в заданной категории на сайте Banggood.

    Args:
        url (str): URL категории на сайте Banggood.
        grabber (Graber): Экземпляр класса Graber для выполнения HTTP-запросов.

    Returns:
        list[str]: Список URL товаров в категории.
    """
```

**Описание**: Извлекает список URL товаров в заданной категории на сайте Banggood, используя предоставленный URL и граббер.

**Параметры**:
- `url` (str): URL категории на сайте Banggood.
- `grabber` (Graber): Экземпляр класса `Graber` для выполнения HTTP-запросов.

**Возвращает**:
- `list[str]`: Список URL товаров в категории.

**Примеры**:
```python
from src.suppliers.bangood import get_list_products_in_category, Graber
url = 'https://www.banggood.com/category'
grabber = Graber()
products = get_list_products_in_category(url, grabber)
print(products)
```

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для выполнения HTTP-запросов и получения данных с веб-сайтов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.
- `get`: Выполняет GET-запрос к указанному URL.

**Параметры**:
- Нет параметров для инициализации.

**Примеры**:
```python
from src.suppliers.bangood import Graber

grabber = Graber()
response = grabber.get('https://www.banggood.com')
print(response.text)
```