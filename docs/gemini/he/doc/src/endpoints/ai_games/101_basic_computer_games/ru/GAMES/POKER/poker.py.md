# poker.py

## סקירה כללית

מודול זה מיישם גרסה פשוטה של משחק הפוקר לשחקן יחיד. השחקן מקבל חמישה קלפים, יכול להחליף חלק מהם פעם אחת, ולאחר מכן מוצגת לו היד הסופית והזכייה (אם יש).

## תוכן עניינים

- [פונקציות](#Functions)
  - [create_hand](#create_hand)
  - [display_hand](#display_hand)
  - [get_cards_to_replace](#get_cards_to_replace)
  - [replace_cards](#replace_cards)
  - [analyze_hand](#analyze_hand)
  - [play_poker](#play_poker)

<br>

## Functions

### `create_hand`

**Description**: יוצר יד של 5 קלפים אקראיים (מספרים מ-1 עד 13).

**Parameters**:
- None

**Returns**:
- `list`: רשימה של 5 מספרים שלמים המייצגים את הקלפים.

**Raises**:
- None

<br>

### `display_hand`

**Description**: מציג את הקלפים על המסך, עם מספור עבור נוחות השחקן.

**Parameters**:
- `hand` (list): רשימה של מספרים שלמים המייצגים את הקלפים.

**Returns**:
- None

**Raises**:
- None

<br>

### `get_cards_to_replace`

**Description**: מבקש מהמשתמש את מספרי הקלפים שהוא רוצה להחליף.

**Parameters**:
- None

**Returns**:
- `list`: רשימה של אינדקסים של קלפים להחלפה (אינדקסים מתחילים מ-0). רשימה ריקה אם השחקן בחר לא להחליף קלפים.

**Raises**:
- None

<br>

### `replace_cards`

**Description**: מחליף את הקלפים הנבחרים בקלפים אקראיים חדשים.

**Parameters**:
- `hand` (list): רשימה של מספרים שלמים המייצגים את הקלפים.
- `replace_indices` (list): רשימה של אינדקסים של קלפים להחלפה.

**Returns**:
- `list`: הרשימה המעודכנת של הקלפים לאחר החלפה.

**Raises**:
- None

<br>

### `analyze_hand`

**Description**: מנתח את היד וקובע את השילוב המנצח (אם יש).

**Parameters**:
- `hand` (list): רשימה של מספרים שלמים המייצגים את הקלפים.

**Returns**:
- None

**Raises**:
- None

<br>

### `play_poker`

**Description**: מפעיל את המשחק פוקר.

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None