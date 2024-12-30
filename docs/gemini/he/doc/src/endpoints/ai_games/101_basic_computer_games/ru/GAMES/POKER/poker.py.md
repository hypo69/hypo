# poker.py

## סקירה כללית

קובץ זה מממש משחק פוקר פשוט לשחקן יחיד. המשחק כולל יצירת יד של 5 קלפים, אפשרות להחליף קלפים וניתוח היד לקביעת שילובים זוכים.

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

**Description**: יוצרת יד של 5 קלפים אקראיים (מספרים מ-1 עד 13).

**Parameters**:
- None

**Returns**:
- `list`: רשימה של 5 מספרים שלמים המייצגים את הקלפים.

<br>

### `display_hand`

**Description**: מציגה את הקלפים של השחקן על המסך, כאשר כל קלף ממוספר.

**Parameters**:
- `hand` (list): רשימה של קלפים (מספרים שלמים).

**Returns**:
- None

<br>

### `get_cards_to_replace`

**Description**: מבקשת מהשחקן להזין את מספרי הקלפים שהוא רוצה להחליף. מאפשרת להזין '0' כדי לא להחליף אף קלף.

**Parameters**:
- None

**Returns**:
- `list`: רשימה של אינדקסים של קלפים להחלפה, או רשימה ריקה אם השחקן בחר לא להחליף.

<br>

### `replace_cards`

**Description**: מחליפה את הקלפים שנבחרו על ידי השחקן בקלפים אקראיים חדשים.

**Parameters**:
- `hand` (list): רשימה של קלפים (מספרים שלמים).
- `replace_indices` (list): רשימה של אינדקסים של קלפים להחלפה.

**Returns**:
- `list`: רשימה מעודכנת של קלפים לאחר ההחלפה.

<br>

### `analyze_hand`

**Description**: מנתחת את היד וקובעת את השילוב המנצח (אם יש). מציגה הודעה בהתאם.

**Parameters**:
- `hand` (list): רשימה של קלפים (מספרים שלמים).

**Returns**:
- None

<br>

### `play_poker`

**Description**: מפעילה את המשחק, כולל יצירת יד, הצגת קלפים, בקשת החלפה, החלפת קלפים וניתוח היד.

**Parameters**:
- None

**Returns**:
- None