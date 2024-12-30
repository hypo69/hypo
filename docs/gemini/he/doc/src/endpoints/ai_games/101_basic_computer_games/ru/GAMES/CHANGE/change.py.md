# change.py

## סקירה כללית

קובץ זה מיישם משחק חיפוש בשם "HURKLE", בו השחקן מנסה למצוא את המחשב ש"מסתתר" במיקום אקראי על רשת 10x10. השחקן מקבל רמזים לגבי הכיוון (צפון, דרום, מזרח, מערב) והמרחק ל-HURKLE לאחר כל ניסיון. המשחק מסתיים כאשר השחקן מוצא את ה-HURKLE.

## תוכן עניינים

1. [פונקציות](#פונקציות)
    *   [המשחק](#המשחק)

## פונקציות

### `המשחק`

**Description**:
פונקציה זו מכילה את הלוגיקה הראשית של המשחק "HURKLE". היא מאתחלת את מיקום ה-HURKLE, מבקשת מהשחקן לנחש מיקום, מספקת רמזים על כיוון ומרחק, ומסיימת את המשחק כאשר ה-HURKLE נמצא.

**Parameters**:
אין פרמטרים.

**Returns**:
אין ערך מוחזר.

**Raises**:
- `ValueError`: מורם כאשר השחקן מכניס קלט שאינו מספר שלם.
```python
import random
import math

# 1. Инициализация координат Хёркла случайными целыми числами от 1 до 10
hurkleX = random.randint(1, 10)
hurkleY = random.randint(1, 10)

# 2. Основной игровой цикл (пока Хёркл не найден)
while True:
    # 2.1 Запрос у игрока координат его попытки
    try:
        userX = int(input("Введите X координату (от 1 до 10): "))
        userY = int(input("Введите Y координату (от 1 до 10): "))
    except ValueError as ex:
        print("Пожалуйста, введите целые числа.")
        continue

    # Проверка ввода координат
    if not (1 <= userX <= 10 and 1 <= userY <= 10):
            print("Координаты должны быть в диапазоне от 1 до 10.")
            continue
    # 2.2 Проверка, угадал ли игрок позицию Хёркла
    if userX == hurkleX and userY == hurkleY:
        print("YOU FOUND HIM!")
        break  # Завершение игры, если Хёркл найден

    # 2.3 Вычисление расстояния между позицией игрока и позицией Хёркла
    distanceX = userX - hurkleX
    distanceY = userY - hurkleY
    distance = math.sqrt(distanceX**2 + distanceY**2)

    # 2.4 Определение направления до Хёркла (комбинация N, S, E, W)
    direction = ""
    if distanceY > 0:
        direction += "N"
    if distanceY < 0:
        direction += "S"
    if distanceX > 0:
        direction += "E"
    if distanceX < 0:
        direction += "W"

    # 2.5 Вывод подсказки (направление и расстояние) до Хёркла
    print(f"{direction if direction else 'Здесь'}, расстояние: {distance:.2f}")