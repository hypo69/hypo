# Анализ кода модуля `openai.js`

**Качество кода**
7
-  Плюсы
    - Код использует классы и методы, что является хорошей практикой для организации кода.
    - Использование `try-catch` блоков для обработки ошибок.
    - Код следует основным принципам JavaScript.
-  Минусы
    - Отсутствует описание модуля, классов и функций.
    - Отсутствует обработка ошибок с использованием `logger`.
    - Не используется импорт logger, как в инструкции.
    - Отсутствуют комментарии в коде для пояснения логики.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, т.к. код на JavaScript, а не Python.

**Рекомендации по улучшению**

1. **Добавить описание модуля**:
   - В начале файла добавить описание модуля.

2. **Добавить комментарии**:
   - Добавить комментарии к функциям и методам.
   - Добавить комментарии, описывающие логику внутри функций.

3. **Использовать `logger`**:
   - Заменить `console.log` на использование `logger` для логирования ошибок.
   - Добавить импорт `logger` из `src/logger`.

4. **Улучшить обработку ошибок**:
   - Использовать `logger.error` для записи ошибок.
   - Вернуть ошибку или `null` в случае возникновения ошибки.

5. **Добавить документацию**:
    - Документировать класс `OpenAI` и его методы с использованием JSDoc.

6. **Использовать константы для моделей**:
   - Определить константы для используемых моделей, чтобы избежать магических строк.

**Оптимизированный код**

```javascript
/**
 * Модуль для взаимодействия с OpenAI API.
 * =========================================================================================
 *
 * Этот модуль содержит класс `OpenAI`, который используется для взаимодействия с OpenAI API,
 * включая создание чат-запросов и транскрипцию аудио.
 *
 * Пример использования
 * --------------------
 *
 * Пример использования класса `OpenAI`:
 *
 * ```javascript
 * const openai = new OpenAI('your-api-key');
 * const response = await openai.chat([{ role: 'user', content: 'Hello' }]);
 * console.log(response);
 * ```
 */
import { Configuration, OpenAIApi } from 'openai'
import config from 'config'
import { createReadStream } from 'fs'
import { logger } from '../../../src/logger' // импорт logger

const GPT_MODEL = 'gpt-3.5-turbo' // Определение константы для модели GPT
const WHISPER_MODEL = 'whisper-1' // Определение константы для модели Whisper

/**
 * Класс для взаимодействия с OpenAI API.
 * @class
 */
class OpenAI {
    /**
     * @type {{ASSISTANT: string, USER: string, SYSTEM: string}}
     * @property {string} ASSISTANT - роль ассистента
     * @property {string} USER - роль пользователя
     * @property {string} SYSTEM - роль системы
     */
    roles = {
        ASSISTANT: 'assistant',
        USER: 'user',
        SYSTEM: 'system',
    }

    /**
     * Конструктор класса OpenAI.
     * @param {string} apiKey - API ключ OpenAI.
     * @constructor
     */
    constructor(apiKey) {
        const configuration = new Configuration({
            apiKey,
        })
        this.openai = new OpenAIApi(configuration)
    }

    /**
     * Отправляет запрос в чат OpenAI.
     * @async
     * @param {Array<{role: string, content: string}>} messages - Массив сообщений для чата.
     * @returns {Promise<string|null>} - Ответ от OpenAI или null в случае ошибки.
     */
    async chat(messages) {
        try {
            // Отправка запроса в чат OpenAI
            const response = await this.openai.createChatCompletion({
                model: GPT_MODEL, // Использование константы для модели
                messages,
            })
            // Возвращает сообщение ответа
            return response.data.choices[0].message
        } catch (e) {
            // Логирование ошибки
            logger.error('Error while gpt chat', e.message)
            return null
        }
    }

    /**
     * Транскрибирует аудиофайл с использованием OpenAI Whisper.
     * @async
     * @param {string} filepath - Путь к аудиофайлу.
     * @returns {Promise<string|null>} - Текст транскрипции или null в случае ошибки.
     */
    async transcription(filepath) {
        try {
            // Отправка запроса на транскрипцию
            const response = await this.openai.createTranscription(
                createReadStream(filepath),
                WHISPER_MODEL // Использование константы для модели
            )
            // Возвращает текст транскрипции
            return response.data.text
        } catch (e) {
             // Логирование ошибки
            logger.error('Error while transcription', e.message)
            return null
        }
    }
}
// Экспорт экземпляра класса OpenAI
export const openai = new OpenAI(config.get('OPENAI_KEY'))
```