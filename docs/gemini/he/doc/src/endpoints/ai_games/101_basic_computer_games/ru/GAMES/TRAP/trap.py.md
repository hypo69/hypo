# trap.py

## סקירה כללית

קובץ זה מיישם את משחק הלוח "מלכודת" לשני שחקנים. המטרה היא להקיף את הריבועים של היריב עם הריבועים שלך כדי ללכוד אותם.

## תוכן עניינים

- [קבועים](#constants)
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

## קבועים

### `BOARD_SIZE`
- **Description**: גודל לוח המשחק.
- **Type**: `int`
- **Value**: 7

## פונקציות

### `create_board`

**Description**: יוצר לוח משחק ריק.

**Returns**:
- `list[list[int]]`: לוח משחק דו-ממדי, המיוצג על ידי רשימה של רשימות, כאשר כל תא מאותחל ל-0.

### `display_board`

**Description**: מציג את המצב הנוכחי של לוח המשחק.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.

**Returns**:
- `None`: הפונקציה לא מחזירה דבר, אלא מדפיסה את מצב הלוח לקונסולה.

### `is_valid_move`

**Description**: בודק אם מהלך נתון הוא חוקי.

**Parameters**:
- `row` (int): מספר השורה.
- `col` (int): מספר העמודה.

**Returns**:
- `bool`: `True` אם המהלך חוקי, אחרת `False`.

### `is_cell_empty`

**Description**: בודק אם תא נתון בלוח ריק.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה.
- `col` (int): מספר העמודה.

**Returns**:
- `bool`: `True` אם התא ריק (ערכו 0), אחרת `False`.

### `get_neighbors`

**Description**: מחזירה את הקואורדינטות של התאים השכנים לתא נתון.

**Parameters**:
- `row` (int): מספר השורה.
- `col` (int): מספר העמודה.

**Returns**:
- `list[tuple[int, int]]`: רשימה של צמדי קואורדינטות של השכנים.

### `can_capture`

**Description**: בודק אם ניתן ללכוד תא של היריב.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.
- `current_player` (int): השחקן הנוכחי (1 או 2).

**Returns**:
- `bool`: `True` אם ניתן ללכוד את התא, אחרת `False`.

### `capture_cell`

**Description**: לוכד תא על ידי החלפת הערך שלו בערך של השחקן הנוכחי.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה של התא.
- `col` (int): מספר העמודה של התא.
- `current_player` (int): השחקן הנוכחי (1 או 2).

**Returns**:
- `None`: הפונקציה לא מחזירה דבר, אלא משנה את לוח המשחק ישירות.

### `make_move`

**Description**: מבצע מהלך על ידי הצבת סימן של השחקן הנוכחי בתא נתון ולכידת תאים אפשריים של היריב.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.
- `row` (int): מספר השורה.
- `col` (int): מספר העמודה.
- `current_player` (int): השחקן הנוכחי (1 או 2).

**Returns**:
- `None`: הפונקציה לא מחזירה דבר, אלא משנה את לוח המשחק ישירות.

### `switch_player`

**Description**: מחליף בין השחקנים.

**Parameters**:
- `current_player` (int): השחקן הנוכחי (1 או 2).

**Returns**:
- `int`: השחקן הבא (1 או 2).

### `is_board_full`

**Description**: בודק אם לוח המשחק מלא.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.

**Returns**:
- `bool`: `True` אם הלוח מלא, אחרת `False`.

### `calculate_scores`

**Description**: מחשב את הניקוד של כל שחקן.

**Parameters**:
- `board` (list[list[int]]): לוח המשחק.

**Returns**:
- `tuple[int, int]`: צמד המכיל את ניקוד השחקן הראשון ואת ניקוד השחקן השני.

### `determine_winner`

**Description**: קובע את המנצח על סמך הניקוד.

**Parameters**:
- `player1_score` (int): ניקוד השחקן הראשון.
- `player2_score` (int): ניקוד השחקן השני.

**Returns**:
- `str`: הודעה על המנצח או על תיקו.

### `play_trap_game`

**Description**: הפונקציה הראשית המנהלת את משחק המלכודת.

**Returns**:
- `None`: הפונקציה לא מחזירה דבר, אלא מנהלת את כל מהלך המשחק, כולל תצוגה, קבלת קלט, עיבוד לוגיקה והצגת תוצאה.

**Raises**:
- ValueError: כאשר הקלט של השחקן אינו מספר שלם.