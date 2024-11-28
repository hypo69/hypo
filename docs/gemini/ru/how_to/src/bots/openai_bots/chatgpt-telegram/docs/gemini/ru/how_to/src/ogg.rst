Как использовать класс OggConverter для преобразования и загрузки аудио
=======================================================================

Описание
-------------------------
Класс `OggConverter` предоставляет методы для загрузки аудиофайлов в формате OGG из URL и преобразования их в MP3.  Он использует библиотеки `axios`, `fluent-ffmpeg`, `fs` и `path` для работы с сетью, файлами и выполнением команд ffmpeg.  Метод `create` загружает аудио в формате OGG, а `toMp3` преобразует OGG в MP3.  Методы используют асинхронные операции и обработку ошибок.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей:** Код импортирует необходимые модули, включая `axios` для запросов к URL, `fs` для работы с файлами, `path` для работы с путями, `ffmpeg` для преобразования файлов, `installer` для установки ffmpeg, и `removeFile` для удаления файлов.
2. **Инициализация класса `OggConverter`:** Создается экземпляр класса `OggConverter`, который настраивает путь к ffmpeg с помощью `ffmpeg.setFfmpegPath(installer.path)`.
3. **Загрузка аудио (метод `create`)**:
    a.  Определяется путь к файлу OGG, используя `resolve(__dirname, '../voices', `${filename}.ogg`)`.
    b.  Производится запрос к указанному URL с использованием `axios` и получение данных в виде потока (`responseType: 'stream'`).
    c.  Данные из запроса `response.data` передаются в `createWriteStream(oggPath)` для записи в файл OGG.
    d.  Метод `stream.on('finish', ...)` вызывается, когда запись файла завершена, и возвращает путь к сохранённому файлу OGG.
    e.  Обработка ошибок при загрузке.
4. **Преобразование в MP3 (метод `toMp3`)**:
    a.  Определяется путь к выходному файлу MP3 (`outputPath`).
    b.  Используется `ffmpeg` для преобразования входного файла `input` в `outputPath` с ограничением длительности в 30 секунд (`-t 30`).
    c.  Обработчик `'end'` вызывается, когда преобразование завершено.  В этом обработчике удаляется исходный файл OGG с помощью `removeFile(input)` и возвращается путь к выходному файлу MP3.
    d.  Обработчик `'error'` обрабатывает ошибки при преобразовании.
    e.  Обработка ошибок при преобразовании.

Пример использования
-------------------------
.. code-block:: javascript
    
    import { ogg } from './ogg.js';
    import { resolve } from 'path';

    const audioUrl = 'https://example.com/audio.ogg';
    const outputFileName = 'output';
    const inputFile = resolve(__dirname, '../voices/test.ogg');

    async function main() {
        try {
          const outputPath = await ogg.create(audioUrl, outputFileName);
          const mp3Path = await ogg.toMp3(outputPath, outputFileName);
          console.log(`MP3 файл создан по пути: ${mp3Path}`);
        } catch (error) {
          console.error('Ошибка:', error);
        }
      }
    
    main();