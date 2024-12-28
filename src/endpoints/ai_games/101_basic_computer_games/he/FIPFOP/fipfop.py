"""
<FIPFOP>:
=================
קושי: 4
-----------------
המשחק "FIPFOP" הוא משחק מילים פשוט בו המחשב בוחר מילה אקראית ממערך מילים נתון, והשחקן צריך לנחש את האותיות במילה. השחקן מנחש אות אחת בכל פעם, והמחשב מציג את המילה עם האותיות שנמצאו במקומן, ואת האותיות הנותרות מוחלפות בסימן "-". השחקן מקבל רמז לגבי האורך של המילה.

חוקי המשחק:
1. המחשב בוחר מילה אקראית מרשימת מילים מוגדרת.
2. השחקן מנחש אות אחת בכל פעם.
3. אם האות מופיעה במילה, המחשב חושף את מיקומה/ות במילה.
4. אם האות לא מופיעה במילה, אין שינוי בתצוגה.
5. השחקן מנחש עד שהוא מגלה את כל האותיות במילה.
6. המשחק מסתיים כאשר כל האותיות במילה נוחשו.
-----------------
אלגוריתם:
1. אתחל את רשימת המילים האפשריות.
2. בחר מילה אקראית מהרשימה.
3. אתחל את המילה המוצגת כך שכל האותיות מוחלפות ב "-".
4. כל עוד המילה לא פוצחה:
    4.1. הצג את המילה עם האותיות שנמצאו ו "-" במקומות הנותרים.
    4.2. בקש מהשחקן להזין אות.
    4.3. אם האות שהוזנה נמצאת במילה:
        4.3.1. חשוף את כל המקומות בהם האות מופיעה במילה המוצגת.
5. הצג הודעה "YOU GOT IT!"
6. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    words = ['python', 'computer', 'programming', 'algorithm', 'variable']<br>
    targetWord = random(words)<br>
    displayWord = ['-' * len(targetWord)]<br>
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד לא כל האותיות נוחשו"}
    LoopStart -- כן --> DisplayWord["הצגת מילה נוכחית: <code><b>displayWord</b></code>"]
    DisplayWord --> InputGuess["קלט אות מהמשתמש: <code><b>userGuess</b></code>"]
    InputGuess --> CheckGuess{"בדיקה: <code><b>userGuess</b></code> בתוך <code><b>targetWord</b></code>?"}
    CheckGuess -- כן --> UpdateDisplayWord["עדכון: הצגת האותיות שנוחשו ב-<code><b>displayWord</b></code>"]
    UpdateDisplayWord --> LoopStart
    CheckGuess -- לא --> LoopStart
    LoopStart -- לא --> OutputWin["הצגת הודעה: <b>YOU GOT IT!</b>"]
    OutputWin --> End["סוף"]

```

Legenda:
     Start - התחלת התוכנית.
     InitializeVariables - אתחול משתנים: רשימת המילים האפשריות, בחירת מילה אקראית מתוכן, יצירת מילה להצגה עם "-" במקום האותיות.
     LoopStart - תחילת הלולאה, הממשיכה כל עוד המילה לא פוצחה (כלומר כל האותיות לא נוחשו).
     DisplayWord - הצגת המילה עם האותיות שנוחשו במקומות המתאימים ו-"-" במקומות הנותרים.
     InputGuess - קלט אות מהמשתמש.
     CheckGuess - בדיקה האם האות שהוזנה נמצאת במילה המוגלת.
     UpdateDisplayWord - עדכון המילה המוצגת כך שהאות שנמצאה מוחלפת ב-"-" במקומות הנכונים.
     OutputWin - הצגת הודעת ניצחון כאשר המילה פוצחה.
     End - סוף התוכנית.
"""
import random

# רשימת המילים האפשריות
words = ['python', 'computer', 'programming', 'algorithm', 'variable']

# בחירת מילה אקראית מהרשימה
targetWord = random.choice(words)

# יצירת מילה להצגה עם קווים תחתונים במקום האותיות
displayWord = ['-' for _ in targetWord]

# לולאת המשחק הראשית
while True:
    # הדפסת המילה הנוכחית עם האותיות שנמצאו והקווים התחתונים
    print(" ".join(displayWord))

    # קבלת קלט מהמשתמש (ניחוש אות)
    userGuess = input("נחש אות: ").lower()

    # בדיקה אם האות נמצאת במילה
    if userGuess in targetWord:
        # עדכון המילה המוצגת עם האותיות שנמצאו
        for i in range(len(targetWord)):
            if targetWord[i] == userGuess:
                displayWord[i] = userGuess
    else:
         print ("נסה שנית") # אם האות לא נמצאת במילה, לא עושים כלום

    # בדיקה אם כל האותיות נוחשו
    if '-' not in displayWord:
        print("YOU GOT IT!")
        break
"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש לבחירת מילה אקראית.

2.  **הגדרת רשימת המילים `words`**:
    - `words = ['python', 'computer', 'programming', 'algorithm', 'variable']`: יצירת רשימה של מילים מהן תבחר המילה למשחק.

3.  **בחירת מילה אקראית `targetWord`**:
    - `targetWord = random.choice(words)`: בחירת מילה אקראית מרשימת המילים ושמירתה במשתנה `targetWord`.

4.  **יצירת מילה להצגה `displayWord`**:
    - `displayWord = ['-' for _ in targetWord]`: יצירת רשימה חדשה באורך המילה שנבחרה, כאשר כל איבר הוא '-'. רשימה זו תציג את המילה עם האותיות שנמצאו.

5.  **לולאת המשחק `while True`**:
    - `while True:`: לולאה אינסופית שתימשך עד שהשחקן ינחש את כל האותיות במילה.

6.  **הדפסת המילה הנוכחית**:
    - `print(" ".join(displayWord))`: הדפסת המילה המוצגת עם רווחים בין התווים.

7.  **קבלת קלט מהמשתמש**:
    - `userGuess = input("נחש אות: ").lower()`: בקשה מהמשתמש להזין אות, והמרתה לאות קטנה.

8.  **בדיקה אם האות נמצאת במילה**:
    - `if userGuess in targetWord:`: בדיקה האם האות שהוזנה נמצאת במילה.

9.  **עדכון המילה המוצגת**:
    - `for i in range(len(targetWord)):`: מעבר על כל האותיות במילה.
    -  `if targetWord[i] == userGuess:`: אם האות הנוכחית במילה שווה לאות שהמשתמש ניחש,
    -  `displayWord[i] = userGuess`: עדכון המילה המוצגת באות הנכונה.

10. **בדיקה אם המשחק הסתיים**:
     - `if '-' not in displayWord:`: אם אין יותר מקפים במילה להצגה, כלומר כל האותיות נוחשו.
     - `print("YOU GOT IT!")`: הודעה למשתמש שניצח.
     - `break`: יציאה מהלולאה והמשחק מסתיים.
"""
