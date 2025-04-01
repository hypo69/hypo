# Модуль `tiny_person_factory.py`

## Обзор

Модуль `tiny_person_factory.py` содержит класс `TinyPersonFactory`, который используется для создания экземпляров класса `TinyPerson` с использованием OpenAI LLM. Этот класс отвечает за генерацию персонажей на основе заданного контекста, управление уникальностью имен и мини-биографий, а также настройку агентов с необходимыми параметрами. Модуль также включает вспомогательные функции для генерации нескольких фабрик персонажей и обработки вызовов к модели OpenAI.

## Подробнее

`TinyPersonFactory` является частью системы генерации персонажей для симуляций. Он использует OpenAI LLM для создания реалистичных персонажей на основе заданного контекста. Фабрика управляет уникальностью имен и мини-биографий, чтобы избежать повторений и обеспечить разнообразие персонажей в симуляции. Этот модуль важен для создания разнообразных и уникальных агентов, которые могут взаимодействовать в рамках симуляции.

## Классы

### `TinyPersonFactory`

**Описание**: Фабрика для создания экземпляров класса `TinyPerson` с использованием OpenAI LLM.

**Наследует**: `TinyFactory`

**Атрибуты**:
- `person_prompt_template_path` (str): Путь к шаблону mustache для генерации запросов персонажа.
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `generated_minibios` (list): Список сгенерированных мини-биографий для отслеживания созданных персонажей.
- `generated_names` (list): Список сгенерированных имен для обеспечения уникальности.

**Методы**:
- `__init__(self, context_text, simulation_id: str = None)`: Инициализирует экземпляр `TinyPersonFactory`.
- `generate_person_factories(number_of_factories, generic_context_text)`: Генерирует список экземпляров `TinyPersonFactory` с использованием OpenAI LLM.
- `generate_person(self, agent_particularities: str = None, temperature: float = 1.5, frequency_penalty: float = 0.0, presence_penalty: float = 0.0, attepmpts: int = 10)`: Генерирует экземпляр `TinyPerson` с использованием OpenAI LLM.
- `generate_people(self, number_of_people: int, agent_particularities: str = None, temperature: float = 1.5, frequency_penalty: float = 0.0, presence_penalty: float = 0.0, attepmpts: int = 10, verbose: bool = False) -> list`: Генерирует список экземпляров `TinyPerson` с использованием OpenAI LLM.
- `_aux_model_call(self, messages, temperature, frequency_penalty, presence_penalty)`: Вспомогательный метод для выполнения вызова к модели OpenAI.
- `_setup_agent(self, agent, configuration)`: Настраивает агента с необходимыми элементами.

## Функции

### `__init__`

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

**Назначение**: Инициализирует экземпляр класса `TinyPersonFactory`.

**Параметры**:
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `simulation_id` (str, optional): ID симуляции. По умолчанию `None`.

**Возвращает**: `None`

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:
1. Вызывает конструктор родительского класса `TinyFactory` с параметром `simulation_id`.
2. Устанавливает путь к шаблону mustache для генерации запросов персонажа.
3. Инициализирует атрибут `context_text` переданным значением.
4. Инициализирует пустой список `generated_minibios` для хранения сгенерированных мини-биографий.
5. Инициализирует пустой список `generated_names` для хранения сгенерированных имен.

**Примеры**:
```python
factory = TinyPersonFactory("Some context", "simulation123")
```

### `generate_person_factories`

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

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1. Логирует начало процесса генерации фабрик персонажей.
2. Открывает и считывает системный промпт из файла `prompts/generate_person_factory.md`.
3. Формирует пользовательский промпт с использованием шаблона chevron, подставляя количество фабрик и контекст.
4. Отправляет сообщение в OpenAI LLM для генерации описаний фабрик персонажей.
5. Извлекает JSON из ответа OpenAI.
6. Создает экземпляры `TinyPersonFactory` на основе извлеченных описаний и добавляет их в список.
7. Возвращает список сгенерированных фабрик.

ASCII схема работы функции:

```
A [Начало]
|
B [Логирование начала генерации]
|
C [Чтение системного промпта]
|
D [Формирование пользовательского промпта]
|
E [Отправка сообщения в OpenAI LLM]
|
F [Извлечение JSON из ответа]
|
G [Создание экземпляров TinyPersonFactory]
|
H [Возврат списка фабрик]
|
I [Конец]
```

**Примеры**:
```python
factories = TinyPersonFactory.generate_person_factories(2, "Generic context")
```

### `generate_person`

```python
def generate_person(self, 
                    agent_particularities:str=None, 
                    temperature:float=1.5, 
                    frequency_penalty:float=0.0,
                    presence_penalty:float=0.0, 
                    attepmpts:int=10):
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
- `agent_particularities` (str, optional): Особенности агента. По умолчанию `None`.
- `temperature` (float, optional): Температура для использования при выборке из LLM. По умолчанию `1.5`.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию `0.0`.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию `0.0`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `10`.

**Возвращает**:
- `TinyPerson`: Экземпляр `TinyPerson`, сгенерированный с использованием LLM.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1. Логирует начало процесса генерации персонажа.
2. Загружает примеры спецификаций агентов из файлов `Friedrich_Wolf.agent.json` и `Sophie_Lefevre.agent.json`.
3. Формирует промпт с использованием шаблона chevron, подставляя контекст, особенности агента, примеры и списки сгенерированных имен и мини-биографий.
4. Определяет внутреннюю функцию `aux_generate`, которая отправляет промпт в OpenAI LLM и извлекает JSON из ответа.
5. В цикле вызывает `aux_generate` до тех пор, пока не будет сгенерирована подходящая спецификация агента или не будет достигнуто максимальное количество попыток.
6. Создает экземпляр `TinyPerson` на основе сгенерированной спецификации и настраивает его.
7. Добавляет мини-биографию и имя агента в соответствующие списки.
8. Возвращает сгенерированного агента.

**Внутренние функции**:

### `aux_generate`

```python
def aux_generate(attempt):
    """
    Внутренняя функция для генерации спецификации агента.

    Args:
        attempt (int): Номер попытки генерации.

    Returns:
        dict: Спецификация агента в виде словаря или None, если не удалось сгенерировать.
    """
    ...
```

**Назначение**: Внутренняя функция, которая отправляет промпт в OpenAI LLM и извлекает JSON из ответа.

**Параметры**:
- `attempt` (int): Номер попытки генерации.

**Возвращает**:
- `dict`: Спецификация агента в виде словаря или `None`, если не удалось сгенерировать.

**Как работает функция**:
1. Формирует список сообщений для отправки в OpenAI LLM, включая системное сообщение и промпт пользователя.
2. Если это не первая попытка, добавляет дополнительное сообщение, чтобы избежать повторения имен.
3. Вызывает метод `_aux_model_call` для отправки сообщения в OpenAI LLM и получения ответа.
4. Извлекает JSON из ответа.
5. Проверяет, что имя агента еще не сгенерировано.
6. Возвращает спецификацию агента, если она удовлетворяет всем требованиям.

ASCII схема работы функции `generate_person`:

```
A [Начало]
|
B [Загрузка примеров спецификаций]
|
C [Формирование промпта]
|
D [Цикл попыток генерации]
|
E [Вызов aux_generate]
|
F [Проверка уникальности имени]
|
G [Создание экземпляра TinyPerson]
|
H [Настройка агента]
|
I [Обновление списков]
|
J [Возврат агента]
|
K [Конец]
```

**Примеры**:
```python
factory = TinyPersonFactory("Some context")
person = factory.generate_person(agent_particularities="Some particularities")
```

### `generate_people`

```python
def generate_people(self, number_of_people:int, 
                    agent_particularities:str=None, 
                    temperature:float=1.5, 
                    frequency_penalty:float=0.0,
                    presence_penalty:float=0.0,
                    attepmpts:int=10, 
                    verbose:bool=False) -> list:
    """
    Generate a list of TinyPerson instances using OpenAI's LLM.

    Args:
        number_of_people (int): The number of TinyPerson instances to generate.
        agent_particularities (str): The particularities of the agent.
        temperature (float): The temperature to use when sampling from the LLM.
        verbose (bool): Whether to print verbose information.

    Returns:
        list: A list of TinyPerson instances generated using the LLM.
    """
    ...
```

**Назначение**: Генерирует список экземпляров `TinyPerson` с использованием OpenAI LLM.

**Параметры**:
- `number_of_people` (int): Количество экземпляров `TinyPerson` для генерации.
- `agent_particularities` (str, optional): Особенности агента. По умолчанию `None`.
- `temperature` (float, optional): Температура для использования при выборке из LLM. По умолчанию `1.5`.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию `0.0`.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию `0.0`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `10`.
- `verbose` (bool, optional): Флаг для вывода подробной информации. По умолчанию `False`.

**Возвращает**:
- `list`: Список экземпляров `TinyPerson`, сгенерированных с использованием LLM.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1. Инициализирует пустой список `people` для хранения сгенерированных агентов.
2. В цикле вызывает метод `generate_person` для генерации каждого агента.
3. Добавляет сгенерированного агента в список `people`.
4. Логирует и, если указано, выводит подробную информацию о сгенерированном агенте.
5. Возвращает список сгенерированных агентов.

ASCII схема работы функции:

```
A [Начало]
|
B [Инициализация списка]
|
C [Цикл генерации персонажей]
|
D [Вызов generate_person]
|
E [Добавление в список]
|
F [Логирование]
|
G [Возврат списка]
|
H [Конец]
```

**Примеры**:
```python
factory = TinyPersonFactory("Some context")
people = factory.generate_people(2, agent_particularities="Some particularities", verbose=True)
```

### `_aux_model_call`

```python
@transactional
def _aux_model_call(self, messages, temperature, frequency_penalty, presence_penalty):
    """
    Auxiliary method to make a model call. This is needed in order to be able to use the transactional decorator,
    due too a technicality - otherwise, the agent creation would be skipped during cache reutilization, and
    we don't want that.
    """
    ...
```

**Назначение**: Вспомогательный метод для выполнения вызова к модели OpenAI.

**Параметры**:
- `messages` (list): Список сообщений для отправки в OpenAI LLM.
- `temperature` (float): Температура для использования при выборке из LLM.
- `frequency_penalty` (float): Штраф за частоту.
- `presence_penalty` (float): Штраф за присутствие.

**Возвращает**:
- `dict`: Ответ от OpenAI LLM.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1. Отправляет сообщение в OpenAI LLM с указанными параметрами.
2. Возвращает ответ от OpenAI LLM.

ASCII схема работы функции:

```
A [Начало]
|
B [Отправка сообщения в OpenAI LLM]
|
C [Возврат ответа]
|
D [Конец]
```

**Примеры**:
```python
factory = TinyPersonFactory("Some context")
messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Tell me a joke."}]
response = factory._aux_model_call(messages, 0.7, 0.0, 0.0)
```

### `_setup_agent`

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
- `agent` (TinyPerson): Экземпляр агента для настройки.
- `configuration` (dict): Конфигурация агента.

**Возвращает**: `None`

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1. Включает определения персонажа в агента на основе предоставленной конфигурации.

ASCII схема работы функции:

```
A [Начало]
|
B [Включение определений персонажа]
|
C [Конец]
```

**Примеры**:
```python
factory = TinyPersonFactory("Some context")
person = TinyPerson("John Doe")
configuration = {"persona": {"age": 30, "occupation": "Software Engineer"}}
factory._setup_agent(person, configuration)