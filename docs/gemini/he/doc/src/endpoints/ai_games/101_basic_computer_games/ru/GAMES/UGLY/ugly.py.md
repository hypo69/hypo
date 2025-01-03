# ugly.py

## סקירה כללית

קובץ זה מיישם משחק ניחושים פשוט בשם "UGLY", שבו המחשב מייצר מספר אקראי והשחקן צריך לנחש אותו. המשחק מספק רמזים אם הניחוש גבוה או נמוך מדי.

## תוכן עניינים

- [פונקציות](#פונקציות)
- [הסבר קוד](#הסבר-קוד)

## פונקציות

אין פונקציות מוגדרות במפורש בקוד זה. הקוד כולל לולאה ראשית בתוך סקריפט ברמה העליונה.

## הסבר קוד

### סקירה כללית של הקוד
הקוד הזה הוא יישום פשוט של משחק ניחושים. הוא מתחיל ביצירת מספר אקראי בין 1 ל-100, ולאחר מכן נכנס ללולאה שממשיכה עד שהמשתמש מנחש את המספר הנכון. הלולאה כוללת בקשות קלט מהמשתמש, בדיקת הניחוש שלו מול המספר המטרה, ומתן משוב (גבוה מדי או נמוך מדי).

### ייבוא מודול `random`

```python
import random
```

- `import random`: מייבא את המודול `random`, שמשמש ליצירת מספר אקראי.

### יצירת מספר אקראי

```python
targetNumber = random.randint(1, 100)
```

- `targetNumber = random.randint(1, 100)`: מייצר מספר שלם אקראי בטווח שבין 1 ל-100 (כולל) ומאחסן אותו במשתנה `targetNumber`.

### לולאה ראשית `while True:`

```python
while True:
    try:
        userGuess = int(input("Угадай число: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if userGuess == targetNumber:
        print("YOU GOT IT!")
        break
    elif userGuess < targetNumber:
        print("TOO LOW")
    else:
        print("TOO HIGH")
```

-   `while True:`: יוצר לולאה אינסופית שרצה עד שהשחקן מנחש נכון את המספר.
-   **טיפול בשגיאות קלט**
    -   `try...except ValueError`: הבלוק הזה נועד להתמודד עם שגיאות אפשריות שעלולות להתרחש כאשר המשתמש מזין קלט. אם המשתמש מזין קלט שאינו מספר שלם, הקוד ידפיס הודעת שגיאה וימשיך לאיטרציה הבאה של הלולאה.
    -  `userGuess = int(input("Угадай число: "))`: מבקש מהמשתמש להזין מספר וממיר אותו למספר שלם, תוך אחסונו במשתנה `userGuess`.
-   **בדיקת ניחוש**
    -   `if userGuess == targetNumber:`: בודק אם הניחוש של המשתמש שווה למספר המטרה.
        -   `print("YOU GOT IT!")`: אם הניחוש נכון, מדפיס הודעת ניצחון.
        -   `break`: יוצא מהלולאה, ובכך מסתיים המשחק.
    -   `elif userGuess < targetNumber:`: אם הניחוש של המשתמש קטן מהמספר המטרה.
        -   `print("TOO LOW")`: מדפיס הודעה המציינת שהניחוש נמוך מדי.
    -   `else:`: אם הניחוש לא נכון וגם לא נמוך מהמספר המטרה, הוא חייב להיות גדול מהמספר המטרה.
        -   `print("TOO HIGH")`: מדפיס הודעה המציינת שהניחוש גבוה מדי.