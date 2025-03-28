# Инструкции для бота

## Обзор

Этот документ описывает команды, доступные для взаимодействия с ботом.

## Содержание

- [Команды](#команды)
  - [`!hi`](#hi)
  - [`!train`](#train)
  - [`!test`](#test)
  - [`!archive`](#archive)
  - [`!select_dataset`](#select_dataset)
  - [`!instruction`](#instruction)

## Команды

### `!hi`

**Описание**:
Выводит приветствие пользователю.

### `!train`

**Описание**:
Обучает модель с использованием предоставленных данных.

**Параметры**:
- `data` (str): Данные для обучения, путь к файлу.
- `data_dir` (str): Путь к каталогу с данными для обучения.
- `positive` (str):  Метка положительного класса.
- `attachment` (str):  Файл вложения с данными для обучения.

### `!test`

**Описание**:
Тестирует модель, используя предоставленные JSON данные для тестирования.

**Параметры**:
- `test_data` (str): JSON данные для тестирования.

### `!archive`

**Описание**:
Архивирует файлы в указанной директории.

**Параметры**:
- `directory` (str): Путь к директории для архивирования.

### `!select_dataset`

**Описание**:
Выбирает набор данных для обучения из указанной директории.

**Параметры**:
- `path_to_dir_positive` (str): Путь к директории с положительными примерами.
- `positive` (str): Метка положительного класса.

### `!instruction`

**Описание**:
Выводит это сообщение с инструкциями.