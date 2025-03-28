
WEKDAY:
=================
קושי: 2
-----------------
המשחק WEKDAY נועד לקבוע את היום בשבוע (ראשון עד שבת) בהינתן תאריך מסוים. השחקן מזין חודש ומספר יום בחודש, והתוכנית מחשבת ומדפיסה את היום בשבוע המתאים.

חוקי המשחק:
1. המשתמש מזין חודש (1-12) ומספר יום בחודש.
2. התוכנית מחשבת את היום בשבוע של התאריך שהוזן ומדפיסה אותו.
3. החישוב מתבצע על בסיס נוסחה לחישוב היום בשבוע, כאשר התאריך הראשון (1/1/1900) הוא יום שני.
-----------------
אלגוריתם:
1. קבע את היום בשבוע של 1/1/1900 כיום שני (DAY = 2).
2. קלוט חודש (MONTH) ומספר יום בחודש (DAYNUMBER) מהמשתמש.
3. אם החודש קטן מ-1 או גדול מ-12, קפוץ לשלב 2.
4. אם מספר הימים בחודש קטן מ-1, קפוץ לשלב 2.
5. קבע מערך DAYS_IN_MONTH שמייצג את מספר הימים בכל חודש (בהתאמה).
6. אם החודש הוא פברואר (חודש 2) ומספר היום גדול מ-28, או אם החודש אינו פברואר ומספר היום גדול ממספר הימים בחודש הרלוונטי, קפוץ לשלב 2.
7. חשב את מספר הימים הכולל מתחילת השנה (TOTALDAYS) על ידי סיכום הימים בכל החודשים שקדמו לחודש שהוזן, וסיכום מספר היום בחודש שהוזן.
8. חשב את היום בשבוע (DAY) על ידי מציאת השארית של חלוקת TOTALDAYS ב-7 והוספת 1 לתוצאה.
9. קבע מערך DAYS_NAME שמייצג את שמות הימים בשבוע (ראשון עד שבת).
10. הדפס את שם היום בשבוע המתאים.
11. חזור לשלב 2 עד שהמשתמש יחליט לסיים.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDay["אתחול: <code><b>day = 2</b></code> (יום שני)"]
    InitializeDay --> LoopStart{"תחילת לולאה"}
    LoopStart --> InputMonthDay["קלט מהמשתמש: <code><b>month, dayNumber</b></code>"]
    InputMonthDay --> ValidateMonth{"בדיקה: <code><b>month < 1 or month > 12</b></code>"}
    ValidateMonth -- כן --> LoopStart
    ValidateMonth -- לא --> ValidateDayNumber{"בדיקה: <code><b>dayNumber < 1</b></code>"}
    ValidateDayNumber -- כן --> LoopStart
    ValidateDayNumber -- לא --> InitializeDaysInMonth["אתחול: <code><b>daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]</b></code>"]
    InitializeDaysInMonth --> CheckDayLimit{"בדיקה: <code><b>month == 2 and dayNumber > 28 or month != 2 and dayNumber > daysInMonth[month - 1]</b></code>"}
    CheckDayLimit -- כן --> LoopStart
    CheckDayLimit -- לא --> CalculateTotalDays["חישוב: <code><b>totalDays = sum(daysInMonth[0:month-1]) + dayNumber</b></code>"]
    CalculateTotalDays --> CalculateDayOfWeek["חישוב: <code><b>day = (totalDays % 7) + 1</b></code>"]
    CalculateDayOfWeek --> InitializeDayNames["אתחול: <code><b>dayNames = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']</b></code>"]
    InitializeDayNames --> OutputDay["הדפסה: <code><b>dayNames[day - 1]</b></code>"]
    OutputDay --> LoopStart
    LoopStart -- סיום --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InitializeDay - אתחול היום בשבוע (יום שני).
    LoopStart - תחילת הלולאה הראשית.
    InputMonthDay - קלט חודש ומספר יום מהמשתמש.
    ValidateMonth - בדיקה אם החודש תקין (1 עד 12).
    ValidateDayNumber - בדיקה אם מספר היום תקין (גדול מ-0).
    InitializeDaysInMonth - אתחול מערך הימים בכל חודש.
    CheckDayLimit - בדיקה אם מספר הימים תואם את החודש (עד 28 בפברואר).
    CalculateTotalDays - חישוב סך הימים מתחילת השנה.
    CalculateDayOfWeek - חישוב היום בשבוע.
    InitializeDayNames - אתחול מערך שמות הימים.
    OutputDay - הדפסת היום בשבוע.
    End - סיום התוכנית.
```



"""
הסברים:
הקוד מדמה את המשחק WEKDAY משפת BASIC לפייתון. המשחק נועד לקבוע את היום בשבוע על פי תאריך שהמשתמש מזין.
הקוד מקבל קלט של חודש ומספר יום בחודש מהמשתמש, מחשב את היום בשבוע של אותו תאריך, ומדפיס את התוצאה.
האלגוריתם עוקב אחרי הלוגיקה המקורית מהספר.
"""
licence:MIT(../licence)
"""
import sys

# יום בשבוע של 1/1/1900 (יום שני)
day = 2

# לולאה ראשית של המשחק
while True:
    # קבלת קלט מהמשתמש: חודש ומספר יום
    try:
        month = int(input("הכנס חודש (1-12): "))
        dayNumber = int(input("הכנס יום בחודש: "))
    except ValueError:
        print("קלט לא תקין, אנא הכנס מספרים שלמים.")
        continue

    # בדיקת תקינות החודש
    if month < 1 or month > 12:
        print("חודש לא תקין, אנא הכנס חודש בין 1 ל-12.")
        continue

    # בדיקת תקינות מספר היום
    if dayNumber < 1:
        print("מספר יום לא תקין, אנא הכנס מספר יום חיובי.")
        continue

    # מערך המכיל את מספר הימים בכל חודש
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # בדיקה האם מספר היום גדול ממספר הימים בחודש
    if (month == 2 and dayNumber > 28) or (month != 2 and dayNumber > daysInMonth[month - 1]):
         print("מספר יום לא תקין עבור החודש הזה.")
         continue

    # חישוב מספר הימים הכולל מתחילת השנה
    totalDays = sum(daysInMonth[0:month - 1]) + dayNumber

    # חישוב היום בשבוע
    day = (totalDays % 7) + 1

    # מערך שמות הימים
    dayNames = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']

    # הדפסת היום בשבוע המתאים
    print(f"היום בשבוע הוא: {dayNames[day - 1]}")

    # אפשרות לסיים את המשחק
    again = input("האם תרצה לחשב תאריך נוסף? (כן/לא): ")
    if again.lower() != 'כן':
      print("תודה ושלום!")
      break

"""
הסבר הקוד:
1. **ייבוא המודול `sys`**:
   - `import sys`: ייבוא המודול `sys`, שלא נעשה בו שימוש ישירות בקוד זה, אך לעתים קרובות משמש למערכת פקודות, כגון יציאה מהתוכנית.

2. **אתחול משתנים**:
   - `day = 2`: אתחול המשתנה `day` לערך 2, המייצג את היום בשבוע (יום שני) של התאריך 1/1/1900.

3. **לולאה ראשית `while True:`**:
   - לולאה אינסופית המאפשרת למשתמש להזין מספר תאריכים.

4. **קלט נתונים**:
   - `try...except ValueError`: בלוק try-except מטפל בשגיאות קלט. אם המשתמש יזין משהו שאינו מספר שלם, תוצג הודעת שגיאה והתוכנית תמשיך לסיבוב הבא של הלולאה.
   - `month = int(input("הכנס חודש (1-12): "))`: בקשה מהמשתמש להזין מספר חודש (1 עד 12).
   - `dayNumber = int(input("הכנס יום בחודש: "))`: בקשה מהמשתמש להזין מספר יום בחודש.

5. **בדיקת תקינות החודש**:
   - `if month < 1 or month > 12`: בדיקה האם החודש שהוזן חוקי (בין 1 ל-12). אם לא, מוצגת הודעת שגיאה.

6. **בדיקת תקינות מספר היום**:
   - `if dayNumber < 1`: בדיקה האם מספר היום חיובי. אם לא, מוצגת הודעת שגיאה.

7. **מערך מספר ימים בכל חודש**:
   - `daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`: הגדרת רשימה המכילה את מספר הימים בכל חודש (ללא התחשבות בשנה מעוברת).

8. **בדיקת תקינות יום בחודש**:
   - `if (month == 2 and dayNumber > 28) or (month != 2 and dayNumber > daysInMonth[month - 1])`: בדיקה האם מספר היום בחודש שהוזן תואם למספר הימים המקסימלי בחודש זה.

9. **חישוב סך הימים**:
   - `totalDays = sum(daysInMonth[0:month - 1]) + dayNumber`: חישוב מספר הימים הכולל מתחילת השנה עד התאריך שהוזן.

10. **חישוב יום בשבוע**:
    - `day = (totalDays % 7) + 1`: חישוב היום בשבוע על ידי מודולו 7 של סך הימים, והוספת 1 כדי שהימים יהיו מ-1 עד 7 במקום מ-0 עד 6.

11. **מערך שמות הימים**:
    - `dayNames = ['ראשון', 'שני', 'שלישי', 'רביעי', 'חמישי', 'שישי', 'שבת']`: הגדרת רשימה של שמות הימים בשבוע.

12. **הדפסת התוצאה**:
    - `print(f"היום בשבוע הוא: {dayNames[day - 1]}")`: הדפסת שם היום בשבוע המתאים לפי האינדקס.

13. **אפשרות להמשך או סיום המשחק**:
    - `again = input("האם תרצה לחשב תאריך נוסף? (כן/לא): ")`: בקשה מהמשתמש להחליט האם להמשיך או לסיים.
    - `if again.lower() != 'כן'`: בדיקה האם המשתמש בחר לסיים את המשחק.
        - `print("תודה ושלום!")`: הודעת סיום.
        - `break`: יציאה מהלולאה.
"""
```