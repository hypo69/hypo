# מבני נתונים בסיסיים בפייתון

## סקירה כללית

קובץ זה מספק סקירה כללית של מבני הנתונים הבסיסיים בפייתון: רשימות, מילונים, טאפלים ומרחבי שמות פשוטים (`SimpleNamespace`). כל מבנה נתונים מוסבר עם דוגמאות לשימוש.

## תוכן עניינים

1. [רשימות (Lists)](#lists)
2. [מילונים (Dictionaries)](#dictionaries)
3. [טאפלים (Tuples)](#tuples)
4. [מרחב שמות פשוט (SimpleNamespace)](#simplenamespace)

## רשימות (Lists)

**הגדרה:** רשימות בפייתון הן אוספים מסודרים וניתנים לשינוי של אלמנטים. ניתן להוסיף, להסיר ולשנות אלמנטים ברשימה, ולסדר האלמנטים יש משמעות.

**ייצוג:** רשימות נוצרות באמצעות סוגריים מרובעים `[]`, והאלמנטים מופרדים בפסיקים.

**דוגמאות:**
```python
# יצירת רשימה
boris_list = ["בוריס", "מוסקבה", 30, "מהנדס"]
print(f"יצירת רשימה: {boris_list}")

# גישה לפי אינדקס
print(f"אלמנט באינדקס 0: {boris_list[0]}")

# שינוי אלמנט
boris_list[2] = 31
print(f"שינוי אלמנט: {boris_list}")

# הוספת אלמנט לסוף הרשימה
boris_list.append("נשוי")
print(f"הוספה לסוף: {boris_list}")

# הוספת אלמנט לפי אינדקס
boris_list.insert(1, "רוסיה")
print(f"הוספת אלמנט: {boris_list}")

# הסרת אלמנט לפי ערך
boris_list.remove("מהנדס")
print(f"הסרת אלמנט לפי ערך: {boris_list}")

# הסרת אלמנט לפי אינדקס
del boris_list[2]
print(f"הסרת אלמנט לפי אינדקס: {boris_list}")

# הרחבת רשימה עם רשימה אחרת
boris_list.extend(["תחביב", "דיג"])
print(f"הרחבת רשימה: {boris_list}")

# הסרת אלמנט מהסוף
boris_list.pop()
print(f"הסרת אלמנט מהסוף: {boris_list}")
```

## מילונים (Dictionaries)

**הגדרה:** מילונים בפייתון הם אוספים לא מסודרים של אלמנטים, כאשר כל אלמנט מורכב מזוג של "מפתח-ערך".

**ייצוג:** מילונים נוצרים באמצעות סוגריים מסולסלים `{}`, וזוגות "מפתח-ערך" מופרדים בנקודותיים `:`.

**דוגמאות:**
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

# הסרת זוג באמצעות pop (עם החזרת ערך)
hobby = alice_dict.pop("hobby")
print(f"הסרה עם החזרת ערך: {alice_dict}, ערך: {hobby}")

# בדיקת קיום מפתח
print(f"קיום מפתח \'name\': {'name' in alice_dict}")
```

## טאפלים (Tuples)

**הגדרה:** טאפלים בפייתון הם אוספים מסודרים ו**בלתי ניתנים לשינוי** של אלמנטים.

**ייצוג:** טאפלים נוצרים באמצעות סוגריים עגולים `()`, והאלמנטים מופרדים בפסיקים.

**דוגמאות:**
```python
# יצירת טאפל
boris_tuple = ("בוריס", "מוסקבה", 30, "מהנדס")
print(f"יצירת טאפל: {boris_tuple}")

# גישה לפי אינדקס
print(f"אלמנט באינדקס 2: {boris_tuple[2]}")

# לא ניתן לשנות אלמנט
# boris_tuple[0] = "בוריס" # יגרום לשגיאה: TypeError: 'tuple' object does not support item assignment

# לא ניתן להוסיף אלמנט
# boris_tuple.append(4) # יגרום לשגיאה: AttributeError: 'tuple' object has no attribute 'append'

# לא ניתן למחוק אלמנט
# del boris_tuple[0]  # יגרום לשגיאה: TypeError: 'tuple' object doesn't support item deletion
```

## מרחב שמות פשוט (SimpleNamespace)

**הגדרה:** `SimpleNamespace` מהמודול `types` הוא מחלקה פשוטה המאפשרת ליצור אובייקטים עם תכונות שניתנות להגדרה הן בעת היצירה והן לאחר מכן.

**ייצוג:** כדי ליצור אובייקט `SimpleNamespace`, יש לייבא אותו מתוך `types` ולהעביר אליו ארגומנטים בעלי שם (או לא להעביר כלל):
```python
from types import SimpleNamespace

alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
```

**מאפיינים:**

*   מאפשר ליצור אובייקטים עם תכונות דינמיות (דומה למילון).
*   נוח ליצירת אובייקטים פשוטים לאחסון נתונים.
*   ניתן לגשת לתכונות באמצעות נקודה, כמו באובייקטים רגילים: `alice_namespace.name`.
*   בניגוד למילונים, סדר התכונות נשמר.
*   ניתן לשנות שדות, אך לא ניתן להוסיף שדות חדשים.

**דוגמאות:**
```python
from types import SimpleNamespace

# יצירת SimpleNamespace
alice_namespace = SimpleNamespace(name="אליס", age=25, city="לונדון")
print(f"יצירת SimpleNamespace: {alice_namespace}")

# גישה לתכונה
print(f"תכונה \'name\': {alice_namespace.name}")

# שינוי תכונה
alice_namespace.age = 26
print(f"שינוי תכונה: {alice_namespace}")

# לא ניתן להוסיף תכונה חדשה
# alice_namespace.occupation = "אמנית" # יגרום לשגיאה: AttributeError: 'SimpleNamespace' object has no attribute 'occupation'

# הוספה באמצעות setattr
setattr(alice_namespace, "occupation", "אמנית")
print(f"הוספת תכונה: {alice_namespace}")

# הסרה באמצעות delattr
delattr(alice_namespace, "city")
print(f"הסרת תכונה: {alice_namespace}")