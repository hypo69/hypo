# Модуль MusicMath

## סקירה כללית

מודול זה מספק דוגמאות לקשר בין מתמטיקה למוזיקה.

## תוכן עניינים

- [פונקציות](#פונקציות)
  - [`calculate_frequency`](#calculate_frequency)
  - [`calculate_interval_ratio`](#calculate_interval_ratio)
  - [`calculate_tempo_duration`](#calculate_tempo_duration)
  - [`calculate_note_duration`](#calculate_note_duration)
  - [`calculate_rhythm_pattern`](#calculate_rhythm_pattern)
  - [`calculate_note_number`](#calculate_note_number)
  - [`generate_scale_frequencies`](#generate_scale_frequencies)
  - [`calculate_tuning_deviation`](#calculate_tuning_deviation)
  - [`get_note_name`](#get_note_name)
  - [`get_note_info_from_freq`](#get_note_info_from_freq)
  - [`tune_instrument`](#tune_instrument)
  - [`note_name_to_number`](#note_name_to_number)
  - [`find_nearest_notes`](#find_nearest_notes)
  - [`print_musical_examples`](#print_musical_examples)

## פונקציות

### `calculate_frequency`

**תיאור**:
מחשבת את התדר של תו, בהינתן המספר שלו בסולם הכרומטי.

**פרמטרים**:
- `note_number` (int): מספר התו ביחס ל-A4 (A4 = 0).
- `concert_a_freq` (float, optional): התדר של התו A4. ברירת מחדל: 440.0.

**החזרות**:
- `float`: תדר התו בהרץ.

### `calculate_interval_ratio`

**תיאור**:
מחשבת את יחס התדרים בין שני תווים, בהינתן המספרים שלהם.

**פרמטרים**:
- `note1_number` (int): מספר התו הראשון.
- `note2_number` (int): מספר התו השני.

**החזרות**:
- `str`: יחס התדרים בצורה של שבר פשוט.

### `calculate_tempo_duration`

**תיאור**:
מחשבת את משך הזמן הכולל בשניות של קטע מוזיקלי.

**פרמטרים**:
- `bpm` (int): טמפו בפעימות לדקה.
- `beat_length` (float): משך זמן של פעימה אחת בשניות.
- `beats` (int): מספר הפעימות בקטע המוזיקלי.

**החזרות**:
- `float`: משך הזמן הכולל של הקטע בשניות.

### `calculate_note_duration`

**תיאור**:
מחשבת את משך הזמן של תו בשניות.

**פרמטרים**:
- `tempo` (int): טמפו בפעימות לדקה.
- `note_value` (float): משך התו ביחס לתו שלם (1.0 = תו שלם, 0.5 = חצי תו, 0.25 = רבע תו, וכו').

**החזרות**:
- `float`: משך הזמן של התו בשניות.

### `calculate_rhythm_pattern`

**תיאור**:
מחשבת את המשך הכולל של דפוס קצבי בשניות.

**פרמטרים**:
- `bar_length` (float): משך זמן של תיבה במספרים של תוים שלמים.
- `note_values` (list): רשימה של משכי זמן של תוים (ביחס לתו שלם).

**החזרות**:
- `float`: משך הזמן הכולל של דפוס הקצבי בשניות.

### `calculate_note_number`

**תיאור**:
מחשבת את מספר התו בסולם הכרומטי על בסיס התדר שלו.

**פרמטרים**:
- `frequency` (float): תדר התו בהרץ.
- `concert_a_freq` (float, optional): התדר של התו A4. ברירת מחדל: 440.0.

**החזרות**:
- `int`: מספר התו ביחס ל-A4 (A4 = 0).

### `generate_scale_frequencies`

**תיאור**:
יוצרת תדרי תווים של סולם נתון.

**פרמטרים**:
- `root_note_number` (int): מספר תו שורש.
- `scale_pattern` (list): תבנית הסולם (רצף של חצאי טונים).
- `concert_a_freq` (float, optional): התדר של התו A4. ברירת מחדל: 440.0.

**החזרות**:
- `list`: רשימה של תדרי התווים בסולם.

### `calculate_tuning_deviation`

**תיאור**:
מחשבת את סטיית התדר מהתדר היעד באחוזים.

**פרמטרים**:
- `target_frequency` (float): תדר היעד.
- `actual_frequency` (float): התדר בפועל.

**החזרות**:
- `float`: אחוז הסטייה.

### `get_note_name`

**תיאור**:
מחזירה את שם התו על פי מספרו בסולם הכרומטי.

**פרמטרים**:
- `note_number` (int): מספר התו ביחס ל-A4 (A4 = 0).

**החזרות**:
- `str`: שם התו (למשל, "A4", "C#5", "Bb3").

### `get_note_info_from_freq`

**תיאור**:
מדפיסה מידע על תו לפי התדר שלו.

**פרמטרים**:
- `freq` (float): תדר התו בהרץ.

### `tune_instrument`

**תיאור**:
מדפיסה מידע לגבי סטיית כלי הנגינה מהתדר המבוקש.

**פרמטרים**:
- `target_freq` (float): תדר היעד.
- `actual_freq` (float): התדר בפועל.

### `note_name_to_number`

**תיאור**:
ממירה שם תו (למשל, "A4") למספר שלו ביחס ל-A4 (A4 = 0).

**פרמטרים**:
- `note_name` (str): שם התו (למשל, "A4", "C#5", "Bb3").

**החזרות**:
- `int`: מספר התו ביחס ל-A4 (A4 = 0), או `None` אם הקלט אינו תקין.

### `find_nearest_notes`

**תיאור**:
מוצאת את שני התווים הקרובים ביותר (מלמעלה ומלמטה) לתדר נתון.

**פרמטרים**:
- `frequency` (float): תדר התו בהרץ.
- `concert_a_freq` (float, optional): התדר של התו A4. ברירת מחדל: 440.0.

**החזרות**:
- `tuple`: טאפל (שם התו התחתון, שם התו העליון).

### `print_musical_examples`

**תיאור**:
מדפיסה דוגמאות לשימוש בפונקציות.