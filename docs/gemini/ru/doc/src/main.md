# Модуль main

## Обзор

Модуль `main` предоставляет интерактивное меню для запуска предопределенных скриптов. Модуль принимает пользовательский ввод для выбора и выполнения скриптов 1 или 2.

## Функции

### `script1`

**Описание**: Выполняет скрипт 1.

**Возвращает**:  Не применимо.

**Вызывает исключения**:  Не применимо.


### `script2`

**Описание**: Выполняет скрипт 2.

**Возвращает**: Не применимо.

**Вызывает исключения**: Не применимо.


### `show_help`

**Описание**: Выводит справку по доступным командам.

**Возвращает**: Не применимо.

**Вызывает исключения**: Не применимо.


### `interactive_menu`

**Описание**: Интерактивное меню для выбора и запуска скриптов.

**Возвращает**: Не применимо.

**Вызывает исключения**: Не применимо.


### `main`

**Описание**: Основная функция для обработки аргументов командной строки и запуска меню.

**Параметры**:
- `args` (объект `argparse.Namespace`): Результат парсинга аргументов командной строки. Содержит информацию о предоставленных пользователем аргументах.

**Возвращает**:  Не применимо.

**Вызывает исключения**:  Не применимо.


## Использование

Для запуска интерактивного меню, запустите файл `main.py` из командной строки:

```bash
python main.py
```

Для отображения справки используйте флаг `--help`:

```bash
python main.py --help
```

##  Модули

- `src.utils.jjson`: Модуль, содержащий функции для работы с JSON.
- `src.logger`: Модуль, содержащий логирование.


## Замечания

- В текущей реализации скрипты 1 и 2 не содержат никакого функционала.  Необходимо добавить код для их реализации.
-  Документация для функций `j_loads` и `j_loads_ns` из модуля `src.utils.jjson` и других модулей, если таковые имеются, должна быть добавлена отдельно.
- Приведенный пример кода демонстрирует шаблон для разработки интерактивного меню.


## Оглавление

[Обзор](#обзор)
[Функции](#функции)
[Использование](#использование)
[Модули](#модули)
[Замечания](#замечания)