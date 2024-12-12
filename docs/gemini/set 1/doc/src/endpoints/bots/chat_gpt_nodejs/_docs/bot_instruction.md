# ИНСТРУКЦИЯ ДЛЯ БОТА CHAT GPT NODEJS

## Обзор

Данный документ содержит описание команд, доступных для бота Chat GPT NodeJS.

## Команды

### `!hi`

**Описание**: Приветствует пользователя.

**Использование**: `!hi`

**Пример**: `!hi`


### `!train <data> <data_dir> <positive> <attachment>`

**Описание**: Обучает модель с предоставленными данными. Используйте `data` для файла, `data_dir` для директории или `attachment` для вложения файла.

**Использование**: `!train <data> <data_dir> <positive> <attachment>`

**Параметры**:

- `data` (строка): Путь к файлу с данными для обучения.
- `data_dir` (строка): Путь к директории с данными для обучения.
- `positive` (строка): Путь к директории с положительными примерами для обучения (используется в conjunction с `data_dir`).
- `attachment` (строка): Путь к приложению для обучения (используется в conjunction с `data_dir`).


**Пример**: `!train data.txt data_dir/ positive_examples.txt`


### `!test <test_data>`

**Описание**: Тестирует модель с предоставленными JSON тестовыми данными.

**Использование**: `!test <test_data>`

**Параметры**:

- `test_data` (строка): Путь к файлу с JSON тестовыми данными.


**Пример**: `!test test_data.json`


### `!archive <directory>`

**Описание**: Архивирует файлы в указанной директории.

**Использование**: `!archive <directory>`

**Параметры**:

- `directory` (строка): Путь к директории, которую нужно заархивировать.


**Пример**: `!archive my_directory`


### `!select_dataset <path_to_dir_positive> <positive>`

**Описание**: Выбирает набор данных для обучения из указанной директории.

**Использование**: `!select_dataset <path_to_dir_positive> <positive>`

**Параметры**:

- `path_to_dir_positive` (строка): Путь к директории с положительными примерами.
- `positive` (строка): Путь к файлу с положительными примерами (используется в conjunction с `path_to_dir_positive`).


**Пример**: `!select_dataset positive_examples_dir positive_examples.txt`


### `!instruction`

**Описание**: Отображает это сообщение с инструкцией.

**Использование**: `!instruction`

**Пример**: `!instruction`