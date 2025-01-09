## <algorithm>
1. **אתחול `previousNumber`**:
   - המשתנה `previousNumber` מאותחל ל-0. זהו הערך ההתחלתי שייצג את המספר הקודם שנוצר.
   - לדוגמה: `previousNumber = 0`.

2. **לולאה אינסופית**:
   - מתחיל לולאה `while True` שתרוץ עד שהיא תופסק על ידי פקודת `break`.
   - הלולאה הזו מייצגת את המשחק עצמו, שרץ עד שהשחקן מפסיד או מחליט לעזוב.

3. **יצירת מספר אקראי `currentNumber`**:
   - נוצר מספר אקראי בין 0 ל-7 (כולל) באמצעות `random.randint(0, 7)`. המספר האקראי הזה נשמר במשתנה `currentNumber`.
   - לדוגמה: `currentNumber` יכול להיות 3, 5, 0 וכו'.

4. **בדיקה אם השחקן רוצה לסיים את המשחק**:
   - נבדק האם `currentNumber` שווה ל-0. אם כן, המשחק מסתיים, ומוצגת ההודעה "YOU BLEW IT!".
   - דוגמה: אם `currentNumber == 0`, המשחק נגמר.

5. **בדיקה אם המספר הנוכחי שווה למספר הקודם**:
   - נבדק האם `currentNumber` שווה ל-`previousNumber`. אם כן, השחקן הפסיד, ומוצגת ההודעה "YOU BLEW IT!".
   - דוגמה: אם `previousNumber = 3` ו-`currentNumber = 3`, המשחק נגמר.

6. **הדפסת המספר הנוכחי**:
   - אם שני התנאים הקודמים לא התקיימו, מדפיסים את הערך של `currentNumber`.

7. **עדכון `previousNumber`**:
   - הערך של `currentNumber` מועבר לתוך `previousNumber` כדי להכין את עצמנו לסיבוב הבא.

8. **חזרה לשלב 2**:
   - הלולאה חוזרת לשלב 2 כדי ליצור מספר אקראי נוסף.
   - התהליך יחזור עד שהמשחק ייגמר או שהלולאה תופסק.

## <mermaid>
```mermaid
flowchart TD
    Start["התחלה"] --> InitializePreviousNumber[/"אתחול: <br> <code><b>previousNumber = 0</b></code>"/]
    InitializePreviousNumber --> LoopStart{{"לולאה אינסופית"}};
    LoopStart --> GenerateRandomNumber[/"יצירת מספר אקראי: <br> <code><b>currentNumber = random(0, 7)</b></code>"/];
    GenerateRandomNumber --> CheckQuit{/"בדיקה: <br> <code><b>currentNumber == 0</b></code>?"/};
    CheckQuit -- "כן" --> OutputBlowIt[/"הדפסה: <b>YOU BLEW IT!</b>"/];
    OutputBlowIt --> End["סיום"];
    CheckQuit -- "לא" --> CheckSame{/"בדיקה: <br> <code><b>currentNumber == previousNumber</b></code>?"/};
    CheckSame -- "כן" --> OutputBlowIt;
    CheckSame -- "לא" --> OutputCurrentNumber[/"הדפסה: <br> <code><b>currentNumber</b></code>"/];
    OutputCurrentNumber --> SetPreviousNumber[/"עדכון: <br> <code><b>previousNumber = currentNumber</b></code>"/];
    SetPreviousNumber --> LoopStart;
    
    
  
```

**הסבר תלויות ב-Mermaid:**
- **flowchart TD**: מגדיר את סוג התרשים כתרשים זרימה מלמעלה למטה.
- **Start, InitializePreviousNumber, LoopStart, GenerateRandomNumber, CheckQuit, OutputBlowIt, End, CheckSame, OutputCurrentNumber, SetPreviousNumber**: אלו הם צמתים שונים בתרשים, המייצגים שלבים או נקודות קריטיות בזרימת הקוד.
- **-->**: החצים שמחברים בין הצמתים מייצגים את כיוון זרימת השליטה או המידע.
- **"/..."/**: תווית על גבי הצומת, הכוללת תיאור מפורט של השלב, בפורמט markdown, כולל קטעי קוד להמחשה.

## <explanation>
### ייבואים (Imports)
- `import random`: מייבא את מודול `random` של פייתון, המכיל פונקציות ליצירת מספרים אקראיים. הוא משמש ליצירת המספרים האקראיים במשחק. אין תלות בחבילות אחרות תחת `src`.

### משתנים (Variables)
- `previousNumber`: משתנה שלם המאחסן את המספר האקראי שנוצר בסיבוב הקודם. מאותחל ל-0 בתחילת המשחק. הוא משמש כדי לוודא שלא נוצרים שני מספרים זהים רצופים.
- `currentNumber`: משתנה שלם שמאחסן את המספר האקראי שנוצר בסיבוב הנוכחי. הערך שלו משתנה בכל איטרציה של הלולאה.

### פונקציות (Functions)
- אין בקוד פונקציות מוגדרות על ידי המשתמש. השימוש בפונקציות נעשה באופן ישיר דרך מודולים, לדוגמה `random.randint()`.

### לולאה (Loop)
- `while True:`: לולאה אינסופית. תמשיך לרוץ עד שתופסק על ידי פקודת `break`. הלולאה הזו היא הליבה של המשחק.

### תנאים (Conditions)
- `if currentNumber == 0:`: בודק האם המשתמש רצה לסיים את המשחק על ידי יצירת 0. אם כן, המשחק מסתיים.
- `if currentNumber == previousNumber:`: בודק האם המספר הנוכחי זהה לקודם. אם כן, השחקן הפסיד והמשחק מסתיים.

### פעולות
- `random.randint(0, 7)`: יוצר מספר אקראי שלם בין 0 ל-7.
- `print("YOU BLEW IT!")`: מדפיס את ההודעה המציינת שהמשחק נגמר (במקרה של הפסד או סיום יזום).
- `print(currentNumber)`: מדפיס את המספר האקראי הנוכחי.

### בעיות אפשריות ותחומים לשיפור:
- **משחק טקסטואלי בסיסי**: המשחק פשוט מאוד, ואין ממשק משתמש אינטראקטיבי.
- **הודעה סיום קשיחה**: ההודעה "YOU BLEW IT!" אינה ידידותית, וניתן להחליפה בהודעה טובה יותר, עם התייחסות גם לסיבת הסיום (הפסד או סיום יזום).
- **חוסר בקלט מהמשתמש**: מעבר ללחיצה על "0" אין אינטראקציה עם השחקן (יכול להיות אפשרות לשחק סיבוב נוסף).
- **המשחק לא מוגדר מראש**: קשה לחזות את זמן סיום המשחק.

### שרשרת קשרים עם חלקים אחרים בפרויקט:
- משחק זה אינו תלוי בחלקים אחרים בפרויקט. הוא משתמש רק במודול `random` של פייתון.