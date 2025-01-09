## ניתוח קוד: `spacwrd.py`

### 1. **<algorithm>**

**תיאור תהליך העבודה:**

הקוד מיישם משחק ניחוש מילים בשם "מילת החלל". המשחק בוחר מילה באופן אקראי מרשימה מוגדרת מראש והשחקן צריך לנחש את המילה על ידי ניחוש אותיות בודדות.

1.  **אתחול:**
    *   רשימת המילים (`word_list`) מוגדרת מראש.
    *   מילה אקראית נבחרת מהרשימה (`target_word`).
    *   משתנה המציג את המילה עם קווים תחתונים במקום אותיות (`guessed_word`) מאותחל.
    *   רשימה ריקה לאחסון אותיות שניחשו נכון (`guessed_letters`) מאותחלת.
    *   מונה עבור אותיות שניחשו נכון `correct_guesses_count` מאותחל.
2.  **לולאת משחק:**
    *   כל עוד השחקן לא ניחש את כל אותיות המילה:
        *   המילה המנוחשת המוצגת עם קווים תחתונים מודפסת למסך.
        *   השחקן מתבקש להזין אות.
        *   אם האות נמצאת במילה המטרה:
            *   האות מתווספת לרשימת האותיות שניחשו.
            *   המילה המוצגת מעודכנת כך שהאות המנוחשת נחשפת בכל המיקומים בהם היא מופיעה.
            *   מונה האותיות המנוחשות מעודכן.
        *  אם האות לא נמצאת, מתקבלת הודעה שהאות לא במילה.
    *   אם כל אותיות המילה נוחשו, המשחק מסתיים ומודפסת הודעת ניצחון.

**דוגמאות לבלוקים לוגיים:**

*   **בחירת מילה אקראית:** `target_word = choose_word(word_list)`. אם `word_list` הוא `["APPLE", "BANANA", "CHERRY"]`, ו-`choose_word` מחזירה "BANANA", אז `target_word` יהיה "BANANA".
*   **אתחול המילה המנוחשת:** `guessed_word = "_ " * len(target_word)`. אם `target_word` הוא "APPLE", אז `guessed_word` יהיה "_ _ _ _ _ ".
*   **ניחוש אות:** אם השחקן מזין "A" ו-`target_word` הוא "APPLE", אז הרשימה `guessed_letters` תהפוך ל `['A']`, והמילה המוצגת תעודכן ל `A _ _ _ _`.
*  **עדכון ספירת האותיות שניחשו:** פונקציה `correct_guesses(guessed_letters, target_word)`: אם `guessed_letters` זה `['A', 'P']` ו- `target_word` זה "APPLE", אז הערך המוחזר יהיה 2.

**זרימת נתונים:**

1.  פונקציה `play_spaceword_game` קוראת לפונקציה `choose_word` כדי לקבל מילה.
2.  פונקציה `play_spaceword_game` קוראת לפונקציה `display_word` כדי להציג את המילה עם קווים תחתונים.
3.  הפונקציה `play_spaceword_game` מקבלת קלט מהמשתמש.
4.  הפונקציה `play_spaceword_game` קוראת לפונקציה `update_word` כדי לעדכן את המילה המוצגת.
5.  הפונקציה `play_spaceword_game` קוראת לפונקציה `correct_guesses` כדי לספור את האותיות שניחשו נכון.

### 2.  **<mermaid>**

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:\n    <code><b>\n    wordList = ['APPLE', 'BANANA', 'CHERRY', ...]\n    targetWord = choose_word(wordList)\n    guessedWord = '_ ' * len(targetWord)\n    guessedLetters = []\n    correctGuessesCount = 0\n    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא נוחשה כל המילה"}
    LoopStart -- כן --> OutputWord["הצגה: <code><b>guessedWord</b></code>"]
    OutputWord --> InputLetter["קליטת קלט: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"בדיקה: <code><b>userLetter in targetWord?</b></code>"}
    CheckLetter -- כן --> UpdateWord["<p align='left'>עדכון:\n    <code><b>\n    guessedLetters.append(userLetter)\n    guessedWord = update_word(targetWord, guessedWord, userLetter)\n    correctGuessesCount = correct_guesses(guessedLetters, targetWord)\n    </b></code></p>"]
     UpdateWord --> CheckWin{ "בדיקה:<code><b>correctGuessesCount == len(targetWord)?</b></code>"}
    CheckLetter -- לא --> MessageNoLetter["הצגה: 'האות לא במילה'"]
    MessageNoLetter --> CheckWin
    CheckWin -- כן --> OutputWin["הצגה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]
    CheckWin -- לא --> LoopStart
    LoopStart -- לא --> End

```

**ניתוח התלויות:**
* אין תלויות מיובאות בקוד. הקוד משתמש בפונקציות בסיסיות של פייתון ובמודול `random`.

### 3. **<explanation>**

**ייבואים (Imports):**

*   `import random`: מייבא את מודול ה-`random`, המשמש ליצירת מספרים אקראיים, ובפרט לבחירת מילה אקראית מרשימת המילים.

**פונקציות (Functions):**

*   `choose_word(word_list)`:
    *   פרמטר: `word_list` - רשימה של מילים.
    *   ערך מוחזר: מילה אקראית מהרשימה.
    *   מטרה: לבחור מילה אקראית מתוך רשימת המילים למשחק.
    *   דוגמה: אם `word_list` הוא `["CAT", "DOG", "BIRD"]`, הפונקציה יכולה להחזיר "DOG".
*   `display_word(word, guessed_letters)`:
    *   פרמטרים: `word` - המילה שצריך להציג, `guessed_letters` - רשימה של אותיות שניחשו.
    *   ערך מוחזר: מחרוזת המציגה את המילה עם קווים תחתונים לאותיות שלא נוחשו.
    *   מטרה: להציג את המילה עם אותיות גלויות רק אם הן נמצאות ברשימה של אותיות שניחשו.
    *   דוגמה: אם `word` הוא "APPLE" ו-`guessed_letters` הוא `['A', 'E']`, הפונקציה תחזיר "A _ _ _ E".
*  `update_word(word, guessed_word, user_letter)`:
    *   פרמטרים: `word` - המילה המקורית, `guessed_word` - המילה הנוכחית עם קווים תחתונים ואותיות מנוחשות, `user_letter` - האות שהמשתמש ניחש.
    *   ערך מוחזר: מחרוזת מעודכנת שמציגה את האותיות המנוחשות.
    *   מטרה: לעדכן את המילה המוצגת על ידי חשיפת כל המיקומים של האות המנוחשת.
    *   דוגמה: אם `word` הוא "APPLE", `guessed_word` הוא "A _ _ _ E" ו-`user_letter` הוא "P", הפונקציה תחזיר "A P P _ E".
*   `correct_guesses(guessed_letters, target_word)`:
    *   פרמטרים: `guessed_letters` - רשימה של אותיות שניחשו, `target_word` - המילה הנכונה.
    *   ערך מוחזר: מספר האותיות שניחשו נכון.
    *   מטרה: לחשב כמה אותיות מנוחשות יש במילה הנכונה.
    *   דוגמה: אם `guessed_letters` זה `['A', 'P']` ו- `target_word` זה "APPLE", אז הערך המוחזר יהיה 2.

*   `play_spaceword_game()`:
    *   פרמטרים: אין.
    *   ערך מוחזר: אין.
    *   מטרה: מממשת את לוגיקת המשחק הכוללת בחירת מילה, הצגת המילה, קבלת קלט מהמשתמש, עידכון מצב המשחק והודעת ניצחון.

**משתנים (Variables):**

*   `word_list`: רשימה קבועה של מילים המשמשות במשחק.
*   `target_word`: המילה האקראית שנבחרה למשחק.
*   `guessed_word`: מחרוזת המציגה את המילה עם קווים תחתונים לאותיות שלא נוחשו.
*   `guessed_letters`: רשימה של אותיות שניחשו נכון.
*   `correct_guesses_count`: ספירה של האותיות שניחשו נכון.

**בעיות אפשריות ותחומים לשיפור:**

*   **בדיקת קלט:** הקוד לא בודק האם קלט המשתמש הוא אות בודדת. שיפור אפשרי יהיה לבדוק את תקינות הקלט.
*   **התייחסות לאותיות כפולות:** כרגע, אם השחקן מנחש אות כפולה, הספירה לא תתעדכן כראוי.
*   **חווית משתמש:** ניתן לשפר את חוויית המשתמש על ידי הוספת מספר נסיונות, רמזים, ועוד.
*   **יעילות:** הפונקציה `correct_guesses` עוברת על הרשימה ומוחקת איברים ממנה, מה שאינו יעיל. אפשר לייעל זאת על ידי שימוש ב-`set` בתחילת הפונקציה.

**שרשרת קשרים עם חלקים אחרים בפרויקט:**
* אין קשרים ישירים עם חלקים אחרים בפרויקט, הקוד עומד בפני עצמו.