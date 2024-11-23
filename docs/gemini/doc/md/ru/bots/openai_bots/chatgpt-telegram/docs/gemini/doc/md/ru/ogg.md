```markdown
# Модуль OggConverter

## Обзор

Этот модуль предоставляет класс `OggConverter` для конвертации аудио файлов в формате OGG в MP3 и загрузки аудио файлов из URL.

## Оглавление

* [Классы](#классы)
    * [OggConverter](#oggconverter)
        * [toMp3](#tomp3)
        * [create](#create)

## Классы

### `OggConverter`

**Описание**: Класс для конвертации аудио файлов OGG в MP3 и загрузки аудио файлов из URL.

**Методы**:

### `toMp3`

**Описание**: Конвертирует файл OGG в MP3.

**Параметры**:

* `input` (str): Путь к файлу OGG для конвертации.
* `output` (str): Имя файла MP3 (без расширения).

**Возвращает**:
* `str | Promise<str>`: Путь к созданному файлу MP3. Возвращает промис, который разрешается с путем к созданному файлу MP3. Возвращает null если произошла ошибка во время преобразования.

**Вызывает исключения**:
* `Error`: Возникает при любой ошибке во время процесса конвертации (например, проблема с FFmpeg, некорректный входной файл).


### `create`

**Описание**: Загружает аудио файл из URL и сохраняет его в формате OGG.

**Параметры**:

* `url` (str): URL аудио файла.
* `filename` (str): Имя файла OGG (без расширения).

**Возвращает**:
* `str | Promise<str>`: Путь к созданному файлу OGG. Возвращает промис, который разрешается с путем к созданному файлу OGG. Возвращает null если произошла ошибка во время загрузки.

**Вызывает исключения**:
* `Error`: Возникает при ошибке запроса к URL (например, ошибка сети, некорректный URL).

```python
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
      return new Promise((resolve, reject) => {
        ffmpeg(input)
          .inputOption('-t 30')
          .output(outputPath)
          .on('end', () => {
            removeFile(input)
            resolve(outputPath)
          })
          .on('error', (err) => reject(err.message))
          .run()
      })
    } catch (e) {
      console.log('Error while creating mp3', e.message)
      return null; // Возвращаем null в случае ошибки
    }
  }
  async create(url, filename) {
    try {
      const oggPath = resolve(__dirname, '../voices', `${filename}.ogg`)
      const response = await axios({
        method: 'get',
        url,
        responseType: 'stream',
      })
      return new Promise((resolve) => {
        const stream = createWriteStream(oggPath)
        response.data.pipe(stream)
        stream.on('finish', () => resolve(oggPath))
      })
    } catch (e) {
      console.log('Error while creating ogg', e.message)
      return null; // Возвращаем null в случае ошибки
    }
  }
}
export const ogg = new OggConverter()
```
