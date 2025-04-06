# Модуль для тестирования функциональности `ChatCompletion` в g4f

## Обзор

Модуль `test_chat_completion.py` предназначен для тестирования асинхронного и синхронного способов взаимодействия с API `g4f.ChatCompletion` для генерации текстовых ответов на основе предоставленных запросов.

## Подробней

Этот модуль тестирует функциональность `g4f.ChatCompletion`, который позволяет генерировать ответы от различных языковых моделей. Он использует как синхронный, так и асинхронный методы для отправки запросов и получения ответов. В частности, модуль проверяет возможность генерации текста в потоковом режиме (stream=True) и асинхронно. Этот код важен для проверки стабильности и корректности работы `ChatCompletion` при использовании различных моделей и провайдеров.

## Функции

### `run_async`

```python
async def run_async():
    """Асинхронно отправляет запрос к g4f.ChatCompletion и выводит ответ.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: Если происходит ошибка во время выполнения запроса.

    Example:
        >>> asyncio.run(run_async())
        create_async: hello!
    """
```

**Как работает функция**:

1.  Функция `run_async` использует асинхронный метод `g4f.ChatCompletion.create_async` для отправки запроса с сообщением "hello!".
2.  Полученный ответ выводится в консоль с префиксом "create_async:".

```text
run_async
    │
    ├── Асинхронный запрос к g4f.ChatCompletion ("hello!")
    │
    └── Вывод ответа в консоль ("create_async:")
```

**Примеры**:

```python
asyncio.run(run_async())
```

## Код

```python
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

import g4f, asyncio

print("create:", end=" ", flush=True)
for response in g4f.ChatCompletion.create(
    model=g4f.models.default,
    #provider=g4f.Provider.Bing,
    messages=[{"role": "user", "content": "write a poem about a tree"}],
    stream=True
):
    print(response, end="", flush=True)
print()

async def run_async():
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.default,
        #provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": "hello!"}],
    )
    print("create_async:", response)

asyncio.run(run_async())