# Описание JSON файла `pmi-rf.json`

## Обзор

Данный JSON файл содержит конфигурационные параметры для парсинга веб-сайта поставщика `ksp`. Он определяет основные настройки, такие как URL-адрес, правила обработки цен, количество товаров для очистки кэша и методы парсинга.

## Оглавление
1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
    - [Поля верхнего уровня](#поля-верхнего-уровня)
    - [Поле `scenarios`](#поле-scenarios)
3. [Пример использования](#пример-использования)

## Структура JSON

### Поля верхнего уровня

- `supplier` (str): Имя поставщика (`ksp`).
- `supplier_prefix` (str): Префикс поставщика (`ksp`).
- `start_url` (str): URL-адрес начальной страницы поставщика (`https://www.ksp.co.il/`).
- `price_rule` (str): Правило ценообразования (`+100`).
- `num_items_4_flush` (int): Количество товаров для очистки кеша (300).
- `if_login` (bool): Флаг, указывающий, требуется ли вход в систему (false).
- `parcing method [webdriver|api]` (str): Метод парсинга, используемый (`web`).
- `about method web scrapping [webdriver|api]` (str): Описание метода веб-парсинга (Если я работаю через API мне не нужен webdriver).
- `collect_products_from_categorypage` (bool): Флаг, указывающий, следует ли собирать продукты со страницы категории (false).
- `scenarios` (dict): Словарь, содержащий сценарии парсинга (пустой словарь `{}`).

### Поле `scenarios`

- `scenarios` (dict): Представляет собой словарь, который в данном случае пуст, но предназначен для хранения различных сценариев парсинга.
   В текущем файле не заданы сценарии парсинга.

## Пример использования

Этот файл используется для настройки парсера, предназначенного для сбора данных с веб-сайта ksp. Поля определяют основные параметры, необходимые для правильной работы парсера, такие как начальный URL, правила обработки цен и используемый метод парсинга (веб-скреппинг).