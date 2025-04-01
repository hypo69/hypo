# Модуль для автоматического обновления прокси-серверов

## Обзор

Модуль `auto_proxy.py` предназначен для автоматического получения, тестирования и обновления списка рабочих прокси-серверов. Это позволяет использовать прокси для обхода ограничений доступа или анонимизации запросов. Модуль включает функции для получения списка прокси, проверки их работоспособности, добавления и удаления прокси из списка рабочих, а также для периодического обновления этого списка.

## Подробней

Этот модуль важен для поддержания актуального списка рабочих прокси-серверов, которые могут использоваться для различных целей, например, для доступа к веб-сайтам, которые могут быть заблокированы в определенном регионе, или для повышения конфиденциальности при отправке запросов. Он автоматически обновляет список прокси, что позволяет избежать необходимости вручную искать и проверять прокси-серверы.

## Функции

### `fetch_proxies`

```python
def fetch_proxies():
    """Fetch a list of proxy servers from proxyscrape.com.

    Returns:
        list: A list of proxy servers in the format "IP:Port".
    """
```

**Назначение**: Получает список прокси-серверов с сайта proxyscrape.com.

**Возвращает**:
- `list`: Список прокси-серверов в формате "IP:Port".

**Как работает функция**:
1.  Формирует URL для запроса списка прокси-серверов.
2.  Отправляет GET-запрос к указанному URL.
3.  Если запрос выполнен успешно (status code 200), разделяет полученный текст на строки, удаляя последнюю пустую строку.
4.  В случае ошибки при запросе выводит сообщение об ошибке и возвращает пустой список.

```ascii
    Fetch Proxies
    |
    ---> GET request to proxyscrape.com
    |
    ---> Split response text into list of proxies
    |
    Return: list of proxies
```

**Примеры**:
```python
proxies = fetch_proxies()
if proxies:
    print(f"Found {len(proxies)} proxies.")
else:
    print("No proxies found.")
```

### `test_proxy`

```python
def test_proxy(proxy, prompt, timeout):
    """Test the given proxy server with a specified prompt and timeout.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
        prompt (str): The test prompt to be used for testing.
        timeout (int): The maximum time in seconds allowed for the test.
    """
```

**Назначение**: Проверяет работоспособность прокси-сервера, отправляя запрос и измеряя время ответа.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".
- `prompt` (str): Тестовый запрос для проверки прокси.
- `timeout` (int): Максимальное время ожидания ответа в секундах.

**Как работает функция**:
1.  Измеряет время начала выполнения теста.
2.  Пытается выполнить запрос через прокси-сервер. <Инструкция для модели gemini: здесь должен быть код для отправки запроса через прокси, но он закомментирован. Необходимо добавить описание этого шага, как если бы код был активен.>
3.  Измеряет время окончания выполнения теста.
4.  Вычисляет время ответа.
5.  Если время ответа меньше заданного таймаута, добавляет прокси в список рабочих прокси.
6.  В случае возникновения исключения во время теста, просто пропускает его.

```ascii
    Test Proxy
    |
    ---> Measure start time
    |
    ---> Send request via proxy  <Инструкция для модели gemini: здесь должен быть код для отправки запроса через прокси>
    |
    ---> Measure end time
    |
    ---> Calculate response time
    |
    ---> Check if response time < timeout
    |   |
    |   Yes
    |   |
    |   ---> Add proxy to working_proxies
    |
    No
    |
    ---> Pass
```

**Примеры**:
```python
test_proxy("127.0.0.1:8080", "Test prompt", 5)
```

### `add_working_proxy`

```python
def add_working_proxy(proxy):
    """Add a working proxy server to the global working_proxies list.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
    """
```

**Назначение**: Добавляет рабочий прокси-сервер в глобальный список `working_proxies`.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".

**Как работает функция**:
1.  Добавляет прокси в глобальный список `working_proxies`.

```ascii
    Add Working Proxy
    |
    ---> Add proxy to working_proxies
```

**Примеры**:
```python
add_working_proxy("127.0.0.1:8080")
```

### `remove_proxy`

```python
def remove_proxy(proxy):
    """Remove a proxy server from the global working_proxies list.

    Args:
        proxy (str): The proxy server in the format "IP:Port".
    """
```

**Назначение**: Удаляет прокси-сервер из глобального списка `working_proxies`.

**Параметры**:
- `proxy` (str): Прокси-сервер в формате "IP:Port".

**Как работает функция**:
1.  Проверяет, есть ли прокси в списке `working_proxies`.
2.  Если прокси есть в списке, удаляет его.

```ascii
    Remove Proxy
    |
    ---> Check if proxy in working_proxies
    |   |
    |   Yes
    |   |
    |   ---> Remove proxy from working_proxies
    |
    No
    |
    ---> End
```

**Примеры**:
```python
remove_proxy("127.0.0.1:8080")
```

### `get_working_proxies`

```python
def get_working_proxies(prompt, timeout=5):
    """Fetch and test proxy servers, adding working proxies to the global working_proxies list.

    Args:
        prompt (str): The test prompt to be used for testing.
        timeout (int, optional): The maximum time in seconds allowed for testing. Defaults to 5.
    """
```

**Назначение**: Получает список прокси-серверов и проверяет их работоспособность, добавляя рабочие прокси в глобальный список `working_proxies`.

**Параметры**:
- `prompt` (str): Тестовый запрос для проверки прокси.
- `timeout` (int, optional): Максимальное время ожидания ответа в секундах. По умолчанию 5.

**Как работает функция**:
1.  Получает список прокси-серверов с помощью функции `fetch_proxies`.
2.  Создает потоки для параллельной проверки каждого прокси-сервера.
3.  Запускает каждый поток для проверки прокси-сервера с помощью функции `test_proxy`.
4.  Ожидает завершения каждого потока в течение заданного таймаута.

```ascii
    Get Working Proxies
    |
    ---> Fetch proxies via fetch_proxies()
    |
    ---> Create threads for each proxy
    |
    ---> Start each thread to test proxy
    |
    ---> Join each thread with timeout
```

**Примеры**:
```python
get_working_proxies("What is the capital of France?", timeout=5)
```

### `update_working_proxies`

```python
def update_working_proxies():
    """Continuously update the global working_proxies list with working proxy servers."""
```

**Назначение**: Периодически обновляет глобальный список `working_proxies`, получая и тестируя прокси-серверы.

**Как работает функция**:
1.  Задает тестовый запрос для проверки прокси.
2.  В бесконечном цикле:
    - Очищает список `working_proxies`.
    - Получает и тестирует прокси-серверы с помощью функции `get_working_proxies`.
    - Выводит сообщение об обновлении прокси.
    - Засыпает на 30 минут (1800 секунд).

```ascii
    Update Working Proxies
    |
    ---> Set test prompt
    |
    ---> While True:
    |   |
    |   ---> Clear working_proxies
    |   |
    |   ---> Get working proxies via get_working_proxies()
    |   |
    |   ---> Print 'proxies updated'
    |   |
    |   ---> Sleep for 30 minutes
```

**Примеры**:
```python
# Запуск в отдельном потоке, чтобы не блокировать основной поток
import threading
thread = threading.Thread(target=update_working_proxies)
thread.start()
```

### `get_random_proxy`

```python
def get_random_proxy():
    """Get a random working proxy server from the global working_proxies list.

    Returns:
        str: A random working proxy server in the format "IP:Port".
    """
```

**Назначение**: Возвращает случайный рабочий прокси-сервер из глобального списка `working_proxies`.

**Возвращает**:
- `str`: Случайный рабочий прокси-сервер в формате "IP:Port".

**Как работает функция**:
1.  Возвращает случайный элемент из списка `working_proxies`.

```ascii
    Get Random Proxy
    |
    ---> Return random proxy from working_proxies
```

**Примеры**:
```python
proxy = get_random_proxy()
if proxy:
    print(f"Using random proxy: {proxy}")
else:
    print("No working proxies available.")
```