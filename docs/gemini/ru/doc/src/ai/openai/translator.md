# Модуль `hypotez/src/ai/openai/translator.py`

## Обзор

Модуль `translator.py` предоставляет функцию `translate` для перевода текста с использованием API OpenAI. Он использует подготовленные данные из файла конфигурации `gs.credentials.openai` для аутентификации в API. Логирование ошибок происходит с помощью модуля `logger`.

## Оглавление

* [Функции](#функции)


## Функции

### `translate`

**Описание**: Переводит текст с использованием API OpenAI.

**Параметры**:
* `text` (str): Текст для перевода.
* `source_language` (str): Язык исходного текста.
* `target_language` (str): Язык для перевода.

**Возвращает**:
* `str`: Переведённый текст. Возвращает `None` в случае ошибки.


**Вызывает исключения**:
* `Exception`: Возникает при ошибке при взаимодействии с API OpenAI. Ошибка будет залогирована с помощью `logger`.


```python
def translate(text, source_language, target_language):
    """
    Перевод текста с использованием OpenAI API.

    Этот метод отправляет текст для перевода на указанный язык с помощью модели OpenAI и возвращает переведённый текст.

    Args:
        text (str): Текст для перевода.
        source_language (str): Язык исходного текста.
        target_language (str): Язык для перевода.

    Returns:
        str: Переведённый текст. Возвращает None в случае ошибки.

    Raises:
        Exception: Возникает при ошибке при взаимодействии с API OpenAI. Ошибка будет залогирована с помощью logger.
    """
    prompt = (
        f"Translate the following text from {source_language} to {target_language}:\\n\\n"
        f"{text}\\n\\n"
        f"Translation:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Укажите нужную модель
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.3
        )

        translation = response.choices[0].text.strip()
        return translation
    except Exception as ex:
        logger.error("Error during translation", ex)
        return
```