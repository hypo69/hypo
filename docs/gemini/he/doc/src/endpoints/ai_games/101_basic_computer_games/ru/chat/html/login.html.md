# `login.html`

## סקירה כללית

קובץ זה הוא דף HTML המציג טופס כניסה (אוטוריזציה) למשתמשים. הטופס כולל שדות עבור שם משתמש וסיסמה.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [מבנה HTML](#מבנה-html)
- [CSS](#css)
- [טופס כניסה](#טופס-כניסה)
- [ספריות חיצוניות](#ספריות-חיצוניות)

## מבנה HTML

המבנה הכללי של קובץ ה-HTML כולל את התגים הבאים:

- `<!DOCTYPE html>`: ההצהרה המציינת את סוג המסמך כ-HTML5.
- `<html lang="ru">`: התג השורשי של מסמך ה-HTML, המציין את השפה כרוסית.
- `<head>`: חלק התגיות שכולל את מטא נתונים של המסמך, כגון:
  - `<meta charset="UTF-8">`: הגדרת קידוד תווים ל-UTF-8.
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: הגדרת תצוגה רספונסיבית.
  - `<title>Авторизация</title>`: הגדרת כותרת הדף כ-"Авторизация" (אוטוריזציה).
  - `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">`: קישור לספריה Bootstrap לעיצוב.
  - `<style>`: הגדרות עיצוב CSS.
- `<body>`: חלק התגיות שכולל את תוכן הדף הגלוי.

## CSS

הקובץ כולל הגדרות עיצוב CSS בתוך תגית ה-`<style>`. הגדרות אלו כוללות:

- `body`: הגדרת צבע רקע לאפור בהיר.
- `.login-container`: הגדרת מידות, מיקום, ריפוד, צבע רקע, פינות מעוגלות וצל למיכל הכניסה.

## טופס כניסה

הטופס עצמו נמצא בתוך ה-`<body>` וכולל את התגים הבאים:

- `<div class="container">`: מיכל ראשי ליישור התוכן.
- `<div class="login-container">`: מיכל ייעודי לטופס הכניסה.
- `<h2 class="text-center mb-4">Вход</h2>`: כותרת הטופס, "Вход" (כניסה).
- `<form action="/api/login" method="post">`: הגדרת הטופס, כולל כתובת ה-API שאליה יישלחו הנתונים (`/api/login`) ושיטת השליחה (`post`).
  - `<div class="mb-3">`: מיכל לשם המשתמש:
    - `<label for="username" class="form-label">Имя пользователя</label>`: תווית עבור שדה שם משתמש.
    - `<input type="text" class="form-control" id="username" name="username" required>`: שדה קלט טקסט עבור שם המשתמש, עם מאפיינים כגון סוג, מזהה, שם ודרישה.
  - `<div class="mb-3">`: מיכל לסיסמה:
    - `<label for="password" class="form-label">Пароль</label>`: תווית עבור שדה הסיסמה.
    - `<input type="password" class="form-control" id="password" name="password" required>`: שדה קלט סיסמה, עם מאפיינים כגון סוג, מזהה, שם ודרישה.
  - `<div class="d-grid">`: מיכל לכפתור השליחה:
    - `<button type="submit" class="btn btn-primary">Войти</button>`: כפתור שליחת הטופס.

## ספריות חיצוניות

הקובץ משתמש בספריות חיצוניות:

- [Bootstrap](https://getbootstrap.com/): ספריה לעיצוב ופונקציונליות של דפי אינטרנט, אשר מקושרת דרך CDN (רשת הפצת תוכן).
  - `https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css`: קובץ CSS של Bootstrap.
  - `https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js`: קובץ JavaScript של Bootstrap.

הספריות מספקות רכיבי ממשק משתמש מוכנים מראש ועוזרות ליצור עמוד אינטרנט רספונסיבי ומעוצב.