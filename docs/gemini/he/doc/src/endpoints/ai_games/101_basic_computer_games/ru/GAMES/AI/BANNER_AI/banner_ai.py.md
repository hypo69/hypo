# `banner_ai.py`

## סקירה כללית

קובץ זה מכיל את היישום של משחק Banner AI, המשתמש ב-Google Generative AI ליצירת באנרים טקסטואליים בהתבסס על קלט מהמשתמש. הוא כולל תמיכה בבחירת סגנון עיצוב באנר והגדרת מפתח API באמצעות משתני סביבה.

## תוכן עניינים

1. [מחלקות](#classes)
    - [GoogleGenerativeAI](#googlegenerativeai)
2. [פונקציות](#functions)
    - [`ask`](#ask)
3. [הוראות הפעלה](#instructions)

## מחלקות

### `GoogleGenerativeAI`

**Description**: מחלקה זו נועדה לאינטראקציה עם מודלי Google Generative AI.

**Methods**:
- `__init__`: אתחול מודל `GoogleGenerativeAI`.
- `ask`: שליחת שאילתה למודל וקבלת תשובה.

#### `__init__`

```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str): הנחיה למודל (system prompt).
        model_name (str, optional): שם מודל Gemini בשימוש. ברירת מחדל: `'gemini-2.0-flash-exp'`.
    """
```

**Description**: מאתחל את מודל `GoogleGenerativeAI` עם מפתח API, הנחיית מערכת ושם מודל.

**Parameters**:
- `api_key` (str): מפתח API לגישה ל-Gemini.
- `system_instruction` (str): הנחיה למודל (system prompt).
- `model_name` (str, optional): שם מודל Gemini בשימוש. ברירת מחדל: `'gemini-2.0-flash-exp'`.

#### `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט השאילתה.

    Returns:
        str: תשובת המודל או הודעת שגיאה.
    """
```

**Description**: שולח שאילתה למודל ומחזיר את התשובה.

**Parameters**:
- `q` (str): טקסט השאילתה.

**Returns**:
- `str`: תשובת המודל או הודעת שגיאה.

## פונקציות

### `ask`

**Description**: שליחת שאילתה למודל וקבלת תשובה.

**Parameters**:
    - `q` (str): טקסט השאילתה.

**Returns**:
    - `str`: תשובת המודל או הודעת שגיאה.

**Raises**:
    - `Exception`: אם מתרחשת שגיאה כלשהי בזמן שליחת השאילתה.

## הוראות הפעלה

1.  ודא שמפתח ה-API של Gemini שלך מוגדר כמשתנה סביבה `API_KEY` או הזן אותו כאשר תתבקש.
2.  בחר סגנון עיצוב באנר מבין האפשרויות המוצגות.
3.  הזן את הטקסט הרצוי לבאנר.
4.  הבאנר הטקסטואלי שנוצר על ידי מודל Gemini יוצג.