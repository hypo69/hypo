# Модуль utils.js

## Обзор

Этот модуль предоставляет функцию для удаления файла.

## Функции

### `removeFile`

**Описание**: Функция асинхронно удаляет файл по заданному пути.

**Параметры**:

- `path` (string): Путь к файлу, который необходимо удалить.

**Возвращает**:

- `void`: Функция не возвращает значение.

**Обрабатывает исключения**:

- `Error`: В случае ошибки при удалении файла, выводится сообщение об ошибке в консоль.


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