# `mugwmp.py`

## סקירה כללית

קובץ זה מיישם את המשחק "MUGWMP", משחק ניחוש מספרים טקסטואלי. המחשב מייצר מספר בן ארבע ספרות, והשחקן מנסה לנחש אותו. לאחר כל ניחוש, השחקן מקבל רמזים בדמות כמות הספרות הנכונות במיקומן הנכון (MUG) וכמות הספרות הנכונות שאינן במיקומן הנכון (WMP).

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`generate_secret_number`](#generate_secret_number)
  - [`count_mug_wmp`](#count_mug_wmp)
- [קוד משחק](#קוד-משחק)
- [הסבר קוד](#הסבר-קוד)

## פונקציות

### `generate_secret_number`

**תיאור**: מייצר מספר אקראי בן ארבע ספרות עם ספרות ייחודיות.

**פרמטרים**:
- אין

**החזרות**:
- `str`: מספר אקראי בן ארבע ספרות עם ספרות ייחודיות.

### `count_mug_wmp`

**תיאור**: סופר את מספר ה-MUG (ספרות נכונות במקומות הנכונים) ואת מספר ה-WMP (ספרות נכונות במקומות הלא נכונים).

**פרמטרים**:
- `secret` (str): המספר הסודי.
- `guess` (str): ניחוש השחקן.

**החזרות**:
- `tuple`: טאפל המכיל את כמות ה-MUG ואת כמות ה-WMP.

## קוד משחק

```python
import random

def generate_secret_number():
    """
    Args:
        None
    Returns:
         str: מספר אקראי בן ארבע ספרות עם ספרות ייחודיות.
    """
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def count_mug_wmp(secret: str, guess: str) -> tuple:
    """
    Args:
         secret (str): המספר הסודי.
         guess (str): ניחוש השחקן.

    Returns:
         tuple: טאפל המכיל את כמות ה-MUG ואת כמות ה-WMP.
    """
    mug = 0
    wmp = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            mug += 1
        elif guess[i] in secret:
            wmp += 1
    return mug, wmp

# 1. Генерируем случайное четырехзначное число с уникальными цифрами
secret_number = generate_secret_number()

# 2. Инициализируем счетчик попыток
number_of_guesses = 0

# 3. Основной игровой цикл
while True:
    # 3.1. Увеличиваем счетчик попыток
    number_of_guesses += 1

    # 3.2. Запрашиваем ввод числа у пользователя
    while True:
        user_guess = input("Введите четырехзначное число с уникальными цифрами: ")

        # 3.3. Проверяем корректность ввода
        if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:
            print("Ошибка ввода. Пожалуйста, введите корректное четырехзначное число с уникальными цифрами.")
        else:
            break

    # 3.4. Проверяем, угадано ли число
    if user_guess == secret_number:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {number_of_guesses} попыток!")
        break  # Завершаем цикл, если число угадано

    # 3.5. Подсчитываем MUG и WMP
    mug, wmp = count_mug_wmp(secret_number, user_guess)

    # 3.6. Выводим подсказку
    print(f"MUG = {mug}, WMP = {wmp}")

```

## הסבר קוד

1.  **ייבוא מודול `random`**:
    - `import random`: מייבא את המודול `random`, המשמש ליצירת מספר אקראי.

2.  **פונקציה `generate_secret_number()`**:
    - `def generate_secret_number():`: מגדירה פונקציה ליצירת מספר סודי בן ארבע ספרות עם ספרות ייחודיות.
    - `digits = list(range(10))`: יוצרת רשימה של ספרות מ-0 עד 9.
    - `random.shuffle(digits)`: מערבבת את הספרות באופן אקראי.
    - `return "".join(map(str, digits[:4]))`: מחזירה מחרוזת של ארבע הספרות המעורבבות הראשונות, ויוצרת מספר בן ארבע ספרות.

3.  **פונקציה `count_mug_wmp(secret, guess)`**:
    - `def count_mug_wmp(secret, guess):`: מגדירה פונקציה לחישוב MUG ו-WMP.
    - `mug = 0`, `wmp = 0`: מאתחלת את מוני ה-MUG וה-WMP.
    - `for i in range(len(secret)):`: עוברת על הספרות של המספר הסודי.
        - `if secret[i] == guess[i]:`: אם הספרה במיקום הנוכחי תואמת, מגדילה את מונה ה-MUG.
        - `elif guess[i] in secret:`: אם הספרה מהניחוש קיימת במספר הסודי, אבל לא במיקום הנכון, מגדילה את מונה ה-WMP.
    - `return mug, wmp`: מחזירה טאפל עם ערכי ה-MUG וה-WMP.

4.  **חלק עיקרי של התוכנית**:
    - `secret_number = generate_secret_number()`: מייצרת מספר סודי באמצעות הפונקציה `generate_secret_number()`.
    - `number_of_guesses = 0`: מאתחלת את מונה הניחושים.
    - `while True:`: מתחילה לולאה אינסופית עד שהשחקן מנחש את המספר.
        - `number_of_guesses += 1`: מגדילה את מונה הניחושים.
        - `while True:`: לולאה פנימית לבדיקת קלט מהמשתמש.
            - `user_guess = input("Введите четырехзначное число с уникальными цифрами: ")`: מבקשת קלט מהמשתמש.
            - `if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:`: בודקת אם הקלט תקין (ארבע ספרות, כולן ייחודיות).
            - `else: break`: אם הקלט תקין, יוצאת מהלולאה הפנימית.
        - `if user_guess == secret_number:`: בודקת אם המספר נוחש.
            - `print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {number_of_guesses} попыток!")`: מציגה הודעת ניצחון.
            - `break`: יוצאת מהלולאה הראשית.
        - `mug, wmp = count_mug_wmp(secret_number, user_guess)`: קוראת לפונקציה `count_mug_wmp` כדי לחשב את ה-MUG וה-WMP.
        - `print(f"MUG = {mug}, WMP = {wmp}")`: מציגה את הרמזים של ה-MUG וה-WMP.