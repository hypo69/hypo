# מודול בוט דיסקורד

## תוכן עניינים
1. [סקירה כללית](#סקירה-כללית)
2. [פונקציות](#פונקציות)
    - [`recognizer`](#recognizer)
    - [`text_to_speech_and_play`](#text_to_speech_and_play)
3. [אירועים](#אירועים)
    - [`on_ready`](#on_ready)
    - [`on_message`](#on_message)
4. [פקודות](#פקודות)
    - [`hi`](#hi)
    - [`join`](#join)
    - [`leave`](#leave)
    - [`train`](#train)
    - [`test`](#test)
    - [`archive`](#archive)
    - [`select_dataset`](#select_dataset)
    - [`instruction`](#instruction)
    - [`correct`](#correct)
    - [`feedback`](#feedback)
    - [`getfile`](#getfile)

## סקירה כללית

קוד זה מייצג בוט דיסקורד שנכתב בפייתון באמצעות הספרייה `discord.py`. הבוט מבצע מספר פונקציות הקשורות לניהול מודל למידת מכונה, עיבוד אודיו ואינטראקציה עם משתמשים בערוצי טקסט וקולי בדיסקורד.

## פונקציות

### `recognizer`

**Description**: פונקציה זו מורידה קובץ אודיו, ממירה אותו לפורמט WAV, ומזהה דיבור באמצעות Google Speech Recognition.

**Parameters**:
- `file_path` (str): הנתיב לקובץ האודיו.
- `lang` (str, optional): שפת הזיהוי. ברירת מחדל: `None`.

**Returns**:
- `str`: הטקסט שזוהה מקובץ האודיו, או `None` אם לא ניתן היה לזהות דיבור.

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך זיהוי הדיבור.

### `text_to_speech_and_play`

**Description**: פונקציה זו ממירה טקסט לדיבור באמצעות הספרייה `gTTS` ומנגנת אותו בערוץ הקולי.

**Parameters**:
- `text` (str): הטקסט להמרה לדיבור.
- `voice_channel` (discord.VoiceChannel): ערוץ הקול שבו יש לנגן את הדיבור.

**Returns**:
- `None`: פונקציה זו אינה מחזירה ערך.

**Raises**:
- `discord.ClientException`: מועלה אם הבוט אינו מחובר לערוץ קולי.
- `discord.errors.ConnectionClosed`: מועלה אם החיבור לערוץ הקולי נסגר.
- `Exception`: מועלה אם מתרחשת שגיאה כללית.

## אירועים

### `on_ready`

**Description**: מטפל באירוע כאשר הבוט מוכן ומוגדר. מדפיס הודעת אישור על פעילות הבוט.

**Parameters**:
- `None`

**Returns**:
- `None`

**Raises**:
- `None`

### `on_message`

**Description**: מטפל בהודעות נכנסות. מתעלם מהודעות של הבוט עצמו. אם ההודעה כוללת קובץ אודיו, הפונקציה תזהה את הטקסט בו. אם המשתמש נמצא בערוץ קולי, הפונקציה תמיר את הטקסט לדיבור ותשמיע אותו בערוץ.

**Parameters**:
- `message` (discord.Message): ההודעה הנכנסת.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך עיבוד ההודעה.

## פקודות

### `hi`

**Description**: פקודה השולחת הודעת פתיחה למשתמש.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.

**Returns**:
- `None`

**Raises**:
- `None`

### `join`

**Description**: פקודה המחברת את הבוט לערוץ הקולי שבו המשתמש נמצא.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.

**Returns**:
- `None`

**Raises**:
- `discord.ClientException`: מועלה אם הבוט כבר מחובר לערוץ קולי.

### `leave`

**Description**: פקודה המנתקת את הבוט מהערוץ הקולי.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.

**Returns**:
- `None`

**Raises**:
- `discord.ClientException`: מועלה אם הבוט אינו מחובר לערוץ קולי.

### `train`

**Description**: פקודה המאמנת את המודל על סמך הנתונים שהועברו על ידי המשתמש, שיכולים להיות קובץ או טקסט.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `data` (str, optional): הנתונים לאימון. ברירת מחדל: `None`.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך אימון המודל.

### `test`

**Description**: פקודה הבודקת את המודל על סמך הנתונים שהועברו על ידי המשתמש, שיכולים להיות קובץ או טקסט.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `data` (str, optional): הנתונים לבדיקה. ברירת מחדל: `None`.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך בדיקת המודל.

### `archive`

**Description**: פקודה המארכבת קבצים בתיקייה ספציפית.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `path` (str): נתיב התיקייה לארכוב.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך ארכוב הקבצים.

### `select_dataset`

**Description**: פקודה לבחירת מאגר נתונים לאימון המודל.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `dataset_name` (str): שם מאגר הנתונים לבחירה.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך בחירת מאגר הנתונים.

### `instruction`

**Description**: פקודה השולחת הוראות מקובץ חיצוני.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך שליחת ההוראות.

### `correct`

**Description**: פקודה המאפשרת למשתמש לתקן הודעה קודמת של הבוט.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `message_id` (int): מזהה ההודעה לתיקון.
- `corrected_text` (str): הטקסט המתוקן.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך תיקון ההודעה.

### `feedback`

**Description**: פקודה המאפשרת למשתמש לשלוח משוב על ביצועי הבוט.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `feedback_text` (str): המשוב שהמשתמש מעוניין לשלוח.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך שליחת המשוב.

### `getfile`

**Description**: פקודה השולחת קובץ מנתיב ספציפי.

**Parameters**:
- `ctx` (discord.ext.commands.Context): הקשר של הפקודה.
- `file_path` (str): נתיב הקובץ לשליחה.

**Returns**:
- `None`

**Raises**:
- `Exception`: מועלה אם מתרחשת שגיאה במהלך שליחת הקובץ.