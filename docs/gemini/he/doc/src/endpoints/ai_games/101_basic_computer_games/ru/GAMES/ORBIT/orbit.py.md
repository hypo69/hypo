# ORBIT

## סקירה כללית

משחק "ORBIT" הוא משחק טקסט שבו השחקן שולט בחללית המסתובבת סביב כוכב לכת. מטרת המשחק היא להגדיר מהירות התחלתית וזווית התחלתית כך שהחללית תגיע למסלול יציב. המשחק משתמש בסימולציה של כוח המשיכה לחישוב מסלול החללית.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`simulate_orbit`](#simulate_orbit)
  - [`play_orbit_game`](#play_orbit_game)

## פונקציות

### `simulate_orbit`

**תיאור**:
מדמה את המסלול של חללית סביב כוכב לכת.

**פרמטרים**:
- `initial_velocity` (float): המהירות ההתחלתית של החללית.
- `initial_angle` (float): הזווית ההתחלתית של כיוון החללית במעלות.

**החזרות**:
- `bool`: `True` אם המסלול נוצר; `False` אחרת.

```python
def simulate_orbit(initial_velocity: float, initial_angle: float) -> bool:
    """
    Args:
        initial_velocity (float): Начальная скорость корабля.
        initial_angle (float): Начальный угол направления корабля в градусах.

    Returns:
         bool: True, если орбита установлена; False в противном случае.
    """
```

### `play_orbit_game`

**תיאור**:
מפעיל את משחק סימולציית המסלול.

**פרמטרים**:
אין

**החזרות**:
אין

```python
def play_orbit_game() -> None:
    """
    Args:

    Returns:
        
    """
```