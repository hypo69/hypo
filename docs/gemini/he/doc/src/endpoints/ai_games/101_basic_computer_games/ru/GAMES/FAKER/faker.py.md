# FakeDataGenerator

## סקירה כללית

מודול זה מספק מחלקה `FakeDataGenerator` ליצירת נתונים מזויפים, כגון שמות, כתובות אימייל, מספרי טלפון וכתובות. הוא שימושי ליצירת נתוני בדיקה או מילוי נתונים ביישומים.

## תוכן עניינים

1. [מחלקות](#מחלקות)
   - [`FakeDataGenerator`](#FakeDataGenerator)
2. [פונקציות](#פונקציות)
   - [`random_name`](#random_name)
   - [`random_email`](#random_email)
   - [`random_phone`](#random_phone)
   - [`random_address`](#random_address)
   - [`random_string`](#random_string)
   - [`random_int`](#random_int)
   - [`random_choice`](#random_choice)

## מחלקות

### `FakeDataGenerator`

**Description**: מחלקה זו מספקת שיטות ליצירת נתונים מזויפים. היא כוללת רשימות סטטיות של שמות פרטיים, שמות משפחה, ערים, רחובות ודומיינים כדי ליצור נתונים מציאותיים.

**Methods**:
- [`random_name`](#random_name): מחזירה שם מלא אקראי.
- [`random_email`](#random_email): מחזירה כתובת דוא"ל אקראית.
- [`random_phone`](#random_phone): מחזירה מספר טלפון אקראי.
- [`random_address`](#random_address): מחזירה כתובת אקראית.
- [`random_string`](#random_string): מחזירה מחרוזת אקראית באורך שצוין.
- [`random_int`](#random_int): מחזירה מספר שלם אקראי בטווח שצוין.
- [`random_choice`](#random_choice): מחזירה פריט אקראי מרשימה שסופקה.

## פונקציות

### `random_name`

**Description**: יוצר שם מלא אקראי על ידי שילוב של שם פרטי אקראי ושם משפחה אקראי.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: שם מלא אקראי.

### `random_email`

**Description**: יוצר כתובת דוא"ל אקראית על ידי שילוב של שם פרטי אקראי, שם משפחה אקראי ודומיין אקראי.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: כתובת דוא"ל אקראית בפורמט `first_name.last_name@domain`.

### `random_phone`

**Description**: יוצר מספר טלפון אקראי בפורמט `+1-XXX-XXX-XXXX`.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: מספר טלפון אקראי.

### `random_address`

**Description**: יוצר כתובת אקראית על ידי שילוב של מספר בית אקראי, רחוב אקראי ועיר אקראית.

**Parameters**:
- אין פרמטרים.

**Returns**:
- `str`: כתובת אקראית בפורמט `house_number street, city`.

### `random_string`

**Description**: יוצר מחרוזת אקראית באורך שצוין, המורכבת מאותיות ומספרים.

**Parameters**:
- `length` (int, optional): אורך המחרוזת. ברירת מחדל: 10.

**Returns**:
- `str`: מחרוזת אקראית.

### `random_int`

**Description**: יוצר מספר שלם אקראי בטווח מינימום ומקסימום שצוין.

**Parameters**:
- `min_value` (int, optional): הערך המינימלי. ברירת מחדל: 0.
- `max_value` (int, optional): הערך המקסימלי. ברירת מחדל: 100.

**Returns**:
- `int`: מספר שלם אקראי.

### `random_choice`

**Description**: בוחר פריט אקראי מרשימה שסופקה.

**Parameters**:
- `options` (List[str]): רשימת ערכים לבחירה.

**Returns**:
- `str`: פריט אקראי מהרשימה.