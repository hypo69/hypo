<WAR 2>:
=================
קושי: 2
-----------------
המשחק "מלחמה" הוא משחק קלפים לשני שחקנים, כאשר כל שחקן מקבל חצי מהחפיסה. כל סיבוב, כל שחקן חושף את הקלף העליון שלו, והשחקן עם הערך הגבוה יותר של הקלף זוכה בשני הקלפים. המנצח הוא השחקן שמצליח לאסוף את כל הקלפים.
חוקי המשחק:
1. המשחק משוחק על ידי שני שחקנים, המכונים "המחשב" ו"המשתמש".
2. בתחילת המשחק, כל שחקן מקבל חצי מחבילת קלפים סטנדרטית (1 עד 10).
3. בכל סיבוב, כל שחקן חושף את הקלף העליון שלו.
4. השחקן עם הקלף בעל הערך הגבוה יותר זוכה בשני הקלפים.
5. במקרה של תיקו, שני השחקנים משליכים את הקלפים, ופותחים קלף נוסף. השחקן עם הערך הגבוה יותר זוכה בכל הקלפים שנצברו.
6. המשחק מסתיים כאשר אחד השחקנים אוסף את כל הקלפים, או לאחר מספר מוגדר של סיבובים (במקרה זה 20).
-----------------
אלגוריתם:
1. אתחל את חבילות הקלפים של המחשב והמשתמש (חצי מהערכים 1-10 לכל אחד).
2. התחל לולאה עבור 20 סיבובים.
3. בכל סיבוב:
   3.1. אם חבילת הקלפים של אחד השחקנים ריקה, צא מהלולאה והכרז על השחקן השני כמנצח.
   3.2. שלוף את הקלף העליון מחבילת הקלפים של כל שחקן.
   3.3. אם קלף המשתמש גדול יותר מקלף המחשב, הוסף את שני הקלפים לחבילת המשתמש.
   3.4. אם קלף המחשב גדול יותר מקלף המשתמש, הוסף את שני הקלפים לחבילת המחשב.
   3.5. אם קלפי השחקנים שווים, התחל "מלחמה":
       3.5.1. כל עוד יש קלפים בשתי החבילות:
           3.5.1.1. השלך את הקלף הבא מכל חבילה (אם אין קלפים אז סיום המשחק והכרזת מנצח).
           3.5.1.2. השלך קלף נוסף מכל חבילה.
           3.5.1.3. אם קלף המשתמש גדול יותר מקלף המחשב, הוסף את כל הקלפים לחבילת המשתמש וצא מלולאת ה"מלחמה".
           3.5.1.4. אם קלף המחשב גדול יותר מקלף המשתמש, הוסף את כל הקלפים לחבילת המחשב וצא מלולאת ה"מלחמה".
4. בדוק מי השחקן עם יותר קלפים, והכרז עליו כמנצח.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeDecks["<p align='left'>אתחול חבילות קלפים:
    <code><b>
    computerDeck = [1, 2, 3, 4, 5]<br>
    userDeck = [6, 7, 8, 9, 10]
    </b></code></p>"]
    InitializeDecks --> LoopStart{"תחילת לולאה: עבור 20 סיבובים"}
    LoopStart -- כן --> CheckEmptyDecks{"בדיקה: האם אחת החבילות ריקה?"}
    CheckEmptyDecks -- כן --> DetermineWinnerEmptyDecks["הכרז על המנצח (חבילה ריקה)"]
    DetermineWinnerEmptyDecks --> End["סוף"]
    CheckEmptyDecks -- לא --> DrawCards["<p align='left'>שליפת קלף עליון מכל חבילה:<br>
    <code><b>
    computerCard = computerDeck.pop(0)<br>
    userCard = userDeck.pop(0)
    </b></code></p>"]
    DrawCards --> CompareCards{"בדיקה: <code><b>userCard > computerCard</b></code> ?"}
    CompareCards -- כן --> UserWinsRound["הוספת קלפים לחבילת המשתמש"]
    UserWinsRound --> LoopStart
    CompareCards -- לא --> CompareCards2{"בדיקה: <code><b>computerCard > userCard</b></code> ?"}
    CompareCards2 -- כן --> ComputerWinsRound["הוספת קלפים לחבילת המחשב"]
    ComputerWinsRound --> LoopStart
    CompareCards2 -- לא --> StartWar["<p align='left'>התחלת מלחמה (קלפים שווים):<br>
    <code><b>warCards = []</b></code></p>"]
    StartWar --> WarLoopStart{"תחילת לולאת מלחמה: כל עוד יש קלפים"}
      WarLoopStart -- כן --> CheckEmptyDecksWar{"בדיקה: האם אחת החבילות ריקה?"}
      CheckEmptyDecksWar -- כן --> DetermineWinnerEmptyDecksWar["הכרז על המנצח (חבילה ריקה במלחמה)"]
      DetermineWinnerEmptyDecksWar --> End
      CheckEmptyDecksWar -- לא --> WarDrawCards["<p align='left'>שליפת קלפים למלחמה:<br>
      <code><b>
      warCards.append(computerCard)<br>
      warCards.append(userCard)<br>
       computerCard = computerDeck.pop(0) if computerDeck else None<br>
        userCard = userDeck.pop(0) if userDeck else None<br>
      warCards.append(computerCard)<br>
        warCards.append(userCard)
      </b></code></p>"]
      WarDrawCards --> CheckWarEmptyCards{"בדיקה האם יש קלפים להשוואה במלחמה"}
      CheckWarEmptyCards -- לא --> CompareCardsWar{"בדיקה: <code><b>userCard > computerCard</b></code> ?"}
      CompareCardsWar -- כן --> UserWinsWarRound["הוספת קלפים לחבילת המשתמש וסיום מלחמה"]
      UserWinsWarRound --> LoopStart
      CompareCardsWar -- לא --> CompareCardsWar2{"בדיקה: <code><b>computerCard > userCard</b></code> ?"}
      CompareCardsWar2 -- כן --> ComputerWinsWarRound["הוספת קלפים לחבילת המחשב וסיום מלחמה"]
      ComputerWinsWarRound --> LoopStart
      CompareCardsWar2 -- לא --> WarLoopStart
     CheckWarEmptyCards -- כן -->  DetermineWinnerEmptyDecksWar["הכרז על המנצח (חבילה ריקה במלחמה)"]
     DetermineWinnerEmptyDecksWar --> End
    WarLoopStart -- לא --> DetermineWinner["קביעת מנצח לפי ספירת קלפים"]
    DetermineWinner --> End

    LoopStart -- לא --> DetermineWinner
```

Legenda:
    Start - התחלת התוכנית.
    InitializeDecks - אתחול חבילות הקלפים של המחשב והמשתמש.
    LoopStart - תחילת לולאה, המתבצעת עבור 20 סיבובים.
    CheckEmptyDecks - בדיקה האם אחת מחבילות הקלפים ריקה, אם כן - הכרזת מנצח (חבילה ריקה)
    DetermineWinnerEmptyDecks - הכרזה על המנצח במקרה שאחת החבילות ריקה.
    DrawCards - שליפת הקלף העליון מחבילת הקלפים של כל שחקן.
    CompareCards - בדיקה אם קלף המשתמש גדול יותר מקלף המחשב.
    UserWinsRound - הוספת שני הקלפים לחבילת הקלפים של המשתמש.
    CompareCards2 - בדיקה אם קלף המחשב גדול יותר מקלף המשתמש.
    ComputerWinsRound - הוספת שני הקלפים לחבילת הקלפים של המחשב.
    StartWar - התחלת מלחמה (במקרה של שוויון בין הקלפים).
    WarLoopStart - תחילת לולאה עבור מלחמה.
    CheckEmptyDecksWar - בדיקה האם אחת מחבילות הקלפים ריקה במהלך המלחמה, אם כן - הכרזת מנצח (חבילה ריקה במלחמה)
    DetermineWinnerEmptyDecksWar - הכרזה על המנצח במקרה שאחת החבילות ריקה במהלך המלחמה.
    WarDrawCards - שליפת קלפים נוספים למלחמה.
    CheckWarEmptyCards - בדיקה האם קיימים קלפים להשוואה במלחמה.
    CompareCardsWar - בדיקה אם קלף המשתמש גדול יותר מקלף המחשב במהלך המלחמה.
    UserWinsWarRound - הוספת כל הקלפים לחבילת המשתמש וסיום מלחמה.
    CompareCardsWar2 - בדיקה אם קלף המחשב גדול יותר מקלף המשתמש במהלך המלחמה.
    ComputerWinsWarRound - הוספת כל הקלפים לחבילת המחשב וסיום מלחמה.
    DetermineWinner - קביעת המנצח בסיום 20 סיבובים לפי כמות הקלפים.
    End - סוף התוכנית.

```
```python
import random

def play_war_game():
    """
     משחק מלחמה בין המחשב למשתמש.

     המשחק משוחק על ידי שני שחקנים, המכונים "המחשב" ו"המשתמש".
     בכל סיבוב, כל שחקן חושף את הקלף העליון שלו, והשחקן עם הערך הגבוה יותר של הקלף זוכה בשני הקלפים.
     המנצח הוא השחקן שמצליח לאסוף את כל הקלפים.
    """

    # חבילות הקלפים ההתחלתיות של המחשב והמשתמש. כל חבילה מקבלת חצי מהקלפים 1-10
    computer_deck = list(range(1, 6))
    user_deck = list(range(6, 11))

    # הדפסת מצב התחלתי של החפיסות
    print("חפיסות התחלתיות:")
    print(f"חפיסת המחשב: {computer_deck}")
    print(f"חפיסת המשתמש: {user_deck}")

    # לולאה של 20 סיבובים
    for turn in range(20):
        print(f"\nסיבוב {turn + 1}:")
        
        # בדיקה האם אחת החבילות ריקה, אם כן - סיום המשחק והכרזת מנצח.
        if not computer_deck:
          print("חפיסת המחשב ריקה, ניצחת!")
          return
        if not user_deck:
          print("חפיסת המשתמש ריקה, המחשב ניצח!")
          return
        
        # שליפת הקלף העליון מחבילות השחקנים
        computer_card = computer_deck.pop(0)
        user_card = user_deck.pop(0)

        print(f"המחשב שולף: {computer_card}")
        print(f"המשתמש שולף: {user_card}")

        # השוואת ערכי הקלפים
        if user_card > computer_card:
          print("המשתמש זוכה בסיבוב")
          user_deck.append(user_card)
          user_deck.append(computer_card)
        elif computer_card > user_card:
          print("המחשב זוכה בסיבוב")
          computer_deck.append(computer_card)
          computer_deck.append(user_card)
        else:
            # במקרה של שוויון - מלחמה
            print("מלחמה!")
            war_cards = [computer_card, user_card]  # שמירת הקלפים שכבר נשלפו
            while True:
                if not computer_deck or not user_deck:
                    if not computer_deck:
                         print("חפיסת המחשב ריקה במלחמה, ניצחת!")
                    else:
                        print("חפיסת המשתמש ריקה במלחמה, המחשב ניצח!")
                    return
                
                # שליפת קלפים נוספים למלחמה
                computer_war_card = computer_deck.pop(0) if computer_deck else None
                user_war_card = user_deck.pop(0) if user_deck else None

                war_cards.append(computer_war_card)
                war_cards.append(user_war_card)
                
                # בדיקה אם אין קלפים להשוואה במלחמה
                if computer_war_card is None or user_war_card is None:
                    if not computer_deck:
                         print("חפיסת המחשב ריקה במלחמה, ניצחת!")
                         return
                    else:
                        print("חפיסת המשתמש ריקה במלחמה, המחשב ניצח!")
                    return

                print(f"המחשב שולף קלף נוסף למלחמה: {computer_war_card}")
                print(f"המשתמש שולף קלף נוסף למלחמה: {user_war_card}")

                if user_war_card > computer_war_card:
                    print("המשתמש זוכה במלחמה!")
                    user_deck.extend(war_cards)  # הוספת כל הקלפים למשתמש
                    break
                elif computer_war_card > user_war_card:
                  print("המחשב זוכה במלחמה!")
                  computer_deck.extend(war_cards) # הוספת כל הקלפים למחשב
                  break
                else:
                  print("שוויון נוסף במלחמה! ממשיכים למלחמה נוספת")
                  
        #הדפסת מצב החפיסות בכל סיבוב
        print(f"חפיסת המחשב: {computer_deck}")
        print(f"חפיסת המשתמש: {user_deck}")


    # קביעת המנצח לאחר 20 סיבובים על פי ספירת הקלפים
    if len(user_deck) > len(computer_deck):
        print("\nהמשתמש ניצח במשחק!")
    elif len(computer_deck) > len(user_deck):
        print("\nהמחשב ניצח במשחק!")
    else:
        print("\nתיקו במשחק!")

if __name__ == "__main__":
    play_war_game()
```
<הסברים:>
הקוד מממש את משחק ה"מלחמה" בין המחשב למשתמש.
1. **ייבוא מודול `random`**:
    - `import random`: ייבוא המודול random, שיכול לשמש לאקראיות בעתיד (לא נעשה בו שימוש במשחק הנוכחי, אך יכול להיות רלוונטי לשיפורים).
2.  **הגדרת הפונקציה `play_war_game()`**:
    -  הפונקציה מכילה את הלוגיקה של המשחק "מלחמה".
    -  `computer_deck = list(range(1, 6))`: אתחול חבילת הקלפים של המחשב, המכילה את הערכים 1 עד 5.
    -  `user_deck = list(range(6, 11))`: אתחול חבילת הקלפים של המשתמש, המכילה את הערכים 6 עד 10.
3.  **לולאת הסיבובים `for turn in range(20)`**:
     -  לולאה המבצעת 20 סיבובים של המשחק.
     -  בכל סיבוב:
        - בדיקה אם אחת החבילות ריקה, אם כן - סיום המשחק והכרזת מנצח.
        - `computer_card = computer_deck.pop(0)`: שליפת הקלף העליון מחבילת המחשב.
        -  `user_card = user_deck.pop(0)`: שליפת הקלף העליון מחבילת המשתמש.
        -  השוואת ערכי הקלפים והוספתם לחבילת הזוכה או התחלת מלחמה במקרה של שוויון.
4.  **מלחמה (במקרה של שוויון)**:
     - `war_cards = [computer_card, user_card]`: יצירת רשימה לאיסוף הקלפים למלחמה.
     - לולאת `while True`: לולאה אינסופית המתבצעת עד שאחד השחקנים מנצח במלחמה.
     - שליפת קלפים נוספים למלחמה והשוואה.
     - אם אחד השחקנים מנצח, הקלפים שנאספו במלחמה מתווספים לחבילה שלו.
     - במקרה של שוויון נוסף במלחמה, ממשיכים למלחמה נוספת.
     - במקרה שאחת החבילות ריקה, מוכרז מנצח על בסיס חבילה ריקה.
5. **הכרזת מנצח**:
    -  בסיום 20 הסיבובים, אם אף אחד לא ניצח, נקבע המנצח לפי כמות הקלפים שנותרו לכל שחקן.
6. **הפעלת המשחק**:
    - `if __name__ == "__main__":` בלוק זה מוודא שהקוד ירוץ רק כאשר הוא מופעל כסקריפט ראשי.
    -  `play_war_game()`: קריאה לפונקציה להפעלת המשחק.
