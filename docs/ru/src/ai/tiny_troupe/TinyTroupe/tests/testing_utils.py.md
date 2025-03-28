# Модуль `testing_utils`

## Обзор

Модуль `testing_utils` содержит набор утилитных функций и фикстур, предназначенных для облегчения тестирования кода в проекте `TinyTroupe`. Он включает функции для проверки действий, стимулов, предложений, а также утилиты для работы с файлами и фикстуры для тестовой среды.

## Содержание

- [Функции](#Функции)
    - [`contains_action_type`](#contains_action_type)
    - [`contains_action_content`](#contains_action_content)
    - [`contains_stimulus_type`](#contains_stimulus_type)
    - [`contains_stimulus_content`](#contains_stimulus_content)
    - [`terminates_with_action_type`](#terminates_with_action_type)
    - [`proposition_holds`](#proposition_holds)
    - [`only_alphanumeric`](#only_alphanumeric)
    - [`create_test_system_user_message`](#create_test_system_user_message)
    - [`agents_configs_are_equal`](#agents_configs_are_equal)
    - [`remove_file_if_exists`](#remove_file_if_exists)
    - [`get_relative_to_test_path`](#get_relative_to_test_path)
- [Фикстуры](#Фикстуры)
    - [`focus_group_world`](#focus_group_world)
    - [`setup`](#setup)

## Функции

### `contains_action_type`

**Описание**:
Проверяет, содержит ли данный список действий действие заданного типа.

**Параметры**:
- `actions` (list): Список действий для проверки.
- `action_type` (str): Тип действия, который нужно найти.

**Возвращает**:
- `bool`: `True`, если в списке есть действие заданного типа, иначе `False`.

### `contains_action_content`

**Описание**:
Проверяет, содержит ли данный список действий действие с заданным содержимым.

**Параметры**:
- `actions` (list): Список действий для проверки.
- `action_content` (str): Содержимое действия, которое нужно найти.

**Возвращает**:
- `bool`: `True`, если в списке есть действие с заданным содержимым, иначе `False`.

### `contains_stimulus_type`

**Описание**:
Проверяет, содержит ли данный список стимулов стимул заданного типа.

**Параметры**:
- `stimuli` (list): Список стимулов для проверки.
- `stimulus_type` (str): Тип стимула, который нужно найти.

**Возвращает**:
- `bool`: `True`, если в списке есть стимул заданного типа, иначе `False`.

### `contains_stimulus_content`

**Описание**:
Проверяет, содержит ли данный список стимулов стимул с заданным содержимым.

**Параметры**:
- `stimuli` (list): Список стимулов для проверки.
- `stimulus_content` (str): Содержимое стимула, которое нужно найти.

**Возвращает**:
- `bool`: `True`, если в списке есть стимул с заданным содержимым, иначе `False`.

### `terminates_with_action_type`

**Описание**:
Проверяет, завершается ли данный список действий действием заданного типа.

**Параметры**:
- `actions` (list): Список действий для проверки.
- `action_type` (str): Тип действия, которым должен заканчиваться список.

**Возвращает**:
- `bool`: `True`, если список заканчивается действием заданного типа, иначе `False`.

### `proposition_holds`

**Описание**:
Проверяет, является ли данное утверждение истинным, используя вызов LLM.

**Параметры**:
- `proposition` (str): Утверждение, которое нужно проверить.

**Возвращает**:
- `bool`: `True`, если утверждение истинно, иначе `False`.

**Вызывает исключения**:
- `Exception`: Если LLM возвращает неожиданный результат.

### `only_alphanumeric`

**Описание**:
Возвращает строку, содержащую только буквенно-цифровые символы.

**Параметры**:
- `string` (str): Исходная строка.

**Возвращает**:
- `str`: Строка, содержащая только буквенно-цифровые символы.

### `create_test_system_user_message`

**Описание**:
Создает список сообщений, содержащий одно системное сообщение и одно пользовательское сообщение.

**Параметры**:
- `user_prompt` (str): Пользовательское сообщение.
- `system_prompt` (str, optional): Системное сообщение. По умолчанию `"You are a helpful AI assistant."`

**Возвращает**:
- `list`: Список сообщений.

### `agents_configs_are_equal`

**Описание**:
Проверяет, совпадают ли конфигурации двух агентов.

**Параметры**:
- `agent1` (TinyPerson): Первый агент для сравнения.
- `agent2` (TinyPerson): Второй агент для сравнения.
- `ignore_name` (bool, optional): Игнорировать ли имя агента при сравнении. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если конфигурации агентов совпадают, иначе `False`.

### `remove_file_if_exists`

**Описание**:
Удаляет файл по заданному пути, если он существует.

**Параметры**:
- `file_path` (str): Путь к файлу, который нужно удалить.

### `get_relative_to_test_path`

**Описание**:
Возвращает путь к тестовому файлу с заданным суффиксом.

**Параметры**:
- `path_suffix` (str): Суффикс пути.

**Возвращает**:
- `str`: Полный путь к тестовому файлу.

## Фикстуры

### `focus_group_world`

**Описание**:
Фикстура, создающая тестовую среду `TinyWorld` с несколькими агентами для фокус-группы.

**Возвращает**:
- `TinyWorld`: Экземпляр тестовой среды `TinyWorld`.

### `setup`

**Описание**:
Фикстура, очищающая агентов и окружения перед каждым тестом.

**Возвращает**:
- None: Фикстура ничего не возвращает, но выполняет очистку.