# Инструкции для бота

## Обзор

Этот документ описывает набор команд, которые бот понимает и может выполнять. Каждая команда начинается с восклицательного знака (`!`).

## Содержание

- [Обзор](#обзор)
- [Команды](#команды)
  - [`!hi`](#hi)
  - [`!train`](#train)
  - [`!test`](#test)
  - [`!archive`](#archive)
  - [`!select_dataset`](#select_dataset)
  - [`!instruction`](#instruction)

## Команды

### `!hi`

**Описание**: Приветствует пользователя.

### `!train`

**Описание**: Обучает модель, используя предоставленные данные.

**Параметры**:
- `data` (string): Путь к файлу с данными.
- `data_dir` (string): Путь к директории с данными.
- `positive` (string): Метка для положительного класса.
- `attachment` (string): Путь к файлу, полученному как вложение.

**Примеры**:
- `!train data.txt my_data_dir positive_label attachment.txt`
- `!train data.txt my_data_dir positive_label`
- `!train my_data_dir positive_label`
- `!train attachment.txt`

### `!test`

**Описание**: Тестирует модель, используя предоставленные JSON-данные.

**Параметры**:
- `test_data` (string): Путь к файлу с JSON-данными для тестирования.

**Пример**:
- `!test test_data.json`

### `!archive`

**Описание**: Архивирует файлы в указанной директории.

**Параметры**:
- `directory` (string): Путь к директории для архивирования.

**Пример**:
- `!archive my_directory`

### `!select_dataset`

**Описание**: Выбирает набор данных для обучения из указанной директории.

**Параметры**:
- `path_to_dir_positive` (string): Путь к директории с положительными данными.
- `positive` (string): Метка для положительного класса.

**Пример**:
- `!select_dataset path/to/positive positive_label`

### `!instruction`

**Описание**: Выводит данное сообщение с инструкциями.