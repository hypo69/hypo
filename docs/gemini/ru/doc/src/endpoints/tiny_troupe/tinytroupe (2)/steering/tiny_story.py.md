# Модуль `tiny_story.py`

## Обзор

Модуль `tiny_story.py` предназначен для создания и управления историями, основанными на симуляциях `TinyTroupe`. Он предоставляет механизмы для формирования историй об окружении или агентах, участвующих в симуляции, и позволяет направлять генерацию истории в соответствии с заданной целью. Модуль включает класс `TinyStory`, который помогает в создании связных и интересных повествований на основе данных симуляции.

## Подробнее

Модуль `tiny_story.py` содержит класс `TinyStory`, который отвечает за формирование историй на основе данных, полученных в ходе симуляции `TinyTroupe`. Он позволяет задавать контекст, цель истории, а также параметры, определяющие, какие взаимодействия агентов и окружающей среды будут включены в историю. Класс также предоставляет методы для начала и продолжения истории, используя шаблоны и AI-модели для генерации текста.

## Классы

### `TinyStory`

**Описание**: Класс `TinyStory` предназначен для создания историй на основе данных симуляции `TinyTroupe`. Он предоставляет методы для инициализации истории, задания цели и контекста, а также для генерации новых фрагментов истории на основе текущего состояния симуляции.

**Принцип работы**: Класс `TinyStory` принимает в качестве аргументов окружение (`TinyWorld`) или агента (`TinyPerson`), цель истории (`purpose`), контекст (`context`) и параметры, определяющие, какие взаимодействия будут включены в историю (`first_n`, `last_n`, `include_omission_info`). Он использует эти данные для формирования запросов к AI-моделям, которые генерируют текст истории.

**Атрибуты**:

-   `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
-   `agent` (TinyPerson, optional): Агент, о котором рассказывается история. По умолчанию `None`.
-   `purpose` (str, optional): Цель истории. По умолчанию "Be a realistic simulation.".
-   `current_story` (str): Текущий контекст истории.
-   `first_n` (int): Количество первых взаимодействий, включаемых в историю. По умолчанию 10.
-   `last_n` (int): Количество последних взаимодействий, включаемых в историю. По умолчанию 20.
-   `include_omission_info` (bool): Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Методы**:

-   `__init__(environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="", first_n=10, last_n=20, include_omission_info:bool=True) -> None`: Инициализирует объект `TinyStory`.
-   `start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str`: Начинает новую историю.
-   `continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str`: Продолжает существующую историю.
-   `_current_story(self) -> str`: Возвращает текущую историю с добавлением информации о последних взаимодействиях.

## Функции

### `__init__`

```python
def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n=10, last_n=20, include_omission_info:bool=True) -> None:
    """
    Initialize the story. The story can be about an environment or an agent. It also has a purpose, which
    is used to guide the story generation. Stories are aware that they are related to simulations, so one can
    specify simulation-related purposes.

    Args:
        environment (TinyWorld, optional): The environment in which the story takes place. Defaults to None.
        agent (TinyPerson, optional): The agent in the story. Defaults to None.
        purpose (str, optional): The purpose of the story. Defaults to "Be a realistic simulation.".
        context (str, optional): The current story context. Defaults to "". The actual story will be appended to this context.
        first_n (int, optional): The number of first interactions to include in the story. Defaults to 10.
        last_n (int, optional): The number of last interactions to include in the story. Defaults to 20.
        include_omission_info (bool, optional): Whether to include information about omitted interactions. Defaults to True.
    """
    ...
```

**Назначение**: Инициализирует объект `TinyStory`, задавая основные параметры истории.

**Параметры**:

-   `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
-   `agent` (TinyPerson, optional): Агент, о котором рассказывается история. По умолчанию `None`.
-   `purpose` (str, optional): Цель истории. По умолчанию "Be a realistic simulation.".
-   `context` (str, optional): Текущий контекст истории. По умолчанию "".
-   `first_n` (int, optional): Количество первых взаимодействий, включаемых в историю. По умолчанию 10.
-   `last_n` (int, optional): Количество последних взаимодействий, включаемых в историю. По умолчанию 20.
-   `include_omission_info` (bool, optional): Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Возвращает**:
    - `None`

**Вызывает исключения**:

-   `Exception`: Если переданы одновременно `environment` и `agent` или не передан ни один из них.

**Как работает функция**:

1.  Проверяет, что передан либо `environment`, либо `agent`, но не оба одновременно, и что хотя бы один из них передан.
2.  Сохраняет переданные параметры в атрибуты объекта `TinyStory`.
3.  Инициализирует атрибут `current_story` переданным контекстом.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.tiny_story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Explore the environment")

# Пример инициализации с агентом
agent = TinyPerson()
story = TinyStory(agent=agent, purpose="Follow the agent's journey")
```

### `start_story`

```python
def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Start a new story.
    """
    ...
```

**Назначение**: Начинает новую историю, генерируя начальный фрагмент текста на основе заданных параметров и шаблонов.

**Параметры**:

-   `requirements` (str, optional): Требования к началу истории. По умолчанию "Start some interesting story about the agents.".
-   `number_of_words` (int, optional): Количество слов в начальном фрагменте истории. По умолчанию 100.
-   `include_plot_twist` (bool, optional): Флаг, указывающий, следует ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

-   `str`: Начальный фрагмент истории.

**Как работает функция**:

1.  Формирует словарь `rendering_configs` с параметрами, необходимыми для генерации истории.
2.  Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для AI-модели на основе шаблонов "story.start.system.mustache" и "story.start.user.mustache".
3.  Отправляет сообщения AI-модели с помощью `openai_utils.client().send_message` и получает ответ.
4.  Извлекает текст начала истории из ответа AI-модели.
5.  Добавляет полученный текст в атрибут `current_story` объекта `TinyStory`.
6.  Возвращает начальный фрагмент истории.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.steering.tiny_story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Explore the environment")

# Начинаем новую историю
start = story.start_story(requirements="Tell a story about a new day in the village.", number_of_words=150)
print(start)
```

### `continue_story`

```python
def continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Propose a continuation of the story.
    """
    ...
```

**Назначение**: Продолжает существующую историю, генерируя следующий фрагмент текста на основе заданных параметров и шаблонов.

**Параметры**:

-   `requirements` (str, optional): Требования к продолжению истории. По умолчанию "Continue the story in an interesting way.".
-   `number_of_words` (int, optional): Количество слов в следующем фрагменте истории. По умолчанию 100.
-   `include_plot_twist` (bool, optional): Флаг, указывающий, следует ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

-   `str`: Следующий фрагмент истории.

**Как работает функция**:

1.  Формирует словарь `rendering_configs` с параметрами, необходимыми для генерации истории.
2.  Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для AI-модели на основе шаблонов "story.continuation.system.mustache" и "story.continuation.user.mustache".
3.  Отправляет сообщения AI-модели с помощью `openai_utils.client().send_message` и получает ответ.
4.  Извлекает текст продолжения истории из ответа AI-модели.
5.  Добавляет полученный текст в атрибут `current_story` объекта `TinyStory`.
6.  Возвращает следующий фрагмент истории.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.steering.tiny_story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Explore the environment")

# Начинаем новую историю
start = story.start_story(requirements="Tell a story about a new day in the village.", number_of_words=150)
print(start)

# Продолжаем историю
continuation = story.continue_story(requirements="Add a conflict between two villagers.", number_of_words=120)
print(continuation)
```

### `_current_story`

```python
def _current_story(self) -> str:
    """
    Get the current story.
    """
    ...
```

**Назначение**: Возвращает текущую историю с добавлением информации о последних взаимодействиях агента или окружения.

**Параметры**:

-   `None`

**Возвращает**:

-   `str`: Текущая история с добавленной информацией о взаимодействиях.

**Как работает функция**:

1.  Инициализирует переменную `interaction_history` пустой строкой.
2.  Если в объекте `TinyStory` задан агент (`self.agent`), то вызывает метод `pretty_current_interactions` агента для получения информации о его взаимодействиях и добавляет эту информацию в `interaction_history`.
3.  Если в объекте `TinyStory` задано окружение (`self.environment`), то вызывает метод `pretty_current_interactions` окружения для получения информации о его взаимодействиях и добавляет эту информацию в `interaction_history`.
4.  Добавляет информацию о новых взаимодействиях в атрибут `current_story` объекта `TinyStory`.
5.  Возвращает текущую историю (`self.current_story`).

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.agent import TinyPerson
from tinytroupe.steering.tiny_story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Explore the environment")

# Получаем текущую историю
current_story = story._current_story()
print(current_story)

# Пример инициализации с агентом
agent = TinyPerson()
story = TinyStory(agent=agent, purpose="Follow the agent's journey")

# Получаем текущую историю
current_story = story._current_story()
print(current_story)