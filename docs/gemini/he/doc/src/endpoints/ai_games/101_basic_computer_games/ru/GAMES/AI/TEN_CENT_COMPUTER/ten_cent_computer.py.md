# ten_cent_computer.py

## סקירה כללית
קובץ זה מיישם משחק מחשב בסיסי באמצעות מודל שפה של Google Generative AI, וכולל גם פונקציונליות לקריאה והגדרה של מפתח API.

## תוכן עניינים
- [מחלקות](#מחלקות)
  - [GoogleGenerativeAI](#GoogleGenerativeAI)
- [פונקציות](#פונקציות)
  - [set_key](#set_key)
- [סקריפט ראשי](#סקריפט-ראשי)

## מחלקות

### `GoogleGenerativeAI`

**Description**:
מחלקה ליצירת אינטראקציה עם מודלים של Google Generative AI.

**Methods**:
- `__init__`: אתחול מופע של `GoogleGenerativeAI` עם מפתח API, הוראה למערכת ושם המודל.
- `ask`: שליחת שאילתה למודל וקבלת תשובה.

#### `__init__`

```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str): הוראה למודל (פרומפט מערכת).
        model_name (str, optional): שם מודל ה-Gemini לשימוש. ברירת מחדל: 'gemini-2-13b'.

    """
```

**Parameters**:
- `api_key` (str): מפתח API לגישה ל-Gemini.
- `system_instruction` (str): הוראה למודל (פרומפט מערכת).
- `model_name` (str, optional): שם מודל ה-Gemini לשימוש. ברירת מחדל: `gemini-2-13b`.

#### `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט השאילתה.

    Returns:
        str: תגובת המודל או הודעת שגיאה.
    """
```

**Description**:
שליחת שאילתה למודל וקבלת תשובה.

**Parameters**:
- `q` (str): טקסט השאילתה.

**Returns**:
- `str`: תגובת המודל או הודעת שגיאה.

## פונקציות

### `set_key`

```python
def set_key(dotenv_path: str, key: str, value: str):
    """
    Args:
        dotenv_path (str): נתיב לקובץ `.env`.
        key (str): מפתח להגדיר או לעדכן.
        value (str): ערך להגדרת המפתח.
    """
```

**Description**:
שומר צמד מפתח-ערך בקובץ ‎.env.

**Parameters**:
- `dotenv_path` (str): הנתיב לקובץ ה-`.env`.
- `key` (str): מפתח להגדרה או עדכון.
- `value` (str): הערך להגדרת המפתח.

## סקריפט ראשי

**Description**:
סקריפט ראשי המאפשר למשתמש לבחור ולשחק משחקי מחשב בסיסיים המופעלים על ידי מודל Gemini.

**הגיון**:
- קורא מפתח API מהסביבה או מבקש אותו מהמשתמש, ושומר אותו בקובץ `.env` אם הוא מסופק על ידי המשתמש.
- מציג תפריט משחקים למשתמש.
- טוען הוראות מערכת ספציפיות למשחק מהקבצים המתאימים בפורמט `md`.
- מפעיל משחק שנבחר על ידי המשתמש, מאפשר אינטראקציה עם המודל של גוגל ומדפיס את התגובה.
- מאפשר למשתמש לשחק משחקים שונים עד שהוא מחליט לצאת.