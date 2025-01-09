# ניתוח קוד - משחקי מחשב בסיסיים

## <algorithm>

להלן תיאור צעד אחר צעד של זרימת הקוד, כולל דוגמאות לכל בלוק לוגי:

1.  **ייבוא ספריות:**
    *   הקוד מייבא את הספרייה `google.generativeai` באמצעות השם `genai`.
    *   דוגמה: `import google.generativeai as genai`
2.  **הגדרת המחלקה `GoogleGenerativeAI`:**
    *   המחלקת מספקת אינטראקציה עם מודלים של Google Generative AI.
    *   היא כוללת את המשתנים `MODELS` המכילים שמות של מודלים זמינים.
    *   דוגמה:
        ```python
         class GoogleGenerativeAI:
            MODELS = [
                'gemini-1.5-flash-8b',
                'gemini-2-13b',
                'gemini-3-20b'
            ]
        ```
3.  **אתחול המחלקה `GoogleGenerativeAI` (`__init__`):**
    *   פונקציית האתחול מקבלת מפתח API, הוראות מערכת ושם מודל כפרמטרים.
    *   היא מגדירה את מפתח ה-API, את שם המודל, קובעת את תצורת הספריה ומייצרת מודל עם הוראות המערכת.
    *   דוגמה:
        ```python
        def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2-13b'):
            self.api_key = api_key
            self.model_name = model_name
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)
        ```
4.  **שיטת `ask` במחלקה `GoogleGenerativeAI`:**
    *   שיטה זו מקבלת מחרוזת שאילתה, שולחת אותה למודל ומחזירה את התגובה.
    *   היא כוללת טיפול בשגיאות להחזרת הודעת שגיאה אם מתרחשת חריגה כלשהי.
    *   דוגמה:
        ```python
        def ask(self, q: str) -> str:
            try:
                response = self.model.generate_content(q)
                return response.text
            except Exception as ex:
                return f'Error: {str(ex)}'
        ```
5.  **הגדרת הוראות מערכת:**
    *   שתי מחרוזות המגדירות את הוראות המערכת עבור המשחקים השונים ("קלט-פלט" ו"מחשב 10 סנט").
    *   דוגמה:
        ```python
        system_instruction_input_output = """
        אתה מנוע משחקים למשחק המתמטיקה "קלט-פלט".
        """
        system_instruction_binary = """
        אתה סימולטור "מחשב 10 סנט" ללמד ילדים על מערכת הבינארית.
        """
        ```
6.  **אתחול משחקים:**
    *   מוגדרים משתנים `api_key`.
    *   נוצרים אובייקטים של `GoogleGenerativeAI` עבור כל משחק, תוך שימוש במפתח API ובהוראות המערכת המתאימות.
    *   דוגמה:
        ```python
        api_key = "YOUR_API_KEY" # יש להחליף במפתח ה-API האמיתי
        input_output_game = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction_input_output)
        binary_computer = GoogleGenerativeAI(api_key=api_key, system_instruction=system_instruction_binary)
        ```
7.  **שימוש לדוגמא:**
    *   מדפיס כותרת עבור כל משחק.
    *   מבצע שיחות `ask` למודלים שונים עם קלטים שונים.
    *   מדפיס את התוצאות.
    *   דוגמה:
        ```python
        print("משחק קלט-פלט:")
        print(input_output_game.ask("קלט: 7"))
        print(input_output_game.ask("קלט: 12"))
        print(input_output_game.ask("הגדר מכונה x / 2"))
        print(input_output_game.ask("קלט: 12"))
        print("\nמחשב 10 סנט:")
        print(binary_computer.ask("עשרוני: 6"))
        print(binary_computer.ask("מנורות: 0111"))
        print(binary_computer.ask("הסבר איך 13"))
        ```
**זרימת נתונים:**

*   נתונים זורמים מהקוד אל מודל ה-Gemini דרך שיטת `ask`.
*   מודל ה-Gemini מעבד את הנתונים בהתאם להוראות המערכת.
*   התגובה מהמודל מוחזרת לקוד ומוצגת למשתמש.

## <mermaid>

```mermaid
flowchart TD
    A[Start] --> B(Import google.generativeai as genai);
    B --> C{class GoogleGenerativeAI};
    C --> D( __init__(api_key, system_instruction, model_name));
    D --> E(genai.configure(api_key));
    E --> F(self.model = genai.GenerativeModel(model_name, system_instruction));
    C --> G(ask(q));
    G --> H{try};
    H -- Yes --> I(response = self.model.generate_content(q));
    I --> J(return response.text);
    H -- No --> K(return f'Error: {str(ex)}');
    J --> L[end];
    K --> L;
    F --> G
    C --> M(system_instruction_input_output);
    C --> N(system_instruction_binary);
    M --> O(api_key = "YOUR_API_KEY");
    N --> O;
    O --> P(input_output_game = GoogleGenerativeAI(api_key, system_instruction_input_output));
     O --> Q(binary_computer = GoogleGenerativeAI(api_key, system_instruction_binary));
    P --> R(input_output_game.ask("קלט: 7"));
    Q --> S(binary_computer.ask("עשרוני: 6"));
    R --> T[print];
    S --> T;
    T --> L;
    
     subgraph GoogleGenerativeAI
    D
    G
    F
    end
     subgraph Main Script
        M
        N
        O
        P
        Q
        R
        S
        T
     end


```
### הסבר תרשים Mermaid:
* **ייבוא:**
  *  `import google.generativeai as genai`: הספרייה `google.generativeai` מייובאת כדי לאפשר אינטראקציה עם מודלים של Gemini.
* **מחלקת GoogleGenerativeAI:**
    *  `class GoogleGenerativeAI`: הגדרת המחלקה שאחראית על האינטראקציה עם מודל ה-Gemini.
    *  `__init__(api_key, system_instruction, model_name)`: פונקציית האתחול של המחלקה, אשר מקבלת את מפתח ה-API, את הוראות המערכת ואת שם המודל.
    *   `genai.configure(api_key)`: מגדירה את מפתח ה-API לספריית `google.generativeai`.
    *   `self.model = genai.GenerativeModel(model_name, system_instruction)`: יוצרת מופע של המודל עם השם וההוראות שסופקו.
   *   `ask(q)`: שיטה השולחת שאילתה למודל ומחזירה את התגובה.
     * `try`: בלוק לטיפול בחריגות.
     *  `response = self.model.generate_content(q)`: שולח את השאילתה `q` למודל ומקבל את התגובה.
     * `return response.text`: אם השאילתה עברה בהצלחה, התגובה הטקסטואלית מוחזרת.
      * `return f'Error: {str(ex)}'`: אם מתרחשת שגיאה, מוחזרת הודעת שגיאה.
*   **הוראות מערכת:**
    *   `system_instruction_input_output`: מחרוזת המכילה את הוראות המערכת למשחק "קלט-פלט".
    *  `system_instruction_binary`: מחרוזת המכילה את הוראות המערכת למשחק "מחשב 10 סנט".
*  **אתחול משחקים:**
    *   `api_key = "YOUR_API_KEY"`: משתנה המחזיק את מפתח ה-API של המשתמש. יש להחליף `"YOUR_API_KEY"` במפתח ה-API האמיתי.
    *   `input_output_game = GoogleGenerativeAI(api_key, system_instruction_input_output)`: יצירת מופע של המחלקה `GoogleGenerativeAI` עבור משחק ה"קלט-פלט".
    *    `binary_computer = GoogleGenerativeAI(api_key, system_instruction_binary)`: יצירת מופע של המחלקה `GoogleGenerativeAI` עבור משחק ה"מחשב 10 סנט".
*   **שימוש לדוגמה:**
    *   `input_output_game.ask("קלט: 7")`: קריאה לשיטת `ask` של משחק ה"קלט-פלט" עם הקלט `"קלט: 7"`.
    *   `binary_computer.ask("עשרוני: 6")`: קריאה לשיטת `ask` של משחק "מחשב 10 סנט" עם הקלט `"עשרוני: 6"`.
    *   `print`: פונקציה המדפיסה את התוצאה שחזרה משיטת ה-ask.
*   **סוף**:
    *  `end`: מציין את סוף התהליך.

## <explanation>

### ייבוא
*   `import google.generativeai as genai`: ייבוא הספרייה `google.generativeai` מאפשר אינטראקציה עם מודלים של Google Gemini. הספרייה הזו מספקת כלים לביצוע שאילתות למודלים וקבלת תגובות.

### מחלקות
*   **`GoogleGenerativeAI`**:
    *   **תפקיד**: המחלקה מאפשרת אינטראקציה עם מודלים של Google Gemini. היא מנהלת את תהליך ההגדרה, השאילתות וקבלת התגובות מהמודל.
    *   **מאפיינים**:
        *   `MODELS`: רשימה של שמות מודלים זמינים של Gemini.
        *   `api_key`: מפתח API לגישה לשירות Gemini.
        *   `system_instruction`: הוראה (פרומפט) למודל, המגדירה את תפקידו והתנהגותו.
        *   `model_name`: שם המודל בו משתמשים.
        *   `model`: מופע של מודל Gemini.
    *   **שיטות**:
        *   `__init__(self, api_key, system_instruction, model_name='gemini-2-13b')`:
            *   **פרמטרים**: מקבל מפתח API, הוראות מערכת, ושם מודל (אופציונלי, ברירת מחדל `gemini-2-13b`).
            *   **ערך מוחזר**: אין.
            *   **מטרה**: מאתחל את המחלקה, קובע את תצורת הגישה למודל Gemini באמצעות מפתח ה-API שסופק, ויוצר מופע של המודל עם ההוראות שניתנו.
            *   **דוגמה**:
                ```python
                input_output_game = GoogleGenerativeAI(api_key="YOUR_API_KEY", system_instruction=system_instruction_input_output)
                ```
        *   `ask(self, q)`:
            *   **פרמטרים**: מקבל מחרוזת שאילתה `q`.
            *   **ערך מוחזר**: מחזיר מחרוזת תגובה מהמודל או הודעת שגיאה.
            *   **מטרה**: שולח את השאילתה למודל Gemini ומחזיר את התגובה הטקסטואלית. מטפל בחריגות על ידי החזרת הודעת שגיאה אם מתרחשת בעיה כלשהי.
            *   **דוגמה**:
                ```python
                response = input_output_game.ask("קלט: 5")
                print(response) # פלט: 'פלט: 8, מכונה +3'
                ```
*   **אינטראקציה:** המחלקה `GoogleGenerativeAI` מתוכננת לעבוד עם ספריית `google.generativeai` כדי לאפשר תקשורת עם מודלים שונים של Gemini. היא משמשת כממשק פשוט לשליחת שאילתות וקבלת תשובות.

### פונקציות

*   בנוסף לשיטות של המחלקה `GoogleGenerativeAI`, בקוד לא מוגדרות פונקציות נוספות.

### משתנים
*   `MODELS`: רשימה סטטית של שמות מודלים זמינים של Gemini (במחלקת `GoogleGenerativeAI`).
*   `api_key`: מחרוזת המכילה מפתח API לגישה למודל Gemini.
*   `system_instruction_input_output`: מחרוזת המכילה את הוראות המערכת למשחק "קלט-פלט" (פרומפט).
*   `system_instruction_binary`: מחרוזת המכילה את הוראות המערכת למשחק "מחשב 10 סנט" (פרומפט).
*   `input_output_game`: מופע של המחלקה `GoogleGenerativeAI` המשמש לניהול משחק ה"קלט-פלט".
*   `binary_computer`: מופע של המחלקה `GoogleGenerativeAI` המשמש לניהול משחק "מחשב 10 סנט".
*   `q`: משתנה מקומי בשיטה `ask` המשמש לאחסון השאילתה (טקסט).
*   `response`: משתנה מקומי בשיטה `ask` לאחסון התגובה ממודל Gemini.
*   `ex`: משתנה מקומי בשיטה `ask` לאחסון מידע על חריגה (שגיאה).

### בעיות אפשריות ואזורי שיפור
1.  **טיפול במפתחות API:** מפתחות API מוטמעים ישירות בקוד, דבר שאינו מומלץ. יש לשקול שימוש במשתני סביבה או מערכת ניהול סודות כדי לנהל מפתחות API.
2.  **הגדרת מודל קשיחה:** הקוד משתמש בשם מודל קבוע (ברירת מחדל `gemini-2-13b`). מומלץ לאפשר למשתמש לבחור את שם המודל או להגדיר את שם המודל כמשתנה סביבה.
3.  **טיפול שגיאות פשוט:** טיפול השגיאות בשיטת `ask` פשוט יחסית. יש לשקול טיפול מפורט יותר בחריגות, כמו שגיאות רשת או שגיאות ספציפיות מ-API של Gemini, ולהוסיף לוגים.
4.  **הפרדת לוגיקה עסקית מהתצוגה:**  הדפסת התוצאות מתבצעת ישירות בסקריפט. רצוי להפריד את הלוגיקה של משחקים מהלוגיקה של הצגת נתונים (לדוגמא, באמצעות פונקציות נפרדות להדפסה).
5.  **אפשרות הרחבה:** ניתן להוסיף תמיכה למודלים נוספים של Gemini או לסוגי משחקים נוספים בקלות על ידי שינוי הוראות המערכת.

### שרשרת קשרים עם חלקים אחרים בפרויקט
*   הקוד מתקשר בעיקר עם ספריית `google.generativeai` לצורך שליחת שאילתות למודלים של Gemini.
*   הוראות המערכת מגדירות את ההתנהגות של מודלים Gemini והן תלויות בסוג המשחק.
*   הקוד אינו תלוי ישירות בחלקים אחרים בפרויקט, אך יכול להתקשר עם רכיבים נוספים אם נדרש, לדוגמא, פונקציות שקולטות את הקלט מהמשתמש ומציגות את הפלט בצורה יפה יותר.