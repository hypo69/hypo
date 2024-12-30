# ACE

## סקירה כללית

משחק "ACE" הוא משחק בו שני שחקנים מתחלפים בהוצאת קלפים מחפיסה ומנסים לצבור יותר נקודות. אס נחשב כנקודה אחת, וקלפים עם מספרים מ-2 עד 10 נספרים לפי הערך הנקוב, וגם וואלט, גברת ומלך נחשבים כ-10. השחקן שצובר יותר נקודות מנצח. המשחק נמשך עד שמשחקים מספר מסוים של סיבובים.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [חוקי המשחק](#חוקי-המשחק)
3. [אלגוריתם](#אלגוריתם)
4. [תרשים זרימה](#תרשים-זרימה)
5. [הסבר לתרשים הזרימה](#הסבר-לתרשים-הזרימה)

## חוקי המשחק

1. משחקים שני שחקנים.
2. השחקנים מתחלפים בשליפת קלפים מחפיסה.
3. לכל קלף יש מספר מסוים של נקודות: אס - 1, קלפים מ-2 עד 10 - לפי הערך הנקוב, וואלט, גברת ומלך - 10.
4. כל שחקן מנסה לצבור כמה שיותר נקודות לסיבוב.
5. בסוף הסיבוב, משווים את נקודות השחקנים.
6. המשחק מורכב ממספר מסוים של סיבובים.
7. מנצח המשחק הוא השחקן שצבר יותר נקודות בכל הסיבובים.

## אלגוריתם

1. אתחול נקודות השחקנים 1 ו-2 לאפס.
2. בקש את מספר הסיבובים.
3. התחל לולאה לפי מספר הסיבובים:
    3.1. שחקן 1 שולף קלף.
    3.2. הצג את הקלף של שחקן 1 ואת מספר הנקודות עבור הקלף.
    3.3. הוסף את הנקודות עבור הקלף לסך הנקודות של שחקן 1.
    3.4. שחקן 2 שולף קלף.
    3.5. הצג את הקלף של שחקן 2 ואת מספר הנקודות עבור הקלף.
    3.6. הוסף את הנקודות עבור הקלף לסך הנקודות של שחקן 2.
    3.7. אם הנקודות של שחקן 1 גדולות מהנקודות של שחקן 2, הצג הודעה "PLAYER 1 WINS THE ROUND".
    3.8. אם הנקודות של שחקן 2 גדולות מהנקודות של שחקן 1, הצג הודעה "PLAYER 2 WINS THE ROUND".
    3.9. אם הנקודות של שחקן 1 שוות לנקודות של שחקן 2, הצג הודעה "TIE GAME THIS ROUND".
4. הצג את סך הנקודות של שחקן 1.
5. הצג את סך הנקודות של שחקן 2.
6. אם סך הנקודות של שחקן 1 גדול מסך הנקודות של שחקן 2, הצג הודעה "PLAYER 1 WINS THE GAME".
7. אם סך הנקודות של שחקן 2 גדול מסך הנקודות של שחקן 1, הצג הודעה "PLAYER 2 WINS THE GAME".
8. אם סך הנקודות של שחקן 1 שווה לסך הנקודות של שחקן 2, הצג הודעה "TIE GAME".
9. סוף המשחק.

## תרשים זרימה

```mermaid
flowchart TD
    Start["Начало"] --> InitializeScores["<p align='left'>Инициализация переменных:<br><code><b>player1Score = 0</b></code><br><code><b>player2Score = 0</b></code></p>"]
    InitializeScores --> InputRounds["Ввод количества раундов: <code><b>numberOfRounds</b></code>"]
    InputRounds --> RoundLoopStart{"Начало цикла по раундам"}
    RoundLoopStart -- Да --> Player1DrawsCard["Игрок 1 тянет карту: <code><b>card1, card1Value</b></code>"]
    Player1DrawsCard --> OutputPlayer1Card["Вывод карты и очков игрока 1: <code><b>card1, card1Value</b></code>"]
    OutputPlayer1Card --> UpdatePlayer1Score["<code><b>player1Score = player1Score + card1Value</b></code>"]
    UpdatePlayer1Score --> Player2DrawsCard["Игрок 2 тянет карту: <code><b>card2, card2Value</b></code>"]
    Player2DrawsCard --> OutputPlayer2Card["Вывод карты и очков игрока 2: <code><b>card2, card2Value</b></code>"]
    OutputPlayer2Card --> UpdatePlayer2Score["<code><b>player2Score = player2Score + card2Value</b></code>"]
    UpdatePlayer2Score --> CompareScores{"Сравнение очков за раунд: <code><b>card1Value > card2Value?</b></code>"}
    CompareScores -- Да --> OutputPlayer1RoundWin["Вывод: <b>PLAYER 1 WINS THE ROUND</b>"]
    CompareScores -- Нет --> CompareScores2{"Сравнение очков за раунд: <code><b>card2Value > card1Value?</b></code>"}
    CompareScores2 -- Да --> OutputPlayer2RoundWin["Вывод: <b>PLAYER 2 WINS THE ROUND</b>"]
    CompareScores2 -- Нет --> OutputTieRound["Вывод: <b>TIE GAME THIS ROUND</b>"]
    OutputPlayer1RoundWin --> RoundLoopEnd
    OutputPlayer2RoundWin --> RoundLoopEnd
    OutputTieRound --> RoundLoopEnd
    RoundLoopEnd --> RoundLoopStart {"Начало цикла по раундам"}
    RoundLoopStart -- Нет --> OutputTotalPlayer1Score["Вывод общего количества очков игрока 1: <code><b>player1Score</b></code>"]
    OutputTotalPlayer1Score --> OutputTotalPlayer2Score["Вывод общего количества очков игрока 2: <code><b>player2Score</b></code>"]
    OutputTotalPlayer2Score --> CompareTotalScores{"Сравнение общих очков: <code><b>player1Score > player2Score?</b></code>"}
    CompareTotalScores -- Да --> OutputPlayer1GameWin["Вывод: <b>PLAYER 1 WINS THE GAME</b>"]
    CompareTotalScores -- Нет --> CompareTotalScores2{"Сравнение общих очков: <code><b>player2Score > player1Score?</b></code>"}
    CompareTotalScores2 -- Да --> OutputPlayer2GameWin["Вывод: <b>PLAYER 2 WINS THE GAME</b>"]
    CompareTotalScores2 -- Нет --> OutputTieGame["Вывод: <b>TIE GAME</b>"]
    OutputPlayer1GameWin --> End["Конец"]
    OutputPlayer2GameWin --> End
    OutputTieGame --> End
```

## הסבר לתרשים הזרימה

- **Start** - תחילת התוכנית.
- **InitializeScores** - אתחול משתני ניקוד השחקנים player1Score ו-player2Score לאפס.
- **InputRounds** - בקשת מספר הסיבובים numberOfRounds מהמשתמש למשחק.
- **RoundLoopStart** - תחילת לולאה עבור כל סיבוב במשחק. הלולאה מבוצעת numberOfRounds פעמים.
- **Player1DrawsCard** - שחקן 1 מושך קלף card1 וערכו card1Value נקבע.
- **OutputPlayer1Card** - הצגה על המסך של פרטי הקלף של שחקן 1 card1 וערכו card1Value.
- **UpdatePlayer1Score** - עדכון הניקוד הכולל של שחקן 1, הוספת הערך card1Value ל- player1Score.
- **Player2DrawsCard** - שחקן 2 מושך קלף card2 וערכו card2Value נקבע.
- **OutputPlayer2Card** - הצגה על המסך של פרטי הקלף של שחקן 2 card2 וערכו card2Value.
- **UpdatePlayer2Score** - עדכון הניקוד הכולל של שחקן 2, הוספת הערך card2Value ל- player2Score.
- **CompareScores** - השוואה בין ערכי הקלפים card1Value ו-card2Value כדי לקבוע את מנצח הסיבוב.
- **OutputPlayer1RoundWin** - הצגת הודעה על ניצחון שחקן 1 בסיבוב.
- **CompareScores2** - השוואה בין ערכי הקלפים card2Value ו-card1Value כדי לקבוע את מנצח הסיבוב.
- **OutputPlayer2RoundWin** - הצגת הודעה על ניצחון שחקן 2 בסיבוב.
- **OutputTieRound** - הצגת הודעה על תיקו בסיבוב.
- **RoundLoopEnd** - סוף הלולאה עבור הסיבובים.
- **OutputTotalPlayer1Score** - הצגה על המסך של הניקוד הכולל של שחקן 1 player1Score.
- **OutputTotalPlayer2Score** - הצגה על המסך של הניקוד הכולל של שחקן 2 player2Score.
- **CompareTotalScores** - השוואה בין הניקוד הכולל של השחקנים player1Score ו-player2Score כדי לקבוע את מנצח המשחק.
- **OutputPlayer1GameWin** - הצגת הודעה על ניצחון שחקן 1 במשחק.
- **CompareTotalScores2** - השוואה בין הניקוד הכולל של השחקנים player2Score ו-player1Score כדי לקבוע את מנצח המשחק.
- **OutputPlayer2GameWin** - הצגת הודעה על ניצחון שחקן 2 במשחק.
- **OutputTieGame** - הצגת הודעה על תיקו במשחק.
- **End** - סוף התוכנית.