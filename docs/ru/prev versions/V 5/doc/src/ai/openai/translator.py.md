# Модуль `translator`

## Обзор

Модуль `translator` предназначен для перевода текста с использованием OpenAI API. Он предоставляет функцию `translate`, которая отправляет текст на указанный язык с помощью модели OpenAI и возвращает переведённый текст.

## Подробней

Этот модуль позволяет интегрировать возможности машинного перевода в проект `hypotez`. Он использует API OpenAI для выполнения перевода текста с одного языка на другой. Модуль содержит функцию `translate`, которая принимает текст, язык оригинала и язык перевода в качестве аргументов и возвращает переведённый текст.

## Функции

### `translate`

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
        f"Translate the following text from {source_language} to {target_language}:\\n\\n"
        f"{text}\\n\\n"
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

**Описание**:
Функция `translate` осуществляет перевод текста с использованием OpenAI API.

**Как работает функция**:

1.  Формируется запрос к OpenAI API, включающий исходный текст, язык оригинала и язык перевода.
2.  Запрос отправляется к OpenAI API с использованием модели `text-davinci-003`.
3.  Извлекается переведённый текст из ответа API.
4.  В случае ошибки, информация об ошибке логируется с использованием `logger.error`.

**Параметры**:

*   `text` (str): Текст, который требуется перевести.
*   `source_language` (str): Язык оригинала текста.
*   `target_language` (str): Язык, на который требуется перевести текст.

**Возвращает**:

*   `str`: Переведённый текст. В случае ошибки возвращает `None`.

**Вызывает исключения**:

*   `Exception`: В случае возникновения ошибки при обращении к OpenAI API или обработке ответа.

**Примеры**:

```python
source_text = "Привет, как дела?"
source_language = "Russian"
target_language = "English"
translation = translate(source_text, source_language, target_language)
print(f"Translated text: {translation}")