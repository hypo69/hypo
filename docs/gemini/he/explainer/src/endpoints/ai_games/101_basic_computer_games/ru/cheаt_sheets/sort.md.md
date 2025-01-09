## <algorithm>
1. **`compare_fruits(fruit1, fruit2)`**:
   - מקבלת שני פריטים מסוג טופל (tuple), כאשר האיבר הראשון הוא גודל הפרי והשני הוא מזהה.
   - יוצרת מילון `order` שמתאים גודל פרי לערך מספרי (למשל, 🍎=0, 🍐=1, 🍉=2, 🧺=3).
   - מחלצת את גודלי הפירות `size1` ו-`size2` מהמילון `order`.
   - משווה בין גדלי הפירות:
     - אם `size1` קטן מ-`size2`, מחזירה -1.
     - אם `size1` גדול מ-`size2`, מחזירה 1.
     - אם הם שווים, מחזירה 0.
   - *דוגמה*: עבור `fruit1 = ("🍎", 1)` ו-`fruit2 = ("🍐", 2)`, הפונקציה תחזיר -1 כי 🍎 < 🍐.

2. **`bubble_sort(fruits)`**:
   - מקבלת רשימה של פירות.
   - עוברת על הרשימה `n` פעמים, כאשר `n` הוא אורך הרשימה.
   - בכל איטרציה, עוברת על החלק הלא ממוין של הרשימה (כל פעם החלק הממוין גדל).
   - משווה בין שני פירות סמוכים באמצעות `compare_fruits`.
   - אם הפרי השמאלי גדול מהפרי הימני, היא מחליפה ביניהם.
   - תהליך זה חוזר עד שהרשימה כולה ממוינת.
   - *דוגמה*: רשימה לא ממוינת `[("🍉", 1), ("🍎", 2)]` תהפוך לרשימה ממוינת `[("🍎", 2), ("🍉", 1)]`.

3. **`insertion_sort(fruits)`**:
   - מקבלת רשימה של פירות.
   - עוברת על הרשימה החל מהפרי השני (הראשון נחשב ממוין).
   - בוחרת את הפרי הנוכחי `key` ומשווה אותו לפרי הקודם לו.
   - אם הפרי הקודם גדול מ-`key`, היא דוחפת אותו מקום אחד ימינה.
   - התהליך ממשיך עד שמוצאים מקום לפרי הנוכחי.
   - *דוגמה*: רשימה לא ממוינת `[("🍉", 1), ("🍎", 2), ("🍐", 3)]`, כאשר  `key` יהיה `("🍎", 2)` תכניס אותו למקומו הנכון: `[("🍎", 2), ("🍉", 1), ("🍐", 3)]`.

4. **`selection_sort(fruits)`**:
   - מקבלת רשימה של פירות.
   - עוברת על הרשימה, ובכל איטרציה מוצאת את האינדקס של הפרי הקטן ביותר מהחלק הלא ממוין של הרשימה.
   - לאחר מציאת הפרי הקטן ביותר, היא מחליפה אותו עם הפרי באינדקס הנוכחי.
   - התהליך חוזר עד שכל הרשימה ממוינת.
   - *דוגמה*: ברשימה לא ממוינת `[("🍉", 1), ("🍎", 2), ("🍐", 3)]`, תחילה היא תמצא ש `("🍎", 2)` הוא הקטן ביותר ותחליף אותו עם הפרי הראשון.

5. **`display_fruits(fruits)`**:
   - מקבלת רשימה של פירות.
   - יוצרת מחרוזת המציגה את כל הפירות כאשר כל פרי מופיע בפורמט "גודל+מזהה" מופרדים בפסיקים.
   - *דוגמה*: עבור הרשימה `[("🍎", 1), ("🍐", 2)]` הפלט יהיה `"🍎1, 🍐2"`.

## <mermaid>
```mermaid
flowchart TD
    subgraph compare_fruits
        A[התחלה] --> B{קבלת שני פירות (fruit1, fruit2)};
        B --> C{הגדרת סדר הפירות (order)};
        C --> D{חילוץ גודל פרי1 (size1)};
        D --> E{חילוץ גודל פרי2 (size2)};
        E --> F{השוואה: size1 < size2?};
        F -- כן --> G[החזר -1];
        F -- לא --> H{השוואה: size1 > size2?};
        H -- כן --> I[החזר 1];
        H -- לא --> J[החזר 0];
    end
    subgraph bubble_sort
        K[התחלה] --> L{n = אורך רשימה};
        L --> M{לולאה i: 0 עד n};
        M --> N{לולאה j: 0 עד n-i-1};
        N --> O{השוואה: compare_fruits(fruits[j], fruits[j + 1]) == 1?};
        O -- כן --> P{החלפת fruits[j] ו-fruits[j+1]};
        P --> Q[המשך לולאה j];
        O -- לא --> Q;
        Q --> R{המשך לולאה i};
        R --> S[החזר רשימה ממויינת];
    end
    subgraph insertion_sort
      T[התחלה] --> U{לולאה i: 1 עד אורך הרשימה};
      U --> V{key = fruits[i]};
      V --> W{j = i - 1};
      W --> X{לולאה while: j >= 0 and compare_fruits(fruits[j], key) == 1?};
      X -- כן --> Y{fruits[j+1] = fruits[j]};
      Y --> Z{j--};
      Z --> X;
      X -- לא --> AA{fruits[j+1] = key};
      AA --> BB{המשך לולאה i};
      BB --> CC[החזר רשימה ממויינת];
    end
    subgraph selection_sort
      DD[התחלה] --> EE{n = אורך הרשימה};
      EE --> FF{לולאה i: 0 עד n};
      FF --> GG{min_index = i};
      GG --> HH{לולאה j: i+1 עד n};
      HH --> II{השוואה: compare_fruits(fruits[j], fruits[min_index]) == -1?};
      II -- כן --> JJ{min_index = j};
      JJ --> HH;
      II -- לא --> HH;
      HH --> KK{החלפת fruits[i] ו-fruits[min_index]};
      KK --> LL{המשך לולאה i};
      LL --> MM[החזר רשימה ממוינת];
    end
     subgraph display_fruits
        NN[התחלה] --> OO{קבלת רשימת פירות};
        OO --> PP{יצירת מחרוזת מפורמטת};
        PP --> QQ[החזרת מחרוזת];
     end
```

## <explanation>
**ייבואים (Imports)**:

*   `from typing import List, Tuple`:
    *   ייבוא זה מאפשר להגדיר את טיפוסי המשתנים בצורה ברורה (type hinting).
    *   `List` מציין רשימה, ו-`Tuple` מציין טופל (רשומה).
    *   השימוש בטיפוסי משתנים משפר את קריאות הקוד ותחזוקה.

**פונקציות (Functions)**:

1.  **`compare_fruits(fruit1: Tuple[str, int], fruit2: Tuple[str, int]) -> int`**:
    *   **פרמטרים**: מקבלת שני טופלים, כל אחד מהם מייצג פרי ומכיל את גודל הפרי (מחרוזת) ומזהה (מספר שלם).
    *   **ערך מוחזר**: מחזירה מספר שלם: -1 אם הפרי הראשון קטן מהשני, 1 אם גדול, 0 אם שווה.
    *   **מטרה**: להשוות בין שני פירות לפי גודלם.
    *   **שימוש**: משמשת בפונקציות המיון כדי להשוות בין פירות סמוכים או למציאת הפרי הקטן ביותר.
    *   **דוגמה**: `compare_fruits(("🍎", 1), ("🍐", 2))` תחזיר -1, כי תפוח קטן מאגס.

2.  **`bubble_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]`**:
    *   **פרמטרים**: מקבלת רשימה של פירות.
    *   **ערך מוחזר**: מחזירה רשימה ממוינת של פירות.
    *   **מטרה**: למיין רשימת פירות באמצעות אלגוריתם מיון בועות.
    *   **שימוש**: מארגנת את הרשימה כך שהפירות הקטנים יופיעו בתחילת הרשימה והגדולים בסוף.
    *   **דוגמה**:  `bubble_sort([("🍉", 1), ("🍎", 2)])` תחזיר `[("🍎", 2), ("🍉", 1)]`.

3.  **`insertion_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]`**:
    *   **פרמטרים**: מקבלת רשימה של פירות.
    *   **ערך מוחזר**: מחזירה רשימה ממוינת של פירות.
    *   **מטרה**: למיין רשימה של פירות באמצעות אלגוריתם מיון הכנסה.
    *   **שימוש**: מכניסה כל פרי במקומו הנכון בחלק הממוין של הרשימה.
    *   **דוגמה**: `insertion_sort([("🍉", 1), ("🍎", 2), ("🍐", 3)])`  תחזיר רשימה ממוינת של הפירות.

4.  **`selection_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]`**:
    *   **פרמטרים**: מקבלת רשימה של פירות.
    *   **ערך מוחזר**: מחזירה רשימה ממוינת של פירות.
    *   **מטרה**: למיין רשימה של פירות באמצעות אלגוריתם מיון בחירה.
    *   **שימוש**: מוצאת בכל איטרציה את הפרי הקטן ביותר בחלק הלא ממוין של הרשימה וממקמת אותו במקומו הנכון.
    *   **דוגמה**: `selection_sort([("🍉", 1), ("🍎", 2), ("🍐", 3)])` תחזיר רשימה ממוינת של הפירות.

5.  **`display_fruits(fruits: List[Tuple[str, int]]) -> str`**:
    *   **פרמטרים**: מקבלת רשימה של פירות.
    *   **ערך מוחזר**: מחזירה מחרוזת המציגה את הפירות ברשימה בפורמט קריא.
    *   **מטרה**: להמיר רשימה של פירות למחרוזת שניתן להציג בקלות.
    *   **שימוש**: לייצוג ויזואלי של רשימת הפירות.
    *   **דוגמה**: `display_fruits([("🍎", 1), ("🍐", 2)])` תחזיר את המחרוזת "🍎1, 🍐2".

**משתנים (Variables)**:

*   `fruits`: רשימה של טופלים (tuple) המייצגים פירות. כל טופל מכיל את גודל הפרי (מחרוזת) ומזהה (מספר שלם).
*   `order`: מילון הממפה גדלי פירות לערכים מספריים המשמשים להשוואה.
*   `n`: מספר הפירות ברשימה.
*   `key`: משתנה זמני המשמש לאחסון פרי במהלך המיון.
*   `min_index`: אינדקס הפרי הקטן ביותר שנמצא במהלך המיון בשיטת הבחירה.

**בעיות אפשריות או תחומים לשיפור**:

*   יעילות אלגוריתמים: מיון בועות הוא אלגוריתם לא יעיל עבור רשימות גדולות, אפשר לשקול להשתמש באלגוריתמים יעילים יותר כמו מיון מיזוג (merge sort) או מיון מהיר (quick sort) עבור מקרים כאלה.
*   קריאות: אפשר להוסיף עוד תגובות (comments) כדי להסביר כל שלב בקוד, במיוחד באלגוריתמים השונים.
*   גמישות: אפשר להפוך את פונקציית ההשוואה `compare_fruits` לגנרית יותר, כך שתוכל לקבל קריטריונים אחרים להשוואה.
*   בדיקות: אפשר להוסיף בדיקות יחידה (unit tests) לכל פונקציה כדי לוודא שהיא מתנהגת כמו שצריך.
*   שימוש ב-`copy()`: הקוד משתמש ב-`fruits.copy()` כדי לא לשנות את רשימת המקור. אפשר לשקול להשתמש במקום ב-`copy()` ב-`sorted()` אשר מחזירה עותק ממוין, זה היה מייעל את הקוד.

**שרשרת קשרים עם חלקים אחרים בפרויקט (אם רלוונטי)**:
אין כרגע קשרים ישירים לחלקים אחרים בפרויקט, אך הקוד יכול לשמש כבסיס למודול מיון, אותו ניתן לשלב במערכות אחרות הזקוקות למיון של רשימות.