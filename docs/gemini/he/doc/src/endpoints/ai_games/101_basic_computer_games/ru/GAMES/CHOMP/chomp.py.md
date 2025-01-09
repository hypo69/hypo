# chomp.py

## סקירה כללית

קובץ זה מיישם את המשחק "CHOMP", משחק לשני שחקנים שבו שחקנים לסירוגין "אוכלים" חתיכות מלוח שוקולד, כאשר אחת החתיכות היא "רעילה". השחקן שמאלץ לאכול את החתיכה הרעילה מפסיד. המשחק מופעל באמצעות שורת הפקודה.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [initialize_board](#initialize_board)
  - [display_board](#display_board)
  - [make_move](#make_move)
  - [is_game_over](#is_game_over)
  - [play_chomp](#play_chomp)

## פונקציות

### `initialize_board`

**תיאור**:
אתחול לוח המשחק (לוח שוקולד).

**פרמטרים**:
- `rows` (int): מספר השורות בלוח.
- `cols` (int): מספר העמודות בלוח.

**ערך מוחזר**:
- `list of lists`: רשימה של רשימות המייצגות את לוח המשחק, כאשר 'X' מייצג שוקולד ו- ' ' מייצג מקום ריק.

```python
def initialize_board(rows, cols) -> list[list[str]]:
    """
    Args:
        rows (int): מספר השורות בלוח.
        cols (int): מספר העמודות בלוח.

    Returns:
        list of lists: רשימה של רשימות המייצגות את לוח המשחק, כאשר 'X' מייצג שוקולד ו- ' ' מייצג מקום ריק.
    """
```

### `display_board`

**תיאור**:
הצגת המצב הנוכחי של הלוח על המסך.

**פרמטרים**:
- `board` (list of lists): לוח המשחק.

**ערך מוחזר**:
- None

```python
def display_board(board: list[list[str]]) -> None:
    """
    Args:
        board (list of lists): לוח המשחק.

    Returns:
        None:
    """
```

### `make_move`

**תיאור**:
עדכון מצב הלוח לאחר מהלך של שחקן. כל התאים מימין ולמטה מהמיקום הנבחר מוסרים.

**פרמטרים**:
- `board` (list of lists): לוח המשחק.
- `row_move` (int): השורה בה השחקן ביצע מהלך.
- `col_move` (int): העמודה בה השחקן ביצע מהלך.

**ערך מוחזר**:
- `list of lists`: לוח המשחק המעודכן.

```python
def make_move(board: list[list[str]], row_move: int, col_move: int) -> list[list[str]]:
    """
    Args:
        board (list of lists): לוח המשחק.
        row_move (int): השורה בה השחקן ביצע מהלך.
        col_move (int): העמודה בה השחקן ביצע מהלך.

    Returns:
        list of lists: לוח המשחק המעודכן.
    """
```

### `is_game_over`

**תיאור**:
בדיקה האם המשחק נגמר. המשחק נגמר כאשר החתיכה הרעילה (פינה שמאלית עליונה) נאכלה.

**פרמטרים**:
- `board` (list of lists): לוח המשחק.

**ערך מוחזר**:
- `bool`: `True` אם המשחק נגמר, אחרת `False`.

```python
def is_game_over(board: list[list[str]]) -> bool:
  """
    Args:
        board (list of lists): לוח המשחק.

    Returns:
        bool: True אם המשחק נגמר, אחרת False.
    """
```

### `play_chomp`

**תיאור**:
הפונקציה הראשית של משחק "CHOMP". מיישמת את המשחק, כולל הזנת מידות הלוח, הצגת הלוח, ועיבוד מהלכי שחקנים.

**פרמטרים**:
- None

**ערך מוחזר**:
- None

**Raises**:
- `ValueError`: אם הקלט אינו מספר שלם.
- `IndexError`: אם המהלך שבוצע חורג מגבולות הלוח.

```python
def play_chomp() -> None:
    """
    Args:
        None:

    Returns:
        None:

    Raises:
        ValueError: אם הקלט אינו מספר שלם.
        IndexError: אם המהלך שבוצע חורג מגבולות הלוח.
    """