# `src/main.js`

## Обзор

Данный файл содержит основной код для Telegram-бота, который обрабатывает голосовые и текстовые сообщения пользователей, используя OpenAI для транскрипции и генерации ответов.

## Оглавление

- [Импорты](#импорты)
- [Инициализация бота](#инициализация-бота)
- [Обработчик команды `/start`](#обработчик-команды-start)
- [Обработчик голосовых сообщений](#обработчик-голосовых-сообщений)
- [Обработчик текстовых сообщений](#обработчик-текстовых-сообщений)
- [Запуск бота](#запуск-бота)
- [Обработка сигналов завершения](#обработка-сигналов-завершения)

## Импорты

```javascript
import { Telegraf } from 'telegraf';
import { message } from 'telegraf/filters';
import { code } from 'telegraf/format';
import config from 'config';
import { ogg } from './ogg.js';
import { openai } from './openai.js';
import { removeFile } from './utils.js';
```

## Инициализация бота

```javascript
const bot = new Telegraf(config.get('TELEGRAM_TOKEN'));
```

Создается экземпляр бота `Telegraf` с использованием токена, полученного из конфигурации.

## Обработчик команды `/start`

```javascript
bot.command('start', async (ctx) => {
    await ctx.reply(JSON.stringify(ctx.message));
});
```

### `bot.command('start', async (ctx) => { ... })`

**Описание**:
Обрабатывает команду `/start`. Отвечает пользователю JSON представлением объекта сообщения.

**Параметры**:
- `ctx` (Telegraf Context): Объект контекста, предоставляющий доступ к информации о сообщении и боте.

**Возвращает**:
- `Promise<void>`: Promise, который разрешается после отправки ответа.

## Обработчик голосовых сообщений

```javascript
bot.on(message('voice'), async (ctx) => {
    try {
        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'));
        const link = await ctx.telegram.getFileLink(ctx.message.voice.file_id);
        const userId = String(ctx.message.from.id);
        const oggPath = await ogg.create(link.href, userId);
        const mp3Path = await ogg.toMp3(oggPath, userId);
        removeFile(oggPath);
        const text = await openai.transcription(mp3Path);
        await ctx.reply(code(`запрос: ${text}`));
        const messages = [{ role: openai.roles.USER, content: text }];
        const response = await openai.chat(messages);
        await ctx.reply(response.content);
    } catch (ex) {
        console.error(`Error while proccessing voice message`, ex.message);
    }
});
```

### `bot.on(message('voice'), async (ctx) => { ... })`

**Описание**:
Обрабатывает входящие голосовые сообщения. Конвертирует голосовое сообщение в текст и отправляет его в OpenAI API для получения ответа.

**Параметры**:
- `ctx` (Telegraf Context): Объект контекста, предоставляющий доступ к информации о сообщении и боте.

**Возвращает**:
- `Promise<void>`: Promise, который разрешается после обработки сообщения и отправки ответа.

**Вызывает исключения**:
- `Error`: Выводится в консоль при ошибке обработки голосового сообщения.

## Обработчик текстовых сообщений

```javascript
bot.on(message('text'), async (ctx) => {
    ctx.session ??= INITIAL_SESSION;
    try {
        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'));
        await processTextToChat(ctx, ctx.message.text);
    } catch (ex) {
        console.log(`Error while voice message`, ex.message);
    }
});
```

### `bot.on(message('text'), async (ctx) => { ... })`

**Описание**:
Обрабатывает входящие текстовые сообщения. Отправляет текст в OpenAI API для получения ответа.

**Параметры**:
- `ctx` (Telegraf Context): Объект контекста, предоставляющий доступ к информации о сообщении и боте.

**Возвращает**:
- `Promise<void>`: Promise, который разрешается после обработки сообщения и отправки ответа.

**Вызывает исключения**:
- `Error`: Выводится в консоль при ошибке обработки текстового сообщения.

## Запуск бота

```javascript
bot.launch();
```
Запускает бота.

## Обработка сигналов завершения

```javascript
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
```

### `process.once('SIGINT', () => bot.stop('SIGINT'))`

**Описание**:
Останавливает бота при получении сигнала `SIGINT` (обычно при нажатии Ctrl+C).

**Параметры**:
- Нет.

**Возвращает**:
- Нет.

### `process.once('SIGTERM', () => bot.stop('SIGTERM'))`

**Описание**:
Останавливает бота при получении сигнала `SIGTERM` (сигнал завершения процесса).

**Параметры**:
- Нет.

**Возвращает**:
- Нет.