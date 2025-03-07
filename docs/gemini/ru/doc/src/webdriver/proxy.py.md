# Модуль для работы с прокси

## Обзор

Модуль определяет функции для загрузки и парсинга списка прокси.
Загружается текстовый файл с прокси-адресами и распределяется по категориям.

## Оглавление
1. [Функции](#Функции)
    - [`download_proxies_list`](#download_proxies_list)
    - [`get_proxies_dict`](#get_proxies_dict)
    - [`check_proxy`](#check_proxy)

## Функции

### `download_proxies_list`

**Описание**: Загружает файл по указанному URL и сохраняет его в заданный путь.

**Параметры**:
- `url` (str): URL файла для загрузки. По умолчанию: `https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt`.
- `save_path` (Path): Путь для сохранения загруженного файла. По умолчанию: `hypotez/src/webdriver/proxies.txt`.

**Возвращает**:
- `bool`: `True`, если загрузка и сохранение файла прошли успешно, `False` в противном случае.

### `get_proxies_dict`

**Описание**: Парсит файл с прокси-адресами и распределяет их по категориям (http, socks4, socks5).

**Параметры**:
- `file_path` (Path): Путь к файлу с прокси. По умолчанию: `hypotez/src/webdriver/proxies.txt`.

**Возвращает**:
- `Dict[str, List[Dict[str, Any]]]`: Словарь, где ключи - это типы прокси (`http`, `socks4`, `socks5`), а значения - списки словарей с данными прокси (`protocol`, `host`, `port`).

**Вызывает исключения**:
- `FileNotFoundError`: Если файл по указанному пути не найден.
- `Exception`: В случае ошибки во время парсинга прокси.

### `check_proxy`

**Описание**: Проверяет работоспособность прокси-сервера, отправляя запрос на `https://httpbin.org/ip`.

**Параметры**:
- `proxy` (dict): Словарь с данными прокси (`protocol`, `host`, `port`).

**Возвращает**:
- `bool`: `True`, если прокси работает, `False` в противном случае.

**Вызывает исключения**:
- `ProxyError`: Если возникает ошибка при подключении через прокси.
- `RequestException`: Если возникает ошибка во время выполнения запроса.