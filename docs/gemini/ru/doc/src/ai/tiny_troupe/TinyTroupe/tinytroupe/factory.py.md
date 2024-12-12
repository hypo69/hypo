# Модуль `factory.py`

## Обзор

Модуль `factory.py` содержит классы `TinyFactory` и `TinyPersonFactory`, которые используются для создания и управления агентами (объектами `TinyPerson`) в контексте симуляций. `TinyFactory` является базовым классом для различных фабрик, обеспечивая механизм кэширования и управления фабриками. `TinyPersonFactory` расширяет этот функционал, предоставляя методы для генерации агентов на основе контекста и параметров.

## Оглавление
- [Классы](#Классы)
    - [`TinyFactory`](#TinyFactory)
        - [`__init__`](#__init__)
        - [`__repr__`](#__repr__)
        - [`set_simulation_for_free_factories`](#set_simulation_for_free_factories)
        - [`add_factory`](#add_factory)
        - [`clear_factories`](#clear_factories)
        - [`encode_complete_state`](#encode_complete_state)
        - [`decode_complete_state`](#decode_complete_state)
    - [`TinyPersonFactory`](#TinyPersonFactory)
        - [`__init__`](#__init__-1)
        - [`generate_person_factories`](#generate_person_factories)
        - [`generate_person`](#generate_person)
        - [`_aux_model_call`](#_aux_model_call)
        - [`_setup_agent`](#_setup_agent)

## Классы

### `TinyFactory`

**Описание**: Базовый класс для различных типов фабрик, который обеспечивает кэширование и управление фабриками.

#### `__init__`

**Описание**: Инициализирует экземпляр `TinyFactory`.

**Параметры**:
- `simulation_id` (str, optional): Идентификатор симуляции. По умолчанию `None`.

#### `__repr__`

**Описание**: Возвращает строковое представление объекта `TinyFactory`.

**Возвращает**:
- `str`: Строковое представление объекта `TinyFactory`.

#### `set_simulation_for_free_factories`

**Описание**: Устанавливает симуляцию для фабрик, у которых не установлен `simulation_id`.

**Параметры**:
- `simulation` (object): Объект симуляции.

#### `add_factory`

**Описание**: Добавляет фабрику в список всех фабрик.

**Параметры**:
- `factory` (object): Объект фабрики.

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким именем уже существует.

#### `clear_factories`

**Описание**: Очищает глобальный список всех фабрик.

#### `encode_complete_state`

**Описание**: Кодирует полное состояние фабрики.

**Возвращает**:
- `dict`: Словарь, представляющий состояние фабрики.

#### `decode_complete_state`

**Описание**: Декодирует полное состояние фабрики.

**Параметры**:
- `state` (dict): Словарь с состоянием фабрики.

**Возвращает**:
- `TinyFactory`: Экземпляр `TinyFactory` с восстановленным состоянием.

### `TinyPersonFactory`

**Описание**: Класс для создания фабрики персонажей `TinyPerson`.

#### `__init__`

**Описание**: Инициализирует экземпляр `TinyPersonFactory`.

**Параметры**:
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `simulation_id` (str, optional): Идентификатор симуляции. По умолчанию `None`.

#### `generate_person_factories`

**Описание**: Генерирует список экземпляров `TinyPersonFactory`, используя LLM OpenAI.

**Параметры**:
- `number_of_factories` (int): Количество экземпляров `TinyPersonFactory` для генерации.
- `generic_context_text` (str): Общий контекстный текст, используемый для генерации `TinyPersonFactory`.

**Возвращает**:
- `list`: Список экземпляров `TinyPersonFactory`.

#### `generate_person`

**Описание**: Генерирует экземпляр `TinyPerson`, используя LLM OpenAI.

**Параметры**:
- `agent_particularities` (str, optional): Особенности агента.
- `temperature` (float, optional): Температура, используемая при выборке из LLM. По умолчанию `1.5`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `5`.

**Возвращает**:
- `TinyPerson | None`: Экземпляр `TinyPerson` или `None`, если не удалось сгенерировать агента.

#### `_aux_model_call`

**Описание**: Вспомогательный метод для выполнения вызова модели.

**Параметры**:
- `messages` (list): Список сообщений для отправки в модель.
- `temperature` (float): Температура, используемая при выборке из LLM.

**Возвращает**:
- `dict | None`: Ответ от модели в виде словаря или `None` в случае ошибки.

#### `_setup_agent`

**Описание**: Настраивает агента с необходимыми элементами.

**Параметры**:
- `agent` (object): Объект агента.
- `configuration` (dict): Словарь с конфигурацией для агента.