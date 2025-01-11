# Модуль `src.translators`

## Обзор

Модуль `src.translators` предназначен для обработки и перевода текста. 
Этот модуль является частью более крупной системы, обеспечивая функциональность перевода в различных контекстах.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`translate_text`](#translate_text)

## Функции

### `translate_text`

**Описание**: 
Функция, которая на данный момент не выполняет никаких действий.
Предполагается, что в будущем она будет отвечать за перевод текста.

**Параметры**:
- `text` (str): Текст, который нужно перевести.
- `source_language` (str): Исходный язык текста.
- `target_language` (str): Язык, на который нужно перевести текст.

**Возвращает**:
- `str`: Возвращает исходный текст без изменений. В будующем это будет перевод.

**Пример использования:**
```python
    text = "Hello, world!"
    source_lang = "en"
    target_lang = "ru"
    translated_text = translate_text(text, source_lang, target_lang)
    print(translated_text) # Выведет: Hello, world!
```
```python
def translate_text(text: str, source_language: str, target_language: str) -> str:
    """
    Args:
        text (str): Текст, который нужно перевести.
        source_language (str): Исходный язык текста.
        target_language (str): Язык, на который нужно перевести текст.

    Returns:
        str: Возвращает исходный текст без изменений. В будующем это будет перевод.
    """
    return text
```