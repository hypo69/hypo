# מדריך לפקודות PowerShell

## תוכן עניינים

- [1. יסודות הניווט והעבודה עם קבצים וספריות](#1-יסודות-הניווט-והעבודה-עם-קבצים-וספריות)
- [2. ניהול תהליכים](#2-ניהול-תהליכים)
- [3. ניהול שירותים](#3-ניהול-שירותים)
- [4. עבודה עם רשת](#4-עבודה-עם-רשת)
- [5. עבודה עם הרישום](#5-עבודה-עם-הרישום)
- [6. שונות](#6-שונות)

## 1. יסודות הניווט והעבודה עם קבצים וספריות

*   **`Get-ChildItem`** (או `gci`, `ls`, `dir`): מקבל רשימה של קבצים ותת-ספריות במיקום שצוין.
    *   **תחביר**: `Get-ChildItem [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Path`: מציין את הנתיב לספרייה.
        *   `-Include`: מסנן לפי שם הקובץ (עם תווים כלליים `*` ו-`?`).
        *   `-Exclude`: מוציא קבצים לפי שם.
        *   `-Recurse`: מציג קבצים ותיקיות בכל תת-הספריות.
        *   `-Force`: מציג קבצים מוסתרים
        *   `-File`: מציג רק קבצים
        *   `-Directory`: מציג רק תיקיות
    *   **דוגמאות:**
        *   `Get-ChildItem`: רשימת קבצים ותיקיות בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: רשימת קבצים ותיקיות ב-`C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: רשימה של קבצי טקסט בלבד בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: מציג את כל התיקיות בכונן C
        *   `Get-ChildItem -Force`: מציג את כל הקבצים, כולל מוסתרים

*   **`Set-Location`** (או `sl`, `cd`): משנה את הספרייה הנוכחית.
    *   **תחביר**: `Set-Location [נתיב]`
    *   **דוגמאות:**
        *   `Set-Location C:\Windows`: מעבר לספרייה `C:\Windows`.
        *   `Set-Location ..`: מעבר לספריית האב.
        *  `Set-Location /` - מעבר לשורש הכונן
*   **`New-Item`**: יוצר קובץ או ספרייה חדשים.
    *   **תחביר**: `New-Item -Path [נתיב] -ItemType [סוג] -Name [שם]`
    *   **פרמטרים עיקריים:**
        *   `-ItemType`: `file` או `directory`.
        *   `-Name`: שם הפריט החדש.
        *   `-Value`: תוכן הקובץ.
    *   **דוגמאות:**
        *   `New-Item -ItemType directory -Name NewFolder`: יצירת תיקייה `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: יצירת קובץ ריק `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: יצירת קובץ `myfile.txt` עם תוכן.

*   **`Remove-Item`** (או `rm`, `del`, `erase`): מוחק קבצים וספריות.
    *   **תחביר:** `Remove-Item [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: מחיקת כל תתי הספריות
        *   `-Force`: מחיקה בכוח (כולל קבצים "לקריאה בלבד" וספריות).
        *   `-Confirm` - דרישת אישור עבור כל מחיקה
    *   **דוגמאות:**
        *   `Remove-Item myfile.txt`: מחיקת קובץ `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: מחיקת תיקייה `C:\Temp` עם כל התוכן שלה.

*   **`Copy-Item`**: מעתיק קבצים וספריות.
    *   **תחביר**: `Copy-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: העתקת כל תתי הספריות.
        *   `-Force`: החלפת קבצים קיימים ללא שאלה.
    *   **דוגמאות:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: העתקת קובץ `myfile.txt` ל-`mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: העתקת תיקייה `C:\Source` לתיקייה `D:\Backup` עם כל התוכן שלה.

*   **`Move-Item`**: מעביר קבצים וספריות.
    *   **תחביר**: `Move-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
    * `-Force` - העברה והחלפה בכוח
    *   **דוגמאות:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: העברת קובץ `myfile.txt` לתיקייה `D:\Documents`.
         * `Move-Item -Path "C:\\MyFolder" -Destination "D:\\" -Force`: העברת תיקייה C:\\MyFolder ל- D:\\ בכוח, גם אם כבר קיימת תיקייה בשם זה

*   **`Rename-Item`**: משנה שם של קובץ או ספרייה.
    *   **תחביר**: `Rename-Item -Path [נתיב] -NewName [שם_חדש]`
    *   **דוגמה:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: שינוי שם הקובץ `myfile.txt` ל-`newfile.txt`.

*   **`Get-Content`** (או `gc`): מציג או מקבל את תוכן הקובץ.
    *   **תחביר**: `Get-Content [נתיב]`
    *   **דוגמה:**
        *   `Get-Content myfile.txt`: מציג את תוכן הקובץ `myfile.txt`.
*  **`Set-Content`**: מחליף או יוצר את תוכן הקובץ.
    *   **תחביר:** `Set-Content [נתיב] [פרמטרים]`
    * `-value` - טקסט לכתיבה
    *   **דוגמה:** `Set-Content myfile.txt "טקסט חדש"` - החלפת הטקסט של הקובץ `myfile.txt`
*   **`Add-Content`**: מוסיף תוכן לסוף הקובץ.
   * **תחביר:** `Add-Content [נתיב] [פרמטרים]`
       *  `-value` - טקסט להוספה
   *   **דוגמה:** `Add-Content myfile.txt "עוד טקסט"` - הוספת טקסט לסוף `myfile.txt`

## 2. ניהול תהליכים:

*   **`Get-Process`** (או `gps`): מקבל רשימה של תהליכים שפועלים.
    *   **תחביר**: `Get-Process [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: סינון לפי שם התהליך.
        *   `-Id`: סינון לפי מזהה התהליך.
        *   `-IncludeUserName`: הצגת המשתמש שהפעיל את התהליך
    *   **דוגמאות:**
        *   `Get-Process`: רשימה של כל התהליכים שפועלים.
        *   `Get-Process -Name notepad`: רשימה של תהליכים עם השם `notepad`.
        *   `Get-Process -IncludeUserName`: רשימה של כל התהליכים שפועלים עם משתמשים.

*   **`Stop-Process`**: מסיים תהליך.
    *   **תחביר**: `Stop-Process [פרמטרים]`
    *  `-Id` - ציון מזהה התהליך
    *   `-Name` - ציון שם התהליך
    *  `-Force` - סיום בכוח
    *   **דוגמאות:**
        *   `Stop-Process -Name notepad`: סיום כל תהליכי `notepad`.
         * `Stop-Process -Id 1234` : סיום התהליך עם המזהה 1234.
        *   `Stop-Process -Name chrome -Force` : סיום בכוח של כל תהליכי `chrome`.

## 3. ניהול שירותים:

*   **`Get-Service`**: מקבל רשימה של שירותים.
    *   **תחביר**: `Get-Service [פרמטרים]`
    *   **פרמטרים עיקריים:**
         * `-Name`: הצגת שירותים רק עם השם שצוין
         * `-DisplayName`: הצגת שירותים רק עם השם המוצג שצוין
        *   `-Status`: סינון לפי סטטוס (Running, Stopped).
    *   **דוגמאות:**
        *   `Get-Service`: רשימה של כל השירותים.
        *   `Get-Service -Name Spooler`: הצגת שירות Spooler.
       *   `Get-Service -Status Running`: הצגת שירותים שפועלים.
*   **`Start-Service`**: מפעיל שירות.
    *   **תחביר**: `Start-Service [שם_שירות]`
    *   **דוגמה:** `Start-Service Spooler` - הפעלת שירות Spooler

*   **`Stop-Service`**: עוצר שירות.
    *   **תחביר**: `Stop-Service [שם_שירות]`
     *  `-Force` - עצירת שירות בכוח
    *   **דוגמה:** `Stop-Service Spooler`: עצירת שירות Spooler.
        *   `Stop-Service Spooler -Force` - עצירת שירות Spooler בכוח.

*   **`Restart-Service`**: מפעיל מחדש שירות.
   *   **תחביר:** `Restart-Service [שם_שירות]`
   *   **דוגמה:** `Restart-Service Spooler` - הפעלה מחדש של שירות Spooler.

## 4. עבודה עם רשת

*   **`Test-NetConnection`**: בודק חיבור רשת.
    *   **תחביר**: `Test-NetConnection [שם_מארח_או_ip-כתובת] [פרמטרים]`
    * `-Port` - מספר פורט
    *   **דוגמאות:**
        *   `Test-NetConnection google.com`: בדיקת חיבור ל-`google.com`.
        * `Test-NetConnection google.com -Port 80`: בדיקת חיבור ל-google.com בפורט 80
*   **`Get-NetIPConfiguration`**: מקבל את תצורת הרשת.
    *   **תחביר**: `Get-NetIPConfiguration`
    *   **דוגמה:**
        *   `Get-NetIPConfiguration`: מציג את תצורת הרשת.
*   **`Resolve-DnsName`**: מבצע שאילתת DNS.
    *   **תחביר**: `Resolve-DnsName [שם_מארח]`
    *   **דוגמה:** `Resolve-DnsName google.com`: שאילתת DNS ל-`google.com`.

## 5. עבודה עם הרישום

*   **`Get-ItemProperty`**: מקבל ערך של מאפיין מהרישום.
    *   **תחביר**: `Get-ItemProperty -Path [נתיב_ברישום]`
    *   **דוגמה:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: מגדיר ערך של מאפיין ברישום.
    *   **תחביר**: `Set-ItemProperty -Path [נתיב_ברישום] -Name [שם_מאפיין] -Value [ערך]`
    *   **דוגמה:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

## 6. שונות

*   **`Clear-Host`**: מנקה את מסך הקונסולה.
    *   **תחביר:** `Clear-Host`
*   **`Get-Date`**: מקבל את התאריך והשעה הנוכחיים.
    *   **תחביר:** `Get-Date`
*   **`Start-Process`**: מפעיל תוכנית או פותח קובץ.
    *   **תחביר:** `Start-Process [שם_תוכנית_או_קובץ] [אפשרויות]`
    *   **דוגמאות:**
        *   `Start-Process notepad.exe`: הפעלת פנקס רשימות.
        *   `Start-Process myfile.txt`: פתיחת קובץ `myfile.txt` עם התוכנית המוגדרת כברירת מחדל.
        *  `Start-Process -FilePath "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" -ArgumentList "https://www.google.com"` - פתיחת האתר בכרום
*   **`Get-Help`**: מציג עזרה עבור פקודה.
    *   **תחביר**: `Get-Help [שם_פקודה]`
    *   **דוגמה:** `Get-Help Get-Process`: הצגת עזרה עבור הפקודה `Get-Process`.
*   **`Exit`**: סיום סשן PowerShell
    *   **תחביר:** `Exit`
*  **`Get-Variable`**: מציג את המשתנים הנוכחיים
    *  **תחביר**: `Get-Variable`
*  **`Get-Alias`**: מציג כינויים לפקודות
    *   **תחביר**: `Get-Alias`
*   **`Set-Alias`**: יוצר כינוי לפקודה
    *  **תחביר**: `Set-Alias [שם_כינוי] [שם_פקודה]`
    *  **דוגמה**: `Set-Alias gci Get-ChildItem`

**הערות:**

*   פקודות `PowerShell` (cmdlets) בדרך כלל בנויות בצורה של `פועל-שם_עצם` (לדוגמה, `Get-Process`, `Set-Location`).
*   `PowerShell` אינו רגיש לאותיות גדולות וקטנות, כך שניתן לכתוב פקודות גם כ-`Get-ChildItem` או גם כ-`get-childitem`.
*  `PowerShell` עובד עם אובייקטים, ולכן ניתן להשתמש באופרטור `|` כדי להעביר את הפלט של פקודה אחת לקלט של פקודה אחרת (לדוגמה, `Get-Process | Sort-Object -Property CPU`).
*  פקודות רבות תומכות בשימוש בתווים כלליים (*) לעבודה עם מספר קבצים (לדוגמה `Get-ChildItem *.txt`).
*  כדי לעבוד עם חלק מהפקודות נדרשות הרשאות מנהל.