# Модуль tinytroupe.factory

## Обзор

Этот модуль предоставляет базовый класс `TinyFactory` и его подкласс `TinyPersonFactory` для создания и управления различными типами фабрик в системе.  `TinyFactory` служит абстрактной базой, облегчая расширение системы, особенно в отношении кэширования транзакций. `TinyPersonFactory` предназначен для генерации агентов типа `TinyPerson` с использованием OpenAI LLM.

## Классы

### `TinyFactory`

**Описание**: Базовый класс для различных типов фабрик. Обеспечивает механизмы для управления фабриками и кэширования состояния.

**Методы**:

- `__init__(self, simulation_id: str = None)`: Инициализирует экземпляр `TinyFactory`.
- `__repr__(self)`: Возвращает строковое представление объекта.
- `set_simulation_for_free_factories(simulation)`: Устанавливает симуляцию для свободных фабрик, если она не задана.
- `add_factory(factory)`: Добавляет фабрику в список всех фабрик.
- `clear_factories()`: Очищает глобальный список всех фабрик.
- `encode_complete_state(self) -> dict`: Кодирует полное состояние фабрики. Подклассы должны переопределять этот метод, если содержат не сериализуемые элементы.
- `decode_complete_state(self, state: dict)`: Декодирует полное состояние фабрики. Подклассы должны переопределять этот метод, если содержат не сериализуемые элементы.


**Атрибуты**:

- `all_factories`: Словарь, содержащий все созданные фабрики.


### `TinyPersonFactory`

**Описание**: Фабрика для генерации агентов типа `TinyPerson` на основе контекста. Поддерживает кэширование сгенерированных мини-биографии, чтобы избежать дублирования.


**Методы**:

- `__init__(self, context_text, simulation_id: str = None)`: Инициализирует экземпляр `TinyPersonFactory`.
- `generate_person_factories(number_of_factories, generic_context_text)`: Генерирует список экземпляров `TinyPersonFactory` используя OpenAI LLM.
- `generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5)`: Генерирует экземпляр `TinyPerson` используя OpenAI LLM.
- `_aux_model_call(self, messages, temperature)`: Вспомогательный метод для вызова модели. Необходим для корректной работы декоратора `transactional`.
- `_setup_agent(self, agent, configuration)`: Настраивает агента с необходимыми элементами.


**Атрибуты**:

- `person_prompt_template_path`: Путь к шаблону запроса для генерации персоны.
- `context_text`: Текст контекста для генерации персоны.
- `generated_minibios`: Список сгенерированных мини-биографий.
- `generated_names`: Список сгенерированных имен.

## Функции

### `TinyFactory.set_simulation_for_free_factories(simulation)`

**Описание**: Устанавливает симуляцию для свободных фабрик, если она не задана.

**Параметры**:

- `simulation`: Объект симуляции.

### `TinyFactory.add_factory(factory)`

**Описание**: Добавляет фабрику в список всех фабрик.

**Параметры**:

- `factory`: Объект фабрики.

**Возвращает исключения**:

- `ValueError`: Если фабрика с таким именем уже существует.

### `TinyFactory.clear_factories()`

**Описание**: Очищает глобальный список всех фабрик.


### `TinyPersonFactory.generate_person_factories(number_of_factories, generic_context_text)`

**Описание**: Генерирует список `TinyPersonFactory` экземпляров с использованием OpenAI LLM.

**Параметры**:

- `number_of_factories`: Количество экземпляров `TinyPersonFactory` для генерации.
- `generic_context_text`: Общий контекст для генерации экземпляров.

**Возвращает**:

- `list`: Список экземпляров `TinyPersonFactory` или `None` при ошибке.


### `TinyPersonFactory.generate_person(agent_particularities=None, temperature=1.5, attempts=5)`

**Описание**: Генерирует экземпляр `TinyPerson` с использованием OpenAI LLM.

**Параметры**:

- `agent_particularities`: Описание особенностей агента.
- `temperature`: Температура для генерации текста.
- `attempts`: Максимальное количество попыток генерации.

**Возвращает**:

- `TinyPerson`: Экземпляр `TinyPerson` или `None` при ошибке.

**Вызывает исключения**:

- `Exception`:  Различные исключения, которые могут возникнуть при общении с моделью OpenAI.


### `TinyPersonFactory._aux_model_call(messages, temperature)`

**Описание**: Вспомогательный метод для вызова модели. Необходим для корректной работы декоратора `transactional`.

**Параметры**:

- `messages`: Список сообщений для модели.
- `temperature`: Температура для генерации.

**Возвращает**:

- `dict`: Ответ модели или `None` при ошибке.


### `TinyPersonFactory._setup_agent(agent, configuration)`

**Описание**: Настраивает агента с необходимыми элементами.

**Параметры**:

- `agent`: Объект агента.
- `configuration`: Словарь конфигурации.