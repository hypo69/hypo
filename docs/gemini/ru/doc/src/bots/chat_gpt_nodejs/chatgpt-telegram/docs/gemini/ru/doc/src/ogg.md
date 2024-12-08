# Модуль `ogg.js`

## Обзор

Этот модуль предоставляет класс `OggConverter` для преобразования аудио файлов OGG в MP3 и загрузки аудио из URL в формате OGG.

## Классы

### `OggConverter`

**Описание**: Класс `OggConverter` предназначен для конвертирования и загрузки аудио файлов OGG.

**Методы**:

#### `toMp3(input, output)`

**Описание**: Конвертирует аудиофайл OGG в MP3.

**Параметры**:

- `input` (str): Путь к файлу OGG для конвертации.
- `output` (str): Имя выходного файла MP3.

**Возвращает**:

- Promise<str | undefined>: Путь к созданному файлу MP3 или `undefined` при ошибке.

**Обрабатывает исключения**:

- `Error`: Возникает при ошибках во время выполнения команды `ffmpeg`.


#### `create(url, filename)`

**Описание**: Загружает аудиофайл OGG из URL.

**Параметры**:

- `url` (str): URL аудиофайла OGG.
- `filename` (str): Имя файла OGG после загрузки.

**Возвращает**:

- Promise<str | undefined>: Путь к загруженному файлу OGG или `undefined` при ошибке.

**Обрабатывает исключения**:

- `Error`: Возникает при ошибках во время загрузки или сохранения файла.

## Модульные переменные

### `ogg`

**Описание**: Экземпляр класса `OggConverter`.

**Тип**: `OggConverter`

```
```
```javascript
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