# Модуль тестирования ChatCompletion для gpt4free

## Обзор

Этот модуль содержит тесты для проверки функциональности `ChatCompletion` из библиотеки `gpt4free`. Он включает в себя примеры использования `ChatCompletion.create` и `ChatCompletion.create_async` для генерации текста с использованием модели по умолчанию.

## Подробней

Этот модуль используется для демонстрации и тестирования библиотеки `gpt4free`. В частности, он показывает, как можно использовать `ChatCompletion` для генерации текста как синхронно, так и асинхронно.

## Функции

### `run_async`

```python
async def run_async():
    """ Асинхронно создает завершение чата с использованием g4f.ChatCompletion.create_async.

    Args:
        None

    Returns:
        None

    """
```

**Назначение**: Асинхронно создает завершение чата с использованием `g4f.ChatCompletion.create_async`.

**Параметры**:
- Нет параметров.

**Возвращает**:
- Ничего.

**Как работает функция**:

1.  **Асинхронный запрос к модели**: Отправляет асинхронный запрос к модели `g4f.models.default` через `g4f.ChatCompletion.create_async` с сообщением `"hello!"`.
2.  **Вывод ответа**: Выводит полученный ответ в консоль.

```
Запрос к g4f.ChatCompletion.create_async -> Получение ответа от модели -> Вывод ответа
```

**Примеры**:

```python
import asyncio
import g4f

async def run_async():
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.default,
        messages=[{"role": "user", "content": "hello!"}],
    )
    print("create_async:", response)

asyncio.run(run_async())
```

## Дополнительная информация

Модуль также содержит пример синхронного использования `g4f.ChatCompletion.create` для генерации стихотворения о дереве. Этот пример демонстрирует потоковую передачу ответа от модели.