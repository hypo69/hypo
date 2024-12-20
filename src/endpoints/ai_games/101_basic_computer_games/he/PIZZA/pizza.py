# PIZZA:
```
=================
קושי: 2
-----------------
המשחק "פיצה" הוא משחק פשוט בו השחקן צריך להחליט כמה פיצות להזמין על סמך מספר האנשים וגודל הפיצות. המשחק מחשב כמה פיצות דרושות בהתבסס על מספר האנשים, ומאפשר להם לבחור בין גדלים שונים של פיצה. הוא מספק המלצה על כמות הפיצות, בהתאם לגודל הנבחר, ומסיים בהצגת מספר הפיצות שהוזמנו.

חוקי המשחק:
1. השחקן מתבקש להזין את מספר האנשים.
2. השחקן מתבקש לבחור בין פיצה קטנה, בינונית או גדולה.
3. בהתבסס על מספר האנשים וגודל הפיצה, המשחק מחשב את מספר הפיצות הנדרש.
4. המשחק מציג את מספר הפיצות שהוזמנו בהתאם לבחירת הגודל.
-----------------
אלגוריתם:
1. קבל קלט מהמשתמש לגבי מספר האנשים.
2. קבל קלט מהמשתמש לגבי סוג הפיצה (קטנה, בינונית, או גדולה).
3. בצע חישוב של מספר הפיצות הנדרש בהתאם לגודל הפיצה שנבחרה:
   - אם נבחרה פיצה קטנה: חשב פיצה אחת לכל 3 אנשים.
   - אם נבחרה פיצה בינונית: חשב פיצה אחת לכל 2 אנשים.
   - אם נבחרה פיצה גדולה: חשב פיצה אחת לכל אדם.
4. הצג את מספר הפיצות הנדרש.
5. סיים את המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InputPeopleNum["קלט: מספר אנשים"]
    InputPeopleNum --> InputPizzaSize["קלט: גודל פיצה (S, M, L)"]
    InputPizzaSize --> CheckPizzaSize{"בדיקה: גודל פיצה?"}
    CheckPizzaSize -- "S" --> CalculateSmallPizza["חישוב: numberOfPizzas = מספר אנשים / 3"]
    CheckPizzaSize -- "M" --> CalculateMediumPizza["חישוב: numberOfPizzas = מספר אנשים / 2"]
    CheckPizzaSize -- "L" --> CalculateLargePizza["חישוב: numberOfPizzas = מספר אנשים / 1"]
    CalculateSmallPizza --> OutputPizzas["הצג: מספר פיצות"]
    CalculateMediumPizza --> OutputPizzas
    CalculateLargePizza --> OutputPizzas
    OutputPizzas --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    InputPeopleNum - קבלת מספר האנשים מהמשתמש.
    InputPizzaSize - קבלת גודל הפיצה הרצוי (S, M, L) מהמשתמש.
    CheckPizzaSize - בדיקה איזה גודל פיצה נבחר.
    CalculateSmallPizza - חישוב מספר הפיצות הנדרש לפי גודל קטן (1 פיצה ל-3 אנשים).
    CalculateMediumPizza - חישוב מספר הפיצות הנדרש לפי גודל בינוני (1 פיצה ל-2 אנשים).
    CalculateLargePizza - חישוב מספר הפיצות הנדרש לפי גודל גדול (1 פיצה לכל אדם).
    OutputPizzas - הצגת מספר הפיצות שהוזמנו.
    End - סוף התוכנית.
```
```python
# פונקציה שמחשבת את מספר הפיצות הדרושות
def calculate_pizza_amount():
    # קבלת מספר האנשים מהמשתמש
    try:
        num_people = int(input("הכנס את מספר האנשים: "))
        if num_people <= 0:
             print("מספר האנשים חייב להיות חיובי.")
             return
    except ValueError:
         print("קלט לא תקין. אנא הכנס מספר שלם.")
         return

    # קבלת גודל הפיצה מהמשתמש
    pizza_size = input("הכנס את גודל הפיצה (S, M, L): ").upper()

    # בדיקה איזה גודל פיצה נבחר וחישוב מספר הפיצות
    if pizza_size == "S":
        # פיצה קטנה - פיצה אחת לכל 3 אנשים
        num_pizzas = (num_people + 2) // 3
        print(f"מומלץ להזמין {num_pizzas} פיצות קטנות.")
    elif pizza_size == "M":
        # פיצה בינונית - פיצה אחת לכל 2 אנשים
        num_pizzas = (num_people + 1) // 2
        print(f"מומלץ להזמין {num_pizzas} פיצות בינוניות.")
    elif pizza_size == "L":
        # פיצה גדולה - פיצה אחת לכל אדם
        num_pizzas = num_people
        print(f"מומלץ להזמין {num_pizzas} פיצות גדולות.")
    else:
        print("גודל פיצה לא תקין. אנא הכנס S, M או L.")


# הפעלת המשחק
if __name__ == "__main__":
    calculate_pizza_amount()

```
```
הסברים:
1.  **הגדרת הפונקציה `calculate_pizza_amount()`**:
    - הפונקציה מוגדרת לביצוע החישוב של מספר הפיצות הדרושות.
2.  **קבלת מספר האנשים**:
    - `num_people = int(input("הכנס את מספר האנשים: "))`: קולטת את מספר האנשים מהמשתמש וממירה אותו למספר שלם.
    -   `try...except ValueError`: מטפל במקרה שהקלט אינו מספר שלם ומדפיס הודעה בהתאם.
    -  `if num_people <= 0`: בודק אם מספר האנשים חיובי ומדפיס הודעה בהתאם.
3.  **קבלת גודל הפיצה**:
    - `pizza_size = input("הכנס את גודל הפיצה (S, M, L): ").upper()`: קולטת את גודל הפיצה מהמשתמש וממירה אותו לאותיות גדולות.
4.  **בדיקת גודל הפיצה וחישוב מספר הפיצות**:
    -   `if pizza_size == "S"`: אם גודל הפיצה הוא קטן, מחשב את מספר הפיצות הדרוש על ידי חלוקה ב-3 (ומעגל כלפי מעלה).
    -   `elif pizza_size == "M"`: אם גודל הפיצה הוא בינוני, מחשב את מספר הפיצות הדרוש על ידי חלוקה ב-2 (ומעגל כלפי מעלה).
    -   `elif pizza_size == "L"`: אם גודל הפיצה הוא גדול, מספר הפיצות הדרוש שווה למספר האנשים.
    -   `else`: אם גודל הפיצה שהוזן אינו תקין, מדפיס הודעה בהתאם.
5.  **הדפסת מספר הפיצות**:
    - מדפיס את מספר הפיצות המומלץ בהתאם לגודל הפיצה שנבחר.
6.  **הפעלת הפונקציה**:
    -   `if __name__ == "__main__":`: מוודא שהקוד יופעל רק אם הקובץ מורץ ישירות, ולא כמודול.
    -   `calculate_pizza_amount()`: קורא לפונקציה להפעלת המשחק.
```
