## Received Code
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

## Improved Code
```javascript
/**
 * Модуль для взаимодействия с OpenAI API.
 * =========================================================================================
 *
 * Этот модуль предоставляет класс :class:`OpenAI`, который инкапсулирует взаимодействие
 * с OpenAI API, включая создание чат-запросов и транскрипцию аудио.
 *
 *
 * .. code-block:: javascript
 *
 *   const openai = new OpenAI(config.get('OPENAI_KEY'))
 *   const response = await openai.chat(messages)
 */
import { Configuration, OpenAIApi } from 'openai'
import config from 'config'
import { createReadStream } from 'fs'
import { logger } from '../../../logger/logger.js'
/**
 * Класс для взаимодействия с OpenAI API.
 *
 * Предоставляет методы для создания чат-запросов и транскрипции аудио.
 */
class OpenAI {
    /**
     * Роли для сообщений в чате.
     *
     * :ASSISTANT: Роль ассистента.
     * :USER: Роль пользователя.
     * :SYSTEM: Системная роль.
     */
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }
    /**
     * Конструктор класса OpenAI.
     *
     * :param apiKey: API ключ для доступа к OpenAI.
     */
    constructor(apiKey) {
        const configuration = new Configuration({
            apiKey,
        })
        # Создание экземпляра OpenAIApi с заданной конфигурацией.
        this.openai = new OpenAIApi(configuration)
    }
    /**
     * Метод для создания чат-запроса.
     *
     * :param messages: Массив сообщений для отправки в чат.
     * :return: Объект сообщения ответа или `undefined` в случае ошибки.
     */
    async chat(messages) {
        try {
            # Отправка запроса на создание чат-завершения.
            const response = await this.openai.createChatCompletion({
                model: 'gpt-3.5-turbo',
                messages,
            })
            # Возврат сообщения ответа.
            return response.data.choices[0].message
        } catch (e) {
            # Логирование ошибки при создании чат-запроса.
            logger.error('Error while gpt chat', e.message)
        }
    }
    /**
     * Метод для транскрипции аудиофайла.
     *
     * :param filepath: Путь к аудиофайлу.
     * :return: Текст транскрипции или `undefined` в случае ошибки.
     */
    async transcription(filepath) {
        try {
            # Отправка запроса на создание транскрипции.
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                'whisper-1'
            )
            # Возврат текста транскрипции.
            return response.data.text
        } catch (e) {
            # Логирование ошибки при транскрипции.
            logger.error('Error while transcription', e.message)
        }
    }
}
# Создание и экспорт экземпляра OpenAI с API ключом из конфигурации.
export const openai = new OpenAI(config.get('OPENAI_KEY'))
```

## Changes Made
- Добавлены docstring для модуля и класса `OpenAI`.
- Добавлены docstring для методов `chat` и `transcription`.
- Добавлены docstring для свойства `roles`.
- Добавлен импорт `logger` из `src/logger/logger.js` для логирования ошибок.
- Заменены `console.log` на `logger.error` для логирования ошибок.
- Добавлены комментарии к коду для пояснения его работы.
- Использован RST формат для комментариев и docstring.
- Убраны лишние комментарии.

## FULL Code
```javascript
/**
 * Модуль для взаимодействия с OpenAI API.
 * =========================================================================================
 *
 * Этот модуль предоставляет класс :class:`OpenAI`, который инкапсулирует взаимодействие
 * с OpenAI API, включая создание чат-запросов и транскрипцию аудио.
 *
 *
 * .. code-block:: javascript
 *
 *   const openai = new OpenAI(config.get('OPENAI_KEY'))
 *   const response = await openai.chat(messages)
 */
import { Configuration, OpenAIApi } from 'openai'
# импорт модуля config для получения настроек
import config from 'config'
# импорт модуля fs для работы с файловой системой
import { createReadStream } from 'fs'
# импорт модуля logger для логирования
import { logger } from '../../../logger/logger.js'
/**
 * Класс для взаимодействия с OpenAI API.
 *
 * Предоставляет методы для создания чат-запросов и транскрипции аудио.
 */
class OpenAI {
    /**
     * Роли для сообщений в чате.
     *
     * :ASSISTANT: Роль ассистента.
     * :USER: Роль пользователя.
     * :SYSTEM: Системная роль.
     */
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }
    /**
     * Конструктор класса OpenAI.
     *
     * :param apiKey: API ключ для доступа к OpenAI.
     */
    constructor(apiKey) {
        const configuration = new Configuration({
            apiKey,
        })
        # Создание экземпляра OpenAIApi с заданной конфигурацией.
        this.openai = new OpenAIApi(configuration)
    }
    /**
     * Метод для создания чат-запроса.
     *
     * :param messages: Массив сообщений для отправки в чат.
     * :return: Объект сообщения ответа или `undefined` в случае ошибки.
     */
    async chat(messages) {
        try {
            # Отправка запроса на создание чат-завершения.
            const response = await this.openai.createChatCompletion({
                model: 'gpt-3.5-turbo',
                messages,
            })
            # Возврат сообщения ответа.
            return response.data.choices[0].message
        } catch (e) {
            # Логирование ошибки при создании чат-запроса.
            logger.error('Error while gpt chat', e.message)
        }
    }
    /**
     * Метод для транскрипции аудиофайла.
     *
     * :param filepath: Путь к аудиофайлу.
     * :return: Текст транскрипции или `undefined` в случае ошибки.
     */
    async transcription(filepath) {
        try {
            # Отправка запроса на создание транскрипции.
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                'whisper-1'
            )
            # Возврат текста транскрипции.
            return response.data.text
        } catch (e) {
            # Логирование ошибки при транскрипции.
            logger.error('Error while transcription', e.message)
        }
    }
}
# Создание и экспорт экземпляра OpenAI с API ключом из конфигурации.
export const openai = new OpenAI(config.get('OPENAI_KEY'))