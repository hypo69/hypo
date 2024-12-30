# סימולטור "מחשב עשר סנט"

## סקירה כללית

מודול זה הוא סימולטור של "מחשב עשר סנט" שמטרתו ללמד ילדים על מערכת המספרים הבינארית. הסימולטור מייצג מספרים בינאריים באמצעות 4 "נורות" (0 - נורה כבויה, 1 - נורה דולקת), כאשר כל נורה מייצגת ערך אחר של חזקה של 2 (1, 2, 4 ו-8 מימין לשמאל).

## תוכן עניינים

- [פונקציות](#פונקציות)
    - [`convert_decimal_to_binary`](#convert_decimal_to_binary)
    - [`convert_binary_to_decimal`](#convert_binary_to_decimal)

## פונקציות

### `convert_decimal_to_binary`

**Description**: ממירה מספר עשרוני למקבילה הבינארית שלו בת 4 סיביות.

**Parameters**:
- `decimal` (int): המספר העשרוני שיש להמיר.

**Returns**:
- `str`: מחרוזת המייצגת את המספר הבינארי עם 4 סיביות, או `None` אם המספר העשרוני אינו בין 0 ל-15.

**Raises**:
- None

```python
def convert_decimal_to_binary(decimal: int) -> str | None:
    """
    Args:
        decimal (int): המספר העשרוני שיש להמיר.

    Returns:
        str | None: מחרוזת המייצגת את המספר הבינארי עם 4 סיביות, או `None` אם המספר העשרוני אינו בין 0 ל-15.

    Raises:
        None
    """
    if not 0 <= decimal <= 15:
        return None
    binary = bin(decimal)[2:].zfill(4)
    return binary
```

### `convert_binary_to_decimal`

**Description**: ממירה מספר בינארי בעל 4 סיביות למקבילה העשרונית שלו.

**Parameters**:
- `binary` (str): מחרוזת המייצגת את המספר הבינארי עם 4 סיביות.

**Returns**:
- `int`: המספר העשרוני המקביל. מחזיר `None` אם מחרוזת הבינארי לא חוקית.

**Raises**:
- `ValueError`: אם מחרוזת הבינארי לא חוקית.

```python
def convert_binary_to_decimal(binary: str) -> int | None:
    """
    Args:
        binary (str): מחרוזת המייצגת את המספר הבינארי עם 4 סיביות.

    Returns:
        int | None: המספר העשרוני המקביל. מחזיר `None` אם מחרוזת הבינארי לא חוקית.

    Raises:
         ValueError: אם מחרוזת הבינארי לא חוקית.
    """
    if len(binary) != 4:
        return None
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError as ex:
        return None
```