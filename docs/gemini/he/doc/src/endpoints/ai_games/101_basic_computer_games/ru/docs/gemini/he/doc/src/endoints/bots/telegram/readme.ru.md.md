# `src.endpoints.bots.telegram`

## סקירה כללית

מודול זה מיישם בוט טלגרם עם פונקציונליות לטיפול בפקודות, הודעות קוליות ואינטראקציות עם משתמשים. הוא משתמש בספריית `python-telegram-bot` כדי לספק אינטראקציה עם ה-API של טלגרם, יחד עם ספריות אחרות כמו `pathlib`, `tempfile`, `asyncio` ו- `requests` כדי להתמודד עם תהליכים שונים. הוא גם משתמש בספרייה מותאמת אישית `src.utils` לסיוע בהמרות קוליות לטקסט וקריאת קבצים.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [מחלקות](#מחלקות)
    - [`TelegramBot`](#telegrambot)
- [פונקציות](#פונקציות)
    - [`main`](#main)

## מחלקות

### `TelegramBot`

**תיאור**: מחלקה זו מגדירה את בוט הטלגרם, ומטפלת בפקודות, הודעות ומענה.

**Methods**:

- [`__init__`](#__init__)
- [`register_handlers`](#register_handlers)
- [`start`](#start)
- [`help_command`](#help_command)
- [`send_pdf`](#send_pdf)
- [`handle_voice`](#handle_voice)
- [`transcribe_voice`](#transcribe_voice)
- [`handle_document`](#handle_document)
- [`handle_message`](#handle_message)

#### `__init__`

```python
def __init__(self, token: str) -> None:
    """
    Args:
        token (str): אסימון בוט הטלגרם.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: מאתחל את מופע ה-`TelegramBot` עם האסימון שסופק.

**Parameters**:
- `token` (str): אסימון בוט הטלגרם.

**Returns**:
- `None`: אין ערך מוחזר.

#### `register_handlers`

```python
def register_handlers(self) -> None:
    """
    Args:
        self: מופע המחלקה.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: רושם את כל המטפלים עבור פקודות והודעות.

**Parameters**:
- `self`: מופע המחלקה.

**Returns**:
- `None`: אין ערך מוחזר.

#### `start`

```python
def start(self, update: Update, context: CallbackContext) -> None:
    """
    Args:
        update (Update): אובייקט העדכון.
        context (CallbackContext): אובייקט ההקשר.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: מטפל בפקודה `/start`, ומספק הודעת ברוכים הבאים.

**Parameters**:
- `update` (Update): אובייקט העדכון.
- `context` (CallbackContext): אובייקט ההקשר.

**Returns**:
- `None`: אין ערך מוחזר.

#### `help_command`

```python
def help_command(self, update: Update, context: CallbackContext) -> None:
    """
    Args:
        update (Update): אובייקט העדכון.
        context (CallbackContext): אובייקט ההקשר.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: מטפל בפקודה `/help`, ומספק רשימה של פקודות זמינות.

**Parameters**:
- `update` (Update): אובייקט העדכון.
- `context` (CallbackContext): אובייקט ההקשר.

**Returns**:
- `None`: אין ערך מוחזר.

#### `send_pdf`

```python
def send_pdf(self, pdf_file: str | Path) -> None:
    """
    Args:
        pdf_file (str | Path): הנתיב לקובץ ה-PDF.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: מטפל בפקודה `/sendpdf` על ידי שליחת קובץ PDF למשתמש.

**Parameters**:
- `pdf_file` (str | Path): הנתיב לקובץ ה-PDF.

**Returns**:
- `None`: אין ערך מוחזר.

#### `handle_voice`

```python
def handle_voice(self, update: Update, context: CallbackContext) -> None:
    """
    Args:
        update (Update): אובייקט העדכון.
        context (CallbackContext): אובייקט ההקשר.

    Returns:
        None: אין ערך מוחזר.
    """
```

**תיאור**: מטפל בהודעות קוליות על ידי הורדת הקובץ וניסיון לתמלל את האודיו.

**Parameters**:
- `update` (Update): אובייקט העדכון.
- `context` (CallbackContext): אובייקט ההקשר.

**Returns**:
- `None`: אין ערך מוחזר.

#### `transcribe_voice`

```python
def transcribe_voice(self, file_path: Path) -> str:
    """
    Args:
        file_path (Path): נתיב לקובץ האודיו.

    Returns:
        str: טקסט מתומלל או הודעת שגיאה.
    """
```

**תיאור**: מתמלל את קובץ האודיו לטקסט, כרגע מוחזרת מחרוזת placeholder.

**Parameters**:
- `file_path` (Path): נתיב לקובץ האודיו.

**Returns**:
- `str`: טקסט מתומלל או הודעת שגיאה.

#### `handle_document`

```python
def handle_document(self, update: Update, context: CallbackContext) -> str:
    """
    Args:
        update (Update): אובייקט העדכון.
        context (CallbackContext): אובייקט ההקשר.

    Returns:
        str: תוכן הקובץ או הודעת שגיאה.
    """
```

**תיאור**: מטפל בקבצי מסמכים, קורא את תוכנם ומחזיר אותו.

**Parameters**:
- `update` (Update): אובייקט העדכון.
- `context` (CallbackContext): אובייקט ההקשר.

**Returns**:
- `str`: תוכן הקובץ או הודעת שגיאה.

#### `handle_message`

```python
def handle_message(self, update: Update, context: CallbackContext) -> str:
    """
    Args:
        update (Update): אובייקט העדכון.
        context (CallbackContext): אובייקט ההקשר.

    Returns:
        str: טקסט ההודעה.
    """
```

**תיאור**: מטפל בהודעות טקסט ומחזיר את הטקסט שהתקבל.

**Parameters**:
- `update` (Update): אובייקט העדכון.
- `context` (CallbackContext): אובייקט ההקשר.

**Returns**:
- `str`: טקסט ההודעה.

## פונקציות

### `main`

```python
def main() -> None:
    """
    Args:
        None: אין פרמטרים.

    Returns:
        None: אין ערך מוחזר.

    Raises:
        telegram.error.InvalidToken: כאשר אסימון בוט הטלגרם אינו תקף.
    """
```

**תיאור**: פונקציית כניסה ראשית, יוזמת ומפעילה את בוט הטלגרם.

**Parameters**:
- `None`: אין פרמטרים.

**Returns**:
- `None`: אין ערך מוחזר.

**Raises**:
- `telegram.error.InvalidToken`: כאשר אסימון בוט הטלגרם אינו תקף.