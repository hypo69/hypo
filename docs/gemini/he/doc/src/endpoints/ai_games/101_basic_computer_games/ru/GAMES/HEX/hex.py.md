# HEX

## סקירה כללית

משחק HEX הוא משחק לוגי שבו שני שחקנים לסירוגין מניחים את האסימונים שלהם על רשת משושה, במטרה לחבר את הצדדים הנגדיים של הלוח. המטרה של כל שחקן היא ליצור שרשרת רציפה של האסימונים שלו המחברת בין הצדדים הנגדיים של הלוח. שחקנים מניחים את האסימונים שלהם על תאים משושים עד שאחד מהם מצליח לחבר בין הצדדים שלו. בגרסה זו, המשחק מיושם עבור שני שחקנים: '1' ו- '2'.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`print_board`](#print_board)
  - [`get_move`](#get_move)
  - [`check_win`](#check_win)
  - [`play_hex`](#play_hex)

## פונקציות

### `print_board`

**Description**:
מציג את המצב הנוכחי של הלוח.

```python
def print_board(board):
    """
    Args:
        board (list[list[str]]): הלוח הנוכחי.

    Returns:
        None
    """
```

### `get_move`

**Description**:
מבקש מהשחקן קואורדינטות למהלך.

```python
def get_move(board: list[list[str]], player: str) -> tuple[int, int]:
    """
    Args:
        board (list[list[str]]): הלוח הנוכחי.
        player (str): השחקן הנוכחי ('1' או '2').

    Returns:
        tuple[int, int]: קואורדינטות המהלך (שורה, עמודה).
    
    Raises:
        ValueError: אם הקלט לא תקין.
    """
```

### `check_win`

**Description**:
בודק האם השחקן ניצח.

```python
def check_win(board: list[list[str]], player: str) -> bool:
    """
    Args:
        board (list[list[str]]): הלוח הנוכחי.
        player (str): השחקן הנוכחי ('1' או '2').

    Returns:
        bool: `True` אם השחקן ניצח, אחרת `False`.
    """
```

### `play_hex`

**Description**:
הפונקציה הראשית של המשחק.

```python
def play_hex():
    """
    Args:
        None

    Returns:
        None
    """
```