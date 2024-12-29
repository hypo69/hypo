# orbit.py

## Обзор

Этот модуль реализует игру "Orbit", симулирующую движение ракеты в гравитационном поле звезды. Игрок задает начальную скорость и угол запуска, а программа моделирует траекторию ракеты, проверяя, не упадет ли она на звезду, не улетит ли слишком далеко или не выйдет ли на стабильную орбиту.

## Содержание

- [Функции](#Функции)
  - [`play_orbit_game`](#play_orbit_game)

## Функции

### `play_orbit_game`

**Описание**:
Запускает игру "Orbit", в которой игрок пытается вывести ракету на стабильную орбиту вокруг звезды.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `None`: Функция не возвращает значения явно, но печатает сообщения о результатах игры (`CRASH`, `OUT OF RANGE`, `ORBIT ESTABLISHED` или сообщение об отсутствии стабильной орбиты).

**Вызывает исключения**:
- `ValueError`: Возникает, если пользователь вводит некорректные данные (не числа) при запросе угла запуска или начальной скорости.

```python
def play_orbit_game():
    """
    Args:
        None

    Returns:
        None: Функция не возвращает значения явно, но печатает сообщения о результатах игры (`CRASH`, `OUT OF RANGE`, `ORBIT ESTABLISHED` или сообщение об отсутствии стабильной орбиты).

    Raises:
        ValueError: Возникает, если пользователь вводит некорректные данные (не числа) при запросе угла запуска или начальной скорости.
    """
    # קבועים
    initial_distance = 200  # מרחק התחלתי מהשמש
    gravitational_constant = 10000 # קבוע כוח הכבידה
    initial_radial_velocity = 0  # מהירות רדיאלית ראשונית
    min_crash_distance = 50  # מרחק מינימלי להתרסקות
    max_escape_distance = 400 # מרחק מקסימלי לבריחה

    # קלט מהמשתמש
    try:
        launch_angle_degrees = float(input("הזן זווית שיגור במעלות (0-90): "))
        initial_velocity = float(input("הזן מהירות התחלתית: "))
    except ValueError as ex:
        print("קלט לא תקין. אנא הזן מספרים.")
        return

    # המרת זווית מרדיאנים למעלות
    launch_angle_radians = math.radians(launch_angle_degrees)

    # מיקום התחלתי
    x = initial_distance
    y = 0

    # מהירות התחלתית
    vx = initial_velocity * math.cos(launch_angle_radians)
    vy = initial_velocity * math.sin(launch_angle_radians)

    # סימולציה
    for _ in range(1000): # במקור, הייתה לולאת FOR עם 1000 איטרציות
        # חישוב מרחק מהשמש
        r = math.sqrt(x**2 + y**2)

        # בדיקה אם הטיל התרסק או ברח
        if r < min_crash_distance:
            print("CRASH")
            return
        if r > max_escape_distance:
            print("OUT OF RANGE")
            return

        # חישוב תאוצת כוח הכבידה
        ag = -gravitational_constant / r**2

        # עדכון מהירויות (רדיאלית וטנגנציאלית)
        vr = initial_radial_velocity + ag * (x / r)
        vt = initial_velocity + ag * (y / r)

        # עדכון מהירויות קרטזיות
        vx = vt * (y / r)
        vy = vt * (x / r)


        # עדכון מיקום
        x = x + vx
        y = y + vy

        # חישוב מהירות כוללת
        v = math.sqrt(vx**2 + vy**2)

        # חישוב פרמטר מסלול יציב
        k = (v**2 * r) / gravitational_constant

        # בדיקה אם המסלול יציב
        if 0.99 < k < 1.01:
             print("ORBIT ESTABLISHED")
             return

    print("לא נוצר מסלול יציב.")