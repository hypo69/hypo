# synonm.py

## סקירה כללית

קובץ זה מיישם משחק "ארטילריה" בו השחקן מנסה לפגוע במטרה הנמצאת במרחק מסוים על ידי ירי מתותח בזווית נתונה ובמהירות התחלתית נתונה. המשחק מתחשב בכוח המשיכה.

## תוכן עניינים

- [פונקציות](#functions)

## פונקציות

### `main`

**Description**: זוהי הפונקציה הראשית של המשחק "ארטילריה". היא מנהלת את לוגיקת המשחק, כולל קבלת קלט מהמשתמש, חישוב מרחק הפגז ובדיקה אם הפגז פגע במטרה.

**Parameters**:
אין פרמטרים.

**Returns**:
אין ערך מוחזר.

**Raises**:
אין חריגות ספציפיות.
```
import random
import math

# Инициализация параметров игры
maxAttempts = 10  # Максимальное количество попыток
gravity = 32.2  # Гравитация
targetDistance = random.randint(100, 1000)  # Случайное расстояние до цели
attempt = 0  # Счетчик попыток
accuracy = 0.1  # Погрешность в 10%

print(f"Расстояние до цели: {targetDistance}")

# Основной игровой цикл
while attempt < maxAttempts:
    attempt += 1
    print(f"Попытка {attempt} из {maxAttempts}")

    # Запрашиваем ввод данных у пользователя
    while True:
        try:
            angle = float(input("Введите угол выстрела (в градусах): "))
            initialSpeed = float(input("Введите начальную скорость: "))
            break
        except ValueError as ex:
             print("Пожалуйста, введите числовое значение")


    # Преобразуем угол в радианы
    angle = math.radians(angle)

    # Вычисляем дальность полета
    distance = (initialSpeed ** 2 * math.sin(2 * angle)) / gravity

    # Проверяем, попал ли снаряд в цель
    if targetDistance * (1- accuracy) <= distance <= targetDistance * (1 + accuracy):
        print("ВЫ ПОПАЛИ В ЦЕЛЬ!")
        break
    elif distance < targetDistance:
        print("Слишком коротко!")
    else:
        print("Слишком далеко!")

# Выводим сообщение о поражении, если все попытки исчерпаны
if attempt == maxAttempts:
    print("Вы проиграли!")