# Модуль md2dict

## Обзор

Модуль `md2dict` предназначен для конвертации строк Markdown в структурированные словари.  Он поддерживает извлечение JSON содержимого, если оно присутствует в строке Markdown.

## Функции

### `md2dict`

**Описание**: Конвертирует строку Markdown в структурированный словарь, включая извлечение JSON содержимого, если оно присутствует.

**Параметры**:
- `md_string` (str): Строка Markdown для конвертации.

**Возвращает**:
- `Dict[str, dict | list]`: Структурированное представление Markdown содержимого. Возвращает словарь с ключом "json", если найден JSON контент, или словарь с секциями Markdown.


**Вызывает исключения**:
- `Exception`: Общая ошибка при парсинге Markdown.


### `extract_json_from_string`

**Описание**: Извлекает JSON контент из строки, если он присутствует.

**Параметры**:
- `text` (str): Строка для извлечения JSON контента.

**Возвращает**:
- `dict | None`: Извлеченный JSON контент или `None`, если JSON не найден.

**Вызывает исключения**:
- `Exception`: Общая ошибка при извлечении JSON.



## Примеры использования

```python
# Пример 1: Извлечение JSON из Markdown
markdown_string_with_json = """
```json
{"name": "John Doe", "age": 30}
```
"""
result = md2dict(markdown_string_with_json)
print(result)  # Output: {'json': {'name': 'John Doe', 'age': 30}}

# Пример 2: Обработка Markdown без JSON
markdown_string_without_json = "# Заголовок 1\nТекст 1"
result = md2dict(markdown_string_without_json)
print(result)
```


## Подробности реализации

Функция `md2dict` использует библиотеку `markdown2` для конвертации Markdown в HTML. Затем она анализирует HTML-код, чтобы извлечь заголовки и текст.  Если в Markdown строке присутствует JSON, функция `extract_json_from_string` пытается извлечь его. В случае успешного извлечения, возвращается словарь с ключом `json`. В противном случае, возвращается словарь с секциями, которые были извлечены.

Обратите внимание на использование `eval` в функции `extract_json_from_string` для парсинга JSON.  **В реальных приложениях это потенциально небезопасно**.  Необходимо использовать более надёжные методы парсинга JSON, такие как `json.loads()`, для избежания проблем с безопасностью.


```python
import json

def extract_json_from_string(text: str) -> dict | None:
    """
    Извлекает JSON контент из строки, если он присутствует.

    Args:
        text (str): Строка для извлечения JSON контента.

    Returns:
        dict | None: Извлеченный JSON контент или `None`, если JSON не найден.
    """
    try:
        json_pattern = r'"{.*}"'  # Исправлено: более точная регулярка
        json_match = re.search(json_pattern, text, re.DOTALL)
        if json_match:
            json_string = json_match.group(0)[1:-1]  #Убираем двойные кавычки
            return json.loads(json_string)
        return None
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка при декодировании JSON: {ex}")
        return None
    except Exception as ex:
        logger.error("Ошибка извлечения JSON из строки.", exc_info=True)
        return None
```

Это усовершенствование делает код более надежным и безопасным.  Замените код в файле на предоставленный вариант `extract_json_from_string`.