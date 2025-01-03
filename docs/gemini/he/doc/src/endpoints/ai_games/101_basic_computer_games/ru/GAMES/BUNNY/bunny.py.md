# BUNNY

## סקירה כללית

המשחק "BUNNY" הוא משחק טקסט בו השחקן מנסה למצוא ארנב שחבוי באחד מעשרה מקומות.
השחקן בוחר מספר מקום, והמשחק מודיע האם הארנב נמצא באותו מקום. המשחק נמשך עד שהארנב נמצא.

## תוכן עניינים
- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
- [הסבר קוד](#הסבר-קוד)

## פונקציות

### `__main__`

**תיאור**: קוד המשחק הראשי.
   
**פרמטרים**: אין.
   
**החזרות**: אין.
   
**חריגות**: 
- `ValueError`:  מועלית כאשר המשתמש מזין קלט שאינו מספר שלם.

## הסבר קוד

1.  **ייבוא מודול `random`**:
    -   `import random`: מייבא את המודול `random`, שמשמש ליצירת מספר אקראי המייצג את המקום שבו הארנב מוסתר.
2.  **אתחול מיקום הארנב**:
    -   `bunnyLocation = random.randint(1, 10)`: מייצר מספר שלם אקראי בטווח שבין 1 ל-10 ושומר אותו במשתנה `bunnyLocation`. מספר זה מייצג את המקום שבו מוסתר הארנב.
3.  **לולאה ראשית `while True:`**:
    -   הלולאה הזו תרוץ עד שהארנב יימצא (כלומר, עד שהפקודה `break` תופעל).
    -   **קבלת קלט של מיקום**:
        -   `try...except ValueError`: בלוק ה-try-except מטפל בשגיאות קלט אפשריות. אם המשתמש מזין ערך שאינו מספר שלם, תוצג הודעת שגיאה.
        -   `userLocation = int(input("Где кролик (1-10)? "))`: מבקש מהמשתמש להזין מספר מקום שבו, לדעתו, הארנב מוסתר, וממיר את הקלט למספר שלם.
    -   **בדיקת מיקום**:
        -   `if userLocation == bunnyLocation`: בודק האם מספר המקום שהוזן תואם את מיקום הארנב.
        -   `print("You found him!")`: אם המקומות תואמים, מדפיס הודעה שהארנב נמצא.
        -   `break`: מסיים את הלולאה הראשית של המשחק.
        -   `else:`: אם המקומות לא תואמים.
        -  `print("He's not there.")`: מדפיס הודעה שהארנב לא נמצא במקום שנבחר.