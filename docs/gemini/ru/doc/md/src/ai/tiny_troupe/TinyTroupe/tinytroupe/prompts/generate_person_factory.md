# Модуль generate_person_factory

## Обзор

Этот модуль предоставляет функции для генерации контекстов, используемых для создания описаний персон.  Он принимает общий контекст с параметрами (демографическими, физическими, поведенческими, убеждениями) и генерирует множество более специфичных контекстов, основываясь на нём.

## Функции

### `generate_person_contexts`

**Описание**: Функция генерирует массив контекстов для создания описаний персон.

**Параметры**:

- `broad_context` (str): Общий контекст для генерации персон, например, "Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not".


**Возвращает**:

- `list[str]`: Список контекстов для создания описаний персон. Возвращает `None`, если входные данные невалидны.

**Вызывает исключения**:

- `ValueError`: Если `broad_context` не является строкой или имеет неверный формат.
- `TypeError`: Если `broad_context` не является строкой.