# Модуль для демонстрации асинхронного взаимодействия с GPT-4Free

## Обзор

Этот модуль содержит пример асинхронного кода, демонстрирующего взаимодействие с моделью GPT-4Free (gpt-4o) через асинхронный клиент. Он отправляет запрос к модели и выводит полученный ответ.

## Подробнее

Модуль предназначен для демонстрации простого асинхронного запроса к GPT-4Free. Он создает асинхронный клиент, отправляет запрос с системным и пользовательским сообщением, а затем выводит ответ, полученный от модели.
Этот код может быть использован для экспериментов с GPT-4Free и для понимания того, как отправлять асинхронные запросы к этой модели.

## Функции

### `main`

```python
async def main():
    """Асинхронная функция, демонстрирующая взаимодействие с GPT-4Free.

    Функция создает асинхронный клиент, отправляет запрос к модели gpt-4o
    и выводит полученный ответ.

    Returns:
        None

    Примеры:
        Запуск функции:
        >>> asyncio.run(main())
    """
```

**Как работает функция**:

1. **Создание асинхронного клиента**: Функция создает экземпляр `AsyncClient` для взаимодействия с GPT-4Free.
2. **Отправка запроса к модели**: Функция отправляет запрос к модели `gpt-4o` с двумя сообщениями: системным и пользовательским. Системное сообщение указывает модели быть полезным ассистентом, а пользовательское сообщение задает вопрос о том, как дело попадает в Верховный суд.
3. **Вывод ответа**: Функция выводит содержимое первого сообщения из списка ответов, полученных от модели.

**Примеры**:

```python
asyncio.run(main())
```
```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me about Python programming language"}
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```
```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain the theory of relativity in simple terms"}
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```

```markdown