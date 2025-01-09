# BATTLE

## סקירה כללית

מודול זה מיישם משחק מלחמה ימית פשוט בין שחקן למחשב. השחקנים יורים בתורות על לוחות המשחק של השני, במטרה לפגוע בספינות. המשחק נמשך 30 סיבובים או עד שאחד השחקנים מנצח.

## תוכן עניינים

- [פונקציות](#פונקציות)
    - [`create_board`](#create_board)
    - [`place_computer_ships`](#place_computer_ships)
    - [`display_board`](#display_board)
    - [`play_battle`](#play_battle)

## פונקציות

### `create_board`

**Description**: יוצר לוח משחק (מטריצה) בגודל שצוין ומאכלס אותו עם אפסים.

**Parameters**:
- `size` (int): גודל לוח המשחק.

**Returns**:
- `list[list[int]]`: לוח משחק (רשימה דו מימדית) מלא באפסים.

### `place_computer_ships`

**Description**: ממקם 5 ספינות בגודל 1 על לוח המשחק של המחשב באופן אקראי.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק שבו הספינות ימוקמו.

**Returns**:
- `None`: הפונקציה משנה את לוח המשחק ישירות.

### `display_board`

**Description**: מציג את לוח המשחק בקונסולה, הסתרת ספינות של המחשב אם `is_computer` נכון.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק שיוצג.
- `is_computer` (bool, optional): מציין האם הלוח של המחשב צריך להיות מוסתר. ברירת מחדל: `False`.

**Returns**:
- `None`: הפונקציה מדפיסה את הלוח בקונסולה.

### `play_battle`

**Description**: מנהל את הלוגיקה של המשחק "Battle". המשחק נמשך 30 סיבובים.

**Parameters**:
- `None`: פונקציה זו אינה מקבלת פרמטרים.

**Returns**:
- `None`: הפונקציה מנהלת את המשחק ישירות.

**Raises**:
- `ValueError`: אם קלט המשתמש אינו מספר.