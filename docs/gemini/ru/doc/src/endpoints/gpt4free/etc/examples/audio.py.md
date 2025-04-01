# Модуль для работы с аудио с использованием g4f

## Обзор

Модуль предоставляет примеры асинхронного взаимодействия с различными провайдерами для генерации и транскрибирования аудио с использованием библиотеки `g4f`. Он демонстрирует, как использовать `AsyncClient` для создания аудиофайлов и транскрибирования существующих аудиофайлов.

## Подробней

Этот модуль демонстрирует, как использовать библиотеку `g4f` для выполнения двух основных задач, связанных с аудио:

1.  **Генерация аудио**: Используется провайдер `PollinationsAI` для генерации аудиофайла на основе текстового запроса. В примере генерируется фраза "Say good day to the world" и сохраняется в файл `alloy.mp3`.
2.  **Транскрибирование аудио**: Используется провайдер `Microsoft_Phi_4` для транскрибирования аудиофайла `audio.wav`. Результат транскрибирования выводится в консоль.

## Функции

### `main`

```python
async def main():
    """
    Асинхронная функция, демонстрирующая генерацию и транскрибирование аудио.

    Args:
        None

    Returns:
        None

    Raises:
        Exception: В случае возникновения ошибки при генерации или транскрибировании аудио.
    """
```

**Как работает функция**:

1.  **Инициализация асинхронного клиента**: Создается экземпляр `AsyncClient` с указанием провайдера `PollinationsAI`.
2.  **Генерация аудио**: Выполняется запрос к провайдеру `PollinationsAI` для генерации аудио на основе текста "Say good day to the world". Указывается модель `openai-audio`, голос `alloy` и формат `mp3`. Сгенерированное аудио сохраняется в файл `alloy.mp3`.
3.  **Транскрибирование аудио**: Открывается аудиофайл `audio.wav` в режиме чтения байтов. Выполняется запрос к провайдеру `Microsoft_Phi_4` для транскрибирования аудиофайла. Указывается, что входные данные содержат медиафайл (аудио) и что ожидается текстовый вывод. Результат транскрибирования выводится в консоль.

```
Создание асинхронного клиента --> Запрос на генерацию аудио --> Сохранение аудио в файл
                                  |
                                  V
                                  Запрос на транскрибирование аудио --> Вывод результата
```

**Примеры**:

```python
import asyncio
from g4f.client import AsyncClient
import g4f.Provider
import g4f.models

async def main():
    client = AsyncClient(provider=g4f.Provider.PollinationsAI)

    # Generate audio with PollinationsAI
    response = await client.chat.completions.create(
        model="openai-audio",
        messages=[{"role": "user", "content": "Say good day to the world"}],
        audio={ "voice": "alloy", "format": "mp3" },
    )
    response.choices[0].message.save("alloy.mp3")

    # Transcribe a audio file
    with open("audio.wav", "rb") as audio_file:
        response = await client.chat.completions.create(
            messages="Transcribe this audio",
            provider=g4f.Provider.Microsoft_Phi_4,
            media=[[audio_file, "audio.wav"]],
            modalities=["text"],
        )
        print(response.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())