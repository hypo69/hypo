# Module: `hypotez/src/ai/openai/translator.py`

## Overview

This module provides a function for translating text using the OpenAI API. It handles API requests, error handling, and logging.

## Functions

### `translate`

**Description**: This function translates a given text from one language to another using the OpenAI API.

**Parameters**:

- `text` (str): The text to be translated.
- `source_language` (str): The language of the input text.
- `target_language` (str): The language to translate the text to.

**Returns**:

- str: The translated text.  Returns `None` if an error occurs during the translation process.

**Raises**:

- `Exception`: Any exception raised during the OpenAI API call or during the processing of the response. The error is logged using the `logger` from the `src.logger` module.


```python
def translate(text, source_language, target_language):
    """
    Перевод текста с использованием OpenAI API.

    Этот метод отправляет текст для перевода на указанный язык с помощью модели OpenAI и возвращает переведённый текст.

    Аргументы:
        text (str): Текст для перевода.
        source_language (str): Язык исходного текста.
        target_language (str): Язык для перевода.

    Возвращает:
        str: Переведённый текст.

    Пример использования:
        >>> source_text = "Привет, как дела?"
        >>> source_language = "Russian"
        >>> target_language = "English"
        >>> translation = translate_text(source_text, source_language, target_language)
        >>> print(f"Translated text: {translation}")
    """

    # Формируем запрос к OpenAI API
    prompt = (
        f"Translate the following text from {source_language} to {target_language}:\n\n"
        f"{text}\n\n"
        f"Translation:"
    )

    try:
        # Отправляем запрос к OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Укажите нужную модель
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.3
        )

        # Извлекаем перевод из ответа API
        translation = response.choices[0].text.strip()
        return translation
    except Exception as ex:
        # Логируем ошибку
        logger.error("Error during translation", ex)
        return
```