# Модуль generate_person_factory

## Обзор

Этот модуль предоставляет функционал для генерации контекстов, используемых для создания описаний персонажей.  Модуль позволяет создавать широкий спектр персонажей, задавая общие характеристики и детализируя их в различных контекстах.

## Функции

### `generate_contexts`

**Описание**: Функция генерирует массив контекстов для создания описаний персонажей.

**Параметры**:

- `input_context` (str): Общий контекст для генерации персонажей. Описание ожидаемого типа персонажей.
- `number_of_contexts` (int, optional): Количество генерируемых контекстов. По умолчанию 3.

**Возвращает**:

- list[str]: Список контекстов, каждый из которых предназначен для генерации отдельного персонажа.

**Вызывает исключения**:

- `ValueError`: Если `number_of_contexts` не является положительным целым числом.
- `TypeError`: Если `input_context` не является строкой.