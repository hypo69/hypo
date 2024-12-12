# Модуль конвертации OGG в MP3

## Обзор

Данный модуль `ogg.js` предоставляет функциональность для конвертации аудиофайлов формата OGG в MP3. Он использует библиотеки `axios` для загрузки OGG файлов, `fluent-ffmpeg` для конвертации форматов и `node:fs` для работы с файловой системой.

## Содержание

- [Классы](#классы)
  - [`OggConverter`](#oggconverter)
- [Функции](#функции)
  - [`ogg`](#ogg)

## Классы

### `OggConverter`

**Описание**: Класс, предоставляющий методы для конвертации OGG в MP3 и загрузки OGG файлов.

**Конструктор**:

-   `constructor()`: Инициализирует `ffmpeg` с путем к исполняемому файлу.

**Методы**:

#### `toMp3(input, output)`

**Описание**: Конвертирует OGG файл в MP3.
**Параметры**:
- `input` (string): Путь к входному OGG файлу.
- `output` (string): Имя выходного MP3 файла (без расширения).

**Возвращает**:
- `Promise<string>`: Promise, разрешающийся с путем к созданному MP3 файлу.

**Вызывает исключения**:
- `Error`: В случае ошибки при конвертации или обработки файла.

**Пример использования**:

```javascript
const converter = new OggConverter();
converter.toMp3('/path/to/input.ogg', 'output_name')
  .then(outputPath => console.log('MP3 файл создан:', outputPath))
  .catch(error => console.error('Ошибка при конвертации:', error));
```

#### `create(url, filename)`

**Описание**: Загружает OGG файл по URL и сохраняет его локально.

**Параметры**:
- `url` (string): URL OGG файла для загрузки.
- `filename` (string): Имя файла для сохранения (без расширения).

**Возвращает**:
- `Promise<string>`: Promise, разрешающийся с путем к сохраненному OGG файлу.

**Вызывает исключения**:
- `Error`: В случае ошибки при загрузке или сохранении файла.

**Пример использования**:

```javascript
const converter = new OggConverter();
converter.create('https://example.com/audio.ogg', 'my_audio')
  .then(oggPath => console.log('OGG файл сохранен:', oggPath))
  .catch(error => console.error('Ошибка при загрузке:', error));
```

## Функции

### `ogg`

**Описание**: Экземпляр класса `OggConverter`, который можно использовать для вызова методов конвертации.

**Пример использования**:

```javascript
import { ogg } from './ogg.js';

ogg.create('https://example.com/audio.ogg', 'my_audio')
  .then(oggPath => ogg.toMp3(oggPath, 'my_audio_mp3'))
  .then(mp3Path => console.log('MP3 файл создан:', mp3Path))
  .catch(error => console.error('Ошибка:', error));
```