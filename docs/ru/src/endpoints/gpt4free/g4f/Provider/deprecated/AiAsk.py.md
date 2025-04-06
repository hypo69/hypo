# Модуль AiAsk

## Обзор

Модуль `AiAsk` предоставляет асинхронный генератор для взаимодействия с сервисом AiAsk.me. Он поддерживает модели GPT-3.5 Turbo и позволяет использовать прокси. Этот модуль предназначен для интеграции в систему, где требуется асинхронное взаимодействие с API AiAsk для получения ответов на основе предоставленных сообщений.

## Подробней

Модуль `AiAsk` является частью проекта `hypotez` и предназначен для работы с сервисом AiAsk.me, предоставляющим доступ к языковым моделям. Он использует асинхронный подход для эффективного взаимодействия с API, что позволяет избежать блокировки основного потока выполнения. Модуль поддерживает передачу истории сообщений и использование прокси для обхода ограничений сети.

## Классы

### `AiAsk`

**Описание**: Класс `AiAsk` является поставщиком асинхронного генератора для взаимодействия с API AiAsk.me.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора от базового класса `AsyncGeneratorProvider`.

**Атрибуты**:
- `url` (str): URL сервиса AiAsk.me.
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (значение `True`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель GPT-3.5 Turbo (значение `True`).
- `working` (bool): Указывает, работает ли провайдер в данный момент (значение `False`).

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для получения ответов от API AiAsk.me.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для получения ответов от API AiAsk.me.

        Args:
            model (str): Название используемой модели.
            messages (Messages): Список сообщений для отправки в API.
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            **kwargs: Дополнительные параметры, такие как `temperature`.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API.

        Raises:
            RuntimeError: Если достигнут лимит запросов (Rate limit reached).
        """
```

**Назначение**: Создает асинхронный генератор для получения ответов от API AiAsk.me.

**Параметры**:
- `model` (str): Название используемой модели.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, такие как `temperature`.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API.

**Вызывает исключения**:
- `RuntimeError`: Если достигнут лимит запросов (Rate limit reached).

**Как работает функция**:

1. **Определение заголовков**: Функция определяет заголовки HTTP-запроса, включая `accept`, `origin` и `referer`.
2. **Создание сессии**: Используется `ClientSession` из библиотеки `aiohttp` для создания асинхронной сессии с заданными заголовками.
3. **Формирование данных**: Формируются данные для отправки в API, включая историю сообщений, параметры модели и прочие настройки.
4. **Отправка запроса**: Отправляется POST-запрос к API AiAsk.me с использованием асинхронной сессии и прокси (если указан).
5. **Обработка ответа**: Полученные чанки данных декодируются и передаются через генератор. Если достигнут лимит запросов, выбрасывается исключение `RuntimeError`.

**ASCII flowchart**:

```
A [Определение заголовков]
|
B [Создание асинхронной сессии]
|
C [Формирование данных для запроса]
|
D [Отправка POST-запроса к API]
|
E [Обработка чанков ответа]
|
F [Проверка на лимит запросов]
|
G [Генерация данных или исключение]
```

**Примеры**:

```python
# Пример использования create_async_generator
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Hello, how are you?"}]
proxy = "http://your-proxy-url:8080"

async def main():
    generator = AiAsk.create_async_generator(model=model, messages=messages, proxy=proxy, temperature=0.7)
    async for chunk in generator:
        print(chunk, end="")

# Запуск асинхронной функции
# import asyncio
# asyncio.run(main())
```
```python
# Пример использования create_async_generator без прокси
model = "gpt-3.5-turbo"
messages = [{"role": "user", "content": "Tell me a joke."}]

async def main():
    generator = AiAsk.create_async_generator(model=model, messages=messages, temperature=0.5)
    async for chunk in generator:
        print(chunk, end="")

# Запуск асинхронной функции
# import asyncio
# asyncio.run(main())