# Модуль `tiny_person_factory.py`

## Обзор

Модуль `tiny_person_factory.py` предоставляет класс `TinyPersonFactory`, который используется для создания экземпляров класса `TinyPerson` с использованием OpenAI LLM. Он включает в себя методы для генерации как отдельных персон, так и списков персон на основе заданного контекста.

## Подробней

Этот модуль является частью системы для генерации реалистичных симуляций людей. Он использует текстовые описания контекста для создания уникальных персонажей с различными характеристиками. Класс `TinyPersonFactory` управляет процессом создания персонажей, гарантируя, что имена персонажей уникальны, и предоставляет возможность настройки процесса генерации с использованием различных параметров, таких как температура и штрафы за частоту и присутствие.

## Классы

### `TinyPersonFactory`

**Описание**: Фабрика для создания экземпляров класса `TinyPerson` на основе контекста с использованием OpenAI LLM.

**Наследует**:
- `TinyFactory`: Класс `TinyPersonFactory` наследует от класса `TinyFactory`, который, вероятно, предоставляет общую функциональность для создания различных объектов в системе.

**Атрибуты**:
- `person_prompt_template_path` (str): Путь к файлу шаблона mustache, используемому для генерации подсказок для создания персон.
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `generated_minibios` (list): Список сгенерированных мини-биографий. Используется для отслеживания сгенерированных персон и предотвращения повторной генерации тех же самых персон.
- `generated_names` (list): Список сгенерированных имен.

**Методы**:
- `__init__`: Инициализирует экземпляр `TinyPersonFactory`.
- `generate_person_factories`: Генерирует список экземпляров `TinyPersonFactory`, используя OpenAI LLM.
- `generate_person`: Генерирует экземпляр `TinyPerson`, используя OpenAI LLM.
- `generate_people`: Генерирует список экземпляров `TinyPerson`, используя OpenAI LLM.
- `_aux_model_call`: Вспомогательный метод для выполнения вызова модели.
- `_setup_agent`: Настраивает агента с необходимыми элементами.

### `__init__`

```python
def __init__(self, context_text, simulation_id:str=None):
    """
    Initialize a TinyPersonFactory instance.

    Args:
        context_text (str): The context text used to generate the TinyPerson instances.
        simulation_id (str, optional): The ID of the simulation. Defaults to None.
    """
```

**Назначение**: Инициализирует экземпляр `TinyPersonFactory`.

**Параметры**:
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `simulation_id` (str, optional): ID симуляции. По умолчанию `None`.

**Как работает функция**:
1. Вызывает конструктор суперкласса (`TinyFactory`) с переданным `simulation_id`.
2. Устанавливает путь к шаблону подсказок для генерации персоны (`person_prompt_template_path`).
3. Сохраняет переданный `context_text` в атрибуте `self.context_text`.
4. Инициализирует пустой список `self.generated_minibios` для отслеживания сгенерированных мини-биографий.
5. Инициализирует пустой список `self.generated_names` для отслеживания сгенерированных имен.

```
A: Вызов конструктора суперкласса
|
B: Установка пути к шаблону подсказок
|
C: Сохранение контекстного текста
|
D: Инициализация списка сгенерированных мини-биографий
|
E: Инициализация списка сгенерированных имен
```

**Примеры**:

```python
factory = TinyPersonFactory("Some context text", "simulation123")
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
```

**Назначение**: Генерирует список экземпляров `TinyPersonFactory`, используя OpenAI LLM.

**Параметры**:
- `number_of_factories` (int): Количество экземпляров `TinyPersonFactory` для генерации.
- `generic_context_text` (str): Общий контекстный текст, используемый для генерации экземпляров `TinyPersonFactory`.

**Возвращает**:
- `list`: Список экземпляров `TinyPersonFactory`.

**Как работает функция**:
1. Логирует начало генерации фабрик персон, используя `logger.info`.
2. Читает системную подсказку из файла `prompts/generate_person_factory.md`.
3. Формирует пользовательскую подсказку, используя шаблон chevron для запроса к OpenAI.
4. Отправляет сообщение в OpenAI, используя `openai_utils.client().send_message`.
5. Извлекает JSON из ответа OpenAI.
6. Создает экземпляры `TinyPersonFactory` на основе извлеченного JSON и добавляет их в список.
7. Возвращает список фабрик.

```
A: Логирование начала генерации фабрик
|
B: Чтение системной подсказки из файла
|
C: Формирование пользовательской подсказки
|
D: Отправка сообщения в OpenAI
|
E: Извлечение JSON из ответа OpenAI
|
F: Создание экземпляров TinyPersonFactory
|
G: Возврат списка фабрик
```

**Примеры**:

```python
factories = TinyPersonFactory.generate_person_factories(3, "Generic context text")
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
```

**Назначение**: Генерирует экземпляр `TinyPerson`, используя OpenAI LLM.

**Параметры**:
- `agent_particularities` (str, optional): Особенности агента. По умолчанию `None`.
- `temperature` (float, optional): Температура для выборки из LLM. По умолчанию `1.5`.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию `0.0`.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию `0.0`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `10`.

**Возвращает**:
- `TinyPerson`: Экземпляр `TinyPerson`, сгенерированный с использованием LLM.

**Как работает функция**:
1. Логирует начало генерации персоны, используя `logger.info`.
2. Загружает примеры спецификаций агентов из файлов JSON.
3. Формирует подсказку, используя шаблон chevron и контекст, особенности агента, примеры и списки сгенерированных имен и мини-биографий.
4. Определяет вспомогательную функцию `aux_generate` для выполнения вызова модели.
5. В цикле пытается сгенерировать спецификацию агента, используя `aux_generate`, пока не будет получена подходящая спецификация или не будет достигнуто максимальное количество попыток.
6. Если спецификация агента получена, создает экземпляр `TinyPerson`, настраивает его, добавляет мини-биографию в список сгенерированных мини-биографий и имя в список сгенерированных имен.
7. Если спецификация агента не получена после всех попыток, логирует ошибку и возвращает `None`.

Внутренняя функция `aux_generate`:
   - Принимает номер попытки `attempt` в качестве аргумента.
   - Формирует список сообщений для отправки в OpenAI, включая системное сообщение и пользовательскую подсказку.
   - Если это не первая попытка, добавляет дополнительное сообщение с указанием не генерировать то же имя снова.
   - Вызывает метод `_aux_model_call` для отправки сообщения в OpenAI и получения результата.
   - Извлекает JSON из результата.
   - Проверяет, что имя не находится в списке уже сгенерированных имен.
   - Логирует сгенерированные параметры персоны.
   - Возвращает результат, если имя уникально, иначе возвращает `None`.
```
A: Логирование начала генерации персоны
|
B: Загрузка примеров спецификаций агентов
|
C: Формирование подсказки
|
D: Определение вспомогательной функции aux_generate
|
E: Цикл попыток генерации спецификации агента
|
F: Создание экземпляра TinyPerson
|
G: Настройка экземпляра TinyPerson
|
H: Обновление списков сгенерированных данных
|
I: Логирование и возврат результата
```

**Примеры**:

```python
person = factory.generate_person("Some agent particularities", temperature=1.0)
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
```

**Назначение**: Генерирует список экземпляров `TinyPerson`, используя OpenAI LLM.

**Параметры**:
- `number_of_people` (int): Количество экземпляров `TinyPerson` для генерации.
- `agent_particularities` (str, optional): Особенности агента. По умолчанию `None`.
- `temperature` (float, optional): Температура для выборки из LLM. По умолчанию `1.5`.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию `0.0`.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию `0.0`.
- `attepmpts` (int, optional): Количество попыток генерации. По умолчанию `10`.
- `verbose` (bool, optional): Флаг, указывающий, следует ли печатать подробную информацию. По умолчанию `False`.

**Возвращает**:
- `list`: Список экземпляров `TinyPerson`, сгенерированных с использованием LLM.

**Как работает функция**:
1. Инициализирует пустой список `people`.
2. В цикле генерирует экземпляры `TinyPerson`, используя метод `generate_person`.
3. Если персона успешно сгенерирована, добавляет ее в список `people`.
4. Логирует информацию о сгенерированной персоне, используя `logger.info`.
5. Если `verbose` равен `True`, выводит информацию о сгенерированной персоне в консоль.
6. Если персона не может быть сгенерирована, логирует ошибку.
7. Возвращает список сгенерированных персон.

```
A: Инициализация списка people
|
B: Цикл генерации экземпляров TinyPerson
|
C: Логирование информации о сгенерированной персоне
|
D: Вывод информации о сгенерированной персоне (если verbose=True)
|
E: Логирование ошибки, если персона не может быть сгенерирована
|
F: Возврат списка сгенерированных персон
```

**Примеры**:

```python
people = factory.generate_people(5, "Some agent particularities", verbose=True)
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
```

**Назначение**: Вспомогательный метод для выполнения вызова модели.

**Параметры**:
- `messages` (list): Список сообщений для отправки в OpenAI.
- `temperature` (float): Температура для выборки из LLM.
- `frequency_penalty` (float): Штраф за частоту.
- `presence_penalty` (float): Штраф за присутствие.

**Возвращает**:
- `dict`: Ответ от OpenAI API.

**Как работает функция**:
1.  Отправляет сообщение в OpenAI, используя `openai_utils.client().send_message`.
2.  Передает параметры `temperature`, `frequency_penalty` и `presence_penalty`.
3.  Указывает формат ответа как JSON.

```
A: Отправка сообщения в OpenAI
```

### `_setup_agent`

```python
@transactional
def _setup_agent(self, agent, configuration):
    """
    Sets up the agent with the necessary elements.
    """
```

**Назначение**: Настраивает агента с необходимыми элементами.

**Параметры**:
- `agent` (TinyPerson): Агент для настройки.
- `configuration` (dict): Конфигурация агента.

**Как работает функция**:
1.  Включает определения персонажа в агенте, используя `agent.include_persona_definitions(configuration)`.

```
A: Включение определений персонажа в агенте
```