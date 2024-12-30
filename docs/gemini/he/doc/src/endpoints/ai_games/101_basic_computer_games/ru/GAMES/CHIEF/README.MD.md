# CHIEF

## סקירה כללית

המשחק "CHIEF" הוא משחק שבו השחקן משחק בתור מנהל, שתפקידו לתכנן את הייצור במפעל. השחקן קובע את כמות הפריטים המיוצרים מכל סוג, והמחשב קובע האם הערכים תואמים את הדרישות הנחוצות. אם לא, השחקן מקבל הודעה אילו ערכים היו שגויים. מטרת המשחק היא להגיע לייצור אופטימלי, על ידי ניחוש נכון של כמות הפריטים.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [חוקי המשחק](#חוקי-המשחק)
- [אלגוריתם](#אלגוריתם)
- [דיאגרמת זרימה](#דיאגרמת-זרימה)
- [מקרא](#מקרא)

## חוקי המשחק

1. המחשב בוחר שלושה ערכים בטווח שבין 1 ל-10: `targetA`, `targetB` ו-`targetC`.
2. השחקן מזין את הניחושים שלו עבור הערכים `userA`, `userB` ו-`userC`.
3. המחשב בודק האם הערכים שהוזנו תואמים לערכים שנבחרו.
4. אם כל שלושת הערכים נוחשו נכונה, המשחק מסתיים בניצחון.
5. אם לפחות ערך אחד לא תואם, המחשב מציג אילו ערכים היו שגויים.
6. המשחק ממשיך עד שהשחקן מנחש את כל שלושת הערכים.

## אלגוריתם

1.  יצירת מספרים שלמים אקראיים `targetA`, `targetB` ו-`targetC` בטווח שבין 1 ל-10.
2.  התחלת לולאה "כל עוד לא נוחשו כל המספרים":
    2.1 בקשה מהשחקן להזין שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
    2.2 אתחול מחרוזת `message` כמחרוזת ריקה.
    2.3 אם `userA` לא שווה ל-`targetA`, הוספה של "A" ל-`message`.
    2.4 אם `userB` לא שווה ל-`targetB`, הוספה של "B" ל-`message`.
    2.5 אם `userC` לא שווה ל-`targetC`, הוספה של "C" ל-`message`.
    2.6 אם `message` לא ריקה, הצגת הודעה "WRONG ON" ו-`message`.
    2.7 אחרת, הצגת הודעה "YOU GOT IT!".
3. סיום המשחק.

## דיאגרמת זרימה

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:\n    <code><b>\n    targetA = random(1, 10)\n    targetB = random(1, 10)\n    targetC = random(1, 10)\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"התחלת לולאה: כל עוד לא נוחש"}
    LoopStart --> InputValues["<p align='left'>קלט מספרים מהמשתמש:\n    <code><b>\n    userA\n    userB\n    userC\n    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"בדיקה: <code><b>userA == targetA?</b></code>"}
    CheckA -- לא --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"בדיקה: <code><b>userB == targetB?</b></code>"}
    CheckA -- כן --> CheckB
    CheckB -- לא --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"בדיקה: <code><b>userC == targetC?</b></code>"}
    CheckB -- כן --> CheckC
    CheckC -- לא --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"בדיקה: <code><b>message != "" ?</b></code>"}
    CheckC -- כן --> CheckMessage
    CheckMessage -- כן --> OutputWrong["הצגת הודעה: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- לא --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סיום"]
    LoopStart -- לא --> End
```

## מקרא

    Start - תחילת התוכנית.
    InitializeVariables - אתחול משתנים: `targetA`, `targetB`, `targetC` נוצרים באופן אקראי בין 1 ל-10.
    LoopStart - תחילת הלולאה, שנמשכת כל עוד השחקן לא ניחש את כל המספרים.
    InputValues - בקשה מהמשתמש להזין שלושה מספרים `userA`, `userB`, `userC`.
    InitializeMessage - אתחול מחרוזת ריקה `message`.
    CheckA - בדיקה האם המספר שהוזן `userA` שווה למספר שנבחר `targetA`.
    AppendA - הוספת 'A' ל-`message`, אם `userA` לא שווה ל-`targetA`.
    CheckB - בדיקה האם המספר שהוזן `userB` שווה למספר שנבחר `targetB`.
    AppendB - הוספת 'B' ל-`message`, אם `userB` לא שווה ל-`targetB`.
    CheckC - בדיקה האם המספר שהוזן `userC` שווה למספר שנבחר `targetC`.
    AppendC - הוספת 'C' ל-`message`, אם `userC` לא שווה ל-`targetC`.
    CheckMessage - בדיקה האם המחרוזת `message` ריקה.
    OutputWrong - הצגת ההודעה "WRONG ON" ואת תוכן `message`, אם המחרוזת לא ריקה.
    OutputWin - הצגת ההודעה "YOU GOT IT!", אם המחרוזת `message` ריקה.
    End - סוף התוכנית.