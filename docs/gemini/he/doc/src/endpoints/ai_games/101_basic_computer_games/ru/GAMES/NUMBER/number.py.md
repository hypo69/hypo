# מודול משחק המספרים

## סקירה כללית

מודול זה מדמה משחק קוביות בו השחקן מנסה לצבור כמה שיותר נקודות מבלי להפסיד על ידי גלגול 1.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)

## פונקציות

### `main`

**תיאור**:
פונקציה ראשית המפעילה את המשחק. המשחק מאפשר לשחקן לגלגל קוביה עד שמופיע המספר 1 או שהשחקן בוחר להפסיק.

**פרמטרים**:
- `אין`

**מחזירה**:
- `אין`

```python
def main():
    """
    Args:
        None.

    Returns:
        None.
    """
    import random

    totalScore = 0

    while True:
        roll_again = input("Roll the dice? (Y/N): ").upper()
        
        if roll_again != "Y":
            print(f"Total Score: {totalScore}")
            break
        
        diceRoll = random.randint(1, 6)
        
        if diceRoll == 1:
            totalScore = 0
            print(f"Sorry, you rolled a 1. Total Score: {totalScore}")
            break
        else:
            totalScore += diceRoll
            print(f"Current Score: {totalScore}")