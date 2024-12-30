# SPACWRD

## סקירה כללית

משחק "מילת החלל" הוא משחק טקסט שבו השחקן מנסה לנחש מילה שהמחשב בחר על ידי הזנת אותיות. המחשב מציג את המילה עם רווחים במקום אותיות שלא נוחשו. לאחר כל ניסיון, השחקן מקבל מידע על כמה אותיות הוא ניחש ויכול להמשיך לנחש את האותיות הנותרות. המשחק מסתיים כאשר השחקן מנחש את כל אותיות המילה.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`choose_word`](#choose_word)
  - [`display_word`](#display_word)
  - [`update_word`](#update_word)
  - [`correct_guesses`](#correct_guesses)
  - [`play_spaceword_game`](#play_spaceword_game)

## פונקציות

### `choose_word`

**Description**: בוחר מילה אקראית מתוך רשימה.

**Parameters**:
- `word_list` (list): רשימת המילים מהן יש לבחור.

**Returns**:
- `str`: מילה שנבחרה באופן אקראי מהרשימה.

### `display_word`

**Description**: מציג את המילה כאשר האותיות שלא נוחשו מוסתרות.

**Parameters**:
- `word` (str): המילה אותה יש להציג.
- `guessed_letters` (list): רשימה של האותיות שהשחקן ניחש.

**Returns**:
- `str`: המילה המוצגת עם רווחים במקום האותיות שלא נוחשו.

### `update_word`

**Description**: מעדכן את המילה המוצגת, חושף את האותיות שנוחשו.

**Parameters**:
- `word` (str): המילה המקורית.
- `guessed_word` (str): המילה הנוכחית עם אותיות מוסתרות.
- `user_letter` (str): האות שהמשתמש ניחש.

**Returns**:
- `str`: המילה המעודכנת עם האותיות שנוחשו חשופות.

### `correct_guesses`

**Description**: סופר את מספר האותיות שנוחשו נכון במילה.

**Parameters**:
- `guessed_letters` (list): רשימת האותיות שהמשתמש ניחש.
- `target_word` (str): המילה שהמחשב בחר.

**Returns**:
- `int`: מספר האותיות שנוחשו נכון.

### `play_spaceword_game`

**Description**: ההגיון המרכזי של המשחק "מילת החלל".

**Parameters**:
- None

**Returns**:
- None

**Raises**:
- None