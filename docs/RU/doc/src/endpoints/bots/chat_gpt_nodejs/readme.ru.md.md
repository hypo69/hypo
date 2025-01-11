# Реализация ChatGPT бота средствами Node.js

## Обзор

Данный документ содержит информацию о реализации бота ChatGPT с использованием Node.js, описанную в статье на Habr: [https://habr.com/ru/companies/selectel/articles/731692/](https://habr.com/ru/companies/selectel/articles/731692/).

## Оглавление

1. [Обзор](#обзор)
2. [Основные концепции](#основные-концепции)
3. [Реализация](#реализация)
4. [Использование](#использование)

## Основные концепции

Статья описывает процесс создания телеграм-бота, способного взаимодействовать с ChatGPT API. Основные концепции включают:

*   **Node.js:** Используется как среда выполнения для создания сервера.
*   **Telegram Bot API:**  Позволяет боту взаимодействовать с пользователями через Telegram.
*   **OpenAI API:** Предоставляет доступ к моделям GPT, включая ChatGPT.
*   **Библиотеки Node.js:** Используются для обработки HTTP-запросов, взаимодействия с Telegram API и OpenAI API.
*   **Управление асинхронными операциями:**  `async/await` используется для эффективной обработки асинхронных запросов к API.

## Реализация

### Подключение необходимых библиотек и переменных окружения
```javascript
require('dotenv').config();
const TelegramBot = require('node-telegram-bot-api');
const { Configuration, OpenAIApi } = require("openai");

const telegramToken = process.env.TELEGRAM_TOKEN;
const openAIApiKey = process.env.OPENAI_API_KEY;
```
-  **Описание:** Загрузка необходимых библиотек и переменных окружения для работы бота.
- **Параметры:**
    - `TELEGRAM_TOKEN` (string): Токен Telegram бота, необходимый для взаимодействия с Telegram API.
    - `OPENAI_API_KEY` (string): API ключ для доступа к OpenAI.

### Инициализация Telegram бота и OpenAI API
```javascript
const bot = new TelegramBot(telegramToken, { polling: true });

const configuration = new Configuration({
    apiKey: openAIApiKey,
});
const openai = new OpenAIApi(configuration);
```
-  **Описание:** Создание экземпляров `TelegramBot` и `OpenAIApi` для работы с соответствующими API.

### Обработчик сообщений
```javascript
bot.on('message', async (msg) => {
  const chatId = msg.chat.id;
  const messageText = msg.text;
  if (messageText === '/start') {
      bot.sendMessage(chatId, 'Привет! Я бот ChatGPT. Задавай свои вопросы.');
      return;
  }
  try {
      const completion = await openai.createChatCompletion({
          model: "gpt-3.5-turbo",
          messages: [{ role: "user", content: messageText }],
      });
      const reply = completion.data.choices[0].message.content;
      bot.sendMessage(chatId, reply);
  } catch (ex) {
      console.error("Произошла ошибка при обращении к OpenAI API:", ex);
      bot.sendMessage(chatId, "Извините, произошла ошибка при обработке запроса.");
  }
});
```
-  **Описание:** Обработчик событий `message` от Telegram.
    -  Получает текст сообщения от пользователя.
    -  Отправляет запрос к OpenAI API для генерации ответа.
    -  Отправляет полученный ответ пользователю.
- **Параметры:**
    - `msg` (object): Объект сообщения от Telegram API. Содержит информацию о чате и тексте сообщения.
    - `chatId` (number): Идентификатор чата, из которого поступило сообщение.
    - `messageText` (string): Текст сообщения пользователя.
    - `completion` (object): Ответ от OpenAI API.
    - `reply` (string): Сгенерированный ответ от ChatGPT.
-   **Исключения:**
    - Возникает при ошибке обращения к OpenAI API.
    -  Отправляет сообщение об ошибке пользователю.

## Использование

1.  **Настройка переменных окружения**:
    -   Создайте файл `.env` в корневом каталоге проекта.
    -   Добавьте в него строки вида:
        ```
        TELEGRAM_TOKEN=your_telegram_bot_token
        OPENAI_API_KEY=your_openai_api_key
        ```
        Замените `your_telegram_bot_token` и `your_openai_api_key` на соответствующие значения.
2.  **Установка зависимостей**:
    ```bash
    npm install node-telegram-bot-api openai dotenv
    ```
3.  **Запуск бота**:
    ```bash
    node your_bot_file.js
    ```
4. **Взаимодействие**:
   - Отправьте боту команду `/start`, чтобы начать диалог.
   - Задавайте боту вопросы, и он будет отвечать с помощью ChatGPT.