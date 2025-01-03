# Acey Ducey Game Flow

## סקירה כללית

תיעוד זה מספק סקירה כללית של זרימת המשחק Acey Ducey, כפי שמוצג בתרשים הזרימה. הוא מתאר את השלבים העיקריים של המשחק, כולל התחלת המשחק, קבלת החלטות והסיום שלו.

## תוכן עניינים

1.  [סקירה כללית](#סקירה-כללית)
2.  [תרשים זרימה](#תרשים-זרימה)
    - [התחלת המשחק](#התחלת-המשחק)
    - [איפוס המשחק](#איפוס-המשחק)
    - [לולאת המשחק](#לולאת-המשחק)
    - [בדיקת יתרה](#בדיקת-יתרה)
    - [הצגת יתרה](#הצגת-יתרה)
    - [חלוקת קלפים](#חלוקת-קלפים)
    - [בדיקת קלפים זהים](#בדיקת-קלפים-זהים)
    - [ציור קלפים מחדש](#ציור-קלפים-מחדש)
    - [הצגת קלפים](#הצגת-קלפים)
    - [ביצוע הימור](#ביצוע-הימור)
    - [אימות הימור](#אימות-הימור)
    - [בדיקת מעבר](#בדיקת-מעבר)
    - [דילוג על תור](#דילוג-על-תור)
    - [ציור קלף הבא](#ציור-קלף-הבא)
    - [בדיקת תוצאה](#בדיקת-תוצאה)
    - [ניצחון](#ניצחון)
    - [הפסד](#הפסד)
    - [עדכון יתרה - ניצחון](#עדכון-יתרה---ניצחון)
    - [עדכון יתרה - הפסד](#עדכון-יתרה---הפסד)
    - [סיום המשחק](#סיום-המשחק)
    - [הצגת יתרה סופית](#הצגת-יתרה-סופית)
    - [סוף המשחק](#סוף-המשחק)

## תרשים זרימה

### התחלת המשחק
 
המשחק מתחיל.

### איפוס המשחק
 
יצירת חפיסת קלפים, היתרה ההתחלתית מוגדרת ל-100$.

### לולאת המשחק
 
מנהלת את המשחק כל עוד היתרה חיובית ויש מספיק קלפים בחפיסה.

### בדיקת יתרה
 
בודקת אם היתרה של השחקן גדולה מ-0 ושיש לפחות 3 קלפים בחפיסה.

### הצגת יתרה
 
מציגה את היתרה הנוכחית של השחקן.

### חלוקת קלפים
 
מחלקת שני קלפים מהחפיסה.

### בדיקת קלפים זהים
 
בודקת אם שני הקלפים שחולקו זהים.

### ציור קלפים מחדש
 
מערבבת מחדש את החפיסה ומחלקת שני קלפים חדשים אם הקלפים הראשונים היו זהים.

### הצגת קלפים
 
מציגה את הקלפים שחולקו לשחקן.

### ביצוע הימור
 
מאפשרת לשחקן לבצע הימור או לדלג על התור.

### אימות הימור
 
בודקת אם ההימור שבוצע תקין.

### בדיקת מעבר
 
בודקת אם ההימור שבוצע הוא 0.

### דילוג על תור
 
מדלגת על התור של השחקן אם הוא לא ביצע הימור.

### ציור קלף הבא
 
מחלקת את הקלף השלישי מהחפיסה.

### בדיקת תוצאה
 
בודקת אם הקלף השלישי נמצא בין שני הקלפים הראשונים.

### ניצחון
 
השחקן ניצח אם הקלף השלישי נמצא בין שני הקלפים הראשונים.

### הפסד
 
השחקן מפסיד אם הקלף השלישי אינו בין שני הקלפים הראשונים או אם הוא שווה לאחד מהם או אם הוא אס.

### עדכון יתרה - ניצחון
 
מעדכנת את יתרת השחקן בתוספת סכום ההימור.

### עדכון יתרה - הפסד
 
מעדכנת את יתרת השחקן בניכוי סכום ההימור.

### סיום המשחק
 
המשחק מסתיים כאשר היתרה של השחקן קטנה או שווה ל-0 או כאשר אין מספיק קלפים בחפיסה.

### הצגת יתרה סופית
 
מציגה את היתרה הסופית של השחקן.

### סוף המשחק
 
סיום המשחק.