# Модуль `hypotez/src/ai/tiny_troupe/TinyTroupe/tests/testing_utils.py`

## Обзор

Данный модуль содержит вспомогательные функции для тестирования модулей `tinytroupe`. Он предоставляет инструменты для проверки действий и стимулов, проверки соответствия конфигураций агентов и управления файлами.

## Функции

### `contains_action_type`

**Описание**: Проверяет, содержит ли список действий действие заданного типа.

**Параметры**:
- `actions` (list): Список словарей, представляющих действия. Каждый словарь должен содержать ключ "action" со значением словаря, содержащим ключ "type".
- `action_type` (str): Тип действия, который ищется.

**Возвращает**:
- `bool`: `True`, если действие заданного типа найдено, иначе `False`.


### `contains_action_content`

**Описание**: Проверяет, содержит ли список действий действие с заданным содержанием.

**Параметры**:
- `actions` (list): Список словарей, представляющих действия. Каждый словарь должен содержать ключ "action" со значением словаря, содержащим ключ "content".
- `action_content` (str):  Строка поиска.

**Возвращает**:
- `bool`: `True`, если действие с заданным содержанием найдено (с учетом регистра), иначе `False`.


### `contains_stimulus_type`

**Описание**: Проверяет, содержит ли список стимулов стимул заданного типа.

**Параметры**:
- `stimuli` (list): Список словарей, представляющих стимулы. Каждый словарь должен содержать ключ "type".
- `stimulus_type` (str): Тип стимула, который ищется.

**Возвращает**:
- `bool`: `True`, если стимул заданного типа найден, иначе `False`.


### `contains_stimulus_content`

**Описание**: Проверяет, содержит ли список стимулов стимул с заданным содержанием.

**Параметры**:
- `stimuli` (list): Список словарей, представляющих стимулы. Каждый словарь должен содержать ключ "content".
- `stimulus_content` (str):  Строка поиска.

**Возвращает**:
- `bool`: `True`, если стимул с заданным содержанием найден (с учетом регистра), иначе `False`.


### `terminates_with_action_type`

**Описание**: Проверяет, заканчивается ли список действий действием заданного типа.

**Параметры**:
- `actions` (list): Список словарей, представляющих действия.
- `action_type` (str): Тип действия, который ищется.

**Возвращает**:
- `bool`: `True`, если последний элемент списка действий имеет заданный тип, иначе `False`.


### `proposition_holds`

**Описание**: Проверяет, истинно ли данное утверждение, вызывая LLM.

**Параметры**:
- `proposition` (str): Утверждение для проверки.

**Возвращает**:
- `bool`: `True`, если утверждение истинно, `False` - если ложно.  Возможна ошибка `Exception`, если LLM вернул неожиданный результат.


### `only_alphanumeric`

**Описание**: Возвращает строку, содержащую только буквенно-цифровые символы.

**Параметры**:
- `string` (str): Исходная строка.

**Возвращает**:
- `str`: Строка, содержащая только буквенно-цифровые символы.


### `create_test_system_user_message`

**Описание**: Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.

**Параметры**:
- `user_prompt` (str, optional): Пользовательское сообщение. По умолчанию `None`.
- `system_prompt` (str, optional): Системное сообщение. По умолчанию "You are a helpful AI assistant.".

**Возвращает**:
- `list`: Список сообщений.


### `agents_configs_are_equal`

**Описание**: Проверяет, равны ли конфигурации двух агентов.

**Параметры**:
- `agent1`: Первый агент.
- `agent2`: Второй агент.
- `ignore_name` (bool, optional): Флаг для игнорирования поля `name`. По умолчанию `False`.

**Возвращает**:
- `bool`: `True`, если конфигурации равны, иначе `False`.


### `remove_file_if_exists`

**Описание**: Удаляет файл, если он существует.

**Параметры**:
- `file_path` (str): Путь к файлу.


### `get_relative_to_test_path`

**Описание**: Возвращает путь к тестовому файлу с заданным суффиксом.

**Параметры**:
- `path_suffix` (str): Суффикс пути.

**Возвращает**:
- `str`: Путь к тестовому файлу.


## Фикстуры

### `focus_group_world`

**Описание**: Фикстура, создающая объект `TinyWorld` с набором тестовых `TinyPerson` из `examples`.

**Возвращает**:
- `TinyWorld`: Объект `TinyWorld`.


### `setup`

**Описание**: Фикстура для очищения глобальных данных агентов и сред перед каждым тестом.