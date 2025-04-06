# Модуль для работы с Ollama

## Обзор

Модуль `Ollama.py` предназначен для взаимодействия с локально установленным сервером Ollama, который позволяет запускать языковые модели на вашей машине. Этот модуль предоставляет класс `Ollama`, который наследуется от `OpenaiAPI` и реализует методы для получения списка доступных моделей и создания асинхронного генератора для запросов к Ollama.

## Подробней

Модуль упрощает интеграцию с Ollama, предоставляя удобный интерфейс для работы с моделями Ollama через API. Он автоматически определяет базовый URL для API на основе переменных окружения `OLLAMA_HOST` и `OLLAMA_PORT`, что позволяет легко настраивать подключение к серверу Ollama.

## Классы

### `Ollama`

**Описание**: Класс `Ollama` предоставляет интерфейс для взаимодействия с сервером Ollama.

**Наследует**:
- `OpenaiAPI`: Наследует функциональность для работы с API, аналогичным OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера, в данном случае "Ollama".
- `url` (str): URL сервера Ollama.
- `login_url` (Optional[str]): URL для логина (отсутствует).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (не требуется).
- `working` (bool): Флаг, указывающий на работоспособность провайдера.

**Методы**:
- `get_models()`: Получает список доступных моделей с сервера Ollama.
- `create_async_generator()`: Создает асинхронный генератор для взаимодействия с Ollama API.

## Функции

### `get_models`

```python
    @classmethod
    def get_models(cls, api_base: str = None, **kwargs):
        """
        Получает список доступных моделей с сервера Ollama.

        Args:
            api_base (str, optional): Базовый URL для API. Если не указан, используется значение из переменных окружения. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Returns:
            List[str]: Список имен доступных моделей.

        Raises:
            requests.exceptions.RequestException: Если возникает ошибка при запросе к API.

        Example:
            >>> Ollama.get_models()
            ['llama2', 'mistral', ...]
        """
        ...
```

**Назначение**: Получение списка доступных моделей с сервера Ollama.

**Параметры**:
- `api_base` (str, optional): Базовый URL для API. Если не указан, используется значение из переменных окружения `OLLAMA_HOST` и `OLLAMA_PORT`. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `List[str]`: Список имен доступных моделей.

**Вызывает исключения**:
- `requests.exceptions.RequestException`: Если возникает ошибка при запросе к API.

**Как работает функция**:
1. Проверяет, был ли уже получен список моделей. Если да, возвращает сохраненный список.
2. Если `api_base` не указан, формирует URL на основе переменных окружения `OLLAMA_HOST` и `OLLAMA_PORT`.
3. Выполняет GET-запрос к API Ollama для получения списка моделей.
4. Извлекает имена моделей из JSON-ответа и сохраняет их в `cls.models`.
5. Устанавливает первую модель в списке в качестве модели по умолчанию (`cls.default_model`).
6. Возвращает список имен моделей.

**ASCII flowchart**:

```
A[Проверка, есть ли cls.models]
|
No
|
B[Определение URL API (api_base или env vars)]
|
C[GET-запрос к API Ollama (/api/tags)]
|
D[Извлечение имен моделей из JSON]
|
E[Сохранение моделей в cls.models]
|
F[Установка cls.default_model]
|
Yes
|
G[Возврат cls.models]
```

**Примеры**:
```python
# Пример получения списка моделей
models = Ollama.get_models()
print(models)
# Вывод: ['llama2', 'mistral', ...]
```

### `create_async_generator`

```python
    @classmethod
    def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        api_base: str = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с Ollama API.

        Args:
            model (str): Имя модели для использования.
            messages (Messages): Список сообщений для отправки в API.
            api_base (str, optional): Базовый URL для API. Если не указан, используется значение из переменных окружения. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор для получения ответов от API.

        Example:
            >>> messages = [{"role": "user", "content": "Hello"}]
            >>> generator = Ollama.create_async_generator(model="llama2", messages=messages)
            >>> async for chunk in generator:
            ...     print(chunk)
        """
        ...
```

**Назначение**: Создание асинхронного генератора для взаимодействия с Ollama API.

**Параметры**:
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в API.
- `api_base` (str, optional): Базовый URL для API. Если не указан, используется значение из переменных окружения `OLLAMA_HOST` и `OLLAMA_PORT`. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор для получения ответов от API.

**Как работает функция**:
1. Проверяет, указан ли `api_base`. Если нет, формирует его на основе переменных окружения `OLLAMA_HOST` и `OLLAMA_PORT`.
2. Вызывает метод `create_async_generator` родительского класса `OpenaiAPI` с указанными параметрами.

**ASCII flowchart**:

```
A[Проверка, указан ли api_base]
|
No
|
B[Формирование URL API (env vars)]
|
Yes
|
C[Вызов super().create_async_generator()]
|
D[Возврат AsyncResult]
```

**Примеры**:
```python
# Пример создания асинхронного генератора
messages = [{"role": "user", "content": "Hello"}]
generator = Ollama.create_async_generator(model="llama2", messages=messages)
# Дальнейшее использование генератора для получения ответов