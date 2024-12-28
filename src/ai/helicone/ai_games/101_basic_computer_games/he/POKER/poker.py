### POKER:
```
=================
קושי: 7
-----------------
משחק פוקר פשוט לשחקן אחד נגד המחשב. המשחק כולל חלוקת קלפים, הערכת ידיים, והימור. השחקן מתחיל עם 200$, ויכול להמר עד 10$ בכל סיבוב. המטרה היא להשיג יד פוקר טובה יותר מהמחשב, ולצבור יותר כסף. המשחק מסתיים כאשר לשחקן אין כסף או שהוא בוחר להפסיק.

חוקי המשחק:
1.  המשחק מתחיל עם חלוקת חמישה קלפים לשחקן וחמישה קלפים למחשב.
2.  השחקן מתחיל עם 200$.
3.  לפני ההשוואה עם יד המחשב, השחקן יכול להמר עד 10$.
4.  ידי הפוקר מוערכות לפי הדירוג הבא (מהגבוה לנמוך):
    -   חמישה קלפים מאותו הסוג, רצף שלם (Straight Flush)
    -   ארבעה קלפים מאותו הערך (Four of a Kind)
    -   שלושה קלפים מאותו הערך ושני קלפים מאותו ערך (Full House)
    -   חמישה קלפים מאותו הסוג (Flush)
    -   חמישה קלפים ברצף (Straight)
    -   שלושה קלפים מאותו הערך (Three of a Kind)
    -   שני זוגות (Two Pair)
    -   זוג אחד (One Pair)
    -   יד חלשה (High Card)
5.  המנצח בסיבוב לוקח את סכום ההימור.
6.  אם לידיים יש אותו ערך, הכסף מוחזר (ללא מנצח).
7.  המשחק נמשך עד שהשחקן בוחר לסיים או שאזל לו הכסף.
-----------------
אלגוריתם:
1.  אתחל את כמות הכסף של השחקן ל-200.
2.  הגדר את דירוג הקלפים.
3.  התחל לולאת משחק:
    3.1  חלק 5 קלפים לשחקן ו-5 קלפים למחשב באופן אקראי.
    3.2  הצג את הקלפים של השחקן.
    3.3  בקש מהשחקן לבחור סכום הימור (עד 10).
    3.4  הערך את יד השחקן ואת יד המחשב.
    3.5  השווה את ידי הפוקר:
        - אם יד השחקן טובה יותר, השחקן זוכה בכסף.
        - אם יד המחשב טובה יותר, השחקן מפסיד את סכום ההימור.
        - אם הידיים שוות, הכסף מוחזר.
    3.6  הצג את תוצאת הסיבוב ואת סכום הכסף הנוכחי של השחקן.
    3.7  אם לשחקן אין כסף, סיים את המשחק.
    3.8  שאל את השחקן אם הוא רוצה לשחק שוב. אם לא, סיים את המשחק.
4. סיום המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeMoney["אתחול: <code><b>playerMoney = 200</b></code>"]
    InitializeMoney --> GameLoopStart{"תחילת לולאת משחק"}
    GameLoopStart --> DealCards["<p align='left'>חלק קלפים:
                                 <code><b>playerHand = 5 cards</b></code>
                                 <code><b>computerHand = 5 cards</b></code></p>"]
    DealCards --> DisplayPlayerHand["הצג קלפים של שחקן"]
    DisplayPlayerHand --> GetBet["קלט הימור מהשחקן (עד 10): <code><b>playerBet</b></code>"]
    GetBet --> EvaluateHands["<p align='left'>הערכת ידיים:
                                    <code><b>playerHandRank</b></code>
                                    <code><b>computerHandRank</b></code></p>"]
    EvaluateHands --> CompareHands{"השוואת ידיים: <code><b>playerHandRank > computerHandRank?</b></code>"}
    CompareHands -- Yes --> PlayerWins["<p align='left'>שחקן מנצח:
                                        <code><b>playerMoney += playerBet</b></code></p>"]
    CompareHands -- No --> CompareHandsEqual{"השוואת ידיים: <code><b>playerHandRank == computerHandRank?</b></code>"}
    CompareHandsEqual -- Yes --> Tie["תיקו: <code><b>playerMoney = playerMoney</b></code>"]
    CompareHandsEqual -- No --> PlayerLoses["<p align='left'>שחקן מפסיד:
                                          <code><b>playerMoney -= playerBet</b></code></p>"]
    PlayerWins --> DisplayRoundResult["הצגת תוצאות הסיבוב ויתרת כסף"]
    Tie --> DisplayRoundResult
    PlayerLoses --> DisplayRoundResult
    DisplayRoundResult --> CheckPlayerMoney{"בדיקה: <code><b>playerMoney > 0?</b></code>"}
    CheckPlayerMoney -- Yes --> PlayAgain{"האם לשחק שוב? (כן/לא)"}
     PlayAgain -- Yes --> GameLoopStart
    PlayAgain -- No --> End["סיום"]
    CheckPlayerMoney -- No --> End
```
Legenda:
    Start - התחלת התוכנית.
    InitializeMoney - אתחול כמות הכסף של השחקן ל-200.
    GameLoopStart - תחילת לולאת המשחק.
    DealCards - חלוקת 5 קלפים לשחקן ו-5 קלפים למחשב באופן אקראי.
    DisplayPlayerHand - הצגת הקלפים של השחקן.
    GetBet - קבלת הימור מהשחקן, סכום ההימור יהיה בין 1 ל-10.
    EvaluateHands - הערכת ידי הפוקר של השחקן והמחשב.
    CompareHands - השוואת ידי הפוקר של השחקן והמחשב.
    PlayerWins - השחקן ניצח, הוספת סכום ההימור ליתרת השחקן.
    CompareHandsEqual - בדיקה האם הידיים שוות בערכן.
    Tie - תיקו, לא מתבצע שינוי ביתרת השחקן.
    PlayerLoses - השחקן הפסיד, הפחתת סכום ההימור מיתרת השחקן.
    DisplayRoundResult - הצגת תוצאת הסיבוב ויתרת הכסף של השחקן.
    CheckPlayerMoney - בדיקה האם לשחקן נשאר כסף.
    PlayAgain - שאלה האם השחקן רוצה לשחק שוב.
    End - סיום המשחק.
```

```python
import random

# הגדרת ערכי הקלפים וסוגי הקלפים
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades

# פונקציה ליצירת חפיסת קלפים
def create_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck

# פונקציה לחלוקת קלפים
def deal_cards(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand

# פונקציה להערכת יד פוקר
def evaluate_hand(hand):
    values_in_hand = [card[:-1] for card in hand]
    suits_in_hand = [card[-1] for card in hand]
    
    # מילון הממיר את ערכי הקלפים למספרים
    value_rank = {value: index for index, value in enumerate(values)}
    numeric_values = [value_rank[value] for value in values_in_hand]
    numeric_values.sort()
    
    is_flush = len(set(suits_in_hand)) == 1
    is_straight = all(numeric_values[i+1] == numeric_values[i] + 1 for i in range(len(numeric_values) - 1)) or \
                  (numeric_values == [0,1,2,3,12]) #A,2,3,4,5
   
    value_counts = {}
    for value in values_in_hand:
        value_counts[value] = value_counts.get(value, 0) + 1
    counts = sorted(value_counts.values(), reverse=True)

    if is_straight and is_flush:
        return 9 # Straight Flush
    if counts[0] == 4:
        return 8 # Four of a Kind
    if counts[0] == 3 and counts[1] == 2:
        return 7 # Full House
    if is_flush:
        return 6 # Flush
    if is_straight:
        return 5 # Straight
    if counts[0] == 3:
        return 4 # Three of a Kind
    if counts[0] == 2 and counts[1] == 2:
        return 3 # Two Pair
    if counts[0] == 2:
        return 2 # One Pair
    return 1 # High Card

# פונקציה להמרת דירוג היד למחרוזת קריאה
def get_hand_rank_name(rank):
    rank_names = {
        1: "High Card",
        2: "One Pair",
        3: "Two Pair",
        4: "Three of a Kind",
        5: "Straight",
        6: "Flush",
        7: "Full House",
        8: "Four of a Kind",
        9: "Straight Flush",
    }
    return rank_names.get(rank, "Unknown Hand")

# פונקציה להדפסת היד של השחקן
def display_hand(hand):
    print("היד שלך:")
    print(" ".join(hand))

# פונקציה להמרת קלף למחרוזת קריאה
def format_card(card):
  value = card[:-1]
  suit = card[-1]
  suit_name = {"H":"♥", "D":"♦", "C":"♣", "S":"♠"}.get(suit, suit)
  return f"{value}{suit_name}"

# פונקציה להדפסת היד של השחקן עם תווים מתאימים
def display_formatted_hand(hand):
    print("היד שלך:")
    formatted_cards = [format_card(card) for card in hand]
    print("  ".join(formatted_cards))


# פונקציית משחק פוקר
def play_poker():
    player_money = 200  # כסף התחלתי של השחקן
    print("ברוכים הבאים למשחק פוקר!")
    
    while player_money > 0:
        print(f"יש לך ${player_money}.")
        deck = create_deck() # יצירת חפיסת קלפים חדשה בכל סיבוב
        player_hand = deal_cards(deck, 5)  # חלוקת 5 קלפים לשחקן
        computer_hand = deal_cards(deck, 5)  # חלוקת 5 קלפים למחשב
        
        display_formatted_hand(player_hand)  # הצגת היד של השחקן
        
        while True:
            try:
              player_bet = int(input("בחר סכום הימור (עד 10$): "))  # קבלת הימור מהשחקן
              if 1 <= player_bet <= 10:
                break
              else:
                print("אנא בחר סכום הימור בין 1 ל-10.")
            except ValueError:
                print("אנא הזן מספר שלם.")
    
        player_rank = evaluate_hand(player_hand) # הערכת יד השחקן
        computer_rank = evaluate_hand(computer_hand) # הערכת יד המחשב
        
        print(f"יד השחקן: {get_hand_rank_name(player_rank)}")
        print(f"יד המחשב: {get_hand_rank_name(computer_rank)}")
    
        if player_rank > computer_rank: # אם יד השחקן טובה יותר
            print("ניצחת בסיבוב!")
            player_money += player_bet  # הוספת ההימור לכסף השחקן
        elif player_rank < computer_rank: # אם יד המחשב טובה יותר
            print("הפסדת בסיבוב.")
            player_money -= player_bet  # הפחתת ההימור מכסף השחקן
        else:
             print("תיקו, הכסף מוחזר.") # אם הידיים שוות
    
        print(f"יתרת הכסף שלך כעת: ${player_money}")
    
        if player_money <= 0: # אם אין לשחקן כסף המשחק נגמר
            print("אין לך יותר כסף. המשחק נגמר.")
            break
    
        play_again = input("האם תרצה לשחק שוב? (כן/לא): ")  # שואל את השחקן אם לשחק שוב
        if play_again.lower() != 'כן':
            break
    
    print("תודה ששיחקת!")

# הרצת המשחק
if __name__ == "__main__":
    play_poker()

```
<br>
הסברים:
1. **ייבוא מודול `random`**:
   - `import random`: ייבוא מודול `random` המשמש ליצירת מספרים אקראיים וערבוב קלפים.

2. **הגדרת משתנים גלובליים**:
   - `values`: רשימה של ערכי הקלפים בפוקר (2 עד אס).
   - `suits`: רשימה של סוגי הקלפים (לב, יהלום, תלתן, עלה).

3. **פונקציה `create_deck()`**:
   - יוצרת חפיסת קלפים חדשה.
   - עוברת על כל שילוב אפשרי של ערכי קלפים וסוגים ומוסיפה אותם לרשימה.

4. **פונקציה `deal_cards(deck, num_cards)`**:
   - מחלקת מספר קלפים (num_cards) מתוך חפיסת הקלפים (deck) באופן אקראי.
   - מסירה את הקלפים המחולקים מהחפיסה.

5. **פונקציה `evaluate_hand(hand)`**:
   - מקבלת יד של קלפים ומחזירה את הדירוג שלה (1 עד 9) לפי חוקי הפוקר.
   - מחשבת אם היד היא פלאש, סטרייט, זוג, שלשה, וכו'.
   - ממירה ערכי קלפים למספרים לצרכי השוואה (לדוגמה: אס נחשב ל-12).

6. **פונקציה `get_hand_rank_name(rank)`**:
    - מקבלת דירוג יד ומחזירה את שמה (למשל "זוג", "סטריט", "פלאש", וכו').

7. **פונקציה `display_hand(hand)`**:
    - מקבלת יד קלפים ומדפיסה את הקלפים של השחקן במסך.

8. **פונקציה `format_card(card)`**:
   -  מקבלת קלף כמחרוזת (למשל, "KH") ומחזירה אותו בפורמט קריא עם סמלי הקלפים (למשל, "K♥").
   - נעזרת במילון כדי להחליף את האותיות H, D, C, S בסמלים המתאימים.

9. **פונקציה `display_formatted_hand(hand)`**:
    - מקבלת יד קלפים, מעצבת כל קלף באמצעות הפונקציה `format_card` ומדפיסה את הקלפים המעוצבים על המסך.

10. **פונקציה `play_poker()`**:
    -  מגדירה את ההיגיון המרכזי של משחק הפוקר.
    -  מאחלת לשחקן ברוכים הבאים למשחק.
    -  מאחלת לשחקן ברוכים הבאים למשחק, משחקת עד שלשחקן אין יותר כסף.
    -  מייצרת חפיסת קלפים חדשה, מחלקת קלפים לשחקן ולמחשב בכל סיבוב.
    -  מציגה את היד של השחקן, מבקשת הימור מהשחקן.
    -  מעריכה את היד של השחקן ואת היד של המחשב, ומכריזה על מנצח הסיבוב.
    -  מעדכנת את סכום הכסף של השחקן בהתאם לתוצאות הסיבוב.
    -  אם לשחקן נגמר הכסף, המשחק מסתיים.
    -  שואלת את השחקן האם הוא רוצה לשחק שוב או לסיים את המשחק.
    -  מאחלת לשחקן תודה ששיחק וסיום המשחק.

11. **בלוק `if __name__ == "__main__":`**:
    -  מבטיח שהפונקציה `play_poker()` תופעל רק אם הקובץ מופעל ישירות ולא אם הוא מיובא כמודול.
    -  מפעיל את פונקציית המשחק `play_poker()`.
<br>
