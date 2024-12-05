# קובץ `code_checker_he.py`

## סיכום

קובץ זה מכיל פונקציות לבדיקת קוד Python, ומציג תיעוד עבור כל פונקציה.

## תוכן עניינים

- [פונקציות](#פונקציות)


## פונקציות

### `check_file_format`

**תיאור**: בודקת אם קובץ Python עומד בדרישות פורמט מסוימות.

**פרמטרים**:
- `file_path` (str): נתיב הקובץ לבדיקה.
- `expected_format` (str, אופציונלי): פורמט צפוי לקובץ. ברירת מחדל: `'py'`

**החזרות**:
- `dict`: מילון שמכיל מידע על תוצאות הבדיקה.
    - `valid` (bool): `True` אם הקובץ עומד בדרישות, אחרת `False`.
    - `errors` (list, אופציונלי): רשימת שגיאות שהתגלו.

**הנאות**:
- `FileNotFoundError`: אם הקובץ אינו קיים.
- `ValueError`: אם הפורמט הצפוי אינו תקין.


```python
def check_file_format(file_path: str, expected_format: str = 'py') -> dict | None:
    """
    בודקת אם קובץ Python עומד בדרישות פורמט מסוימות.

    :param file_path: נתיב הקובץ לבדיקה.
    :type file_path: str
    :param expected_format: פורמט צפוי לקובץ. ברירת מחדל: 'py'
    :type expected_format: str
    :returns: מילון שמכיל מידע על תוצאות הבדיקה.
              - valid (bool): True אם הקובץ עומד בדרישות, אחרת False.
              - errors (list, אופציונלי): רשימת שגיאות שהתגלו.
    :rtype: dict | None
    :raises FileNotFoundError: אם הקובץ אינו קיים.
    :raises ValueError: אם הפורמט הצפוי אינו תקין.
    """
    try:
        # ... קוד לבדיקה ...
        pass
    exсept FileNotFoundError as ex:
        return {'valid': False, 'errors': [f'קובץ לא נמצא: {ex}']}
    except ValueError as ex:
        return {'valid': False, 'errors': [f'פורמט לא תקי: {ex}']}
```

<!-- TODO: להוסיף פונקציות נוספות לבדיקת קוד, כגון בדיקה של משתנים, יבואים, וכו' -->
```