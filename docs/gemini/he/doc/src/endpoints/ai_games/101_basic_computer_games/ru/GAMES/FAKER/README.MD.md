# FakeDataGenerator

## סקירה כללית

קוד זה מגדיר את המחלקה `FakeDataGenerator` ליצירת נתונים אקראיים כגון שמות, כתובות, מספרי טלפון, כתובות דוא"ל וכו'.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [מחלקות](#מחלקות)
    - [FakeDataGenerator](#fakedatagenerator)
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

**Description**: מחלקה זו מספקת שיטות ליצירת נתונים אקראיים שונים.

**Attributes**:
- `first_names` (list): רשימה של שמות פרטיים.
- `last_names` (list): רשימה של שמות משפחה.
- `cities` (list): רשימה של ערים.
- `streets` (list): רשימה של רחובות.
- `domains` (list): רשימה של דומיינים.

**Methods**:
- `random_name`: יוצר שם אקראי.
- `random_email`: יוצר כתובת דוא"ל אקראית.
- `random_phone`: יוצר מספר טלפון אקראי.
- `random_address`: יוצר כתובת אקראית.
- `random_string`: יוצר מחרוזת אקראית.
- `random_int`: יוצר מספר שלם אקראי.
- `random_choice`: בוחר אלמנט אקראי מרשימה.

## פונקציות

### `random_name`

**Description**: יוצר שם אקראי המורכב משם פרטי ושם משפחה.

**Returns**:
- `str`: שם מלא אקראי.

### `random_email`

**Description**: יוצר כתובת דוא"ל אקראית בפורמט `שם.משפחה@דומיין`.

**Returns**:
- `str`: כתובת דוא"ל אקראית.

### `random_phone`

**Description**: יוצר מספר טלפון אקראי בפורמט `+1-XXX-XXX-XXXX`.

**Returns**:
- `str`: מספר טלפון אקראי.

### `random_address`

**Description**: יוצר כתובת אקראית בפורמט `מספר רחוב, עיר`.

**Returns**:
- `str`: כתובת אקראית.

### `random_string`

**Description**: יוצר מחרוזת אקראית באורך נתון, הכוללת אותיות ומספרים.

**Parameters**:
- `length` (int, optional): אורך המחרוזת. ברירת מחדל: 10.

**Returns**:
- `str`: מחרוזת אקראית.

### `random_int`

**Description**: יוצר מספר שלם אקראי בטווח נתון.

**Parameters**:
- `min_value` (int, optional): ערך מינימלי. ברירת מחדל: 0.
- `max_value` (int, optional): ערך מקסימלי. ברירת מחדל: 100.

**Returns**:
- `int`: מספר שלם אקראי.

### `random_choice`

**Description**: בוחר אלמנט אקראי מתוך רשימה נתונה.

**Parameters**:
- `options` (List[str]): רשימה של ערכים לבחירה.

**Returns**:
- `str`: אלמנט אקראי מהרשימה.