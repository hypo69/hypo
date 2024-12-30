# מודול `can_am`

## סקירה כללית

מודול זה מדמה משחק מירוץ בו השחקן שולט במכונית וצריך להגיע לקו הסיום על ידי חישוב נכון של ההאצה.

## תוכן עניינים

1.  [סקירה כללית](#סקירה-כללית)
2.  [פונקציות](#פונקציות)

## פונקציות

### `main`

**Description**: פונקציה שמדמה את משחק המירוץ.

**Parameters**:
- אין פרמטרים לפונקציה זו.

**Returns**:
- אין ערך החזרה.

**Raises**:
- אין חריגות.
```python
def main():
    """
    Args:
        None
    Returns:
        None
    Raises:
        None
    """
```
```python
import time

# Инициализация переменных
position = 0 # Начальная позиция автомобиля
speed = 0    # Начальная скорость автомобиля
trackLength = 200 # Длина трассы

print("Игра CAN AM началась!")
time.sleep(1)  # Задержка 1 секунду
# Основной игровой цикл
while True:
    print(f"Текущая позиция: {position}, текущая скорость: {speed}")
    # Запрашиваем у пользователя ввод ускорения
    try:
        acceleration = int(input("Введите ускорение (0-9): "))
    except ValueError ex:
        print("Пожалуйста, введите целое число от 0 до 9.")
        continue
    
    if acceleration < 0 or acceleration > 9:
      print("Ускорение должно быть в диапазоне от 0 до 9.")
      continue

    # Обновляем скорость
    speed += acceleration
    # Обновляем позицию
    position += speed

    # Проверяем, не вылетела ли машина с трассы
    if position < 0 or position > trackLength:
        print("CRASH! Вы вылетели с трассы!")
        break # Завершаем игру
    # Проверяем, не достигли ли финиша
    if position >= trackLength:
        print("WINNER! Вы достигли финиша!")
        break # Завершаем игру
    time.sleep(1) # Задержка 1 секунду
```