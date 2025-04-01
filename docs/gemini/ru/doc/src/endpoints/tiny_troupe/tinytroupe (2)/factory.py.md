# Модуль `factory.py`

## Обзор

Модуль `factory.py` содержит классы и функции для создания агентов `TinyPerson` с использованием OpenAI LLM. Он включает механизмы кэширования и обеспечивает уникальность создаваемых агентов.

## Подробней

Модуль предоставляет базовый класс `TinyFactory`, от которого наследуется `TinyPersonFactory`. `TinyFactory` содержит общую логику для фабрик, включая управление списком фабрик и механизмы кэширования. `TinyPersonFactory` специализируется на создании экземпляров `TinyPerson` на основе контекста и шаблонов, используя OpenAI для генерации спецификаций агентов. Модуль обеспечивает возможность генерации нескольких фабрик агентов на основе заданного контекста.

## Классы

### `TinyFactory`

**Описание**: Базовый класс для различных типов фабрик.

**Принцип работы**:
`TinyFactory` служит базовым классом для создания различных фабрик в системе. Он предоставляет основные механизмы для управления фабриками, такие как добавление, удаление и кэширование. Класс также обеспечивает методы для кодирования и декодирования состояния фабрики, что важно для сохранения состояния при кэшировании транзакций.

**Аттрибуты**:
- `all_factories` (dict): Словарь, содержащий все созданные фабрики. Ключ - имя фабрики, значение - экземпляр фабрики.
- `name` (str): Уникальное имя фабрики.
- `simulation_id` (str): ID симуляции, к которой принадлежит фабрика.

**Методы**:
- `__init__(simulation_id: str = None) -> None`: Инициализирует экземпляр `TinyFactory`.
- `__repr__() -> str`: Возвращает строковое представление объекта `TinyFactory`.
- `set_simulation_for_free_factories(simulation)`: Устанавливает симуляцию для свободных фабрик.
- `add_factory(factory)`: Добавляет фабрику в список всех фабрик.
- `clear_factories()`: Очищает глобальный список всех фабрик.
- `encode_complete_state() -> dict`: Кодирует полное состояние фабрики.
- `decode_complete_state(state: dict)`: Декодирует полное состояние фабрики.

### `TinyPersonFactory`

**Описание**: Класс для создания экземпляров `TinyPerson`.

**Наследует**:
- `TinyFactory`: Наследует функциональность базовой фабрики.

**Принцип работы**:
`TinyPersonFactory` специализируется на создании агентов `TinyPerson` с использованием OpenAI LLM. Он использует контекстный текст и шаблоны для генерации спецификаций агентов. Класс включает механизмы для отслеживания сгенерированных агентов и обеспечения их уникальности. Также предоставляет методы для настройки агентов и выполнения вызовов к модели OpenAI с использованием декоратора `transactional` для кэширования.

**Аттрибуты**:
- `person_prompt_template_path` (str): Путь к шаблону prompt для генерации персоны.
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `generated_minibios` (list): Список сгенерированных `minibio` для отслеживания созданных персон.
- `generated_names` (list): Список сгенерированных имен для обеспечения уникальности персон.

**Методы**:
- `__init__(context_text, simulation_id: str = None)`: Инициализирует экземпляр `TinyPersonFactory`.
- `generate_person_factories(number_of_factories, generic_context_text)`: Генерирует список экземпляров `TinyPersonFactory` с использованием OpenAI LLM.
- `generate_person(agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5)`: Генерирует экземпляр `TinyPerson` с использованием OpenAI LLM.
- `_aux_model_call(messages, temperature)`: Вспомогательный метод для выполнения вызова модели.
- `_setup_agent(agent, configuration)`: Настраивает агента с необходимыми элементами.

## Функции

### `TinyFactory.__init__`

```python
def __init__(self, simulation_id:str=None) -> None:
    """
    Initialize a TinyFactory instance.

    Args:
        simulation_id (str, optional): The ID of the simulation. Defaults to None.
    """
    ...
```

**Назначение**: Инициализирует экземпляр `TinyFactory`.

**Параметры**:
- `simulation_id` (str, optional): ID симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Как работает функция**:
1. Присваивает фабрике уникальное имя, используя `utils.fresh_id()`.
2. Устанавливает ID симуляции.
3. Добавляет фабрику в статический словарь `TinyFactory.all_factories`.

```
Создание имени фабрики --> Присвоение ID симуляции --> Добавление фабрики в общий список
```

**Примеры**:
```python
factory = TinyFactory(simulation_id="sim123")
print(factory.name)  # Вывод: Factory <id>
```

### `TinyFactory.__repr__`

```python
def __repr__(self):
    """
    Returns:
        str: Строковое представление объекта `TinyFactory`.
    """
    ...
```

**Назначение**: Возвращает строковое представление объекта `TinyFactory`.

**Возвращает**:
- `str`: Строковое представление объекта `TinyFactory`.

**Как работает функция**:
Функция формирует строковое представление объекта `TinyFactory`, которое включает имя фабрики.

```
Формирование строки --> Возврат строки
```

**Примеры**:
```python
factory = TinyFactory(simulation_id="sim123")
print(repr(factory))  # Вывод: TinyFactory(name='Factory <id>')
```

### `TinyFactory.set_simulation_for_free_factories`

```python
@staticmethod
def set_simulation_for_free_factories(simulation):
    """
    Sets the simulation if it is None. This allows free environments to be captured by specific simulation scopes
    if desired.
    """
    ...
```

**Назначение**: Устанавливает симуляцию для фабрик, у которых `simulation_id` равен `None`.

**Параметры**:
- `simulation`: Объект симуляции, который нужно установить для свободных фабрик.

**Как работает функция**:
1. Проходит по всем фабрикам в `TinyFactory.all_factories`.
2. Если у фабрики `simulation_id` равен `None`, добавляет фабрику в симуляцию.

```
Перебор фабрик --> Проверка на отсутствие ID симуляции --> Добавление фабрики в симуляцию
```

**Примеры**:
```python
from tinytroupe.simulation import Simulation  # Предполагается, что класс Simulation существует

simulation = Simulation()
factory1 = TinyFactory(simulation_id=None)
factory2 = TinyFactory(simulation_id="sim123")
TinyFactory.set_simulation_for_free_factories(simulation)
# factory1 будет добавлена в simulation
```

### `TinyFactory.add_factory`

```python
@staticmethod
def add_factory(factory):
    """
    Adds a factory to the list of all factories. Factory names must be unique,
    so if an factory with the same name already exists, an error is raised.
    """
    ...
```

**Назначение**: Добавляет фабрику в список всех фабрик.

**Параметры**:
- `factory`: Фабрика, которую нужно добавить.

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким именем уже существует.

**Как работает функция**:
1. Проверяет, существует ли фабрика с таким именем в `TinyFactory.all_factories`.
2. Если фабрика с таким именем уже существует, выбрасывает исключение `ValueError`.
3. Иначе добавляет фабрику в `TinyFactory.all_factories`.

```
Проверка имени фабрики на уникальность --> Добавление фабрики в общий список (если имя уникально)
```

**Примеры**:
```python
factory = TinyFactory(simulation_id="sim123")
TinyFactory.add_factory(factory)
```

### `TinyFactory.clear_factories`

```python
@staticmethod
def clear_factories():
    """
    Clears the global list of all factories.
    """
    ...
```

**Назначение**: Очищает глобальный список всех фабрик.

**Как работает функция**:
Функция присваивает `TinyFactory.all_factories` пустой словарь, очищая список фабрик.

```
Очистка списка фабрик
```

**Примеры**:
```python
TinyFactory.clear_factories()
```

### `TinyFactory.encode_complete_state`

```python
def encode_complete_state(self) -> dict:
    """
    Encodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Кодирует полное состояние фабрики.

**Возвращает**:
- `dict`: Словарь, представляющий состояние фабрики.

**Как работает функция**:
1. Создает глубокую копию словаря `__dict__` фабрики.
2. Возвращает словарь, представляющий состояние фабрики.

```
Копирование состояния фабрики --> Возврат состояния
```

**Примеры**:
```python
factory = TinyFactory(simulation_id="sim123")
state = factory.encode_complete_state()
print(state)  # Вывод: Словарь с состоянием фабрики
```

### `TinyFactory.decode_complete_state`

```python
def decode_complete_state(self, state:dict):
    """
    Decodes the complete state of the factory. If subclasses have elmements that are not serializable, they should override this method.
    """
    ...
```

**Назначение**: Декодирует полное состояние фабрики.

**Параметры**:
- `state` (dict): Словарь, представляющий состояние фабрики.

**Возвращает**:
- `self`: Объект `TinyFactory` с восстановленным состоянием.

**Как работает функция**:
1. Создает глубокую копию переданного словаря `state`.
2. Обновляет словарь `__dict__` фабрики с использованием состояния из словаря `state`.
3. Возвращает объект `TinyFactory` с восстановленным состоянием.

```
Копирование состояния --> Обновление состояния фабрики --> Возврат фабрики с восстановленным состоянием
```

**Примеры**:
```python
factory = TinyFactory(simulation_id="sim123")
state = {"name": "Factory123", "simulation_id": "sim456"}
factory.decode_complete_state(state)
print(factory.simulation_id)  # Вывод: sim456
```

### `TinyPersonFactory.__init__`

```python
def __init__(self, context_text, simulation_id:str=None):
    """
    Initialize a TinyPersonFactory instance.

    Args:
        context_text (str): The context text used to generate the TinyPerson instances.
        simulation_id (str, optional): The ID of the simulation. Defaults to None.
    """
    ...
```

**Назначение**: Инициализирует экземпляр `TinyPersonFactory`.

**Параметры**:
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `simulation_id` (str, optional): ID симуляции. По умолчанию `None`.

**Как работает функция**:
1. Вызывает конструктор базового класса `TinyFactory` с переданным `simulation_id`.
2. Устанавливает путь к шаблону prompt для генерации персоны (`person_prompt_template_path`).
3. Сохраняет контекстный текст (`context_text`).
4. Инициализирует пустой список для хранения сгенерированных `minibio` (`generated_minibios`).
5. Инициализирует пустой список для хранения сгенерированных имен (`generated_names`).

```
Вызов конструктора базового класса --> Установка пути к шаблону --> Сохранение контекстного текста --> Инициализация списков для сгенерированных данных
```

**Примеры**:
```python
factory = TinyPersonFactory(context_text="Some context", simulation_id="sim123")
print(factory.context_text)  # Вывод: Some context
```

### `TinyPersonFactory.generate_person_factories`

```python
@staticmethod
def generate_person_factories(number_of_factories, generic_context_text):
    """
    Generate a list of TinyPersonFactory instances using OpenAI's LLM.

    Args:
        number_of_factories (int): The number of TinyPersonFactory instances to generate.
        generic_context_text (str): The generic context text used to generate the TinyPersonFactory instances.

    Returns:
        list: A list of TinyPersonFactory instances.
    """
    ...
```

**Назначение**: Генерирует список экземпляров `TinyPersonFactory` с использованием OpenAI LLM.

**Параметры**:
- `number_of_factories` (int): Количество экземпляров `TinyPersonFactory` для генерации.
- `generic_context_text` (str): Общий контекстный текст, используемый для генерации экземпляров `TinyPersonFactory`.

**Возвращает**:
- `list`: Список экземпляров `TinyPersonFactory`.

**Как работает функция**:
1. Формирует системный prompt на основе файла `prompts/generate_person_factory.md`.
2. Формирует пользовательский prompt, запрашивая `number_of_factories` описаний персон на основе `generic_context_text`.
3. Отправляет сообщение в OpenAI LLM.
4. Извлекает JSON из ответа LLM.
5. Создает экземпляры `TinyPersonFactory` на основе извлеченных JSON.
6. Возвращает список созданных фабрик.

```
Формирование системного prompt --> Формирование пользовательского prompt --> Отправка сообщения в OpenAI --> Извлечение JSON из ответа --> Создание экземпляров TinyPersonFactory --> Возврат списка фабрик
```

**Примеры**:
```python
factories = TinyPersonFactory.generate_person_factories(number_of_factories=2, generic_context_text="Some generic context")
print(len(factories))  # Вывод: 2
```

### `TinyPersonFactory.generate_person`

```python
def generate_person(self, agent_particularities:str=None, temperature:float=1.5, attepmpts:int=5):
    """
    Generate a TinyPerson instance using OpenAI's LLM.

    Args:
        agent_particularities (str): The particularities of the agent.
        temperature (float): The temperature to use when sampling from the LLM.

    Returns:
        TinyPerson: A TinyPerson instance generated using the LLM.
    """
    ...
```

**Назначение**: Генерирует экземпляр `TinyPerson` с использованием OpenAI LLM.

**Параметры**:
- `agent_particularities` (str): Особенности агента.
- `temperature` (float): Температура для выборки из LLM.
- `attepmpts` (int): Число попыток генерации агента

**Возвращает**:
- `TinyPerson`: Экземпляр `TinyPerson`, сгенерированный с использованием LLM.

**Как работает функция**:
1.  Формирует prompt на основе шаблона `person_prompt_template_path`, контекстного текста, особенностей агента и уже сгенерированных `minibio`.
2.  Определяет внутреннюю функцию `aux_generate` для выполнения вызова модели.
3.  Вызывает `aux_generate` в цикле `attepmpts` раз, пока не будет сгенерирован подходящий агент или не истекут попытки.
4.  Если агент сгенерирован, создает экземпляр `TinyPerson`, настраивает его с помощью `_setup_agent`, добавляет `minibio` и имя агента в списки сгенерированных данных.
5.  Возвращает сгенерированного агента.

**Внутренние функции**:

#### `aux_generate`

```python
def aux_generate():
    """
    Внутренняя функция для выполнения вызова модели OpenAI.

    Returns:
        dict | None: Спецификация агента, если агент сгенерирован и его имя уникально, иначе `None`.
    """
    ...
```

**Назначение**: Внутренняя функция для выполнения вызова модели OpenAI.

**Как работает функция**:
1. Формирует список сообщений для отправки в OpenAI LLM.
2. Вызывает метод `_aux_model_call` для отправки сообщения в LLM и получения ответа.
3. Извлекает JSON из ответа LLM.
4. Проверяет, что имя агента не содержится в списке уже сгенерированных имен.
5. Если имя уникально, возвращает спецификацию агента, иначе возвращает `None`.

```
Формирование списка сообщений --> Вызов _aux_model_call --> Извлечение JSON из ответа --> Проверка уникальности имени --> Возврат спецификации агента или None
```

```
Формирование prompt --> Цикл попыток генерации:
    --> Вызов aux_generate:
        --> Формирование списка сообщений
        --> Вызов _aux_model_call
        --> Извлечение JSON из ответа
        --> Проверка уникальности имени
        --> Возврат спецификации агента или None
    --> Создание экземпляра TinyPerson
    --> Настройка агента
    --> Добавление данных в списки сгенерированных данных
    --> Возврат агента
```

**Примеры**:
```python
factory = TinyPersonFactory(context_text="Some context")
person = factory.generate_person(agent_particularities="Some particularities")
if person:
    print(person.name)
```

### `TinyPersonFactory._aux_model_call`

```python
@transactional
def _aux_model_call(self, messages, temperature):
    """
    Auxiliary method to make a model call. This is needed in order to be able to use the transactional decorator,
    due too a technicality - otherwise, the agent creation would be skipped during cache reutilization, and
    we don't want that.
    """
    ...
```

**Назначение**: Вспомогательный метод для выполнения вызова модели.

**Параметры**:
- `messages`: Список сообщений для отправки в LLM.
- `temperature`: Температура для выборки из LLM.

**Возвращает**:
- Ответ от OpenAI LLM.

**Как работает функция**:
Функция отправляет сообщение в OpenAI LLM с использованием `openai_utils.client().send_message` и возвращает ответ. Декоратор `@transactional` обеспечивает кэширование результата вызова.

```
Отправка сообщения в OpenAI --> Возврат ответа
```

**Примеры**:
```python
factory = TinyPersonFactory(context_text="Some context")
messages = [{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a joke."}]
response = factory._aux_model_call(messages=messages, temperature=0.7)
print(response)
```

### `TinyPersonFactory._setup_agent`

```python
@transactional
def _setup_agent(self, agent, configuration):
    """
    Sets up the agent with the necessary elements.
    """
    ...
```

**Назначение**: Настраивает агента с необходимыми элементами.

**Параметры**:
- `agent`: Агент для настройки.
- `configuration`: Словарь конфигурации агента.

**Как работает функция**:
1. Проходит по всем элементам в словаре конфигурации.
2. Если значение элемента является списком, вызывает `agent.define_several` для определения нескольких значений для ключа.
3. Иначе вызывает `agent.define` для определения одного значения для ключа.

```
Перебор элементов конфигурации --> Определение значений для агента (define_several или define)
```

**Примеры**:
```python
from tinytroupe.agent import TinyPerson  # Предполагается, что класс TinyPerson существует

factory = TinyPersonFactory(context_text="Some context")
agent = TinyPerson(name="John Doe")
configuration = {"age": 30, "hobbies": ["reading", "hiking"]}
factory._setup_agent(agent=agent, configuration=configuration)
print(agent.get("age"))  # Вывод: 30
print(agent.get("hobbies"))  # Вывод: ['reading', 'hiking']
```