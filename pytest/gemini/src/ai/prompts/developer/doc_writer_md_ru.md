# Модуль: doc_writer_md

Этот модуль содержит функции для генерации Markdown-документации для Python-кода.

## Пример использования

```python
from doc_writer_md import generate_markdown_doc

code_snippet = """
def add(x, y):
    """Складывает два числа."""
    return x + y
"""

markdown_doc = generate_markdown_doc(code_snippet)
print(markdown_doc)
```

## Платформы
- Python 3.8+

## Краткое описание
Модуль предназначен для создания структурированной документации в формате Markdown из фрагментов кода Python.

## Функции

### `generate_markdown_doc(code_snippet)`

Функция преобразует фрагмент кода Python в Markdown-документацию, соответствующую заданному формату.

#### Параметры
- `code_snippet`: Фрагмент кода Python, для которого требуется сгенерировать документацию (строка).

#### Возвращаемое значение
- Строка, содержащая Markdown-документацию. Возвращает пустую строку, если ввод не соответствует ожидаемому формату.

#### Пример использования
```python
from doc_writer_md import generate_markdown_doc

code_snippet = """
def add(x, y):
    \"\"\"Складывает два числа.\"\"\"
    return x + y
"""

markdown_doc = generate_markdown_doc(code_snippet)
print(markdown_doc)
```

#### Возможные исключения
- `TypeError`: Если `code_snippet` не является строкой.


```python
# Пример обработки исключения
def process_doc_generation(code_snippet):
    try:
        markdown_doc = generate_markdown_doc(code_snippet)
        return markdown_doc
    except TypeError as e:
        return f"Ошибка: {e}"
```
```markdown
# Исключение: Некорректный формат кода

Это исключение возникает, если входной код не соответствует ожидаемому формату документации.


## Пример использования

```python
try:
    generate_markdown_doc("Некорректный код")
except ValueError as ex:
    print(ex)

```
```

```python
import pytest

def test_generate_markdown_doc_valid_code():
    """Проверка генерации Markdown для корректного кода."""
    code_snippet = """
def add(x, y):
    \"\"\"Складывает два числа.\"\"\"
    return x + y
"""
    expected_output = """# Функция: add\n\nФункция `add` складывает два числа.\n\n## Параметры\n- `x`: Первое число.\n- `y`: Второе число.\n\n## Возвращаемое значение\n- Возвращает сумму чисел `x` и `y`.\n\n## Пример использования\n\n```python\nresult = add(2, 3)\nprint(result)  # Вывод: 5\n```"""
    actual_output = generate_markdown_doc(code_snippet)
    assert actual_output == expected_output
```
```python
def test_generate_markdown_doc_invalid_code():
    """Проверка обработки некорректного кода."""
    code_snippet = "Некорректный код"
    expected_output = ""  #Ожидается пустая строка для некорректного кода.
    actual_output = generate_markdown_doc(code_snippet)
    assert actual_output == expected_output
```
```python
def test_generate_markdown_doc_type_error():
    """Проверка обработки ошибки типа."""
    code_snippet = 123  # Неправильный тип
    with pytest.raises(TypeError):
        generate_markdown_doc(code_snippet)
```
```