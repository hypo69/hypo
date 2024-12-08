# Received Code

```javascript
import axios from 'axios'
import { createWriteStream } from 'fs'
import { dirname, resolve } from 'path'
import { fileURLToPath } from 'url'
import ffmpeg from 'fluent-ffmpeg'
import installer from '@ffmpeg-installer/ffmpeg'
import { removeFile } from './utils.js'

const __dirname = dirname(fileURLToPath(import.meta.url))
// ====
class OggConverter {
  constructor() {
    ffmpeg.setFfmpegPath(installer.path)
  }
    toMp3(input, output) {
        try {
            const outputPath = resolve(dirname(input), `${output}.mp3`)
            return new Promise((resolve, reject) : {
                ffmpeg(input)
                    .inputOption('-t 30')
                    .output(outputPath)
                    .on('end', () : {
                        removeFile(input)
                        resolve(outputPath)
                    })
                    .on('error', (err) : reject(err.message))
                    .run()
            })
        } catch (e) {
            console.log('Error while creating mp3', e.message)
        }
    } // ====
    async create(url, filename) {
        try {
            const oggPath = resolve(__dirname, '../voices', `${filename}.ogg`)
            const response = await axios({
                method: 'get',
                url,
                responseType: 'stream',
            })
            return new Promise((resolve) : {
                const stream = createWriteStream(oggPath)
                response.data.pipe(stream)
                stream.on('finish', () : resolve(oggPath))
            })
        } catch (e) {
            console.log('Error while creating ogg', e.message)
        }
    }
}
export const ogg = new OggConverter()
```

# Improved Code

```javascript
import axios from 'axios';
import { createWriteStream } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';
import ffmpeg from 'fluent-ffmpeg';
import installer from '@ffmpeg-installer/ffmpeg';
import { removeFile } from './utils.js';
import { logger } from './logger.js'; // Импорт logger

// Модуль для конвертации аудио в формат OGG и MP3.
/**
 * Класс для конвертации аудио файлов.
 */
class OggConverter {
    /**
     * Конструктор класса OggConverter.
     * Устанавливает путь к FFmpeg.
     */
    constructor() {
        ffmpeg.setFfmpegPath(installer.path);
    }

    /**
     * Конвертирует аудио файл в MP3.
     *
     * :param input: Путь к входному аудио файлу.
     * :param output: Имя выходного файла (без расширения).
     * :return: Путь к выходному файлу (MP3).
     * :raises Exception: Если произошла ошибка при конвертации.
     */
    toMp3(input, output) {
        const outputPath = resolve(dirname(input), `${output}.mp3`);
        return new Promise((resolve, reject) => {
            ffmpeg(input)
                .inputOption('-t 30')
                .output(outputPath)
                .on('end', () => {
                    removeFile(input);
                    resolve(outputPath);
                })
                .on('error', (err) => {
                    logger.error('Ошибка при конвертации в MP3:', err.message);
                    reject(err.message);
                })
                .run();
        });
    }

    /**
     * Загружает аудио файл из URL в формате OGG.
     *
     * :param url: URL аудио файла.
     * :param filename: Имя файла (без расширения).
     * :return: Путь к загруженному файлу (OGG).
     * :raises Exception: Если произошла ошибка при загрузке.
     */
    async create(url, filename) {
        const oggPath = resolve(__dirname, '../voices', `${filename}.ogg`);
        try {
            const response = await axios({
                method: 'get',
                url,
                responseType: 'stream',
            });

            return new Promise((resolve, reject) => {
                const stream = createWriteStream(oggPath);
                response.data.pipe(stream);
                stream.on('finish', () => {
                    resolve(oggPath);
                });
                stream.on('error', (err) => {
                    logger.error('Ошибка при сохранении OGG:', err);
                    reject(err);
                });
            });

        } catch (error) {
            logger.error('Ошибка при загрузке OGG:', error.message);
            throw error; // Перебрасываем ошибку наружу
        }
    }
}

export const ogg = new OggConverter();
```

# Changes Made

*   Импортирован модуль `logger` из `./logger.js`.
*   Добавлены комментарии RST к классу `OggConverter` и его методам.
*   Используется `logger.error` для логирования ошибок, вместо `console.log`.
*   Обработка ошибок в методах `toMp3` и `create` переписана с использованием `logger.error` и `reject`.
*   Исключение `Exception` переброшено наружу в методе `create`.
*   Исправлены стили комментариев, добавив теги `:param`, `:return`, `:raises` в комментарии RST.
*   Добавлена подробная документация к методам в формате RST.
*   Исправлены ошибки в синтаксисе `Promise`.

# FULL Code

```javascript
import axios from 'axios';
import { createWriteStream } from 'fs';
import { dirname, resolve } from 'path';
import { fileURLToPath } from 'url';
import ffmpeg from 'fluent-ffmpeg';
import installer from '@ffmpeg-installer/ffmpeg';
import { removeFile } from './utils.js';
import { logger } from './logger.js'; // Импорт logger

// Модуль для конвертации аудио в формат OGG и MP3.
/**
 * Класс для конвертации аудио файлов.
 */
class OggConverter {
    /**
     * Конструктор класса OggConverter.
     * Устанавливает путь к FFmpeg.
     */
    constructor() {
        ffmpeg.setFfmpegPath(installer.path);
    }

    /**
     * Конвертирует аудио файл в MP3.
     *
     * :param input: Путь к входному аудио файлу.
     * :param output: Имя выходного файла (без расширения).
     * :return: Путь к выходному файлу (MP3).
     * :raises Exception: Если произошла ошибка при конвертации.
     */
    toMp3(input, output) {
        const outputPath = resolve(dirname(input), `${output}.mp3`);
        return new Promise((resolve, reject) => {
            ffmpeg(input)
                .inputOption('-t 30')
                .output(outputPath)
                .on('end', () => {
                    removeFile(input);
                    resolve(outputPath);
                })
                .on('error', (err) => {
                    logger.error('Ошибка при конвертации в MP3:', err.message);
                    reject(err.message);
                })
                .run();
        });
    }

    /**
     * Загружает аудио файл из URL в формате OGG.
     *
     * :param url: URL аудио файла.
     * :param filename: Имя файла (без расширения).
     * :return: Путь к загруженному файлу (OGG).
     * :raises Exception: Если произошла ошибка при загрузке.
     */
    async create(url, filename) {
        const oggPath = resolve(__dirname, '../voices', `${filename}.ogg`);
        try {
            const response = await axios({
                method: 'get',
                url,
                responseType: 'stream',
            });

            return new Promise((resolve, reject) => {
                const stream = createWriteStream(oggPath);
                response.data.pipe(stream);
                stream.on('finish', () => {
                    resolve(oggPath);
                });
                stream.on('error', (err) => {
                    logger.error('Ошибка при сохранении OGG:', err);
                    reject(err);
                });
            });

        } catch (error) {
            logger.error('Ошибка при загрузке OGG:', error.message);
            throw error; // Перебрасываем ошибку наружу
        }
    }
}

export const ogg = new OggConverter();
```