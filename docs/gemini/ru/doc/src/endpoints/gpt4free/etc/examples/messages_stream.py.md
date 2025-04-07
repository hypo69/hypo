# Модуль для асинхронной потоковой передачи сообщений с использованием g4f

## Обзор

Этот модуль демонстрирует, как использовать асинхронный клиент `AsyncClient` из библиотеки `g4f` для отправки запросов к модели `gpt-4` и получения потоковых ответов. Модуль показывает пример простого чат-взаимодействия, где отправляется сообщение "Say hello there!" и полученный ответ выводится в консоль по частям.

## Подробнее

Модуль предназначен для демонстрации асинхронной работы с потоковыми данными. Он инициализирует асинхронный клиент, отправляет запрос к модели GPT-4 и обрабатывает потоковые ответы, выводя их в консоль. Также предусмотрена обработка ошибок и вывод накопленного текста после завершения потока.

## Функции

### `main`

```python
async def main():
    """Асинхронная функция для демонстрации потоковой передачи сообщений.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при обработке потока.

    Пример:
        >>> asyncio.run(main())
        Hello there!
        
        Final accumulated text: Hello there!
    """
    ...
```

**Назначение**: Асинхронная функция `main` выполняет демонстрацию потоковой передачи сообщений с использованием асинхронного клиента `AsyncClient` из библиотеки `g4f`.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- `Exception`: Возникает, если происходит ошибка во время обработки потока.

**Как работает функция**:

1. **Инициализация клиента**: Создается экземпляр асинхронного клиента `AsyncClient`.
2. **Отправка запроса**: Отправляется запрос к модели `gpt-4` с сообщением "Say hello there!" и указанием, что ожидается потоковый ответ (`stream=True`).
3. **Обработка потока**: В цикле `async for` обрабатываются чанки (фрагменты) ответа. Если чанк содержит контент, он добавляется к накопленному тексту и выводится в консоль.
4. **Обработка ошибок**: Если в процессе обработки потока возникает исключение, оно перехватывается, и в консоль выводится сообщение об ошибке.
5. **Вывод результата**: После завершения потока выводится накопленный текст.

**ASCII flowchart**:

```
Инициализация AsyncClient
↓
Отправка запроса к gpt-4 (stream=True)
↓
Обработка чанков ответа
│
├──→ Есть контент? (chunk.choices[0].delta.content)
│   │
│   └──→ Да: Добавить контент к accumulated_text и вывести в консоль
│   │
└──→ Нет: Пропустить
↓
Обработка ошибок (try...except)
↓
Вывод accumulated_text
```

**Примеры**:

```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say hello there!"}],
        stream=True,
    )
    
    accumulated_text = ""
    try:
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                accumulated_text += content
                print(content, end="", flush=True)
    except Exception as e:
        print(f"\nError occurred: {e}")
    finally:
        print("\n\nFinal accumulated text:", accumulated_text)

asyncio.run(main())
```
```python
import asyncio
from g4f.client import AsyncClient

async def main():
    client = AsyncClient()
    
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Как тебя зовут?"}],
        stream=True,
    )
    
    accumulated_text = ""
    try:
        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                accumulated_text += content
                print(content, end="", flush=True)
    except Exception as e:
        print(f"\nError occurred: {e}")
    finally:
        print("\n\nFinal accumulated text:", accumulated_text)

asyncio.run(main())