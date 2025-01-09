# `melody_composer.py`

## סקירה כללית

מודול זה יוצר קטעי מוזיקה באמצעות מודל Melody RNN, מאפשר בחירת ז'אנר וקצב, וכולל ליווי של תופים.

## תוכן עניינים

- [פונקציות](#functions)
- [משתנים גלובליים](#global-variables)

## פונקציות

### `main`

**Description**: פונקציה ראשית שמגדירה את תהליך יצירת המוזיקה. מקבלת קלט מהמשתמש עבור ז'אנר וקצב, ויוצרת מספר קטעי מוזיקה.

**Parameters**:
- אין פרמטרים.

**Returns**:
- אין ערך מוחזר.

**Raises**:
- אין חריגות ספציפיות שמתועדות.

## משתנים גלובליים

### `output_dir`
**Description**: נתיב לספרייה בה יישמרו קבצי ה-MIDI שנוצרו.

### `model_name`
**Description**: שם המודל Melody RNN בשימוש.

### `melody_rnn`
**Description**: מופע של המחלקה `MelodyRnnSequenceGenerator`.

### `temperature`
**Description**: ערך טמפרטורה המשפיע על רמת האקראיות ביצירת המוזיקה.

### `num_music_pieces`
**Description**: מספר קטעי המוזיקה שייוצרו.

### `steps_per_music_piece`
**Description**: מספר הצעדים (step) בקטע מוזיקלי.

### `preferred_genre`
**Description**: הז'אנר המועדף של המשתמש.

### `preferred_tempo`
**Description**: הקצב המועדף של המשתמש.

### `chord_progressions`
**Description**: מילון המכיל אקורדים לפי ז'אנר.

### `drum_pattern`
**Description**: תבנית תופים בסיסית.