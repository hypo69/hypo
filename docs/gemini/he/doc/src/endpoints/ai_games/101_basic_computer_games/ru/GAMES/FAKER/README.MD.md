# FakeDataGenerator

## סקירה כללית

הקוד מספק מחלקה `FakeDataGenerator` המיועדת ליצירת נתונים מזויפים (אקראיים) כמו שמות, כתובות, מספרי טלפון, כתובות דוא"ל ועוד. מחלקה זו יכולה להיות שימושית לבדיקות, מילוי מסדי נתונים, יצירת נתוני הדגמה ומשימות אחרות שבהן נדרשת יצירת ערכים אקראיים.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [מחלקות](#מחלקות)
  - [FakeDataGenerator](#fakedatagenerator)
- [פונקציות](#פונקציות)
  - [random_name](#random_name)
  - [random_email](#random_email)
  - [random_phone](#random_phone)
  - [random_address](#random_address)
  - [random_string](#random_string)
  - [random_int](#random_int)
  - [random_choice](#random_choice)
- [דוגמה לשימוש](#דוגמה-לשימוש)

## מחלקות

### `FakeDataGenerator`

**Description**: מחלקה זו מספקת שיטות ליצירת סוגים שונים של נתונים מזויפים.

**Attributes**:

- `first_names`: רשימה של שמות פרטיים.
- `last_names`: רשימה של שמות משפחה.
- `cities`: רשימה של שמות ערים.
- `streets`: רשימה של שמות רחובות.
- `domains`: רשימה של דומיינים.

**Methods**:
- `random_name`: מחזירה שם מלא אקראי.
- `random_email`: מחזירה כתובת דוא"ל אקראית.
- `random_phone`: מחזירה מספר טלפון אקראי.
- `random_address`: מחזירה כתובת אקראית.
- `random_string`: מחזירה מחרוזת אקראית באורך נתון.
- `random_int`: מחזירה מספר שלם אקראי בטווח נתון.
- `random_choice`: מחזירה בחירה אקראית מתוך רשימה נתונה.

## פונקציות

### `random_name`

**Description**: יוצר שם מלא אקראי.

```python
def random_name(self) -> str:
    """
    Args:
        None

    Returns:
        str: שם מלא, מורכב משם פרטי ושם משפחה אקראיים.
    """
```

### `random_email`

**Description**: יוצר כתובת דוא"ל אקראית.

```python
def random_email(self) -> str:
    """
    Args:
        None

    Returns:
        str: כתובת דוא"ל בפורמט `name.lastname@domain`.
    """
```

### `random_phone`

**Description**: יוצר מספר טלפון אקראי בפורמט "+1-XXX-XXX-XXXX".

```python
def random_phone(self) -> str:
    """
    Args:
        None

    Returns:
        str: מספר טלפון.
    """
```

### `random_address`

**Description**: יוצר כתובת אקראית.

```python
def random_address(self) -> str:
    """
    Args:
        None

    Returns:
        str: כתובת בפורמט `street, city`.
    """
```

### `random_string`

**Description**: יוצר מחרוזת אקראית באורך נתון.

```python
def random_string(self, length: int = 10) -> str:
    """
    Args:
        length (int, optional): אורך המחרוזת. ברירת מחדל: 10.

    Returns:
        str: מחרוזת אקראית המכילה אותיות ומספרים.
    """
```

### `random_int`

**Description**: יוצר מספר שלם אקראי בטווח נתון.

```python
def random_int(self, min_value: int = 0, max_value: int = 100) -> int:
    """
    Args:
        min_value (int, optional): ערך מינימלי. ברירת מחדל: 0.
        max_value (int, optional): ערך מקסימלי. ברירת מחדל: 100.

    Returns:
        int: מספר שלם אקראי.
    """
```

### `random_choice`

**Description**: בוחר רכיב אקראי מתוך רשימה.

```python
def random_choice(self, options: List[str]) -> str:
    """
    Args:
        options (List[str]): רשימת ערכים לבחירה.

    Returns:
        str: רכיב אקראי מתוך הרשימה.
    """
```

## דוגמה לשימוש

```python
if __name__ == '__main__':
    faker = FakeDataGenerator()

    print(f'Name: {faker.random_name()}')
    print(f'Email: {faker.random_email()}')
    print(f'Phone: {faker.random_phone()}')
    print(f'Address: {faker.random_address()}')
    print(f'Random String: {faker.random_string(12)}')
    print(f'Random Int: {faker.random_int(50, 150)}')
    print(f'Random Choice: {faker.random_choice(["Option1", "Option2", "Option3"])}')
```
- יוצר מופע של המחלקה `FakeDataGenerator`.
- קורא למתודות המחלקה ליצירת סוגי נתונים שונים.
- מדפיס את התוצאות.