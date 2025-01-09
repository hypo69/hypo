# blkjak.py

## סקירה כללית

קובץ זה מיישם את משחק הקלפים בלק ג'ק. המשחק כולל שחקן שמתחרה נגד דילר, כאשר המטרה היא להגיע לערך הקרוב ל-21 נקודות מבלי לחרוג ממנו. המשחק מציע את האפשרות לקחת קלפים נוספים או לעצור.

## תוכן עניינים

- [פונקציות](#functions)
  - [`deal_card`](#deal_card)
  - [`calculate_hand_value`](#calculate_hand_value)
  - [`display_cards`](#display_cards)
  - [`play_blackjack`](#play_blackjack)

<a name="functions"></a>
## פונקציות

<a name="deal_card"></a>
### `deal_card`

**Description**: מוציא קלף מהחפיסה.

**Parameters**:
- `deck` (list): רשימה שמייצגת את חפיסת הקלפים.

**Returns**:
- `int`: הקלף שהוצא מהחפיסה.

<a name="calculate_hand_value"></a>
### `calculate_hand_value`

**Description**: מחשבת את הערך של יד הקלפים.

**Parameters**:
- `hand` (list): רשימה של קלפים ביד.

**Returns**:
- `int`: סכום ערכי הקלפים ביד.

<a name="display_cards"></a>
### `display_cards`

**Description**: מציגה את הקלפים של השחקן והדילר.

**Parameters**:
- `player_hand` (list): רשימת הקלפים של השחקן.
- `dealer_hand` (list): רשימת הקלפים של הדילר.
- `show_dealer_full` (bool, optional): האם להציג את כל הקלפים של הדילר. ברירת מחדל: `False`.

**Returns**:
- `None`

<a name="play_blackjack"></a>
### `play_blackjack`

**Description**: מריצה את משחק הבלאק ג'ק.

**Parameters**:
- `None`

**Returns**:
- `None`

```