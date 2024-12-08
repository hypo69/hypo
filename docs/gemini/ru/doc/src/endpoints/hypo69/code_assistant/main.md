# Модуль `hypotez/src/endpoints/hypo69/code_assistant/main.py`

## Обзор

Модуль `main.py` представляет собой командную строку (CLI) приложение для запуска CodeAssistant. Он позволяет настроить CodeAssistant с помощью параметров из командной строки или файла настроек JSON.  Приложение обрабатывает файлы в заданных директориях, используя указанные модели (Gemini или OpenAI) и роль.

## Оглавление

- [Функция `parse_args()`](#функция-parse_args)
- [Функция `main()`](#функция-main)


## Функции

### `parse_args()`

**Описание**: Функция парсит аргументы командной строки и возвращает словарь с настройками.

**Параметры**:
-  `--settings` (str): Путь к файлу настроек JSON.
-  `--role` (str):  Выбор роли ассистента (`code_checker`, `code_analyzer`, `doc_writer`, `tests_creator`).
-  `--lang` (str): Выбор языка (`ru`, `en`). По умолчанию `en`.
-  `--models` (str, nargs='+'): Список моделей для использования (`gemini`, `openai`).
-  `--start_dirs` (str, nargs='+'): Список стартовых директорий.


**Возвращает**:
- dict: Словарь с параметрами запуска.


### `main()`

**Описание**: Главная функция для запуска `CodeAssistant` с настроенными параметрами.


**Параметры**:
Нет явных параметров. Использует аргументы из функции `parse_args()`.

**Возвращает**:
- Нет возвращаемого значения.


**Обрабатывает исключения**:
- Нет явно описанных исключений. Возможные исключения из `CodeAssistant` будут обрабатываться внутри объекта.


## Использование

Для запуска приложения необходимо указать параметры либо в командной строке, либо в файле настроек JSON.

**Примеры командной строки:**

1. Запуск с готовыми настройками:
   ```bash
   python main.py --settings settings.json
   ```

2. Запуск с указанием роли, языка, моделей и директорий:
   ```bash
   python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
   ```

3. Запуск с указанием роли, языка и модели:
   ```bash
   python main.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
   ```

4. Запуск с указанием роли, языка и модели:
   ```bash
   python main.py --role doc_writer --lang en --models openai
   ```


**Файл настроек (settings.json):**


```json
{
  "role": "doc_writer",
  "lang": "ru",
  "model": ["gemini", "openai"],
  "start_dirs": ["/path/to/dir1", "/path/to/dir2"]
}
```


```
```
```