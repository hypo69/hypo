# Тестирование модуля `test_tinyperson.py`

## Обзор

Этот модуль содержит набор unit-тестов для проверки корректности работы класса `TinyPerson` и его методов. Тесты охватывают различные аспекты поведения агента, включая восприятие стимулов, выполнение действий, управление состоянием и сериализацию.

## Содержание

- [Функции](#Функции)
  - [`test_act`](#test_act)
  - [`test_listen`](#test_listen)
  - [`test_define`](#test_define)
  - [`test_define_several`](#test_define_several)
  - [`test_socialize`](#test_socialize)
  - [`test_see`](#test_see)
  - [`test_think`](#test_think)
  - [`test_internalize_goal`](#test_internalize_goal)
  - [`test_move_to`](#test_move_to)
  - [`test_change_context`](#test_change_context)
  - [`test_save_spec`](#test_save_spec)

## Функции

### `test_act`

**Описание**:
Тестирует способность агента выполнять действия в ответ на запрос.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не выполняет хотя бы одно действие, не содержит действие типа "TALK" или не завершает действия типом "DONE".

### `test_listen`

**Описание**:
Тестирует способность агента воспринимать речевой стимул и обновлять свои текущие сообщения.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не сохраняет сообщение в списке текущих сообщений, не помечает последнее сообщение как "user", не присваивает стимулу тип "CONVERSATION" или не сохраняет правильное содержание стимула.

### `test_define`

**Описание**:
Тестирует способность агента определять значение в своей конфигурации и сбрасывать свой prompt.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не сохраняет новое значение в конфигурации, не изменяет prompt после определения нового значения или не включает новое значение в prompt.

### `test_define_several`

**Описание**:
Тестирует способность агента определять несколько значений в группу конфигурации.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не сохраняет указанные значения в заданной группе конфигурации.

### `test_socialize`

**Описание**:
Тестирует способность агента взаимодействовать с другим агентом.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не выполняет хотя бы одно действие, не содержит действие типа "TALK" или не упоминает имя другого агента в действии "TALK".

### `test_see`

**Описание**:
Тестирует способность агента воспринимать визуальный стимул.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не выполняет хотя бы одно действие, не содержит действие типа "THINK" или не упоминает содержание визуального стимула в действии "THINK".

### `test_think`

**Описание**:
Тестирует способность агента размышлять о чем-либо.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не выполняет хотя бы одно действие, не содержит действие типа "TALK" или не упоминает содержание своих мыслей в действии "TALK".

### `test_internalize_goal`

**Описание**:
Тестирует способность агента усваивать цель.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не выполняет хотя бы одно действие, не содержит действие типа "SEARCH" или не упоминает содержание цели в действии "SEARCH".

### `test_move_to`

**Описание**:
Тестирует способность агента перемещаться в новое местоположение и обновлять свой контекст.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не обновляет свое текущее местоположение или не включает новый контекст в свой текущий контекст.

### `test_change_context`

**Описание**:
Тестирует способность агента изменять свой текущий контекст.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не включает новый контекст в свой текущий контекст.

### `test_save_spec`

**Описание**:
Тестирует способность агента сохранять и загружать свою спецификацию.

**Параметры**:
- `setup` (fixture): Fixture для настройки окружения тестирования.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если агент не сохраняет файл спецификации, загруженный агент имеет другое имя, или загруженный агент имеет другую конфигурацию (за исключением имени) по сравнению с оригинальным агентом.