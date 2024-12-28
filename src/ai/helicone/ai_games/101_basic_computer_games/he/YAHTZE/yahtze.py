<YAHTZE>:
=================
קושי: 5
-----------------
המשחק "יאצי" הוא משחק קוביות קלאסי בו המטרה היא לצבור את מירב הנקודות על ידי הטלת 5 קוביות וסידורן בקטגוריות שונות, כאשר כל קטגוריה נותנת ניקוד שונה בהתאם לתוצאות ההטלה. לשחקן יש שלושה ניסיונות הטלה בכל תור, והוא יכול לבחור אילו קוביות להטיל שוב בכל ניסיון. בסוף התור, השחקן חייב להכניס את הנקודות לאחת מהקטגוריות הפנויות. המשחק מסתיים כאשר כל הקטגוריות מלאות.

חוקי המשחק:
1. המשחק משוחק עם 5 קוביות בעלות 6 פאות.
2. בכל תור, השחקן מטיל את הקוביות עד 3 פעמים.
3. בין ההטלות, השחקן יכול לבחור אילו קוביות להשאיר ואילו להטיל מחדש.
4. בסוף כל תור, השחקן צריך להכניס את תוצאת ההטלה לאחת מהקטגוריות הבאות:
    *   1 - סכום כל הקוביות שערכן 1
    *   2 - סכום כל הקוביות שערכן 2
    *   3 - סכום כל הקוביות שערכן 3
    *   4 - סכום כל הקוביות שערכן 4
    *   5 - סכום כל הקוביות שערכן 5
    *   6 - סכום כל הקוביות שערכן 6
    *   3 OF A KIND - שלוש קוביות בעלות ערך זהה (סכום כל הקוביות)
    *   4 OF A KIND - ארבע קוביות בעלות ערך זהה (סכום כל הקוביות)
    *   FULL HOUSE - שלוש קוביות מאותו ערך ועוד זוג קוביות מאותו ערך (25 נקודות)
    *   SMALL STRAIGHT - רצף של 4 מספרים (30 נקודות)
    *   LARGE STRAIGHT - רצף של 5 מספרים (40 נקודות)
    *   YAHTZE - חמש קוביות מאותו ערך (50 נקודות)
    *   CHANCE - סכום כל הקוביות
5. כל קטגוריה יכולה להיות בשימוש רק פעם אחת במהלך המשחק.
6. המטרה היא לצבור את מירב הנקודות.
7. המשחק מסתיים כאשר כל הקטגוריות מולאו.

-----------------
אלגוריתם:
1. אתחל את מערך הקטגוריות (13 קטגוריות), כאשר כל קטגוריה מסומנת כפנויה (ערך 0).
2. אתחל את מערך הנקודות, שבו יאוחסנו הנקודות לכל קטגוריה.
3. התחל לולאה ראשית: עבור כל תור (13 תורות):
    3.1. אתחל את מספר הטלות ל-0.
    3.2. התחל לולאה פנימית: כל עוד מספר ההטלות קטן מ-3:
        3.2.1. הטל את 5 הקוביות באופן אקראי (ערכים בין 1 ל-6).
        3.2.2. הצג את תוצאות ההטלה.
        3.2.3. אם מספר ההטלות קטן מ-2, שאל את השחקן אילו קוביות להטיל שוב (אחרת, השחקן לא יכול לשנות יותר את הקוביות).
        3.2.4. הגדל את מספר ההטלות ב-1.
    3.3. הצג את תוצאות ההטלה הסופיות.
    3.4. הצג את הקטגוריות הפנויות.
    3.5. שאל את השחקן לאיזו קטגוריה הוא רוצה להכניס את הנקודות (בחר קטגוריה בין 1-13).
    3.6. בדוק אם הקטגוריה שבחר השחקן פנויה, אם לא, בקש מהשחקן לבחור קטגוריה פנויה אחרת.
    3.7. חשב את הנקודות עבור הקטגוריה הנבחרת והוסף אותם למערך הנקודות.
    3.8. סמן את הקטגוריה שבחר השחקן כלא פנויה.
4. לאחר סיום כל התורות, חשב את סך הנקודות.
5. הצג את סך הנקודות.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["אתחול: 
    <br><code><b>categoriesAvailable=[True]*13, scores=[0]*13
    <br>turnCounter = 0</b></code>"]
    InitializeGame --> TurnLoopStart{"תחילת לולאת תורות:
     <br><code><b>turnCounter < 13</b></code>"}
    TurnLoopStart -- כן --> ResetRolls["<code><b>numberOfRolls = 0</b></code>"]
    ResetRolls --> RollLoopStart{"תחילת לולאת הטלות:
    <br><code><b>numberOfRolls < 3</b></code>"}
    RollLoopStart -- כן --> RollDice["הטלת 5 קוביות
    <br><code><b>diceValues = random(1,6), 5 פעמים</b></code>"]
    RollDice --> OutputRoll["הצגת תוצאות ההטלה"]
    OutputRoll --> CheckRollsNumber{"בדיקה: 
     <br><code><b>numberOfRolls < 2?</b></code>"}
    CheckRollsNumber -- כן --> SelectDiceToReRoll["קלט: בחירת קוביות להטלה חוזרת"]
    SelectDiceToReRoll --> ReRollDice["הטלה חוזרת של הקוביות שנבחרו"]
     ReRollDice --> IncreaseRolls["<code><b>numberOfRolls += 1</b></code>"]
    IncreaseRolls --> RollLoopStart
    CheckRollsNumber -- לא --> IncreaseRolls
   RollLoopStart -- לא --> OutputFinalRoll["הצגת תוצאות ההטלה הסופיות"]
    OutputFinalRoll --> OutputAvailableCategories["הצגת הקטגוריות הפנויות"]
    OutputAvailableCategories --> InputCategoryChoice["קלט: בחירת קטגוריה"]
    InputCategoryChoice --> CheckCategoryAvailability{"בדיקה: הקטגוריה פנויה?"}
    CheckCategoryAvailability -- לא --> OutputCategoryError["הודעת שגיאה: קטגוריה תפוסה, בחר אחרת"]
    OutputCategoryError --> InputCategoryChoice
    CheckCategoryAvailability -- כן --> CalculateScore["חישוב נקודות עבור הקטגוריה הנבחרת"]
     CalculateScore --> SaveScore["שמירת הנקודות בקטגוריה הנבחרת
    <br><code><b>scores[categoryChoice]=calculatedScore</b></code>"]
     SaveScore --> MarkCategoryUnavailable["סימון הקטגוריה כלא פנויה
     <br><code><b>categoriesAvailable[categoryChoice] = False</b></code>"]
    MarkCategoryUnavailable --> IncreaseTurnCounter["<code><b>turnCounter += 1</b></code>"]
    IncreaseTurnCounter --> TurnLoopStart
    TurnLoopStart -- לא --> CalculateTotalScore["חישוב סך הנקודות"]
    CalculateTotalScore --> OutputTotalScore["הצגת סך הנקודות"]
    OutputTotalScore --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתני המשחק: מערך `categoriesAvailable` המסמן אילו קטגוריות פנויות (אמת לכולן בהתחלה), מערך `scores` לאחסון הנקודות (מאותחל לאפס), ומונה תורות `turnCounter` מאותחל ל-0.
    TurnLoopStart - תחילת לולאה המבצעת את התורות, כל עוד `turnCounter` קטן מ-13 (מספר התורות במשחק).
    ResetRolls - איפוס מספר ההטלות בתחילת תור חדש.
    RollLoopStart - תחילת לולאת ההטלות, המאפשרת עד 3 הטלות בכל תור.
    RollDice - הטלת 5 קוביות אקראיות (ערכים בין 1 ל-6).
    OutputRoll - הצגת תוצאות הטלת הקוביות לשחקן.
    CheckRollsNumber - בדיקה האם מספר ההטלות קטן מ-2, כדי לאפשר בחירת קוביות להטלה חוזרת רק ב-2 ההטלות הראשונות.
    SelectDiceToReRoll - קבלת קלט מהשחקן לגבי אילו קוביות להטיל מחדש.
    ReRollDice - ביצוע הטלה מחדש של הקוביות שנבחרו על ידי השחקן.
    IncreaseRolls - הגדלת מונה מספר ההטלות ב-1.
    OutputFinalRoll - הצגת תוצאות ההטלה הסופיות לשחקן בתום 3 ההטלות או פחות.
    OutputAvailableCategories - הצגת הקטגוריות הפנויות לשחקן.
    InputCategoryChoice - קבלת בחירת קטגוריה מהשחקן.
    CheckCategoryAvailability - בדיקה האם הקטגוריה שבחר השחקן פנויה.
    OutputCategoryError - הצגת הודעה כי הקטגוריה תפוסה, במידה ונבחרה קטגוריה תפוסה, ובקשה לבחור קטגוריה אחרת.
    CalculateScore - חישוב הניקוד בהתאם לחוקי המשחק והקטגוריה שנבחרה.
     SaveScore - שמירת הניקוד של השחקן בקטגוריה הנבחרת.
     MarkCategoryUnavailable - סימון הקטגוריה כלא פנויה, על מנת שלא תהיה זמינה לשימוש נוסף.
     IncreaseTurnCounter - הגדלת מונה התורות, לקראת התור הבא.
    CalculateTotalScore - חישוב סך הנקודות שצבר השחקן במשחק.
    OutputTotalScore - הצגת סך הנקודות לשחקן.
    End - סיום המשחק.

```
```python
import random

# פונקציה להטלת קובייה בודדת
def roll_die():
    """
    מגרילה מספר אקראי בין 1 ל-6, המייצג הטלת קובייה.
    """
    return random.randint(1, 6)

# פונקציה להטלת 5 קוביות
def roll_dice():
    """
    מגרילה 5 קוביות ומחזירה רשימה של תוצאות.
    """
    return [roll_die() for _ in range(5)]

# פונקציה להדפסת הקוביות
def print_dice(dice):
    """
    מדפיסה את תוצאות הטלת הקוביות.
    """
    print("הקוביות שהתקבלו:", dice)

# פונקציה לבחירת קוביות להטלה חוזרת
def select_dice_to_reroll(dice):
    """
    מאפשרת לשחקן לבחור אילו קוביות להטיל מחדש.
    הפונקציה מקבלת את תוצאות הקוביות הנוכחיות ומחזירה רשימה של אינדקסים של קוביות להטלה חוזרת.
    """
    while True:
        try:
            print("בחר את מספרי הקוביות שברצונך להטיל שוב (הפרד במספרים רווחים, 1-5. לדוגמה: 1 3 5), או הקש ENTER אם לא רוצים לבחור :")
            choice = input().strip()
            if not choice:
                return []
            indices = [int(x) - 1 for x in choice.split()]
            if any(index < 0 or index > 4 for index in indices):
                 print("מספרי הקוביות צריכים להיות בין 1 ל-5.")
                 continue
            return indices
        except ValueError:
            print("קלט לא תקין, אנא הכנס מספרים מופרדים ברווחים")

# פונקציה לחישוב הניקוד לפי קטגוריה
def calculate_score(dice, category):
    """
    מחשבת את הניקוד לפי הקטגוריה שנבחרה.
    """
    counts = [0] * 7  # רשימה לספירת מופעים של כל ערך קוביה
    for value in dice:
        counts[value] += 1

    if category <= 6:  # סכום כל הקוביות עם הערך המתאים
        return sum(value for value in dice if value == category)

    elif category == 7:  # 3 OF A KIND
        if any(count >= 3 for count in counts):
            return sum(dice)
        return 0

    elif category == 8:  # 4 OF A KIND
        if any(count >= 4 for count in counts):
            return sum(dice)
        return 0

    elif category == 9:  # FULL HOUSE
        if any(count == 3 for count in counts) and any(count == 2 for count in counts):
            return 25
        return 0
    
    elif category == 10: # SMALL STRAIGHT
        if any(counts[i] > 0 for i in range(1,5)) and any(counts[i] > 0 for i in range(2,6)) and  any(counts[i] > 0 for i in range(3,7)):
           return 30
        return 0

    elif category == 11:  # LARGE STRAIGHT
        if all(counts[i] == 1 for i in range(1, 6)):
            return 40
        return 0
    elif category == 12:  # YAHTZE
        if any(count == 5 for count in counts):
            return 50
        return 0

    elif category == 13:  # CHANCE
        return sum(dice)

    return 0

# פונקציה להצגת הקטגוריות הזמינות
def display_available_categories(categories_available):
    """
    מדפיסה את רשימת הקטגוריות הזמינות לשחקן.
    הפונקציה מקבלת את מערך הקטגוריות הזמינות ומדפיסה את רשימת האפשרויות.
    """
    print("\nקטגוריות זמינות:")
    for i, available in enumerate(categories_available):
        if available:
           category_name = get_category_name(i + 1)
           print(f"{i + 1}. {category_name}")

def get_category_name(category_number):
    """
    מחזירה את השם של הקטגוריה לפי מספרה.
    """
    if category_number == 1:
        return "סכום כל הקוביות שערכן 1"
    elif category_number == 2:
        return "סכום כל הקוביות שערכן 2"
    elif category_number == 3:
        return "סכום כל הקוביות שערכן 3"
    elif category_number == 4:
        return "סכום כל הקוביות שערכן 4"
    elif category_number == 5:
        return "סכום כל הקוביות שערכן 5"
    elif category_number == 6:
        return "סכום כל הקוביות שערכן 6"
    elif category_number == 7:
        return "3 OF A KIND"
    elif category_number == 8:
        return "4 OF A KIND"
    elif category_number == 9:
        return "FULL HOUSE"
    elif category_number == 10:
        return "SMALL STRAIGHT"
    elif category_number == 11:
        return "LARGE STRAIGHT"
    elif category_number == 12:
        return "YAHTZE"
    elif category_number == 13:
         return "CHANCE"
    else:
        return "לא ידוע"

# פונקציה לקבלת קלט מהמשתמש לבחירת קטגוריה
def get_category_choice(categories_available):
    """
    מבקשת מהשחקן לבחור קטגוריה.
    הפונקציה מקבלת את מערך הקטגוריות הזמינות, וממשיכה לבקש קלט מהמשתמש עד שהוא בוחר קטגוריה זמינה.
    """
    while True:
        try:
            choice = int(input("בחר קטגוריה (1-13): "))
            if 1 <= choice <= 13 and categories_available[choice - 1]:
                return choice
            else:
                print("בחירה לא תקינה או קטגוריה תפוסה. אנא בחר קטגוריה זמינה.")
        except ValueError:
            print("קלט לא תקין, אנא הכנס מספר")

# פונקציה ראשית של המשחק
def play_yahtze():
    """
    מנהלת את משחק היאצי.
    """
    categories_available = [True] * 13 # מערך בוליאני לציון קטגוריות זמינות
    scores = [0] * 13 # מערך של נקודות לכל קטגוריה
    turn_counter = 0 # מונה תורות

    while turn_counter < 13: # 13 תורות
        print(f"\nתור {turn_counter + 1}:")

        dice = [] # רשימה לתוצאות הטלות הקוביות
        number_of_rolls = 0 # מספר הטלות בתור הנוכחי

        while number_of_rolls < 3: # עד 3 הטלות בכל תור
            dice = roll_dice()
            print_dice(dice)

            if number_of_rolls < 2: # מאפשרים לבחור קוביות להטלה חוזרת רק בשתי ההטלות הראשונות
                reroll_indices = select_dice_to_reroll(dice)
                for index in reroll_indices:
                     dice[index] = roll_die()
            number_of_rolls += 1
        print("תוצאה סופית: ",dice) # הצגת תוצאה סופית לאחר הטלה שלישית
        
        display_available_categories(categories_available) # הצגת הקטגוריות הזמינות
        
        category_choice = get_category_choice(categories_available) # קבלת קלט מהמשתמש לגבי הקטגוריה
       
        score = calculate_score(dice, category_choice)  # חישוב נקודות לפי הקטגוריה
        scores[category_choice - 1] = score # שמירת הנקודות
        categories_available[category_choice - 1] = False  # סימון קטגוריה כלא זמינה

        turn_counter += 1 # מעבר לתור הבא
    
    total_score = sum(scores)
    print("\nהמשחק הסתיים!")
    print("סך הנקודות:", total_score)

if __name__ == "__main__":
    play_yahtze()
```
<הערות סיום>
הקוד של המשחק "יאצי" מורכב מכמה פונקציות עיקריות:
1.  `roll_die()`: פונקציה שמדמה הטלת קובייה בודדת על ידי יצירת מספר אקראי בין 1 ל-6.
2.  `roll_dice()`: פונקציה שמדמה הטלת 5 קוביות על ידי קריאה לפונקציה `roll_die()` חמש פעמים, ומחזירה רשימה של תוצאות.
3.  `print_dice(dice)`: פונקציה שמקבלת רשימה של תוצאות קוביות ומדפיסה אותן למסך.
4.  `select_dice_to_reroll(dice)`: פונקציה שמאפשרת לשחקן לבחור אילו קוביות להטיל מחדש. הפונקציה מבקשת מהשחקן להכניס את מספרי הקוביות שברצונו להטיל שוב (בין 1 ל-5) ומחזירה רשימה של אינדקסים של הקוביות להטלה חוזרת.
5.  `calculate_score(dice, category)`: פונקציה שמקבלת רשימת קוביות ואת מספר הקטגוריה שאליה רוצים להכניס את הנקודות, ומחזירה את הניקוד המתאים לפי חוקי המשחק. הפונקציה כוללת בדיקות לכל קטגוריה אפשרית, כגון סכום לפי מספר מסוים, שלשות, רצפים וכו'.
6.  `display_available_categories(categories_available)`: פונקציה שמקבלת מערך בוליאני שמייצג אילו קטגוריות עדיין פנויות, ומדפיסה למסך את רשימת הקטגוריות הזמינות לבחירה.
7.  `get_category_name(category_number)`: פונקציה המחזירה את שם הקטגוריה לפי מספרה.
8.  `get_category_choice(categories_available)`: פונקציה שמבקשת מהשחקן לבחור קטגוריה מהרשימה, תוך בדיקה שהבחירה תקינה (קיימת וזמינה).
9.  `play_yahtze()`: פונקציה שמנהלת את כל המשחק. היא מאתחלת את מצב המשחק, כולל רשימות הקטגוריות הזמינות והנקודות, ומנהלת את מהלך המשחק על ידי לולאה של 13 סיבובים (תורות). בכל תור, השחקן מבצע עד 3 הטלות, בוחר אילו קוביות להטיל שוב, בוחר קטגוריה להכניס אליה את הנקודות, והניקוד מחושב בהתאם. בסוף המשחק מחושב ומודפס סך הנקודות.
10. `if __name__ == "__main__":`: בלוק קוד זה מבטיח שהפונקציה play_yahtze() תופעל רק אם הקובץ מורץ ישירות ולא כאשר הוא מיובא כמודול.
הקוד כולל הערות בעברית שמסבירות את המטרות והתהליכים של כל פונקציה ושלב במשחק. הקוד בנוי כך שיהיה קל להבנה גם למתחילים, עם חלוקה לפונקציות מודולריות ושימוש בשמות משתנים ברורים.
</הערות סיום>
