# `ten_cent_computer.py`

## סקירה כללית

קובץ זה מממש ממשק משתמש למשחקי AI, המשתמש במודלים של Google Generative AI. הוא מאפשר למשתמש לבחור בין משחקים שונים, להזין קלט ולראות את התגובות של המודל. הקובץ כולל גם פונקציונליות לאחסון מפתח API בסביבה או בקובץ `.env`.

## תוכן עניינים

1. [מחלקות](#מחלקות)
   - [`GoogleGenerativeAI`](#googlegenerativeai)
2. [פונקציות](#פונקציות)
   - [`set_key`](#set_key)
3. [קוד ראשי](#קוד-ראשי)

## מחלקות

### `GoogleGenerativeAI`

**Description**:
מחלקה ליצירת אינטראקציה עם מודלים של Google Generative AI.

**Methods**:

- `__init__`: מאתחל את המחלקה עם מפתח API, הוראה למערכת ושם מודל.
- `ask`: שולח שאילתה למודל ומחזיר את התשובה.

#### `__init__`

```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b'):
    """
    Args:
        api_key (str): מפתח API לגישה ל-Gemini.
        system_instruction (str): הוראה למודל (בקשה מערכת).
        model_name (str, optional): שם המודל Gemini שמשמש. ברירת מחדל: 'gemini-2-13b'.
    """
```

#### `ask`

```python
def ask(self, q: str) -> str:
    """
    Args:
        q (str): טקסט השאילתה.

    Returns:
        str: תשובת המודל או הודעת שגיאה.

    Raises:
        Exception: אם מתרחשת שגיאה במהלך שליחת השאילתה או קבלת התגובה.
    """
```

## פונקציות

### `set_key`

**Description**:
שומר זוג מפתח-ערך בקובץ `.env`.

```python
def set_key(dotenv_path: str, key: str, value: str):
    """
    Args:
        dotenv_path (str): נתיב לקובץ ה-.env.
        key (str): מפתח הערך שצריך לשמור.
        value (str): הערך שצריך לשמור.
    """
```

## קוד ראשי

**Description**:
חלק זה של הקוד מטפל בממשק המשתמש, טוען את מפתח ה-API, ומאפשר למשתמש לשחק משחקים שונים על ידי שאילתה של מודלים של AI.

**פונקציונליות**:

1. קובע את הנתיבים למשחקי ה-AI.
2. טוען מפתח API מהסביבה או מבקש אותו מהמשתמש אם הוא לא נמצא.
3. מגדיר הוראות שונות למשחקי AI.
4. מציג תפריט למשתמש לבחירת המשחק.
5. יוצר מופע של `GoogleGenerativeAI` עם ההוראה המתאימה למשחק הנבחר.
6. מאפשר למשתמש לשלוח שאילתות ולקבל תשובות מהמודל עד שהוא בוחר לצאת.

**הערה**: הקוד מובנה לשימוש עם משחקי AI מרובים, אך הדוגמה הנוכחית כוללת שני משחקים בלבד. ניתן להרחיב את הקוד בקלות כך שיכלול עוד משחקים על ידי הוספת הוראות ותנאים נוספים.
```python
if __name__ == '__main__':
    # הגדרת נתיבים
    __root__ = Path(__file__).resolve().parent
    relative_path: Path = Path('games', 'ai')
    base_path: Path = __root__ / relative_path

    # קריאת מפתח API
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('API מפתח לא נמצא. הכנס מפתח API מ `gemini`: ')
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {
        '1': 'input_output',
        '2': 'ten_cent_computer',
    }

    # ממשק משתמש
    print('ברוכים הבאים לעולם משחקי המתמטיקה!')
    print('בחר איזה משחק תרצה לשחק:')

    while True:
        print('1. משחק "קלט-פלט"')
        print('2. משחק "מחשב 10 סנט"')
        choice = input('הכנס מספר משחק (1 או 2, או "q" ליציאה): ')

        if choice == 'q':
            print('להתראות!')
            break

        if choice in ('1', '2'):
            system_instruction: str = Path(base_path, f'{instructions[choice]}.md').read_text(encoding='UTF-8')
            model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
            if choice == '1':
                while True:
                    user_input = input("הכנס שאילתה למשחק 'קלט-פלט' ('q' ליציאה): ")
                    if user_input.lower() == 'q':
                        break
                    response = model.ask(user_input)
                    print(response)

            elif choice == '2':
                while True:
                    user_input = input("הכנס שאילתה למשחק 'מחשב 10 סנט' ('q' ליציאה): ")
                    if user_input.lower() == 'q':
                        break
                    response = model.ask(user_input)
                    print(response)
        else:
            print('בחירה לא נכונה. נסה שוב.')