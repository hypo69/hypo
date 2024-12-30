# FURS

## סקירה כללית

המשחק "FURS" הוא משחק טקסטואלי בו המחשב מייצר טקסט אקראי המורכב ממילים ומספרים אקראיים. השחקן מנסה לנחש אילו מילים ומספרים אקראיים נוצרו. המשחק ממשיך עד שהשחקן מנחש את כל המילים והמספרים שנוצרו.

## תוכן עניינים

1.  [סקירה כללית](#סקירה-כללית)
2.  [פונקציות](#פונקציות)

## פונקציות

### `main`

**Description**:
פונקציה זו מתחילה משחק ניחושים בו השחקן צריך לנחש 4 מילים ו-4 ספרות אקראיות.

**Parameters**:
- אין פרמטרים

**Returns**:
- אין ערך מוחזר

**Raises**:
- ValueError: נזרק כאשר קלט המשתמש אינו מספר.

```python
import random

# רשימת המילים האפשריות
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# רשימה ריקה לאחסון המילים הנבחרות
chosenWords = []
# רשימה ריקה לאחסון הספרות הנבחרות
chosenDigits = []

# בוחר 4 מילים אקראיות מהרשימה
chosenWords = random.sample(words, 4)
# בוחר 4 ספרות אקראיות בין 0 ל-9
chosenDigits = [random.randint(0, 9) for _ in range(4)]

# לולאה ראשית של המשחק
while True:
    # קבלת קלט משתמש
    user_input = input("הכנס 4 מילים (A-J) ו-4 ספרות (0-9) מופרדות ברווח: ").upper()
    # חלוקת הקלט למילים וספרות
    userWords = user_input.split()[:4]
    userDigits = user_input.split()[4:]

    # דגל לבדוק אם כל המילים והספרות נכונות
    all_correct = True

    # בדיקת מילים
    for i in range(4):
        if userWords[i] == chosenWords[i]:
            print(f"המילה {userWords[i]} במיקום {i+1} נכונה")
        else:
            all_correct = False
    # בדיקת ספרות
    for i in range(4):
        try:
          if int(userDigits[i]) == chosenDigits[i]:
              print(f"הספרה {userDigits[i]} במיקום {i+1} נכונה")
          else:
            all_correct = False
        except ValueError as ex:
          print(f"שגיאה: '{userDigits[i]}' אינו מספר. נסה שוב.")
          all_correct = False
          break
    # אם כל המילים והספרות נכונות - המשחק מסתיים
    if all_correct:
        print("ניצחת!")
        break