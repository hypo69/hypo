## <algorithm>
הקוד מיישם משחק ניחוש מילים פשוט בשם "CHEMST", בו המשתמש מנסה לנחש שם של יסוד כימי. להלן תיאור צעד אחר צעד של האלגוריתם:

1. **הגדרת רשימת יסודות כימיים**:
    - `elements = ['HYDROGEN', 'HELIUM', ... ]`: נוצרת רשימה של יסודות כימיים.
    - דוגמה: `elements` תהיה רשימה של מחרוזות, כל מחרוזת מייצגת שם של יסוד כימי.

2. **בחירת יסוד כימי אקראי**:
   - `targetElement = random.choice(elements)`: נבחר באופן אקראי יסוד כימי מתוך רשימת היסודות.
   - דוגמה: `targetElement` יכול לקבל את הערך 'CARBON'.

3.  **איפוס מספר הניחושים**:
    - `numberOfGuesses = 0`: מונה הניחושים מאותחל לאפס.
    - דוגמה:  הערך ההתחלתי של `numberOfGuesses` הוא 0.

4.  **לולאת משחק ראשית**:
    - `while numberOfGuesses < 8:`:  המשחק ימשיך כל עוד מספר הניחושים קטן מ-8.

5.  **קבלת ניחוש מהמשתמש**:
    - `userGuess = input("Введите название элемента: ").upper()`:  המשתמש מתבקש להכניס ניחוש, והקלט הופך לאותיות גדולות.
    - דוגמה: אם המשתמש מכניס "carbon", `userGuess` יהיה "CARBON".

6.  **הגדלת מספר הניחושים**:
    -  `numberOfGuesses += 1`: מספר הניחושים מוגדל ב-1.
    - דוגמה: אם `numberOfGuesses` היה 0, עכשיו הוא יהיה 1.

7.  **בדיקת ניחוש**:
    -  `if userGuess == targetElement:`: בודק האם הניחוש שווה ליסוד הכימי שנבחר.
    -  אם שווה:
      -  `print(f"ПОЗДРАВЛЯЮ! Вы угадали элемент за {numberOfGuesses} попыток!")`: מוצגת הודעת ניצחון עם מספר הניחושים.
      - `break`: הלולאה מסתיימת.
    - אם לא שווה:
        - `hint = ""`:  מחרוזת רמז ריקה נוצרת.
        -  **לולאת רמז**:
           -  `for i in range(len(targetElement)):`: לולאה שעוברת על כל תו ביסוד הכימי הנבחר.
            - `if i < len(userGuess):`: בדיקה שהאינדקס לא חורג מאורך ניחוש המשתמש.
             -  `if userGuess[i] == targetElement[i]:`: אם התו במיקום הנוכחי בניחוש זהה לתו ביסוד הכימי, התו מתווסף לרמז.
              - דוגמה: אם `targetElement` הוא "CARBON" ו-`userGuess` הוא "CARROT", אז הרמז יהיה "CAR".
             -  `elif userGuess[i] in targetElement:`: אם התו בניחוש נמצא ביסוד הכימי (אך במיקום שונה) "+" מתווסף לרמז.
              - דוגמה: אם `targetElement` הוא "CARBON" ו-`userGuess` הוא "ROCKS", אז הרמז יהיה "++--".
             - `else:` אם התו אינו נמצא ביסוד הכימי, "-" מתווסף לרמז.
              - דוגמה: אם `targetElement` הוא "CARBON" ו-`userGuess` הוא "SADLY", אז הרמז יהיה "--".
            - `else:` אם האינדקס חורג מאורך ניחוש המשתמש, "-" מתווסף לרמז.
         - `print(hint)`: הרמז מוצג למשתמש.

8. **בדיקת הפסד**:
    - `if numberOfGuesses == 8:`:  אם מספר הניחושים הגיע ל-8, המשחק מסתיים בהפסד.
        -  `print(f"ВЫ ПРОИГРАЛИ! Загаданный элемент был {targetElement}")`: מוצגת הודעה על הפסד עם היסוד הכימי הנכון.

## <mermaid>
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:<br><code>elements = [...]<br>targetElement = random(elements)<br>numberOfGuesses = 0</code></p>"]
    InitializeVariables --> GameLoopStart{"התחלת לולאת משחק:<br><code>numberOfGuesses < 8</code>"}
    GameLoopStart -- "כן" --> GetUserGuess["קבלת ניחוש מהמשתמש:<br><code>userGuess = input().upper()</code>"]
    GetUserGuess --> IncrementGuesses["הגדלת מונה הניחושים:<br><code>numberOfGuesses += 1</code>"]
    IncrementGuesses --> CheckWinCondition{"בדיקת תנאי ניצחון:<br><code>userGuess == targetElement</code>"}
    CheckWinCondition -- "כן" --> OutputWinMessage["פלט הודעת ניצחון:<br><code>"ניצחת! ב{numberOfGuesses} ניסיונות"</code>"]
    OutputWinMessage --> End["סיום"]
    CheckWinCondition -- "לא" --> GenerateHintString["יצירת מחרוזת רמז:<br><code>hint = ""<br>לולאה על כל תו ב-targetElement</code>"]
    GenerateHintString --> DisplayHint["פלט רמז:<br><code>print(hint)</code>"]
    DisplayHint --> GameLoopStart
    GameLoopStart -- "לא" --> OutputLoseMessage["פלט הודעת הפסד:<br><code>"הפסדת! היסוד היה {targetElement}"</code>"]
    OutputLoseMessage --> End
    
    subgraph "מחולל רמז"
    GenerateHintString --> CheckUserGuessLength["בדיקת אורך ניחוש:<br><code>i < len(userGuess)</code>"]
    CheckUserGuessLength -- "כן" --> CheckMatchingChar["בדיקת תו זהה:<br><code>userGuess[i] == targetElement[i]</code>"]
    CheckMatchingChar -- "כן" --> AddMatchingChar["הוספת תו תואם ל-hint"]
    AddMatchingChar --> CheckNextChar["לולאה על התו הבא"]
    CheckMatchingChar -- "לא" --> CheckCharInTarget["בדיקה אם התו קיים ביסוד:<br><code>userGuess[i] in targetElement</code>"]
    CheckCharInTarget -- "כן" --> AddPlusSign["הוספת '+' ל-hint"]
    AddPlusSign --> CheckNextChar
    CheckCharInTarget -- "לא" --> AddMinusSign["הוספת '-' ל-hint"]
    AddMinusSign --> CheckNextChar
     CheckUserGuessLength -- "לא" --> AddMinusSign_short
     AddMinusSign_short --> CheckNextChar
     CheckNextChar --> GenerateHintString
    end
```

התרשים מציג את זרימת הפעולות במשחק "CHEMST". הוא מתחיל באתחול משתנים כמו רשימת היסודות ומספר הניחושים. לאחר מכן, מתחילת לולאה שרצה כל עוד מספר הניחושים קטן מ-8. בתוך הלולאה, המשתמש מכניס ניחוש, מונה הניחושים עולה באחד ונבדק האם הניחוש נכון. אם הוא נכון, מוצגת הודעת ניצחון והמשחק מסתיים. אם הניחוש לא נכון, נוצר רמז, מוצג למשתמש והלולאה ממשיכה. אם הלולאה מסתיימת מבלי שהמשתמש ניצח (כלומר, מספר הניחושים הגיע ל-8), מוצגת הודעת הפסד. התרשים מחלק את חלק יצירת הרמז לתוך תת-גרף המציג את תהליך השוואת האותיות בין הניחוש למילה הנכונה, וכיצד נבנית מחרוזת הרמז.

## <explanation>

### ייבואים (Imports)
- `import random`: מייבא את מודול `random` המאפשר יצירת מספרים אקראיים. זה נחוץ לבחירת יסוד כימי אקראי מתוך רשימת היסודות.

### משתנים (Variables)
- `elements`: רשימה (list) של מחרוזות (string), כאשר כל מחרוזת מייצגת שם של יסוד כימי.
- `targetElement`: מחרוזת (string) המכילה את שם היסוד הכימי האקראי שנבחר על ידי המחשב.
- `numberOfGuesses`: מספר שלם (int) המייצג את מספר הניחושים שהמשתמש ביצע.

### פונקציות (Functions)
- אין פונקציות מוגדרות במפורש, אך הקוד משתמש בפונקציות מובנות של פייתון כמו `input()`, `print()`, `random.choice()` ו- `upper()`:
    - `input()`: מקבל קלט מהמשתמש.
    - `print()`: מציג פלט למסך.
    - `random.choice(elements)`: בוחר באופן אקראי איבר מתוך הרשימה `elements`.
    - `upper()`: ממיר מחרוזת לאותיות גדולות.

### מחלקות (Classes)
- אין מחלקות בקוד זה.

### הסבר מפורט
- הקוד מיישם משחק ניחושים פשוט. הוא מתחיל ביצירת רשימה של שמות יסודות כימיים. לאחר מכן הוא בוחר יסוד כימי באופן אקראי מהרשימה. המשתמש מנסה לנחש את שם היסוד כאשר אחרי כל ניסיון מקבל רמז המציין אילו אותיות נכונות ובאיזה מיקום (אות נכונה במיקום נכון, אות נכונה במיקום לא נכון, אות לא קיימת). למשתמש יש עד 8 ניסיונות. אם הוא מצליח לנחש את היסוד, הוא מנצח. אם לא, הוא מפסיד.

### בעיות אפשריות ותחומים לשיפור
1. **טיפול בקלט שגוי**: הקוד לא מטפל במקרים בהם המשתמש מכניס קלט שאינו אותיות או אם הקלט ריק. כדאי להוסיף בדיקות קלט.
2. **מגבלת רשימת היסודות**: רשימת היסודות מוגבלת, ניתן להרחיב אותה.
3. **שיפור הרמז**: ניתן לשפר את הרמז כך שיהיה יותר אינפורמטיבי. לדוגמה, במקום "+" פשוט, אפשר לספק מידע על המיקום של האות הנכונה.
4. **עיצוב ממשק המשתמש**: ממשק המשתמש פשוט. אפשר להשתמש בספריות כמו `curses` כדי ליצור ממשק טקסטואלי יותר אינטראקטיבי.
5. **הגבלת מספר ניסיונות**: כרגע מספר הניסיונות קבוע (8). ניתן להוסיף אפשרות שהמשתמש יבחר את מספר הניסיונות.
6.  **אפשרות למשחק חוזר**: בסיום המשחק, אין אופציה לשחק שוב. כדאי להוסיף את האפשרות הזו.

### קשרי גומלין עם חלקים אחרים בפרויקט
- הקוד עצמאי ואין לו תלות בקבצים אחרים או חבילות בפרויקט `hypotez` (למעט `random`, שזו ספריה סטנדרטית של פייתון). הקוד מהווה משחק בפני עצמו, לכן אין קשרי גומלין ישירים.