# BULL

## סקירה כללית

משחק "BULL" הוא משחק לוגי מספרי שבו המחשב מייצר מספר אקראי בן ארבע ספרות, כאשר כל הספרות שונות, והשחקן מנסה לנחש את המספר הזה. לאחר כל ניסיון, המחשב מדווח על מספר ה"שור" (ספרה שנוחשה ונמצאת במקום הנכון) ו"פרות" (ספרה שנוחשה, אך נמצאת במקום לא נכון).

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`generate_target_number`](#generate_target_number)
  - [`get_bulls_and_cows`](#get_bulls_and_cows)

## פונקציות

### `generate_target_number`

**תיאור**: מייצרת מספר אקראי בן ארבע ספרות עם ספרות ייחודיות.

```python
def generate_target_number() -> str:
    """
    Args:
        None

    Returns:
        str: מספר אקראי בן ארבע ספרות עם ספרות ייחודיות.
    """
```

### `get_bulls_and_cows`

**תיאור**: סופרת את מספר ה"שור" וה"פרות".

**פרמטרים**:

-   `user_guess` (str): ניחוש המשתמש כמחרוזת.
-   `target_number` (str): המספר המטרה כמחרוזת.

**החזרות**:

-   tuple(int, int): טאפל המכיל את מספר השור והפרות, בהתאמה.

```python
def get_bulls_and_cows(user_guess: str, target_number: str) -> tuple[int, int]:
    """
    Args:
        user_guess (str): ניחוש המשתמש כמחרוזת.
        target_number (str): המספר המטרה כמחרוזת.

    Returns:
        tuple[int, int]: טאפל המכיל את מספר השור והפרות, בהתאמה.
    """
```
```