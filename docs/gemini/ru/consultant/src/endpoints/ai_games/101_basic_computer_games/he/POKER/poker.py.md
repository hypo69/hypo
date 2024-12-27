# ניתוח קוד מודול `poker.py`

**איכות הקוד**
7/10
*   **יתרונות**
    *   קוד ברור וקל לקריאה עם חלוקה לפונקציות לוגיות.
    *   הקוד מיועד למשחק פוקר בסיסי, וכולל את כל הפונקציונליות הנדרשת (חלוקת קלפים, הערכת ידיים, הימור וכו').
    *   שימוש נכון במשתנים ובמבני נתונים כמו רשימות ומילונים.
    *   הקוד כולל הסברים מפורטים על הלוגיקה של המשחק והפונקציות.
    *   הקוד כולל תרשים זרימה של המשחק.
    *   קיימת פונקציה להדפסת קלפים בפורמט קריא למשתמש.
*   **חסרונות**
    *   הקוד לא כולל טיפול בשגיאות בצורה מלאה (לדוגמא, בדיקת תקינות הקלט מהמשתמש מעבר להמרת המחרוזת למספר).
    *   הקוד לא כולל תיעוד בפורמט reStructuredText (RST) כמבוקש.
    *   אין שימוש ב logger לרישום הודעות שגיאה.
    *   הקוד לא משתמש ב `j_loads` או `j_loads_ns` לקריאת נתונים.
    *   יש חוסר עקביות בשימוש במרכאות יחידות/כפולות במחרוזות.

**המלצות לשיפור**

1.  **תיעוד:**
    *   יש להוסיף תיעוד מפורט לכל הפונקציות והמודול בפורמט reStructuredText (RST).
2.  **טיפול בשגיאות:**
    *   יש להשתמש ב `try-except` בצורה מושכלת ולשלב שימוש ב `logger.error` לרישום שגיאות.
3.  **קריאת נתונים:**
    *   אם יש קבצי נתונים, יש להשתמש ב `j_loads` או `j_loads_ns` מ `src.utils.jjson` לקריאתם.
4.  **הפרדה בין לוגיקה לתצוגה:**
    *   יש להפריד את הלוגיקה של המשחק מן התצוגה למשתמש כדי לשפר את הניידות של הקוד.
5.  **אחידות במרכאות:**
    *   יש להשתמש במרכאות יחידות (' ') באופן עקבי במחרוזות.
6. **הוספת בדיקות תקינות קלט:**
   *   בדיקות נוספות לקלט המשתמש (מעבר להמרת מחרוזת למספר) כדי למנוע קריסת התוכנית. לדוגמא: האם הקלט הוא מספר שלם? האם הוא בתחום המותר (1-10)?

**קוד משופר**

```python
"""
מודול זה מממש משחק פוקר בסיסי לשחקן יחיד נגד המחשב.
=====================================================

המשחק כולל חלוקת קלפים, הערכת ידיים, והימור. השחקן מתחיל עם 200$, ויכול להמר עד 10$ בכל סיבוב.
המטרה היא להשיג יד פוקר טובה יותר מהמחשב, ולצבור יותר כסף. המשחק מסתיים כאשר לשחקן אין כסף או שהוא בוחר להפסיק.

חוקי המשחק:
1. המשחק מתחיל עם חלוקת חמישה קלפים לשחקן וחמישה קלפים למחשב.
2. השחקן מתחיל עם 200$.
3. לפני ההשוואה עם יד המחשב, השחקן יכול להמר עד 10$.
4. ידי הפוקר מוערכות לפי הדירוג הבא (מהגבוה לנמוך):
   - חמישה קלפים מאותו הסוג, רצף שלם (Straight Flush)
   - ארבעה קלפים מאותו הערך (Four of a Kind)
   - שלושה קלפים מאותו הערך ושני קלפים מאותו ערך (Full House)
   - חמישה קלפים מאותו הסוג (Flush)
   - חמישה קלפים ברצף (Straight)
   - שלושה קלפים מאותו הערך (Three of a Kind)
   - שני זוגות (Two Pair)
   - זוג אחד (One Pair)
   - יד חלשה (High Card)
5. המנצח בסיבוב לוקח את סכום ההימור.
6. אם לידיים יש אותו ערך, הכסף מוחזר (ללא מנצח).
7. המשחק נמשך עד שהשחקן בוחר לסיים או שאזל לו הכסף.

"""
import random
from src.logger.logger import logger  # ייבוא logger לרישום שגיאות


# הגדרת ערכי הקלפים וסוגי הקלפים
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades


def create_deck():
    """
    יוצרת חפיסת קלפים סטנדרטית.

    :return: רשימה המייצגת חפיסת קלפים.
    :rtype: list
    """
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck


def deal_cards(deck, num_cards):
    """
    מחלקת מספר קלפים מחפיסת קלפים נתונה.

    :param deck: חפיסת הקלפים ממנה יחולקו הקלפים.
    :type deck: list
    :param num_cards: מספר הקלפים לחלק.
    :type num_cards: int
    :return: רשימה של קלפים שחולקו.
    :rtype: list
    """
    hand = []
    for _ in range(num_cards):
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand


def evaluate_hand(hand):
    """
    מעריכה את ערך יד הפוקר.

    :param hand: רשימה של קלפים ביד.
    :type hand: list
    :return: דירוג היד (1-9).
    :rtype: int
    """
    values_in_hand = [card[:-1] for card in hand] #  מחלץ את הערכים של הקלפים מהיד
    suits_in_hand = [card[-1] for card in hand] #  מחלץ את סוגי הקלפים מהיד
    
    # מילון הממיר את ערכי הקלפים למספרים
    value_rank = {value: index for index, value in enumerate(values)}
    numeric_values = [value_rank[value] for value in values_in_hand] # ממיר את הערכים לערכים מספריים
    numeric_values.sort() #  ממיין את הערכים המספריים בסדר עולה
    
    is_flush = len(set(suits_in_hand)) == 1  # בדיקה האם כל הקלפים מאותו הסוג
    is_straight = all(numeric_values[i+1] == numeric_values[i] + 1 for i in range(len(numeric_values) - 1)) or \
                  (numeric_values == [0,1,2,3,12]) # בדיקה האם הקלפים הם ברצף או רצף מיוחד A,2,3,4,5
   
    value_counts = {}
    for value in values_in_hand:
        value_counts[value] = value_counts.get(value, 0) + 1 # סופר את הערכים של הקלפים
    counts = sorted(value_counts.values(), reverse=True)  # ממיין את ספירות הערכים בסדר יורד

    if is_straight and is_flush:
        return 9  # Straight Flush
    if counts[0] == 4:
        return 8  # Four of a Kind
    if counts[0] == 3 and counts[1] == 2:
        return 7  # Full House
    if is_flush:
        return 6  # Flush
    if is_straight:
        return 5  # Straight
    if counts[0] == 3:
        return 4  # Three of a Kind
    if counts[0] == 2 and counts[1] == 2:
        return 3  # Two Pair
    if counts[0] == 2:
        return 2  # One Pair
    return 1  # High Card


def get_hand_rank_name(rank):
    """
    מחזירה את שם הדירוג של היד כטקסט.

    :param rank: דירוג היד (1-9).
    :type rank: int
    :return: שם הדירוג של היד.
    :rtype: str
    """
    rank_names = {
        1: 'High Card',
        2: 'One Pair',
        3: 'Two Pair',
        4: 'Three of a Kind',
        5: 'Straight',
        6: 'Flush',
        7: 'Full House',
        8: 'Four of a Kind',
        9: 'Straight Flush',
    }
    return rank_names.get(rank, 'Unknown Hand')


def format_card(card):
    """
    מעצבת קלף למחרוזת קריאה עם סמלי קלפים מתאימים.

    :param card: מחרוזת המייצגת קלף (למשל, 'KH').
    :type card: str
    :return: מחרוזת המייצגת את הקלף עם סמלי קלפים (למשל, 'K♥').
    :rtype: str
    """
    value = card[:-1]  # חילוץ ערך הקלף
    suit = card[-1]  # חילוץ סוג הקלף
    suit_name = {'H': '♥', 'D': '♦', 'C': '♣', 'S': '♠'}.get(suit, suit) # המרת האות לסמל מתאים
    return f'{value}{suit_name}'  # החזרת קלף בפורמט מעוצב


def display_formatted_hand(hand):
    """
    מדפיסה את היד של השחקן בפורמט מעוצב.

    :param hand: רשימה של קלפים ביד.
    :type hand: list
    """
    print('היד שלך:')
    formatted_cards = [format_card(card) for card in hand] #  מעצב כל קלף ברשימה
    print('  '.join(formatted_cards)) # מדפיס את היד המעוצבת


def play_poker():
    """
    מפעילה את המשחק פוקר.
    """
    player_money = 200  # כסף התחלתי של השחקן
    print('ברוכים הבאים למשחק פוקר!')

    while player_money > 0:
        print(f'יש לך ${player_money}.')
        deck = create_deck()  # יוצר חפיסת קלפים חדשה בכל סיבוב
        player_hand = deal_cards(deck, 5)  # חלוקת 5 קלפים לשחקן
        computer_hand = deal_cards(deck, 5)  # חלוקת 5 קלפים למחשב
        
        display_formatted_hand(player_hand)  # מציג את היד של השחקן
        
        while True:
            try:
                player_bet = input('בחר סכום הימור (עד 10$): ') # קבלת הימור מהשחקן
                player_bet = int(player_bet)
                if 1 <= player_bet <= 10:
                  break
                else:
                  print('אנא בחר סכום הימור בין 1 ל-10.')
            except ValueError:
                logger.error('קלט לא תקין, אנא הזן מספר שלם')
                print('אנא הזן מספר שלם.')
            except Exception as ex:
                logger.error(f'אירעה שגיאה לא צפויה: {ex}')
                print('אירעה שגיאה, נסה שוב.')

        player_rank = evaluate_hand(player_hand)  # הערכת יד השחקן
        computer_rank = evaluate_hand(computer_hand) # הערכת יד המחשב

        print(f'יד השחקן: {get_hand_rank_name(player_rank)}')
        print(f'יד המחשב: {get_hand_rank_name(computer_rank)}')

        if player_rank > computer_rank:  # אם יד השחקן טובה יותר
            print('ניצחת בסיבוב!')
            player_money += player_bet  # הוספת ההימור לכסף השחקן
        elif player_rank < computer_rank:  # אם יד המחשב טובה יותר
            print('הפסדת בסיבוב.')
            player_money -= player_bet  # הפחתת ההימור מכסף השחקן
        else:
            print('תיקו, הכסף מוחזר.')  # אם הידיים שוות

        print(f'יתרת הכסף שלך כעת: ${player_money}')

        if player_money <= 0:  # אם אין לשחקן כסף המשחק נגמר
            print('אין לך יותר כסף. המשחק נגמר.')
            break

        play_again = input('האם תרצה לשחק שוב? (כן/לא): ')  # שואל את השחקן אם לשחק שוב
        if play_again.lower() != 'כן':
            break
    
    print('תודה ששיחקת!')


# הרצת המשחק
if __name__ == '__main__':
    play_poker()
```