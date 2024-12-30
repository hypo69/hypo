# DOGS

## סקירה כללית

משחק "כלבים" הוא משחק טקסט בו השחקן שולט בשני כלבים ומנסה לתפוס גנבים. השחקן מזין פקודות להזזת הכלבים, והגנבים נעים באופן אקראי. מטרת המשחק היא לתפוס את הגנבים במספר המינימלי של מהלכים.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [פונקציות](#פונקציות)
    - [create_field](#create_field)
    - [place_object](#place_object)
    - [print_field](#print_field)
    - [get_user_command](#get_user_command)
    - [move_dogs](#move_dogs)
    - [move_thieves](#move_thieves)
    - [check_catch](#check_catch)
    - [play_dogs_game](#play_dogs_game)

## פונקציות

### `create_field`

**תיאור**: יוצרת את לוח המשחק בגודל `FIELD_SIZE` x `FIELD_SIZE`, המיוצג כרשימה של רשימות.

```python
def create_field() -> list[list[str]]:
    """
    Args:
        None

    Returns:
        list[list[str]]: לוח המשחק.
    """
```

### `place_object`

**תיאור**: ממקמת אובייקט (כלב או גנב) במיקום פנוי אקראי בלוח.

```python
def place_object(field: list[list[str]], symbol: str) -> tuple[int, int]:
    """
    Args:
        field (list[list[str]]): רשימה דו-ממדית המייצגת את לוח המשחק.
        symbol (str): סמל האובייקט למיקום בלוח.

    Returns:
        tuple[int, int]: קואורדינטות (שורה, טור) של האובייקט שמוקם.
    """
```

### `print_field`

**תיאור**: מדפיסה את המצב הנוכחי של לוח המשחק למסך.

```python
def print_field(field: list[list[str]]) -> None:
    """
    Args:
        field (list[list[str]]): רשימה דו-ממדית המייצגת את לוח המשחק.

    Returns:
        None
    """
```

### `get_user_command`

**תיאור**: מבקשת מהמשתמש פקודה להזזת הכלבים.

```python
def get_user_command() -> str:
    """
    Args:
         None
    Returns:
        str: הפקודה שהזין המשתמש.
    """
```

### `move_dogs`

**תיאור**: מזיזה את הכלבים בהתאם לפקודת המשתמש.

```python
def move_dogs(field: list[list[str]], dog1: tuple[int, int], dog2: tuple[int, int], command: str) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Args:
        field (list[list[str]]): לוח המשחק.
        dog1 (tuple[int, int]): קואורדינטות הכלב הראשון.
        dog2 (tuple[int, int]): קואורדינטות הכלב השני.
        command (str): פקודת המשתמש.

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: קואורדינטות הכלבים לאחר התזוזה.
    """
```

### `move_thieves`

**תיאור**: מזיזה את הגנבים באופן אקראי על גבי לוח המשחק.

```python
def move_thieves(field: list[list[str]], thief1: tuple[int, int], thief2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Args:
        field (list[list[str]]): רשימה דו-ממדית המייצגת את לוח המשחק.
        thief1 (tuple[int, int]): קואורדינטות הגנב הראשון (row, col).
        thief2 (tuple[int, int]): קואורדינטות הגנב השני (row, col).

    Returns:
        tuple[tuple[int, int], tuple[int, int]]: קואורדינטות הגנבים לאחר התזוזה.
    """
```

### `check_catch`

**תיאור**: בודקת האם הכלבים תפסו את הגנבים.

```python
def check_catch(dog1: tuple[int, int], dog2: tuple[int, int], thief1: tuple[int, int], thief2: tuple[int, int]) -> bool:
    """
    Args:
        dog1 (tuple[int, int]): קואורדינטות הכלב הראשון.
        dog2 (tuple[int, int]): קואורדינטות הכלב השני.
        thief1 (tuple[int, int]): קואורדינטות הגנב הראשון.
        thief2 (tuple[int, int]): קואורדינטות הגנב השני.

    Returns:
        bool: האם הכלבים תפסו את הגנבים.
    """
```

### `play_dogs_game`

**תיאור**: פונקציית המשחק הראשית.

```python
def play_dogs_game() -> None:
    """
    Args:
         None

    Returns:
        None
    """