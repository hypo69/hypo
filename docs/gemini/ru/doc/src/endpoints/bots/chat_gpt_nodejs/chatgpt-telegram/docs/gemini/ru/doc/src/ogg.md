# Модуль `ogg.js`

## Обзор

Модуль `ogg.js` предоставляет класс `OggConverter` для конвертации аудио файлов в формате OGG в MP3 и загрузки аудио из URL в формат OGG.

## Класс `OggConverter`

### Описание

Класс `OggConverter` отвечает за конвертацию аудио файлов и загрузку аудио из URL в формат OGG.

### Методы

#### `toMp3(input, output)`

**Описание**: Конвертирует аудио файл в формате OGG в MP3.

**Параметры**:

- `input` (строка): Путь к входному файлу OGG.
- `output` (строка): Имя выходного файла MP3 (без расширения).

**Возвращает**:

- `Promise<string>`: Путь к созданному файлу MP3 или `null` в случае ошибки.

**Обрабатывает исключения**:

- `Error`: Возникает при ошибках в процессе конвертации. Сообщение об ошибке выводится в консоль.


#### `create(url, filename)`

**Описание**: Загружает аудио из URL в формат OGG.

**Параметры**:

- `url` (строка): URL аудио файла.
- `filename` (строка): Имя выходного файла OGG (без расширения).


**Возвращает**:

- `Promise<string>`: Путь к созданному файлу OGG или `null` в случае ошибки.

**Обрабатывает исключения**:

- `Error`: Возникает при ошибках во время загрузки или сохранения файла. Сообщение об ошибке выводится в консоль.


## Использование

```javascript
import { ogg } from './ogg.js';

async function convertAndSave() {
  try {
    const oggFilePath = await ogg.create('https://example.com/audio.ogg', 'audio');
    if (oggFilePath) {
      const mp3FilePath = await ogg.toMp3(oggFilePath, 'audio-converted');
      if (mp3FilePath) {
          console.log(`Файл успешно преобразован в MP3: ${mp3FilePath}`);
      } else {
          console.error("Ошибка преобразования в MP3");
      }
    } else {
        console.error("Ошибка загрузки OGG");
    }
  } catch (error) {
    console.error('Ошибка:', error);
  }
}

convertAndSave();
```

**Примечание**: Для корректной работы модуля необходимо установить зависимости `axios`, `fs`, `path`, `url`, `fluent-ffmpeg`, `@ffmpeg-installer/ffmpeg`, `./utils.js`.  Также убедитесь, что FFmpeg установлен и доступен в системе.  `utils.js` должен содержать функцию `removeFile(input)`.