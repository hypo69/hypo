# מודול ממיר טמפרטורה

## סקירה כללית

מודול זה מספק שני יישומי מחשבון טמפרטורה המאפשרים המרה בין מעלות צלזיוס, פרנהייט וקלווין.

## תוכן עניינים

1.  [סקירה כללית](#סקירה-כללית)
2.  [קובץ `convertor_kcf.py`](#קובץ-convertor_kcfpy)
    *   [פונקציות המרה](#פונקציות-המרה)
    *   [פונקציית המרה אוניברסלית](#פונקציית-המרה-אוניברסלית)
    *   [פונקציית `main`](#פונקציית-main)
3.  [קובץ `convertor_kcf_dataclass.py`](#קובץ-convertor_kcf_dataclasspy)
    *   [מחלקת `TemperatureConverter`](#מחלקת-temperatureconverter)
    *   [פונקציית `convert_temperature`](#פונקציית-convert_temperature)
    *   [פונקציית `main`](#פונקציית-main-1)
4.  [השוואה בין שתי הגישות](#השוואה-בין-שתי-הגישות)
5.  [הרצת הקוד](#הרצת-הקוד)

## קובץ `convertor_kcf.py`

קובץ זה מכיל יישום של מחשבון טמפרטורה באמצעות פונקציות נפרדות.

### פונקציות המרה

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    ממירה טמפרטורה ממעלות צלזיוס למעלות פרנהייט.

    Args:
        celsius (float): טמפרטורה במעלות צלזיוס.

    Returns:
        float: טמפרטורה במעלות פרנהייט.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    ממירה טמפרטורה ממעלות פרנהייט למעלות צלזיוס.

    Args:
        fahrenheit (float): טמפרטורה במעלות פרנהייט.

    Returns:
        float: טמפרטורה במעלות צלזיוס.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """
    ממירה טמפרטורה ממעלות צלזיוס לקלווין.

    Args:
        celsius (float): טמפרטורה במעלות צלזיוס.

    Returns:
        float: טמפרטורה בקלווין.
    """
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """
    ממירה טמפרטורה מקלווין למעלות צלזיוס.

    Args:
        kelvin (float): טמפרטורה בקלווין.

    Returns:
        float: טמפרטורה במעלות צלזיוס.
    """
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    ממירה טמפרטורה ממעלות פרנהייט לקלווין.

    Args:
        fahrenheit (float): טמפרטורה במעלות פרנהייט.

    Returns:
        float: טמפרטורה בקלווין.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    ממירה טמפרטורה מקלווין למעלות פרנהייט.

    Args:
        kelvin (float): טמפרטורה בקלווין.

    Returns:
        float: טמפרטורה במעלות פרנהייט.
    """
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit
```

כל פונקציה כוללת:

-   **הערות סוג:** `(celsius: float) -> float` מציין את סוג הארגומנט והערך המוחזר.
-   **Docstring:** מחרוזת תיעוד המתארת את מטרת הפונקציה, הארגומנטים והערך המוחזר.
-   **לוגיקה:** הפונקציה מבצעת המרה בהתאם לנוסחאות ידועות.

### פונקציית המרה אוניברסלית

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    ממירה טמפרטורה מיחידת מידה אחת לאחרת.

    Args:
        value (float): טמפרטורה להמרה.
        from_unit (str): יחידת המידה המקורית ('C', 'F', 'K').
        to_unit (str): יחידת המידה היעד ('C', 'F', 'K').

    Returns:
        float: הטמפרטורה המומרת.

    Raises:
        ValueError: אם מצויינות יחידות מידה לא תקינות.
    """
    if from_unit == to_unit:
        return value  # אין צורך בהמרה

    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)

    raise ValueError("יחידות מידה לא תקינות.")
```

פונקציה זו מקבלת ערך טמפרטורה, יחידת מידה מקורית ויחידת מידה יעד. בהתבסס על פרמטרים אלה, היא קוראת לפונקציית ההמרה המתאימה. אם יחידות המידה זהות, היא מחזירה את הערך המקורי. אם מצוינות יחידות מידה לא תקינות, היא מעלה `ValueError`.

### פונקציית `main`

```python
def main():
    """
    פונקציה ראשית לאינטראקציה עם המשתמש.
    """
    while True:
        print("\nבחר פעולה:")
        print("1. המר טמפרטורה")
        print("2. יציאה")

        choice = input("הכנס מספר פעולה: ")

        if choice == '1':
            try:
                value = float(input("הכנס טמפרטורה: "))
                from_unit = input("הכנס יחידת מידה מקורית (C, F, K): ").upper()
                to_unit = input("הכנס יחידת מידה יעד (C, F, K): ").upper()

                result = convert_temperature(value, from_unit, to_unit)
                print(f"תוצאה: {result:.2f} {to_unit}")

            except ValueError as ex:
                print(f"שגיאה: {ex}")
            except Exception as ex:
                print(f"שגיאה בלתי צפויה: {ex}")

        elif choice == '2':
            print("להתראות!")
            break
        else:
            print("קלט לא תקין. נסה שוב.")

if __name__ == "__main__":
    main()
```

פונקציית `main` מכילה לולאה אינסופית שבה מוצגת למשתמש אפשרות לבחור פעולה. אם המשתמש בוחר בהמרה, התוכנית מבקשת ערך טמפרטורה, יחידות מידה מקוריות ויעד, קוראת לפונקציה `convert_temperature` ומציגה את התוצאה. כמו כן, אנו מטפלים בשגיאות קלט אפשריות באמצעות בלוק `try-except`.

## קובץ `convertor_kcf_dataclass.py`

קובץ זה מכיל יישום של מחשבון טמפרטורה באמצעות `dataclass`.

### מחלקת `TemperatureConverter`

```python
from dataclasses import dataclass

@dataclass
class TemperatureConverter:
    """
    מחלקה להמרת טמפרטורות בין מעלות צלזיוס, פרנהייט וקלווין.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        ...  # הגדרת שיטות המרה
```

-   **ייבוא `dataclass`:** אנו מייבאים את הדקורטור `dataclass` מהמודול `dataclasses`.
-   **מחלקה `TemperatureConverter`:** אנו יוצרים מחלקה `TemperatureConverter` ומקשטים אותה באמצעות `@dataclass`. זה ייצור באופן אוטומטי בנאי ושיטות אחרות הדרושות למחלקה.
-   **שיטות מחלקה:** כל פונקציות ההמרה שלנו הן כעת שיטות של מחלקה `TemperatureConverter`. הפרמטר הראשון `self` מציין את מופע המחלקה.

שיטות ההמרה דומות לשיטות ב-`convertor_kcf.py`, מלבד העובדה שהן שיטות מחלקה ומקבלות `self` כארגומנט הראשון.

### פונקציית `convert_temperature`

```python
    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        ...  # קריאה לשיטות מחלקה
```

פונקציה זו, כמו ב-`convertor_kcf.py`, מקבלת ערך טמפרטורה, יחידת מידה מקורית ויחידת מידה יעד. אבל כעת היא קוראת לשיטות המחלקה `TemperatureConverter`.

### פונקציית `main`

```python
def main():
    """
    פונקציה ראשית לאינטראקציה עם המשתמש.
    """
    converter = TemperatureConverter()

    while True:
       ...  # אינטראקציה עם המשתמש
            result = converter.convert_temperature(value, from_unit, to_unit)
        ...
```

בפונקציה `main`, אנו יוצרים מופע של המחלקה `TemperatureConverter` בשם `converter`. כעת אנו קוראים לשיטות ההמרה דרך מופע זה, לדוגמה: `converter.convert_temperature()`.

## השוואה בין שתי הגישות

-   **`convertor_kcf.py`:** פונקציות ההמרה קיימות באופן עצמאי זו מזו, מה שיכול להיות פחות מאורגן עבור תוכניות מורכבות יותר.
-   **`convertor_kcf_dataclass.py`:** כל פונקציות ההמרה מקובצות בתוך מחלקה, מה שהופך את הקוד למודולרי וקריא יותר. `dataclass` גם מספק יצירה אוטומטית של בנאי ושיטות אחרות.

## הרצת הקוד

כדי להפעיל כל אחד מהקבצים, ודא שמותקן אצלך Python. לאחר מכן, בצע את הפעולות הבאות בטרמינל:

```bash
python convertor_kcf.py
```

או

```bash
python convertor_kcf_dataclass.py
```

שתי הגישות פותרות את אותה הבעיה, אך בשיטות שונות של ארגון קוד.
`dataclass` מאפשרת גישה מובנית יותר לפתרון הבעיה ומפשטת את תחזוקת והרחבת הקוד.