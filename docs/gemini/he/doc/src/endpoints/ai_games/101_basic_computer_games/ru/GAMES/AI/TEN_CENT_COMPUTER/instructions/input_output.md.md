# מנוע משחקי Input-Output

## סקירה כללית

קובץ זה מתאר מנוע משחק המיועד למשחק מתמטי "קלט-פלט". המנוע אחראי על המרת מספר קלט בהתאם לכלל מוגדר מראש (המכונה "מכונה") ומתן הפלט כתוצאה. המנוע יתחיל עם כללים פשוטים ובהדרגה יעבור לכללים מורכבים יותר, תוך מתן אפשרות למשתמש לציין כלל ספציפי.

## תוכן עניינים
- [סקירה כללית](#סקירה-כללית)
- [פורמט קלט/פלט](#פורמט-קלטפלט)
- [דוגמאות](#דוגמאות)
- [מכונות](#מכונות)

## פורמט קלט/פלט

### **קלט מהמשתמש:**
- `Ввод: <число>`

### **פלט מהמערכת:**
- `Вывод: <результат>, машина:<описание операции>`

## דוגמאות

### דוגמאות קלט ופלט:
- משתמש: `Ввод: 5`
- מערכת: `Вывод: 8, машина +3`
- משתמש: `Ввод: 10`
- מערכת: `Вывод: 21, машина 2x+1`
- משתמש: `Ввод: 9`
- מערכת: `Вывод: 3, машина квадратный корень`
- משתמש: `Задайте машину x * 2`
- מערכת: `Окей, машина: x*2`

## מכונות
### תיאור המכונות
- המכונות מתחילות עם כללים פשוטים (חיבור או חיסור עם מספר שלם).
- ככל שהמשתמש מצליח, המכונות עוברות בהדרגה לכללים מורכבים יותר (כפל, חילוק, שורש, שילוב פעולות וכו').
- אם המשתמש מבקש כלל ספציפי, המכונה תשתמש בו.

### קוד פייטון
```python
def game_logic(input_value: int | float, machine: str) -> tuple[int | float, str]:
    """
    Args:
        input_value (int | float): הערך שמתקבל כקלט.
        machine (str): תיאור הפעולה שיש לבצע.

    Returns:
        tuple[int | float, str]: הערך המוחזר והפעולה שבוצעה.

    Raises:
        ValueError: אם הפעולה אינה מוכרת או אם יש בעיה בחישוב.
    """
    try:
        if machine == "+3":
            result = input_value + 3
        elif machine == "2x+1":
            result = input_value * 2 + 1
        elif machine == "квадратный корень":
            result = input_value ** 0.5
        elif machine == "x*2":
            result = input_value * 2
        else:
            raise ValueError("Неизвестная машина")

        return result, f"машина {machine}"

    except ValueError as ex:
         raise ValueError(f"Ошибка при обработке: {ex}")

```
### `game_logic`
**Description**: פונקציה זו מבצעת את ההיגיון של המשחק. בהינתן ערך קלט ומכונה, היא מחשבת את ערך הפלט בהתאם לכלל המוגדר, ומחזירה את התוצאה ואת תיאור הפעולה.

**Parameters**:
- `input_value` (int | float): הערך שמתקבל כקלט.
- `machine` (str): תיאור הפעולה שיש לבצע.

**Returns**:
- `tuple[int | float, str]`: הערך המוחזר והפעולה שבוצעה.

**Raises**:
- `ValueError`: אם הפעולה אינה מוכרת או אם יש בעיה בחישוב.