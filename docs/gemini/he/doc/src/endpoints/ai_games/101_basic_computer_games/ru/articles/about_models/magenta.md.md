# תיעוד שימוש במודל Melody RNN של Magenta

## סקירה כללית
מסמך זה מספק מדריך מפורט כיצד להשתמש במודל Melody RNN מבית Magenta, תוך שימוש ב-Python ו-TensorFlow. המדריך מכסה את תהליך ההתקנה, טעינת המודל, יצירת מלודיות, ואינטגרציה עם אקורדים ותיפוף.

## תוכן עניינים
1. [התקנת Magenta](#התקנת-magenta)
2. [ייבוא מודולים נדרשים](#ייבוא-מודולים-נדרשים)
3. [טעינת מודל מאומן](#טעינת-מודל-מאומן)
4. [יצירת מלודיה](#יצירת-מלודיה)
5. [עבודה עם MIDI](#עבודה-עם-midi)
6. [הוספת אקורדים ותיפוף](#הוספת-אקורדים-ותיפוף)
7. [דוגמה מלאה](#דוגמה-מלאה)
8. [טיפים נוספים](#טיפים-נוספים)

## התקנת Magenta
לפני שמתחילים, יש להתקין את ספריית Magenta. ההתקנה המומלצת היא באמצעות pip.

### יצירת סביבה וירטואלית (מומלץ):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### התקנת Magenta:
```bash
pip install magenta
```
**הערה:** Magenta עשויה לדרוש TensorFlow. אם אינו מותקן, pip יתקין אותו אוטומטית.
*   **האצת GPU:** אם יש לך NVIDIA GPU ו-CUDA, ניתן להתקין את גרסת TensorFlow התומכת ב-GPU.

## ייבוא מודולים נדרשים
לאחר התקנת Magenta, יש לייבא את המודולים הדרושים לסקריפט Python שלך:

```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.common import sequence_example_lib
```

## טעינת מודל מאומן
מודלי Melody RNN מאומנים על מערכי נתונים גדולים וזמינים להורדה. ניתן לבחור אחד מהמודלים המאומנים מראש (למשל, `attention_rnn` או `basic_rnn`).

### אתחול המודל:
```python
model_name = 'attention_rnn'  # או 'basic_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model_name=model_name
)
```
בעת האתחול, המודל יטען אוטומטית את המשקולות הנדרשים.

## יצירת מלודיה
כעת אפשר ליצור מלודיה באמצעות המתודה `generate()`:
```python
# הגדרת פרמטרים ליצירת המלודיה
temperature = 1.0  # שליטה באקראיות, 1.0 הוא ערך ברירת המחדל
num_steps = 128   # מספר הצעדים (אורך) המלודיה
primer_sequence = None #  ניתן להגדיר מלודיה התחלתית, אם נשאר None, המודל יתחיל מאפס.

# יצירת מלודיה
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)
```
*   `temperature`: ככל שהערך גבוה יותר, כך היצירה תהיה אקראית ו"יצירתית" יותר, אך עשויה להיות פחות עקבית.
*   `steps`: קובע את מספר הצעדים במלודיה שנוצרת.
*   `primer_sequence`: קובע מלודיה שהמודל ייצא ממנה. אם `None`, המודל יתחיל מאפס.

## עבודה עם MIDI
המלודיה שנוצרה מיוצגת כאובייקט `Sequence` וניתן לשמור אותה כקובץ MIDI או להשתמש בה לעיבוד נוסף:

### שמירה כקובץ MIDI:
```python
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)
midi_file = os.path.join(output_dir, 'generated_melody.mid')
mm.sequence_proto_to_midi_file(melody_sequence, midi_file)

print(f"Melody saved to: {midi_file}")
```

## הוספת אקורדים ותיפוף
ניתן לשלב את המלודיה שנוצרה עם אקורדים ועם תפקידי תיפוף, כפי שמוצג בדוגמת הקוד:

```python
# הגדרת אקורדים
chords = ["C", "G", "Am", "F"] * (num_steps // 4)  # יצירת רצף אקורדים, על ידי חזרה
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# הגדרת תיפוף
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps//4,
    steps_per_quarter=4,
)

music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120  # קביעת הטמפו

# שמירה של השיר המלא כקובץ MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

## דוגמה מלאה
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
# 2. יצירת מלודיה
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)

# 3. הוספת אקורדים
chords = ["C", "G", "Am", "F"] * (num_steps // 4)
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# 4. הוספת תיפוף
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps // 4,
    steps_per_quarter=4,
)
music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120

# 5. שמירה כקובץ MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

## טיפים נוספים

*   **ניסוי עם פרמטרים:** נסה ערכים שונים עבור `temperature` ו-`num_steps`.
*   **טעינת קובצי MIDI משלך:** ניתן להשתמש במלודיות שלך כהתחלה (`primer_sequence`).
*   **אימון המודל על נתונים שלך:** אם אתה רוצה סגנון ספציפי, נסה לאמן את המודל על מערך נתונים שלך.
*   **לימוד מדריך Magenta:** Magenta מספקת תיעוד טוב ודוגמאות.
*   **שימו לב:** `primer_sequence` צריך להיות מסוג `mm.NoteSequence()`.