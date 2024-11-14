```python
# hypotez/src/ai/openai/translator.py
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
    Переводит текст с одного языка на другой с использованием OpenAI API.

    Args:
        text: Текст для перевода.
        source_language: Язык исходного текста (например, "Russian").
        target_language: Язык целевого текста (например, "English").

    Returns:
        Строка с переведенным текстом, если перевод успешен, иначе None.
        Возможные ошибки логгируются в logger.
    """
    if not text:
        logger.warning("Input text is empty.")
        return None

    # Формируем запрос к OpenAI API. Важно правильно сформулировать запрос.
    prompt = (
        f"Translate the following text from {source_language} to {target_language}:\n\n"
        f"{text}\n\n"
        f"Translation:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Используйте подходящую модель
            prompt=prompt,
            max_tokens=256,  # Ограничьте максимальную длину перевода
            n=1,
            stop=None,
            temperature=0.7  # Подберите подходящую температуру
        )
        translation = response.choices[0].text.strip()
        return translation.strip()  # Удаляем лишние пробелы и переносы
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return None
    except IndexError:
        logger.error("No translation found in the response.")
        return None
    except Exception as ex:
        logger.error(f"Error during translation: {ex}")
        return None
```

**Изменения и улучшения:**

* **Документация:** Добавлена подробная документация к функции `translate_text` с описанием аргументов, возвращаемого значения и возможных ошибок.  Теперь пример использования понятнее.
* **Обработка пустого текста:** Добавлена проверка на пустой входной текст и соответствующее логирование.  Функция возвращает `None` в случае пустого входного текста.
* **Обработка ошибок:**  Теперь код обрабатывает `openai.error.OpenAIError` для более надежного кода и  `IndexError`, который может возникнуть, если ответ OpenAI пуст или отсутствует.  Все ошибки логгируются в `logger`.
* **Возвращение `None` при ошибках:** Функция возвращает `None`, если перевод не удался из-за ошибки. Это позволяет вызывающей функции обрабатывать этот случай.
* **Ограничение максимальной длины:** Добавлен `max_tokens=256`. Это важно, чтобы OpenAI не выдавал слишком длинные ответы, которые могут быть нежелательны или привести к ошибкам.  Значение 256 - пример, его можно настроить.
* **Температура:** Параметр `temperature` изменен на `0.7`, чтобы получить более разнообразный и менее механистический перевод, чем при `0.3`.   Подбор температуры - это важная часть настройки.
* **Устранение лишних пробелов:**  Добавлен `.strip()` для удаления лишних пробелов и переносов в возвращаемом значении.


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

Этот улучшенный код более надежный, читабельный и соответствует лучшим практикам работы с API.  Помните, что для `temperature` и `max_tokens`  требуется подбор значений, оптимальных для вашей конкретной задачи.