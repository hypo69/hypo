# Received Code

```python
### Code Rules:

1. **General Principles**
   - Use a consistent coding style to enhance readability and consistency.
   - All changes and recommendations must adhere to this format.

---

2. **Comments**
   - **Comments after the `#` symbol**:
     - **Do not modify**: Comments after the `#` symbol should remain unchanged and be clear. Do not rewrite or delete them, even if they start with code.
     - **Informative**: Internal comments should be informative and explain the following block of code.
     - **Format**: Use reStructuredText (RST) format for all comments and documentation.
     - **Terminology**: Avoid using terms like 'get', 'do' in comments. Instead, use phrases like 'check', 'send', 'code executes ...'.
     - **Passive forms**: Prefer passive forms: 'copying', 'formatting', 'creating', etc.
     - **Empty lines**: If there are empty lines or `...`, do not document them.

   - **Comments after the `"""` symbol**:
     - **Optimize**: Comments after the `"""` symbol can and should be optimized based on the actual behavior of the code.

---

3. **Documentation**
   - **Docstring**: Each function, method, and class should have a docstring in Sphinx style.
     - Example for a function:
       ```python
       def function(param: str, param1: Optional[str | dict] = None) -> dict | None:
           """
           Function description.

           :param param: Description of the `param` parameter.
           :param param1: (Optional) Description of the `param1` parameter.
           :return: Description of the return value.
           :raises SomeError: Conditions for the exception.
           """
       ```
   - **Module description**: Add a module description at the beginning of each file:
     ```python
     """
     Module for working with a programmer assistant
     =========================================================================================

     Description of the module functionality.

     Example usage
     -------------

     .. code-block:: python

         example_usage()
     """
     ```

---

4. **Code Formatting**
   - **Quotes**: Use single quotes instead of double quotes.
   - **Spaces**: Use spaces around the assignment operator `=`. Example:
     ```python
     a = 1
     ```
   - **Consistency**: Apply spaces consistently in all expressions and assignments:
     ```python
     result = 10 if x > 5 else 20
     ```
   - **Import header**: Always include the `import header` line at the beginning of the file.
   - **Debugging**: Add `...` between `logger` and `return` for debugging, example:
     ```python
     logger.error('Error while executing task', ex)
     ...
     return
     ```

---

5. **Function Parameters**
   - **Typing**: Parameters should be explicitly typed. If the default value is `None`, use `Optional`. Example:
     ```python
     def critical(self, message: str, ex: Optional = None, exc_info: Optional[bool] = True):
     ```
   - **Avoid Union**: Avoid using `Union`.

---

6. **Pydantic**
   - **Validation**: Use Pydantic for data validation if possible and appropriate.
   - **Models**: Prefer Pydantic models for classes handling structured data.

---

7. **Logging**
   - **Logger**: Use `from src.logger import logger` for logging instead of the standard `logging`.
   - **Error logging example**:
     ```python
     logger.error('Error while starting bot: ', ex)
     ...
     return
     ```

---

8. **Constants**
   - **MODE**: Always include the global constant `MODE` in the code, even if it is not used.

---

### Response Format:

All responses should follow the Markdown format.

The structure of the response should include:

- **Improved code**: A block with the improved code, formatted and with added comments.
- **Changes**: A detailed list of modifications and explanations.

Code should be enclosed in appropriate syntax highlighting tags (e.g., `python`, `markdown`, `json`).

---

### Examples:

#### Example 1 (Python Code):
Input:
```python
def add_numbers(a,b):
    return a+b
```

Expected response:

```


```
```


```
```python

```


```


```
```

# Improved Code

```python
# TODO: Add module docstring in RST format.
# TODO: Add function docstring in RST format.
# TODO: Add type hints.
# TODO: Add import statements for necessary modules.


def add_numbers(a: int, b: int) -> int:
    """
    Функция сложения двух чисел.

    :param a: Первое число.
    :type a: int
    :param b: Второе число.
    :type b: int
    :return: Сумма чисел a и b.
    :rtype: int
    """
    return a + b


```

# Changes Made

- Добавлены комментарии в формате RST к функции `add_numbers`.
- Добавлены аннотации типов для параметров `a` и `b`.
- Добавлены аннотации типов для возвращаемого значения.
- Исправлен стиль кода (пробелы вокруг оператора `+`).


# FULL Code

```python
# TODO: Add module docstring in RST format.
# TODO: Add function docstring in RST format.
# TODO: Add type hints.
# TODO: Add import statements for necessary modules.


def add_numbers(a: int, b: int) -> int:
    """
    Функция сложения двух чисел.

    :param a: Первое число.
    :type a: int
    :param b: Второе число.
    :type b: int
    :return: Сумма чисел a и b.
    :rtype: int
    """
    return a + b
```
```


```
```


```


```
```


```