# Модуль utils.js

## Обзор

Данный модуль содержит функцию для удаления файла.

## Функции

### `removeFile`

**Описание**: Функция асинхронно удаляет файл по заданному пути.

**Параметры**:

- `path` (string): Путь к файлу, который необходимо удалить.

**Возвращает**:

- `undefined`: Функция не возвращает никакого значения.

**Обрабатывает исключения**:

- `Error`:  В случае возникновения ошибки при удалении файла, выводит сообщение об ошибке в консоль и не прерывает выполнение программы.