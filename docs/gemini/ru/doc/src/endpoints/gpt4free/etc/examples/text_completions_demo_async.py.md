# Модуль для демонстрации асинхронных текстовых завершений с использованием gpt4free

## Обзор

Этот модуль демонстрирует, как использовать асинхронный клиент из библиотеки `g4f` для создания текстовых завершений с использованием модели `gpt-4o`. Он содержит пример асинхронного кода, который отправляет запрос к модели и выводит полученный ответ.

## Подробнее

Модуль использует библиотеку `g4f` для взаимодействия с API gpt4free. Асинхронный клиент позволяет отправлять запросы неблокирующим образом, что может быть полезно для приложений, требующих высокой производительности и отзывчивости. В данном примере демонстрируется отправка запроса к модели `gpt-4o` с простым вопросом о том, как судебное дело попадает в Верховный суд.

## Функции

### `main`

```python
async def main():
    """Асинхронная функция, демонстрирующая создание текстового завершения с использованием gpt4free.

    Returns:
        None

    """
```

**Назначение**:
Асинхронная функция `main` создает экземпляр асинхронного клиента, отправляет запрос к модели `gpt-4o` и выводит полученный ответ.

**Как работает функция**:

1.  **Создание асинхронного клиента**: Создается экземпляр класса `AsyncClient` из библиотеки `g4f`.
2.  **Отправка запроса к модели**: Используется метод `client.chat.completions.create` для отправки запроса к модели `gpt-4o`. Запрос содержит системное сообщение, устанавливающее роль ассистента, и пользовательское сообщение с вопросом.
3.  **Вывод ответа**: Полученный ответ выводится на экран.

```
    Создание асинхронного клиента
    │
    │
    Отправка запроса к модели gpt-4o
    │
    │
    Вывод ответа
```

**Примеры**:

```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "how does a court case get to the Supreme Court?"}
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())
```
### `asyncio.run(main())`

**Назначение**:
Выполняет асинхронную функцию `main`.

**Как работает функция**:

1.  **Запуск асинхронной функции**: `asyncio.run(main())` запускает асинхронную функцию `main` и ожидает ее завершения.

**Примеры**:

```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "how does a court case get to the Supreme Court?"}
        ]
    )
    
    print(response.choices[0].message.content)

asyncio.run(main())