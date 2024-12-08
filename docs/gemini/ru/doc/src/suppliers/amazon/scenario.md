# Модуль `hypotez/src/suppliers/amazon/scenario.py`

## Обзор

Данный модуль реализует сценарий сбора данных о товарах с сайта Amazon. Он предназначен для автоматизации процесса сбора информации о товарах из категорий.

## Постоянные переменные

### `MODE`

**Описание**: Переменная, хранящая режим работы (например, 'dev', 'prod').

**Значение**: `'dev'`

## Функции

### `get_list_products_in_category`

**Описание**: Функция собирает список ссылок на страницы товаров в заданной категории.  Функция обрабатывает страницу категории и возвращает список URL-адресов товаров.

**Параметры**:

- `s` (объект): Экземпляр класса поставщика (Supplier).  Необходимые данные для работы с сайтом должны быть доступны через объект.

**Возвращает**:

- `list[str, str, None]`: Список URL-адресов товаров в виде списка кортежей или None при ошибке.

**Вызывает исключения**:

- Не описаны


**Детали**:

Функция взаимодействует с веб-драйвером для получения ссылок на товары.  Важно отметить наличие обработки случаев, когда локаторы товаров отсутствуют или  получен неверный тип данных.  В коде присутствует логгирование (logger.error, logger.warning, logger.info).  В текущей реализации отсутствует обработка страниц категорий с пагинацией.  В коде есть комментарии, указывающие на необходимость реализации проверки наличия товара в базе данных.  Эта проверка ещё не реализована, но в будущем будет критично важна для избежания дублирования данных.