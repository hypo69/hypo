# BANNER AI

## סקירה כללית

מודול זה משתמש במודל Gemini כדי ליצור באנרים בפורמט ASCII על פי הנחיות נתונות.
התוכנית יוצרת אינטראקציה עם מודל Google Generative AI ליצירת באנרים טקסטואליים.
המשתמש יכול לבחור סגנון לבאנר ולשלוח טקסט לעיבוד.

## תוכן עניינים
1. [התקנת תלויות](#התקנת-תלויות)
2. [ייבוא ספריות](#ייבוא-ספריות)
3. [טעינת משתני סביבה](#טעינת-משתני-סביבה)
4. [מחלקה `GoogleGenerativeAI`](#מחלקה-googlegenerativeai)
    - [אтрибуטים של המחלקה](#אтрибуטים-של-המחלקה)
    - [שיטת `__init__`](#שיטת-__init__)
    - [שיטת `ask`](#שיטת-ask)
5. [החלק העיקרי של התוכנית](#החלק-העיקרי-של-התוכנית)
    - [הגדרת נתיבים](#הגדרת-נתיבים)
    - [קריאת מפתח API](#קריאת-מפתח-api)
    - [הוראות למודל](#הוראות-למודל)
    - [פנייה למשתמש](#פנייה-למשתמש)
    - [בחירת סגנון באנר](#בחירת-סגנון-באנר)
    - [קריאת הוראות למודל](#קריאת-הוראות-למודל)
    - [יצירת מופע של המחלקה](#יצירת-מופע-של-המחלקה)
    - [קלט מהמשתמש](#קלט-מהמשתמש)
    - [בדיקת טקסט](#בדיקת-טקסט)


## התקנת תלויות

לצורך הפעלת הקוד במכונה מקומית, נדרשת התקנה של ספריות גוגל.

```python
pip install google
pip install google-generativeai
```

מומלץ לבצע את כל הניסויים בסביבה וירטואלית.

## מאפייני קוד בתוכנית זו

1. ההוראות מאוחסנות בקבצים שונים ונטענות לפי הצורך.
2. החל מדוגמה זו, מפתח המודל נשמר במשתנה סביבה, מה שמבטל את הצורך להזין את המפתח שוב ושוב.
3. משתמשים בנתיבים מוחלטים לקבצים.
    לצורך קביעת ספריית השורש של הפרויקט, מתבצע חיפוש רקורסיבי כלפי מעלה אחר קבצי סימון ('pyproject.toml', 'requirements.txt', '.git').
    הספרייה שנמצאה נשמרת במשתנה `__root__`. ממנה נבנה הנתיב להוראות המערכת:

    ```python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
    ```

## ייבוא ספריות

```python
import google.generativeai as genai  # ייבוא ספרייה לעבודה עם Gemini
import re  # ייבוא ספרייה לעבודה עם ביטויים רגולריים
from pathlib import Path  # ייבוא לעבודה עם נתיבי מערכת קבצים
from header import __root__  # ייבוא אובייקט __root__, המכיל נתיב מוחלט לשורש הפרויקט
from dotenv import load_dotenv, set_key  # ייבוא פונקציות לעבודה עם משתני סביבה
import os  # ייבוא לעבודה עם משתני סביבה
```

- **`google.generativeai`**: משמש לאינטראקציה עם Google Generative AI API.
- **`re`**: ספרייה לעבודה עם ביטויים רגולריים (לא בשימוש בקוד זה, אך עשוי להיות שימושי בעתיד).
- **`Path`**: מאפשר עבודה עם נתיבי מערכת קבצים.
- **`__root__`**: אובייקט המכיל את הנתיב המוחלט לשורש הפרויקט.
- **`dotenv`**: מאפשר טעינת משתני סביבה מקובץ `.env` ושמירתם.
- **`os`**: משמש לעבודה עם משתני סביבה.

## טעינת משתני סביבה

```python
load_dotenv()
```

- הפונקציה `load_dotenv()` טוענת משתני סביבה מקובץ `.env` אם הוא קיים.

## מחלקה `GoogleGenerativeAI`

מחלקה זו נועדה ליצור אינטראקציה עם מודל Google Generative AI.

### אטריבוטים של המחלקה

```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```

- רשימה של מודלי Google Generative AI זמינים.

### שיטת `__init__`

```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str): הוראה למודל (פרומפט מערכת).
        model_name (str, optional): שם מודל Gemini בו משתמשים. ברירת מחדל: 'gemini-2.0-flash-exp'.
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # הגדרת הספרייה עם מפתח API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול המודל עם ההוראות
```
- `api_key`: מפתח API לגישה ל-Google Generative AI.
- `system_instruction`: הוראה למודל (למשל, סגנון עיצוב הטקסט).
- `model_name`: שם המודל, ברירת המחדל היא `gemini-2.0-flash-exp`.
- `genai.configure(api_key=self.api_key)`: הגדרת הספריה באמצעות מפתח ה-API.
- `genai.GenerativeModel(...)`: אתחול המודל עם הפרמטרים שצוינו.

### שיטת `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט הבקשה.

    Returns:
        str: תשובת המודל או הודעת שגיאה.
    """
    try:
        response = self.model.generate_content(q)  # שליחת בקשה למודל
        return response.text  # קבלת תגובה טקסטואלית
    except Exception as ex:
        return f'Error: {str(ex)}'  # טיפול וקבלת שגיאה
```
- `q`: טקסט הבקשה שנשלח למודל.
- `self.model.generate_content(q)`: שליחת הבקשה למודל.
- `response.text`: קבלת התגובה הטקסטואלית מהמודל.
- `except Exception as ex`: טיפול בשגיאות והחזרת הודעת שגיאה.

## החלק העיקרי של התוכנית

```python
if __name__ == '__main__':
```
- בדיקה שהתוכנית מופעלת כסקריפט עצמאי.

### הגדרת נתיבים

```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
```
- `relative_path`: נתיב יחסי לספרייה בתוך הפרויקט.
- `base_path`: נתיב מוחלט שמתקבל משילוב של `__root__` ו-`relative_path`.

### קריאת מפתח API

```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # בקשת מפתח API מהמשתמש
    set_key('.env', 'API_KEY', API_KEY)  # שמירת המפתח בקובץ .env
```
- `os.getenv('API_KEY')`: מנסים לקבל את מפתח ה-API ממשתני הסביבה.
- אם המפתח לא נמצא, מבקשים אותו מהמשתמש באמצעות `input`.
- `set_key('.env', 'API_KEY', API_KEY)`: שומרים את המפתח שהוזן בקובץ `.env` לשימוש עתידי.

### הוראות למודל

```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- מילון המכיל את שמות הקבצים עם ההוראות למודל.

### פנייה למשתמש

```python
print('Добро пожаловать в игру Banner!')
print('Введите текст, и я создам для вас текстовый баннер.')
```
- פנייה למשתמש והסבר על פונקציונליות התוכנית.

### בחירת סגנון באנר

```python
while True:
    print('Выберите стиль оформления баннера:')
    print('1. Символ \'\\*\'')
    print('2. Символ \'~\'')
    print('3. Символ \'#\'')
    choice = input('Введите номер стиля (1, 2 или 3): ')
```
- המשתמש בוחר סגנון לעיצוב הבאנר.

### קריאת הוראות למודל

```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # קריאת ההוראה מהקובץ
else:
    print('Неверный выбор. Используется стиль по умолчанию \'\\*\'')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # קריאת הוראת ברירת מחדל
```
- אם הבחירה נכונה, נקראת ההוראה המתאימה מהקובץ.
- אם הבחירה שגויה, נעשה שימוש בהוראת ברירת המחדל.

### יצירת מופע של המחלקה

```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- יצירת מופע של המחלקה `GoogleGenerativeAI` עם הפרמטרים שצוינו.

### קלט מהמשתמש

```python
user_text: str = input('Введите текст для баннера: ')
```
- המשתמש מזין טקסט עבור הבאנר.

### בדיקת טקסט

```python
if user_text.strip() == '':
    print('Вы не ввели текст. Попробуйте снова.')
else:
    response = model.ask(user_text)
    print('\nВаш баннер готов:')
    print(response)
```
- אם הטקסט ריק, מוצגת הודעת שגיאה.
- אם הטקסט הוזן, הוא נשלח למודל והתוצאה מוצגת.