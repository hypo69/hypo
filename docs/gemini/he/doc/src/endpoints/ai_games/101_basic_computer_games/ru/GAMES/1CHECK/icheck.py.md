# Checkerboard Puzzle Solver

## סקירה כללית

קוד זה מיישם פותר חידות לוח דמקה. המטרה היא להסיר כמה שיותר דמקות מהלוח על ידי ביצוע קפיצות חוקיות. המשחק מתחיל עם דמקות בשורות החיצוניות של לוח 8x8 ומסתיים כאשר לא ניתן לבצע קפיצות נוספות.

## תוכן עניינים

- [מחלקה `Checkerboard`](#מחלקה-checkerboard)
  - [`__init__`](#__init__)
  - [`is_valid_jump`](#is_valid_jump)
  - [`perform_jump`](#perform_jump)
  - [`find_possible_jumps`](#find_possible_jumps)
  - [`play`](#play)
  - [`display_board`](#display_board)

## מחלקות

### `Checkerboard`

**תיאור**: מייצגת את לוח הדמקה ואת מצבו.

**מאפיינים**:
- `board` (List[List[int]]): מצב הלוח, כאשר `0` מייצג משבצת ריקה ו-`1` מייצג דמקה.
- `removed_checkers` (int): מונה הדמקות שהוסרו.

**שיטות**:
- [`__init__`](#__init__)
- [`is_valid_jump`](#is_valid_jump)
- [`perform_jump`](#perform_jump)
- [`find_possible_jumps`](#find_possible_jumps)
- [`play`](#play)
- [`display_board`](#display_board)

### `__init__`

**תיאור**: מאתחל את הלוח עם 48 דמקות בשורות החיצוניות.

```python
def __init__(self) -> None:
    """
    Args:
        self: מייצג את האובייקט של המחלקה.

    Returns:
        None: הפונקציה לא מחזירה ערך.
    """
```

### `is_valid_jump`

**תיאור**: בודקת האם קפיצה חוקית.

**פרמטרים**:
- `start` (Tuple[int, int]): מיקום ההתחלה (שורה, טור).
- `end` (Tuple[int, int]): מיקום הנחיתה (שורה, טור).

**החזרות**:
- `bool`: `True` אם הקפיצה חוקית, אחרת `False`.

```python
def is_valid_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> bool:
    """
    Args:
        self: מייצג את האובייקט של המחלקה.
        start (Tuple[int, int]): מיקום ההתחלה (שורה, טור).
        end (Tuple[int, int]): מיקום הנחיתה (שורה, טור).

    Returns:
        bool: `True` אם הקפיצה חוקית, אחרת `False`.
    """
```

### `perform_jump`

**תיאור**: מבצעת קפיצה ומסירה את הדמקה שקפצו מעליה.

**פרמטרים**:
- `start` (Tuple[int, int]): מיקום ההתחלה (שורה, טור).
- `end` (Tuple[int, int]): מיקום הנחיתה (שורה, טור).

**החזרות**:
- `None`: הפונקציה לא מחזירה ערך.

```python
def perform_jump(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
    """
    Args:
        self: מייצג את האובייקט של המחלקה.
        start (Tuple[int, int]): מיקום ההתחלה (שורה, טור).
        end (Tuple[int, int]): מיקום הנחיתה (שורה, טור).

    Returns:
        None: הפונקציה לא מחזירה ערך.
    """
```

### `find_possible_jumps`

**תיאור**: מוצאת את כל הקפיצות האפשריות על הלוח.

**החזרות**:
- `List[Tuple[Tuple[int, int], Tuple[int, int]]]`: רשימה של טאפלים, כאשר כל טאפל מכיל את מיקומי ההתחלה והסיום של קפיצה חוקית.

```python
def find_possible_jumps(self) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Args:
        self: מייצג את האובייקט של המחלקה.

    Returns:
        List[Tuple[Tuple[int, int], Tuple[int, int]]]: רשימה של טאפלים, כאשר כל טאפל מכיל את מיקומי ההתחלה והסיום של קפיצה חוקית.
    """
```

### `play`

**תיאור**: מדמה את המשחק על ידי ביצוע קפיצות עד שלא ניתן לבצע עוד קפיצות.

**החזרות**:
- `None`: הפונקציה לא מחזירה ערך.

```python
def play(self) -> None:
    """
    Args:
         self: מייצג את האובייקט של המחלקה.

    Returns:
         None: הפונקציה לא מחזירה ערך.
    """
```

### `display_board`

**תיאור**: מציגה את המצב הנוכחי של הלוח.

**החזרות**:
- `None`: הפונקציה לא מחזירה ערך.

```python
def display_board(self) -> None:
    """
    Args:
         self: מייצג את האובייקט של המחלקה.

    Returns:
         None: הפונקציה לא מחזירה ערך.
    """
```