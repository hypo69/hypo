# מודול `ask.py`

## סקירה כללית

מודול זה מספק אינטראקציה עם מודלי Google Generative AI, בעיקר באמצעות המחלקה `GoogleGenerativeAI`. הוא מאפשר שליחת שאילתות טקסט וקבלת תגובות.

## תוכן עניינים

- [מחלקות](#מחלקות)
    - [`GoogleGenerativeAI`](#googlegenerativeai)
- [פונקציות](#פונקציות)
    - [`ask`](#ask)

## מחלקות

### `GoogleGenerativeAI`

**Description**: מחלקה ליצירת אינטראקציה עם מודלים של Google Generative AI.

**Methods**:
- `__init__`: אתחול המודל עם מפתח API, הוראות מערכת ושם מודל.
- `ask`: שליחת שאילתת טקסט למודל וקבלת תגובה.

#### `__init__`
```python
def __init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str, optional): הוראה למודל (פרומפט מערכת). ברירת מחדל: ''.
        model_name (str, optional): שם מודל ה-Gemini בו יש להשתמש. ברירת מחדל: 'gemini-2.0-flash-exp'.
    """
```
**Description**: אתחול מודל ה-GoogleGenerativeAI.

**Parameters**:
- `api_key` (str): מפתח API לגישה ל-Gemini.
- `system_instruction` (str, optional): הוראה למודל (פרומפט מערכת). ברירת מחדל: ''.
- `model_name` (str, optional): שם מודל ה-Gemini בו יש להשתמש. ברירת מחדל: 'gemini-2.0-flash-exp'.

#### `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): השאלה שתישלח למודל.

    Returns:
        str: תגובה מהמודל.
    """
```

**Description**: שולח שאילתת טקסט למודל ומחזיר תגובה.

**Parameters**:
- `q` (str): השאלה שתישלח למודל.

**Returns**:
- `str`: תגובה מהמודל.

**Raises**:
- `Exception`: במקרה של שגיאה במהלך יצירת התגובה, יוחזר הודעת שגיאה.

## פונקציות
### `ask`
```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): השאלה שתישלח למודל.

    Returns:
        str: תגובה מהמודל.
    """
```

**Description**: שולח שאילתת טקסט למודל ומחזיר תגובה.

**Parameters**:
- `q` (str): השאלה שתישלח למודל.

**Returns**:
- `str`: תגובה מהמודל.

**Raises**:
- `Exception`: במקרה של שגיאה במהלך יצירת התגובה, יוחזר הודעת שגיאה.