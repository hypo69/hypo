# HURKLE

## סקירה כללית

המשחק "HURKLE" הוא משחק ניחושים בו השחקן מנסה למצוא את מיקום ה-"HURKLE" המוסתר על גבי מפה בגודל 10x10. השחקן מבצע ניחושים על ידי הזנת קואורדינטות, ומקבל רמזים על כיוון מיקומו של ה-"HURKLE" יחסית לניחושים. המטרה היא למצוא את ה-"HURKLE" במספר מינימלי של ניסיונות.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`get_direction`](#get_direction)

## פונקציות

### `get_direction`

**Description**:
   פונקציה המגדירה את הכיוון של ה-HURKLE מקואורדינטות המשתמש.

**Parameters**:
   - `user_x` (int): קואורדינטת X שהזין המשתמש.
   - `user_y` (int): קואורדינטת Y שהזין המשתמש.
   - `hurkle_x` (int): קואורדינטת X של ה-HURKLE.
   - `hurkle_y` (int): קואורדינטת Y של ה-HURKLE.

**Returns**:
   - `str`: מחזירה מחרוזת שמייצגת את הכיוון.

**Raises**:
   - אין

```python
def get_direction(user_x, user_y, hurkle_x, hurkle_y):
    """
    Args:
        user_x (int): קואורדינטת X שהזין המשתמש.
        user_y (int): קואורדינטת Y שהזין המשתמש.
        hurkle_x (int): קואורדינטת X של ה-HURKLE.
        hurkle_y (int): קואורדינטת Y של ה-HURKLE.

    Returns:
        str: מחזירה מחרוזת שמייצגת את הכיוון.
    """
    if user_x < hurkle_x and user_y < hurkle_y:
        return "СЕВЕРО-ВОСТОК"
    elif user_x < hurkle_x and user_y > hurkle_y:
        return "ЮГО-ВОСТОК"
    elif user_x > hurkle_x and user_y < hurkle_y:
        return "СЕВЕРО-ЗАПАД"
    elif user_x > hurkle_x and user_y > hurkle_y:
        return "ЮГО-ЗАПАД"
    elif user_x < hurkle_x:
        return "ВОСТОК"
    elif user_x > hurkle_x:
        return "ЗАПАД"
    elif user_y < hurkle_y:
        return "СЕВЕР"
    else:
        return "ЮГ"