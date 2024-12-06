# Received Code

```javascript
import { Configuration, OpenAIApi } from 'openai'
import config from 'config'
import { createReadStream } from 'fs'
class OpenAI {
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }
    constructor(apiKey) {
        const configuration = new Configuration({
            apiKey,
        })
        this.openai = new OpenAIApi(configuration)
    }
    async chat(messages) {
        try {
            const response = await this.openai.createChatCompletion({
                model: 'gpt-3.5-turbo',
                messages,
            })
            return response.data.choices[0].message
        } catch (e) {
            console.log('Error while gpt chat', e.message)
        }
    }
    async transcription(filepath) {
        try {
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                'whisper-1'
            )
            return response.data.text
        } catch (e) {
            console.log('Error while transcription', e.message)
        }
    }
}
export const openai = new OpenAI(config.get('OPENAI_KEY'))
```

# Improved Code

```javascript
import { Configuration, OpenAIApi } from 'openai';
import config from 'config';
import { createReadStream } from 'fs';
import { logger } from './src/logger'; // Импорт логирования

class OpenAI {
    """
    Класс для работы с API OpenAI.
    ====================================

    Этот класс предоставляет методы для взаимодействия с API OpenAI,
    включая чат-ботов и транскрипцию аудио.
    """
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }
    """Словарь ролей для сообщений в чате."""

    constructor(apiKey) {
        """
        Инициализация объекта OpenAI.

        :param apiKey: Ключ API OpenAI.
        """
        const configuration = new Configuration({
            apiKey,
        });
        this.openai = new OpenAIApi(configuration);
    }

    async chat(messages) {
        """
        Отправка запроса на чат с моделью GPT-3.5-turbo.

        :param messages: Список сообщений для чата.
        :return: Сообщение от модели.
        """
        try {
            const response = await this.openai.createChatCompletion({
                model: 'gpt-3.5-turbo',
                messages,
            });
            return response.data.choices[0].message;
        } catch (error) {
            logger.error('Ошибка при отправке запроса в чат GPT:', error);
            // Возврат null или другого подходящего значения в случае ошибки
            return null;
        }
    }

    async transcription(filepath) {
        """
        Транскрипция аудио файла с помощью модели Whisper-1.

        :param filepath: Путь к аудио файлу.
        :return: Текст транскрипции.
        """
        try {
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                'whisper-1'
            );
            return response.data.text;
        } catch (error) {
            logger.error('Ошибка при транскрипции аудио:', error);
            return null; // Или другое подходящее значение в случае ошибки
        }
    }
}
export const openai = new OpenAI(config.get('OPENAI_KEY'));
```

# Changes Made

*   Импортирован модуль `logger` из `./src/logger`.
*   Добавлены комментарии RST для класса `OpenAI` и методов `chat` и `transcription` с использованием описаний параметров и возвращаемых значений.
*   В блоках `try...catch` ошибка теперь логгируется с помощью `logger.error`, а не выводится в консоль.
*   Изменены сообщения об ошибках в логировании.
*   Добавлена обработка ошибок внутри функций `chat` и `transcription` (возвращается `null` в случае ошибки).
*   Изменены имена переменных в соответствии с PSR-12 и PEP 8.
*   Добавлено описание `roles`

# FULL Code

```javascript
import { Configuration, OpenAIApi } from 'openai';
import config from 'config';
import { createReadStream } from 'fs';
import { logger } from './src/logger'; // Импорт логирования

class OpenAI {
    """
    Класс для работы с API OpenAI.
    ====================================

    Этот класс предоставляет методы для взаимодействия с API OpenAI,
    включая чат-ботов и транскрипцию аудио.
    """
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }
    """Словарь ролей для сообщений в чате."""

    constructor(apiKey) {
        """
        Инициализация объекта OpenAI.

        :param apiKey: Ключ API OpenAI.
        """
        const configuration = new Configuration({
            apiKey,
        });
        this.openai = new OpenAIApi(configuration);
    }

    async chat(messages) {
        """
        Отправка запроса на чат с моделью GPT-3.5-turbo.

        :param messages: Список сообщений для чата.
        :return: Сообщение от модели.
        """
        try {
            const response = await this.openai.createChatCompletion({
                model: 'gpt-3.5-turbo',
                messages,
            });
            return response.data.choices[0].message;
        } catch (error) {
            logger.error('Ошибка при отправке запроса в чат GPT:', error);
            // Возврат null или другого подходящего значения в случае ошибки
            return null;
        }
    }

    async transcription(filepath) {
        """
        Транскрипция аудио файла с помощью модели Whisper-1.

        :param filepath: Путь к аудио файлу.
        :return: Текст транскрипции.
        """
        try {
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                'whisper-1'
            );
            return response.data.text;
        } catch (error) {
            logger.error('Ошибка при транскрипции аудио:', error);
            return null; // Или другое подходящее значение в случае ошибки
        }
    }
}
export const openai = new OpenAI(config.get('OPENAI_KEY'));