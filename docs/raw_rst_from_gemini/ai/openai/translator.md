```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.openai """
""" Переводчик текста с использованием OpenAI API.

@code
# Пример использования функции
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"
translation = translate_text(source_text, source_language, target_language)
if translation:
    print(f"Translated text: {translation}")
else:
    print("Translation failed.")
@endcode
"""

import openai
from __init__ import gs
from src.logger import logger

openai.api_key = gs.credentials.openai

def translate_text(text, source_language, target_language):
    """
    Переводит текст с одного языка на другой с помощью OpenAI API.

    Args:
        text: Текст для перевода.
        source_language: Исходный язык (например, "Russian").
        target_language: Целевой язык (например, "English").

    Returns:
        Строка с переведенным текстом, или None, если произошла ошибка.
    """

    # Проверка входных данных.  Важная часть!
    if not text or not source_language or not target_language:
        logger.error("Invalid input parameters for translation.")
        return None


    # Формируем запрос к OpenAI API. Важно использовать f-строки для безопасности
    prompt = (
        f"Translate the following text from {source_language} to {target_language}:\n\n"
        f"{text}\n\n"
        f"Translation:"
    )


    try:
        # Отправляем запрос к OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Используйте engine, который подходит вашей задаче
            prompt=prompt,
            max_tokens=150,  # Оптимальное значение,  может варьироваться
            n=1,
            stop=None,
            temperature=0.7  # Экспериментируйте с этим значением
        )

        # Извлекаем перевод из ответа API, избегаем ошибок
        translation = response.choices[0].text.strip()
        return translation
    except openai.error.OpenAIError as ex:
        logger.error(f"Error during translation from OpenAI API: {ex}")
        return None
    except IndexError:
        logger.error("No translation found in the OpenAI response.")
        return None
    except Exception as ex:
        logger.error(f"An unexpected error occurred during translation: {ex}")
        return None
```

**Изменения и улучшения:**

* **Документация:** Добавлена подробная документация к функции `translate_text` с описанием аргументов и возвращаемого значения.  Очень важно для читаемости кода.
* **Обработка ошибок:** Добавлена обработка `try...except` блоков, чтобы перехватывать и обрабатывать различные возможные ошибки, такие как `openai.error.OpenAIError`, `IndexError`, и общую ошибку `Exception`.  Это критически важно для стабильности кода.
* **Проверка входных данных:** Добавлена проверка на пустые или отсутствующие входные параметры (`text`, `source_language`, `target_language`).  Это предотвращает ошибки.
* **Возвращаемое значение:** Функция теперь возвращает `None` в случае ошибки, что позволяет вызывающей функции правильно обработать ситуацию.
* **Максимальное количество токенов:** Установлено `max_tokens=150`.  Это важно для управления размером ответа и предотвращения проблем с API.  В зависимости от задачи может потребоваться изменение.
* **Temperature:** Изменено значение `temperature` на `0.7`.  Это может улучшить качество перевода. Экспериментируйте с этим значением.
* **Ясность сообщений об ошибках:** В `except` блоках добавлены более информативные сообщения об ошибках, чтобы легче отслеживать проблемы.
* **Изменение engine:** Вместо `text-davinci-003` можно использовать другие модели, если нужно.

**Как использовать:**

```python
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"

translation = translate_text(source_text, source_language, target_language)

if translation:
    print(f"Translated text: {translation}")
else:
    print("Translation failed.")
```

Этот улучшенный код более надежен, читаем, и соответствует лучшим практикам разработки.  Не забудьте правильно настроить `openai` и `gs`.