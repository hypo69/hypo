"""
BIORHYTHM:
=================
קושי: 7
-----------------
המשחק "ביוריתמוס" הוא משחק שמחשב את הביוריתמוס שלך על סמך תאריך הלידה שלך ויום המבוקש. ביוריתמוס מבוסס על שלושה מחזורים: פיזי, רגשי ואינטלקטואלי, שלכל אחד מהם יש מחזוריות משלו. המשחק מחשב את הערכים של מחזורים אלה עבור יום מסוים.

חוקי המשחק:
1. השחקן מזין את תאריך הלידה שלו.
2. השחקן מזין את התאריך שאותו הוא רוצה לבדוק.
3. המשחק מחשב את הביוריתמוסים הפיזי, הרגשי והאינטלקטואלי עבור התאריך המבוקש.
4. הביוריתמוסים מחושבים באמצעות נוסחה המבוססת על מספר הימים בין תאריך הלידה לבין התאריך המבוקש.
5. התוצאה מודפסת בטבלה.
-----------------
אלגוריתם:
1. קבל תאריך לידה מהמשתמש.
2. קבל תאריך בדיקה מהמשתמש.
3. חשב את מספר הימים שעברו בין תאריך הלידה לתאריך הבדיקה.
4. חשב את הביוריתמוס הפיזי באמצעות הנוסחה: SIN(2*PI*ימים/23).
5. חשב את הביוריתמוס הרגשי באמצעות הנוסחה: SIN(2*PI*ימים/28).
6. חשב את הביוריתמוס האינטלקטואלי באמצעות הנוסחה: SIN(2*PI*ימים/33).
7. הצג טבלה המציגה את תאריך הלידה, תאריך הבדיקה ואת ערכי הביוריתמוסים הפיזי, הרגשי והאינטלקטואלי.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputBirthDate["קלט תאריך לידה"]
    InputBirthDate --> InputCheckDate["קלט תאריך בדיקה"]
    InputCheckDate --> CalculateDays["חישוב הפרש ימים בין התאריכים"]
    CalculateDays --> CalculatePhysical["חישוב ביוריתמוס פיזי"]
    CalculatePhysical --> CalculateEmotional["חישוב ביוריתמוס רגשי"]
    CalculateEmotional --> CalculateIntellectual["חישוב ביוריתמוס אינטלקטואלי"]
    CalculateIntellectual --> OutputTable["הצגת טבלה עם התוצאות"]
    OutputTable --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InputBirthDate - קבלת תאריך הלידה מהמשתמש.
    InputCheckDate - קבלת התאריך לבדיקה מהמשתמש.
    CalculateDays - חישוב ההפרש במספר הימים בין תאריך הלידה לתאריך הבדיקה.
    CalculatePhysical - חישוב הביוריתמוס הפיזי על ידי שימוש בנוסחה.
    CalculateEmotional - חישוב הביוריתמוס הרגשי על ידי שימוש בנוסחה.
    CalculateIntellectual - חישוב הביוריתמוס האינטלקטואלי על ידי שימוש בנוסחה.
    OutputTable - הצגת טבלה עם תאריכי הלידה והבדיקה וערכי הביוריתמוסים.
    End - סוף התוכנית.
"""
import math
from datetime import date

__author__ = 'hypo69 (hypo69@davidka.net)'
"""
הסברים:
הקוד הבא מחשב את הביוריתמוסים של משתמש על פי תאריך הלידה שלו ויום מסוים.
הביוריתמוס מורכב משלושה מחזורים: פיזי (23 ימים), רגשי (28 ימים), ואינטלקטואלי (33 ימים).
כל מחזור מחושב על פי פונקציית הסינוס של מספר הימים שעברו מתאריך הלידה.
"""


def calculate_biorhythm(birth_date, check_date):
    """
    מחשב את הביוריתמוסים עבור תאריך לידה ותאריך בדיקה.

    :param birth_date: תאריך הלידה של המשתמש.
    :param check_date: התאריך לבדיקה.
    :return: טבלה עם תוצאות הביוריתמוס.
    """
    # חישוב מספר הימים בין תאריכי הלידה והבדיקה
    delta = check_date - birth_date
    days = delta.days

    # חישוב הביוריתמוסים
    physical = math.sin(2 * math.pi * days / 23)
    emotional = math.sin(2 * math.pi * days / 28)
    intellectual = math.sin(2 * math.pi * days / 33)

    # יצירת טבלה של התוצאות
    print("---------------------------------------------------")
    print("|        תאריך לידה      |      תאריך בדיקה    |      ביוריתמוס       |")
    print("---------------------------------------------------")
    print(f"| {birth_date.strftime('%d/%m/%Y')}    | {check_date.strftime('%d/%m/%Y')}  | פיזי: {physical:.2f}   |")
    print(f"|                        |                     | רגשי: {emotional:.2f}   |")
    print(f"|                        |                     | אינטלקטואלי: {intellectual:.2f} |")
    print("---------------------------------------------------")


# קבלת תאריך הלידה מהמשתמש
try:
    birth_date_str = input("הכנס תאריך לידה בפורמט DD/MM/YYYY: ")
    birth_date = date.fromisoformat(birth_date_str.replace('/', '-'))
except ValueError:
    print("פורמט תאריך לא תקין. אנא הזן בפורמט DD/MM/YYYY.")
    exit()

# קבלת התאריך לבדיקה מהמשתמש
try:
    check_date_str = input("הכנס תאריך לבדיקה בפורמט DD/MM/YYYY: ")
    check_date = date.fromisoformat(check_date_str.replace('/', '-'))
except ValueError:
    print("פורמט תאריך לא תקין. אנא הזן בפורמט DD/MM/YYYY.")
    exit()

# הפעלת פונקציית חישוב הביוריתמוסים
calculate_biorhythm(birth_date, check_date)

"""
הסבר מפורט על הקוד:

1. **ייבוא מודולים:**
   - `import math`: ייבוא מודול `math` לצורך שימוש בפונקציה `sin` וקבוע `pi`.
   - `from datetime import date`: ייבוא המודול `date` לטיפול בתאריכים.

2. **פונקציה `calculate_biorhythm(birth_date, check_date)`:**
   - מקבלת שני פרמטרים: `birth_date` (תאריך לידה) ו- `check_date` (תאריך בדיקה).
   - `delta = check_date - birth_date`: חישוב ההפרש בין שני התאריכים.
   - `days = delta.days`: מספר הימים בין התאריכים.
   - `physical = math.sin(2 * math.pi * days / 23)`: חישוב הביוריתמוס הפיזי.
   - `emotional = math.sin(2 * math.pi * days / 28)`: חישוב הביוריתמוס הרגשי.
   - `intellectual = math.sin(2 * math.pi * days / 33)`: חישוב הביוריתמוס האינטלקטואלי.
   - הדפסת טבלה עם תאריכי הלידה, הבדיקה והתוצאות.

3. **קבלת קלט מהמשתמש:**
   - `birth_date_str = input("הכנס תאריך לידה בפורמט DD/MM/YYYY: ")`: קבלת תאריך הלידה מהמשתמש.
   - `birth_date = date.fromisoformat(birth_date_str.replace('/', '-'))`: המרת מחרוזת התאריך לאובייקט `date` לאחר החלפת התו `/` ב-`-`.
   - טיפול בשגיאות אפשריות באמצעות בלוק `try-except` לשגיאת `ValueError`.
   - `check_date_str = input("הכנס תאריך לבדיקה בפורמט DD/MM/YYYY: ")`: קבלת תאריך הבדיקה מהמשתמש.
   - `check_date = date.fromisoformat(check_date_str.replace('/', '-'))`: המרת מחרוזת התאריך לאובייקט `date` לאחר החלפת התו `/` ב-`-`.
   - טיפול בשגיאות אפשריות באמצעות בלוק `try-except` לשגיאת `ValueError`.

4. **הפעלת הפונקציה:**
   - `calculate_biorhythm(birth_date, check_date)`: הפעלת פונקציית חישוב הביוריתמוס עם התאריכים שהתקבלו.
"""
