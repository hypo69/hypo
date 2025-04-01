# Модуль `Cerebras.py`

## Обзор

Модуль предоставляет класс `Cerebras`, который используется для взаимодействия с API Cerebras Inference для генерации текста на основе моделей LLM. Он наследуется от класса `OpenaiAPI` и реализует асинхронную генерацию текста. Модуль также предоставляет методы для получения ключа API и обработки ответов от API Cerebras.

## Подробней

Модуль `Cerebras` предназначен для работы с моделями машинного обучения, размещенными на платформе Cerebras Inference. Он обеспечивает асинхронное взаимодействие с API Cerebras, включая аутентификацию и обработку ответов. Этот модуль является частью проекта `hypotez` и используется для предоставления доступа к передовым моделям LLM, таким как Llama 3 и Deepseek, через унифицированный интерфейс.

## Классы

### `Cerebras`

**Описание**: Класс для взаимодействия с API Cerebras Inference. Предоставляет методы для асинхронной генерации текста на основе моделей LLM.

**Наследует**:

- `OpenaiAPI`: Наследует базовый функционал для работы с API OpenAI, включая обработку запросов и токенов.

**Атрибуты**:

- `label` (str): Метка провайдера "Cerebras Inference".
- `url` (str): URL для доступа к Cerebras Inference.
- `login_url` (str): URL для логина в Cerebras Cloud.
- `api_base` (str): Базовый URL для API Cerebras.
- `working` (bool): Флаг, указывающий на работоспособность провайдера.
- `default_model` (str): Модель по умолчанию "llama3.1-70b".
- `models` (List[str]): Список поддерживаемых моделей.
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей.

**Методы**:

- `create_async_generator`: Асинхронный генератор для создания текста на основе API Cerebras.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    cookies: Cookies = None,
    **kwargs
) -> AsyncResult:
    """Асинхронно генерирует текст, используя API Cerebras.

    Args:
        model (str): Модель для использования.
        messages (Messages): Список сообщений для отправки в API.
        api_key (str, optional): Ключ API. По умолчанию `None`.
        cookies (Cookies, optional): Куки для аутентификации. По умолчанию `None`.

    Returns:
        AsyncResult: Асинхронный генератор чанков текста.

    Как работает функция:
    1. Проверяет наличие `api_key`. Если он не предоставлен, пытается получить его из cookies.
    2. Если `cookies` также не предоставлены, пытается получить их для домена `.cerebras.ai`.
    3. Если `api_key` все еще не найден, выполняет GET-запрос к `"https://inference.cerebras.ai/api/auth/session"` для получения `api_key` из ответа JSON.
    4. Вызывает метод `create_async_generator` из родительского класса `OpenaiAPI` для генерации текста, используя полученный `api_key` и другие параметры.
    5. Передает заголовки User-Agent для имитации запроса из браузера Chrome.
    6. Возвращает асинхронный генератор чанков текста.

    A -- Проверка наличия api_key
    |
    B -- Получение cookies, если api_key отсутствует
    |
    C -- Запрос к API для получения api_key, если cookies отсутствуют
    |
    D -- Вызов create_async_generator из OpenaiAPI с полученным api_key
    |
    E -- Генерация чанков текста
    |
    F -- Возврат асинхронного генератора
    """
```

## Примеры

```python
# Пример использования асинхронного генератора
async def main():
    messages = [{"role": "user", "content": "Напиши небольшое стихотворение о космосе."}]
    async for chunk in Cerebras.create_async_generator(model="llama3.1-70b", messages=messages):
        print(chunk, end="")

# Пример получения api_key из cookies
# Предполагается, что cookies уже установлены в браузере для домена .cerebras.ai
async def main():
    messages = [{"role": "user", "content": "Напиши небольшое стихотворение о космосе."}]
    cookies = get_cookies(".cerebras.ai")
    async for chunk in Cerebras.create_async_generator(model="llama3.1-70b", messages=messages, cookies=cookies):
        print(chunk, end="")