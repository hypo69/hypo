# מודול `GoogleGenerativeAI`

## סקירה כללית

מודול זה מספק מחלקה `GoogleGenerativeAI` לשימוש ב-Google Gemini API. הוא מאפשר ליצור מודלים ולהפעיל אותם על בסיס הוראות מערכת, תוך טיפול בשגיאות.

## תוכן עניינים

1. [מחלקות](#מחלקות)
    - [`GoogleGenerativeAI`](#googlegenerativeai)
2. [פונקציות](#פונקציות)
    - [`__init__`](#__init__)
    - [`ask`](#ask)

## מחלקות

### `GoogleGenerativeAI`

**Description**: מחלקה המאפשרת אינטראקציה עם Google Gemini API.

**Methods**:
- [`__init__`](#__init__): מאתחל את המופע של המחלקה.
- [`ask`](#ask): שולח שאילתה למודל ומחזיר את התגובה.

## פונקציות

### `__init__`

**Description**: מאתחל מופע של המחלקה `GoogleGenerativeAI`.

```python
def __init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp') -> None:
    """
    Args:
        api_key (str): מפתח API של Google Gemini.
        system_instruction (str, optional): הוראת מערכת שתגדיר את התנהגות המודל. ברירת מחדל: ''.
        model_name (str, optional): שם המודל שבו יש להשתמש. ברירת מחדל: 'gemini-2.0-flash-exp'.

    Returns:
        None: הפונקציה אינה מחזירה ערך.
    """
```

**Parameters**:
- `api_key` (str): מפתח API של Google Gemini.
- `system_instruction` (str, optional): הוראת מערכת שתגדיר את התנהגות המודל. ברירת מחדל: `''`.
- `model_name` (str, optional): שם המודל שבו יש להשתמש. ברירת מחדל: `'gemini-2.0-flash-exp'`.

**Returns**:
- `None`: הפונקציה אינה מחזירה ערך.

### `ask`

**Description**: שולח שאילתה למודל ומחזיר את התגובה הטקסטואלית.

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): השאילתה שנשלחת למודל.

    Returns:
        str: התגובה הטקסטואלית מהמודל או הודעת שגיאה במקרה של כישלון.

    Raises:
        Exception: שגיאה במקרה של כישלון במהלך התקשורת עם המודל.
    """
```

**Parameters**:
- `q` (str): השאילתה שנשלחת למודל.

**Returns**:
- `str`: התגובה הטקסטואלית מהמודל או הודעת שגיאה במקרה של כישלון.

**Raises**:
- `Exception`: שגיאה במקרה של כישלון במהלך התקשורת עם המודל.