# `melody_composer.py`

## סקירה כללית

סקריפט זה משתמש במודל Melody RNN של Magenta ליצירת קטעי מוזיקה המבוססים על ז'אנר וטמפו מועדפים על המשתמש. בנוסף, הוא מוסיף אקורדים ותבנית תופים בסיסית לקטע המוזיקלי.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
- [משתנים](#משתנים)
- [לולאות](#לולאות)

## פונקציות

אין פונקציות מוגדרות במפורש בסקריפט זה. הסקריפט משתמש במודול `magenta`  ובפונקציות שלו.

## משתנים

### `output_dir`
**Description**: תיקייה לשמירת קבצי MIDI שנוצרו.

**Type**: `str`

**Default**: `'generated_music'`

### `model_name`
**Description**: שם מודל Melody RNN המשמש ליצירת מוזיקה.

**Type**: `str`

**Default**: `'attention_rnn'`

### `melody_rnn`
**Description**: מודל Melody RNN המשמש ליצירת רצפים מלודיים.

**Type**: `melody_rnn_sequence_generator.MelodyRnnSequenceGenerator`

### `temperature`
**Description**: ערך השולט על רנדומליות יצירת המוזיקה (ערכים גבוהים יותר מובילים ליותר אקראיות).

**Type**: `float`

**Default**: `1.0`

### `num_music_pieces`
**Description**: מספר קטעי המוזיקה שיש ליצור.

**Type**: `int`

**Default**: `3`

### `steps_per_music_piece`
**Description**: מספר הצעדים (step) בכל קטע מוזיקלי.

**Type**: `int`

**Default**: `128`

### `preferred_genre`
**Description**: הז'אנר המועדף על המשתמש (לדוגמה, "classical", "jazz", "rock").

**Type**: `str`

**User Input**: משתמש כקלט מהמשתמש.

### `preferred_tempo`
**Description**: הטמפו המועדף על המשתמש (BPM).

**Type**: `int`

**User Input**: משתמש כקלט מהמשתמש.

### `chord_progressions`
**Description**: מילון של התקדמות אקורדים עבור ז'אנרים שונים.

**Type**: `dict`

**Default**:
```python
{
    "classical": ["C", "Am", "F", "G"],
    "jazz": ["Cmaj7", "Dm7", "Em7", "A7"],
    "rock": ["C", "G", "Am", "F"],
}
```

### `drum_pattern`
**Description**: תבנית תופים בסיסית לליווי המוזיקה.

**Type**: `mm.DrumTrack`

## לולאות

### `for i in range(num_music_pieces)`

**Description**: לולאה היוצרת מספר קטעי מוזיקה לפי `num_music_pieces`.
בתוך הלולאה:
- יוצר רצף מלודיה באמצעות `melody_rnn.generate`.
- יוצר רצף אקורדים המבוסס על הז'אנר המועדף.
- משלב את המלודיה והאקורדים יחד.
- יוצר רצף מוזיקלי סופי על ידי הוספת תבנית תופים.
- שומר את הרצף כקובץ MIDI.
- מדפיס הודעה על יצירת קטע המוזיקה.
```markdown