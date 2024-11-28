# Модуль `hypotez/src/endpoints/hypo69/code_assistant/main.py`

## Обзор

Этот модуль реализует командную строку для запуска Code Assistant.  Он позволяет конфигурировать ассистента через файл настроек JSON или аргументы командной строки, обрабатывать файлы в заданных директориях и использовать различные модели.

## Оглавление

- [Функция `parse_args()`](#функция-parse_args)
- [Функция `main()`](#функция-main)


## Функции

### `parse_args()`

**Описание**: Парсит аргументы командной строки для настройки Code Assistant.

**Параметры**:
-  `--settings` (str): Путь к файлу настроек JSON.
- `--role` (str): Роль ассистента (`code_checker`, `code_analyzer`, `doc_writer`, `tests_creator`). По умолчанию `code_checker`.
- `--lang` (str): Язык (`ru`, `en`). По умолчанию `en`.
- `--models` (str, `*args`): Список моделей (`gemini`, `openai`).
- `--start_dirs` (str, `*args`): Список стартовых директорий.

**Возвращает**:
- dict: Словарь с параметрами запуска.


### `main()`

**Описание**: Главный метод для запуска CodeAssistant. Обрабатывает входные данные и передает их в `CodeAssistant`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- Возможные исключения, генерируемые при работе с файлами настроек, созданием `CodeAssistant` или обработкой файлов.


## Использование

Для запуска программы необходимо использовать следующие аргументы командной строки:

**Примеры запуска:**

1. **Запуск с файлом настроек:**
   ```bash
   python main.py --settings settings.json
   ```

2. **Запуск с параметрами командной строки:**
   ```bash
   python main.py --role doc_writer --lang ru --models gemini openai --start_dirs /path/to/dir1 /path/to/dir2
   ```

3. **Запуск с ограничением моделей:**
   ```bash
   python main.py --role code_checker --lang en --models gemini --start_dirs /path/to/dir
   ```

4. **Запуск с определенными настройками и ролью:**
   ```bash
   python main.py --role doc_writer --lang en --models openai
   ```

**Файл настроек (settings.json):**

```json
{
  "role": "doc_writer",
  "lang": "ru",
  "models": ["gemini", "openai"],
  "start_dirs": ["/path/to/dir1", "/path/to/dir2"]
}
```

В файле `settings.json` нужно указать параметры, необходимые для инициализации `CodeAssistant`.  Обратите внимание, что пустые массивы/списки для параметров, таких как `start_dirs`, в JSON могут не работать корректно. Рекомендуется использовать пустые массивы, если вы не хотите задавать начальные директории.

```json
{
  "role": "doc_writer",
  "lang": "ru",
  "models": ["gemini"],
  "start_dirs": [] 
}
```