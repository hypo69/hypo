
  "prompt": "אתה צריך לתעד את הקוד בסגנון הבא. כל ההערות בקוד, כולל תיאורי המודול, מחלקות ופונקציות, צריכות להיות כתובות בפורמט reStructuredText (RST). לכל מודול, מחלקה ופונקציה, עקוב אחרי התבנית הבאה:

1. **מודול**:
    - תיאור המודול צריך להיכתב בכותרת, תוך ציון מטרתו.
    - ספק דוגמאות לשימוש במודול, אם אפשר. דוגמאות קוד צריכות להיות בתוך בלוק `.. code-block:: python`.
    - ציין את הפלטפורמות והסינופסיס של המודול.
    - השתמש בכותרות עבור מאפיינים ושיטות של המודול כשנדרש.

דוגמה לתיעוד מודול:
```
מודול לעבודה עם עוזר תוכנה
=========================================================================================

מודול זה מכיל את המחלקה :class:`CodeAssistant`, המשמשת לעבודה עם דגמי AI שונים, 
כגון Google Gemini ו-OpenAI, לביצוע משימות עיבוד קוד.

שימוש לדוגמה
--------------------

שימוש במחלקה `CodeAssistant`:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
```

2. **מחלקות**:
    - כל מחלקה צריכה להיות מתועדת בהתאם למטרתה. כלל תיאור למחלקה, מאפיינים ושיטות שלה.
    - בחלק המחלקות, ציין את כל השיטות, מטרתן ודוגמאות לשימוש.
    - לכל שיטה, כלל תיאור של פרמטרים וערכים מוחזרים, ודוגמאות לשימוש.

דוגמה לתיעוד מחלקה:
```
מחלקה לעבודה עם עוזר תוכנה
=========================================================================================

המחלקה :class:`CodeAssistant` משמשת לעבודה עם דגמי AI שונים כמו Google Gemini, 
ומספקת שיטות לניתוח ויצירת תיעוד עבור קוד.

מאפיינים:
----------
- `role`: תפקיד העוזר (למשל, 'code_checker').
- `lang`: השפה בה העוזר יעבוד (למשל, 'ru').
- `model`: רשימה של דגמי AI בשימוש (למשל, ['gemini']).

שיטות:
--------
- `process_files`: שיטה לעיבוד קבצי קוד.

שימוש לדוגמה:
---------------------

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
```

3. **פונקציות ושיטות**:
    - תעד כל פונקציה או שיטה, תוך ציון פרמטרים וערכים מוחזרים.
    - עבור כל פונקציה, ספק תיאור של מטרתה ודוגמאות לשימוש בפורמט `.. code-block:: python`.

דוגמה לתיעוד שיטה:
```
שיטה לעיבוד קבצים
=========================================================================================

שיטה זו משמשת לניתוח ועיבוד קבצי קוד.

פרמטרים:
-----------
- `files`: רשימה של קבצים לעיבוד.
- `options`: פרמטרים נוספים לשימוש בקביעת עיבוד הקבצים.

ערך מוחזר:
----------------------
- מחזיר את תוצאת העיבוד כרשימה של נתונים מעובדים.

שימוש לדוגמה:
---------------------

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
```

4. **הערות בקוד**:
    - כל ההערות בקוד צריכות להיות כתובות בפורמט RST ולציין מה עושה חלק ספציפי בקוד.
    - השאר הערות בבלוקים, ולא בשורות בודדות. השתמש בהערות כדי להסביר את הלוגיקה ולהסביר החלטות או פתרונות זמניים בקוד.
    - דוגמה:
    ```
    # כאן מתבצע טיפול בשגיאות כדי להמשיך בביצוע אם הקובץ לא נמצא
    try:
        process_file(file)
    except FileNotFoundError as ex:
        handle_exception(ex)
    ```

5. **שגיאות (Exceptions)**:
    - תעד את השגיאות במחלקות, שיטות ופונקציות.
    - ציין אילו שגיאות עשויות להתעורר ובאילו נסיבות.

דוגמה לתיעוד שגיאה:
```
שגיאת קובץ לא נמצא
=========================================================================================

שגיאה זו מתעוררת כאשר קובץ לא נמצא במהלך העיבוד.

פרמטרים:
-----------
- `file`: נתיב הקובץ שלא נמצא.

שימוש לדוגמה:
---------------------

.. code-block:: python

    try:
        open(file)
    except FileNotFoundError as ex:
        raise FileNotFoundError("הקובץ לא נמצא") from ex
```

עקוב אחרי ההוראות האלה לתיעוד הקוד שלך. כל ההערות צריכות להיות ברורות, אינפורמטיביות ולעמוד בסטנדרט RST."