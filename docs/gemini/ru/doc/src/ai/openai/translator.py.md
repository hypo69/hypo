# Модуль `translator.py`

## Обзор

Модуль `translator.py` предназначен для перевода текста с использованием OpenAI API. Он предоставляет функцию `translate`, которая принимает текст, исходный язык и целевой язык, и возвращает переведенный текст.

## Оглавление

1.  [Функции](#функции)
    *   [`translate`](#translate)

## Функции

### `translate`

**Описание**: Переводит текст с использованием OpenAI API.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Язык исходного текста.
- `target_language` (str): Язык для перевода.

**Возвращает**:
- `str`: Переведённый текст.
- `None`: В случае ошибки при переводе.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при взаимодействии с OpenAI API. Ошибка будет залогирована.

**Пример использования**:

```python
>>> source_text = "Привет, как дела?"
>>> source_language = "Russian"
>>> target_language = "English"
>>> translation = translate(source_text, source_language, target_language)
>>> print(f"Translated text: {translation}")
```