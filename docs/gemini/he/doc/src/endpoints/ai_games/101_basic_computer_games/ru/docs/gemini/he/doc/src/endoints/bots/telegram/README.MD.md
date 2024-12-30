# מודול Telegram Bot

## סקירה כללית

הבוט מבצע מספר פונקציות הקשורות לטיפול בפקודות, עיבוד הודעות קוליות ואינטראקציה עם משתמשים בטלגרם.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [פונקציות ופקודות עיקריות של הבוט](#פונקציות-ופקודות-עיקריות-של-הבוט)
- [מודולים וספריות עיקריים](#מודולים-וספריות-עיקריים)
- [מחלקה ושיטות](#מחלקה-ושיטות)
- [פונקציה ראשית](#פונקציה-ראשית)

## פונקציות ופקודות עיקריות של הבוט

1. **אתחול הבוט:**
   - הבוט מאותחל עם אסימון, המשמש לאימות הבוט באמצעות Telegram API.

2. **פקודות:**
   - `/start`: שולח הודעת ברוכים הבאים למשתמש.
   - `/help`: מספק רשימה של פקודות זמינות.
   - `/sendpdf`: שולח קובץ PDF למשתמש.

3. **טיפול בהודעות:**
   - הבוט מעבד הודעות טקסט נכנסות, הודעות קוליות וקבצי מסמכים.
   - עבור הודעות קוליות, הבוט מתמלל את השמע (כרגע, זוהי פונקציית מציין מיקום).
   - עבור קבצי מסמכים, הבוט קורא את תוכן מסמך הטקסט.

4. **טיפול בהודעות קוליות:**
   - הבוט מוריד את קובץ ההודעה הקולית, שומר אותו באופן מקומי ומנסה לתמלל אותו באמצעות שירות זיהוי דיבור (כרגע, זוהי פונקציית מציין מיקום).

5. **טיפול במסמכים:**
   - הבוט מוריד את קובץ המסמך, שומר אותו באופן מקומי וקורא את תוכן מסמך הטקסט.

6. **טיפול בהודעות טקסט:**
   - הבוט פשוט מחזיר את הטקסט שהתקבל מהמשתמש.

## מודולים וספריות עיקריים

- `python-telegram-bot`: הספרייה הראשית ליצירת בוטים של טלגרם.
- `pathlib`: לעבודה עם נתיבי קבצים.
- `tempfile`: ליצירת קבצים זמניים.
- `asyncio`: לביצוע משימות אסינכרוניות.
- `requests`: להורדת קבצים.
- `src.utils.convertors.tts`: לזיהוי דיבור והמרת טקסט לדיבור.
- `src.utils.file`: לקריאת קבצי טקסט.

## מחלקה ושיטות

### `TelegramBot`

**תיאור**: מחלקה המייצגת את בוט הטלגרם.

**Methods**:
   - `__init__(self, token: str)`
     - **Description**: מאתחל את הבוט עם אסימון ורושם מטפלים.
     - **Parameters**:
       - `token` (str): אסימון הבוט.
   - `register_handlers(self)`
     - **Description**: רושם מטפלים בפקודות ובהודעות.
   - `start(self, update: Update, context: CallbackContext)`
      - **Description**: מטפל בפקודה `/start`.
      - **Parameters**:
          - `update` (Update): אובייקט העדכון מה-Telegram API.
          - `context` (CallbackContext): אובייקט ההקשר מה-Telegram API.
   - `help_command(self, update: Update, context: CallbackContext)`
     - **Description**: מטפל בפקודה `/help`.
      - **Parameters**:
          - `update` (Update): אובייקט העדכון מה-Telegram API.
          - `context` (CallbackContext): אובייקט ההקשר מה-Telegram API.
   - `send_pdf(self, pdf_file: str | Path)`
      - **Description**: מטפל בפקודה `/sendpdf` כדי לשלוח קובץ PDF.
      - **Parameters**:
        - `pdf_file` (str | Path): נתיב לקובץ PDF.
   - `handle_voice(self, update: Update, context: CallbackContext)`
      - **Description**: מטפל בהודעות קוליות ומתמלל את השמע.
      - **Parameters**:
          - `update` (Update): אובייקט העדכון מה-Telegram API.
          - `context` (CallbackContext): אובייקט ההקשר מה-Telegram API.
   - `transcribe_voice(self, file_path: Path) -> str`
      - **Description**: מתמלל הודעות קוליות (פונקציית מציין מיקום).
      - **Parameters**:
        - `file_path` (Path): נתיב לקובץ הקול.
      - **Returns**:
        - `str`: הטקסט המתומלל.
   - `handle_document(self, update: Update, context: CallbackContext) -> str`
      - **Description**: מטפל בקבצי מסמכים וקורא את התוכן שלהם.
        - **Parameters**:
          - `update` (Update): אובייקט העדכון מה-Telegram API.
          - `context` (CallbackContext): אובייקט ההקשר מה-Telegram API.
      - **Returns**:
        - `str`: תוכן המסמך.
   - `handle_message(self, update: Update, context: CallbackContext) -> str`
      - **Description**: מטפל בהודעות טקסט ומחזיר את הטקסט שהתקבל.
        - **Parameters**:
          - `update` (Update): אובייקט העדכון מה-Telegram API.
          - `context` (CallbackContext): אובייקט ההקשר מה-Telegram API.
      - **Returns**:
        - `str`: הטקסט שהתקבל מהמשתמש.

## פונקציה ראשית

- `main()`: מאתחל את הבוט, רושם מטפלים בפקודות והודעות, ומפעיל את הבוט באמצעות `run_polling()`.