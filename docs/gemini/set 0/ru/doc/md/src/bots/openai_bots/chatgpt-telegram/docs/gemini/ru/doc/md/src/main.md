# Модуль `main.js`

## Обзор

Этот модуль содержит основную логику бота, обрабатывающую входящие сообщения голосом и текстом.  Он использует библиотеки Telegraf для работы с Telegram, OpenAI для обработки запросов и вспомогательные функции для работы с файлами.

## Импорты

```javascript
import { Telegraf } from 'telegraf'
import { message } from 'telegraf/filters'
import { code } from 'telegraf/format'
import config from 'config'
import { ogg } from './ogg.js'
import { openai } from './openai.js'
import { removeFile } from './utils.js'
```

## Переменные

```javascript
const bot = new Telegraf(config.get('TELEGRAM_TOKEN'))
```

*   `bot`: экземпляр класса `Telegraf`, используемый для взаимодействия с Telegram API.  Инициализируется с токеном бота, полученным из файла `config.js`.


## Обработчики сообщений

### Команда `/start`

```javascript
bot.command('start', async(ctx) : {\n    await ctx.reply(JSON.stringify(ctx.message));\n})
```

**Описание**: Обрабатывает команду `/start`. Возвращает JSON-представление сообщения `ctx.message`.

### Обработчик сообщений голосом (`message('voice')`)

```javascript
bot.on(message('voice'), async (ctx) : {\n    try {\n        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))\n        const link = await ctx.telegram.getFileLink(ctx.message.voice.file_id)\n        const userId = String(ctx.message.from.id)\n        const oggPath = await ogg.create(link.href, userId)\n        const mp3Path = await ogg.toMp3(oggPath, userId)\n        removeFile(oggPath)\n        const text = await openai.transcription(mp3Path)\n        await ctx.reply(code(`запрос: ${text}`))\n        const messages = [{ role: openai.roles.USER, content: text }]\n        const response = await openai.chat(messages)\n        await ctx.reply(response.content)\n    } catch (e) {\n        console.error(`Error while proccessing voice message`, e.message)\n    } \n})
```

**Описание**: Обрабатывает входящие голосовые сообщения. Конвертирует голосовое сообщение в текст, используя OpenAI, и отправляет ответ.

**Обрабатывает исключения**:
- `e`:  Обрабатывает ошибки во время обработки голосового сообщения. Выводит сообщение об ошибке в консоль.


### Обработчик сообщений текстом (`message('text')`)

```javascript
bot.on(message('text'), async (ctx) : {\n    ctx.session ??= INITIAL_SESSION\n    try {\n        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))\n        await processTextToChat(ctx, ctx.message.text)\n    } catch (e) {\n        console.log(`Error while voice message`, e.message)\n    }\n})
```

**Описание**: Обрабатывает входящие текстовые сообщения.  Использует функцию `processTextToChat` для обработки текста и отправки ответа.


**Обрабатывает исключения**:
- `e`:  Обрабатывает ошибки во время обработки текстового сообщения. Выводит сообщение об ошибке в консоль.


## Запуск бота

```javascript
bot.launch()
process.once('SIGINT', () => bot.stop('SIGINT'))
process.once('SIGTERM', () => bot.stop('SIGTERM'))
```

**Описание**: Запускает бота и устанавливает обработчики для завершения работы при получении сигналов `SIGINT` и `SIGTERM`.


```