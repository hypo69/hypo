# PowerShell Cheat Sheet

## תוכן עניינים

1.  [יסודות ניווט ועבודה עם קבצים וספריות](#1-יסודות-ניווט-ועבודה-עם-קבצים-וספריות)
2.  [ניהול תהליכים](#2-ניהול-תהליכים)
3.  [ניהול שירותים](#3-ניהול-שירותים)
4.  [עבודה עם רשת](#4-עבודה-עם-רשת)
5.  [עבודה עם רישום](#5-עבודה-עם-רישום)
6.  [שונות](#6-שונות)

## 1. יסודות ניווט ועבודה עם קבצים וספריות

*   **`Get-ChildItem` (או `gci`, `ls`, `dir`)**: מקבל רשימה של קבצים ותתי ספריות במיקום שצוין.
    *   **תחביר**: `Get-ChildItem [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Path`: מציין את הנתיב לספרייה.
        *   `-Include`: מסנן לפי שם קובץ (עם תווים כלליים `*` ו- `?`).
        *   `-Exclude`: מוציא קבצים לפי שם.
        *   `-Recurse`: מציג קבצים ותיקיות בכל תתי הספריות.
        *   `-Force`: הצג קבצים מוסתרים
        *   `-File`: הצג רק קבצים
        *   `-Directory`: הצג רק תיקיות
    *   **דוגמאות:**
        *   `Get-ChildItem`: רשימת קבצים ותיקיות בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\Users\User\Documents`: רשימת קבצים ותיקיות ב-`C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt`: רשימה של קבצי טקסט בלבד בספרייה הנוכחית.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory`: הצג את כל הספריות בדיסק C
        *  `Get-ChildItem -Force`: הצג את כל הקבצים, כולל קבצים מוסתרים
*   **`Set-Location` (או `sl`, `cd`)**: משנה את הספרייה הנוכחית.
    *   **תחביר**: `Set-Location [נתיב]`
    *   **דוגמאות:**
        *   `Set-Location C:\Windows`: מעבר לספרייה `C:\Windows`.
        *   `Set-Location ..`: מעבר לספריית האב.
        * `Set-Location /` - מעבר לשורש הדיסק
*   **`New-Item`**: יוצר קובץ או ספרייה חדשים.
    *   **תחביר**: `New-Item -Path [נתיב] -ItemType [סוג] -Name [שם]`
    *   **פרמטרים עיקריים:**
        *   `-ItemType`: `file` או `directory`.
        *   `-Name`: שם הפריט החדש.
        *   `-Value`: תוכן הקובץ.
    *   **דוגמאות:**
        *   `New-Item -ItemType directory -Name NewFolder`: יוצר תיקייה `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt`: יוצר קובץ ריק `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"`: יוצר קובץ `myfile.txt` עם תוכן.
*  **`Remove-Item` (או `rm`, `del`, `erase`)**: מסיר קבצים ותיקיות.
    *   **תחביר:** `Remove-Item [נתיב] [פרמטרים]`
    *   **פרמטרים עיקריים:**
         *   `-Recurse`:  מחק את כל תתי הספריות
        *   `-Force`: מחיקה בכפייה (כולל קבצים "לקריאה בלבד" ותיקיות).
       *  `-Confirm` - בקש אישור לכל מחיקה
    *   **דוגמאות:**
        *   `Remove-Item myfile.txt`: מוחק את הקובץ `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force`: מוחק את התיקייה `C:\Temp` עם כל תיקיות וקבצים מקוננים.
*   **`Copy-Item`**: מעתיק קבצים ותיקיות.
    *   **תחביר**: `Copy-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Recurse`: העתק את כל תתי הספריות.
        *   `-Force`: דרוס קבצים קיימים ללא בקשה.
    *   **דוגמאות:**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt`: מעתיק את הקובץ `myfile.txt` ל-`mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse`: מעתיק את התיקייה `C:\Source` לכל תתי הספריות בתיקייה `D:\Backup`.
*   **`Move-Item`**: מעביר קבצים ותיקיות.
    *   **תחביר**: `Move-Item [נתיב_מקור] [נתיב_יעד] [פרמטרים]`
      *  `-Force` - העבר ודרוס בכוח
    *   **דוגמאות:**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents`: מעביר את הקובץ `myfile.txt` לתיקייה `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force`: העבר את התיקייה C:\MyFolder ל D:\ בכפייה, גם אם שם כבר קיימת תיקייה בשם זה
*   **`Rename-Item`**: משנה שם של קובץ או תיקייה.
    *   **תחביר**: `Rename-Item -Path [נתיב] -NewName [שם_חדש]`
    *   **דוגמה:**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt`: משנה שם של הקובץ `myfile.txt` ל- `newfile.txt`.
*   **`Get-Content` (או `gc`)**: מציג או מקבל את תוכן הקובץ.
    *   **תחביר**: `Get-Content [נתיב]`
    *   **דוגמה:**
        *   `Get-Content myfile.txt`: מציג את תוכן הקובץ `myfile.txt`.
*   **`Set-Content`**: מחליף או יוצר תוכן של קובץ.
    *   **תחביר:** `Set-Content [נתיב] [פרמטרים]`
        *  `-value` - טקסט לכתיבה
   *   **דוגמה:** `Set-Content myfile.txt "טקסט חדש"` - החלף את הטקסט של הקובץ `myfile.txt`
*   **`Add-Content`**: מוסיף תוכן לסוף הקובץ.
   * **תחביר:** `Add-Content [נתיב] [פרמטרים]`
       *  `-value` - טקסט להוספה
   *   **דוגמה:** `Add-Content myfile.txt "עוד טקסט"` - הוסף טקסט לסוף `myfile.txt`

## 2. ניהול תהליכים:

*   **`Get-Process` (או `gps`)**: מקבל רשימה של תהליכים פועלים.
    *   **תחביר**: `Get-Process [פרמטרים]`
    *   **פרמטרים עיקריים:**
        *   `-Name`: מסנן לפי שם התהליך.
        *   `-Id`: מסנן לפי מזהה התהליך.
        *    `-IncludeUserName`: הצג את המשתמש שהפעיל את התהליך
    *   **דוגמאות:**
        *   `Get-Process`: רשימה של כל התהליכים הפועלים.
        *   `Get-Process -Name notepad`: רשימה של תהליכים בשם `notepad`.
        *    `Get-Process -IncludeUserName`: רשימה של כל התהליכים הפועלים עם משתמשים.
*   **`Stop-Process`**: מסיים תהליך.
    *   **תחביר**: `Stop-Process [פרמטרים]`
     *  `-Id` - ציין מזהה תהליך
    *   `-Name` - ציין שם תהליך
    *  `-Force` - סיים תהליך בכפייה
    *   **דוגמאות:**
        *   `Stop-Process -Name notepad`: מסיים את כל תהליכי `notepad`.
         *    `Stop-Process -Id 1234` : סיים תהליך עם מזהה 1234.
        *    `Stop-Process -Name chrome -Force` : סיים בכפייה את כל תהליכי `chrome`.

## 3. ניהול שירותים:

*   **`Get-Service`**: מקבל רשימה של שירותים.
    *   **תחביר**: `Get-Service [פרמטרים]`
    *   **פרמטרים עיקריים:**
         * `-Name`: הצג רק שירותים עם השם שצוין
         * `-DisplayName`: הצג רק שירותים עם השם המוצג שצוין
        *   `-Status`: מסנן לפי סטטוס (Running, Stopped).
    *   **דוגמאות:**
        *   `Get-Service`: רשימה של כל השירותים.
        *   `Get-Service -Name Spooler`: הצג את השירות Spooler.
       *   `Get-Service -Status Running`: הצג שירותים פועלים.
*  **`Start-Service`**: מפעיל שירות.
   *   **תחביר**: `Start-Service [שם_שירות]`
   *   **דוגמה:** `Start-Service Spooler` - הפעל את השירות Spooler
*   **`Stop-Service`**: עוצר שירות.
    *   **תחביר**: `Stop-Service [שם_שירות]`
        *  `-Force` - עצור שירות בכפייה
    *   **דוגמה:** `Stop-Service Spooler`: עצור את השירות Spooler.
        *   `Stop-Service Spooler -Force` - עצור את השירות Spooler בכפייה.
*  **`Restart-Service`**: מפעיל מחדש שירות.
   *   **תחביר:** `Restart-Service [שם_שירות]`
   *   **דוגמה:** `Restart-Service Spooler` - הפעל מחדש את השירות Spooler.

## 4. עבודה עם רשת

*   **`Test-NetConnection`**: בודק חיבור רשת.
    *   **תחביר**: `Test-NetConnection [שם_מארח_או_כתובת_ip] [פרמטרים]`
    *  `-Port` - מספר פורט
    *   **דוגמאות:**
        *   `Test-NetConnection google.com`: בדוק חיבור עם `google.com`.
        * `Test-NetConnection google.com -Port 80`: בדוק חיבור עם google.com בפורט 80
*   **`Get-NetIPConfiguration`**: מקבל את תצורת הרשת.
    *   **תחביר**: `Get-NetIPConfiguration`
    *   **דוגמה:**
        *   `Get-NetIPConfiguration`: הצג את תצורת הרשת.
*   **`Resolve-DnsName`**: מבקש מידע DNS.
    *   **תחביר**: `Resolve-DnsName [שם_מארח]`
    *   **דוגמה:** `Resolve-DnsName google.com`: בקש מידע DNS עבור `google.com`.

## 5. עבודה עם רישום

*   **`Get-ItemProperty`**: מקבל את הערך של מאפיין מהרישום.
    *   **תחביר**: `Get-ItemProperty -Path [נתיב_ברישום]`
    *   **דוגמה:** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`**: מגדיר את הערך של מאפיין ברישום.
    *   **תחביר**: `Set-ItemProperty -Path [נתיב_ברישום] -Name [שם_מאפיין] -Value [ערך]`
    *   **דוגמה:** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

## 6. שונות

*   **`Clear-Host`**: מנקה את מסך הקונסולה.
    *   **תחביר:** `Clear-Host`
*   **`Get-Date`**: מקבל את התאריך והשעה הנוכחיים.
    *   **תחביר:** `Get-Date`
*    **`Start-Process`**: מפעיל תוכנית או פותח קובץ.
    *   **תחביר:** `Start-Process [שם_תוכנית_או_קובץ] [אפשרויות]`
   *   **דוגמאות:**
        *   `Start-Process notepad.exe`: הפעל את פנקס הרשימות.
        *   `Start-Process myfile.txt`: פתח את הקובץ `myfile.txt` עם תוכנית ברירת המחדל.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - פתח אתר בכרום
*   **`Get-Help`**: מציג עזרה על פקודה.
    *   **תחביר**: `Get-Help [שם_פקודה]`
    *   **דוגמה:** `Get-Help Get-Process`: הצג עזרה על הפקודה `Get-Process`.
*   **`Exit`**: מסיים את הפעלת PowerShell
    *   **תחביר:** `Exit`
*  **`Get-Variable`**: הצג משתנים נוכחיים
    *  **תחביר**: `Get-Variable`
*  **`Get-Alias`**: הצג קיצורי פקודות
    *   **תחביר**: `Get-Alias`
*   **`Set-Alias`**: צור כינוי לפקודה
    *  **תחביר**: `Set-Alias [שם_כינוי] [שם_פקודה]`
    *  **דוגמה**: `Set-Alias gci Get-ChildItem`

**הערות:**

*   לפקודות `PowerShell` (cmdlets) יש בדרך כלל צורה של `פועל-שם_עצם` (לדוגמה, `Get-Process`, `Set-Location`).
*   `PowerShell` אינו תלוי רישיות, כך שאתה יכול לכתוב פקודות כ-`Get-ChildItem` או `get-childitem`.
*   `PowerShell` עובד עם אובייקטים, כך שאתה יכול להשתמש באופרטור `|` כדי להעביר את הפלט של פקודה אחת כקלט לפקודה אחרת (לדוגמה, `Get-Process | Sort-Object -Property CPU`).
*  פקודות רבות תומכות בשימוש בתווים כלליים (*) לעבודה עם מספר קבצים (לדוגמה `Get-ChildItem *.txt`).
*   לביצוע חלק מהפקודות נדרשות הרשאות מנהל.