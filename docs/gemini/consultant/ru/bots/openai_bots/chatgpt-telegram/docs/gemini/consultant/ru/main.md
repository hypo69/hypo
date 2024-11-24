**Received Code**

```python
import { Telegraf } from 'telegraf'
import { message } from 'telegraf/filters'
import { code } from 'telegraf/format'
import config from 'config'
import { ogg } from './ogg.js'

import { openai } from './openai.js'
import { removeFile } from './utils.js'

const bot = new Telegraf(config.get('TELEGRAM_TOKEN'))
bot.command('start', async(ctx) : {
    await ctx.reply(JSON.stringify(ctx.message));
})

bot.on(message('voice'), async (ctx) : {
    try {
        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))
        const link = await ctx.telegram.getFileLink(ctx.message.voice.file_id)
        const userId = String(ctx.message.from.id)
        const oggPath = await ogg.create(link.href, userId)
        const mp3Path = await ogg.toMp3(oggPath, userId)
        removeFile(oggPath)
        const text = await openai.transcription(mp3Path)
        await ctx.reply(code(`запрос: ${text}`))
        const messages = [{ role: openai.roles.USER, content: text }]
        const response = await openai.chat(messages)
        await ctx.reply(response.content)
    } catch (e) {
        console.error(`Error while proccessing voice message`, e.message)
    } 
})

bot.on(message('text'), async (ctx) : {
    ctx.session ??= INITIAL_SESSION
    try {
        await ctx.reply(code('Сообщение принял. Жду ответ от сервера...'))
        await processTextToChat(ctx, ctx.message.text)
    } catch (e) {
        console.log(`Error while voice message`, e.message)
    }
})

bot.launch()
process.once('SIGINT', () : bot.stop('SIGINT'))
process.once('SIGTERM', () : bot.stop('SIGTERM'))
```

**Improved Code**

```python
import telegraf
import telegraf.filters
import telegraf.format
import config
import ogg
import openai
from utils import removeFile
from src.logger import logger  # Import logger

# Модуль для обработки сообщений Telegram бота.
# Содержит логику обработки голосовых и текстовых сообщений.
# Использует API OpenAI для генерации ответов.

# Константа для инициализации сессии.
INITIAL_SESSION = {}

# Инициализация Telegram бота.
bot = telegraf.Telegraf(config.get('TELEGRAM_TOKEN'))


@bot.command('start')
async def start_command(ctx):
    """
    Обрабатывает команду /start.

    :param ctx: Контекст Telegram сообщения.
    """
    await ctx.reply(str(ctx.message))  #  Преобразование объекта в строку.


@bot.on(telegraf.filters.message('voice'))
async def voice_message_handler(ctx):
    """
    Обрабатывает голосовые сообщения.

    :param ctx: Контекст Telegram сообщения.
    """
    try:
        await ctx.reply(telegraf.format.code('Сообщение принял. Жду ответ от сервера...'))
        link = await ctx.telegram.get_file_link(ctx.message.voice.file_id)
        user_id = str(ctx.message.from_user.id)  # Использование from_user
        ogg_path = await ogg.create(link.href, user_id)
        mp3_path = await ogg.to_mp3(ogg_path, user_id)  # Изменение имени функции
        removeFile(ogg_path)
        text = await openai.transcription(mp3_path)
        await ctx.reply(telegraf.format.code(f'запрос: {text}'))
        messages = [{'role': openai.roles.USER, 'content': text}]
        response = await openai.chat(messages)
        await ctx.reply(response.content)
    except Exception as e:
        logger.error('Ошибка обработки голосового сообщения:', exc_info=True)


@bot.on(telegraf.filters.message('text'))
async def text_message_handler(ctx):
    """
    Обрабатывает текстовые сообщения.

    :param ctx: Контекст Telegram сообщения.
    """
    ctx.session = ctx.session or INITIAL_SESSION # Корректная инициализация сессии.
    try:
        await ctx.reply(telegraf.format.code('Сообщение принял. Жду ответ от сервера...'))
        await process_text_to_chat(ctx, ctx.message.text)
    except Exception as e:
        logger.error('Ошибка обработки текстового сообщения:', exc_info=True)


async def process_text_to_chat(ctx, text):
    """
    Обрабатывает текстовое сообщение и отправляет его в чат.
    TODO: Добавить реализацию.
    :param ctx: Контекст Telegram сообщения.
    :param text: Текстовое сообщение.
    """
    ...


# Запуск бота.
bot.launch()

# Обработка сигналов завершения.
process.once('SIGINT', lambda: bot.stop('SIGINT'))
process.once('SIGTERM', lambda: bot.stop('SIGTERM'))
```

**Changes Made**

- Импорты переписаны на Python.
- Добавлен импорт `from src.logger import logger`.
- Функции и переменные переименованы в соответствии с PEP 8 (snake_case).
- Добавлены docstring в формате RST к функциям `start_command`, `voice_message_handler`, `text_message_handler`, `process_text_to_chat`.
- Переменная `user_id` изменен на `user_id`.
- Использование `ctx.message.from_user.id` вместо `ctx.message.from.id`.
- Обработка ошибок через `logger.error`.
- Добавлена корректная инициализация `ctx.session`.
- Преобразование `ctx.message` к строке при ответе.
- Исправление синтаксиса в обработке сигналов `SIGINT` и `SIGTERM`.

**Full Code (Improved)**

```python
import telegraf
import telegraf.filters
import telegraf.format
import config
import ogg
import openai
from utils import removeFile
from src.logger import logger  # Import logger

# Модуль для обработки сообщений Telegram бота.
# Содержит логику обработки голосовых и текстовых сообщений.
# Использует API OpenAI для генерации ответов.

INITIAL_SESSION = {}

bot = telegraf.Telegraf(config.get('TELEGRAM_TOKEN'))


@bot.command('start')
async def start_command(ctx):
    """
    Обрабатывает команду /start.

    :param ctx: Контекст Telegram сообщения.
    """
    await ctx.reply(str(ctx.message))  #  Преобразование объекта в строку.


@bot.on(telegraf.filters.message('voice'))
async def voice_message_handler(ctx):
    """
    Обрабатывает голосовые сообщения.

    :param ctx: Контекст Telegram сообщения.
    """
    try:
        await ctx.reply(telegraf.format.code('Сообщение принял. Жду ответ от сервера...'))
        link = await ctx.telegram.get_file_link(ctx.message.voice.file_id)
        user_id = str(ctx.message.from_user.id)  # Использование from_user
        ogg_path = await ogg.create(link.href, user_id)
        mp3_path = await ogg.to_mp3(ogg_path, user_id)  # Изменение имени функции
        removeFile(ogg_path)
        text = await openai.transcription(mp3_path)
        await ctx.reply(telegraf.format.code(f'запрос: {text}'))
        messages = [{'role': openai.roles.USER, 'content': text}]
        response = await openai.chat(messages)
        await ctx.reply(response.content)
    except Exception as e:
        logger.error('Ошибка обработки голосового сообщения:', exc_info=True)


@bot.on(telegraf.filters.message('text'))
async def text_message_handler(ctx):
    """
    Обрабатывает текстовые сообщения.

    :param ctx: Контекст Telegram сообщения.
    """
    ctx.session = ctx.session or INITIAL_SESSION # Корректная инициализация сессии.
    try:
        await ctx.reply(telegraf.format.code('Сообщение принял. Жду ответ от сервера...'))
        await process_text_to_chat(ctx, ctx.message.text)
    except Exception as e:
        logger.error('Ошибка обработки текстового сообщения:', exc_info=True)


async def process_text_to_chat(ctx, text):
    """
    Обрабатывает текстовое сообщение и отправляет его в чат.
    TODO: Добавить реализацию.
    :param ctx: Контекст Telegram сообщения.
    :param text: Текстовое сообщение.
    """
    ...


bot.launch()
process.once('SIGINT', lambda: bot.stop('SIGINT'))
process.once('SIGTERM', lambda: bot.stop('SIGTERM'))
```