## <algorithm>

הקוד שסופק מדגים את הרעיון של מערכות ספירה שונות, הן מופשטות (כמו מערכת ספירה של פירות) והן ספציפיות (כמו בינארית, טרינרית, הקסהדצימלית).

**1. מערכת ספירה פירות (Fruit Number System):**

*   **התחלה:**
    *   קבלת מחרוזות קלט של פירות (🍎, 🍐, 🍉, 🧺).
*   **`normalize_fruits(fruits)`:**
    *   **ספירת פירות:** סופר את מספר כל פרי במחרוזת הקלט.
    *   **המרת פירות:**
        *   ממיר 3 🍎 ל- 1 🍐.
            *   לדוגמה: אם יש 5 🍎, זה יהפוך ל-1 🍐 ו- 2 🍎 (5 = 1\*3 + 2).
        *   ממיר 5 🍐 ל- 3 🍉.
            *   לדוגמה: אם יש 7 🍐, זה יהפוך ל- 4 🍉 ו- 2 🍐 (7 \* 3 = 21, 21 = 4\*5 + 1, 1%5=1)
        *   ממיר 2 🍉 ל- 1 🧺.
            *   לדוגמה: אם יש 3 🍉, זה יהפוך ל- 1 🧺 ו- 1 🍉 (3 = 1\*2 + 1).
    *   **בניית מחרוזת:** בונה מחרוזת פלט חדשה עם הפירות המומרים, בסדר הבא: 🧺, 🍉, 🍐, 🍎.
*   **`add_fruits(fruits1, fruits2)`:**
    *   **חיבור:** מחבר שתי מחרוזות פירות.
    *   **נורמליזציה:** קורא לפונקציה `normalize_fruits` כדי להמיר את המחרוזת המשולבת לייצוג מינימלי.
*   **`sub_fruits(fruits1, fruits2)`:**
    *   **ספירת פירות:** סופר את מספר כל פרי בכל מחרוזת קלט.
    *   **המרה לכמות כוללת של תפוחים:**
        *   ממיר את כל הפירות למספר שווה ערך של תפוחים (🍎), באמצעות חוקי ההמרה. לדוגמה: 1 🧺 שווה ל-30 🍎, 1 🍉 שווה ל- 5 🍎, ו- 1 🍐 שווה ל- 3 🍎.
    *   **חיסור:** מחסר את הכמות הכוללת של תפוחים של המחרוזת השנייה מהכמות הכוללת של תפוחים של המחרוזת הראשונה.
    *   **בדיקת תוקף:** אם החיסור יוצר מספר שלילי, הפונקציה מחזירה "Невозможно вычесть" (אי אפשר לחסר).
    *   **המרה חזרה לפירות:** אם החיסור אפשרי, המר את הכמות הכוללת של תפוחים בחזרה לפורמט מחרוזת פירות מנורמלת.
*   **דוגמאות:**
    *   קריאה לפונקציות עם מחרוזות פירות שונות ומדפיס את התוצאות.

**2. המרות מערכות ספירה ספציפיות:**

*   **`bin_to_dec(binary)`:**
    *   **התחלה:** קבל מחרוזת בינארית.
    *   **איטרציה:** עבור על ספרות המחרוזת הבינארית מהסוף להתחלה.
    *   **חישוב ערך עשרוני:** אם הספרה היא '1', הוסף 2 בחזקת המיקום הנוכחי לערך העשרוני.
*   **`dec_to_bin(decimal)`:**
    *   **התחלה:** קבל מספר עשרוני.
    *   **מקרה בסיס:** אם המספר העשרוני הוא 0, החזר "0".
    *   **איטרציה:** בצע לולאה כל עוד המספר העשרוני גדול מ-0.
        *   חשב את השארית של חלוקת המספר העשרוני ב-2 והוסף אותה לתחילת המחרוזת הבינארית.
        *   עדכן את המספר העשרוני על ידי חלוקה שלמה ב-2.
*   **`ternary_to_dec(ternary)`:**
    *   **התחלה:** קבל מחרוזת טרנרית (בסיס 3).
    *   **איטרציה:** עבור על ספרות המחרוזת הטרנרית מהסוף להתחלה.
    *   **חישוב ערך עשרוני:** הוסף את הספרה כפול 3 בחזקת המיקום הנוכחי לערך העשרוני.
*   **`dec_to_ternary(decimal)`:**
    *   **התחלה:** קבל מספר עשרוני.
    *   **מקרה בסיס:** אם המספר העשרוני הוא 0, החזר "0".
    *   **איטרציה:** בצע לולאה כל עוד המספר העשרוני גדול מ-0.
        *   חשב את השארית של חלוקת המספר העשרוני ב-3 והוסף אותה לתחילת המחרוזת הטרנרית.
        *   עדכן את המספר העשרוני על ידי חלוקה שלמה ב-3.
*   **`septenary_to_dec(septenary)`:**
    *   **התחלה:** קבל מחרוזת ספטנרית (בסיס 7).
    *   **איטרציה:** עבור על ספרות המחרוזת הספטנרית מהסוף להתחלה.
    *   **חישוב ערך עשרוני:** הוסף את הספרה כפול 7 בחזקת המיקום הנוכחי לערך העשרוני.
*   **`dec_to_septenary(decimal)`:**
    *   **התחלה:** קבל מספר עשרוני.
    *   **מקרה בסיס:** אם המספר העשרוני הוא 0, החזר "0".
    *   **איטרציה:** בצע לולאה כל עוד המספר העשרוני גדול מ-0.
        *   חשב את השארית של חלוקת המספר העשרוני ב-7 והוסף אותה לתחילת המחרוזת הספטנרית.
        *   עדכן את המספר העשרוני על ידי חלוקה שלמה ב-7.
*   **`hex_to_dec(hexadecimal)`:**
    *   **התחלה:** קבל מחרוזת הקסדצימלית.
    *   **איטרציה:** עבור על ספרות המחרוזת ההקסדצימלית מהסוף להתחלה.
    *   **חישוב ערך עשרוני:** אם הספרה היא מספר, הוסף את הספרה כפול 16 בחזקת המיקום הנוכחי לערך העשרוני. אם הספרה היא A-F, הוסף את הערך המתאים (10-15) כפול 16 בחזקת המיקום הנוכחי.
*   **`dec_to_hex(decimal)`:**
    *   **התחלה:** קבל מספר עשרוני.
    *   **מקרה בסיס:** אם המספר העשרוני הוא 0, החזר "0".
    *   **איטרציה:** בצע לולאה כל עוד המספר העשרוני גדול מ-0.
        *   חשב את השארית של חלוקת המספר העשרוני ב-16, מצא את הספרה ההקסדצימלית המתאימה והוסף אותה לתחילת המחרוזת ההקסדצימלית.
        *   עדכן את המספר העשרוני על ידי חלוקה שלמה ב-16.

**3. המרת ספרות רומיות:**

*   **`roman_to_int(roman_str)`:**
    *   **התחלה:** קבל מחרוזת רומית.
    *   **המרת מחרוזות:** המר את כל השילובים של ספרות רומיות שיוצרות מספרי חיסור (IV, IX, XL וכו') לספרות חיבור רגילות (IIII, VIIII, XXXX וכו').
    *   **איטרציה:** עבור על כל תו במחרוזת הרומית.
    *   **חישוב ערך עשרוני:** הוסף את הערך המתאים (ממילון) לערך העשרוני.

**4. המרת קוד מורס:**

*   **`text_to_morse(text)`:**
    *   **התחלה:** קבל מחרוזת טקסט.
    *   **איטרציה:** עבור על כל תו בטקסט.
    *   **מילון קוד מורס:** אם התו נמצא במילון קוד המורס, הוסף את קוד המורס המתאים למחרוזת קוד המורס, ואם לא - הוסף סימן '/' (רווח).
*   **`morse_to_sound(morse_code)`:**
    *   **התחלה:** קבל מחרוזת קוד מורס.
    *   **איטרציה:** עבור על כל תו במחרוזת קוד המורס.
        *   אם התו הוא '.', הפעל צליל קצר.
        *   אם התו הוא '-', הפעל צליל ארוך.
        *   אם התו הוא ' ', המתן לזמן קצר.
        *   אם התו הוא '/', המתן לזמן ארוך יותר.

**5. חישוב יום בשבוע:**

*   **`calculate_day_of_week(start_day, days_passed)`:**
    *   **התחלה:** קבל יום התחלה (0-6) ומספר הימים שחלפו.
    *   **בדיקת קלט:** ודא כי יום ההתחלה הוא מספר שלם בין 0 ל-6, וכי מספר הימים שחלפו הוא מספר.
    *   **חישוב:** מחשב את היום החדש על ידי הוספת מספר הימים שחלפו ליום ההתחלה וחישוב השארית מחלוקה ב-7.
*   **`day_number_to_name(day_number)`:**
    *   **התחלה:** קבל מספר יום בשבוע (0-6).
    *   **מילון:** החזר את שם היום המתאים מתוך מילון של ימי השבוע.

## <mermaid>

```mermaid
flowchart TD
    subgraph Fruit Number System
        A[קבלת מחרוזות פירות] --> B{ספירת פירות}
        B --> C{המרת פירות (🍎->🍐, 🍐->🍉, 🍉->🧺)}
        C --> D[בניית מחרוזת פלט]
        A --> E[פונקציה add_fruits]
        E --> F[חיבור מחרוזות פירות]
        F --> G[קריאה ל- normalize_fruits]
        A --> H[פונקציה sub_fruits]
        H --> I{ספירת פירות}
        I --> J{המרה ל- תפוחים}
        J --> K{חיסור תפוחים}
        K --> L{בדיקה: חיסור אפשרי?}
        L -- כן --> M[המרה חזרה לפירות]
        L -- לא --> N[החזר "Невозможно вычесть"]
    end

    subgraph Number System Conversions
        O[קבלת מחרוזת בינארית] --> P{bin_to_dec}
        P --> Q{איטרציה על ספרות}
        Q --> R{חישוב ערך עשרוני}
        S[קבלת מספר עשרוני] --> T{dec_to_bin}
        T --> U{מקרה בסיס: decimal == 0}
        U -- נכון --> V[החזר "0"]
        U -- לא נכון --> W{איטרציה: decimal > 0}
         W --> X{חישוב שארית ועדכון מחרוזת}
        X--> Y{עדכון decimal}
        Y--> W

        AA[קבלת מחרוזת טרנרית] --> BB{ternary_to_dec}
        BB --> CC{איטרציה על ספרות}
        CC --> DD{חישוב ערך עשרוני}
        EE[קבלת מספר עשרוני] --> FF{dec_to_ternary}
         FF --> GG{מקרה בסיס: decimal == 0}
         GG -- נכון --> HH[החזר "0"]
          GG -- לא נכון --> II{איטרציה: decimal > 0}
         II --> JJ{חישוב שארית ועדכון מחרוזת}
          JJ --> KK{עדכון decimal}
         KK --> II

        LL[קבלת מחרוזת ספטנרית] --> MM{septenary_to_dec}
        MM --> NN{איטרציה על ספרות}
        NN --> OO{חישוב ערך עשרוני}

         PP[קבלת מספר עשרוני] --> QQ{dec_to_septenary}
         QQ --> RR{מקרה בסיס: decimal == 0}
           RR -- נכון --> SS[החזר "0"]
        RR -- לא נכון --> TT{איטרציה: decimal > 0}
        TT --> UU{חישוב שארית ועדכון מחרוזת}
        UU --> VV{עדכון decimal}
        VV --> TT

        WW[קבלת מחרוזת הקסדצימלית] --> XX{hex_to_dec}
        XX --> YY{איטרציה על ספרות}
        YY --> ZZ{חישוב ערך עשרוני}
        AAA[קבלת מספר עשרוני] --> BBB{dec_to_hex}
         BBB --> CCC{מקרה בסיס: decimal == 0}
         CCC -- נכון --> DDD[החזר "0"]
         CCC -- לא נכון --> EEE{איטרציה: decimal > 0}
         EEE --> FFF{חישוב שארית ועדכון מחרוזת}
         FFF --> GGG{עדכון decimal}
         GGG --> EEE

    end

    subgraph Roman Number Conversion
        HHH[קבלת מחרוזת רומית] --> III{roman_to_int}
        III --> JJJ{המרת ספרות חיסור לחיבור}
        JJJ --> KKK{איטרציה על ספרות}
        KKK --> LLL{חישוב ערך עשרוני}
    end
    
   subgraph Morse Code Conversion
        MMM[קבלת טקסט] --> NNN{text_to_morse}
        NNN --> OOO{איטרציה על תווים}
        OOO --> PPP{חיפוש קוד מורס}
        PPP --> QQQ{בניית מחרוזת קוד מורס}
        RRR[קבלת מחרוזת קוד מורס] --> SSS{morse_to_sound}
        SSS --> TTT{איטרציה על תווים}
        TTT --> UUU{הפעלת צליל בהתאם}
     end

    subgraph Day Calculation
    VVV[קבלת יום התחלה ומספר ימים] --> WWW{calculate_day_of_week}
    WWW --> XXX{בדיקת תוקף קלט}
    XXX --> YYY{חישוב יום חדש}
    ZZZ[קבלת מספר יום] --> AAAA{day_number_to_name}
    AAAA --> BBBB[החזר שם יום]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style N fill:#ccf,stroke:#333,stroke-width:2px
    style R fill:#ccf,stroke:#333,stroke-width:2px
    style V fill:#ccf,stroke:#333,stroke-width:2px
    style HH fill:#ccf,stroke:#333,stroke-width:2px
    style SS fill:#ccf,stroke:#333,stroke-width:2px
    style DDD fill:#ccf,stroke:#333,stroke-width:2px
    style LLL fill:#ccf,stroke:#333,stroke-width:2px
    style BBBB fill:#ccf,stroke:#333,stroke-width:2px
    classDef plain fill:#ddd,stroke:#333,stroke-width:2px;
    class B,C,E,F,G,H,I,J,K,L,M,O,P,Q,T,U,W,X,Y,AA,BB,CC,DD,EE,FF,GG,II,JJ,KK,LL,MM,NN,OO,PP,QQ,RR,TT,UU,VV,WW,XX,YY,ZZ,AAA,BBB,CCC,EEE,FFF,GGG,HHH,III,JJJ,KKK,MMM,NNN,OOO,PPP,QQQ,RRR,SSS,TTT,UUU,VVV,WWW,XXX,YYY,ZZZ,AAAA plain;
```

## <explanation>

**ייבואים (Imports):**

*   `import sys`: משמש לקבלת ארגומנטים משורת הפקודה, שמשמשים כדי לקבל קלט עבור פונקציית המרת הספרות הרומיות (roman_to_int).
*   `import time`: משמש עבור השהיות בתוך פונקצית ההשמעת קוד מורס `morse_to_sound`.
*   `import platform`: משמש לזיהוי מערכת ההפעלה של המשתמש, על מנת להשתמש בהפעלת צליל מתאימה `play_sound` (צליל מערכת או צליל חלונות).
*   `import winsound` (בתוך `play_sound`): ספריה ספציפית לחלונות, משמשת להשמעת צליל.
*   `import os` (בתוך `play_sound`): ספריה המאפשרת להשתמש בפקודות מערכת, כדי להשמיע צליל במערכות הפעלה דמויות לינוקס.

**מחלקות (Classes):**

אין מחלקות מוגדרות בקוד זה.

**פונקציות (Functions):**

*   **`normalize_fruits(fruits)`:**
    *   **פרמטרים:** `fruits` (str): מחרוזת המייצגת אוסף של פירות (🍎, 🍐, 🍉, 🧺).
    *   **ערך החזרה:** מחזירה מחרוזת עם כמות מינימלית של פירות (str).
    *   **מטרה:** ממירה מחרוזת פירות לייצוג מינימלי באמצעות חוקי המרה (למשל, 3 🍎 הופכים ל- 1 🍐).
    *   **שימוש:** `normalize_fruits("🍎🍎🍎🍎🍎🍐")` תחזיר `"🍐🍎🍎🍐"`.
*   **`add_fruits(fruits1, fruits2)`:**
    *   **פרמטרים:** `fruits1`, `fruits2` (str): שתי מחרוזות פירות.
    *   **ערך החזרה:** מחזירה מחרוזת המייצגת את סכום הפירות (str).
    *   **מטרה:** מחברת שתי מחרוזות פירות ומנרמלת את התוצאה.
    *   **שימוש:** `add_fruits("🍎🍎", "🍐")` תחזיר `"🍐🍎🍎"`.
*   **`sub_fruits(fruits1, fruits2)`:**
    *   **פרמטרים:** `fruits1`, `fruits2` (str): שתי מחרוזות פירות.
    *   **ערך החזרה:** מחזירה מחרוזת המייצגת את ההפרש בין הפירות (str) או "Невозможно вычесть" אם החיסור לא אפשרי.
    *   **מטרה:** מחסרת את הפירות במחרוזת השנייה מהפירות במחרוזת הראשונה.
    *   **שימוש:** `sub_fruits("🍐🍎🍎","🍎")` תחזיר `"🍐🍎"`.
*   **`bin_to_dec(binary)`:**
    *   **פרמטרים:** `binary` (str): מחרוזת המייצגת מספר בינארי.
    *   **ערך החזרה:** מחזירה את הערך העשרוני של המספר הבינארי (int).
    *   **מטרה:** ממירה מספר בינארי לעשרוני.
    *   **שימוש:** `bin_to_dec("1011")` תחזיר `11`.
*   **`dec_to_bin(decimal)`:**
    *   **פרמטרים:** `decimal` (int): מספר עשרוני.
    *   **ערך החזרה:** מחזירה את הייצוג הבינארי של המספר העשרוני (str).
    *   **מטרה:** ממירה מספר עשרוני לבינארי.
    *   **שימוש:** `dec_to_bin(11)` תחזיר `"1011"`.
*   **`ternary_to_dec(ternary)`:**
    *   **פרמטרים:** `ternary` (str): מחרוזת המייצגת מספר טרנרי.
    *   **ערך החזרה:** מחזירה את הערך העשרוני של המספר הטרנרי (int).
    *   **מטרה:** ממירה מספר טרנרי לעשרוני.
    *   **שימוש:** `ternary_to_dec("210")` תחזיר `21`.
*   **`dec_to_ternary(decimal)`:**
    *   **פרמטרים:** `decimal` (int): מספר עשרוני.
    *   **ערך החזרה:** מחזירה את הייצוג הטרנרי של המספר העשרוני (str).
    *   **מטרה:** ממירה מספר עשרוני לטרנרי.
    *   **שימוש:** `dec_to_ternary(21)` תחזיר `"210"`.
*   **`septenary_to_dec(septenary)`:**
    *   **פרמטרים:** `septenary` (str): מחרוזת המייצגת מספר ספטנרי.
    *   **ערך החזרה:** מחזירה את הערך העשרוני של המספר הספטנרי (int).
    *   **מטרה:** ממירה מספר ספטנרי לעשרוני.
    *   **שימוש:** `septenary_to_dec("345")` תחזיר `180`.
*   **`dec_to_septenary(decimal)`:**
    *   **פרמטרים:** `decimal` (int): מספר עשרוני.
    *   **ערך החזרה:** מחזירה את הייצוג הספטנרי של המספר העשרוני (str).
    *   **מטרה:** ממירה מספר עשרוני לספטנרי.
    *   **שימוש:** `dec_to_septenary(180)` תחזיר `"345"`.
*   **`hex_to_dec(hexadecimal)`:**
    *   **פרמטרים:** `hexadecimal` (str): מחרוזת המייצגת מספר הקסדצימלי.
    *   **ערך החזרה:** מחזירה את הערך העשרוני של המספר ההקסדצימלי (int).
    *   **מטרה:** ממירה מספר הקסדצימלי לעשרוני.
    *   **שימוש:** `hex_to_dec("2AF")` תחזיר `687`.
*   **`dec_to_hex(decimal)`:**
    *   **פרמטרים:** `decimal` (int): מספר עשרוני.
    *   **ערך החזרה:** מחזירה את הייצוג ההקסדצימלי של המספר העשרוני (str).
    *   **מטרה:** ממירה מספר עשרוני להקסדצימלי.
    *   **שימוש:** `dec_to_hex(687)` תחזיר `"2AF"`.
*  **`roman_to_int(roman_str)`:**
    *   **פרמטרים:** `roman_str` (str): מחרוזת המייצגת מספר רומי.
    *   **ערך החזרה:** מחזירה את הערך העשרוני של המספר הרומי (int).
    *   **מטרה:** ממירה מספר רומי לעשרוני.
    *   **שימוש:** `roman_to_int("MCMXCIV")` תחזיר `1994`.
*   **`play_sound(duration)`:**
    *   **פרמטרים:** `duration` (int): משך הצליל במילישניות.
    *   **ערך החזרה:** אין.
    *   **מטרה:** מפיקה צליל באורך נתון, תלוי במערכת ההפעלה (חלונות או לינוקס).
*  **`text_to_morse(text)`:**
    *   **פרמטרים:** `text` (str): מחרוזת טקסט.
    *   **ערך החזרה:** מחזירה את קוד המורס של הטקסט (str).
    *   **מטרה:** ממירה טקסט לקוד מורס.
    *    **שימוש:** `text_to_morse("SOS")` תחזיר `"... --- ... "`.
*  **`morse_to_sound(morse_code)`:**
    *   **פרמטרים:** `morse_code` (str): מחרוזת קוד מורס.
    *   **ערך החזרה:** אין.
    *   **מטרה:** מפעילה צליל בהתאם לקוד המורס.
*   **`calculate_day_of_week(start_day, days_passed)`:**
    *   **פרמטרים:** `start_day` (int): יום התחלה בשבוע (0-6), `days_passed` (float or int): מספר ימים שחלפו.
    *   **ערך החזרה:** מחזירה את מספר היום בשבוע לאחר מספר הימים שעברו (int).
    *   **מטרה:** חישוב יום בשבוע עתידי או בעבר בהתבסס על יום התחלה ומספר ימים שעברו.
    *   **שימוש:** `calculate_day_of_week(0, 7)` תחזיר 0, `calculate_day_of_week(0, 10)` תחזיר 3.
*   **`day_number_to_name(day_number)`:**
    *   **פרמטרים:** `day_number` (int): מספר יום בשבוע (0-6).
    *   **ערך החזרה:** מחזירה את שם היום המתאים (str).
    *   **מטרה:** ממירה מספר יום לשם היום.
    *   **שימוש:** `day_number_to_name(0)` תחזיר `"понедельник"`.

**משתנים (Variables):**

*   קיימים משתנים מקומיים רבים בתוך הפונקציות.
*   בנוסף, ישנו `morse_code_dict` שהוא מילון גלובלי המכיל את ההתאמות בין אותיות/תווים לקוד מורס.

**בעיות אפשריות/תחומים לשיפור:**

*   פונקציית החיסור של הפירות `sub_fruits` לא מטפלת בתוצאות שליליות.
*   פונקציות המרת המספרים השונות יכולות להיות מאוחדות לפונקציה אחת גנרית, למרות שזה יגרום לפונקציה להיות מורכבת יותר.
*   ייתכן שיהיה צורך לבצע בדיקות קלט עבור הפונקציות, כדי למנוע שגיאות.
*   ניתן לשפר את קוד המורס כך שיהיה יותר גמיש וניתן להרחבה.
*   בנוסף, ישנם מספר תרגילים המוצעים, הנותנים כיוונים לשיפור ופיתוח נוסף.

**שרשרת קשרים:**

*   הפונקציות של המרת מערכות ספירה אינן קשורות ישירות אחת לשנייה, מלבד הדוגמאות, אך הן משתמשות באותו עיקרון.
*   פונקציות הפירות עובדות יחד כדי לדמות מערכת ספירה מופשטת.
*   פונקציות קוד המורס עובדות יחד להמרת טקסט לקוד מורס והשמעתו.
*   פונקציות חישוב היום פועלות יחד כדי לחשב ולהציג ימים בשבוע.
*   הקוד מדגים את הרעיון של מערכות ספירה שונות, הן מופשטות (פירות) והן קונקרטיות (בינארי, עשרוני, הקסדצימלי וכו').