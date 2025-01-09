# ACE

## סקירה כללית

משחק ACE הוא משחק בו שני שחקנים מתחלפים לשלוף קלפים מחפיסה ומנסים לצבור יותר נקודות. אס נחשב לנקודה אחת, קלפים עם מספרים מ-2 עד 10 נחשבים לפי הערך שלהם, וכן ג'ק, מלכה ומלך נחשבים ל-10. השחקן עם הכי הרבה נקודות מנצח. המשחק נמשך עד שמשוחק מספר מסוים של סיבובים.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [חוקי המשחק](#חוקי-המשחק)
- [אלגוריתם](#אלגוריתם)
- [דיאגרמת זרימה](#דיאגרמת-זרימה)

## חוקי המשחק

1. שני שחקנים משחקים.
2. השחקנים מתחלפים לשלוף קלפים מהחפיסה.
3. לכל קלף יש מספר מסוים של נקודות: אס - 1, קלפים מ-2 עד 10 - לפי הערך הנקוב שלהם, ג'ק, מלכה ומלך - 10.
4. כל שחקן מנסה לצבור כמה שיותר נקודות לסיבוב.
5. בסוף הסיבוב משווים את הנקודות של השחקנים.
6. המשחק מורכב ממספר מסוים של סיבובים.
7. המנצח במשחק מוכרז כמי שצבר את מירב הנקודות בכל הסיבובים.

## אלגוריתם

1. אתחל את הנקודות של שחקן 1 ושחקן 2 לאפס.
2. בקש את מספר הסיבובים.
3. התחל לולאה לפי מספר הסיבובים:
    3.1. שחקן 1 שולף קלף.
    3.2. הצג את הקלף של שחקן 1 ואת מספר הנקודות עבור הקלף.
    3.3. הוסף נקודות עבור הקלף לסך הנקודות של שחקן 1.
    3.4. שחקן 2 שולף קלף.
    3.5. הצג את הקלף של שחקן 2 ואת מספר הנקודות עבור הקלף.
    3.6. הוסף נקודות עבור הקלף לסך הנקודות של שחקן 2.
    3.7. אם הנקודות של שחקן 1 גבוהות מהנקודות של שחקן 2, הצג את ההודעה "PLAYER 1 WINS THE ROUND".
    3.8. אם הנקודות של שחקן 2 גבוהות מהנקודות של שחקן 1, הצג את ההודעה "PLAYER 2 WINS THE ROUND".
    3.9. אם הנקודות של שחקן 1 שוות לנקודות של שחקן 2, הצג את ההודעה "TIE GAME THIS ROUND".
4. הצג את הסך הכולל של הנקודות של שחקן 1.
5. הצג את הסך הכולל של הנקודות של שחקן 2.
6. אם הסך הכולל של הנקודות של שחקן 1 גבוה מהסך הכולל של הנקודות של שחקן 2, הצג את ההודעה "PLAYER 1 WINS THE GAME".
7. אם הסך הכולל של הנקודות של שחקן 2 גבוה מהסך הכולל של הנקודות של שחקן 1, הצג את ההודעה "PLAYER 2 WINS THE GAME".
8. אם הסך הכולל של הנקודות של שחקן 1 שווה לסך הכולל של הנקודות של שחקן 2, הצג את ההודעה "TIE GAME".
9. סוף המשחק.

## דיאגרמת זרימה

```mermaid
flowchart TD
    Start["התחלה"] --> InitializeScores["<p align='left'>אתחול משתנים:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["קלט מספר סיבובים: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"התחלת לולאה לפי סיבובים"}
    RoundLoopStart -- כן --> Player1DrawsCard["שחקן 1 שולף קלף: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["הצגת קלף ונקודות של שחקן 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["שחקן 2 שולף קלף: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["הצגת קלף ונקודות של שחקן 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"השוואת נקודות לסיבוב: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- כן --> OutputPlayer1RoundWin["הצג: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- לא --> CompareScores2{"השוואת נקודות לסיבוב: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- כן --> OutputPlayer2RoundWin["הצג: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- לא --> OutputTieRound["הצג: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
     RoundLoopEnd --> RoundLoopStart {"התחלת לולאה לפי סיבובים"}

    RoundLoopStart -- לא --> OutputTotalPlayer1Score["הצג סך הנקודות של שחקן 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["הצג סך הנקודות של שחקן 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"השוואת סך הנקודות: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- כן --> OutputPlayer1GameWin["הצג: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- לא --> CompareTotalScores2{"השוואת סך הנקודות: <code><b>player2Score > player1Score?</b></code>"}
     CompareTotalScores2 -- כן --> OutputPlayer2GameWin["הצג: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- לא --> OutputTieGame["הצג: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["סוף"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```
**מקרא**
    Start - תחילת התוכנית.
    InitializeScores - אתחול משתני הנקודות של השחקנים player1Score ו player2Score לאפס.
    InputRounds - בקשת מספר הסיבובים numberOfRounds מהמשתמש למשחק.
    RoundLoopStart - תחילת לולאה עבור כל סיבוב במשחק. הלולאה מתבצעת numberOfRounds פעמים.
    Player1DrawsCard - שחקן 1 שולף קלף card1 ונקבע ערכו card1Value.
    OutputPlayer1Card - הצגת מידע על הקלף card1 של שחקן 1 וערכו card1Value על המסך.
    UpdatePlayer1Score - עדכון סך הנקודות של שחקן 1, הוספת הערך card1Value ל player1Score.
    Player2DrawsCard - שחקן 2 שולף קלף card2 ונקבע ערכו card2Value.
    OutputPlayer2Card - הצגת מידע על הקלף card2 של שחקן 2 וערכו card2Value על המסך.
    UpdatePlayer2Score - עדכון סך הנקודות של שחקן 2, הוספת הערך card2Value ל player2Score.
    CompareScores - השוואת ערכי הקלפים card1Value ו card2Value כדי לקבוע את מנצח הסיבוב.
    OutputPlayer1RoundWin - הצגת הודעה על ניצחון שחקן 1 בסיבוב.
    CompareScores2 - השוואת ערכי הקלפים card2Value ו card1Value כדי לקבוע את מנצח הסיבוב.
    OutputPlayer2RoundWin - הצגת הודעה על ניצחון שחקן 2 בסיבוב.
    OutputTieRound - הצגת הודעה על תיקו בסיבוב.
    RoundLoopEnd - סוף הלולאה של הסיבובים.
    OutputTotalPlayer1Score - הצגת סך הנקודות של שחקן 1 player1Score על המסך.
    OutputTotalPlayer2Score - הצגת סך הנקודות של שחקן 2 player2Score על המסך.
    CompareTotalScores - השוואת סך הנקודות של השחקנים player1Score ו player2Score כדי לקבוע את מנצח המשחק.
    OutputPlayer1GameWin - הצגת הודעה על ניצחון שחקן 1 במשחק.
     CompareTotalScores2 - השוואת סך הנקודות של השחקנים player2Score ו player1Score כדי לקבוע את מנצח המשחק.
    OutputPlayer2GameWin - הצגת הודעה על ניצחון שחקן 2 במשחק.
    OutputTieGame - הצגת הודעה על תיקו במשחק.
    End - סוף התוכנית.