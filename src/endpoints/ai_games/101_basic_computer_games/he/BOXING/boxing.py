<BOXING>:
=================
קושי: 4
-----------------
המשחק "איגרוף" מדמה קרב איגרוף בין שני מתאגרפים, כאשר כל שחקן מנסה להוריד את כוח החיים של המתאגרף השני לאפס. השחקנים מתחלפים בתורם, ובכל תור הם בוחרים מכה, שגורמת נזק אקראי ליריב.

חוקי המשחק:
1. המשחק מתחיל עם שני מתאגרפים, כאשר לכל אחד מהם 100 נקודות חיים.
2. השחקנים מתחלפים בתורם, ובכל תור הם בוחרים מכה אקראית.
3. כל מכה גורמת לנזק אקראי בין 0 ל-20 נקודות חיים.
4. המשחק מסתיים כאשר כוח החיים של אחד המתאגרפים מגיע לאפס או פחות מכך.
5. השחקן השני מנצח.
-----------------
אלגוריתם:
1. אתחל את נקודות החיים של שני המתאגרפים ל-100.
2. הגדר את השחקן הנוכחי כשחקן 1.
3. התחל לולאה "כל עוד נקודות החיים של שני המתאגרפים גדולות מ-0":
   3.1 הצג את מצב החיים של שני המתאגרפים.
   3.2 בחר מספר אקראי בין 0 ל-20 כמכה.
   3.3 הפחת את ערך המכה מנקודות החיים של המתאגרף השני (בהתאם לשחקן הנוכחי).
   3.4 אם נקודות החיים של אחד המתאגרפים קטנות או שוות ל-0, עבור לשלב 4.
   3.5 החלף שחקנים (אם השחקן הנוכחי הוא 1, הפוך אותו ל-2, אחרת הפוך אותו ל-1).
4. הצג הודעה שהשחקן השני (זה שלא סיים עם 0 נקודות חיים או פחות) ניצח.
5. סוף המשחק.
-----------------
תרשים זרימה:
```mermaid
flowchart TD
    Start["התחלה"] --> InitializeVariables["<p align='left'>אתחול משתנים:
    <code><b>
    player1Health = 100<br>
    player2Health = 100<br>
    currentPlayer = 1
    </b></code></p>"]
    InitializeVariables --> LoopStart{"תחילת לולאה: כל עוד שני המתאגרפים בחיים"}
    LoopStart -- כן --> ShowHealth["הצגת מצב חיים: <code><b>player1Health, player2Health</b></code>"]
    ShowHealth --> GenerateAttack["יצירת מכה אקראית: <code><b>attackDamage = random(0, 20)</b></code>"]
    GenerateAttack --> ApplyDamage{"<p align='left'>הפחתת נזק:
    <code><b>
    if currentPlayer == 1:<br>
        player2Health = player2Health - attackDamage<br>
    else:<br>
        player1Health = player1Health - attackDamage<br>
    </b></code></p>"}
    ApplyDamage --> CheckHealth{"בדיקה: <code><b>player1Health <= 0 OR player2Health <= 0 ?</b></code>"}
    CheckHealth -- כן --> OutputWinner["הצגת מנצח: <code><b>if player1Health <= 0: print 'Player 2 Wins'<br> else: print 'Player 1 Wins'</b></code>"]
    OutputWinner --> End["סוף"]
    CheckHealth -- לא --> SwitchPlayer{"<p align='left'>החלפת שחקנים:
        <code><b>
        if currentPlayer == 1:<br>
            currentPlayer = 2<br>
        else:<br>
            currentPlayer = 1<br>
    </b></code></p>"}
    SwitchPlayer --> LoopStart
    LoopStart -- לא --> End
```

Legenda:
    Start - התחלת התוכנית.
    InitializeVariables - אתחול משתנים: player1Health (כוח החיים של שחקן 1) ו-player2Health (כוח החיים של שחקן 2) מאותחלים ל-100, ו-currentPlayer (השחקן הנוכחי) מאותחל ל-1.
    LoopStart - תחילת הלולאה, הממשיכה כל עוד שני השחקנים בחיים.
    ShowHealth - הצגת מצב החיים של שני השחקנים.
    GenerateAttack - יצירת מכה אקראית עם נזק בין 0 ל-20.
    ApplyDamage - הפחתת נזק מנקודות החיים של השחקן השני בהתאם לשחקן הנוכחי.
    CheckHealth - בדיקה האם כוח החיים של אחד השחקנים הגיע ל-0 או פחות.
    OutputWinner - הצגת הודעת ניצחון לשחקן שלא הגיע ל-0 נקודות חיים או פחות.
    End - סוף התוכנית.
    SwitchPlayer - החלפת השחקן הנוכחי.

"""
import random

# אתחול נקודות החיים של שני השחקנים
player1Health = 100
player2Health = 100

# השחקן הנוכחי מתחיל כשחקן 1
currentPlayer = 1

# לולאת המשחק הראשית
while player1Health > 0 and player2Health > 0:
    # הצגת מצב הבריאות של שני השחקנים
    print(f"שחקן 1 חיים: {player1Health}")
    print(f"שחקן 2 חיים: {player2Health}")

    # יצירת נזק אקראי למכה
    attackDamage = random.randint(0, 20)
    print(f"שחקן {currentPlayer} הנחית מכה של {attackDamage} נקודות נזק.")

    # הפחתת הנזק משחקן היריב
    if currentPlayer == 1:
        player2Health -= attackDamage
    else:
        player1Health -= attackDamage

    # בדיקה האם אחד השחקנים הפסיד
    if player1Health <= 0 or player2Health <= 0:
        break

    # החלפת שחקן
    if currentPlayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1

# הכרזת המנצח
if player1Health <= 0:
    print("שחקן 2 ניצח!")
else:
    print("שחקן 1 ניצח!")

"""
הסבר הקוד:
1. **ייבוא המודול `random`**:
    - `import random`: ייבוא המודול `random`, המשמש ליצירת מספר אקראי.
2. **אתחול משתנים**:
    - `player1Health = 100`: אתחול כמות הנקודות חיים של שחקן 1 ל-100.
    - `player2Health = 100`: אתחול כמות הנקודות חיים של שחקן 2 ל-100.
    - `currentPlayer = 1`: אתחול השחקן הנוכחי לשחקן 1.
3. **לולאת המשחק `while player1Health > 0 and player2Health > 0:`**:
   - לולאה זו ממשיכה כל עוד לשני השחקנים יש נקודות חיים (גדול מ-0).
    - **הצגת מצב בריאות**:
        - `print(f"שחקן 1 חיים: {player1Health}")`: הדפסת נקודות החיים של שחקן 1.
        - `print(f"שחקן 2 חיים: {player2Health}")`: הדפסת נקודות החיים של שחקן 2.
    - **יצירת מכה אקראית**:
        - `attackDamage = random.randint(0, 20)`: בחירת ערך נזק אקראי בין 0 ל-20.
        - `print(f"שחקן {currentPlayer} הנחית מכה של {attackDamage} נקודות נזק.")`: הדפסת הודעה על הנזק שגרם השחקן הנוכחי.
    - **הפחתת נזק**:
        - `if currentPlayer == 1:`: אם השחקן הנוכחי הוא שחקן 1, אז...
            - `player2Health -= attackDamage`: הפחת את ערך המכה מנקודות החיים של שחקן 2.
        - `else:`: אם השחקן הנוכחי הוא שחקן 2, אז...
            - `player1Health -= attackDamage`: הפחת את ערך המכה מנקודות החיים של שחקן 1.
    - **בדיקת סיום המשחק**:
        - `if player1Health <= 0 or player2Health <= 0:`: אם נקודות החיים של אחד השחקנים קטנות או שוות ל-0, המשחק מסתיים.
            - `break`: הפסק את הלולאה.
    - **החלפת שחקנים**:
        - `if currentPlayer == 1:`: אם השחקן הנוכחי הוא שחקן 1, אז...
            - `currentPlayer = 2`: השחקן הבא הוא שחקן 2.
        - `else:`: אם השחקן הנוכחי הוא שחקן 2, אז...
            - `currentPlayer = 1`: השחקן הבא הוא שחקן 1.
4. **הכרזת המנצח**:
    - `if player1Health <= 0:`: אם נקודות החיים של שחקן 1 קטנות או שוות ל-0, אז...
        - `print("שחקן 2 ניצח!")`: הדפס ששחקן 2 ניצח.
    - `else:`: אחרת, כלומר אם נקודות החיים של שחקן 2 קטנות או שוות ל-0, אז...
        - `print("שחקן 1 ניצח!")`: הדפס ששחקן 1 ניצח.
"""
