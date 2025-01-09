# GoogleGenerativeAI מודול

## סקירה כללית

מודול זה מספק מחלקה `GoogleGenerativeAI` לאינטראקציה עם מודלי Google Generative AI.
הוא תוכנן כדי לאפשר למשתמשים לשלוח שאילתות ולעבד תגובות, במיוחד בהקשר של יצירת אנאגרמות מסט נתון של אותיות.

## תוכן עניינים

- [מחלקות](#מחלקות)
  - [`GoogleGenerativeAI`](#google-generative-ai)
- [פונקציות](#פונקציות)
  - [`ask`](#ask)
- [קבועים](#קבועים)
  - [`system_instruction`](#system_instruction)
  - [`API_KEY`](#api_key)

## מחלקות

### `GoogleGenerativeAI`

**Description**: מחלקה זו מטפלת בפעולות התקשורת עם מודלי Google Generative AI.

**Methods**:
- `__init__`: מאתחל מופע של המחלקה `GoogleGenerativeAI` עם מפתח API, הוראת מערכת ושם מודל.
- `ask`: שולח שאילתה למודל ומחזיר את התגובה.

#### `__init__`

```python
def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2.0-flash-exp") -> None:
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str, optional): הוראה למודל (פרומפט מערכת). ברירת מחדל: "".
        model_name (str, optional): שם מודל Gemini המשמש. ברירת מחדל: "gemini-2.0-flash-exp".
    
    Returns:
        None
    """
```

#### `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט השאילתה.

    Returns:
        str: תגובת המודל או הודעת שגיאה.

    Raises:
        Exception: אם מתרחשת שגיאה במהלך שליחת השאילתה.
    """
```

## פונקציות

### `ask`

**Description**: פונקציה זו שולחת שאילתה למודל ומחזירה את התגובה.

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט השאילתה.

    Returns:
        str: תגובת המודל או הודעת שגיאה.

    Raises:
        Exception: אם מתרחשת שגיאה במהלך שליחת השאילתה.
    """
```

## קבועים

### `system_instruction`

**Description**: הוראה למודל (פרומפט מערכת) להנחות אותו בייצור אנאגרמות.

```python
system_instruction = """
אתה מחולל אנאגרמות. המשימה שלך היא למצוא מילה קיימת בשפה הרוסית, המורכבת מקבוצה נתונה של אותיות (המשתמשת בכל או בחלקן).

חוקים:

1. התעלם מכל סמל מלבד אותיות רוסיות. אין להשתמש במספרים או בסמלים אחרים.
2. אם ניתן ליצור מספר מילים מהאותיות הנתונות, החזר אחת מהן.
3. אם לא ניתן ליצור אף מילה בשפה הרוסית מהאותיות הנתונות, החזר "אין אנאגרמות".
4. אל תיצור ניאולוגיזמים או מילים מומצאות. השתמש רק במילים קיימות בשפה הרוסית.
5. אל תסביר את התהליך, פשוט החזר מילה או "אין אנאגרמות".
"""
```

### `API_KEY`

**Description**: מפתח API עבור מודל gemini שנקלט מהמשתמש.

```python
API_KEY: str = input("API key from `gemini`: ")
```