# סימולטור "מחשב של 10 סנט"

## סקירה כללית

מודול זה מדמה "מחשב של 10 סנט" כדי ללמד ילדים על מערכת המספרים הבינארית. הוא מייצג מספרים בינאריים באמצעות 4 "נורות" (0 - כבוי, 1 - דולק) המייצגות את הערכים 1, 2, 4 ו-8 בהתאמה.

## תוכן עניינים

- [פונקציות](#פונקציות)
    - [`convert_decimal_to_binary`](#convert_decimal_to_binary)
    - [`convert_binary_to_decimal`](#convert_binary_to_decimal)
    - [`explain_binary_representation`](#explain_binary_representation)
    - [`process_input`](#process_input)

## פונקציות

### `convert_decimal_to_binary`

**Description**: ממיר מספר עשרוני למקבילה הבינארית שלו עם 4 סיביות.

**Parameters**:
- `decimal` (int): מספר עשרוני שיש להמיר.

**Returns**:
- `str`: מחרוזת המייצגת את המספר הבינארי.

**Raises**:
- `ValueError`: אם המספר העשרוני אינו בטווח 0-15.

```python
def convert_decimal_to_binary(decimal: int) -> str:
    """
    Args:
        decimal (int): מספר עשרוני שיש להמיר.

    Returns:
        str: מחרוזת המייצגת את המספר הבינארי.

    Raises:
        ValueError: אם המספר העשרוני אינו בטווח 0-15.
    """
```

### `convert_binary_to_decimal`

**Description**: ממיר מספר בינארי למקבילה העשרונית שלו.

**Parameters**:
- `binary` (str): מחרוזת המייצגת את המספר הבינארי.

**Returns**:
- `int`: המספר העשרוני.

**Raises**:
- `ValueError`: אם המספר הבינארי אינו חוקי (לדוגמה, אינו מכיל בדיוק 4 תווים של 0 או 1).

```python
def convert_binary_to_decimal(binary: str) -> int:
    """
    Args:
        binary (str): מחרוזת המייצגת את המספר הבינארי.

    Returns:
        int: המספר העשרוני.

    Raises:
        ValueError: אם המספר הבינארי אינו חוקי (לדוגמה, אינו מכיל בדיוק 4 תווים של 0 או 1).
    """
```

### `explain_binary_representation`

**Description**: מספק הסבר כיצד מספר עשרוני מיוצג בבינארית.

**Parameters**:
- `binary` (str): מחרוזת המייצגת את המספר הבינארי.
- `decimal` (int): המספר העשרוני המקביל.

**Returns**:
- `str`: הסבר על הייצוג הבינארי.

```python
def explain_binary_representation(binary: str, decimal: int) -> str:
    """
    Args:
        binary (str): מחרוזת המייצגת את המספר הבינארי.
        decimal (int): המספר העשרוני המקביל.

    Returns:
        str: הסבר על הייצוג הבינארי.
    """
```

### `process_input`

**Description**: מעבד את קלט המשתמש ומחזיר את התגובה המתאימה.

**Parameters**:
- `user_input` (str): קלט המשתמש.

**Returns**:
- `str`: תגובת המערכת.

```python
def process_input(user_input: str) -> str:
    """
    Args:
        user_input (str): קלט המשתמש.

    Returns:
        str: תגובת המערכת.
    """