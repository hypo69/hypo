"""
MNOPLY:
=================
קושי: 4
-----------------
משחק מרובה משתתפים בו כל שחקן מתחיל עם כמות מסוימת של כסף, מגלגל קוביות ונע על גבי לוח המשחק. על הלוח ישנם נכסים שניתן לרכוש, והשחקנים משלמים שכר דירה כאשר הם נוחתים על נכס בבעלות שחקן אחר. המטרה היא להישאר השחקן האחרון עם כסף.

חוקי המשחק:
1. המשחק מתנהל בין 2-4 שחקנים.
2. כל שחקן מתחיל עם 1000 דולר.
3. השחקנים מתחלפים בתורם, כאשר בכל תור הם מטילים קוביות ומתקדמים על הלוח.
4. כאשר שחקן נוחת על נכס פנוי, יש לו אפשרות לרכוש אותו.
5. כאשר שחקן נוחת על נכס בבעלות שחקן אחר, הוא צריך לשלם שכר דירה.
6. אם שחקן מגיע ל-0 דולר או פחות, הוא מפסיד.
7. המשחק נמשך עד שנותר שחקן אחד עם כסף.

-----------------
אלגוריתם:
1. אתחל את מספר השחקנים, יתרה לכל שחקן, מיקום השחקנים ובעלות הנכסים.
2. התחל לולאה "כל עוד יש יותר משחקן אחד":
    2.1 עבור על רשימת השחקנים, כל עוד שחקן לא הפסיד:
        2.1.1 הטל קוביה וקדם את השחקן על הלוח.
        2.1.2 אם השחקן נוחת על נכס פנוי: שאל את השחקן האם הוא רוצה לקנות.
        2.1.3 אם השחקן נוחת על נכס בבעלות שחקן אחר: חושב ומוריד שכר דירה מיתרת השחקן הנוכחי.
        2.1.4 אם יתרת השחקן קטנה או שווה ל-0, הוצא את השחקן מהמשחק.
3. הדפס הודעת ניצחון לשחקן האחרון שנותר.

-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeGame["<p align='left'>אתחול משחק:
    <code><b>
    numberOfPlayers = input()
    playerBalance = [1000, 1000, ...]
    playerLocation = [0, 0, ...]
    propertyOwner = [-1, -1, ...]
    </b></code></p>"]
    InitializeGame --> GameLoopStart{"תחילת לולאה: כל עוד יש יותר משחקן אחד"}
    GameLoopStart -- כן --> PlayerTurnStart{"תחילת תור שחקן"}
    PlayerTurnStart --> GetCurrentPlayer["קבלת שחקן נוכחי"]
    GetCurrentPlayer --> RollDice["גלגול קוביה"]
    RollDice --> MovePlayer["הזזת שחקן"]
    MovePlayer --> CheckProperty["בדיקה: האם הנכס פנוי?"]
    CheckProperty -- כן --> AskBuyProperty{"שאלה: האם השחקן רוצה לקנות את הנכס?"}
    AskBuyProperty -- כן --> BuyProperty["רכישת הנכס והורדת כסף מהשחקן"]
    BuyProperty --> CheckPlayerBalance{"בדיקה: האם יתרת השחקן קטנה או שווה ל-0?"}
    AskBuyProperty -- לא --> CheckPlayerBalance
    CheckProperty -- לא --> CheckOwner["בדיקה: האם הנכס בבעלות שחקן אחר?"]
    CheckOwner -- כן --> PayRent["תשלום שכר דירה"]
    PayRent --> CheckPlayerBalance
    CheckOwner -- לא --> CheckPlayerBalance
    CheckPlayerBalance -- כן --> RemovePlayer["הסרת שחקן מהמשחק"]
    RemovePlayer --> GameLoopStart
    CheckPlayerBalance -- לא --> PlayerTurnEnd["סוף תור שחקן"]
    PlayerTurnEnd --> GameLoopStart
    GameLoopStart -- לא --> OutputWinner["הכרזת המנצח"]
    OutputWinner --> End["סוף"]
```

Legenda:
    Start - התחלת התוכנית.
    InitializeGame - אתחול משתנים: מספר שחקנים, יתרת כל שחקן, מיקום השחקנים על הלוח, בעלות על נכסים.
    GameLoopStart - תחילת הלולאה המרכזית של המשחק, ממשיכה כל עוד יש יותר משחקן אחד עם כסף.
	PlayerTurnStart - התחלה של תור שחקן בודד.
    GetCurrentPlayer - בחירת השחקן הנוכחי מהרשימה.
    RollDice - גלגול קוביה לקביעת מספר הצעדים שהשחקן יזוז.
    MovePlayer - הזזת השחקן על הלוח.
    CheckProperty - בדיקה האם השחקן נחת על נכס פנוי.
    AskBuyProperty - שאילת השחקן אם ברצונו לרכוש את הנכס.
    BuyProperty - רכישת הנכס והורדת עלות הנכס מיתרת השחקן.
    CheckPlayerBalance - בדיקה אם יתרת השחקן שווה ל-0 או פחות.
	CheckOwner - בדיקה האם הנכס שבו השחקן נחת שייך לשחקן אחר.
	PayRent - גביית תשלום שכר דירה מהשחקן שדרס נכס בבעלות אחרת.
	RemovePlayer - הסרת שחקן שהפסיד (יתרה שלילית) מהמשחק.
	PlayerTurnEnd - סיום התור של השחקן הנוכחי.
    OutputWinner - הכרזה על השחקן המנצח (האחרון שנשאר).
    End - סיום התוכנית.
"""
import random

def play_monopoly():
    """
    משחק מונופול פשוט בגרסת טקסט.
    """

    # 1. אתחול המשחק
    while True:
      try:
        num_players = int(input("הכנס את מספר השחקנים (2-4): "))
        if 2 <= num_players <= 4:
            break
        else:
            print("מספר השחקנים חייב להיות בין 2 ל-4.")
      except ValueError:
        print("קלט לא תקין. אנא הזן מספר שלם.")

    player_balances = [1000] * num_players # יתרה התחלתית לכל שחקן
    player_positions = [0] * num_players  # מיקום התחלתי על הלוח
    property_owners = [-1] * 12 # מערך המייצג את הבעלים של כל נכס. -1 מציין נכס פנוי

    # נכסים
    properties_prices = [60, 60, 100, 100, 120, 140, 150, 180, 200, 220, 240, 300] # מחירי הנכסים
    properties_rent = [50, 50, 75, 75, 100, 120, 125, 150, 175, 200, 225, 250] # שכר דירה

    # 2. לולאת משחק ראשית
    while sum(1 for balance in player_balances if balance > 0) > 1: # כל עוד יש יותר משחקן אחד עם כסף
        for player in range(num_players): # לכל שחקן
            if player_balances[player] <= 0:
              continue # אם לשחקן אין כסף - דלג על התור שלו

            print(f"\nתורו של שחקן {player + 1}:")

            # 2.1 גלגול קוביה
            dice_roll = random.randint(1, 6)
            print(f"גלגלת {dice_roll}.")
            player_positions[player] = (player_positions[player] + dice_roll) % 12 # הזז את השחקן על הלוח. הלוח מעגלי (12 נכסים)
            current_position = player_positions[player]
            print(f"אתה נמצא כעת במיקום {current_position + 1}.")

            # 2.2 נחיתה על נכס פנוי
            if property_owners[current_position] == -1: # אם הנכס פנוי
                while True:
                  buy_choice = input(f"האם ברצונך לרכוש את הנכס במחיר {properties_prices[current_position]}? (כן/לא): ").lower()
                  if buy_choice == 'כן':
                      if player_balances[player] >= properties_prices[current_position]:
                          player_balances[player] -= properties_prices[current_position]
                          property_owners[current_position] = player
                          print(f"רכשת את הנכס, יתרתך כעת: {player_balances[player]}.")
                      else:
                          print("אין לך מספיק כסף לרכישה.")
                      break
                  elif buy_choice == 'לא':
                    break
                  else:
                     print("אפשרות לא חוקית, אנא בחר 'כן' או 'לא'.")

            # 2.3 נחיתה על נכס בבעלות שחקן אחר
            elif property_owners[current_position] != player:
                owner = property_owners[current_position]
                rent = properties_rent[current_position]
                if player_balances[player] >= rent:
                   player_balances[player] -= rent
                   player_balances[owner] += rent
                   print(f"שילמת שכר דירה לשחקן {owner + 1}, יתרתך כעת: {player_balances[player]}.")
                else:
                  print(f"אין לך מספיק כסף לשלם שכר דירה, אתה מחוץ למשחק!")
                  player_balances[player] = 0 # השחקן הפסיד


            # 2.4 הדפסת יתרות שחקנים
            for i in range(num_players):
              print(f"יתרת שחקן {i+1} = {player_balances[i]}")
    # 3. הכרזת המנצח
    winner = [i+1 for i, balance in enumerate(player_balances) if balance > 0][0]
    print(f"\nשחקן {winner} ניצח במשחק!")

if __name__ == "__main__":
    play_monopoly()


"""
הסבר הקוד:

1.  **ייבוא מודול `random`**:
    - `import random`: מייבא את המודול `random` לייצור מספרים אקראיים עבור הטלת הקוביה.

2.  **פונקציה `play_monopoly()`**:
    - מגדירה את הפונקציה הראשית של המשחק, שמכילה את כל ההגיון.

3.  **אתחול המשחק**:
    - `while True`: לולאה המבטיחה קלט תקין של מספר שחקנים (2-4)
    - `player_balances = [1000] * num_players`: יוצרת רשימה של יתרות שחקנים, כאשר כל שחקן מתחיל עם 1000.
    - `player_positions = [0] * num_players`: יוצרת רשימה של מיקומי שחקנים על הלוח, כאשר כל שחקן מתחיל במיקום 0.
    - `property_owners = [-1] * 12`: יוצרת רשימה שמייצגת את הבעלים של כל נכס. `-1` מציין שהנכס פנוי.
	- `properties_prices` - רשימה של מחירי נכסים.
	- `properties_rent` - רשימה של שכר דירה לכל נכס.

4.  **לולאת המשחק הראשית `while sum(1 for balance in player_balances if balance > 0) > 1:`**:
	- הלולאה ממשיכה כל עוד יש יותר משחקן אחד עם יתרה חיובית (כלומר, שעדיין לא הפסיד).

5.  **מעבר על כל השחקנים `for player in range(num_players)`**:
    - לולאה שעוברת על כל השחקנים.
	- `if player_balances[player] <= 0: continue` אם לשחקן אין כסף - דלג על התור שלו.

6.  **מהלך השחקן**:
    - `dice_roll = random.randint(1, 6)`: מטיל קוביה (מספר אקראי בין 1 ל-6).
    - `player_positions[player] = (player_positions[player] + dice_roll) % 12`: מעדכן את מיקום השחקן על הלוח (במעגל של 12 נכסים).
    - `current_position = player_positions[player]`: מקבל את מיקום השחקן הנוכחי.

7.  **נחיתה על נכס פנוי**:
    - `if property_owners[current_position] == -1`: אם הנכס פנוי
	- `while True`: לולאה שמבטיחה קלט תקין. שואל את השחקן אם הוא מעוניין לקנות את הנכס.
    - `if buy_choice == 'כן'`: אם השחקן בחר לקנות
      - `if player_balances[player] >= properties_prices[current_position]`: אם יש מספיק כסף, מעדכן את יתרת השחקן ומסמן אותו כבעלים של הנכס.

8.  **נחיתה על נכס של שחקן אחר**:
    - `elif property_owners[current_position] != player`: אם הנכס שייך לשחקן אחר
    - `if player_balances[player] >= rent`: אם לשחקן יש מספיק כסף כדי לשלם את שכר הדירה.
        - מעדכן את יתרת השחקן הנוכחי ואת יתרת הבעלים.
    - `else`: אם אין לשחקן כסף, הוא מפסיד ומוצא מהמשחק.
       - `player_balances[player] = 0`: יתרת השחקן מתאפסת.

9.  **הדפסת יתרות שחקנים**:
     - `for i in range(num_players): print(f"יתרת שחקן {i+1} = {player_balances[i]}")` : מדפיס את יתרת כל השחקנים לאחר סיום התור.

10. **הכרזת המנצח**:
     -  `winner = [i+1 for i, balance in enumerate(player_balances) if balance > 0][0]`: מקבל את מספר השחקן שנותר אחרון במשחק.
     - `print(f"\nשחקן {winner} ניצח במשחק!")`: מדפיס הודעה עם שם השחקן המנצח.

11. **הפעלת המשחק**:
     - `if __name__ == "__main__": play_monopoly()`: מפעיל את המשחק כאשר הקובץ מורץ ישירות.
"""
