<WAR>:
=================
קושי: 5
-----------------
משחק מלחמה הוא משחק קלפים לשני שחקנים, כאשר כל שחקן מקבל מחצית מחפיסת קלפים רגילה. כל שחקן חושף קלף מהחפיסה שלו, והשחקן עם הקלף הגבוה יותר לוקח את שני הקלפים. כאשר הקלפים שווים, מתרחשת "מלחמה", בה כל שחקן חושף קלף נוסף והגבוה יותר לוקח את כל הקלפים. המשחק ממשיך עד שאחד השחקנים לוקח את כל הקלפים.
חוקי המשחק:
1. שני שחקנים משתתפים במשחק.
2. חפיסת קלפים סטנדרטית (ללא ג'וקרים) מחולקת שווה בשווה בין שני השחקנים.
3. כל שחקן חושף קלף מהחפיסה שלו.
4. השחקן עם הקלף הגבוה יותר לוקח את שני הקלפים ומניח אותם בתחתית החפיסה שלו.
5. אם הקלפים שווים, מתרחשת "מלחמה": כל שחקן חושף קלף נוסף, והגבוה לוקח את כל הקלפים.
6. אם גם קלפי המלחמה שווים, מלחמה נוספת מתרחשת.
7. המשחק נמשך עד שאחד השחקנים לוקח את כל הקלפים.
8. ערכי הקלפים: 2-10 לפי הערך הנקוב, J=11, Q=12, K=13, A=14.
-----------------
אלגוריתם:
1. צור חפיסת קלפים סטנדרטית (52 קלפים).
2. ערבב את החפיסה.
3. חלק את החפיסה שווה בשווה בין שני השחקנים.
4. התחל לולאה "כל עוד שני השחקנים מחזיקים קלפים":
   4.1 כל שחקן חושף קלף.
   4.2 השווה את הקלפים:
       4.2.1 אם קלף שחקן 1 גבוה, שחקן 1 לוקח את הקלפים.
       4.2.2 אם קלף שחקן 2 גבוה, שחקן 2 לוקח את הקלפים.
       4.2.3 אם הקלפים שווים, התחל "מלחמה":
          4.2.3.1 כל עוד יש מספיק קלפים לשחקנים, כל שחקן חושף קלף נוסף.
          4.2.3.2 השווה את קלפי המלחמה: השחקן עם הקלף הגבוה לוקח את כל הקלפים שנאספו עד כה.
   4.3 אם נגמרו הקלפים לאחד השחקנים, סיים את הלולאה.
5. בדוק מי השחקן עם יותר קלפים: הכרז על המנצח.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> CreateDeck["יצירת חפיסת קלפים (52 קלפים)"]
    CreateDeck --> ShuffleDeck["ערבוב חפיסת הקלפים"]
    ShuffleDeck --> DistributeCards["חלוקת חפיסת הקלפים שווה בשווה בין שני שחקנים"]
    DistributeCards --> GameLoopStart{"תחילת לולאת המשחק: כל עוד לשני השחקנים יש קלפים"}
    GameLoopStart -- "כן" --> Player1DrawsCard["שחקן 1 שולף קלף"]
    Player1DrawsCard --> Player2DrawsCard["שחקן 2 שולף קלף"]
    Player2DrawsCard --> CompareCards{"השוואת הקלפים"}
    CompareCards -- "קלף שחקן 1 גבוה" --> Player1WinsRound["שחקן 1 לוקח את הקלפים"]
    Player1WinsRound --> GameLoopStart
    CompareCards -- "קלף שחקן 2 גבוה" --> Player2WinsRound["שחקן 2 לוקח את הקלפים"]
    Player2WinsRound --> GameLoopStart
    CompareCards -- "הקלפים שווים" --> WarStart["תחילת מלחמה"]
    WarStart --> CheckWarCards{"בדיקה: האם יש מספיק קלפים למלחמה?"}
    CheckWarCards -- "כן" --> Player1DrawsWarCard["שחקן 1 שולף קלף מלחמה"]
    Player1DrawsWarCard --> Player2DrawsWarCard["שחקן 2 שולף קלף מלחמה"]
    Player2DrawsWarCard --> CompareWarCards{"השוואת קלפי מלחמה"}
    CompareWarCards -- "קלף שחקן 1 גבוה" --> Player1WinsWar["שחקן 1 לוקח את הקלפים של המלחמה"]
    Player1WinsWar --> GameLoopStart
   CompareWarCards -- "קלף שחקן 2 גבוה" --> Player2WinsWar["שחקן 2 לוקח את הקלפים של המלחמה"]
    Player2WinsWar --> GameLoopStart
   CompareWarCards -- "הקלפים שווים" --> WarStart
    CheckWarCards -- "לא" --> CheckWinner["בדיקת מנצח"]
     GameLoopStart -- "לא" --> CheckWinner
    CheckWinner --> OutputWinner["הצגת המנצח"]
    OutputWinner --> End["סוף"]
```
Legenda:
    Start - התחלת התוכנית.
    CreateDeck - יצירת חפיסת קלפים סטנדרטית (52 קלפים).
    ShuffleDeck - ערבוב הקלפים בחפיסה.
    DistributeCards - חלוקת החפיסה שווה בשווה בין שני השחקנים.
    GameLoopStart - תחילת הלולאה, הממשיכה כל עוד לשני השחקנים יש קלפים.
    Player1DrawsCard - שחקן 1 שולף קלף מהחפיסה שלו.
    Player2DrawsCard - שחקן 2 שולף קלף מהחפיסה שלו.
    CompareCards - השוואת הקלפים של שני השחקנים.
    Player1WinsRound - שחקן 1 לוקח את הקלפים של הסיבוב.
    Player2WinsRound - שחקן 2 לוקח את הקלפים של הסיבוב.
    WarStart - תחילת מצב "מלחמה" כאשר הקלפים שווים.
    CheckWarCards - בדיקה האם יש מספיק קלפים לשחקנים להמשיך את המלחמה.
    Player1DrawsWarCard - שחקן 1 שולף קלף מלחמה.
    Player2DrawsWarCard - שחקן 2 שולף קלף מלחמה.
    CompareWarCards - השוואת קלפי המלחמה של שני השחקנים.
    Player1WinsWar - שחקן 1 לוקח את הקלפים של המלחמה.
    Player2WinsWar - שחקן 2 לוקח את הקלפים של המלחמה.
    CheckWinner - בדיקה מי ניצח במשחק (השחקן עם כל הקלפים).
    OutputWinner - הצגת הודעת ניצחון למנצח.
    End - סוף המשחק.
"""
import random

# פונקציה ליצירת חפיסת קלפים סטנדרטית
def create_deck():
    suits = ["C", "D", "H", "S"]  # מועדונים, יהלומים, לבבות, עלים
    ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

# פונקציה להמרת ערך קלף למספר לצורך השוואה
def card_value(card):
    rank = card[0]
    if rank == "A":
        return 14
    elif rank == "K":
        return 13
    elif rank == "Q":
        return 12
    elif rank == "J":
        return 11
    else:
        return int(rank)

# פונקציה לשיחוק חפיסת קלפים
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# פונקציה לחלוקת קלפים בין שני שחקנים
def deal_cards(deck):
    half = len(deck) // 2
    player1_cards = deck[:half]
    player2_cards = deck[half:]
    return player1_cards, player2_cards

# פונקציה המדמה סיבוב במשחק
def play_round(player1_cards, player2_cards):
    player1_card = player1_cards.pop(0)
    player2_card = player2_cards.pop(0)
    print(f"שחקן 1: {player1_card}, שחקן 2: {player2_card}")

    cards_in_play = [player1_card, player2_card]
    
    # בדיקה מי ניצח בסיבוב
    player1_value = card_value(player1_card)
    player2_value = card_value(player2_card)

    if player1_value > player2_value:
        print("שחקן 1 מנצח את הסיבוב")
        player1_cards.extend(cards_in_play)
        return player1_cards, player2_cards, False
    elif player2_value > player1_value:
        print("שחקן 2 מנצח את הסיבוב")
        player2_cards.extend(cards_in_play)
        return player1_cards, player2_cards, False
    else:
        print("מלחמה!")
        return war(player1_cards, player2_cards, cards_in_play)
    
# פונקציה המדמה מצב מלחמה
def war(player1_cards, player2_cards, cards_in_play):
    # בדיקה אם יש מספיק קלפים למלחמה
    if len(player1_cards) < 2 or len(player2_cards) < 2:
        print("לא מספיק קלפים למלחמה")
        return player1_cards, player2_cards, True # החזרת True כדי לסיים את המשחק
    
    # שולפים קלפים למלחמה
    player1_war_cards = [player1_cards.pop(0), player1_cards.pop(0)]
    player2_war_cards = [player2_cards.pop(0), player2_cards.pop(0)]
    print(f"קלפי מלחמה שחקן 1: {player1_war_cards[1]}, שחקן 2: {player2_war_cards[1]}")

    cards_in_play.extend(player1_war_cards)
    cards_in_play.extend(player2_war_cards)

    # השוואת קלפי המלחמה
    player1_war_value = card_value(player1_war_cards[1])
    player2_war_value = card_value(player2_war_cards[1])
    
    if player1_war_value > player2_war_value:
        print("שחקן 1 מנצח במלחמה")
        player1_cards.extend(cards_in_play)
        return player1_cards, player2_cards, False
    elif player2_war_value > player1_war_value:
        print("שחקן 2 מנצח במלחמה")
        player2_cards.extend(cards_in_play)
        return player1_cards, player2_cards, False
    else:
        print("מלחמה נוספת!")
        return war(player1_cards, player2_cards, cards_in_play)

# פונקציה המדמה את המשחק
def play_war():
    deck = create_deck()
    deck = shuffle_deck(deck)
    player1_cards, player2_cards = deal_cards(deck)

    round_number = 0
    while player1_cards and player2_cards:
        round_number += 1
        print(f"\nסיבוב {round_number}")
        player1_cards, player2_cards, game_over = play_round(player1_cards, player2_cards)
        if game_over:
            break

    # בדיקה מי ניצח במשחק
    if len(player1_cards) > len(player2_cards):
        print("\nשחקן 1 ניצח!")
    elif len(player2_cards) > len(player1_cards):
        print("\nשחקן 2 ניצח!")
    else:
        print("\nתיקו!")

if __name__ == "__main__":
    play_war()

"""
הסבר הקוד:
1.  **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש לערבוב הקלפים.
2.  **פונקציה `create_deck()`**:
    - יוצרת חפיסת קלפים סטנדרטית (52 קלפים) ומחזירה אותה.
3.  **פונקציה `card_value(card)`**:
    - מקבלת קלף ומחזירה את ערכו המספרי (A=14, K=13, Q=12, J=11, שאר הערכים לפי מספרם).
4.  **פונקציה `shuffle_deck(deck)`**:
    - מקבלת חפיסת קלפים ומערבבת אותה באופן אקראי באמצעות הפונקציה `random.shuffle()`.
5.  **פונקציה `deal_cards(deck)`**:
    - מחלקת את חפיסת הקלפים לשני שחקנים שווה בשווה.
6.  **פונקציה `play_round(player1_cards, player2_cards)`**:
    - מדמה סיבוב אחד של המשחק.
    - כל שחקן שולף קלף מהחפיסה שלו.
    - משווה בין ערכי הקלפים וקובעת מי מנצח.
    - אם יש תיקו, קוראת לפונקציה `war` למצב "מלחמה".
7.  **פונקציה `war(player1_cards, player2_cards, cards_in_play)`**:
    - מדמה מצב של "מלחמה".
    - כל שחקן שולף 2 קלפים מהחפיסה.
    - משווה את קלפי המלחמה וקובעת מי מנצח את המלחמה.
    - מחזירה את הקלפים המעודכנים ואת מצב המשחק.
8.  **פונקציה `play_war()`**:
    - הפונקציה הראשית שמנהלת את המשחק.
    - יוצרת ומערבבת את חפיסת הקלפים, ומחלקת לשני השחקנים.
    - ממשיכה סיבובים עד שאחד השחקנים לוקח את כל הקלפים או שאחד השחקנים אין לו מספיק קלפים למלחמה.
    - בסוף המשחק מדפיסה את המנצח.
9.  **`if __name__ == "__main__":`**:
    - מבטיח שהפונקציה `play_war()` תפעל רק כאשר הקובץ מופעל ישירות.
"""
