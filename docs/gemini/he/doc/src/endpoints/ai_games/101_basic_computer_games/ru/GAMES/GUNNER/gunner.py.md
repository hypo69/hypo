# GUNNER

## סקירה כללית

משחק "GUNNER" הוא סימולציה של ירי למטרה. השחקן מזין את זווית הירי ואת מהירותו, והמחשב מחשב האם הפגז יפגע במטרה. לשחקן יש 5 ניסיונות, ולאחר כל ניסיון, הוא מקבל רמז:
- "TOO LOW" - אם הפגז לא הגיע למטרה.
- "TOO HIGH" - אם הפגז עבר את המטרה.
- "BINGO" - אם הפגז פגע במטרה.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [משתנים גלובליים](#משתנים-גלובליים)
3. [לולאה ראשית](#לולאה-ראשית)
4. [הסבר קוד](#הסבר-קוד)

## משתנים גלובליים

- `attemptsLeft`: מספר הניסיונות שנותרו לשחקן.
- `targetDistance`: המרחק האקראי למטרה.

## לולאה ראשית
הלולאה הראשית של המשחק מבוצעת כל עוד לשחקן יש ניסיונות:
1. קולט את זווית ומהירות הירי מהשחקן.
2. בודק שהזווית נמצאת בטווח המותר (0-90).
3. מחשב את מרחק הפגז.
4. בודק האם הפגז פגע, עבר או לא הגיע למטרה, ומדפיס את ההודעה המתאימה.
5. מפחית את כמות הניסיונות שנותרו.
בסוף, בודק אם נגמרו הניסיונות, ובמידה וכן, מדפיס הודעת הפסד.

## הסבר קוד
### פונקציות

#### `main`
**Description**: הפונקציה הראשית שמבצעת את המשחק.

**Parameters**:
- אין פרמטרים.

**Returns**:
- אין ערך מוחזר.

**Raises**:
- `ValueError`: אם הקלט של המשתמש אינו מספר.
```python
import random
import math

# Инициализация количества попыток
attemptsLeft = 5
# Генерация случайного расстояния до цели от 100 до 1000 футов
targetDistance = random.randint(100, 1000)

# Основной игровой цикл
while attemptsLeft > 0:
    # Запрашиваем ввод угла и скорости выстрела
    try:
        angle = float(input("Введите угол выстрела в градусах (0-90): "))
        speed = float(input("Введите скорость выстрела в футах в секунду: "))
    except ValueError as ex:
        print("Пожалуйста, введите числовые значения.")
        continue

    # Проверка ввода угла
    if not (0 <= angle <= 90):
        print("Угол должен быть в диапазоне от 0 до 90 градусов.")
        continue

    # Расчет дальности полета снаряда
    # Перевод угла в радианы
    angle_radians = math.radians(angle)
    distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2

    # Проверка попадания
    if abs(distance - targetDistance) < 0.01: # Используем небольшую погрешность для сравнения
        print("BINGO!")
        break  # Завершаем игру при попадании в цель
    elif distance < targetDistance:
        print("TOO LOW") # Сообщаем, что снаряд не долетел
    else:
        print("TOO HIGH") # Сообщаем, что снаряд перелетел

    # Уменьшаем количество оставшихся попыток
    attemptsLeft -= 1

# Вывод сообщения о проигрыше, если попытки закончились
if attemptsLeft == 0:
    print("YOU LOSE")
```
### הסבר נוסף

1.  **ייבוא מודולים**:
    *   `import random`: מייבא את המודול `random`, שמשמש ליצירת מרחק אקראי למטרה.
    *   `import math`: מייבא את המודול `math`, שמשמש לחישובים מתמטיים (סינוס והמרת מעלות לרדיאנים).

2.  **אתחול משתנים**:
    *   `attemptsLeft = 5`: מאתחל את המשתנה `attemptsLeft` כדי לעקוב אחר מספר הניסיונות שנותרו, ומתחיל ב-5.
    *   `targetDistance = random.randint(100, 1000)`: יוצר מספר שלם אקראי בין 100 ל-1000, שמייצג את המרחק למטרה, ושומר אותו ב-`targetDistance`.

3.  **לולאת משחק ראשית `while attemptsLeft > 0:`**:
    *   הלולאה מתבצעת כל עוד לשחקן נותרו ניסיונות.

4.  **קלט נתונים**:
    *   `try...except ValueError`: בלוק `try-except` מטפל בשגיאות קלט אפשריות. אם המשתמש מכניס קלט שאינו מספרי, תוצג הודעת שגיאה.
    *   `angle = float(input("Введите угол выстрела в градусах (0-90): "))`: מבקש מהמשתמש להזין את זווית הירי וממיר אותה למספר נקודה צפה.
    *   `speed = float(input("Введите скорость выстрела в футах в секунду: "))`: מבקש מהמשתמש להזין את מהירות הירי וממיר אותה למספר נקודה צפה.

5.  **בדיקת קלט זווית**:
    *   `if not (0 <= angle <= 90):`: בודק האם הזווית שהוכנסה נמצאת בטווח המותר (מ-0 עד 90 מעלות).
    *   `print("Угол должен быть в диапазоне от 0 до 90 градусов.")`: מדפיס הודעת שגיאה אם הזווית שהוכנסה שגויה.
    *   `continue`: מעביר לאיטרציה הבאה בלולאה, מבלי להמשיך עם הקוד באיטרציה הנוכחית.

6.  **חישוב מרחק טיסה**:
    *   `angle_radians = math.radians(angle)`: ממיר את הזווית ממעלות לרדיאנים, מפני שהפונקציה `math.sin()` מצפה לרדיאנים.
    *   `distance = (speed**2 * math.sin(2 * angle_radians)) / 32.2`: מחשב את מרחק הטיסה של הפגז על פי הנוסחה הנתונה.

7.  **בדיקת פגיעה**:
    *   `if abs(distance - targetDistance) < 0.01:`: בודק האם הפגז פגע במטרה. משתמש ב-`abs()` כדי לקבל את הערך המוחלט של ההפרש, וסובלנות קטנה (0.01) לצורך השוואת מספרי נקודה צפה בגלל אי דיוקים בייצוג.
    *   `print("BINGO!")`: מדפיס הודעה שהפגיעה הצליחה.
    *   `break`: מסיים את הלולאה (המשחק) במקרה של פגיעה.
    *   `elif distance < targetDistance:`: בודק אם הפגז לא הגיע למטרה.
    *   `print("TOO LOW")`: מדפיס הודעה שהפגז לא הגיע.
    *   `else:`: אם הפגז עבר את המטרה.
    *   `print("TOO HIGH")`: מדפיס הודעה שהפגז עבר את המטרה.

8.  **הפחתת מספר הניסיונות**:
    *   `attemptsLeft -= 1`: מפחית את מספר הניסיונות שנותרו ב-1.

9.  **הדפסת הודעת הפסד**:
    *   `if attemptsLeft == 0:`: בודק אם נגמרו הניסיונות.
    *   `print("YOU LOSE")`: מדפיס הודעת הפסד.