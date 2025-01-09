## <algorithm>
1. **התחלה**:
   - אתחל את גודל צבא האיחוד (unionForce) ל-1000.
   - אתחל את גודל צבא הקונפדרציה (confederateForce) ל-800.
   
   דוגמה:
   ```
   unionForce = 1000
   confederateForce = 800
   ```
2. **לולאת משחק ראשית**: כל עוד לשני הצבאות יש חיילים (unionForce > 0 וגם confederateForce > 0), המשחק ממשיך.
    
   דוגמה:
   ```
   while unionForce > 0 and confederateForce > 0:
       #המשך המשחק
   ```
3.  **קבלת קלט שחקן - כוח תקיפה**:
    - בקש מהשחקן להזין את מספר החיילים מהקונפדרציה שישלחו להתקפה (attackForce).
    - בדוק שהערך שהוזן הוא מספר שלם.
    - אם attackForce גדול מ- confederateForce, הדפס "לא מספיק חיילים" וחזור על השלב הנוכחי.
    
    דוגמה:
    ```
    while True:
       try:
           attackForce = int(input("כמה חיילים תשלח להתקפה?"))
           if attackForce > confederateForce:
               print("לא מספיק חיילים")
           else:
               break
       except ValueError:
           print("הזן מספר שלם")
    ```
4.  **קבלת קלט שחקן - סוג התקפה**:
    - בקש מהשחקן להזין סוג התקפה: 1 - ישיר או 2 - עוקף.
    - בדוק שהערך שהוזן הוא מספר שלם 1 או 2.
    - אם סוג ההתקפה אינו 1 או 2, הדפס "סוג התקפה לא תקין" וחזור על השלב הנוכחי.

    דוגמה:
    ```
    while True:
       try:
          attackType = int(input("בחר סוג התקפה (1- ישיר, 2- עוקף): "))
          if attackType in [1, 2]:
             break
          else:
            print("סוג התקפה לא תקין")
       except ValueError:
          print("הזן מספר שלם 1 או 2")
    ```
5. **חישוב אבדות של הקונפדרציה**:
   - אם סוג ההתקפה הוא ישיר (attackType == 1), חשב את האבדות של הקונפדרציה על ידי הכפלת attackForce במספר אקראי בין 0 ל-0.4.
   - אם סוג ההתקפה הוא עוקף (attackType == 2), חשב את האבדות של הקונפדרציה על ידי הכפלת attackForce במספר אקראי בין 0 ל-0.2.
   - אם האבדות גדולות מכוח התקיפה, הגדר את האבדות שוות לכוח התקיפה.
   
   דוגמה:
   ```
   if attackType == 1:
       confederateLosses = int(attackForce * random.random() * 0.4)
   else:
       confederateLosses = int(attackForce * random.random() * 0.2)
   if confederateLosses > attackForce:
       confederateLosses = attackForce
   ```
6. **חישוב אבדות של האיחוד**:
   - חשב את האבדות של האיחוד על ידי הכפלת attackForce במספר אקראי בין 0 ל-0.3.
   - אם סוג ההתקפה הוא עוקף (attackType == 2), הוסף לאבדות האיחוד מספר אקראי בין 0 ל-100.
   
   דוגמה:
   ```
   unionLosses = int(attackForce * random.random() * 0.3)
   if attackType == 2:
      unionLosses += random.randint(0, 100)
   ```
7. **עדכון גודל צבאות**:
   - הפחת את אבדות הקונפדרציה (confederateLosses) מגודל הצבא של הקונפדרציה (confederateForce).
   - הפחת את אבדות האיחוד (unionLosses) מגודל צבא האיחוד (unionForce).
   
   דוגמה:
   ```
   confederateForce -= confederateLosses
   unionForce -= unionLosses
   ```
8. **הדפס גודל צבאות נוכחי**:
    - הצג את מספר החיילים הנוכחי של כל צבא.
    
    דוגמה:
    ```
    print(f"קונפדרציה: {confederateForce} חיילים")
    print(f"איחוד: {unionForce} חיילים")
    ```
9. **בדיקת תנאי ניצחון**:
   - אם גודל צבא האיחוד (unionForce) קטן או שווה ל-0, הצג "הקונפדרציה ניצחה!" והמשחק נגמר.
   - אם גודל צבא הקונפדרציה (confederateForce) קטן או שווה ל-0, הצג "האיחוד ניצח!" והמשחק נגמר.
    
    דוגמה:
    ```
    if unionForce <= 0:
       print("הקונפדרציה ניצחה!")
    elif confederateForce <= 0:
        print("האיחוד ניצח!")
    ```
10. **סיום**: המשחק הסתיים.

## <mermaid>
```mermaid
flowchart TD
    Start(התחלה) --> InitializeForces[אתחול גודל צבאות: <br> unionForce = 1000, <br> confederateForce = 800];
    InitializeForces --> GameLoopStart{Game Loop: <br> (unionForce > 0 and confederateForce > 0)?};
    GameLoopStart -- Yes --> GetAttackForceInput[קבל קלט: כמות חיילים להתקפה <br> (attackForce)];
    GetAttackForceInput --> ValidateAttackForce{attackForce > confederateForce?};
     ValidateAttackForce -- Yes --> InsufficientForceMessage[הדפס: "לא מספיק חיילים"];
    InsufficientForceMessage --> GetAttackForceInput;
    ValidateAttackForce -- No --> GetAttackTypeInput[קבל קלט: סוג התקפה <br> (attackType: 1=ישיר, 2=עוקף)];
    GetAttackTypeInput --> ValidateAttackType{attackType in [1,2]?};
    ValidateAttackType -- No --> InvalidAttackTypeMessage[הדפס: "סוג התקפה לא תקין"];
     InvalidAttackTypeMessage --> GetAttackTypeInput;
     ValidateAttackType -- Yes --> CalculateConfederateLosses[חשב אבדות קונפדרציה (confederateLosses)];
    CalculateConfederateLosses --> CheckConfederateLosses{confederateLosses > attackForce?};
    CheckConfederateLosses -- Yes --> SetConfederateLosses[confederateLosses = attackForce];
     SetConfederateLosses --> CalculateUnionLosses[חשב אבדות איחוד <br> (unionLosses)];
      CheckConfederateLosses -- No --> CalculateUnionLosses
    CalculateUnionLosses --> UpdateForces[עדכן גודל צבאות: <br> confederateForce -= confederateLosses, <br> unionForce -= unionLosses];
    UpdateForces --> DisplayForces[הצג גודל צבאות נוכחי];
    DisplayForces --> CheckWinConditions[בדיקת תנאי ניצחון: <br> (unionForce <= 0) or <br> (confederateForce <= 0)?];
    CheckWinConditions -- Yes --> UnionWin{unionForce <= 0?};
     UnionWin -- Yes --> ConfederateWinMessage[הדפס: "הקונפדרציה ניצחה!"];
     UnionWin -- No -->  ConfederateWinMessage[הדפס: "האיחוד ניצח!"];
   ConfederateWinMessage --> End(סיום);
    CheckWinConditions -- No --> GameLoopStart;
     GameLoopStart -- No --> End

```
## <explanation>
**ייבואים (Imports):**
   - `import random`: מביא את מודול random שמאפשר לייצר מספרים אקראיים לחישוב אבדות במהלך הקרב. המודול הוא חלק מהספרייה הסטנדרטית של פייתון.

**משתנים (Variables):**
   - `unionForce`: משתנה המייצג את גודל צבא האיחוד. הוא מאותחל ל-1000 בתחילת המשחק.
   - `confederateForce`: משתנה המייצג את גודל צבא הקונפדרציה. הוא מאותחל ל-800 בתחילת המשחק.
   - `attackForce`: משתנה המייצג את מספר החיילים מהקונפדרציה שנשלחים להתקפה, הערך מתקבל כקלט מהמשתמש.
   - `attackType`: משתנה המייצג את סוג ההתקפה: 1 עבור התקפה ישירה, 2 עבור התקפה עוקפת, הערך מתקבל כקלט מהמשתמש.
   - `confederateLosses`: משתנה המייצג את האבדות של צבא הקונפדרציה במהלך קרב, מחושב בצורה אקראית בהתאם לסוג ההתקפה.
   - `unionLosses`: משתנה המייצג את האבדות של צבא האיחוד במהלך קרב, מחושב בצורה אקראית בהתאם לסוג ההתקפה.
   
**פונקציות (Functions):**
  - אין פונקציות המוגדרות בקוד הזה, כל הפעולות מתבצעות בתוך לולאת ה-`while` הראשית.

**הסברים מפורטים:**
   - הקוד מדמה משחק מלחמה בין שני צבאות: הקונפדרציה והאיחוד.
   - המשחק נמשך כל עוד לשני הצבאות יש חיילים.
   - בכל סיבוב, השחקן (ששולט על הקונפדרציה) צריך להזין:
        - מספר החיילים שיישלחו להתקפה.
        - סוג ההתקפה (ישירה או עוקפת).
   - בהתבסס על הקלט וערכים אקראיים, מחושבות האבדות של שני הצבאות.
   - גודל הצבאות מעודכן, ומוצג גודלם הנוכחי.
   - המשחק מסתיים כאשר אחד הצבאות מגיע ל-0 חיילים או פחות, והמנצח מוכרז.
   - **בעיות אפשריות:**
        - הקוד משתמש ב-`input()` לקבלת קלט מהמשתמש, מה שאומר שצריך להריץ אותו בטרמינל.
        - חסר טיפול שגיאות מעמיק יותר, כמו קלט שאינו מספר או קלט שלילי עבור כמות החיילים לתקיפה.
        - אפשר להוסיף יותר פיצ'רים ואיזונים כדי להפוך את המשחק ליותר מעניין.

**שרשרת קשרים עם חלקים אחרים בפרויקט:**
   - הקוד הזה עומד בפני עצמו ואין לו יחסי תלות ישירים עם חלקים אחרים בפרויקט. עם זאת, אם ירצו להרחיב את המשחק, אפשר לשלב אותו עם מודולים אחרים כמו מודול GUI ליצירת משק משתמש גרפי.