# life.py

## סקירה כללית

קובץ זה מיישם את המשחק "חיים" - סימולציה של אוטומט תאים שפותחה על ידי ג'ון קונוויי. המשחק מבוסס על רשת של תאים, כל תא יכול להיות במצב "חי" או "מת". מצבו של כל תא בדור הבא תלוי במצבי השכנים שלו בדור הנוכחי. מטרת המשחק היא לצפות בהתפתחות תצורה התחלתית של תאים ולחקור דפוסים מעניינים שמתעוררים בתהליך הסימולציה.

## תוכן עניינים

- [פונקציות](#Functions)
  - [`get_grid_size`](#get_grid_size)
  - [`get_generations`](#get_generations)
  - [`get_initial_config`](#get_initial_config)
  - [`create_grid`](#create_grid)
  - [`print_grid`](#print_grid)
  - [`count_live_neighbours`](#count_live_neighbours)
  - [`apply_rules`](#apply_rules)
  - [`next_generation`](#next_generation)
  - [`play_game_of_life`](#play_game_of_life)

## Functions

### `get_grid_size`

**Description**: מבקשת מהמשתמש את גודל הרשת.

**Parameters**:
None

**Returns**:
- `tuple[int, int]`: גודל השורות והעמודות של הרשת.

**Raises**:
- `ValueError`: אם המשתמש מזין ערך לא חוקי.

### `get_generations`

**Description**: מבקשת מהמשתמש את מספר הדורות.

**Parameters**:
None

**Returns**:
- `int`: מספר הדורות.

**Raises**:
- `ValueError`: אם המשתמש מזין ערך לא חוקי.

### `get_initial_config`

**Description**: מבקשת מהמשתמש תצורה התחלתית או משתמשת באקראית.

**Parameters**:
- `rows` (int): מספר השורות ברשת.
- `cols` (int): מספר העמודות ברשת.

**Returns**:
- `list[str]`: תצורה התחלתית של הרשת.

**Raises**:
- None

### `create_grid`

**Description**: יוצרת רשת בהתבסס על הגדלים והתצורה ההתחלתית.

**Parameters**:
- `rows` (int): מספר השורות ברשת.
- `cols` (int): מספר העמודות ברשת.
- `initial_config` (Optional[list[str]], optional): התצורה ההתחלתית. ברירת מחדל: `None`.

**Returns**:
- `list[list[str]]`: הרשת.

**Raises**:
- None

### `print_grid`

**Description**: מדפיסה את הרשת על המסך.

**Parameters**:
- `grid` (list[list[str]]): הרשת להדפסה.

**Returns**:
- `None`

**Raises**:
- None

### `count_live_neighbours`

**Description**: סופרת את מספר השכנים החיים של תא נתון.

**Parameters**:
- `grid` (list[list[str]]): הרשת.
- `row` (int): אינדקס השורה של התא.
- `col` (int): אינדקס העמודה של התא.

**Returns**:
- `int`: מספר השכנים החיים.

**Raises**:
- None

### `apply_rules`

**Description**: מחילה את חוקי המשחק כדי לקבוע את מצב התא בדור הבא.

**Parameters**:
- `grid` (list[list[str]]): הרשת.
- `row` (int): אינדקס השורה של התא.
- `col` (int): אינדקס העמודה של התא.

**Returns**:
- `str`: מצב התא בדור הבא (`*` אם חי, ` ` אם מת).

**Raises**:
- None

### `next_generation`

**Description**: יוצרת את הרשת של הדור הבא.

**Parameters**:
- `grid` (list[list[str]]): הרשת הנוכחית.

**Returns**:
- `list[list[str]]`: הרשת של הדור הבא.

**Raises**:
- None

### `play_game_of_life`

**Description**: פונקציה ראשית המנהלת את הסימולציה של המשחק "חיים".

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None