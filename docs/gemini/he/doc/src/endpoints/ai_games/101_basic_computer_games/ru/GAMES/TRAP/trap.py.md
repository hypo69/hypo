# trap.py

## סקירה כללית

קובץ זה מיישם את משחק הלוח "מלכודת" לשני שחקנים. מטרת המשחק היא להקיף משבצות של היריב עם המשבצות שלך, ובכך להשתלט עליהן. השחקן עם מספר המשבצות הגדול ביותר בסוף המשחק מנצח.

## תוכן עניינים

- [פונקציות](#functions)
    - [`create_board`](#create_board)
    - [`display_board`](#display_board)
    - [`is_valid_move`](#is_valid_move)
    - [`is_cell_empty`](#is_cell_empty)
    - [`get_neighbors`](#get_neighbors)
    - [`can_capture`](#can_capture)
    - [`capture_cell`](#capture_cell)
    - [`make_move`](#make_move)
    - [`switch_player`](#switch_player)
    - [`is_board_full`](#is_board_full)
    - [`calculate_scores`](#calculate_scores)
    - [`determine_winner`](#determine_winner)
    - [`play_trap_game`](#play_trap_game)

## פונקציות

### `create_board`

**תיאור**: יוצרת לוח משחק ריק.

**Returns**:
- `list[list[int]]`: לוח משחק בגודל `BOARD_SIZE` x `BOARD_SIZE` המאוכלס באפסים (תאים ריקים).

### `display_board`

**תיאור**: מציגה את מצב לוח המשחק הנוכחי בקונסולה.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק להצגה.

**Returns**:
- `None`: פונקציה זו אינה מחזירה דבר.

### `is_valid_move`

**תיאור**: בודקת אם מהלך מסוים (שורה ועמודה) נמצא בתוך גבולות לוח המשחק.

**Parameters**:
- `row` (int): מספר השורה של המהלך.
- `col` (int): מספר העמודה של המהלך.

**Returns**:
- `bool`: `True` אם המהלך תקף, אחרת `False`.

### `is_cell_empty`

**תיאור**: בודקת האם תא מסוים בלוח המשחק ריק.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.

**Returns**:
- `bool`: `True` אם התא ריק (מכיל 0), אחרת `False`.

### `get_neighbors`

**תיאור**: מחזירה את רשימת התאים השכנים לתא נתון.

**Parameters**:
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.

**Returns**:
- `list[tuple[int, int]]`: רשימה של קואורדינטות (שורה, עמודה) עבור השכנים.

### `can_capture`

**תיאור**: בודקת האם ניתן ללכוד תא של היריב.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.
- `current_player` (int): מספר השחקן הנוכחי (1 או 2).

**Returns**:
- `bool`: `True` אם התא יכול להילכד, אחרת `False`.

### `capture_cell`

**תיאור**: לוכדת תא מסוים על ידי החלפת התוכן שלו בשחקן הנוכחי.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.
- `current_player` (int): מספר השחקן הנוכחי (1 או 2).

**Returns**:
- `None`: פונקציה זו אינה מחזירה דבר.

### `make_move`

**תיאור**: מבצעת מהלך של שחקן על ידי הצבת סממן בלוח המשחק ולוכדת משבצות של היריב אם יש כאלה.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של המהלך.
- `col` (int): מספר העמודה של המהלך.
- `current_player` (int): מספר השחקן הנוכחי (1 או 2).

**Returns**:
- `None`: פונקציה זו אינה מחזירה דבר.

### `switch_player`

**תיאור**: מחליפה בין השחקן הנוכחי לשחקן היריב.

**Parameters**:
- `current_player` (int): מספר השחקן הנוכחי (1 או 2).

**Returns**:
- `int`: מספר השחקן היריב (2 אם השחקן הנוכחי הוא 1, 1 אם השחקן הנוכחי הוא 2).

### `is_board_full`

**תיאור**: בודקת האם כל לוח המשחק מלא.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.

**Returns**:
- `bool`: `True` אם לוח המשחק מלא, אחרת `False`.

### `calculate_scores`

**תיאור**: מחשבת את הניקוד עבור כל שחקן.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.

**Returns**:
- `tuple[int, int]`: מספר הנקודות של שחקן 1 ושחקן 2.

### `determine_winner`

**תיאור**: קובעת את המנצח על סמך הניקוד.

**Parameters**:
- `player1_score` (int): הניקוד של שחקן 1.
- `player2_score` (int): הניקוד של שחקן 2.

**Returns**:
- `str`: הודעה המציינת את המנצח או תיקו.

### `play_trap_game`

**תיאור**: פונקציית המשחק הראשית שיוזמת את המשחק, מקבלת קלט מהמשתמש, מבצעת מהלכים, ומציגה את התוצאה.

**Returns**:
- `None`: פונקציה זו אינה מחזירה דבר.