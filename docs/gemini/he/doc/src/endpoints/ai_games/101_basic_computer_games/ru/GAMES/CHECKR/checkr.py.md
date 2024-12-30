# CHECKR

## סקירה כללית

קובץ זה מכיל יישום טקסטואלי של משחק הדמקה הבסיסי. המשחק מתנהל על לוח 8x8, כאשר השחקן משחק נגד המחשב. המטרה היא להגיע לקצה הנגדי של הלוח עם אחד מהכלים שלך, תוך הימנעות מלכידה על ידי כלי היריב.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
    - [`initialize_board`](#initialize_board)
    - [`draw_board`](#draw_board)
    - [`is_valid_move`](#is_valid_move)
    - [`update_board`](#update_board)
    - [`check_win`](#check_win)
    - [`get_computer_moves`](#get_computer_moves)
    - [`computer_turn`](#computer_turn)
    - [`player_turn`](#player_turn)
    - [`play_checkers`](#play_checkers)

## פונקציות

### `initialize_board`

**Description**: מאתחל את הלוח 8x8 עם מיקום התחלתי של הכלים.

**Parameters**:
    - אין

**Returns**:
    - `list[list[str]]`: לוח משחק מאותחל כרשימה של רשימות, כאשר כל רשימה מייצגת שורה, וכל תא מכיל את הערך של 'EMPTY', 'PLAYER' או 'COMPUTER'.

### `draw_board`

**Description**: מצייר את המצב הנוכחי של הלוח במסוף.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.

**Returns**:
    - `None`: פונקציה זו אינה מחזירה דבר, אך היא מדפיסה את לוח המשחק למסוף.

### `is_valid_move`

**Description**: בודק אם המהלך של השחקן חוקי.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.
    - `row` (int): השורה הנוכחית של הכלי.
    - `col` (int): העמודה הנוכחית של הכלי.
    - `new_row` (int): השורה החדשה של הכלי.
    - `new_col` (int): העמודה החדשה של הכלי.
    - `player` (str): סוג השחקן ("1" לשחקן, "2" למחשב).

**Returns**:
    - `bool`: `True` אם המהלך חוקי, `False` אחרת.

### `update_board`

**Description**: מעדכן את הלוח לאחר מהלך.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.
    - `row` (int): השורה הנוכחית של הכלי.
    - `col` (int): העמודה הנוכחית של הכלי.
    - `new_row` (int): השורה החדשה של הכלי.
    - `new_col` (int): העמודה החדשה של הכלי.

**Returns**:
    - `None`: הפונקציה מעדכנת את הלוח ישירות ואינה מחזירה דבר.

### `check_win`

**Description**: בודק אם שחקן או מחשב ניצחו.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.
    - `player` (str): סוג השחקן ("1" לשחקן, "2" למחשב).

**Returns**:
    - `bool`: `True` אם השחקן ניצח, `False` אחרת.

### `get_computer_moves`

**Description**: מוצא את כל המהלכים האפשריים של המחשב.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.

**Returns**:
    - `list[tuple[int, int, int, int]]`: רשימה של כל המהלכים האפשריים, כאשר כל מהלך מיוצג על ידי 4 מספרים: שורה ועמודה נוכחיות ושורה ועמודה חדשות.

### `computer_turn`

**Description**: מבצע מהלך של המחשב.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.

**Returns**:
    - `None`: הפונקציה מעדכנת את הלוח ישירות ואינה מחזירה דבר.

### `player_turn`

**Description**: מבקשת ומבצעת מהלך של שחקן.

**Parameters**:
    - `board` (list[list[str]]): לוח המשחק כרשימה של רשימות.

**Returns**:
    - `None`: הפונקציה מעדכנת את הלוח ישירות ואינה מחזירה דבר.

**Raises**:
    - `ValueError`: אם קלט השחקן אינו מספר שלם.

### `play_checkers`

**Description**: פונקציית המשחק הראשית.

**Parameters**:
    - אין

**Returns**:
    - `None`: הפונקציה מריצה את המשחק ואינה מחזירה דבר.