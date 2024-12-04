# מדריך לכתוב תיעוד עבור קובצי Python

## מבוא

המדריך מציג כיצד ליצור תיעוד Markdown עבור קובצי Python. התיעוד יכלול תיאור כללי, תיעוד של מחלקות, פונקציות ושיטות, וטיפול בשגיאות.

## מבנה תיעוד

### מבנה כללי

כל קובץ יתחיל בכותרת ותיאור קצר של תוכן הקובץ.  התיעוד יכלול פרקים עבור מחלקות, פונקציות, שיטות ומשתנים.

### תיעוד פונקציות/שיטות

כל פונקציה ושיטה תידרש בתיעוד RST:

```python
def my_function(param1: str, param2: int = 0) -> str:
    """
    תיאור הפונקציה.

    :param param1: תיאור פרמטר 1.
    :type param1: str
    :param param2: תיאור פרמטר 2 (ברירת מחדל 0).
    :type param2: int
    :raises ValueError: אם param1 אינו מחרוזת.
    :return: תיאור הערך המוחזר.
    :rtype: str
    """
    # גוף הפונקציה
    ...
```


### טיפול בשגיאות

שימוש ב- `logger.error` לטיפול בשגיאות:

```python
import logging
from src.logger import logger

def my_function():
    try:
        # קוד שעלול להכיל שגיאות
        ...
    except Exception as ex:
        logger.error("שגיאה בביצוע הפונקציה:", exc_info=True)
        return None
```


### תיעוד משתנים

משתנים חשובים יידרשו תיעוד RST:

```python
my_variable: str = "תיאור המשתנה" # תיעוד של משתנה
```

## דוגמה

```python
# דוגמה לפונקציה עם תיעוד
def my_function(param: str) -> int:
    """
    תיאור הפונקציה.

    :param param: תיאור של הפרמטר.
    :type param: str
    :raises ValueError: אם הפרמטר אינו מחרוזת.
    :return: תיאור הערך המוחזר.
    :rtype: int
    """
    try:
        # גוף הפונקציה
        result = int(param)
        return result
    except ValueError as e:
        logger.error("שגיאה בפירוק למספר:", exc_info=True)
        return -1

```

## טיפול בקבצים


### קריאת קבצים

השתמשו ב- `j_loads` או `j_loads_ns` (מתוך `src.utils.jjson`) לקריאת קבצים במקום `json.load`:

```python
from src.utils.jjson import j_loads

data = j_loads("path/to/file.json")
```

## הערות


כל שינוי בקוד יידרש הערות שורה ב- #, כגון:

```python
# תיקון שגיאת פונקציה
def my_function(...):
    # ... קוד נוסף
```

## סיכום

המדריך מספק הנחיות לתיעוד קוד Python בפורמט Markdown, כולל טיפול בתיעוד פונקציות, שיטות ומשתנים, טיפול בשגיאות וטיפול בקבצים.  השתמשו בתיעוד RST לכל הערות.