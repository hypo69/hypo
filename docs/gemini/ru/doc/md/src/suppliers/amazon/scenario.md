# Модуль scenario.py

## Обзор

Этот модуль содержит сценарий для сбора данных о товарах с сайта Amazon. Он отвечает за получение списка категорий, списков товаров в каждой категории и извлечение данных о каждом товаре.

## Функции

### `get_list_products_in_category`

**Описание**: Функция собирает список ссылок на страницы товаров из страницы категории.

**Параметры**:

- `s` (Supplier): Экземпляр класса Supplier, содержащий информацию о поставщике и драйвер браузера.

**Возвращает**:

- `list[str,str,None]`: Список ссылок на страницы товаров, или `None`, если список пуст или произошла ошибка.

**Вызывает исключения**:

- `Exception`:  Возникает в случае необработанных ошибок.


## Константы

### `MODE`

**Описание**: Переменная, определяющая режим работы (например, 'dev', 'prod').

**Значение**: 'dev' по умолчанию.