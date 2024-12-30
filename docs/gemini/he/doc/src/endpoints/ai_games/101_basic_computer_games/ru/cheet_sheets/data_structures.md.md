# מבני נתונים

## סקירה כללית

מסמך זה מספק סקירה מקיפה של מבני נתונים בסיסיים ב-Python, כולל רשימות, מילונים, טאפלים ומרחבי שמות פשוטים. הוא מסביר את ההגדרה, הייצוג והדוגמאות של כל מבנה נתונים.

## תוכן עניינים

- [רשימות (Lists)](#רשימות-lists)
- [מילונים (Dictionaries)](#מילונים-dictionaries)
- [טאפלים (Tuples)](#טאפלים-tuples)
- [SimpleNamespace](#simplenamespace)

## רשימות (Lists)

**הגדרה:** רשימות ב-Python הן אוספים מסודרים וניתנים לשינוי של פריטים. המשמעות היא שאתה יכול להוסיף, להסיר ולשנות פריטים ברשימה, ולסדר הפריטים יש משמעות.

**ייצוג:** רשימות נוצרות באמצעות סוגריים מרובעים `[]`, והפריטים מופרדים באמצעות פסיקים.

*   **דוגמאות:**
    ```python
    # יצירת רשימה
    boris_list = ["בוריס", "מוסקבה", 30, "מהנדס"]
    print(f"יצירת רשימה: {boris_list}")

    # גישה לפי אינדקס
    print(f"פריט באינדקס 0: {boris_list[0]}")

    # שינוי פריט
    boris_list[2] = 31
    print(f"שינוי פריט: {boris_list}")

    # הוספת פריט לסוף
    boris_list.append("נשוי")
    print(f"הוספה לסוף: {boris_list}")

    # הוספת פריט באינדקס
    boris_list.insert(1, "רוסיה")
    print(f"הוספת פריט: {boris_list}")

    # הסרת פריט לפי ערך
    boris_list.remove("מהנדס")
    print(f"הסרת פריט לפי ערך: {boris_list}")

    # הסרת פריט לפי אינדקס
    del boris_list[2]
    print(f"הסרת פריט לפי אינדקס: {boris_list}")

    # הרחבת רשימה עם רשימה אחרת
    boris_list.extend(["תחביב", "דיג"])
    print(f"הרחבת רשימה: {boris_list}")

    # הסרת פריט מהסוף
    boris_list.pop()
    print(f"הסרת פריט מהסוף: {boris_list}")
    ```

## מילונים (Dictionaries)

**הגדרה:** מילונים ב-Python הם אוספים לא מסודרים של פריטים, כאשר כל פריט מורכב מזוג "מפתח-ערך".

**ייצוג:** מילונים נוצרים באמצעות סוגריים מסולסלים `{}`, וזוגות "מפתח-ערך" מופרדים באמצעות נקודתיים `:`.

*   **דוגמאות:**
    ```python
    # יצירת מילון
    alice_dict = {"name": "אליס", "age": 25, "city": "לונדון", "occupation": "אמנית"}
    print(f"יצירת מילון: {alice_dict}")

    # גישה לפי מפתח
    print(f"ערך לפי מפתח \'name\': {alice_dict['name']}")

    # שינוי ערך
    alice_dict["age"] = 26
    print(f"שינוי ערך: {alice_dict}")

    # הוספת זוג מפתח-ערך
    alice_dict["hobby"] = "ציור"
    print(f"הוספת זוג: {alice_dict}")

    # הסרת זוג לפי מפתח
    del alice_dict["city"]
    print(f"הסרת זוג: {alice_dict}")

    # הסרת זוג באמצעות מתודת pop (עם החזרת ערך)
    hobby = alice_dict.pop("hobby")
    print(f"הסרה עם החזרת ערך: {alice_dict}, ערך: {hobby}")

    # בדיקת קיום מפתח
    print(f"קיום מפתח \'name\': {'name' in alice_dict}")
    ```

## טאפלים (Tuples)

**הגדרה:** טאפלים ב-Python הם אוספים מסודרים **בלתי ניתנים לשינוי** של פריטים.

**ייצוג:** טאפלים נוצרים באמצעות סוגריים עגולים `()`, והפריטים מופרדים באמצעות פסיקים.

*   **דוגמאות:**
    ```python
    # יצירת טאפל
    boris_tuple = ("בוריס", "מוסקבה", 30, "מהנדס")
    print(f"יצירת טאפל: {boris_tuple}")

    # גישה לפי אינדקס
    print(f"פריט באינדקס 2: {boris_tuple[2]}")

    # אי אפשר לשנות פריט
    # boris_tuple[0] = "בוריס" # זה יגרום לשגיאה: TypeError: 'tuple' object does not support item assignment

    # אי אפשר להוסיף פריט
    # boris_tuple.append(4) # זה יגרום לשגיאה: AttributeError: 'tuple' object has no attribute 'append'

    # אי אפשר להסיר פריט
    # del boris_tuple[0]  # זה יגרום לשגיאה: TypeError: 'tuple' object doesn't support item deletion
    ```

## SimpleNamespace

**הגדרה:** `SimpleNamespace` מהמודול `types` הוא מחלקה פשוטה המאפשרת ליצור אובייקטים שניתן להגדיר את המאפיינים שלהם בעת היצירה או מאוחר יותר.

**ייצוג:** כדי ליצור אובייקט `SimpleNamespace`, עליך לייבא אותו מ-`types` ולהעביר לו ארגומנטים בעלי שם (או לא להעביר אותם):

    ```python
    from types import SimpleNamespace

    alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
    ```

* **מאפיינים:**
    *   מאפשר ליצור אובייקטים עם מאפיינים דינמיים (דומה למילון).
    *   נוח ליצירת אובייקטים פשוטים לאחסון נתונים.
    *   ניתן לגשת למאפיינים באמצעות נקודה, כמו באובייקטים רגילים: `alice_namespace.name`
    *   בניגוד למילונים, סדר המאפיינים נשמר.
    *   ניתן לשנות שדות, אך לא ניתן להוסיף שדות חדשים

*   **דוגמאות:**
    ```python
    from types import SimpleNamespace

    # יצירת SimpleNamespace
    alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
    print(f"יצירת SimpleNamespace: {alice_namespace}")

    # גישה למאפיין
    print(f"מאפיין \'name\': {alice_namespace.name}")

    # שינוי מאפיין
    alice_namespace.age = 26
    print(f"שינוי מאפיין: {alice_namespace}")

    # אי אפשר להוסיף מאפיין חדש
    # alice_namespace.occupation = "אמנית" # זה יגרום לשגיאה: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

    # הוספה באמצעות setattr
    setattr(alice_namespace, "occupation", "אמנית")
    print(f"הוספת מאפיין: {alice_namespace}")

    # הסרה באמצעות delattr
    delattr(alice_namespace, "city")
    print(f"הסרת מאפיין: {alice_namespace}")
    ```