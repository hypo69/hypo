# SPLAT

## Обзор

Этот файл содержит реализацию игры "SPLAT", в которой игрок пытается сбить самолет, стреляя из пушки. Игрок вводит угол и скорость выстрела, а игра имитирует траекторию снаряда. Если снаряд попадает в самолет, игрок выигрывает. В противном случае самолет улетает дальше.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [calculate_distance](#calculate_distance)
- [Переменные](#переменные)

## Функции

### `calculate_distance`

**Описание**:
Функция вычисляет расстояние, которое пролетит снаряд, исходя из заданных угла и начальной скорости.

**Параметры**:
- `angle` (float): Угол выстрела в градусах.
- `velocity` (float): Начальная скорость выстрела.

**Возвращает**:
- `float`: Расстояние, которое пролетит снаряд.

## Переменные

- `plane_position` (int): Начальное положение самолета (20).
- `game_status` (str): Состояние игры, изначально установлено в 'playing'.
```python
import math

# פונקציה לחישוב מרחק הפגז
def calculate_distance(angle, velocity):
    """
    פונקציה זו מחשבת את מרחק הפגז בהתבסס על זווית ומהירות ההתחלה.

    Args:
        angle: זווית השיגור במעלות.
        velocity: מהירות השיגור.

    Returns:
        float: מרחק הפגז.
    """
    # המרת הזווית מרדיאנים
    angle_rad = math.radians(angle)
    # חישוב המרחק האופקי של הפגז
    distance = (velocity ** 2 * math.sin(2 * angle_rad)) / 9.81
    return distance

# משתנה המייצג את מיקום המטוס
plane_position = 20
# מצב המשחק
game_status = 'playing'

# לולאת המשחק הראשית
while game_status == 'playing':
    # קבלת קלט מהמשתמש
    try:
        angle = float(input("הזן זווית (0-90): "))
        velocity = float(input("הזן מהירות (0-90): "))
        if not (0 <= angle <= 90) or not (0 <= velocity <= 90):
           print("הזווית והמהירות חייבות להיות בין 0 ל-90. נסה שוב.")
           continue
    except ValueError as ex:
        print("קלט לא תקין, אנא הזן מספרים.")
        continue

    # חישוב מרחק הפגז
    distance = calculate_distance(angle, velocity)

    # בדיקה אם הפגז פגע במטוס
    if abs(distance - plane_position) < 10:  # סף הפגיעה הוא 10 יחידות
        print("SPLAT!!! YOU GOT IT!")
        game_status = 'end' # סיום המשחק
    else:
        # בדיקה אם המטוס הגיע לקצה המסך
        if plane_position < 100:
            plane_position += 10 # הזזת המטוס ימינה
        else:
             print("YOU MISSED, PLANE FLEW AWAY")
             game_status = 'end' # סיום המשחק
```