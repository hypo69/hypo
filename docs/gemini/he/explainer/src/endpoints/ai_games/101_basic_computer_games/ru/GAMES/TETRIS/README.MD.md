## ניתוח קוד המשחק טטריס

### <algorithm>

להלן תיאור מפורט של זרימת העבודה של קוד המשחק טטריס, כולל דוגמאות לבלוקים לוגיים והזרימה של נתונים בין פונקציות, מחלקות ושיטות:

1.  **התחלת המשחק:**
    *   המשחק מתחיל ב-`if __name__ == '__main__':`, שיוצר מופע של `QApplication` ומפעיל את `Tetris`.
    *   `Tetris` יוצר את החלון הראשי, ומאתחל את הממשק המשתמש בעזרת `initUI()`.
        *   `initUI()` יוצר מופע של `Board` (לוח המשחק) וממקם אותו בחלון הראשי, ומחבר את האות של הלוח להצגת הודעות בשורת המצב.
        *   קורא ל- `start()` על הלוח.
        *   מגדיר את גודל החלון ומציג אותו.
    *   דוגמא:

        ```mermaid
        flowchart TD
        A[app = QApplication([])] --> B[tetris = Tetris()];
        B --> C[tetris.initUI()];
        C --> D[tboard = Board(self)];
        D --> E[setCentralWidget(self.tboard)];
        E --> F[statusbar = self.statusBar()];
        F --> G[tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)];
        G --> H[tboard.start()];
        H --> I[resize(180, 380)];
         I --> J[center()];
        J --> K[setWindowTitle('Tetris')];
        K --> L[show()];
        ```
2.  **אתחול לוח המשחק (`Board.initBoard()`):**
    *   מאפס את כל משתני המשחק כמו `timer`, `isWaitingAfterLine`, קואורדינטות, מספר השורות שהוסרו, הלוח, מצב הפוקוס ומצבי המשחק (`isStarted`, `isPaused`).
    *   קורא ל-`clearBoard()` לניקוי הלוח.
    *   דוגמא:

        ```python
        def initBoard(self) -> None:
            self.timer = QBasicTimer()
            self.isWaitingAfterLine = False
            self.curX = 0
            self.curY = 0
            self.numLinesRemoved = 0
            self.board = []
            self.setFocusPolicy(Qt.StrongFocus)
            self.isStarted = False
            self.isPaused = False
            self.clearBoard()
        ```
3.  **התחלת משחק (`Board.start()`):**
    *   בודק אם המשחק מושהה, אם כן לא עושה כלום.
    *   מעדכן את משתני המצב `isStarted` ו`isWaitingAfterLine`.
    *   מאפס את מספר השורות שהוסרו (`numLinesRemoved`).
    *   מנקה את הלוח באמצעות `clearBoard()`.
    *   שולח את הודעה עם מספר השורות שהוסרו לשורת המצב.
    *   יוצר חתיכה חדשה באמצעות `newPiece()`.
    *   מתחיל את הטיימר עם קצב קבוע (`Board.Speed`).
    *   דוגמא:

        ```mermaid
        flowchart TD
            A[start()] --> B{isPaused?};
            B -- True --> C[return];
            B -- False --> D[isStarted = True];
            D --> E[isWaitingAfterLine = False];
            E --> F[numLinesRemoved = 0];
            F --> G[clearBoard()];
            G --> H[emit(str(self.numLinesRemoved))];
            H --> I[newPiece()];
            I --> J[timer.start(Board.Speed, self)];
        ```
4.  **הצגת הלוח (`Board.paintEvent()`):**
    *   מאתחל את ה-`QPainter` כדי לצייר על הווידג'ט.
    *   מחשב את גובהו של החלק העליון של הלוח.
    *   עובר על כל משבצת בלוח ומצייר ריבוע בצבע המתאים.
    *   מצייר את החתיכה הנוכחית על הלוח.
    *    דוגמא:
        ```python
        def paintEvent(self, event: object) -> None:
            painter = QPainter(self)
            rect = self.contentsRect()
            boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
            for i in range(Board.BoardHeight):
                for j in range(Board.BoardWidth):
                    shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                    if shape != Tetrominoe.NoShape:
                        self.drawSquare(painter,
                            rect.left() + j * self.squareWidth(),
                            boardTop + i * self.squareHeight(), shape)
            if self.curPiece.shape() != Tetrominoe.NoShape:
                for i in range(4):
                    x = self.curX + self.curPiece.x(i)
                    y = self.curY - self.curPiece.y(i)
                    self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                        boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                        self.curPiece.shape())
        ```
5.  **תזוזת חתיכה (`Board.tryMove()`):**
    *   בודק אם תנועה לקואורדינטות החדשות אפשרית.
        *   בודק אם הקואורדינטות החדשות נמצאות בתוך גבולות הלוח.
        *   בודק אם הקואורדינטות החדשות לא תופסות משבצת שכבר תפוסה על ידי חתיכה אחרת.
    *   אם התנועה אפשרית:
        *   מעדכן את מיקום החתיכה הנוכחית (`curX`, `curY`).
        *   מעדכן את החתיכה הנוכחית (`curPiece`).
        *   קורא ל- `update()`, שגורם ל-`paintEvent()` להתרחש שוב כדי לצייר את החתיכה במיקומה החדש.
    *   מחזיר `True` אם התנועה אפשרית ו-`False` אחרת.
    *   דוגמא:
        ```mermaid
        flowchart TD
        A[tryMove(newPiece, newX, newY)] --> B{האם התנועה אפשרית?};
        B -- כן --> C[עדכן מיקום החתיכה: curPiece = newPiece, curX = newX, curY = newY];
        C --> D[עדכן את התצוגה: update()];
        D --> E[החזר True];
        B -- לא --> F[החזר False];
        ```
6.  **הפלת חתיכה (`Board.dropDown()`):**
    *   מוריד את החתיכה עד למטה ככל האפשר.
    *   קורא ל- `pieceDropped()` אחרי שהחתיכה מגיעה למטה.
    *   דוגמא:
         ```mermaid
        flowchart TD
        A[dropDown()] --> B[newY = curY];
        B --> C{newY > 0?};
        C -- כן --> D{האם התנועה למטה אפשרית?};
        D -- כן --> E[newY = newY - 1];
        E --> C;
         D -- לא --> F[pieceDropped()];
         C--לא-->F;
         ```
7.  **הורדת שורה אחת (`Board.oneLineDown()`):**
    *   מנסה להוריד את החתיכה שורה אחת למטה.
    *    אם התנועה למטה לא אפשרית, קורא ל- `pieceDropped()`.
    *   דוגמא:
         ```mermaid
        flowchart TD
        A[oneLineDown()] --> B{האם התנועה למטה אפשרית?};
        B -- כן --> C[return];
        B -- לא --> D[pieceDropped()];
         ```
8.  **הדבקת חתיכה (`Board.pieceDropped()`):**
    *   מעתיק את צורת החתיכה הנוכחית ללוח.
    *   מפעיל את `removeFullLines()` כדי להסיר שורות מלאות.
    *   יוצר חתיכה חדשה אם אין המתנה אחרי הסרת שורה.
     *   דוגמא:
        ```mermaid
         flowchart TD
            A[pieceDropped()] --> B{מעתיק את צורת החתיכה הנוכחית ללוח};
            B --> C[removeFullLines()];
            C --> D{isWaitingAfterLine == false?};
            D -- true --> E[newPiece()];
            D -- false --> F[return];
        ```
9.  **הסרת שורות מלאות (`Board.removeFullLines()`):**
    *   מוצא את השורות המלאות.
    *   אם קיימות שורות מלאות, מסיר אותן מהלוח.
    *   מעדכן את מספר השורות שהוסרו.
    *   שולח הודעה עם מספר השורות שהוסרו לשורת המצב.
    *   מגדיר את  `isWaitingAfterLine` ל-`True`, ומאפס את החתיכה הנוכחית.
    *   קורא ל- `update()`.
      *   דוגמא:
         ```mermaid
        flowchart TD
            A[removeFullLines()] --> B[מוצא שורות מלאות];
            B --> C{האם יש שורות מלאות?};
            C -- true --> D[מסיר את השורות המלאות ודוחף שורות מעל למטה];
             D --> E[מעדכן את מספר השורות שהוסרו];
            E --> F[שולח הודעה עם מספר השורות שהוסרו לשורת המצב];
            F --> G[isWaitingAfterLine = True];
            G --> H[curPiece.setShape(Tetrominoe.NoShape)];
            H --> I[update()];
             C -- false --> K[return];
         ```
10. **יצירת חתיכה חדשה (`Board.newPiece()`):**
    *   יוצר מופע חדש של `Shape`.
    *   בוחר צורה אקראית לחתיכה.
    *   מאתחל את מיקום החתיכה הנוכחית.
    *   אם אין מספיק מקום לחתיכה החדשה (כלומר `tryMove()` מחזיר `False`), המשחק נגמר.
    *   דוגמא:
        ```mermaid
            flowchart TD
            A[newPiece()] --> B[curPiece = Shape()];
            B --> C[curPiece.setRandomShape()];
            C --> D[אתחול מיקום החתיכה: curX, curY];
            D --> E{האם יש מספיק מקום לחתיכה?};
             E -- true --> F[return];
            E -- false --> G[curPiece.setShape(Tetrominoe.NoShape)];
             G --> H[timer.stop()];
            H --> I[isStarted = False];
            I --> J[הצגת הודעת סיום המשחק];
        ```
11. **טיפול באירועי לחיצה על מקשים (`Board.keyPressEvent()`):**
    *   בודק אם המשחק התחיל ואם יש חתיכה נוכחית. אם לא, מעביר את האירוע לטיפול ברירת המחדל.
    *   בודק האם המקש שנלחץ הוא "P" - משמש לפאוס.
    *   בודק אם המשחק מושהה, אם כן אין תגובה ללחיצות מקשים.
    *   מבצע פעולה בהתאם למקש שנלחץ:
        *   חץ שמאלה: מזיז את החתיכה שמאלה.
        *   חץ ימינה: מזיז את החתיכה ימינה.
        *   חץ למטה: מסובב את החתיכה ימינה.
        *   חץ למעלה: מסובב את החתיכה שמאלה.
        *   רווח: מוריד את החתיכה עד למטה.
        *   D: מוריד את החתיכה שורה אחת למטה.
    *   דוגמא:
        ```mermaid
        flowchart TD
            A[keyPressEvent(event)] --> B{האם המשחק התחיל ויש חתיכה?};
            B -- no --> C[מעביר את האירוע לטיפול ברירת המחדל];
            B -- yes --> D{האם המקש שנלחץ הוא 'P'?};
            D -- yes --> E[pause()];
             E --> F[return];
            D -- no --> G{האם המשחק מושהה?};
            G -- yes --> H[return];
            G -- no --> I{בודק איזה מקש נלחץ};
             I --> J{מזיז/מסובב/מוריד את החתיכה בהתאם};
            J-->K[return];
        ```
12. **טיפול באירועי טיימר (`Board.timerEvent()`):**
    *   בודק אם אירוע הטיימר מתאים לטיימר של המשחק.
    *   אם קיימת המתנה אחרי הסרת שורה, יוצר חתיכה חדשה.
    *   אחרת, מוריד את החתיכה שורה אחת למטה.
    *   דוגמא:
         ```mermaid
        flowchart TD
            A[timerEvent(event)] --> B{האם זה האירוע של טיימר המשחק?};
            B -- true --> C{האם קיימת המתנה לאחר הסרת שורה?};
            C -- true --> D[isWaitingAfterLine = False, newPiece()];
            C -- false --> E[oneLineDown()];
             B -- false --> F[מעביר את האירוע לטיפול ברירת המחדל];
         ```
13. **מצבי המשחק:**
    *   **פאוס:** המשחק יכול להיות מושהה וממשיך על ידי לחיצה על מקש "P". במהלך ההשהיה הטיימר נעצר.
    *   **סיום משחק:** המשחק מסתיים כאשר חתיכה חדשה לא יכולה להיווצר.

### <mermaid>

```mermaid
flowchart TD
    A[Tetris] --> B{initUI()};
    B --> C[Board];
    C --> D[initBoard()];
    D --> E[clearBoard()];
     E --> F[start()];
    F --> G{isPaused?};
    G -- No --> H[isStarted=True];
        H --> I[isWaitingAfterLine=False];
    I --> J[numLinesRemoved=0];
    J --> K[clearBoard()];
    K --> L[msg2Statusbar.emit(str(self.numLinesRemoved))];
     L --> M[newPiece()];
    M --> N[timer.start(Board.Speed, self)];
    G -- Yes --> O[return]
    N --> P[paintEvent()];
    P --> Q[drawSquare()];
     Q --> R[keyPressEvent(event)];
    R --> S{key == Qt.Key_P?};
    S -- Yes --> T[pause()];
    T --> U{isPaused?};
    U -- Yes --> V[timer.stop()];
    V --> W[msg2Statusbar.emit("paused")];
     U -- No --> X[timer.start(Board.Speed, self)];
       X --> Y[msg2Statusbar.emit(str(self.numLinesRemoved))];
    Y -->Z[update()]
     S -- No --> AA{isPaused?};
    AA -- Yes --> AB[return];
       AA -- No --> AC{key == Qt.Key_Left?};
    AC -- Yes --> AD[tryMove(curPiece, curX - 1, curY)];
       AC -- No --> AE{key == Qt.Key_Right?};
    AE -- Yes --> AF[tryMove(curPiece, curX + 1, curY)];
    AE -- No --> AG{key == Qt.Key_Down?};
    AG -- Yes --> AH[tryMove(curPiece.rotateRight(), curX, curY)];
      AG -- No --> AI{key == Qt.Key_Up?};
   AI -- Yes --> AJ[tryMove(curPiece.rotateLeft(), curX, curY)];
        AI -- No --> AK{key == Qt.Key_Space?};
     AK -- Yes --> AL[dropDown()];
   AK -- No --> AM{key == Qt.Key_D?};
    AM -- Yes --> AN[oneLineDown()];
     AM -- No --> AO[super(Board, self).keyPressEvent(event)];
        AD --> AP[timerEvent(event)];
       AF --> AP;
        AH --> AP;
       AJ --> AP;
       AL --> AP;
       AN --> AP;
        AP --> AQ{timerId == self.timer.timerId()?};
     AQ -- Yes --> AR{isWaitingAfterLine?};
   AR -- Yes --> AS[isWaitingAfterLine = False, newPiece()];
   AR -- No --> AT[oneLineDown()];
       AT --> AU{tryMove()?};
      AU -- Yes --> AV[update()];
       AU -- No --> AW[pieceDropped()];
      AW --> AX[removeFullLines()];
    AX --> AY{numFullLines > 0?};
     AY -- Yes --> AZ[msg2Statusbar.emit(str(self.numLinesRemoved))];
    AZ --> BA[isWaitingAfterLine = True];
    BA --> BB[curPiece.setShape(Tetrominoe.NoShape)];
    BB --> BC[update()];
    BC --> BD[newPiece()];
     BD --> BE{tryMove?};
   BE -- No --> BF[curPiece.setShape(Tetrominoe.NoShape)];
      BF --> BG[timer.stop()];
      BG --> BH[isStarted = False];
      BH --> BI[msg2Statusbar.emit("Game over")];
   BE -- Yes --> BJ[return];
  AY -- No --> BJ;
  AQ -- No --> BK[super(Board, self).timerEvent(event)];

  style A fill:#f9f,stroke:#333,stroke-width:2px
```
**ניתוח תלויות ב-mermaid:**
* אין תלויות חיצוניות מלבד התחביר של `mermaid`, שמשמש ליצירת דיאגרמות זרימה.
* התרשים מציג את הזרימה הלוגית של הקוד, החל מהאתחול ועד לסיום המשחק.
* שמות המשתנים בתרשים משמעותיים ומתארים את הפעולה או המשתנה שהם מייצגים.

### <explanation>

**ייבוא (Imports):**

*   `import sys, random`: מייבא את ספריית המערכת לגישה לארגומנטים של שורת הפקודה ופונקציונליות אקראית.
*   `from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication`: מייבא מודולים ממשק המשתמש של PyQt5 המשמשים לבניית החלונות והווידג'טים.
    *   `QMainWindow`: חלון ראשי של היישום.
    *   `QFrame`: משמש כבסיס עבור `Board` לוח המשחק.
    *    `QDesktopWidget`: גישה למידע על שטח המסך.
    *    `QApplication`: מנהל את האפליקציה.
*   `from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal`: מייבא מודולים מה-Core של PyQt5.
    *   `Qt`: קבועי קוד לאירועים שונים כמו לחיצות מקשים.
    *   `QBasicTimer`: משמש ליצירת אירועי טיימר.
    *   `pyqtSignal`: משמש לתקשורת בין אובייקטים באמצעות אותות.
*   `from PyQt5.QtGui import QPainter, QColor`: מייבא מודולים של PyQt5 המשמשים לציור על הווידג'טים.
    *   `QPainter`: משמש לציור צורות וטקסט על וידג'טים.
    *   `QColor`: משמש להגדרת צבעים.

**מחלקות (Classes):**

1.  **`Tetris(QMainWindow)`**:
    *   **תפקיד:** החלון הראשי של האפליקציה.
    *   **מאפיינים:**
        *   `tboard`: מופע של המחלקה `Board`, המשמש כלוח המשחק.
        *   `statusbar`: שורת מצב להצגת הודעות.
    *   **שיטות:**
        *   `__init__`: מאתחל את החלון, קורא ל- `initUI`.
        *   `initUI`: מאתחל את ממשק המשתמש, כולל יצירת לוח המשחק (`Board`), הגדרת שורת המצב, וחיבור האות (`signal`) של לוח המשחק להודעות בשורת המצב, כמו כן הגדרת גודל החלון והצגתו במרכז המסך.
        *   `center`: ממקם את החלון במרכז המסך.
    *   **אינטראקציה:** יוצר ומציג את לוח המשחק.
2.  **`Board(QFrame)`:**
    *   **תפקיד:** מייצג את לוח המשחק של הטטריס.
    *   **מאפיינים:**
        *   `msg2Statusbar`: אות שמשמש להעברת הודעות לשורת המצב.
        *   `BoardWidth`: רוחב הלוח (10).
        *   `BoardHeight`: גובה הלוח (22).
        *   `Speed`: מהירות נפילת החתיכות (300 מילישניות).
        *   `timer`: מופע של `QBasicTimer`.
        *   `isWaitingAfterLine`: מציין אם המשחק ממתין אחרי הסרת שורה מלאה.
        *   `curX`, `curY`: קואורדינטות של החתיכה הנוכחית.
        *   `numLinesRemoved`: מספר השורות שהוסרו.
        *   `board`: רשימה שמייצגת את מצב הלוח.
        *   `isStarted`, `isPaused`: מצבי המשחק.
        *   `curPiece`: החתיכה הנוכחית.
    *   **שיטות:**
        *   `__init__`: מאתחל את הלוח, קורא ל-`initBoard`.
        *   `initBoard`: מאתחל את כל משתני לוח המשחק, כולל את הטיימר, המשתנים, ומנקה את הלוח.
        *    `shapeAt(x, y)`: מחזיר את צורת החתיכה במיקום נתון על הלוח.
        *   `setShapeAt(x, y, shape)`: מגדיר את צורת החתיכה במיקום נתון על הלוח.
        *   `squareWidth` / `squareHeight`: מחשב את רוחב וגובה הריבועים בלוח.
        *   `start`: מתחיל את המשחק, יוצר חתיכה חדשה ומתחיל את הטיימר.
        *   `pause`: עוצר או ממשיך את המשחק.
        *   `paintEvent`: מצייר את הלוח והחתיכות.
        *   `keyPressEvent`: מטפל באירועי לחיצות מקשים.
        *   `timerEvent`: מטפל באירועי טיימר.
        *   `clearBoard`: מנקה את הלוח.
        *   `dropDown`: מפיל את החתיכה עד למטה.
        *   `oneLineDown`: מפיל את החתיכה שורה אחת למטה.
        *   `pieceDropped`: מדביק את החתיכה בלוח, מסיר שורות מלאות, יוצר חתיכה חדשה.
        *   `removeFullLines`: מסיר את השורות המלאות ומשנה את הניקוד.
        *   `newPiece`: יוצר חתיכה חדשה.
        *   `tryMove`: מנסה להזיז את החתיכה למיקום חדש.
        *    `drawSquare`: מצייר ריבוע בלוח.
    *   **אינטראקציה:** אחראי על כל הלוגיקה של משחק הטטריס, מציג את הלוח, מקבל פקודות מהמשתמש ומעדכן את הלוח בהתאם.
3.  **`Tetrominoe`**:
    *   **תפקיד:** מגדיר את סוגי הצורות האפשריות.
    *   **מאפיינים:**
        *   קבועי קוד לכל צורה (NoShape, ZShape, SShape, וכו').
    *   **אינטראקציה:** משמש כקבועים סטטיים לצורות השונות.
4.  **`Shape`**:
    *   **תפקיד:** מייצג את החתיכה הבודדת.
    *   **מאפיינים:**
        *   `coords`: מערך של 4 קואורדינטות שמתארות את הצורה.
        *   `pieceShape`: קבוע שמציין את סוג הצורה (מ-`Tetrominoe`).
    *   **שיטות:**
        *   `__init__`: מאתחל את החתיכה עם צורה ריקה.
        *   `shape`: מחזיר את סוג הצורה.
        *   `setShape`: מגדיר את סוג הצורה ומעדכן את הקואורדינטות.
        *    `setRandomShape`: בוחר צורה אקראית.
        *   `x(index)`/`y(index)`: מחזיר את קואורדינטות ה-X וה-Y של הנקודה באינדקס נתון.
        *   `setX(index, x)`/`setY(index, y)`: מגדיר את קואורדינטות ה-X וה-Y של הנקודה באינדקס נתון.
        *   `minX`,`maxX`,`minY`,`maxY`: מחזיר את ערכי ה- X וה-Y המינימליים והמקסימליים של הצורה.
        *   `rotateLeft`: מסובב את הצורה שמאלה.
        *   `rotateRight`: מסובב את הצורה ימינה.
    *   **אינטראקציה:** משמש ליצירת חתיכות, הגדרת צורות וסיבוב שלהן.

**פונקציות (Functions):**

*   רוב הפונקציות מוגדרות כשיטות במחלקות `Tetris`, `Board`, ו- `Shape`, והן מתוארות לעיל.
*   הפונקציה `__main__` בודקת את שם הסקריפט ומפעילה את האפליקציה.
    *   יוצר מופע של `QApplication` ומריץ את לולאת האפליקציה.
    *   מייצר מופע של המחלקה `Tetris` שמרכיב את המשחק.

**משתנים (Variables):**

*   משתנים רבים מוגדרים בתוך המחלקות, כגון:
    *   `BoardWidth`, `BoardHeight`, `Speed` ב-`Board`.
    *    `curX`, `curY`, `numLinesRemoved` ב-`Board`.
    *   `coords`, `pieceShape` ב-`Shape`.
*   המשתנים משמשים לאחסון מצב המשחק, מיקום החתיכות ונתונים אחרים הדרושים ללוגיקה.

**בעיות אפשריות ותחומים לשיפור:**

*   **קוד לא מסודר:** הקוד יכול להיות מפוצל לפונקציות קטנות יותר וברורות יותר.
*   **טיפול באגים:** אין טיפול מספיק במקרים בהם משתמש עושה פעולה לא חוקית.
*   **קריאות:** שמות המשתנים יכולים להיות ברורים יותר.
*   **מורכבות:** חלק מהשיטות כמו `removeFullLines` יכולות להיות מפוצלות לשיטות קטנות יותר.
*   **יכולת הרחבה:** מבנה הקוד לא מאפשר בקלות הוספה של סוגי צורות חדשות או תכונות משחק נוספות.

**שרשרת קשרים:**

*   `Tetris` (חלון ראשי) יוצר `Board` (לוח המשחק) ומשתמש בו.
*   `Board` משתמש ב- `Shape` לייצוג החתיכות הנופלות.
*   `Board` משתמש ב- `Tetrominoe` כדי להגדיר את סוגי החתיכות.
*   שימוש באותות (`pyqtSignal`) לתקשורת בין `Board` ל- `Tetris`.

זהו ניתוח מפורט של הקוד, שמספק הבנה מעמיקה של הפונקציונליות שלו.