## <algorithm>

1. **הגדרת משתנים גלובליים:**
   - `base_path`: נתיב בסיס לקבצי המשחק.
     - לדוגמה: `/hypotez/src/endpoints/ai_games/101_basic_computer_games/ru/chat`
   - `locales_path`: נתיב לקבצי שפה (`.json`).
     - לדוגמה: `/hypotez/src/endpoints/ai_games/101_basic_computer_games/ru/chat/html/locales`
   - `_html`: נתיב לתיקיית האפליקציה (`Angular`).
     - לדוגמה: `/hypotez/src/endpoints/ai_games/101_basic_computer_games/ru/chat/html`
2. **אתחול FastAPI:**
   - יצירת מופע של `FastAPI` בשם `app`.
   - הגדרת `CORSMiddleware` כדי לאפשר בקשות ממקורות שונים.
3. **אבטחה (Authentication):**
   - הגדרת משתמשים וסיסמאות בתוך משתנה `USERS`.
     - לדוגמה: `{"user": "password123"}`.
   - `SESSION_DATA` משמש לאחסון נתוני סשן זמניים.
   - `SESSION_COOKIE_NAME` מגדיר את שם העוגייה של הסשן (`session_id`).
   - `SESSION_TTL` מגדיר את משך הזמן של סשן (`1 hour`).
   - `get_current_user`: פונקציה לקבלת משתמש נוכחי לפי `session_id` מהעוגייה.
     - אם הסשן אינו חוקי או פג תוקף, מחזיר `None`.
     - אם הסשן חוקי, מאריך את משך התוקף שלו ומחזיר את שם המשתמש.
   - `login`: נקודת קצה (`/api/login`) לביצוע התחברות.
     - מקבל שם משתמש וסיסמה מתוך הטופס.
     - בודק את זהות המשתמש מול המשתנה `USERS`.
     - אם האימות נכשל, מחזיר שגיאת 401.
     - יוצר `session_id` חדש ומאחסן אותו ב-`SESSION_DATA` עם שם המשתמש וזמן פג תוקף.
     - מגדיר את ה-`session_id` בעוגייה ומחזיר הפניה לכתובת `/`.
   - `logout`: נקודת קצה (`/api/logout`) לביצוע התנתקות.
     - מקבל את ה-`session_id` מהעוגייה.
     - אם ה-`session_id` לא חוקי, מחזיר שגיאת 401.
     - מוחק את הסשן מ-`SESSION_DATA` ומסיר את העוגייה מהדפדפן.
4. **אפליקציה ראשית:**
   - `ChatRequest`: מודל `Pydantic` לייצוג בקשת צ'אט.
     - מכיל שדה `message` (טקסט ההודעה).
   - `model`: משתנה גלובלי המכיל את מודל ה-AI (`GoogleGenerativeAI`) לאחר אתחול.
   - `api_key`: מפתח ה-API עבור Google Gemini (נלקח מ-`gs`).
   - `system_instruction`: מחרוזת להוראות מערכת (לא בשימוש כרגע).
   - `root`: נקודת קצה (`/`) המשמשת להצגת דף האינדקס (`index.html`) או דף ההתחברות (`login.html`) בהתאם למשתמש המחובר.
     - אם המשתמש מחובר (יש `current_user`), קורא את קובץ `index.html` ומחזיר אותו.
     - אם המשתמש אינו מחובר, קורא את קובץ `login.html` ומחזיר אותו.
     - במקרה של שגיאה, נרשמת שגיאה ב-logger ומוחזרת שגיאת HTTP.
   - `chat`: נקודת קצה (`/api/chat`) לטיפול בבקשות צ'אט.
     - אם המודל `model` לא אתחול, יוצר מופע חדש של `GoogleGenerativeAI`.
     - שולח את ההודעה למודל ה-AI ומחזיר את התגובה.
     - במקרה של שגיאה, נרשמת שגיאה ב-logger ומוחזרת שגיאת HTTP.
   - `get_locale_file`: פונקציה לקריאת קובץ שפה (`.json`) לפי שם השפה.
     - קוראת את קובץ ה-JSON ומחזירה מילון של שפה.
     - במקרה של שגיאה, נרשמת שגיאה ב-logger ומוחזרת שגיאת HTTP.
   - `locales`: נקודת קצה (`/locales/{lang}.json`) לשליפת קבצי שפה.
     - קורא את קובץ השפה באמצעות `get_locale_file` ומחזיר אותו.
   - `rules`: נקודת קצה (`/api/rules`) לשליפת רשימת קבצי החוקים.
     - משתמש ב-`recursively_get_file_path` כדי לקבל את כל קבצי החוקים.
     - מחזיר רשימה של שמות הקבצים.
5. **הפעלת שרת מקומי:**
   - אם הקובץ רץ ישירות (`__name__ == "__main__"`), מפעיל את שרת Uvicorn בכתובת `127.0.0.1` ובפורט `8000`.

## <mermaid>

```mermaid
flowchart TD
    subgraph FastAPI Application
        Start[Start] --> BasePath[קביעת נתיב בסיס: <code>base_path</code>]
        BasePath --> LocalesPath[קביעת נתיב שפות: <code>locales_path</code>]
        LocalesPath --> HTMLPath[קביעת נתיב HTML: <code>_html</code>]
        HTMLPath --> FastAPIInit[אתחול FastAPI: <code>app = FastAPI()</code>]
        FastAPIInit --> CORSMiddleware[הגדרת CORS]
        CORSMiddleware --> Auth[אבטחה]
        Auth --> MainApp[אפליקציה ראשית]
        MainApp --> RunServer[הפעלת שרת Uvicorn]
    end
    
    subgraph Auth
        AuthStart[Auth Start] --> USERS[הגדרת משתמשים: <code>USERS</code>]
        USERS --> SessionData[אתחול נתוני סשן: <code>SESSION_DATA</code>]
        SessionData --> SessionCookie[הגדרת עוגייה: <code>SESSION_COOKIE_NAME</code>]
        SessionCookie --> SessionTTL[הגדרת זמן תפוגה לסשן: <code>SESSION_TTL</code>]
        SessionTTL --> GetCurrentUser[פונקציה: <code>get_current_user</code>]
        GetCurrentUser --> LoginEndpoint[נקודת קצה: <code>/api/login</code>]
        LoginEndpoint --> LogoutEndpoint[נקודת קצה: <code>/api/logout</code>]
        LogoutEndpoint --> AuthEnd[Auth End]
    end

    subgraph MainApp
        MainAppStart[MainApp Start] --> ChatRequestModel[מודל: <code>ChatRequest</code>]
        ChatRequestModel --> ModelVar[משתנה גלובלי: <code>model</code>]
        ModelVar --> APIKey[מפתח API: <code>api_key</code>]
        APIKey --> SystemInstruction[הוראות מערכת: <code>system_instruction</code>]
        SystemInstruction --> RootEndpoint[נקודת קצה: <code>/</code>]
        RootEndpoint --> ChatEndpoint[נקודת קצה: <code>/api/chat</code>]
        ChatEndpoint --> GetLocaleFile[פונקציה: <code>get_locale_file</code>]
        GetLocaleFile --> LocalesEndpoint[נקודת קצה: <code>/locales/{lang}.json</code>]
        LocalesEndpoint --> RulesEndpoint[נקודת קצה: <code>/api/rules</code>]
       RulesEndpoint --> MainAppEnd[MainApp End]
    end

    
     subgraph Header
         HeaderStart[Start] --> HeaderModule[<code>header.py</code><br>קביעת שורש הפרויקט]
         HeaderModule --> ImportGS[ייבוא הגדרות גלובליות: <br><code>from src import gs</code>]
         ImportGS --> HeaderEnd[Header End]
    end


    Start --> Header
    AuthEnd --> MainAppStart
```

## <explanation>

### ייבואים (Imports)

*   `from __future__ import annotations`: מאפשר שימוש בהערות טיפוסים (type hints) מסוג forward references.
*   `json`: לטיפול בנתוני JSON.
*   `sys`: לגישה למשתנים ופונקציות ספציפיים למערכת.
*   `pathlib.Path`: לטיפול בנתיבי קבצים בצורה נוחה ואובייקטיבית.
*   `fastapi`: הספרייה המרכזית לבניית ה-API.
    *   `FastAPI`: המחלקה העיקרית ליצירת מופע של אפליקציית FastAPI.
    *   `HTTPException`: מחלקה לשגיאות HTTP.
    *   `status`: קבועים עבור קודי סטטוס HTTP.
    *   `Depends`: לניהול תלויות בין פונקציות.
    *   `Request`: לייצוג בקשת HTTP.
    *   `Form`: לטיפול בנתונים שהתקבלו מטופס.
*   `fastapi.middleware.cors.CORSMiddleware`: מאפשר בקשות ממקורות שונים (Cross-Origin Resource Sharing).
*   `fastapi.responses`: מחלקות לתגובות HTTP שונות (HTMLResponse, JSONResponse, RedirectResponse).
*   `fastapi.staticfiles.StaticFiles`: לטיפול בקבצים סטטיים.
*   `pydantic.BaseModel`: ליצירת מודלים לאימות נתונים.
*   `uvicorn`: שרת ASGI לייצור עבור אפליקציות FastAPI.
*   `typing.Any`: מאפשר לקבוע שמשתנה יכול להכיל כל סוג נתונים.
*   `typing.Annotated`: מאפשר הוספת מטא-דאטה להערות טיפוסים.
*   `fastapi.Cookie`: לטיפול בעוגיות.
*   `datetime`: לטיפול בתאריכים ושעות.
*   `uuid`: ליצירת מזהים ייחודיים.
*   `header`: מודול המכיל את קביעת שורש הפרויקט.
*   `src.gs`: משתנה המכיל הגדרות גלובליות של הפרויקט.
*   `src.logger.logger`: מודול לרישום הודעות (logging).
*   `src.ai.GoogleGenerativeAI`: המחלקה המשמשת לאינטראקציה עם מודל הבינה המלאכותית של Google Gemini.
*  `src.utils.file.recursively_get_file_path`: פונקציה לקבלת נתיבים לקבצים באופן רקורסיבי

### מחלקות (Classes)

*   `ChatRequest(BaseModel)`: מחלקה לייצוג בקשת צ'אט, מכילה שדה `message` (טקסט ההודעה).

### פונקציות (Functions)

*   `get_current_user(session_id: Annotated[str | None, Cookie()] = None) -> str | None`:
    *   **פרמטרים**: `session_id` (אופציונלי) - מזהה הסשן מהעוגייה.
    *   **ערך מוחזר**: `str | None` - שם המשתמש או `None` אם הסשן אינו חוקי.
    *   **מטרה**: מאמת את סשן המשתמש באמצעות ה-`session_id` ומחזיר את שם המשתמש.
    *   **דוגמה**:
        ```python
        current_user = await get_current_user(session_id="some_session_id")
        if current_user:
            print(f"User logged in: {current_user}")
        else:
            print("User not logged in")
        ```
*   `login(username: str = Form(), password: str = Form()) -> RedirectResponse`:
    *   **פרמטרים**: `username` ו-`password` (מחרוזות) - שם משתמש וסיסמה מהטופס.
    *   **ערך מוחזר**: `RedirectResponse` - תגובה המפנה לדף הבית.
    *   **מטרה**: מאמת את פרטי ההתחברות של המשתמש, יוצר סשן ומחזיר הפניה לדף הבית.
    *   **דוגמה**:
        ```python
        # Request (POST /api/login with form data)
        username = "user"
        password = "password123"
        # Response (Redirects to / with session cookie)
        ```
*   `logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse`:
    *   **פרמטרים**: `session_id` (אופציונלי) - מזהה הסשן מהעוגייה.
    *   **ערך מוחזר**: `JSONResponse` - תגובה המציינת שהתנתקות בוצעה בהצלחה.
    *   **מטרה**: מוחק את הסשן הקיים ומוחק את העוגייה מהדפדפן.
    *   **דוגמה**:
        ```python
        # Request (POST /api/logout with session cookie)
        # Response ({"message": "Logout successful"})
        ```
*   `root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse`:
    *   **פרמטרים**: `request` - בקשת ה-HTTP, `current_user` - שם המשתמש המחובר (תלוי ב-`get_current_user`).
    *   **ערך מוחזר**: `HTMLResponse` - תגובה עם תוכן HTML של דף האינדקס או דף ההתחברות.
    *   **מטרה**: מציג את דף הבית של האפליקציה (index.html) אם המשתמש מחובר, או את דף ההתחברות (login.html) אם המשתמש אינו מחובר.
    *   **דוגמה**:
        ```python
        # Request (GET /)
        # Response (index.html if logged in, login.html if logged out)
        ```
*  `chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]`:
    *   **פרמטרים**: `request` - בקשת צ'אט (מכיל את הודעת המשתמש), `current_user` - שם המשתמש המחובר (תלוי ב-`get_current_user`).
    *   **ערך מוחזר**: `dict[str, Any]` - מילון המכיל את תגובת הצ'אט.
    *   **מטרה**: מטפל בבקשות צ'אט, שולח את ההודעה למודל ה-AI ומחזיר את התגובה.
    *   **דוגמה**:
        ```python
        # Request (POST /api/chat with JSON {"message": "Hello"})
        # Response ({"response": "Hi there!"})
        ```
*  `get_locale_file(lang: str) -> dict[str, str]`:
    *  **פרמטרים**: `lang` - קוד השפה (למשל, "ru").
    *  **ערך מוחזר**: `dict[str, str]` - מילון המכיל את המחרוזות המקומיות של השפה.
    *  **מטרה**: קורא את קובץ השפה המתאים ומחזיר את תוכנו כמילון.
    *   **דוגמה**:
        ```python
        locale = get_locale_file(lang="ru")
        print(locale.get("welcome"))  # Prints the Russian translation for "welcome"
        ```
*   `locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]`:
    *   **פרמטרים**: `lang` - קוד השפה (למשל, "ru"), `current_user` - שם המשתמש המחובר (תלוי ב-`get_current_user`).
    *   **ערך מוחזר**: `dict[str, str]` - מילון המכיל את המחרוזות המקומיות של השפה.
    *   **מטרה**: נקודת קצה (API) לשליפת קובץ שפה ספציפי.
    *   **דוגמה**:
        ```python
        # Request (GET /locales/ru.json)
        # Response (json with locale strings for Russian)
        ```
*  `rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]`:
    *   **פרמטרים**: `current_user` - שם המשתמש המחובר (תלוי ב-`get_current_user`).
    *   **ערך מוחזר**: `list[dict[str, str]]` - רשימה של שמות קבצי החוקים.
    *   **מטרה**: נקודת קצה (API) לשליפת רשימה של שמות קבצי החוקים.
    *    **דוגמה**:
        ```python
        # Request (GET /api/rules)
        # Response (list of file names in the rules directory)
        ```
### משתנים (Variables)

*   `base_path`: נתיב בסיס לאפליקציה.
*   `locales_path`: נתיב לקבצי שפה.
*   `_html`: נתיב לתיקיית HTML.
*  `app`: מופע של FastAPI.
*  `USERS`: מילון המכיל שמות משתמש וסיסמאות.
*   `SESSION_DATA`: מילון לאחסון מידע על סשנים.
*   `SESSION_COOKIE_NAME`: שם העוגייה של הסשן.
*   `SESSION_TTL`: משך הזמן של סשן (timedelta).
*   `model`: מופע של GoogleGenerativeAI (מודל AI).
*   `api_key`: מפתח API עבור Google Gemini.
*   `system_instruction`: מחרוזת להוראות מערכת.

### בעיות אפשריות או תחומים לשיפור

1.  **אחסון נתוני סשן**:
    *   `SESSION_DATA` מאחסן נתוני סשן בזיכרון, וזה לא מתאים לסביבת ייצור (production). יש להשתמש במאגר נתונים חיצוני (כמו Redis או DB) לצורך כך.
2.  **אבטחה**:
    *   הסיסמאות מאוחסנות בתוך הקוד (`USERS`) וזה מאוד לא בטוח. יש להשתמש במאגר נתונים מאובטח וטכניקות hashing לסיסמאות.
    *   בנוסף, השרת מוגדר כך שיקבל כל מקור (`allow_origins=["*"]`) - זה לא מומלץ בסביבת ייצור ויש לצמצם את המקורות המותרים.
3.  **טיפול בשגיאות**:
    *  ייתכן וצריך להוסיף טיפול טוב יותר בשגיאות שונות שעלולות להתרחש במהלך פעולת השרת.
4. **ניהול מודל AI**:
     *  האתחול של מודל ה-AI מתרחש רק בפעם הראשונה שמשתמש פונה לנקודת הקצה `/api/chat` , וזה עלול להוביל לעיכוב בזמן התגובה הראשונית. יש לשקול אתחול מוקדם של המודל.
5.  **ארגון הקוד**:
    *   קובץ קוד זה משלב גם את ההגדרות, האבטחה והלוגיקה העסקית באותו מקום. יש לשקול לחלק את הקוד למודולים קטנים יותר כדי לשפר את הקריאות והתחזוקה.
6.  **בדיקות**:
    *   אין בדיקות יחידה או בדיקות אינטגרציה לקוד. יש להוסיף בדיקות כדי להבטיח את תקינות הקוד ולמנוע באגים.

### שרשרת קשרים עם חלקים אחרים בפרויקט

*   **`header.py`**: מגדיר את שורש הפרויקט ומאפשר לייבא משתנים גלובליים (כמו `gs`).
*   **`src.gs`**: מכיל הגדרות גלובליות (כמו נתיבים ומפתחות API) המשמשות בכל הפרויקט.
*   **`src.logger`**: מספק יכולות רישום הודעות, המשמשות לרישום שגיאות ואירועים חשובים.
*   **`src.ai.GoogleGenerativeAI`**: משמש לאינטראקציה עם מודל הבינה המלאכותית של גוגל.
*   **`src.utils.file`**: משמש לקבלת נתיבים לקבצים באופן רקורסיבי.

קובץ זה משמש כנקודת הכניסה לאפליקציית הצ'אט, ומסתמך על מודולים אחרים בפרויקט כדי לתפקד כהלכה.

```mermaid
flowchart TD
    Start --> Header
    Header --> GS
    GS --> Logger
    Logger --> GoogleGenerativeAI
    GoogleGenerativeAI --> FileUtils
    FileUtils --> App
     subgraph Modules
        Header[header.py]
        GS[src.gs]
        Logger[src.logger]
        GoogleGenerativeAI[src.ai.GoogleGenerativeAI]
        FileUtils[src.utils.file]
        App[main.py]
    end