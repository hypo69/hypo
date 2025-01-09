# FakeDataGenerator

## סקירה כללית

מודול זה מספק מחלקה `FakeDataGenerator` ליצירת נתונים מזויפים כמו שמות, כתובות דוא"ל, מספרי טלפון וכתובות.

## תוכן עניינים

- [מחלקות](#מחלקות)
    - [`FakeDataGenerator`](#FakeDataGenerator)
- [פונקציות](#פונקציות)
    - [`random_name`](#random_name)
    - [`random_email`](#random_email)
    - [`random_phone`](#random_phone)
    - [`random_address`](#random_address)
    - [`random_string`](#random_string)
    - [`random_int`](#random_int)
    - [`random_choice`](#random_choice)

## מחלקות

### `FakeDataGenerator`

**Description**: מחלקה זו מייצגת גנרטור נתונים מזויפים. היא מיישמת פונקציות ליצירת נתונים שונים כמו שמות, כתובות דוא"ל, מספרי טלפון וכתובות.

**Methods**:
- `random_name`: יצירת שם מלא אקראי.
- `random_email`: יצירת כתובת דוא"ל אקראית.
- `random_phone`: יצירת מספר טלפון אקראי.
- `random_address`: יצירת כתובת אקראית.
- `random_string`: יצירת מחרוזת אקראית.
- `random_int`: יצירת מספר שלם אקראי.
- `random_choice`: בחירת ערך אקראי מרשימה.

## פונקציות

### `random_name`

**Description**: יוצר שם מלא אקראי.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: שם מלא, המורכב משם פרטי אקראי ושם משפחה אקראי.

### `random_email`

**Description**: יוצר כתובת דוא"ל אקראית.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: כתובת דוא"ל בפורמט `firstname.lastname@domain`.

### `random_phone`

**Description**: יוצר מספר טלפון אקראי בפורמט `+1-XXX-XXX-XXXX`.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: מספר טלפון.

### `random_address`

**Description**: יוצר כתובת אקראית בפורמט `מספר רחוב, עיר`.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: כתובת.

### `random_string`

**Description**: יוצר מחרוזת אקראית באורך נתון.

**Parameters**:
- `length` (int, optional): אורך המחרוזת. ברירת מחדל: 10.

**Returns**:
- `str`: מחרוזת אקראית המכילה אותיות ומספרים.

### `random_int`

**Description**: יוצר מספר שלם אקראי בטווח נתון.

**Parameters**:
- `min_value` (int, optional): ערך מינימלי. ברירת מחדל: 0.
- `max_value` (int, optional): ערך מקסימלי. ברירת מחדל: 100.

**Returns**:
- `int`: מספר שלם אקראי.

### `random_choice`

**Description**: בוחר ערך אקראי מרשימת אפשרויות.

**Parameters**:
- `options` (List[str]): רשימת ערכים לבחירה.

**Returns**:
- `str`: ערך אקראי מהרשימה.