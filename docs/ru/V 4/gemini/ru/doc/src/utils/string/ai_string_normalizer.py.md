# Модуль `ai_response_normalizer`

## Обзор

Модуль предназначен для нормализации ответов, полученных от AI-моделей, путем удаления лишних префиксов и постфиксов, таких как маркеры кода (` ``` `), которые могут присутствовать в начале и конце текста ответа.

## Подробнее

Этот модуль содержит функцию `normalize_answer`, которая принимает строку в качестве входных данных и пытается удалить известные префиксы и постфиксы, чтобы вернуть "чистый" текст ответа. Это полезно для обработки ответов от AI-моделей, которые часто включают маркеры кода для форматирования.

## Функции

### `normalize_answer`

```python
def normalize_answer(text: str) -> str:
    """
    Args:
        text (str): Строка, которую необходимо нормализовать.

    Returns:
        str: Нормализованная строка, из которой удалены префиксы и постфиксы.

    Example:
        >>> from src.utils.string.ai_response_normalizer import normalize_answer
        >>> normalize_answer("```html\\nПример строки <b>с HTML</b>\\n```")
        'Пример строки <b>с HTML</b>'
    """
    # Объявляем список префиксов, которые нужно удалить из текста.
    prefixes: list = [
        '```md\n',
        '```md',
        '```markdown\n',
        '```markdown',
        '```html\n',
        '```html',
        '```\n',
        '```',
    ]

    # Проверяем, начинается ли текст с одного из префиксов, и если да, удаляем префикс и постфикс '```'.
    for prefix in prefixes:
        if text.startswith(prefix):
            return text.removeprefix(prefix).removesuffix('```')

    # Если ни один из префиксов не найден, возвращаем исходный текст без изменений.
    return text
```

**Описание**: 
Функция `normalize_answer` принимает строку `text` и пытается удалить из неё префиксы и постфиксы, такие как маркеры кода, чтобы получить "чистый" текст.

**Параметры**:
- `text` (str): Строка, которую необходимо нормализовать.

**Возвращает**:
- `str`: Нормализованная строка, из которой удалены префиксы и постфиксы, если они присутствовали.

**Примеры**:

```python
from src.utils.string.ai_response_normalizer import normalize_answer

# Пример с HTML-кодом
normalized_str = normalize_answer("```html\nПример строки <b>с HTML</b>\n```")
print(normalized_str)  # Вывод: Пример строки <b>с HTML</b>

# Пример с Markdown-кодом
normalized_str = normalize_answer("```markdown\nПример текста с Markdown\n```")
print(normalized_str)  # Вывод: Пример текста с Markdown

# Пример без префиксов и постфиксов
normalized_str = normalize_answer("Простой текст")
print(normalized_str)  # Вывод: Простой текст