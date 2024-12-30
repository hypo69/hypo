# bullcow.py

## סקירה כללית

קובץ זה מיישם את המשחק "שור פר" (Bull and Cow), משחק ניחושים בו שחקן מנסה לנחש מספר סודי בן 4 ספרות. המשחק מספק רמזים בדמות "שוורים" (ספרות במקום הנכון) ו"פרות" (ספרות נכונות אבל לא במקום הנכון).

## תוכן עניינים

- [פונקציות](#פונקציות)
    - [`generate_target_number`](#generate_target_number)
- [משתנים](#משתנים)
- [לולאת המשחק](#לולאת-המשחק)

## פונקציות

### `generate_target_number`

**תיאור**:
מייצר מספר בן 4 ספרות עם ספרות ייחודיות באופן אקראי.

**Returns**:
- `int`: מספר בן 4 ספרות עם ספרות ייחודיות.

## משתנים

- `targetNumber`: המספר הסודי שנוצר על ידי הפונקציה `generate_target_number` שהשחקן צריך לנחש.
- `numberOfGuesses`: מונה את מספר הניסיונות של השחקן לנחש את המספר.

## לולאת המשחק

הלולאה הראשית של המשחק ממשיכה עד שהשחקן מנחש את המספר בצורה נכונה.

1. **קבלת קלט מהמשתמש**:
    - מבקשת מהמשתמש להזין ניחוש בן 4 ספרות.
    - מטפלת בשגיאות קלט, כמו קלט שאינו מספר או קלט שאינו בן 4 ספרות, ומבקשת מהמשתמש להזין מספר חוקי.

2. **השוואת הניחוש עם המספר הסודי**:
    - מחשבת את מספר ה"שוורים" (ספרות נכונות במקומן הנכון) ואת מספר ה"פרות" (ספרות נכונות, אך במקומות שגויים).

3. **מתן משוב**:
    - מציגה את מספר ה"שוורים" וה"פרות" למשתמש.

4. **בדיקת תנאי זכייה**:
    - אם מספר ה"שוורים" שווה ל-4, מציגה הודעת ניצחון ואת מספר הניסיונות שהיו נחוצים.

```python
def generate_target_number() -> int:
    """
    Args:
        None

    Returns:
        int: מייצר מספר בן 4 ספרות עם ספרות ייחודיות באופן אקראי.
    """
    digits = list(range(10))
    random.shuffle(digits)
    target = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
    if digits[0] == 0:
        return generate_target_number()
    return target


targetNumber = generate_target_number()
numberOfGuesses = 0

while True:
    numberOfGuesses += 1
    try:
        userGuess = int(input("Введите 4-значное число: "))
    except ValueError:
        print("Пожалуйста, введите целое 4-значное число.")
        continue

    if not (1000 <= userGuess <= 9999):
        print("Пожалуйста, введите 4-значное число.")
        continue

    bulls = 0
    cows = 0
    
    target_str = str(targetNumber)
    guess_str = str(userGuess)

    for i in range(4):
        if guess_str[i] == target_str[i]:
            bulls += 1
        elif guess_str[i] in target_str:
            cows += 1
            
    print(f"{bulls} быков, {cows} коров")

    if bulls == 4:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")
        break