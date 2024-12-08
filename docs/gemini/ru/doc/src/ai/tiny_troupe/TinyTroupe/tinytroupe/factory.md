# Модуль tinytroupe.factory

## Обзор

Этот модуль предоставляет классы для создания и управления объектами `TinyPerson` и другими типами агентов.  Он включает базовый класс `TinyFactory` и специализированный класс `TinyPersonFactory`, предназначенный для генерации `TinyPerson` с помощью OpenAI LLM.  Модуль реализует механизмы кэширования для повышения производительности и обеспечивает возможность транзакционного управления объектами.

## Классы

### `TinyFactory`

**Описание**: Базовый класс для различных типов фабрик. Он важен для расширяемости системы, особенно при кэшировании транзакций.

**Атрибуты**:

- `all_factories`: Словарь, хранящий все созданные фабрики (имя -> фабрика).

**Методы**:

- `__init__(self, simulation_id: str = None) -> None`: Инициализирует экземпляр `TinyFactory`.
    - **Параметры**:
        - `simulation_id` (str, необязательно): ID симуляции. По умолчанию `None`.
    - **Возвращает**: `None`
- `__repr__(self) -> str`: Возвращает строковое представление объекта.
- `set_simulation_for_free_factories(simulation)`: Устанавливает симуляцию для свободных фабрик, если она не задана.
    - **Параметры**:
        - `simulation`: Объект симуляции.
- `add_factory(factory)`: Добавляет фабрику в список всех фабрик. Имена фабрик должны быть уникальными.
    - **Параметры**:
        - `factory`: Экземпляр `TinyFactory`.
    - **Возвращает**: `None`
    - **Исключения**:
        - `ValueError`: Если фабрика с таким именем уже существует.
- `clear_factories()`: Очищает глобальный список всех фабрик.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние фабрики. Подклассы должны переопределять этот метод, если содержат несериализуемые элементы.
- `decode_complete_state(self, state: dict)`: Декодирует полное состояние фабрики. Подклассы должны переопределять этот метод, если содержат несериализуемые элементы.


### `TinyPersonFactory`

**Описание**: Фабрика для создания объектов `TinyPerson`.

**Атрибуты**:

- `person_prompt_template_path`: Путь к шаблону запроса для генерации `TinyPerson`.
- `context_text`: Текст контекста для генерации.
- `generated_minibios`: Список сгенерированных minibios `TinyPerson`.
- `generated_names`: Список сгенерированных имён `TinyPerson`.


**Методы**:

- `__init__(self, context_text, simulation_id: str = None)`: Инициализирует экземпляр `TinyPersonFactory`.
    - **Параметры**:
        - `context_text` (str): Текст контекста.
        - `simulation_id` (str, необязательно): ID симуляции. По умолчанию `None`.
- `generate_person_factories(number_of_factories, generic_context_text)`: Генерирует список `TinyPersonFactory` используя OpenAI LLM.
    - **Параметры**:
        - `number_of_factories` (int): Количество фабрик.
        - `generic_context_text` (str): Текст общего контекста.
    - **Возвращает**: Список `TinyPersonFactory` или `None` при ошибке.
- `generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attempts: int = 5)`: Генерирует объект `TinyPerson` используя OpenAI LLM.
    - **Параметры**:
        - `agent_particularities` (str, необязательно): Особенности агента.
        - `temperature` (float, необязательно): Температура для выборки от LLM.
        - `attempts` (int, необязательно): Количество попыток генерации.
    - **Возвращает**: `TinyPerson` или `None` при ошибке.
    - **Исключения**:
        - `Exception`: Общие исключения при генерации.
- `_aux_model_call(self, messages, temperature)`: Вспомогательный метод вызова модели. Необходимо для использования декоратора `transactional`.
- `_setup_agent(self, agent, configuration)`: Настройка агента.


## Функции

### `TinyFactory.set_simulation_for_free_factories(simulation)`

**Описание**: Устанавливает симуляцию для свободных фабрик, если она не задана.

### `TinyFactory.add_factory(factory)`

**Описание**: Добавляет фабрику в список всех фабрик.


### `TinyFactory.clear_factories()`

**Описание**: Очищает глобальный список всех фабрик.