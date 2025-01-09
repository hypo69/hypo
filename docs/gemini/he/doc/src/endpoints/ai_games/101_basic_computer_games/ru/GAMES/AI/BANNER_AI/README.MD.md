# BANNER_AI

## סקירה כללית

מודול זה משתמש במודל Google Generative AI ליצירת באנרים טקסטואליים בפורמט ASCII, בהתאם להוראות הניתנות למודל. התוכנית מאפשרת למשתמש לבחור סגנון עיצוב לבאנר ולספק טקסט לעיבוד.

## תוכן עניינים
1. [סקירה כללית](#סקירה-כללית)
2. [התקנת תלויות](#התקנת-תלויות)
3. [תכונות של הקוד](#תכונות-של-הקוד)
4. [יבוא ספריות](#1-יבוא-ספריות-הכרחיות)
5. [טעינת משתני סביבה](#2-טעינת-משתני-סביבה)
6. [מחלקה `GoogleGenerativeAI`](#3-מחלקה-googlegenerativeai)
    - [מאפייני המחלקה](#31-מאפייני-המחלקה)
    - [שיטת `__init__`](#32-שיטת-__init__)
    - [שיטת `ask`](#33-שיטת-ask)
7. [חלק עיקרי של התוכנית](#4-חלק-עיקרי-של-התוכנית)
    - [הגדרת נתיבים](#41-הגדרת-נתיבים)
    - [קריאת מפתח API](#42-קריאת-מפתח-api)
    - [הוראות למודל](#43-הוראות-למודל)
    - [ברכת משתמש](#44-ברכת-משתמש)
    - [בחירת סגנון באנר](#45-מחזור-לבחירת-סגנון-באנר)
    - [קריאת הוראה למודל](#46-קריאת-הוראה-למודל)
    - [יצירת מופע של המחלקה](#47-יצירת-מופע-של-המחלקה)
    - [קבלת טקסט מהמשתמש](#48-קבלת-טקסט-מהמשתמש)
    - [בדיקת טקסט](#49-בדיקת-טקסט)

## התקנת תלויות
כדי להפעיל את הקוד במחשב מקומי, יש להתקין את ספריות Google הבאות:
```python
pip install google
pip install google-generativeai
```
מומלץ לבצע את כל הניסויים בסביבה וירטואלית.

## תכונות של הקוד
1. ההוראות מאוחסנות בקבצים שונים ונטענות לפי הצורך.
2. החל מדוגמה זו, מפתח המודל נשמר במשתנה סביבה, מה שמונע את הצורך להזין את המפתח שוב ושוב.
3. נעשה שימוש בנתיבים מוחלטים לקבצים. כדי לקבוע את ספריית השורש של הפרויקט, מתבצע חיפוש רקורסיבי כלפי מעלה אחר קבצי סימון ('pyproject.toml', 'requirements.txt', '.git'). ספריית השורש מאוחסנת במשתנה `__root__`. ממנה נבנה הנתיב להוראות המערכת:
    ```python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # נתיב יחסי לספרייה
    base_path: Path = __root__ / relative_path  # נתיב מוחלט לספרייה באמצעות __root__
    ```

### 1. **יבוא ספריות הכרחיות**
```python
import google.generativeai as genai
import re
from pathlib import Path
from header import __root__
from dotenv import load_dotenv, set_key
import os
```
- **`google.generativeai`**: משמש לאינטראקציה עם Google Generative AI API.
- **`re`**: ספרייה לטיפול בביטויים רגולריים (לא בשימוש בקוד הנוכחי, אך יכולה להיות שימושית בעתיד).
- **`Path`**: משמש לטיפול בנתיבי מערכת הקבצים.
- **`__root__`**: אובייקט המכיל את הנתיב המוחלט לשורש הפרויקט.
- **`dotenv`**: משמש לטעינת משתני סביבה מקובץ `.env` ולשמירתם.
- **`os`**: משמש לטיפול במשתני סביבה.

---
### 2. **טעינת משתני סביבה**
```python
load_dotenv()
```
- הפונקציה `load_dotenv()` טוענת משתני סביבה מקובץ `.env`, אם הוא קיים.

---
### 3. **מחלקה `GoogleGenerativeAI`**
המחלקה מיועדת לאינטראקציה עם מודל Google Generative AI.

#### 3.1. **מאפייני המחלקה**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- רשימה של מודלי Google Generative AI זמינים.

#### 3.2. **שיטת `__init__`**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str): הוראה למודל (הנחיה מערכתית).
        model_name (str, optional): שם מודל ה-Gemini לשימוש. ברירת מחדל: 'gemini-2.0-flash-exp'.

    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # הגדרת הספריה עם מפתח API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # אתחול מודל עם הוראות
```
- **`api_key`**: מפתח API לגישה ל-Google Generative AI.
- **`system_instruction`**: הוראה למודל (לדוגמה, סגנון עיצוב טקסט).
- **`model_name`**: שם המודל, ברירת מחדל 'gemini-2.0-flash-exp'.
- **`genai.configure(api_key=self.api_key)`**: הגדרת הספריה באמצעות מפתח ה-API.
- **`genai.GenerativeModel(...)`**: אתחול המודל עם הפרמטרים שצוינו.

#### 3.3. **שיטת `ask`**
```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט הבקשה.

    Returns:
        str: תגובת המודל או הודעת שגיאה.
    
    Raises:
        Exception: אם מתרחשת שגיאה במהלך השאילתה למודל.
    """
    try:
        response = self.model.generate_content(q)
        return response.text
    except Exception as ex:
        return f'Error: {str(ex)}'
```
- **`q`**: טקסט הבקשה שנשלח למודל.
- **`self.model.generate_content(q)`**: שליחת בקשה למודל.
- **`response.text`**: קבלת תגובה טקסטואלית מהמודל.
- **`except Exception as ex`**: טיפול בשגיאות והחזרת הודעת שגיאה.

---

### 4. **חלק עיקרי של התוכנית**
```python
if __name__ == '__main__':
```
- בדיקה שהתוכנית מופעלת כסקריפט עצמאי.

#### 4.1. **הגדרת נתיבים**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')
base_path: Path = __root__ / relative_path
```
- **`relative_path`**: נתיב יחסי לספרייה בתוך הפרויקט.
- **`base_path`**: נתיב מוחלט, המתקבל מאיחוד `__root__` ו-`relative_path`.

#### 4.2. **קריאת מפתח API**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')
    set_key('.env', 'API_KEY', API_KEY)
```
- **`os.getenv('API_KEY')`**: ניסיון לקבל את מפתח ה-API ממשתני הסביבה.
- אם המפתח לא נמצא, הוא מבוקש מהמשתמש באמצעות `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: שמירת המפתח שהוזן בקובץ `.env` לשימוש עתידי.

#### 4.3. **הוראות למודל**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- מילון המכיל שמות קבצים עם הוראות למודל.

#### 4.4. **ברכת משתמש**
```python
print('Добро пожаловать в игру Banner!')
print('Введите текст, и я создам для вас текстовый баннер.')
```
- ברכת משתמש והסבר על פונקציונליות התוכנית.

#### 4.5. **מחזור לבחירת סגנון באנר**
```python
while True:
    print('Выберите стиль оформления баннера:')
    print('1. Символ \'*\'')
    print('2. Символ \'~\'')
    print('3. Символ \'#\'')
    choice = input('Введите номер стиля (1, 2 или 3): ')
```
- המשתמש בוחר את סגנון העיצוב של הבאנר.

#### 4.6. **קריאת הוראה למודל**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')
else:
    print('Неверный выбор. Используется стиль по умолчанию \'*\'')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')
```
- אם הבחירה נכונה, ההוראה המתאימה נקראת מהקובץ.
- אם הבחירה לא נכונה, נעשה שימוש בהוראת ברירת מחדל.

#### 4.7. **יצירת מופע של המחלקה**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- יצירת מופע של המחלקה `GoogleGenerativeAI` עם הפרמטרים שצוינו.

#### 4.8. **קבלת טקסט מהמשתמש**
```python
user_text: str = input('Введите текст для баннера: ')
```
- המשתמש מזין את הטקסט עבור הבאנר.

#### 4.9. **בדיקת טקסט**
```python
if user_text.strip() == '':
    print('Вы не ввели текст. Попробуйте снова.')
else:
    response = model.ask(user_text)
    print('\nВаш баннер готов:')
    print(response)
```
- אם הטקסט ריק, מוצגת הודעת שגיאה.
- אם הטקסט הוזן, הוא נשלח למודל, והתוצאה מוצגת.