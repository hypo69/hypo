# FOOTBL

## סקירה כללית

משחק "כדורגל" הוא משחק טקסט שבו שני שחקנים מתחלפים בהזנת מספרים המייצגים ניסיונות בעיטה לשער. המשחק נמשך עד שמוכנס שער. מטרת המשחק היא להבקיע שער נגד היריב.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)

## פונקציות

### `game_loop`

**Description**: לולאת המשחק הראשית. מטפלת בתורות השחקנים, קלט המשתמש ובדיקת שער.

**Parameters**:
- אין פרמטרים

**Returns**:
- אין ערך מוחזר

**Raises**:
- אין חריגות ידועות

```python
currentPlayer = 1

while True:
    print(f"PLAYER {currentPlayer} --- YOUR SHOT")
    
    try:
        shot = int(input("Введите число от 1 до 10: "))
    except ValueError as ex:
        print("Пожалуйста, введите целое число.")
        continue
        
    if shot != 1:
        print(f"GOAL!!! PLAYER {currentPlayer} WINS!!!")
        break
    
    currentPlayer = 3 - currentPlayer
```
**Description**:
   -   `currentPlayer = 1`: מגדיר את הערך ההתחלתי של משתנה `currentPlayer` ל-1, כלומר השחקן הראשון מתחיל את המשחק.
   -   `while True:`: לולאה אינסופית שרצה עד שאחד השחקנים מבקיע שער (הפקודה `break` מופעלת).
   -   `print(f"PLAYER {currentPlayer} --- YOUR SHOT")`: מדפיס הודעה שמציינת את תור השחקן הנוכחי.
    -  `try...except ValueError`: בלוק try-except לטיפול בשגיאות אפשריות. אם המשתמש מזין לא מספר שלם, הודעת שגיאה תודפס.
    - `shot = int(input("Введите число от 1 до 10: "))`: מבקש מהשחקן הנוכחי להזין מספר וממיר את הקלט למספר שלם. המספר מייצג ניסיון בעיטה.
   -   `if shot != 1:`: בודק אם המספר שהוזן לא שווה ל-1. אם לא, זה נחשב שער.
   -   `print(f"GOAL!!! PLAYER {currentPlayer} WINS!!!")`: מדפיס הודעה שהשחקן הבקיע שער וניצח במשחק.
   -   `break`: מסיים את הלולאה ואת המשחק.
   -   `currentPlayer = 3 - currentPlayer`: מחליף את השחקן הנוכחי ליריב. אם `currentPlayer` היה 1, הוא הופך ל-2, ולהיפך.
```