# Gemini Chatbot

## סקירה כללית

קובץ HTML זה יוצר ממשק צ'אט בסיסי עם Gemini Chatbot. הוא תומך בריבוי שפות, שליחת הודעות, קבלת תגובות ושמירה על היסטוריית הצ'אט.

## תוכן עניינים

- [סקירה כללית](#סקירה-כללית)
- [אלמנטים HTML](#אלמנטים-html)
- [סקריפטים](#סקריפטים)
  - [פונקציות](#פונקציות)
    - [`sendMessage`](#sendmessage)
    - [`addMessage`](#addmessage)
    - [`setLocale`](#setlocale)
    - [`updateText`](#updatetext)
    - [`loadRules`](#loadrules)

## אלמנטים HTML

- `<!DOCTYPE html>`: הכרזה שמסמנת את סוג המסמך כ-HTML5.
- `<html lang="ru">`: האלמנט השורשי של הדף, המציין שהשפה היא רוסית.
- `<head>`: מכיל מטא נתונים, קישורים לסגנונות CSS וקובץ ג'אווהסקריפט.
  - `<meta charset="UTF-8">`: מגדיר את קידוד התווים UTF-8.
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: מגדיר את הגדרות ה-viewport עבור תגובה.
  - `<title data-i18n="title">Gemini Chatbot</title>`: כותרת הדף, מותאמת לשפה באמצעות `data-i18n`.
  - `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">`: קישור לספרייית Bootstrap CSS.
  - `<style>`: סגנונות CSS מותאמים אישית עבור ממשק הצ'אט.
- `<body>`: מכיל את התוכן הגלוי של הדף.
  - `<div class="container mt-3">`: עוטף את כל התוכן עם מיכל Bootstrap.
  - `<div class="d-flex justify-content-between align-items-center mb-3">`: מכיל כפתורי שפה ורשימה נפתחת של חוקים.
  - `<div class="chat-container">`: מכיל את ממשק הצ'אט.
    - `<h2 class="text-center mb-4" data-i18n="title">Gemini Chatbot</h2>`: כותרת הצ'אט, מותאמת לשפה באמצעות `data-i18n`.
    - `<div class="chat-window" id="chat-window"></div>`: חלון הצ'אט להצגת ההודעות.
    - `<div class="input-group">`: מכיל את שדה הקלט וכפתור השליחה.
      - `<input type="text" class="form-control" id="message-input" data-i18n="placeholder" placeholder="Введите сообщение...">`: שדה קלט להודעה, עם מציין מיקום מותאם לשפה.
      - `<button class="btn btn-primary" id="send-button" data-i18n="send">Отправить</button>`: כפתור לשליחת הודעה, מותאם לשפה.
  - `<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>`: קישור לספריית jQuery.
  - `<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>`: קישור לספריית Bootstrap JS.
  - `<script>`: מכיל את סקריפט ג'אווהסקריפט עבור פונקציונליות הצ'אט.

## סקריפטים

### פונקציות

#### `sendMessage`

**תיאור**: שולח הודעת משתמש לשרת ומציג את התגובה בצ'אט.

**פרמטרים**:
- אין

**Returns**:
- אין

**Raises**:
- `Error`: אם יש שגיאה בשליחת ההודעה או קבלת התגובה מהשרת.

```javascript
async function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const sendButton = document.getElementById('send-button');
  const message = messageInput.value.trim();

  if (!message) return;

  addMessage('user', message);
  messageInput.value = '';
  sendButton.disabled = true;
  sendButton.textContent = 'Отправка...'; 

  try {
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error('Ошибка при отправке сообщения');
    }

    const data = await response.json();
    addMessage('bot', data.response);
  } catch (ex) {
    console.error('Ошибка:', ex);
    addMessage('bot', 'Произошла ошибка при отправке сообщения. Пожалуйста, попробуйте еще раз.'); 
  } finally {
    sendButton.disabled = false;
    sendButton.textContent = 'Отправить'; 
  }
}
```

#### `addMessage`

**תיאור**: מוסיף הודעה לצ'אט.

**פרמטרים**:
- `sender` (str): סוג השולח - 'user' או 'bot'.
- `text` (str): תוכן ההודעה.

**Returns**:
- אין

**Raises**:
- אין

```javascript
function addMessage(sender, text) {
  const chatWindow = document.getElementById('chat-window');
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');

  const time = new Date().toLocaleTimeString();
  messageElement.innerHTML = `<strong>${sender === 'user' ? 'Вы' : 'Бот'}</strong> (${time}): ${text}`;

  chatWindow.appendChild(messageElement);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}
```

#### `setLocale`

**תיאור**: טוען קובץ לוקליזציה ומעדכן את הטקסט בדף.

**פרמטרים**:
- `lang` (str): קוד השפה.

**Returns**:
- אין

**Raises**:
- `Error`: אם טעינת קובץ הלוקליזציה נכשלה.

```javascript
async function setLocale(lang) {
  currentLocale = lang;
  try {
    const response = await fetch(`/locales/${lang}.json`);
    if (!response.ok) {
      throw new Error(`Failed to load locale file for ${lang}`);
    }
    const localeData = await response.json();
    updateText(localeData);
  } catch (ex) {
    console.error("Error loading locale:", ex);
  }
}
```

#### `updateText`

**תיאור**: מעדכן את כל רכיבי הטקסט עם נתוני לוקליזציה.

**פרמטרים**:
- `localeData` (object): נתוני לוקליזציה.

**Returns**:
- אין

**Raises**:
- אין

```javascript
function updateText(localeData) {
  document.querySelectorAll('[data-i18n]').forEach(element => {
    const key = element.getAttribute('data-i18n');
    if (key && localeData[key]) {
      if (key === "placeholder") element.placeholder = localeData[key];
      else element.textContent = localeData[key];
    }
  });
  const chatWindow = document.getElementById('chat-window');
  const userMessages = chatWindow.querySelectorAll('.user-message strong');
  userMessages.forEach(element => {
    element.textContent = localeData.user || "You";
  });
  const botMessages = chatWindow.querySelectorAll('.bot-message strong');
  botMessages.forEach(element => {
    element.textContent = localeData.bot || "Bot";
  });
}
```

#### `loadRules`

**תיאור**: טוען את רשימת החוקים מהשרת ומציג אותם ברשימה נפתחת.

**פרמטרים**:
- אין

**Returns**:
- אין

**Raises**:
- `Error`: אם טעינת רשימת החוקים נכשלה.

```javascript
async function loadRules() {
  try {
    const response = await fetch('/api/rules');
    if (!response.ok) {
      throw new Error('Failed to load rules');
    }
    const rules = await response.json();
    const rulesList = document.getElementById('rules-list');
    rules.forEach(rule => {
      const ruleItem = document.createElement('li');
      const link = document.createElement('a');
      link.classList.add("dropdown-item")
      link.href = "#"; // Optional - set up link to view rule
      link.textContent = rule.name;
      //  link.onclick = () => {
      //     console.log("rule link clicked", rule)
      //  }
      ruleItem.appendChild(link);
      rulesList.appendChild(ruleItem);
    });
  } catch (ex) {
    console.error("Error loading rules:", ex);
    const rulesList = document.getElementById('rules-list');
    rulesList.innerHTML = `<li><a class="dropdown-item">Error loading rules</a></li>`
  }
}