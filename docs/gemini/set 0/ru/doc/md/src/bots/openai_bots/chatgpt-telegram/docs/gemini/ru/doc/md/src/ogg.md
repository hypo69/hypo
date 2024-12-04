# Модуль `ogg.js`

## Обзор

Этот модуль предоставляет класс `OggConverter` для конвертации аудиофайлов в формате OGG в MP3 и загрузки аудио с URL в формате OGG.

## Классы

### `OggConverter`

**Описание**: Класс для конвертации аудиофайлов в формате OGG в MP3 и загрузки аудио с URL в формате OGG.

**Методы**

#### `toMp3(input, output)`

**Описание**: Конвертирует аудиофайл в формате OGG в MP3.

**Параметры**:

- `input` (str): Путь к файлу OGG.
- `output` (str): Имя выходного файла MP3 (без расширения).

**Возвращает**:

- Promise<str | null>: Promise, который разрешается путем возврата пути к созданному файлу MP3 или `null` в случае ошибки.


**Вызывает исключения**:

- Возможны ошибки при обработке файла ffmpeg, а также ошибки при работе с файловой системой.


#### `create(url, filename)`

**Описание**: Загружает аудиофайл в формате OGG с указанного URL и сохраняет его с заданным именем.

**Параметры**:

- `url` (str): URL аудиофайла.
- `filename` (str): Имя файла OGG (без расширения).

**Возвращает**:

- Promise<string | null>: Promise, который разрешается путем возврата пути к созданному файлу OGG или `null` в случае ошибки.


**Вызывает исключения**:

- Возможны ошибки при работе с сетью (например, проблемы с подключением к серверу), а также ошибки при работе с файловой системой.


## Функции

(Нет функций в этом модуле)


## Использование

```javascript
import { ogg } from './ogg.js';

// Пример конвертации OGG в MP3
async function convertOggToMp3() {
  try {
    const outputPath = await ogg.toMp3('/path/to/input.ogg', 'output');
    console.log('Файл MP3 сохранен по пути:', outputPath);
  } catch (error) {
    console.error('Ошибка при конвертации:', error);
  }
}

// Пример загрузки файла с URL
async function downloadFromUrl() {
  try {
    const oggPath = await ogg.create('https://example.com/audio.ogg', 'downloaded_audio');
    console.log('Файл OGG загружен по пути:', oggPath);
  } catch (error) {
    console.error('Ошибка при загрузке:', error);
  }
}


convertOggToMp3();
downloadFromUrl();
```

**Примечание**: Замените `/path/to/input.ogg` и `https://example.com/audio.ogg` на соответствующие значения.  Также убедитесь, что у вас установлен и настроен `ffmpeg`.