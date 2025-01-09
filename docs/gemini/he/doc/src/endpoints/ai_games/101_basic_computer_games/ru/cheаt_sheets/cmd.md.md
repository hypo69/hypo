# מדריך פקודות CMD

## סקירה כללית

מסמך זה מספק מדריך מקיף לפקודות שורת הפקודה (CMD) של Windows. הוא כולל פקודות לניהול קבצים וספריות, עבודה עם דיסקים, ניהול מערכת, פעולות רשת, ופקודות שונות נוספות. המסמך נועד לסייע למפתחים ומשתמשים להבין ולנצל את היכולות של שורת הפקודה.

## תוכן עניינים

1. [ניהול קבצים וספריות](#ניהול-קבצים-וספריות)
2. [עבודה עם דיסקים](#עבודה-עם-דיסקים)
3. [ניהול מערכת](#ניהול-מערכת)
4. [רשת](#רשת)
5. [פקודות אחרות](#פקודות-אחרות)
6. [פקודות לעבודה עם קבצי אצווה](#פקודות-לעבודה-עם-קבצי-אצווה)

## ניהול קבצים וספריות

### `attrib`

**Description**: מציג או משנה תכונות של קובץ או ספרייה (מוסתר, לקריאה בלבד, ארכיון, וכו').

**Syntax**: `attrib [+r|-r] [+a|-a] [+s|-s] [+h|-h] [כונן:][נתיב]שם_קובץ`

**Parameters**:
- `+r`: הגדר את התכונה "לקריאה בלבד".
- `-r`: הסר את התכונה "לקריאה בלבד".
- `+a`: הגדר את התכונה "ארכיון".
- `-a`: הסר את התכונה "ארכיון".
- `+s`: הגדר את התכונה "מערכת".
- `-s`: הסר את התכונה "מערכת".
- `+h`: הגדר את התכונה "מוסתר".
- `-h`: הסר את התכונה "מוסתר".

**Examples**:
- `attrib +h myfile.txt`: הופך את הקובץ `myfile.txt` למוסתר.
- `attrib -r myfile.txt`: מסיר את התכונה "לקריאה בלבד" מהקובץ `myfile.txt`.
- `attrib *.*`: מציג את תכונות כל הקבצים בספרייה הנוכחית.

### `cd` או `chdir`

**Description**: משנה את הספרייה הנוכחית.

**Syntax**: `cd [נתיב]` או `chdir [נתיב]`

**Parameters**:
- `..`: מעבר לספריית האב.
- `\`: מעבר לשורש הכונן.

**Examples**:
- `cd Documents`: מעבר לתיקייה `Documents` בספרייה הנוכחית.
- `cd C:\Users\User\Downloads`: מעבר לתיקייה `Downloads` בכונן C.
- `cd ..`: מעבר לספריית האב.
- `cd \`: מעבר לשורש הכונן הנוכחי.

### `copy`

**Description**: מעתיק קובץ אחד או יותר.

**Syntax**: `copy [קובץ_מקור] [קובץ_יעד]`

**Parameters**:
- `/a`: העתקת קובץ ASCII.
- `/b`: העתקת קובץ בינארי.
- `/v`: אימות שהקבצים הועתקו כראוי.

**Examples**:
- `copy myfile.txt mycopy.txt`: מעתיק את הקובץ `myfile.txt` ל-`mycopy.txt`.
- `copy *.txt C:\Backup`: מעתיק את כל הקבצים עם סיומת `.txt` לתיקייה `C:\Backup`.

### `del` או `erase`

**Description**: מוחק קובץ אחד או יותר.

**Syntax**: `del [שם_קובץ]` או `erase [שם_קובץ]`

**Parameters**:
- `/p`: בקשה לאישור לפני מחיקת כל קובץ.
- `/f`: מחיקת קבצים "לקריאה בלבד".
- `/s`: מחיקת קבצים מתת-ספריות.
- `/q`: מחיקת קבצים ללא אישור.

**Examples**:
- `del myfile.txt`: מחיקת הקובץ `myfile.txt`.
- `del *.tmp`: מחיקת כל הקבצים עם סיומת `.tmp`.
- `del /f /s *.log`: מחיקת כל קבצי ה-.log בספרייה הנוכחית ובתת-הספריות ללא אישור.

### `dir`

**Description**: מציג רשימה של קבצים וספריות בספרייה הנוכחית.

**Syntax**: `dir [נתיב] [אפשרויות]`

**Parameters**:
- `/a`: הצגת כל הקבצים (כולל מוסתרים).
- `/w`: הצגת הרשימה בפורמט רחב.
- `/p`: הצגת הרשימה בדפים.
- `/s`: הצגת קבצים מתת-ספריות.
- `/b`: הצגת רק את שם הקובץ.

**Examples**:
- `dir`: הצגת רשימת הקבצים והספריות בספרייה הנוכחית.
- `dir C:\Users\User\Documents /a`: הצגת כל הקבצים בתיקייה `Documents`.
- `dir /w`: הצגת רשימת הקבצים והספריות בפורמט רחב.
- `dir /b /s *.txt`: הצגת כל קבצי ה-*.txt עם הנתיב המלא שלהם.

### `mkdir` או `md`

**Description**: יוצר ספרייה חדשה.

**Syntax**: `mkdir [נתיב]` או `md [נתיב]`

**Examples**:
- `mkdir NewFolder`: יצירת תיקייה חדשה `NewFolder` בספרייה הנוכחית.
- `mkdir C:\Backup`: יצירת תיקייה חדשה `Backup` בכונן C.

### `move`

**Description**: מעביר קובץ אחד או יותר או ספריות.

**Syntax**: `move [קובץ_מקור] [קובץ_יעד]`

**Examples**:
- `move myfile.txt C:\Documents`: העברת הקובץ `myfile.txt` לתיקייה `C:\Documents`.
- `move dir1 dir2`: העברת התיקייה `dir1` לתיקייה `dir2`.

### `rd` או `rmdir`

**Description**: מוחק ספרייה.

**Syntax**: `rd [נתיב]` או `rmdir [נתיב]`

**Parameters**:
- `/s`: מחיקת הספרייה וכל תת-הספריות שלה.
- `/q`: מחיקת הספרייה ללא אישור.

**Examples**:
- `rd myfolder`: מחיקת התיקייה הריקה `myfolder`.
- `rd /s /q myfolder`: מחיקת התיקייה `myfolder` עם כל תכולתה ללא אישור.

### `ren` או `rename`

**Description**: משנה שם של קובץ או ספרייה.

**Syntax**: `ren [שם_ישן] [שם_חדש]`

**Examples**:
- `ren myfile.txt newfile.txt`: שינוי שם הקובץ `myfile.txt` ל-`newfile.txt`.

### `type`

**Description**: מציג את תוכן קובץ הטקסט.

**Syntax**: `type [שם_קובץ]`

**Example**: `type myfile.txt`: הצגת תוכן הקובץ `myfile.txt`.

### `xcopy`

**Description**: מעתיק קבצים וספריות (כולל תת-ספריות).

**Syntax**: `xcopy [מקור] [יעד] [אפשרויות]`

**Parameters**:
- `/s`: העתקת ספריות ותת-ספריות (לא כולל ריקות).
- `/e`: העתקת ספריות ותת-ספריות (כולל ריקות).
- `/i`: אם היעד לא קיים, צור אותו.
- `/y`: דיכוי בקשת אישור להעתקה.
- `/d`: העתקת רק קבצים חדשים.

**Examples**:
- `xcopy C:\Source D:\Destination /s`: העתקת התיקייה `C:\Source` וכל תת-הספריות לתיקייה `D:\Destination`.
- `xcopy C:\Source D:\Destination /e /y`: העתקת התיקייה `C:\Source` וכל תת-הספריות לתיקייה `D:\Destination`, כולל ריקות, ללא אישור.

## עבודה עם דיסקים

### `diskpart`

**Description**: הפעלת כלי לניהול דיסקים (מחיצות, כרכים).

**Syntax**: `diskpart`

**Notes**:
- `diskpart` הוא כלי אינטראקטיבי עם סט פקודות משלו.
- דורש הרשאות מנהל מערכת.
- פרטים נוספים ניתן ללמוד באמצעות פקודת `help` בתוך הכלי.

### `format`

**Description**: פרמוט דיסק.

**Syntax**: `format [כונן:] [אפשרויות]`

**Parameters**:
- `/q`: פרמוט מהיר.
- `/fs:file-system`: בחירת סוג מערכת הקבצים (לדוגמה, NTFS, FAT32).

**Examples**:
- `format D: /q`: פרמוט מהיר של כונן D:.
- `format E: /fs:NTFS`: פרמוט כונן E: למערכת קבצים NTFS.

**Warning**: פרמוט דיסק מוחק את כל הנתונים בו!

### `label`

**Description**: מגדיר או משנה תווית של דיסק.

**Syntax**: `label [כונן:][תווית]`

**Examples**:
- `label D: NewLabel`: הגדרת התווית `NewLabel` על כונן D.
- `label D:`: מחיקת התווית מכונן D.

## ניהול מערכת

### `cls`

**Description**: מנקה את מסך שורת הפקודה.

**Syntax**: `cls`

### `date`

**Description**: מציג או משנה את התאריך הנוכחי.

**Syntax**: `date [תאריך_חדש]`

**Examples**:
- `date`: הצגת התאריך הנוכחי.
- `date 12-25-2024`: שינוי התאריך ל-25 בדצמבר 2024.

### `exit`

**Description**: סוגר את שורת הפקודה.

**Syntax**: `exit`

### `shutdown`

**Description**: כיבוי או הפעלה מחדש של המחשב.

**Syntax**: `shutdown [אפשרויות]`

**Parameters**:
- `/s`: כיבוי המחשב.
- `/r`: הפעלה מחדש של המחשב.
- `/a`: ביטול כיבוי או הפעלה מחדש.
- `/t xxx`: עיכוב בשניות לפני כיבוי או הפעלה מחדש.

**Examples**:
- `shutdown /s /t 60`: כיבוי המחשב לאחר 60 שניות.
- `shutdown /r`: הפעלה מחדש של המחשב.
- `shutdown /a`: ביטול כיבוי או הפעלה מחדש מתוכננים.

### `tasklist`

**Description**: הצגת רשימה של תהליכים רצים.

**Syntax**: `tasklist [אפשרויות]`

**Parameters**:
- `/v`: מידע נוסף.
- `/fo csv`: פלט בפורמט CSV.
- `/fi "имя_образа eq notepad.exe"`: מציאת תהליכי פנקס רשימות.

**Examples**:
- `tasklist`: הצגת רשימת תהליכים רצים.
- `tasklist /v`: הצגת רשימת תהליכים רצים עם מידע מפורט.

### `taskkill`

**Description**: סיום תהליך.

**Syntax**: `taskkill [אפשרויות]`

**Parameters**:
- `/im שם_התוכנה`: סיום תהליך לפי שם.
- `/pid מזהה`: סיום תהליך לפי מזהה.
- `/f`: סיום תהליך בכפייה.

**Examples**:
- `taskkill /im notepad.exe`: סיום כל תהליכי `notepad.exe`.
- `taskkill /pid 1234`: סיום תהליך עם מזהה 1234.
- `taskkill /im notepad.exe /f`: סיום בכפייה של כל תהליכי `notepad.exe`.

### `time`

**Description**: מציג או משנה את השעה הנוכחית.

**Syntax**: `time [שעה_חדשה]`

**Examples**:
- `time`: הצגת השעה הנוכחית.
- `time 15:30`: הגדרת השעה ל-15:30.

### `ver`

**Description**: מציג את גרסת מערכת ההפעלה.

**Syntax**: `ver`

### `systeminfo`

**Description**: מציג מידע מפורט על המערכת.

**Syntax**: `systeminfo`

### `taskmgr`

**Description**: פותח את מנהל המשימות.

**Syntax**: `taskmgr`

## רשת

### `ipconfig`

**Description**: מציג את תצורת הרשת.

**Syntax**: `ipconfig [אפשרויות]`

**Parameters**:
- `/all`: הצגת מידע מלא על מתאמי הרשת.
- `/release`: שחרור כתובת IP.
- `/renew`: בקשת כתובת IP חדשה.

**Examples**:
- `ipconfig`: הצגת תצורת רשת בסיסית.
- `ipconfig /all`: הצגת מידע מלא על כל מתאמי הרשת.
- `ipconfig /release`: שחרור כתובת ה-IP.
- `ipconfig /renew`: בקשת כתובת IP חדשה.

### `ping`

**Description**: שליחת בקשת הד לשרת אחר ברשת.

**Syntax**: `ping [שם_מארח_או_כתובת_ip] [אפשרויות]`

**Parameters**:
- `-n xxx`: מספר הבקשות.
- `-t`: בקשות פינג אינסופיות.

**Examples**:
- `ping google.com`: פינג לשרת `google.com`.
- `ping 192.168.1.100`: פינג למחשב עם כתובת IP `192.168.1.100`.
- `ping google.com -n 10`: ביצוע 10 פינגים.

### `tracert`

**Description**: מציג את נתיב החבילות למחשב אחר ברשת.

**Syntax**: `tracert [שם_מארח_או_כתובת_ip]`

**Example**: `tracert google.com`: הצגת נתיב החבילות ל-`google.com`.

### `netstat`

**Description**: מציג חיבורי רשת.

**Syntax**: `netstat [אפשרויות]`

**Parameters**:
- `-a`: הצגת כל החיבורים.
- `-b`: הצגת יישומים שיצרו חיבורים.

**Examples**:
- `netstat`: הצגת כל החיבורים הפעילים.
- `netstat -a -b`: הצגת כל החיבורים ויישומים שיצרו אותם.

### `nslookup`

**Description**: שאילתות מידע DNS.

**Syntax**: `nslookup [שם_מארח]`

**Example**: `nslookup google.com`: שאילתת מידע DNS עבור `google.com`.

## פקודות אחרות

### `assoc`

**Description**: מציג או משנה אסוציאציות קבצים.

**Syntax**: `assoc [.סיומת]=[סוג_קובץ]`

**Examples**:
- `assoc .txt`: הצגת סוג הקובץ עבור סיומת `.txt`.
- `assoc .txt=txtfile`: הגדרת סוג הקובץ עבור סיומת `.txt` כ-`txtfile`.

### `call`

**Description**: קורא לקובץ אצווה אחר.

**Syntax**: `call [שם_קובץ_אצווה]`

**Example**: `call mybatch.bat`: קריאה לקובץ האצווה `mybatch.bat`.

### `chcp`

**Description**: משנה את קידוד העמוד של המסוף.

**Syntax**: `chcp [מספר_קידוד]`

**Examples**:
- `chcp 1251`: הגדרת קידוד עבור קירילית.
- `chcp`: הצגת קידוד נוכחי.

### `choice`

**Description**: מאפשר למשתמש לבחור מרשימת אפשרויות.

**Syntax**: `choice [/c [אפשרויות]] [/n] [/t [שניות]] [/d [אפשרות]] [טקסט]`

**Parameters**:
- `/c`: הגדרת אפשרויות זמינות.
- `/n`: הסתרת רשימת אפשרויות.
- `/t`: הגדרת זמן המתנה (בשניות).
- `/d`: הגדרת אפשרות ברירת מחדל.

**Example**: `choice /c yn /t 10 /d n "האם אתה באמת רוצה לצאת?"`

### `find`

**Description**: חיפוש מחרוזת טקסט בקובץ.

**Syntax**: `find "מחרוזת" [שם_קובץ]`

**Examples**:
- `find "Hello" myfile.txt`: חיפוש מחרוזת "Hello" בקובץ `myfile.txt`.

### `findstr`

**Description**: חיפוש מחרוזות טקסט בקבצים (חזק יותר מ-`find`).

**Syntax**: `findstr [אפשרויות] "מחרוזת" [שם_קובץ]`

**Parameters**:
- `/i`: חיפוש ללא תלות באותיות רישיות/קטנות.
- `/n`: הצגת מספרי שורות.
- `/s`: חיפוש בכל תת-ספריות.

**Examples**:
- `findstr /i "error" myfile.log`: חיפוש מחרוזת "error" (ללא תלות באותיות) ב-`myfile.log`.
- `findstr /n "error" *.log`: חיפוש מחרוזת "error" בכל קבצי ה-.log והצגת מספרי שורות.

### `gpupdate`

**Description**: עדכון מדיניות קבוצתית.

**Syntax**: `gpupdate [אפשרויות]`

**Parameters**:
- `/force`: עדכון בכפייה.

**Example**: `gpupdate /force`: עדכון בכפייה של מדיניות קבוצתית.

### `help` או `/?`

**Description**: הצגת עזרה עבור פקודה.

**Syntax**: `help [שם_פקודה]` או `[שם_פקודה] /?`

**Example**: `help dir` או `dir /?`: הצגת עזרה עבור פקודה `dir`.

### `pause`

**Description**: השהיית ביצוע של קובץ אצווה והמתנה ללחיצת מקש.

**Syntax**: `pause`

### `path`

**Description**: הצגה או שינוי של משתני סביבה PATH.

**Syntax**: `path [נתיב]`

**Examples**:
- `path`: הצגת הערך הנוכחי של משתנה PATH.
- `path C:\bin`: הוספת התיקייה `C:\bin` למשתנה PATH.

### `prompt`

**Description**: הגדרת מחרוזת שורת הפקודה.

**Syntax**: `prompt [טקסט]`

**Examples**:
- `prompt $p$g`: הגדרת שורת הפקודה לנתיב הנוכחי.
- `prompt MyPrompt>`: הגדרת שורת הפקודה ל-`MyPrompt>`.

### `set`

**Description**: הצגה, הגדרה או הסרה של משתני סביבה.

**Syntax**: `set [שם=[ערך]]`

**Examples**:
- `set`: הצגת כל משתני הסביבה.
- `set myvar=myvalue`: הגדרת משתנה סביבה `myvar` לערך `myvalue`.
- `set myvar=`: הסרת משתנה סביבה `myvar`.

### `start`

**Description**: הפעלת תוכנית או פתיחת קובץ.

**Syntax**: `start [שם_תוכנית_או_קובץ] [אפשרויות]`

**Examples**:
- `start notepad.exe`: הפעלת פנקס רשימות.
- `start myfile.txt`: פתיחת הקובץ `myfile.txt` בתוכנית ברירת המחדל.
- `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"`: פתיחת אתר בכרום.

### `tree`

**Description**: הצגת מבנה גרפי של ספריות.

**Syntax**: `tree [כונן:][נתיב] [אפשרויות]`

**Parameters**:
- `/f`: הצגת גם שמות קבצים.
- `/a`: שימוש בתווי ASCII.

**Examples**:
- `tree`: הצגת מבנה התיקייה הנוכחית.
- `tree /f`: הצגת מבנה התיקייה הנוכחית עם קבצים.

### `where`

**Description**: מציאת מיקום קובץ.

**Syntax**: `where [שם_קובץ]`

**Example**: `where notepad.exe`

## פקודות לעבודה עם קבצי אצווה

### `echo`

**Description**: הצגת טקסט על המסך.

**Syntax**: `echo [טקסט]`
*  `echo on` - הפעלת הצגת פקודות בביצוע קובץ אצווה
*  `echo off` - כיבוי הצגת פקודות בביצוע קובץ אצווה

**Examples**:
- `echo Hello, world!`: הצגת "Hello, world!".
- `echo off`: כיבוי הצגת פקודות.
- `echo on`: הפעלת הצגת פקודות.

### `rem`

**Description**: הוספת הערה לקובץ אצווה.

**Syntax**: `rem [הערה]`

**Example**: `rem This is a comment`

### `goto`

**Description**: מעבר לתווית.

**Syntax**: `goto [תווית]`

**Example**:
```batch
:start
echo Hello
goto end
echo This will not be displayed
:end
echo Goodbye
```

### `if`

**Description**: ביצוע לוגיקה מותנית.

**Syntax**: `if [not] condition (פקודה1) else (פקודה2)`

**Examples**:
* `if exist file.txt echo file exists`: בדיקה אם הקובץ קיים.
* `if %var%== "text" echo variable has value`: בדיקה אם משתנה שווה ל-"text".

### `for`

**Description**: ביצוע פעולה בלולאה.

**Syntax**: `for %%משתנה in (אוסף) do [פקודה]`

**Example**:
```batch
for %%a in (*.txt) do (
 echo %%a
 type %%a
 echo -------------
)
```
* הצגת שם כל קובץ `.txt` ותוכנו.

**Warning:**
* יש לנקוט זהירות בעת שימוש בפקודות שעלולות לשנות את המערכת, במיוחד עם הרשאות מנהל מערכת.
* לפני ביצוע פקודה `format` יש לוודא שאתה בוחר את הדיסק הנכון.