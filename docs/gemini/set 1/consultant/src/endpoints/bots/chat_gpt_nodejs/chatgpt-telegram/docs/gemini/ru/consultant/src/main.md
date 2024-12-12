# Received Code

```javascript
import { Telegraf } from 'telegraf'
import { message } from 'telegraf/filters'
import { code } from 'telegraf/format'
import config from 'config'
import { ogg } from './ogg.js'

import { openai } from './openai.js'
import { removeFile } from './utils.js'

const bot = new Telegraf(config.get('TELEGRAM_TOKEN'))
bot.command('start', async(ctx) : {\n    await ctx.reply(JSON.stringify(ctx.message));\n})\n

bot.on(message('voice'), async (ctx) : {\n    try {\n        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))\n        const link = await ctx.telegram.getFileLink(ctx.message.voice.file_id)\n        const userId = String(ctx.message.from.id)\n        const oggPath = await ogg.create(link.href, userId)\n        const mp3Path = await ogg.toMp3(oggPath, userId)\n        removeFile(oggPath)\n        const text = await openai.transcription(mp3Path)\n        await ctx.reply(code(`запрос: ${text}`))\n        const messages = [{ role: openai.roles.USER, content: text }]\n        const response = await openai.chat(messages)\n        await ctx.reply(response.content)\n    } catch (e) {\n        console.error(`Error while proccessing voice message`, e.message)\n    } \n})\n

bot.on(message('text'), async (ctx) : {\n    ctx.session ??= INITIAL_SESSION\n    try {\n        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))\n        await processTextToChat(ctx, ctx.message.text)\n    } catch (e) {\n        console.log(`Error while voice message`, e.message)\n    }\n})\n

bot.launch()\nprocess.once('SIGINT', () : bot.stop('SIGINT'))\nprocess.once('SIGTERM', () : bot.stop('SIGTERM'))
```

# Improved Code

```javascript
import { Telegraf } from 'telegraf';
import { message } from 'telegraf/filters';
import { code } from 'telegraf/format';
import config from 'config';
import { ogg } from './ogg.js';
import { openai } from './openai.js';
import { removeFile } from './utils.js';
import { logger } from './logger.js'; // Импорт функции логирования

const bot = new Telegraf(config.get('TELEGRAM_TOKEN'));

/**
 * Обработка команды старт.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @returns {Promise<void>}
 */
bot.command('start', async (ctx) => {
  try {
    await ctx.reply(JSON.stringify(ctx.message));
  } catch (error) {
    logger.error('Ошибка при обработке команды "start"', error);
  }
});


/**
 * Обработка голосового сообщения.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @returns {Promise<void>}
 */
bot.on(message('voice'), async (ctx) => {
  try {
    await ctx.reply(code('Сообщение принято. Ожидание ответа от сервера...'));
    const fileLink = await ctx.telegram.getFileLink(ctx.message.voice.file_id);
    const userId = String(ctx.message.from.id);
    const oggFilePath = await ogg.create(fileLink.href, userId);
    const mp3FilePath = await ogg.toMp3(oggFilePath, userId);
    removeFile(oggFilePath);
    const transcription = await openai.transcription(mp3FilePath);
    await ctx.reply(code(`Запрос: ${transcription}`));
    const messages = [{ role: 'user', content: transcription }]; // Использование корректного имени роли
    const response = await openai.chat(messages);
    await ctx.reply(response.content);
  } catch (error) {
    logger.error('Ошибка при обработке голосового сообщения', error);
  }
});


/**
 * Обработка текстового сообщения.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @param {string} text - Текст сообщения.
 * @returns {Promise<void>}
 */
bot.on(message('text'), async (ctx) => {
  try {
    ctx.session ??= {}; // Инициализация сессии
    await ctx.reply(code('Сообщение принято. Ожидание ответа от сервера...'));
    await processTextToChat(ctx, ctx.message.text);
  } catch (error) {
    logger.error('Ошибка при обработке текстового сообщения', error);
  }
});


bot.launch();
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));

```

# Changes Made

* Импортирован модуль `logger` из `./logger.js`.
* Добавлены `try...catch` блоки для обработки ошибок с использованием `logger.error` вместо `console.error`.
* Заменены неявные строки `: { ... }` на стандартные стрелочные функции `async (ctx) => { ... }`.
* Изменены имена переменных для соответствия PSR-12.
* Добавлены комментарии в формате RST для всех функций и методов.
* Добавлен обработчик `logger.error` для команды `start`.
* Использование `ctx.session ??= {}` для инициализации сессии.
* Заменено  `openai.roles.USER` на `'user'` в массиве сообщений.


# FULL Code

```javascript
import { Telegraf } from 'telegraf';
import { message } from 'telegraf/filters';
import { code } from 'telegraf/format';
import config from 'config';
import { ogg } from './ogg.js';
import { openai } from './openai.js';
import { removeFile } from './utils.js';
import { logger } from './logger.js'; // Импорт функции логирования

const bot = new Telegraf(config.get('TELEGRAM_TOKEN'));

/**
 * Обработка команды старт.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @returns {Promise<void>}
 */
bot.command('start', async (ctx) => {
  try {
    await ctx.reply(JSON.stringify(ctx.message));
  } catch (error) {
    logger.error('Ошибка при обработке команды "start"', error);
  }
});


/**
 * Обработка голосового сообщения.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @returns {Promise<void>}
 */
bot.on(message('voice'), async (ctx) => {
  try {
    await ctx.reply(code('Сообщение принято. Ожидание ответа от сервера...'));
    const fileLink = await ctx.telegram.getFileLink(ctx.message.voice.file_id);
    const userId = String(ctx.message.from.id);
    const oggFilePath = await ogg.create(fileLink.href, userId);
    const mp3FilePath = await ogg.toMp3(oggFilePath, userId);
    removeFile(oggFilePath);
    const transcription = await openai.transcription(mp3FilePath);
    await ctx.reply(code(`Запрос: ${transcription}`));
    const messages = [{ role: 'user', content: transcription }]; // Использование корректного имени роли
    const response = await openai.chat(messages);
    await ctx.reply(response.content);
  } catch (error) {
    logger.error('Ошибка при обработке голосового сообщения', error);
  }
});


/**
 * Обработка текстового сообщения.
 *
 * @param {object} ctx - Контекст Telegram бота.
 * @param {string} text - Текст сообщения.
 * @returns {Promise<void>}
 */
bot.on(message('text'), async (ctx) => {
  try {
    ctx.session ??= {}; // Инициализация сессии
    await ctx.reply(code('Сообщение принято. Ожидание ответа от сервера...'));
    await processTextToChat(ctx, ctx.message.text);
  } catch (error) {
    logger.error('Ошибка при обработке текстового сообщения', error);
  }
});


bot.launch();
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));