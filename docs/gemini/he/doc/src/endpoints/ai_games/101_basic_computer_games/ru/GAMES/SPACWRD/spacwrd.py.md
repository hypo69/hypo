# SPACWRD

## סקירה כללית

משחק "מילת החלל" הוא משחק מילים טקסטואלי שבו השחקן מנסה לנחש מילה שהמחשב בחר על ידי הזנת אותיות. המחשב מציג את המילה עם רווחים במקום אותיות שלא נוחשו. לאחר כל ניסיון, השחקן מקבל מידע על כמה אותיות הוא ניחש נכון, ויכול להמשיך לנחש את האותיות הנותרות. המשחק מסתיים כאשר השחקן מנחש את כל האותיות במילה.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [פונקציות](#פונקציות)
   - [`choose_word`](#choose_word)
   - [`display_word`](#display_word)
   - [`update_word`](#update_word)
   - [`correct_guesses`](#correct_guesses)
   - [`play_spaceword_game`](#play_spaceword_game)

## פונקציות

### `choose_word`

**Description**: בוחרת מילה אקראית מתוך רשימה.

**Parameters**:
- `word_list` (list): רשימה של מילים לבחירה.

**Returns**:
- `str`: מילה שנבחרה באופן אקראי.

### `display_word`

**Description**: מציגה את המילה, מסתירה אותיות שלא נוחשו.

**Parameters**:
- `word` (str): המילה להצגה.
- `guessed_letters` (list): רשימה של אותיות שניחשו.

**Returns**:
- `str`: המילה המוצגת עם אותיות מנוחשות ורווחים לאותיות שלא נוחשו.

### `update_word`

**Description**: מעדכנת את המילה המוצגת, חושפת אותיות שניחשו.

**Parameters**:
- `word` (str): המילה המקורית.
- `guessed_word` (str): המילה המוצגת עם אותיות מנוחשות ורווחים.
- `user_letter` (str): האות שניחשה.

**Returns**:
- `str`: המילה המעודכנת עם האותיות שנחשו.

### `correct_guesses`

**Description**: סופרת את מספר האותיות שנוחשו נכון במילה.

**Parameters**:
- `guessed_letters` (list): רשימה של אותיות שניחשו.
- `target_word` (str): המילה המקורית.

**Returns**:
- `int`: מספר האותיות שנוחשו נכון.

### `play_spaceword_game`

**Description**: הלוגיקה הראשית של משחק "מילת החלל".

**Parameters**:
    אין פרמטרים.

**Returns**:
    None: הפונקציה לא מחזירה דבר.

**Raises**:
    None: הפונקציה לא מעלה חריגות.