# CHIEF

## סקירה כללית

משחק "CHIEF" הוא משחק בו השחקן משחק בתור מנהל, שתפקידו לתכנן את הייצור במפעל. השחקן קובע את הכמות המיוצרת מכל סוג של פריטים, והמחשב קובע האם הערכים האלו עומדים בדרישות. אם לא, השחקן מקבל מידע על אילו ערכים היו שגויים. מטרת המשחק היא להשיג ייצור מיטבי, על ידי ניחוש נכון של כמות הפריטים.

## תוכן עניינים

- [חוקי המשחק](#חוקי-המשחק)
- [אלגוריתם](#אלגוריתם)
- [תרשים זרימה](#תרשים-זרימה)
- [הסברים לתרשים זרימה](#הסברים-לתרשים-זרימה)

## חוקי המשחק

1. המחשב בוחר שלושה ערכים אקראיים בטווח של 1 עד 10: `targetA`, `targetB` ו-`targetC`.
2. השחקן מזין את הניחושים שלו עבור הערכים: `userA`, `userB` ו-`userC`.
3. המחשב בודק האם הערכים שהוזנו תואמים לערכים שנבחרו אקראית.
4. אם כל שלושת הערכים נוחשו נכון, המשחק מסתיים בניצחון.
5. אם לפחות ערך אחד לא תואם, המחשב מציג אילו ערכים היו שגויים.
6. המשחק נמשך עד שהשחקן מנחש את כל שלושת הערכים נכונה.

## אלגוריתם

1. ליצור מספרים אקראיים שלמים `targetA`, `targetB` ו-`targetC` בטווח מ-1 עד 10.
2. להתחיל לולאה "כל עוד כל המספרים לא נוחשו נכון":
   2.1 לבקש מהשחקן להזין שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
   2.2 לאתחל את המחרוזת `message` למחרוזת ריקה.
   2.3 אם `userA` לא שווה ל-`targetA`, להוסיף "A" ל-`message`.
   2.4 אם `userB` לא שווה ל-`targetB`, להוסיף "B" ל-`message`.
   2.5 אם `userC` לא שווה ל-`targetC`, להוסיף "C" ל-`message`.
   2.6 אם `message` אינה ריקה, להדפיס את ההודעה "WRONG ON" ואת `message`.
   2.7 אחרת, להדפיס את ההודעה "YOU GOT IT!".
3. סוף המשחק.

## תרשים זרימה

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:\n    <code><b>\n    targetA = random(1, 10)\n    targetB = random(1, 10)\n    targetC = random(1, 10)\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחש"}\
    LoopStart --> InputValues["<p align='left'>קלט מספרים מהמשתמש:\n    <code><b>\n    userA\n    userB\n    userC\n    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA?</b></code>"}\
    CheckA -- לא --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB?</b></code>"}\
    CheckA -- כן --> CheckB
    CheckB -- לא --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC?</b></code>"}\
    CheckB -- כן --> CheckC
    CheckC -- לא --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}\
    CheckC -- כן --> CheckMessage
    CheckMessage -- כן --> OutputWrong["פלט הודעה: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- לא --> OutputWin["פלט הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    LoopStart -- לא --> End
```

## הסברים לתרשים זרימה

*   **Start** - תחילת התוכנית.
*   **InitializeVariables** - אתחול משתנים: `targetA`, `targetB`, `targetC` נוצרים באופן אקראי מ-1 עד 10.
*   **LoopStart** - תחילת לולאה, שנמשכת עד שהשחקן מנחש את כל המספרים.
*   **InputValues** - בקשה מהמשתמש להזין שלושה מספרים `userA`, `userB`, `userC`.
*   **InitializeMessage** - אתחול מחרוזת ריקה `message`.
*   **CheckA** - בדיקה האם המספר שהוזן `userA` שווה למספר שנבחר אקראית `targetA`.
*   **AppendA** - הוספת 'A' למחרוזת `message`, אם `userA` לא שווה ל-`targetA`.
*   **CheckB** - בדיקה האם המספר שהוזן `userB` שווה למספר שנבחר אקראית `targetB`.
*   **AppendB** - הוספת 'B' למחרוזת `message`, אם `userB` לא שווה ל-`targetB`.
*   **CheckC** - בדיקה האם המספר שהוזן `userC` שווה למספר שנבחר אקראית `targetC`.
*   **AppendC** - הוספת 'C' למחרוזת `message`, אם `userC` לא שווה ל-`targetC`.
*   **CheckMessage** - בדיקה האם המחרוזת `message` ריקה.
*   **OutputWrong** - הדפסת ההודעה "WRONG ON" ואת תוכן המשתנה `message`, אם המחרוזת אינה ריקה.
*   **OutputWin** - הדפסת ההודעה "YOU GOT IT!", אם המחרוזת `message` ריקה.
*   **End** - סוף התוכנית.