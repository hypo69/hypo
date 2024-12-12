# Название модуля: code_explainer_md_en.md

## Обзор

Этот модуль содержит инструкции для генерации документации для разработчиков в формате Markdown. Он описывает структуру и содержание документации, включая оглавление, форматирование, заголовки разделов и примеры. Инструкция также включает примеры анализа кода, алгоритмы и объяснения, а также описывает, как использовать HTML в описании узлов в диаграммах Mermaid.

## Содержание

- [Обзор](#обзор)
- [Инструкция](#инструкция)
    - [Формат документации](#формат-документации)
    - [Содержание (TOC)](#содержание-toc)
    - [Форматирование документации](#форматирование-документации)
    - [Заголовки разделов](#заголовки-разделов)
    - [Пример файла](#пример-файла)
- [Входной код](#входной-код)
- [Пример запроса](#пример-запроса)
- [Ожидаемый ответ](#ожидаемый-ответ)
- [Инструкции по созданию диаграмм Mermaid](#инструкции-по-созданию-диаграмм-mermaid)
- [Пример диаграммы](#пример-диаграммы)
- [Генерация узлов](#генерация-узлов)
- [Метки и комментарии](#метки-и-комментарии)
- [Проверка синтаксиса](#проверка-синтаксиса)
- [Формат текста ответа](#формат-текста-ответа)

## Инструкция

### Формат документации

- Используйте стандарт `Markdown (.md)`.
- Каждый файл должен начинаться с заголовка и краткого описания его содержимого.
- Для всех классов и функций используйте следующий формат комментариев:

  ```python
  def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
      """
      Args:
          param (str): Описание параметра `param`.
          param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

      Returns:
          dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

      Raises:
          SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
      """
  ```
- Используйте `ex` вместо `e` в блоках обработки исключений.

### Содержание (TOC)

- В начале каждого файла документации добавьте раздел с оглавлением.
- Структура оглавления должна включать ссылки на все основные разделы документации модуля.

### Форматирование документации

- Используйте правильный синтаксис Markdown для всех заголовков, списков и ссылок.
- Для документирования классов, функций и методов включайте структурированные разделы с описаниями, деталями параметров, возвращаемых значений и вызываемых исключений. Пример:

  ```markdown
  ## Функции

  ### `function_name`

  **Описание**: Краткое описание функции.

  **Параметры**:
  - `param` (str): Описание параметра `param`.
  - `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

  **Возвращает**:
  - `dict | None`: Описание возвращаемого значения.

  **Вызывает исключения**:
  - `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
  ```

### Заголовки разделов

- Используйте заголовки первого уровня (`#`), второго уровня (`##`), третьего уровня (`###`) и четвёртого уровня (`####`) последовательно на протяжении всего файла.

### Пример файла

```markdown
# Название модуля

## Обзор

Краткое описание назначения модуля.

## Классы

### `ClassName`

**Описание**: Краткое описание класса.

**Методы**:
- `method_name`: Краткое описание метода.
- `method_name`: Краткое описание метода.
**Параметры**:
- `param` (str): Описание параметра `param`.
- `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.


## Функции

### `function_name`

**Описание**: Краткое описание функции.

**Методы**:
- `method_name`: Краткое описание метода.
- `method_name`: Краткое описание метода.****

**Параметры**:
- `param` (str): Описание параметра `param`.
- `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Описание возвращаемого значения.

**Вызывает исключения**:
- `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
```

## Входной код

```
**Prompt**:  
Your task is to help the developer of the code of the project `hypotez` explain to the developer how the code works
### Requirements:  
Analyze the provided code and explain its functionality.

### Response Format:  

```
<input code>
<algorithm>
<explanation>
```

1. **<input code>**:  
   - Provide the given code without any modifications.  

2. **<algorithm>**:  
   - Describe the code's workflow in a step-by-step block diagram format.  
   - For each logical block, provide examples of how it works (if applicable).  
   - Show how data flows between functions, classes, or methods.  

3. **<explanation>**:  
   - Provide a detailed description:  
     - Imports: Explain their purpose and describe their relationship with other packages, especially those starting with `src.` (if applicable).  
     - Classes: Detail their purpose, attributes, and methods, as well as their relationships with other project components.  
     - Functions: Explain their purpose, arguments, return values, and include examples.  
     - Variables: Describe their types and usage.  
   - Build a chain of relationships with other parts of the project (if any).  
   - Highlight potential errors or areas for improvement, if any.  

---

**Example Request**:  

```python
from src.utils.calculator import calculate_sum

def add_numbers(a, b):
    result = calculate_sum(a, b)
    return result
```
```

## Пример запроса

```python
from src.utils.calculator import calculate_sum

def add_numbers(a, b):
    result = calculate_sum(a, b)
    return result
```

## Ожидаемый ответ

```
<input code>
from src.utils.calculator import calculate_sum

def add_numbers(a, b):
    result = calculate_sum(a, b)
    return result

<algorithm>
1. The function `calculate_sum` is imported from the `src.utils.calculator` module.
2. A function `add_numbers` is defined, taking two arguments, `a` and `b`.
3. The `calculate_sum(a, b)` function is called to compute the sum of `a` and `b`.
4. The result of the function is returned to the caller.

Example:  
- Input: `a = 3`, `b = 5`.  
- Algorithm: `calculate_sum(3, 5)`.  
- Result: `8`.  

<explanation>
**Imports**:  
- `from src.utils.calculator import calculate_sum`: Imports the `calculate_sum` function, which is used to perform the addition. This module is located in the `src.utils` package.

**Function `add_numbers`**:  
- Purpose: Simplifies the addition of two numbers by utilizing the `calculate_sum` function.  
- Arguments:  
  - `a` (number): The first operand.  
  - `b` (number): The second operand.  
- Return Value: The result of adding `a` and `b`.  

**Relationship with Other Packages**:  
- The `src.utils.calculator` module is likely part of a library for mathematical operations.  
- If `calculate_sum` relies on additional modules, this can be clarified in its documentation.

**Possible Improvements**:  
- Add type checks for the `a` and `b` arguments to prevent errors.  
- Localize the `calculate_sum` call within the module if it is not reused elsewhere.
```

## Инструкции по созданию диаграмм Mermaid

1. **Graph Type:**
    - Use `flowchart` (e.g., `flowchart TD` for a top-to-bottom directed graph).
    - Other options: `LR` (left-to-right), `BT` (bottom-to-top), `RL` (right-to-left).

2. **Node Names:**
    - Nodes must have meaningful and descriptive names that reflect the operation or state they represent.
    - Avoid names like `A`, `B`, `C`. Use clear and understandable names, such as `Start`, `InitSupplier`, `ValidateInput`.

3. **Using HTML:**
    - Apply HTML tags to style the text in nodes.
    - Supported tags include text formatting (e.g., `<b>`, `<i>`, `<h1>`, `<h3>`, `<code>`).
    - Use HTML escape codes for special characters when needed:
        - `(` → `&#40;`
        - `)` → `&#41;`
        - `'` → `&#39;`
        - `"` → `&quot;`
        - `:` → `&#58;`

4. **Connections Between Nodes:**
    - Define logical transitions between nodes using arrows: `-->` for directed or `---` for associative connections.
    - Add text labels to arrows to clarify transition conditions, e.g., `-->|Success|`.

## Пример диаграммы

```mermaid
flowchart TD
    Start[<html>Start of the process<br><b>Create instance</b></html>] 
        --> InitSupplier[<html>Initialize Supplier<br><code>_payload&#40;params&#41;</code></html>]
    InitSupplier --> Validate[<html>Validate parameters<br><i>is_valid&#40;params&#41;</i></html>]
    Validate -->|Validation passed| Success[<html><b>Success</b><br>Creation completed</html>]
    Validate -->|Error| Error[<html>Error<br><span style="color:red;">Invalid parameters</span></html>]
```

## Генерация узлов

- Generate node names based on the action or state they represent.
- Nodes should be concise but informative. Use HTML tags to enhance readability where needed.

## Метки и комментарии

- Add labels to arrows to explain transition conditions.
- Use comments with `%%` to describe complex connections.

## Проверка синтаксиса

- Ensure the HTML inside nodes is valid and does not break Mermaid syntax.

## Формат текста ответа

`UTF-8`