## <algorithm>

1. **התחלה:**
   - אתחול מונה הניסיונות (`numberOfGuesses`) ל-0.
   - יצירת מספר אקראי שלם בין 1 ל-100 (`targetNumber`).

   *דוגמה:* `numberOfGuesses = 0`, `targetNumber = 42`

2. **לולאת משחק:**
   -  הלולאה רצה עד שהמשתמש מנחש נכון.

3. **עדכון מונה ניסיונות:**
    - מונה הניסיונות (`numberOfGuesses`) גדל ב-1.

    *דוגמה:* `numberOfGuesses` הופך מ-0 ל-1.

4.  **חישוב מספר פיבונאצ'י:**
    - קריאה לפונקציה `fibonacci()` עם מונה הניסיונות הנוכחי (`numberOfGuesses`) כדי לחשב את המספר פיבונאצ'י המתאים (`fibonacciNumber`).
    - הפונקציה מחשבת את סדרת פיבונאצ'י באופן איטרטיבי.
    *דוגמה:* עבור `numberOfGuesses=1`, `fibonacci(1)` יחזיר 1. עבור `numberOfGuesses=3`, `fibonacci(3)` יחזיר 2.

5.  **חישוב מספר בחזקת פיבונאצ'י:**
    - העלאת המספר האקראי שנבחר (`targetNumber`) בחזקת המספר פיבונאצ'י שחושב (`fibonacciNumber`). התוצאה נשמרת במשתנה `poweredNumber`.
    *דוגמה:* עבור `targetNumber = 42` ו-`fibonacciNumber = 1`, `poweredNumber` יהיה 42^1=42. עבור  `targetNumber = 42` ו-`fibonacciNumber = 2`, `poweredNumber` יהיה 42^2=1764.

6. **קבלת קלט מהמשתמש:**
    - בקשת קלט מהמשתמש עם הודעה שמציינת את מספר הניסיון הנוכחי.
    - המרת הקלט למספר שלם. אם הקלט אינו מספר, תודפס הודעת שגיאה והלולאה תמשיך לניסיון הבא.

    *דוגמה:* המשתמש מזין "50" והקלט מומר ל-`userGuess = 50`.

7. **בדיקת ניחוש:**
    - השוואה בין הקלט מהמשתמש (`userGuess`) לתוצאה של החישוב (`poweredNumber`).
    - **אם שווה:** הודעת ניצחון, כולל מספר הניסיונות והלולאה מסתיימת.
        *דוגמה:* אם `userGuess` שווה ל-`poweredNumber`, נניח 42, תודפס הודעה: "POZDRАVLYАYU! Vy ugadali chislo za 1 popytok!".
    - **אם לא שווה:** הודעה למשתמש לנסות שוב והלולאה ממשיכה לניסיון הבא.

8. **סיום:**
   - הלולאה מסתיימת רק אם הניחוש נכון.

## <mermaid>

```mermaid
flowchart TD
    A[התחלה: numberOfGuesses = 0, יצירת targetNumber] --> B{התחלת לולאת משחק};
    B -- לולאה רצה כל עוד לא ניחשו --> C[numberOfGuesses += 1];
    C --> D[חישוב fibonacciNumber = fibonacci(numberOfGuesses)];
    D --> E[חישוב poweredNumber = targetNumber ** fibonacciNumber];
    E --> F{קבלת קלט מהמשתמש userGuess};
    F -- קלט תקין --> G{userGuess == poweredNumber?};
    F -- קלט לא תקין --> H[הודעת שגיאה "הזן מספר שלם"];
    H --> B;
    G -- כן --> I[הודעת ניצחון: "ניחשת נכון!"];
    I --> J[סיום];
    G -- לא --> K[הודעה: "נסה שוב!"];
    K --> B;
```

## <explanation>

**ייבואים (Imports):**

-   `import random`: משמש ליצירת מספר אקראי.

    *   **קשר לחבילות `src.` אחרות:** לא קיים קשר ישיר לחבילות `src.`, זהו מודול סטנדרטי של פייתון.

**פונקציות (Functions):**

-   `fibonacci(n)`:
    -   **פרמטרים:** `n` - מספר שלם המייצג את מיקום האיבר בסדרת פיבונאצ'י.
    -   **ערך מוחזר:** המספר פיבונאצ'י במקום ה-`n`.
    -   **מטרה:** מחשבת את המספר פיבונאצ'י לפי המיקום שניתן.
    -   **דוגמאות:** `fibonacci(0)` יחזיר 0, `fibonacci(1)` יחזיר 1, `fibonacci(5)` יחזיר 5.

**משתנים (Variables):**

-   `numberOfGuesses` (int): סופר את מספר הניסיונות של המשתמש.
-   `targetNumber` (int): מספר אקראי שלם שנוצר בין 1 ל-100.
-   `fibonacciNumber` (int): מספר פיבונאצ'י שחושב עבור כל ניסיון.
-   `poweredNumber` (int): `targetNumber` בחזקת `fibonacciNumber`.
-   `userGuess` (int): הקלט מהמשתמש.

**הסבר מפורט:**

הקוד מיישם משחק ניחוש מספרים פשוט.
המשתמש מנסה לנחש מספר שהמערכת חישבה על ידי העלאת מספר רנדומלי במספר פיבונאצ'י של מספר הניסיון הנוכחי.
הפונקציה `fibonacci` מחשבת את המספר הפיבונאצ'י הרלוונטי לכל ניסיון.
הלולאה `while` ממשיכה עד שהמשתמש מנחש את המספר הנכון.
הקלט מהמשתמש נבדק והופך למספר שלם.
אם הקלט אינו מספר שלם, ההודעה `Please enter an integer` תוצג, והלולאה תמשיך לניסיון הבא.
אם המשתמש מנחש נכון, הודעת ניצחון מוצגת, והמשחק מסתיים.
אחרת, המשתמש מתבקש לנסות שוב.

**בעיות אפשריות ותחומים לשיפור:**

1.  **היעדר בדיקת טווח קלט:** הקוד אינו בודק אם המספר שקולט המשתמש הוא במסגרת טווח סביר.
2.  **מגבלת חישוב:** החזקה של המספר האקראי במספר פיבונאצ'י עלולה לייצר מספרים גדולים מאוד במהירות, דבר שעלול להוביל לבעיות חישוב או גלישה.
3.  **הודעות למשתמש:**  ההודעות למשתמש יכולות להיות יותר מפורטות וידידותיות למשתמש.

**שרשרת קשרים עם חלקים אחרים בפרויקט:**

-   אין קשר ישיר לחלקים אחרים בפרויקט במקרה הזה. הקוד עצמאי ואינו תלוי במודולים אחרים מלבד המודול הסטנדרטי `random`.