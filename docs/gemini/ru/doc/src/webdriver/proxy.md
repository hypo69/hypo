# Модуль `proxy.py`

## Обзор

Модуль `proxy.py` предоставляет функции для работы с прокси-серверами. Он позволяет загружать список прокси из внешнего источника, парсить его и проверять работоспособность.

## Функции

### `download_proxies_list`

**Описание**: Загружает файл с прокси-серверами из указанного URL и сохраняет его на диск.

**Параметры**:

- `url` (str, optional): URL файла для загрузки. По умолчанию `https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt`.
- `save_path` (Path, optional): Путь для сохранения загруженного файла. По умолчанию `src/webdriver/proxies.txt`.

**Возвращает**:

- `bool`: `True`, если загрузка успешна, иначе `False`.

**Вызывает исключения**:

- `RequestException`: Ошибки при работе с HTTP запросом.
- Другие ошибки:  Общий класс ошибок при выполнении запроса и сохранении файла.

### `get_proxies_dict`

**Описание**: Парсит файл с прокси-адресами и распределяет их по протоколам (http, socks4, socks5).

**Параметры**:

- `file_path` (Path, optional): Путь к файлу с прокси-адресами. По умолчанию `src/webdriver/proxies.txt`.

**Возвращает**:

- `Dict[str, List[Dict[str, Any]]]`: Словарь, где ключи - типы протоколов (http, socks4, socks5), а значения - списки словарей, содержащих информацию о каждом прокси (protocol, host, port).

**Вызывает исключения**:

- `FileNotFoundError`: Если указанный файл не найден.
- Другие ошибки:  Общий класс ошибок при чтении файла и парсинге данных.

### `check_proxy`

**Описание**: Проверяет работоспособность заданного прокси-сервера.

**Параметры**:

- `proxy` (dict): Словарь, содержащий данные о прокси (protocol, host, port).

**Возвращает**:

- `bool`: `True`, если прокси работает, иначе `False`.

**Вызывает исключения**:

- `ProxyError`: Ошибка при использовании прокси-сервера.
- `RequestException`: Ошибка при отправке запроса.


## Использование

Пример использования функций модуля:

```python
if __name__ == '__main__':
    # Загрузка списка прокси и парсинг
    if download_proxies_list():
        parsed_proxies = get_proxies_dict()
        logger.info(f'Обработано {sum(len(v) for v in parsed_proxies.values())} прокси.')

        # Проверка работоспособности прокси
        for protocol in parsed_proxies:
            for proxy in parsed_proxies[protocol]:
                if check_proxy(proxy):
                    print(f"Прокси {proxy['protocol']}://{proxy['host']}:{proxy['port']} работает.")
```


```python

```
```