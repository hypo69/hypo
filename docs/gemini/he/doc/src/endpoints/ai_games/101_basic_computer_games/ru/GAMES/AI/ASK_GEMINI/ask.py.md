# `ask.py`

## סקירה כללית

מודול זה מספק מחלקה `GoogleGenerativeAI` לשילוב עם מודלי Google Generative AI. הוא מאפשר לשלוח שאילתות למודל ומחזיר תגובות טקסט.

## תוכן עניינים

- [מחלקות](#מחלקות)
  - [`GoogleGenerativeAI`](#googlegenerativeai)
- [פונקציות](#פונקציות)
  - [`ask`](#ask)

## מחלקות

### `GoogleGenerativeAI`

**Description**:
מחלקה לאינטראקציה עם מודלי Google Generative AI.

**Methods**:
- [`__init__`](#__init__): אתחול מופע של `GoogleGenerativeAI`.
- [`ask`](#ask): שליחת שאילתה טקסטואלית למודל והחזרת התשובה.

#### `__init__`

```python
def __init__(self, api_key: str, system_instruction: str = '', model_name: str = 'gemini-2.0-flash-exp')
```

**Description**:
אתחול מודל GoogleGenerativeAI.

**Parameters**:
- `api_key` (str): מפתח API לגישה ל-Gemini.
- `system_instruction` (str, optional): הוראה למודל (פרומפט מערכת). ברירת מחדל: ''.
- `model_name` (str, optional): שם מודל Gemini בו משתמשים. ברירת מחדל: 'gemini-2.0-flash-exp'.

**Returns**:
- `None`

#### `ask`
```python
def ask(self, q: str) -> str
```

**Description**:
שולח שאילתת טקסט למודל ומחזיר את התשובה.

**Parameters**:
- `q` (str): השאלה שתשלח למודל.

**Returns**:
- `str`: התשובה מהמודל.

**Raises**:
- `Exception`: אם מתרחשת שגיאה במהלך הפנייה למודל.

## פונקציות

אין פונקציות גלובליות מוגדרות בתיעוד זה.