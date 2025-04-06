# Модуль для автоматического обновления и тестирования прокси-серверов
## Обзор

Модуль `auto_proxy.py` предназначен для автоматического получения, тестирования и обновления списка рабочих прокси-серверов. Он использует многопоточность для параллельной проверки прокси и поддерживает глобальный список `working_proxies`, который обновляется каждые 30 минут.

## Подробнее
Этот код важен для обеспечения надежной работы веб-приложений, требующих использования прокси-серверов, особенно в условиях блокировок или географических ограничений. Модуль автоматически поддерживает актуальный список рабочих прокси, что позволяет приложению продолжать функционировать без ручного вмешательства.

## Функции

### `fetch_proxies`

```python
def fetch_proxies() -> list:
    """Fetch a list of proxy servers from proxyscrape.com.

    Returns:
        list: A list of proxy servers in the format "IP:Port".
    """
```

**Назначение**: Получение списка прокси-серверов с сайта proxyscrape.com.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `list`: Список прокси-серверов в формате "IP:Port".

**Вызывает исключения**:
- Не обрабатывает исключения напрямую, но может возникнуть `requests.exceptions.RequestException` при неудачном запросе.

**Как работает функция**:
1. Функция отправляет GET-запрос на URL `https://www.proxy-list.download/api/v1/get?type=http`.
2. Если запрос успешен (код состояния 200), функция разбивает полученный текст на строки, удаляет последнюю пустую строку и возвращает список прокси-серверов.
3. В случае ошибки при запросе, выводит сообщение об ошибке и возвращает пустой список.

**Примеры**:
```python
proxies = fetch_proxies()
if proxies:
    print(f"Найдено {len(proxies)} прокси-серверов.")
else:
    print("Не удалось получить прокси-серверы.")
```

### `test_proxy`

```python
def test_proxy(proxy: str, prompt: str, timeout: int) -> None:
    """Test the given proxy server with a specified prompt and timeout.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
        prompt (str): The test prompt to be used for testing.
        timeout (int): The maximum time in seconds allowed for the test.
    """
```

**Назначение**: Проверка работоспособности прокси-сервера с заданным запросом и таймаутом.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".
- `prompt` (str): Тестовый запрос для проверки прокси.
- `timeout` (int): Максимальное время ожидания ответа в секундах.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Измеряет время выполнения запроса через прокси-сервер.
2.  `# res = gpt3.Completion.create(prompt=prompt, proxy=proxy)` -  закомментированная строка для отправки запроса к API GPT-3 (предположительно).
3. Если время ответа меньше заданного таймаута, добавляет прокси в список рабочих прокси.
4. В случае возникновения исключения во время проверки, пропускает прокси.

**Примеры**:
```python
test_proxy("127.0.0.1:8080", "Привет", 5)
```

### `add_working_proxy`

```python
def add_working_proxy(proxy: str) -> None:
    """Add a working proxy server to the global working_proxies list.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
    """
```

**Назначение**: Добавление рабочего прокси-сервера в глобальный список `working_proxies`.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Добавляет прокси в глобальный список `working_proxies`.

**Примеры**:
```python
add_working_proxy("127.0.0.1:8080")
```

### `remove_proxy`

```python
def remove_proxy(proxy: str) -> None:
    """Remove a proxy server from the global working_proxies list.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
    """
```

**Назначение**: Удаление прокси-сервера из глобального списка `working_proxies`.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Проверяет, присутствует ли прокси в списке `working_proxies`.
2. Если прокси присутствует, удаляет его из списка.

**Примеры**:
```python
remove_proxy("127.0.0.1:8080")
```

### `get_working_proxies`

```python
def get_working_proxies(prompt: str, timeout: int = 5) -> None:
    """Fetch and test proxy servers, adding working proxies to the global working_proxies list.

    Args:
        prompt (str): The test prompt to be used for testing.
        timeout (int, optional): The maximum time in seconds allowed for testing. Defaults to 5.
    """
```

**Назначение**: Получение и тестирование прокси-серверов, добавление рабочих прокси в глобальный список `working_proxies`.

**Параметры**:
- `prompt` (str): Тестовый запрос для проверки прокси.
- `timeout` (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию 5.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Получает список прокси-серверов с помощью функции `fetch_proxies`.
2. Создает и запускает потоки для параллельной проверки каждого прокси-сервера с использованием функции `test_proxy`.
3. Ожидает завершения всех потоков с заданным таймаутом.

**Примеры**:
```python
get_working_proxies("Привет", timeout=5)
```

### `update_working_proxies`

```python
def update_working_proxies() -> None:
    """Continuously update the global working_proxies list with working proxy servers."""
```

**Назначение**: Непрерывное обновление глобального списка `working_proxies` рабочими прокси-серверами.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Запускает бесконечный цикл.
2. Очищает список `working_proxies` перед обновлением.
3. Получает и тестирует прокси-серверы с помощью функции `get_working_proxies`.
4. Выводит сообщение "proxies updated".
5. Приостанавливает выполнение на 30 минут (1800 секунд).

**Примеры**:
```python
# Запуск в отдельном потоке для непрерывного обновления прокси
import threading
thread = threading.Thread(target=update_working_proxies)
thread.start()
```

### `get_random_proxy`

```python
def get_random_proxy() -> str:
    """Get a random working proxy server from the global working_proxies list.

    Returns:
        str: A random working proxy server in the format "IP:Port".
    """
```

**Назначение**: Получение случайного рабочего прокси-сервера из глобального списка `working_proxies`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `str`: Случайный рабочий прокси-сервер в формате "IP:Port".

**Как работает функция**:
1. Возвращает случайный элемент из списка `working_proxies` с помощью функции `random.choice`.

**Примеры**:
```python
proxy = get_random_proxy()
if proxy:
    print(f"Используем прокси: {proxy}")
else:
    print("Нет доступных рабочих прокси-серверов.")