# Модуль `main`

## Обзор

Этот модуль предоставляет интерактивное меню для запуска предопределенных скриптов.
Он принимает ввод пользователя для выбора и выполнения скриптов 1 или 2.

## Оглавление
1. [Обзор](#обзор)
2. [Функции](#функции)
    - [`script1`](#script1)
    - [`script2`](#script2)
    - [`show_help`](#show_help)
    - [`interactive_menu`](#interactive_menu)
    - [`main`](#main)

## Функции

### `script1`

**Описание**: Выполняет скрипт 1.

### `script2`

**Описание**: Выполняет скрипт 2.

### `show_help`

**Описание**: Выводит справочную информацию по доступным командам.

### `interactive_menu`

**Описание**: Интерактивное меню для выбора и запуска скриптов.

### `main`

**Описание**: Основная функция для обработки аргументов командной строки и запуска меню.

```
python
def main():
    """Main function for handling command-line arguments and starting the menu."""
    parser = argparse.ArgumentParser(description="Interactive menu for running scripts.")
    parser.add_argument(
        "--help",
        action="store_true",
        help="Show available options and help information",
    )
    args = parser.parse_args()

    if args.help:
        show_help()
    else:
        interactive_menu()
```
**Параметры**:
 - `args`: Namespace - Аргументы командной строки.

**Возвращает**:
 - `None`: Функция ничего не возвращает.

**Вызывает исключения**:
 - `ArgumentParser.error`: Возникает, если аргументы командной строки неверны.
```