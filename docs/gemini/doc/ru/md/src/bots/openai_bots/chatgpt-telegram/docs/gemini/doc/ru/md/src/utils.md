# Модуль utils.js

## Обзор

Данный модуль содержит функцию для удаления файла.

## Функции

### `removeFile`

**Описание**: Асинхронная функция для удаления файла по заданному пути.

**Параметры**:

- `path` (string): Путь к файлу, который необходимо удалить.

**Возвращает**:

- `undefined`: Функция не возвращает значения.

**Обрабатывает исключения**:

- `e` (Error): В случае ошибки при удалении файла выводит сообщение об ошибке в консоль.


```javascript
import { unlink } from 'fs/promises'
export async function removeFile(path) {
    try {
        await unlink(path)
    } catch (e) {
        console.log('Error while removing file', e.message)
    }
}
```