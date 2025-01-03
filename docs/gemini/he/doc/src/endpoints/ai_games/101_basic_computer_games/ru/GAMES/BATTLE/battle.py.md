# BATTLE

## סקירה כללית

משחק "BATTLE" הוא סימולציה של קרב ימי בין שני שחקנים - מחשב ואדם. השחקנים מתחלפים "ביריות" בתאים בלוח המשחק, בניסיון להטביע את ספינות האויב. המשחק נמשך עד שכל הספינות של אחד השחקנים מוטבעות.

## תוכן עניינים
- [סקירה כללית](#סקירה-כללית)
- [פונקציות](#פונקציות)
  - [`create_board`](#create_board)
  - [`place_computer_ships`](#place_computer_ships)
  - [`display_board`](#display_board)
  - [`play_battle`](#play_battle)

## פונקציות

### `create_board`

**תיאור**:
פונקציה היוצרת לוח משחק (מטריצה) בגודל שצוין וממלאת אותו באפסים.

**פרמטרים**:
- `size` (int): גודל לוח המשחק.

**החזרות**:
- `list[list[int]]`: לוח המשחק, מיוצג כמטריצה.

### `place_computer_ships`

**תיאור**:
ממקמת 5 ספינות בגודל 1 (תא אחד) באופן אקראי על לוח המשחק של המחשב.

**פרמטרים**:
- `board` (list[list[int]]): לוח המשחק של המחשב.

**החזרות**:
- `None`: פונקציה זו אינה מחזירה ערך.

### `display_board`

**תיאור**:
מציגה את לוח המשחק בטרמינל. אם `is_computer` הוא `True`, ספינות המחשב יוסתרו.

**פרמטרים**:
- `board` (list[list[int]]): לוח המשחק.
- `is_computer` (bool, אופציונלי): אם `True`, ספינות המחשב מוסתרות, ברירת מחדל: `False`.

**החזרות**:
- `None`: פונקציה זו אינה מחזירה ערך.

### `play_battle`

**תיאור**:
פונקצית המשחק הראשית המנהלת את כל מהלך המשחק.

**פרמטרים**:
- `None`: פונקציה זו אינה מקבלת פרמטרים.

**החזרות**:
- `None`: פונקציה זו אינה מחזירה ערך.

**הערות**:
- המשחק מורכב מסיבובים עד 30 סיבובים.
- תור השחקן כולל קבלת קלט מהמשתמש לגבי מיקום הירי.
- תור המחשב כולל בחירה אקראית של מיקום הירי.
- המשחק מדווח אם היריה פגעה או החטיאה.
- המשחק מציג את לוח המשחק בכל תור.
```