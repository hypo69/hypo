# CHIEF

## סקירה כללית

משחק "CHIEF" הוא משחק בו השחקן משחק בתפקיד מנהל, המתכנן את הייצור במפעל. השחקן קובע את כמות המוצרים המיוצרים מכל סוג, והמחשב קובע אם הערכים הללו עומדים בדרישות הנדרשות. אם לא, השחקן מקבל הודעה אילו ערכים היו שגויים. מטרת המשחק היא להגיע לייצור מיטבי על ידי ניחוש נכון של מספר הפריטים.

## תוכן עניינים

1. [סקירה כללית](#סקירה-כללית)
2. [חוקי המשחק](#חוקי-המשחק)
3. [אלגוריתם](#אלגוריתם)
4. [פונקציות](#פונקציות)

## חוקי המשחק

1. המחשב בוחר שלושה ערכים בטווח שבין 1 ל-10: `targetA`, `targetB` ו-`targetC`.
2. השחקן מזין את ההשערות שלו לגבי הערכים `userA`, `userB` ו-`userC`.
3. המחשב בודק אם הערכים שהוזנו תואמים את הערכים שנבחרו.
4. אם כל שלושת הערכים מנוחשים נכון, המשחק מסתיים בניצחון.
5. אם לפחות ערך אחד אינו תואם, המחשב מציג אילו ערכים היו שגויים.
6. המשחק נמשך עד שהשחקן מנחש את כל שלושת הערכים.

## אלגוריתם

1. יצירת מספרים שלמים אקראיים `targetA`, `targetB` ו-`targetC` בטווח שבין 1 ל-10.
2. התחלת לולאה "כל עוד לא נוחשו כל המספרים":
    2.1. בקשת קלט משחקן של שלושה מספרים שלמים: `userA`, `userB` ו-`userC`.
    2.2. אתחול מחרוזת `message` כמחרוזת ריקה.
    2.3. אם `userA` אינו שווה ל-`targetA`, הוספת "A" ל-`message`.
    2.4. אם `userB` אינו שווה ל-`targetB`, הוספת "B" ל-`message`.
    2.5. אם `userC` אינו שווה ל-`targetC`, הוספת "C" ל-`message`.
    2.6. אם `message` אינה ריקה, הצגת ההודעה "WRONG ON " ו-`message`.
    2.7. אחרת, הצגת ההודעה "YOU GOT IT!".
3. סיום המשחק.

## פונקציות

### אין פונקציות מוגדרות באופן מפורש בקוד זה.
הקוד משתמש בלולאה ראשית ליישום ההיגיון של המשחק. עם זאת, ישנם קטעי קוד שניתן לראות בהם פונקציות לוגיות:

#### הגרלת מספרים אקראיים
    
**תיאור**: מייצרת מספרים אקראיים לניחוש.

**פרמטרים**:
- אין פרמטרים.

**מחזירה**:
- אין ערך מוחזר ישירות. המשתנים `targetA`, `targetB`, ו-`targetC` מוגדרים עם מספרים אקראיים בין 1 ל-10.

#### קבלת קלט משתמש

**תיאור**: מקבלת קלט משתמש עבור ניחוש שלושת המספרים.
     
**פרמטרים**:
- אין פרמטרים.

**מחזירה**:
- אין ערך מוחזר ישירות. המשתנים `userA`, `userB`, ו-`userC` מתעדכנים עם קלט משתמש.

**Raises**:
- `ValueError`: אם המשתמש מזין קלט שאינו מספר שלם.

#### בדיקת קלט המשתמש

**תיאור**: בודקת את הקלט של המשתמש מול המספרים האקראיים.

**פרמטרים**:
- אין פרמטרים. משתמש במשתנים `userA`, `userB`, `userC`, `targetA`, `targetB`, ו-`targetC`.

**מחזירה**:
- אין ערך מוחזר ישירות. מחרוזת `message` מעודכנת בהתאם לשגיאות הקלט.

#### הצגת תוצאות

**תיאור**: מציגה את תוצאות הניחוש למשתמש.

**פרמטרים**:
- אין פרמטרים. משתמש במשתנה `message`.

**מחזירה**:
- אין ערך מוחזר ישירות. מדפיס פלט למסך, או הודעת שגיאה או הודעת הצלחה.