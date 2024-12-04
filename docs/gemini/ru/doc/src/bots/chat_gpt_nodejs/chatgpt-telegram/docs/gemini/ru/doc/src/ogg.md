# Модуль ogg.js

## Обзор

Данный модуль предоставляет класс `OggConverter` для конвертации аудиофайлов в формате OGG в MP3 и загрузки аудио из URL в формате OGG.

## Классы

### `OggConverter`

**Описание**: Класс для конвертации и загрузки аудиофайлов.

**Методы**:

#### `toMp3(input, output)`

**Описание**: Конвертирует аудиофайл в формате OGG в MP3.

**Параметры**:

- `input` (строка): Путь к входному файлу OGG.
- `output` (строка): Имя выходного файла MP3.


**Возвращает**:
- `Promise<string | null>`: Путь к созданному файлу MP3, если конвертация прошла успешно. Если произошла ошибка, возвращает null.


**Обрабатывает исключения**:

- `Error`: Выбрасывается, если произошла ошибка при конвертации файла. Сообщение об ошибке будет выведено в консоль.


#### `create(url, filename)`

**Описание**: Загружает аудиофайл из URL в формате OGG и сохраняет его.

**Параметры**:

- `url` (строка): URL аудиофайла.
- `filename` (строка): Имя файла для сохранения.


**Возвращает**:
- `Promise<string | null>`: Путь к созданному файлу OGG, если загрузка прошла успешно. Если произошла ошибка, возвращает null.


**Обрабатывает исключения**:

- `Error`: Выбрасывается, если произошла ошибка при загрузке файла. Сообщение об ошибке будет выведено в консоль.


##  Использование

```javascript
import { ogg } from './ogg.js';

async function convertAndSave() {
  const inputFilePath = '/path/to/your/input.ogg';
  const outputFileName = 'output';
  const convertedFilePath = await ogg.toMp3(inputFilePath, outputFileName);
  if (convertedFilePath) {
    console.log(`Файл успешно преобразован в ${convertedFilePath}`);
  } else {
    console.error('Ошибка при преобразовании файла.');
  }
}


async function downloadAndSave() {
  const url = 'https://example.com/audio.ogg';
  const filename = 'downloaded_audio';
  const downloadedFilePath = await ogg.create(url, filename);
  if (downloadedFilePath) {
    console.log(`Файл успешно загружен в ${downloadedFilePath}`);
  } else {
    console.error('Ошибка при загрузке файла.');
  }
}

convertAndSave();
downloadAndSave();

```

**Примечание**: Замените `/path/to/your/input.ogg` и `https://example.com/audio.ogg` на действительные пути и URL.  Обратите внимание на использование асинхронных функций (`async/await`) для работы с `Promise`.
```