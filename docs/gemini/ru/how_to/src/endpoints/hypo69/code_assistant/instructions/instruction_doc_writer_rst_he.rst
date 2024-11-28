איך להשתמש בבלוק קוד זה
========================================================================================

תיאור
-------------------------
[הוסף כאן תיאור של מה עושה הבלוק של הקוד.]

שלבים לביצוע
-------------------------
1. [הוסף כאן תיאור של שלב 1.  לדוגמא: "קרא את הקלט מהקובץ"].
2. [הוסף כאן תיאור של שלב 2. לדוגמא: "עבד על הקלט"].
3. [הוסף כאן תיאור של שלב 3. לדוגמא: "הדפס את התוצאה"].

דוגמה לשימוש
-------------------------
.. code-block:: python

    # דוגמה לקוד.  חשוב להחליף את הדוגמא עם הקוד הספציפי שצריך לתעד.
    #  השתמשו בתיעוד תוך שימוש בפרטים שבתחילת הקוד
    #  (לדוגמה, פונקציות ותיאורים שלהם)
    import os

    def read_file(file_path: str) -> str:
        """
        ארגומנטים:
            file_path (str):  נתיב לקובץ.

        ערך מוחזר:
            str: תוכן הקובץ.

        יוצאים:
            FileNotFoundError: אם הקובץ לא נמצא.
            PermissionError: אם אין גישה לקובץ.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"הקובץ {file_path} לא נמצא")
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except PermissionError as e:
            raise PermissionError(f"אין גישה לקובץ {file_path}") from e


    file_path = "my_file.txt"
    try:
        content = read_file(file_path)
        print(content)
    except FileNotFoundError as e:
        print(f"שגיאה: {e}")
    except PermissionError as e:
        print(f"שגיאה: {e}")