# Модуль для перевода текста с использованием OpenAI API

## Обзор

Модуль `translator.py` предназначен для перевода текста с одного языка на другой, используя API OpenAI. Он содержит функцию `translate`, которая принимает текст, исходный язык и целевой язык в качестве аргументов и возвращает переведенный текст.

## Подробней

Этот модуль предоставляет удобный интерфейс для использования возможностей перевода OpenAI в проекте `hypotez`. Он позволяет легко интегрировать функцию перевода текста в различные части проекта, где это необходимо.

## Функции

### `translate`

```python
def translate(text: str, source_language: str, target_language: str) -> str:
    """
    Перевод текста с использованием OpenAI API.

    Этот метод отправляет текст для перевода на указанный язык с помощью модели OpenAI и возвращает переведённый текст.

    Args:
        text (str): Текст для перевода.
        source_language (str): Язык исходного текста.
        target_language (str): Язык для перевода.

    Returns:
        str: Переведённый текст.

    Raises:
        Exception: Возникает при ошибке во время перевода.

    Example:
        >>> source_text = "Привет, как дела?"
        >>> source_language = "Russian"
        >>> target_language = "English"
        >>> translation = translate_text(source_text, source_language, target_language)
        >>> print(f"Translated text: {translation}")
    """
```

**Назначение**: Переводит текст с использованием OpenAI API.

**Параметры**:

- `text` (str): Текст, который необходимо перевести.
- `source_language` (str): Язык, с которого нужно перевести текст.
- `target_language` (str): Язык, на который нужно перевести текст.

**Возвращает**:

- `str`: Переведенный текст. В случае возникновения ошибки возвращает `None`.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке во время взаимодействия с OpenAI API.

**Как работает функция**:

1. **Формирование запроса**: Функция создает запрос к OpenAI API, включающий текст для перевода, исходный язык и целевой язык.
2. **Отправка запроса**: Запрос отправляется к OpenAI API с использованием указанной модели (`text-davinci-003`).
3. **Получение ответа**: Функция получает ответ от OpenAI API, содержащий переведенный текст.
4. **Извлечение перевода**: Из ответа API извлекается переведенный текст.
5. **Обработка ошибок**: Если во время любого из этапов возникает ошибка, она логируется с использованием `logger.error`, и функция возвращает `None`.

```ascii
   Начало
     ↓
   Формирование запроса (prompt)
     ↓
   Отправка запроса в OpenAI API
     ↓
   Получение ответа от OpenAI API
     ↓
   Извлечение перевода из ответа
     ↓
   Возврат переведенного текста
     ↓
   Конец
```

**Примеры**:

```python
from src.ai.openai.translator import translate
text = "Привет, мир!"
source_language = "Russian"
target_language = "English"
translation = translate(text, source_language, target_language)
print(translation)  # Output: Hello, world!

text = "This is a test."
source_language = "English"
target_language = "German"
translation = translate(text, source_language, target_language)
print(translation) # Output: Dies ist ein Test.