# Magenta Melody RNN - מדריך למפתחים

## סקירה כללית

מדריך זה מספק למפתחים הנחיות מקיפות על אופן ההתקנה, ההגדרה והשימוש במודל Melody RNN של Magenta באמצעות Python ו-TensorFlow. המדריך מכסה את התהליך מההתקנה ועד לשילוב מנגינות עם אקורדים וכלי הקשה.

## תוכן עניינים

1.  [התקנת Magenta](#התקנת-magenta)
2.  [ייבוא מודולים נדרשים](#ייבוא-מודולים-נדרשים)
3.  [טעינת מודל מאומן](#טעינת-מודל-מאומן)
4.  [יצירת מנגינה](#יצירת-מנגינה)
5.  [עבודה עם MIDI](#עבודה-עם-midi)
6.  [הוספת אקורדים וכלי הקשה](#הוספת-אקורדים-וכלי-הקשה)
7.  [דוגמה מלאה](#דוגמה-מלאה)
8.  [טיפים נוספים](#טיפים-נוספים)

## התקנת Magenta

השלבים הבאים מנחים אותך בהתקנת ספריית Magenta.

1.  **יצירת סביבה וירטואלית (מומלץ):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```
2.  **התקנת Magenta:**
    ```bash
    pip install magenta
    ```

    *   **הערה:** ייתכן ש-Magenta תדרוש TensorFlow. אם אין לך אותה, pip תתקין אותה אוטומטית.
    *   **עבור האצת GPU:** אם יש לך NVIDIA GPU ו-CUDA, אתה יכול להתקין גרסה של TensorFlow עם תמיכת GPU (עיין בתיעוד של TensorFlow).

## ייבוא מודולים נדרשים

לאחר התקנת Magenta, ייבא את המודולים הדרושים לסקריפט ה-Python שלך:

```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.common import sequence_example_lib
```

## טעינת מודל מאומן

מודלי Melody RNN מאומנים על מערכי נתונים גדולים וזמינים להורדה. אתה יכול לבחור אחד מהמודלים המאומנים מראש (למשל, `attention_rnn` או `basic_rnn`).

*   **אתחול המודל:**

    ```python
    model_name = 'attention_rnn'  # או 'basic_rnn'
    melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
        model_name=model_name
    )
    ```

    *   בעת האתחול, המודל יטען אוטומטית את המשקלים הדרושים.

## יצירת מנגינה

כעת, תוכל ליצור מנגינה באמצעות הפונקציה `generate()`:

```python
# פרמטרי יצירה
temperature = 1.0  # שולט באקראיות, 1.0 הוא ערך נורמלי
num_steps = 128   # מספר הצעדים (אורך) של המנגינה
primer_sequence = None # אפשר להגדיר מנגינת התחלה. אם נשאר None, המודל יתחיל מאפס.

# יצירת מנגינה
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)
```

*   `temperature`: ככל שהערך גבוה יותר, כך היצירה תהיה אקראית ו"יצירתית" יותר, אך היא גם עלולה להיות פחות קוהרנטית.
*   `steps`: מגדיר את מספר הצעדים במנגינה שנוצרה.
*   `primer_sequence`: מגדיר מנגינה שהמודל משתמש בה כנקודת התחלה ליצירה. אם הערך הוא `None`, המודל יתחיל מאפס.

## עבודה עם MIDI

המנגינה שנוצרה מיוצגת כאובייקט `Sequence`, שאפשר לשמור כקובץ MIDI או להשתמש בו לעיבוד נוסף:

```python
# שמירה ב-MIDI
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)
midi_file = os.path.join(output_dir, 'generated_melody.mid')
mm.sequence_proto_to_midi_file(melody_sequence, midi_file)

print(f"Melody saved to: {midi_file}")
```

## הוספת אקורדים וכלי הקשה

ניתן לשלב את המנגינה שנוצרה עם רצפי אקורדים וקצבי תופים, כפי שמוצג בדוגמה הבאה:

```python
# אקורדים
chords = ["C", "G", "Am", "F"] * (num_steps // 4)  # יצירת רצף אקורדים על ידי חזרה
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# כלי הקשה
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps//4,
    steps_per_quarter=4,
)

music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120  # הגדרת טמפו

# שמירת הרצועה המלאה ב-MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

## דוגמה מלאה

הקוד הבא מדגים כיצד ליצור מנגינה, להוסיף אליה אקורדים וכלי הקשה, ולשמור את הכל כקובץ MIDI:

```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator

# 1. הגדרת פרמטרים
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)

model_name = 'attention_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model_name=model_name
)

temperature = 1.0
num_steps = 128
primer_sequence = None

# 2. יצירת מנגינה
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)

# 3. הוספת אקורדים
chords = ["C", "G", "Am", "F"] * (num_steps // 4)
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# 4. הוספת כלי הקשה
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps // 4,
    steps_per_quarter=4,
)
music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120

# 5. שמירה ב-MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

## טיפים נוספים

*   **נסו עם פרמטרים שונים:** נסו ערכים שונים של `temperature` ו-`num_steps`.
*   **טעינת MIDI משלכם:** אפשר להשתמש במנגינות משלכם כבסיס (`primer_sequence`).
*   **אמנו את המודל על הנתונים שלכם:** אם אתם רוצים סגנון ספציפי, נסו לאמן את המודל על מערך הנתונים שלכם.
*   **עיינו בתיעוד של Magenta:** Magenta מספקת תיעוד ודוגמאות טובים.
*   **שימו לב:**  `primer_sequence` צריך להיות מסוג `mm.NoteSequence()`.

אני מקווה שהמדריך המפורט הזה יעזור לכם להתחיל לעבוד עם Melody RNN! אם יש לכם שאלות נוספות, אל תהססו לשאול.