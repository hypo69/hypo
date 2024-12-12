# Анализ кода модуля `ogg.js`

**Качество кода**
8
-  Плюсы
    - Код выполняет конвертацию аудио из OGG в MP3.
    - Использует `ffmpeg` для конвертации аудио.
    - Применяет `axios` для загрузки аудиофайлов.
    - Использует промисы для асинхронных операций.
    - Удаляет временный файл OGG после конвертации.
-  Минусы
    - Отсутствуют docstring для классов и методов.
    - Обработка ошибок выводит сообщение в консоль (`console.log`) вместо использования логгера.
    - Некорректное использование типов в Promise (несоответствие типов resolve и reject в `toMp3`).
    - Не используются асинхронные функции в методе `create`, что не соответствует стандарту кода.
    - Не реализована обработка ошибок при записи в поток.

**Рекомендации по улучшению**

1. Добавить docstring для класса `OggConverter` и его методов `toMp3` и `create` в формате reStructuredText.
2. Заменить `console.log` на `logger.error` для логирования ошибок с указанием контекста.
3. Исправить использование типов в Promise в методе `toMp3` для соответствия типам.
4. Использовать async/await для более корректной обработки асинхронных операций в методе `create`.
5. Добавить обработку ошибок при работе с потоком `stream.on('error', ...)` в методе `create`.
6. Использовать `src.utils.jjson` для загрузки файлов, если это необходимо.
7. Добавить импорт для `logger` из `src.logger.logger`.

**Оптимизированный код**

```python
"""
Модуль для конвертации аудиофайлов из OGG в MP3.
=================================================

Этот модуль предоставляет класс :class:`OggConverter`, который используется для конвертации аудиофайлов из формата OGG в формат MP3.
Он использует `ffmpeg` для конвертации и `axios` для загрузки OGG файлов по URL.

Пример использования
--------------------

Пример использования класса `OggConverter`:

.. code-block:: python

    ogg_converter = OggConverter()
    ogg_converter.create('url_to_ogg', 'test_file').then(oggPath => {
         ogg_converter.toMp3(oggPath, 'output_file').then(mp3Path => {
               console.log(`MP3 file: ${mp3Path}`)
           })
    })
"""
import axios from 'axios'
import { createWriteStream } from 'fs'
import { dirname, resolve } from 'path'
import { fileURLToPath } from 'url'
import ffmpeg from 'fluent-ffmpeg'
import installer from '@ffmpeg-installer/ffmpeg'
import { removeFile } from './utils.js'
#  Импорт логгера
from src.logger.logger import logger

const __dirname = dirname(fileURLToPath(import.meta.url))

class OggConverter {
  """
    Класс для конвертации аудиофайлов из OGG в MP3.
    """
  constructor() {
    """
        Инициализирует класс OggConverter, устанавливая путь к ffmpeg.
        """
    ffmpeg.setFfmpegPath(installer.path)
  }

  toMp3(input, output) {
    """
        Конвертирует OGG файл в MP3.

        :param input: Путь к входному OGG файлу.
        :param output: Имя выходного MP3 файла (без расширения).
        :return: Promise, который разрешается с путем к выходному MP3 файлу.
        """
    try {
      #  формирует путь для выходного mp3 файла
      const outputPath = resolve(dirname(input), `${output}.mp3`)
      return new Promise((resolve, reject) => { #  Исправлено использование типов для resolve и reject
          #  Запускает процесс конвертации
        ffmpeg(input)
            .inputOption('-t 30')
            .output(outputPath)
            .on('end', () => {
              #  Удаляет исходный ogg файл после конвертации
              removeFile(input)
              resolve(outputPath)
            })
            .on('error', (err) => {
              # Логирует ошибку при конвертации
              logger.error(`Ошибка при конвертации в mp3: ${err.message}`, err)
              reject(err)
            })
            .run()
      })
    } catch (e) {
      # Логирует ошибку при создании mp3
      logger.error(`Ошибка при создании mp3: ${e.message}`, e)
    }
  }

  async create(url, filename) {
    """
        Создает OGG файл, загружая его по URL.

        :param url: URL для загрузки OGG файла.
        :param filename: Имя сохраняемого OGG файла (без расширения).
        :return: Promise, который разрешается с путем к созданному OGG файлу.
        """
    try {
      # Формирует путь для сохранения ogg файла
      const oggPath = resolve(__dirname, '../voices', `${filename}.ogg`)
      #  Выполняет запрос на загрузку файла
      const response = await axios({
        method: 'get',
        url,
        responseType: 'stream',
      })
      return new Promise((resolve, reject) => {
        # Создает поток для записи файла
        const stream = createWriteStream(oggPath)
        #  Передает данные из потока ответа в поток записи
        response.data.pipe(stream)
        #  Обрабатывает событие завершения записи
        stream.on('finish', () => resolve(oggPath))
         # Обрабатывает ошибку при записи в поток
        stream.on('error', (err) => {
            logger.error(`Ошибка при записи ogg файла: ${err.message}`, err);
            reject(err);
        });
      })
    } catch (e) {
        # Логирует ошибку при создании ogg
      logger.error(`Ошибка при создании ogg: ${e.message}`, e)
    }
  }
}

export const ogg = new OggConverter()
```