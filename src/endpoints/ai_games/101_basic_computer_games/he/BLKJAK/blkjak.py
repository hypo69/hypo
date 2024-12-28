"""
<BLKJAK>:
=================
קושי: 7
-----------------
בלאק ג'ק הוא משחק קלפים שבו השחקן מתחרה נגד הדילר. מטרת המשחק היא לקבל סכום קלפים קרוב ככל האפשר ל-21, אך לא לעבור אותו (לפרוץ). קלפי הנקובים שווים לערכם הנקוב, קלפי תמונה שווים 10, ואס יכול להיות שווה 1 או 11, תלוי מה טוב יותר ליד.
בגרסה זו של המשחק, השחקן מתחיל עם שני קלפים. לאחר מכן, הוא יכול לבקש עוד קלף (hit) או להישאר עם היד הנוכחית שלו (stand). לאחר שהשחקן סיים, הדילר חושף את הקלפים שלו ומושך קלפים נוספים עד שיש לו לפחות 17. היד עם הסכום הגבוה ביותר (עד 21) מנצחת. אם שחקן או דילר עוברים את 21, הם מפסידים.
חוקי המשחק:
1. משחק נגד הדילר.
2. מטרת המשחק היא לקבל סכום קלפים קרוב ל-21, אבל לא יותר.
3. קלפי מספר שווים לערכם הנקוב.
4. קלפי תמונה (נסיך, מלכה, מלך) שווים 10.
5. אס יכול להיות שווה 1 או 11, תלוי מה טוב יותר ליד.
6. השחקן מתחיל עם שני קלפים.
7. השחקן יכול לבקש קלפים נוספים (hit) או להישאר עם היד שלו (stand).
8. לאחר שהשחקן מסיים, הדילר חושף את הקלפים שלו ומושך קלפים נוספים עד שיש לו לפחות 17.
9. היד עם הסכום הגבוה ביותר (עד 21) מנצחת.
10. אם השחקן או הדילר עוברים את 21, הם מפסידים.
-----------------
אלגוריתם:
1. אתחל את סכום הקלפים של השחקן והדילר לאפס.
2. שחקן מקבל 2 קלפים, הדילר מקבל 2 קלפים (אחד גלוי).
3. שאל את השחקן האם הוא רוצה 'Hit' (לקבל עוד קלף) או 'Stand' (לעצור).
   3.1 אם השחקן בחר 'Hit', תן לו קלף נוסף והוסף את ערכו לסכום הקלפים של השחקן.
   3.2 אם סכום הקלפים של השחקן גדול מ-21, השחקן מפסיד והמשחק מסתיים.
   3.3 אם השחקן בחר 'Stand', עבור לשלב 4.
4. הדילר חושף את הקלף הנסתר שלו.
5. כל עוד סכום הקלפים של הדילר קטן מ-17, הדילר מושך קלפים נוספים.
   5.1 אם סכום הקלפים של הדילר גדול מ-21, הדילר מפסיד והמשחק מסתיים.
6. השווה את סכום הקלפים של השחקן ושל הדילר.
   6.1 אם סכום הקלפים של השחקן גדול מסכום הקלפים של הדילר, השחקן מנצח.
   6.2 אם סכום הקלפים של הדילר גדול מסכום הקלפים של השחקן, הדילר מנצח.
   6.3 אם סכום הקלפים של השחקן ושל הדילר שווים, המשחק מסתיים בתיקו.
7. הצג את תוצאת המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול משתנים:
    <code><b>
    playerScore = 0
    dealerScore = 0
    </b></code></p>"]
    InitializeGame --> DealInitialCards["<p align='left'>חלקת קלפים:
    <code><b>
    player получает 2 карты
    dealer получает 2 карты (1 скрыта)
    </b></code></p>"]
    DealInitialCards --> PlayerTurnStart{"תחילת תור שחקן:
    <code><b>
    выбор 'Hit' или 'Stand'
    </b></code>"}
    PlayerTurnStart -- "Hit" --> PlayerHit["<p align='left'>השחקן מקבל קלף:
    <code><b>
    playerScore = playerScore + value(new card)
    </b></code></p>"]
    PlayerHit --> CheckPlayerBust{"<p align='left'>בדיקת פריצה:
    <code><b>
    playerScore > 21?
    </b></code></p>"}
    CheckPlayerBust -- כן --> PlayerBust["<p align='left'>הודעה:
    <code><b>
    PLAYER BUST - DEALER WINS!
    </b></code></p>"]
    PlayerBust --> End["סוף"]
    CheckPlayerBust -- לא --> PlayerTurnStart
    PlayerTurnStart -- "Stand" --> DealerTurnStart{"תחילת תור הדילר:
    <code><b>
    раскрытие скрытой карты дилера
    </b></code>"}
    DealerTurnStart --> DealerDraws{"<p align='left'>הדילר מושך קלפים:
    <code><b>
        while dealerScore < 17:
            dealerScore = dealerScore + value(new card)
    </b></code></p>"}
    DealerDraws --> CheckDealerBust{"<p align='left'>בדיקת פריצה:
        <code><b>
            dealerScore > 21?
        </b></code></p>"}
    CheckDealerBust -- כן --> DealerBust["<p align='left'>הודעה:
        <code><b>
            DEALER BUST - PLAYER WINS!
        </b></code></p>"]
    DealerBust --> End
    CheckDealerBust -- לא --> CompareScores{"השוואת ניקוד:
    <code><b>
        Compare player scores with dealer scores
    </b></code>"}
    CompareScores --> DetermineWinner{"<p align='left'>קביעת מנצח:
    <code><b>
        if playerScore > dealerScore:
            PLAYER WINS
        else if dealerScore > playerScore:
            DEALER WINS
        else:
            PUSH
    </b></code></p>"}
    DetermineWinner --> OutputResult["<p align='left'>הצגת תוצאה:
    <code><b>
        result (PLAYER WINS, DEALER WINS or PUSH)
    </b></code></p>"]
    OutputResult --> End
```
Legenda:
    Start - תחילת המשחק.
    InitializeGame - אתחול משתני המשחק, כגון ניקוד השחקן והדילר.
    DealInitialCards - חלוקת שני קלפים לשחקן ושני קלפים לדילר (אחד גלוי).
    PlayerTurnStart - תחילת תור השחקן, בו הוא בוחר האם לקחת קלף נוסף (Hit) או לעצור (Stand).
    PlayerHit - השחקן מקבל קלף נוסף, והערך שלו מתווסף לניקוד השחקן.
    CheckPlayerBust - בדיקה האם ניקוד השחקן עבר את 21 (Bust).
    PlayerBust - אם ניקוד השחקן עבר 21, הוא מפסיד.
    DealerTurnStart - תחילת תור הדילר, בו הוא חושף את הקלף הנסתר שלו.
    DealerDraws - הדילר מושך קלפים עד שהוא מגיע לניקוד של 17 ומעלה.
    CheckDealerBust - בדיקה האם ניקוד הדילר עבר את 21 (Bust).
    DealerBust - אם ניקוד הדילר עבר 21, הוא מפסיד.
    CompareScores - השוואת הניקוד של השחקן והדילר.
    DetermineWinner - קביעת המנצח על פי הניקוד.
    OutputResult - הצגת תוצאת המשחק.
    End - סוף המשחק.
"""
import random

# פונקציה המחזירה ערך של קלף
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 11 #אס מתחיל כ 11, נשנה ל 1 בהמשך אם יהיה צורך
    return int(card)

# פונקציה לחישוב סכום היד (עם טיפול באס)
def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_val = card_value(card)
        value += card_val
        if card == 'A':
            aces += 1
    # אם היד גדולה מ 21 ויש אס, נשנה את ערך האס ל 1.
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

# פונקציה ליצירת חפיסת קלפים
def create_deck():
    suits = ['H', 'D', 'C', 'S'] # Hearts, Diamonds, Clubs, Spades
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# פונקציה לחלוקת קלף
def deal_card(deck):
    return deck.pop()

# פונקציה להצגת יד
def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print(" [Hidden], " + ", ".join(hand[1:]))
    else:
        print(", ".join(hand))

# פונקציה לניהול משחק בלק ג'ק
def play_blackjack():
    deck = create_deck()
    player_hand = []
    dealer_hand = []
    # חלוקת 2 קלפים לשחקן ולדילר
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))
    
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)
        
    print("הקלפים שלך: ")
    display_hand(player_hand)
    print("הקלפים של הדילר: ")
    display_hand(dealer_hand, hide_first_card=True)
    
    # תור השחקן
    while True:
        print("הניקוד שלך: " ,player_score)
        action = input("רוצה 'Hit' (לקחת עוד קלף) או 'Stand' (לעצור)? (h/s): ").lower()
        
        if action == 'h':
            player_hand.append(deal_card(deck))
            player_score = calculate_hand_value(player_hand)
            print("הקלפים שלך: ")
            display_hand(player_hand)
            if player_score > 21:
                print("הניקוד שלך: ", player_score)
                print("פרצת! הפסדת!")
                return
        elif action == 's':
            break
        else:
            print("בבקשה תבחר בין 'h' ל 's'")

    # תור הדילר
    print("תור הדילר")
    print("הקלפים של הדילר: ")
    display_hand(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deal_card(deck))
        dealer_score = calculate_hand_value(dealer_hand)
        print("הקלפים של הדילר: ")
        display_hand(dealer_hand)
    
    print("הניקוד שלך: ", player_score)
    print("הניקוד של הדילר: ", dealer_score)
        
    # הכרעת המשחק
    if dealer_score > 21:
        print("הדילר פרץ! ניצחת!")
    elif player_score > dealer_score or dealer_score > 21:
            print("ניצחת!")
    elif dealer_score > player_score:
            print("הדילר ניצח!")
    else:
        print("תיקו!")

# הפעלת המשחק
if __name__ == "__main__":
    play_blackjack()

"""
הסבר מפורט לקוד:
1. **ייבוא מודול random**:
   - `import random`: מייבא את מודול `random` עבור פונקציות ליצירת ערכים אקראיים (כמו ערבוב החפיסה).
2. **פונקציה card_value(card)**:
   - מקבלת קלף (מחרוזת) ומחזירה את הערך המספרי שלו.
   - קלפי תמונה (J, Q, K) שווים 10.
   - אס (A) מוחזר כ-11, אך ערכו יכול להשתנות בהמשך בהתאם ליד.
   - קלפים מספריים מוחזרים כערכם המספרי (מספר שלם).
3. **פונקציה calculate_hand_value(hand)**:
   - מקבלת יד (רשימת קלפים) ומחשבת את סכום ערכיה.
   - מעדכנת את הערך של אס ל-1 אם סכום היד עולה על 21 ויש אסים (מטפלת בפציעה).
4. **פונקציה create_deck()**:
   - יוצרת חפיסת קלפים סטנדרטית:
     - suits - רשימה של סוגי קלפים (לב, יהלום, תלתן, עלה).
     - ranks - רשימה של ערכי קלפים (2-10, J, Q, K, A).
     - יוצרת חפיסה מלאה (52 קלפים) באמצעות רשימה מובנית, ומערבבת אותה.
5. **פונקציה deal_card(deck)**:
    - מקבלת חפיסת קלפים (רשימה) ומחזירה קלף אקראי מחפיסה (מוציאה מהרשימה).
6. **פונקציה display_hand(hand, hide_first_card=False)**:
   - מקבלת יד של קלפים ומציגה אותה.
   - אם hide_first_card=True, הקלף הראשון מוסתר (משמש להצגת היד של הדילר).
7. **פונקציה play_blackjack()**:
    - יוצרת חפיסת קלפים חדשה, ידיים לשחקן ולדילר.
    - מחלקת 2 קלפים לשחקן ו-2 לדילר (אחד נסתר).
    - מציגה את היד של השחקן ואת היד של הדילר (עם קלף נסתר).
    - תור השחקן:
        - השחקן בוחר האם לבקש עוד קלף (Hit) או לעצור (Stand).
        - אם השחקן מבקש עוד קלף (Hit), מקבל קלף חדש.
        - אם השחקן פורץ (סכום הקלפים מעל 21), המשחק נגמר.
        - אם השחקן עוצר (Stand), עוברים לתור הדילר.
    - תור הדילר:
        - הדילר מושך קלפים עד שסכום הקלפים שלו מגיע ל-17 ומעלה.
        - אם הדילר פורץ, השחקן מנצח.
    - הכרעת המשחק:
      - בודקת מי ניצח, מי הפסיד, או האם יש תיקו, ומדפיסה את התוצאה.
8. **if __name__ == "__main__":**:
    - מוודא שהפונקציה `play_blackjack()` תרוץ רק כאשר קובץ זה רץ כסקריפט ראשי, ולא אם הוא מיובא כמודול.
    - מפעיל את המשחק.
"""
