# Модуль для создания изображений через Bing

## Обзор

Модуль предоставляет функциональность для создания изображений на основе текстового запроса с использованием сервиса Bing. Он включает в себя функции для установления сессии, отправки запроса на создание изображений и извлечения URL-адресов сгенерированных изображений.

## Подробней

Этот модуль является частью проекта `hypotez` и предназначен для интеграции с другими модулями, требующими генерации изображений на основе текстовых описаний. Он использует библиотеки `aiohttp` для асинхронных HTTP-запросов и `Beautiful Soup` для парсинга HTML-контента. Модуль обрабатывает ошибки, связанные с лимитами запросов, блокировкой запросов и другими проблемами при создании изображений.

## Функции

### `create_session`

```python
def create_session(cookies: Dict[str, str], proxy: str | None = None, connector: BaseConnector | None = None) -> ClientSession:
    """
    Создает новый клиентский сеанс с указанными файлами cookie и заголовками.

    Args:
        cookies (Dict[str, str]): Файлы cookie, которые будут использоваться для сеанса.
        proxy (Optional[str], optional): Конфигурация прокси-сервера. По умолчанию `None`.
        connector (Optional[BaseConnector], optional): Пользовательский коннектор для сессии aiohttp. По умолчанию `None`.

    Returns:
        ClientSession: Созданный клиентский сеанс.
    """
    ...
```

**Назначение**: Создает сессию клиента с заданными cookie-файлами и заголовками для выполнения HTTP-запросов.

**Параметры**:
- `cookies` (Dict[str, str]): Словарь, содержащий cookie-файлы для сессии.
- `proxy` (Optional[str], optional): Адрес прокси-сервера для использования в сессии. По умолчанию `None`.
- `connector` (Optional[BaseConnector], optional): Экземпляр `BaseConnector` для управления базовым соединением. По умолчанию `None`.

**Возвращает**:
- `ClientSession`: Объект `ClientSession`, настроенный с переданными заголовками и cookie-файлами.

**Как работает функция**:

1.  Определяются заголовки HTTP-запроса, включая `User-Agent`, `Accept`, `Accept-Language` и другие необходимые параметры.
2.  Если переданы cookie-файлы, они форматируются и добавляются в заголовок `Cookie`.
3.  Инициализируется объект `ClientSession` с заданными заголовками и, если указано, прокси-сервером.

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession

async def main():
    cookies = {'cookie1': 'value1', 'cookie2': 'value2'}
    session = create_session(cookies=cookies)
    async with session.get('https://www.bing.com') as response:
        print(response.status)

    await session.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### `create_images`

```python
async def create_images(session: ClientSession, prompt: str, timeout: int = TIMEOUT_IMAGE_CREATION) -> List[str]:
    """
    Создает изображения на основе заданного запроса с использованием сервиса Bing.

    Args:
        session (ClientSession): Активная клиентская сессия.
        prompt (str): Запрос для генерации изображений.
        timeout (int): Время ожидания для запроса.

    Returns:
        List[str]: Список URL-адресов созданных изображений.

    Raises:
        MissingRequirementsError: Если отсутствует пакет "beautifulsoup4".
        RateLimitError: Если закончились монеты. Войдите в систему с другой учетной записью или подождите некоторое время.
        RuntimeError: Если не удалось создать изображения или истекло время ожидания.
    """
    ...
```

**Назначение**: Отправляет запрос в Bing для создания изображений на основе предоставленного запроса и возвращает список URL-адресов сгенерированных изображений.

**Параметры**:
- `session` (ClientSession): Активная клиентская сессия для выполнения HTTP-запросов.
- `prompt` (str): Текстовый запрос для генерации изображений.
- `timeout` (int): Максимальное время ожидания запроса в секундах. По умолчанию `TIMEOUT_IMAGE_CREATION`.

**Возвращает**:
- `List[str]`: Список URL-адресов сгенерированных изображений.

**Вызывает исключения**:
- `MissingRequirementsError`: Если отсутствует библиотека `beautifulsoup4`.
- `RateLimitError`: Если достигнут лимит запросов (нет доступных "монет").
- `RuntimeError`: Если запрос завершился неудачно по другим причинам (например, таймаут, блокировка запроса).

**Как работает функция**:

1.  Проверяется наличие необходимой библиотеки `beautifulsoup4`. Если библиотека не установлена, вызывается исключение `MissingRequirementsError`.
2.  Запрос кодируется с использованием `urllib.parse.quote`.
3.  Отправляется POST-запрос к Bing с закодированным запросом.
4.  Обрабатываются возможные ошибки, такие как отсутствие доступных "монет" или блокировка запроса.
5.  Если запрос перенаправлен, извлекается URL перенаправления и выполняется GET-запрос для получения результатов.
6.  Выполняется опрос (polling) URL до тех пор, пока не будут получены результаты или не истечет время ожидания.
7.  Извлекаются URL-адреса изображений из полученного HTML-контента с использованием функции `read_images`.

ASCII flowchart:

```
A: Проверка наличия beautifulsoup4
|
B: Кодирование запроса
|
C: Отправка POST-запроса в Bing
|
D: Обработка ошибок (лимит, блокировка)
|
E: Получение URL перенаправления
|
F: Опрос URL до получения результатов
|
G: Извлечение URL-адресов изображений
|
H: Возврат списка URL-адресов
```

**Примеры**:

```python
import asyncio
from aiohttp import ClientSession

async def main():
    prompt = "A beautiful cat"
    cookies = {'cookie1': 'value1', 'cookie2': 'value2'}

    session = create_session(cookies=cookies)
    try:
        image_urls = await create_images(session=session, prompt=prompt)
        print(image_urls)
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        await session.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### `read_images`

```python
def read_images(html_content: str) -> List[str]:
    """
    Извлекает URL-адреса изображений из HTML-контента.

    Args:
        html_content (str): HTML-контент, содержащий URL-адреса изображений.

    Returns:
        List[str]: Список URL-адресов изображений.

    Raises:
        RuntimeError: Если не найдены изображения или найдены плохие изображения.
    """
    ...
```

**Назначение**: Извлекает URL-адреса изображений из предоставленного HTML-контента, используя библиотеку `Beautiful Soup`.

**Параметры**:
- `html_content` (str): HTML-контент, содержащий URL-адреса изображений.

**Возвращает**:
- `List[str]`: Список URL-адресов изображений, извлеченных из HTML-контента.

**Вызывает исключения**:
- `RuntimeError`: Если не удалось найти изображения или обнаружены "плохие" изображения (содержащиеся в списке `BAD_IMAGES`).

**Как работает функция**:

1.  HTML-контент анализируется с использованием `BeautifulSoup`.
2.  Выполняется поиск всех тегов `img` с классами `mimg` или `gir_mmimg`.
3.  Извлекаются атрибуты `src` из найденных тегов.
4.  Удаляются параметры ширины `?w=` из URL-адресов.
5.  Проверяется, содержатся ли какие-либо из полученных URL-адресов в списке `BAD_IMAGES`. Если да, вызывается исключение `RuntimeError`.
6.  Если не найдено ни одного изображения, вызывается исключение `RuntimeError`.

ASCII flowchart:

```
A: Анализ HTML-контента с BeautifulSoup
|
B: Поиск тегов img с классами mimg или gir_mmimg
|
C: Извлечение атрибутов src
|
D: Удаление параметров ширины из URL
|
E: Проверка на наличие "плохих" изображений
|
F: Проверка на наличие изображений
|
G: Возврат списка URL-адресов
```

**Примеры**:

```python
html_content = """
<img class="mimg" src="https://example.com/image1.jpg?w=300">
<img class="gir_mmimg" src="https://example.com/image2.jpg?w=300">
"""
image_urls = read_images(html_content)
print(image_urls)  # Вывод: ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']