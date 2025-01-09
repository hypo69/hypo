# `main.py`

## סקירה כללית

קובץ זה מגדיר את נקודות הקצה של ה-API עבור משחק צ'אט, כולל אימות, שליחת הודעות צ'אט וקבלת כללי המשחק וקבצי לוקליזציה.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [מחלקות](#מחלקות)
- [פונקציות](#פונקציות)
    - [`get_current_user`](#get_current_user)
    - [`login`](#login)
    - [`logout`](#logout)
    - [`root`](#root)
    - [`chat`](#chat)
    - [`get_locale_file`](#get_locale_file)
    - [`locales`](#locales)
    - [`rules`](#rules)

## מחלקות

### `ChatRequest`

**Description**: מודל Pydantic לייצוג בקשת צ'אט.

**Fields**:
- `message` (str): ההודעה שהמשתמש שולח.

## פונקציות

### `get_current_user`

```python
async def get_current_user(session_id: Annotated[str | None, Cookie()] = None) -> str | None:
    """
    Args:
        session_id (Annotated[str | None, Cookie()], optional): מזהה סשן המאוחסן בקובץ Cookie. ברירת מחדל: `None`.

    Returns:
        str | None: שם המשתמש אם הסשן תקף, אחרת `None`.
    """
```

**Description**: מקבל את המשתמש הנוכחי ממזהה סשן המאוחסן בקובץ cookie. אם הסשן לא תקף או שפג תוקפו, הפונקציה תחזיר `None`.

**Parameters**:
- `session_id` (Annotated[str | None, Cookie()], optional): מזהה הסשן, שנמצא בקובץ Cookie. ברירת מחדל: `None`.

**Returns**:
- `str | None`: שם המשתמש אם הסשן תקף, אחרת `None`.

### `login`

```python
async def login(username: str = Form(), password: str = Form()) -> RedirectResponse:
    """
    Args:
        username (str, optional): שם המשתמש שנשלח בטופס. ברירת מחדל: `Form()`.
        password (str, optional): הסיסמה שנשלחה בטופס. ברירת מחדל: `Form()`.

    Returns:
        RedirectResponse: תגובה עם הפנייה מחדש לדף הבית לאחר כניסה מוצלחת.

    Raises:
        HTTPException: אם אימות הכניסה נכשל עם קוד סטטוס 401.
    """
```

**Description**: מבצע אימות כניסה. אם האימות מצליח, נוצר מזהה סשן חדש, והמשתמש מופנה לדף הבית.

**Parameters**:
- `username` (str, optional): שם המשתמש שנשלח בטופס. ברירת מחדל: `Form()`.
- `password` (str, optional): הסיסמה שנשלחה בטופס. ברירת מחדל: `Form()`.

**Returns**:
- `RedirectResponse`: תגובה עם הפנייה מחדש לדף הבית לאחר כניסה מוצלחת.

**Raises**:
- `HTTPException`: אם אימות הכניסה נכשל עם קוד סטטוס 401.

### `logout`

```python
async def logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse:
    """
    Args:
        session_id (Annotated[str | None, Cookie()], optional): מזהה הסשן שנמצא בקובץ Cookie. ברירת מחדל: `None`.

    Returns:
        JSONResponse: תגובת JSON המציינת שהמשתמש התנתק בהצלחה.

    Raises:
        HTTPException: אם הסשן אינו תקף.
    """
```

**Description**: מבצע פעולת יציאה. מסיר את מזהה הסשן מהנתונים ומוחק את קובץ ה-Cookie.

**Parameters**:
- `session_id` (Annotated[str | None, Cookie()], optional): מזהה הסשן שנמצא בקובץ Cookie. ברירת מחדל: `None`.

**Returns**:
- `JSONResponse`: תגובת JSON המציינת שהמשתמש התנתק בהצלחה.

**Raises**:
- `HTTPException`: אם הסשן אינו תקף.

### `root`

```python
async def root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse:
    """
    Args:
        request (Request): אובייקט הבקשה של FastAPI.
        current_user (str | None, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

    Returns:
        HTMLResponse: תגובת HTML, מציג את index.html אם המשתמש מחובר, אחרת את login.html.

    Raises:
        HTTPException: אם קובץ index.html או login.html לא נמצא.
    """
```

**Description**: משרת את קובץ index.html הראשי עבור האפליקציה, או את login.html אם המשתמש אינו מחובר.

**Parameters**:
- `request` (Request): אובייקט הבקשה של FastAPI.
- `current_user` (str | None, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

**Returns**:
- `HTMLResponse`: תגובת HTML, מציג את index.html אם המשתמש מחובר, אחרת את login.html.

**Raises**:
- `HTTPException`: אם קובץ index.html או login.html לא נמצא.

### `chat`

```python
async def chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]:
    """
    Args:
        request (ChatRequest): מודל בקשת צ'אט המכיל את הודעת המשתמש.
        current_user (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

    Returns:
        dict[str, Any]: תגובה ממודל הצ'אט.

    Raises:
        HTTPException: אם מתרחשת שגיאה בעת עיבוד בקשת הצ'אט.
    """
```

**Description**: מטפל בבקשות צ'אט ומחזיר תגובה מהבוט.

**Parameters**:
- `request` (ChatRequest): מודל בקשת צ'אט המכיל את הודעת המשתמש.
- `current_user` (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

**Returns**:
- `dict[str, Any]`: תגובה ממודל הצ'אט.

**Raises**:
- `HTTPException`: אם מתרחשת שגיאה בעת עיבוד בקשת הצ'אט.

### `get_locale_file`

```python
def get_locale_file(lang: str) -> dict[str, str]:
    """
    Args:
        lang (str): שפת הלוקליזציה.

    Returns:
        dict[str, str]: מילון של מחרוזות הלוקליזציה.

    Raises:
        HTTPException: אם קובץ הלוקליזציה לא נמצא או לא תקין.
    """
```

**Description**: קורא קובץ לוקליזציה בהתבסס על השפה הנתונה.

**Parameters**:
- `lang` (str): שפת הלוקליזציה.

**Returns**:
- `dict[str, str]`: מילון של מחרוזות הלוקליזציה.

**Raises**:
- `HTTPException`: אם קובץ הלוקליזציה לא נמצא או לא תקין.

### `locales`

```python
async def locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]:
    """
    Args:
        lang (str): שפת הלוקליזציה.
        current_user (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

    Returns:
        dict[str, str]: מילון של מחרוזות הלוקליזציה.
    """
```

**Description**: נקודת קצה לאחזור קבצי לוקליזציה.

**Parameters**:
- `lang` (str): שפת הלוקליזציה.
- `current_user` (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

**Returns**:
- `dict[str, str]`: מילון של מחרוזות הלוקליזציה.

### `rules`

```python
async def rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]:
    """
    Args:
        current_user (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

    Returns:
        list[dict[str, str]]: רשימה של שמות קבצי הכללים.
    """
```

**Description**: מחזיר רשימה של שמות קבצי הכללים.

**Parameters**:
- `current_user` (str, optional): שם המשתמש הנוכחי, מאוחזר באמצעות `get_current_user`. ברירת מחדל: `Depends(get_current_user)`.

**Returns**:
- `list[dict[str, str]]`: רשימה של שמות קבצי הכללים.