## \file hypotez/consultant/gemini/ai/openai/translator.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.ai.openai """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.ai.openai """
""" Переводчик 
@code
# Пример использования функции
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"
translation = translate_text(source_text, source_language, target_language)
print(f"Translated text: {translation}")
@endcode
"""




import openai
from __init__ import gs
from src.logger import logger

openai.api_key = gs.credentials.openai

def translate_text(text, source_language, target_language):
    # Формируем запрос к OpenAI API
    prompt = (
        f"Translate the following text from {source_language} to {target_language}:\n\n"
        f"{text}\n\n"
        f"Translation:"
    )

    try:
        # Отправляем запрос к OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Укажите нужную модель, возможно, лучше  "text-curie-001" или "text-babbage-001" для экономии
            prompt=prompt,
            max_tokens=150,  # Ограничение на количество возвращаемых токенов.  Измените, если требуется больше.
            n=1,
            stop=None,
            temperature=0.7 # Попробуйте значения от 0 до 1.  0 - более формальный, 1 - более творческий.
        )

        # Извлекаем перевод из ответа API
        translation = response.choices[0].text.strip()
        return translation
    except openai.error.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        return None  # Или верните какое-то значение, обозначающее ошибку
    except Exception as ex:
        logger.error(f"Error during translation: {ex}")
        return None  # Или верните какое-то значение, обозначающее ошибку


```

**Изменения и объяснения:**

* **Обработка исключений:** Добавлена обработка `openai.error.OpenAIError` для более конкретных ошибок API OpenAI.  Это важно, так как  просто `try...except Exception` слишком широко и может скрывать ошибки OpenAI, которые дают больше информации.  Более конкретная обработка позволяет лучше отследить проблему и принять меры.
* **Возврат `None` при ошибках:** Вместо `return`, функция возвращает `None`, чтобы вызывающая функция могла обрабатывать ошибку. Это более гибкий подход, чем просто `return`.
* **`max_tokens`:** Установлено разумное значение `max_tokens=150`. Избыточное количество токенов может привести к нежелательным результатам, а чрезмерно большое количество может вызвать ошибки. Настройте его в соответствии с вашими потребностями.  Не забудьте, что длины текста в ответе должны соответствовать заданным ограничениям в OpenAI.
* **`temperature`:**  Добавил `temperature=0.7`.   Это параметр, влияющий на вероятность выбора случайных слов в генерируемом тексте.  Значение 0 дает наиболее вероятный ответ, а 1 - более креативный. Экспериментируйте с этим параметром.


**Важные рекомендации:**

* **Анализ ошибок:** Если функция возвращает `None`,  необходимо выяснить причину ошибки. Проверьте сообщения `logger.error` и/или `print(e)` для более подробной информации.
* **Ограничение размера входных данных:** Если вы ожидаете больших текстов для перевода, убедитесь, что вы используете функцию API OpenAI, подходящую для работы с большими текстами, или разделяете текст на более мелкие части.
* **Контроль частоты запросов:**  Убедитесь, что ваши запросы к OpenAI не нарушают их лимиты запросов.
* **Управление ключами API:** Не храните API-ключ OpenAI напрямую в коде. Используйте безопасные методы хранения ключей.


**Пример использования (и проверки на ошибки):**

```python
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"

translation = translate_text(source_text, source_language, target_language)

if translation is not None:
    print(f"Translated text: {translation}")
else:
    print("Translation failed.")
```

Этот улучшенный код более надежен, помогает в отладке и предоставляет больше возможностей для управления возможными ошибками.  Помните, что `temperature` и `max_tokens` могут быть важны для оптимизации качества перевода.
