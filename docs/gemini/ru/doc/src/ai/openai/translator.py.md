# Модуль `translator.py`

## Обзор

Модуль `translator.py` предназначен для перевода текста с использованием OpenAI API. Он предоставляет функцию `translate` для перевода текста с одного языка на другой.

## Содержание

1. [Обзор](#обзор)
2. [Функции](#функции)
   - [`translate`](#translate)

## Функции

### `translate`

**Описание**:
Переводит текст с использованием OpenAI API.

Этот метод отправляет текст для перевода на указанный язык с помощью модели OpenAI и возвращает переведённый текст.

**Параметры**:
- `text` (str): Текст для перевода.
- `source_language` (str): Язык исходного текста.
- `target_language` (str): Язык для перевода.

**Возвращает**:
- `str`: Переведённый текст.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке во время перевода или при обращении к OpenAI API.

**Пример использования**:
```python
>>> source_text = "Привет, как дела?"
>>> source_language = "Russian"
>>> target_language = "English"
>>> translation = translate_text(source_text, source_language, target_language)
>>> print(f"Translated text: {translation}")
```