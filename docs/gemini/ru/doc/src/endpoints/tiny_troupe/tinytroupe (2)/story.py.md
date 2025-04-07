# Модуль для создания историй в TinyTroupe

## Обзор

Модуль `story.py` предоставляет механизмы для создания историй на основе симуляций в TinyTroupe. Он содержит класс `TinyStory`, который позволяет генерировать и продолжать истории, учитывая окружение и агентов.

## Подробнее

Этот модуль помогает создавать интересные и реалистичные истории, основанные на данных симуляций. Он использует шаблоны и OpenAI для генерации текста, который может быть использован для визуализации или анализа поведения агентов в симуляции. Модуль особенно полезен для создания контекста и повествования вокруг автоматизированных симуляций.

## Классы

### `TinyStory`

**Описание**: Класс для создания и управления историями, основанными на симуляциях TinyTroupe.

**Принцип работы**: Класс инициализируется либо с окружением (`TinyWorld`), либо с агентом (`TinyPerson`). Он использует эти данные для создания и продолжения истории, генерируя текст с помощью OpenAI.

**Атрибуты**:

- `environment (TinyWorld, optional)`: Окружение, в котором происходит история. По умолчанию `None`.
- `agent (TinyPerson, optional)`: Агент, о котором рассказывается история. По умолчанию `None`.
- `purpose (str, optional)`: Цель истории. Используется для направления генерации истории. По умолчанию `"Be a realistic simulation."`.
- `context (str, optional)`: Текущий контекст истории. По умолчанию `""`.
- `first_n (int, optional)`: Количество первых взаимодействий для включения в историю. По умолчанию `10`.
- `last_n (int, optional)`: Количество последних взаимодействий для включения в историю. По умолчанию `20`.
- `include_omission_info (bool, optional)`: Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.
- `current_story (str)`: Текущая история.

**Методы**:

- `__init__(environment: TinyWorld = None, agent: TinyPerson = None, purpose: str = "Be a realistic simulation.", context: str = "", first_n: int = 10, last_n: int = 20, include_omission_info: bool = True) -> None`: Инициализирует экземпляр класса `TinyStory`.
- `start_story(requirements: str = "Start some interesting story about the agents.", number_of_words: int = 100, include_plot_twist: bool = False) -> str`: Начинает новую историю.
- `continue_story(requirements: str = "Continue the story in an interesting way.", number_of_words: int = 100, include_plot_twist: bool = False) -> str`: Предлагает продолжение истории.
- `_current_story() -> str`: Возвращает текущую историю.

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

**Назначение**: Инициализация объекта `TinyStory`.

**Параметры**:

- `environment (TinyWorld, optional)`: Окружение, в котором происходит история. По умолчанию `None`.
- `agent (TinyPerson, optional)`: Агент, о котором рассказывается история. По умолчанию `None`.
- `purpose (str, optional)`: Цель истории. Используется для направления генерации истории. По умолчанию `"Be a realistic simulation."`.
- `context (str, optional)`: Текущий контекст истории. По умолчанию `""`.
- `first_n (int, optional)`: Количество первых взаимодействий для включения в историю. По умолчанию `10`.
- `last_n (int, optional)`: Количество последних взаимодействий для включения в историю. По умолчанию `20`.
- `include_omission_info (bool, optional)`: Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `Exception`: Если одновременно предоставлены `environment` и `agent` или если не предоставлен ни один из них.

**Как работает функция**:

1. Проверяет, что предоставлен либо `environment`, либо `agent`, но не оба сразу.
2. Инициализирует атрибуты объекта `TinyStory` значениями, переданными в параметрах.
3. Устанавливает цель истории, контекст, количество первых и последних взаимодействий для включения, а также флаг включения информации об опущенных взаимодействиях.

```
Проверка параметров -> Инициализация атрибутов класса
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример инициализации с агентом
from tinytroupe.agent import TinyPerson
agent = TinyPerson()
story = TinyStory(agent=agent)
```

### `start_story`

```python
def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Start a new story.
    """
    ...
```

**Назначение**: Начинает новую историю, генерируя текст с помощью OpenAI на основе предоставленных требований и текущего контекста симуляции.

**Параметры**:

- `requirements (str, optional)`: Дополнительные требования к началу истории. По умолчанию `"Start some interesting story about the agents."`.
- `number_of_words (int, optional)`: Количество слов в сгенерированном тексте. По умолчанию `100`.
- `include_plot_twist (bool, optional)`: Флаг, указывающий, следует ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

- `str`: Сгенерированный текст начала истории.

**Как работает функция**:

1. Создает словарь `rendering_configs` с параметрами для генерации истории, такими как цель, требования, текущий контекст симуляции, количество слов и флаг сюжетного поворота.
2. Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для языковой модели (LLM) на основе шаблонов.
3. Отправляет сообщения в OpenAI для генерации текста начала истории.
4. Добавляет сгенерированный текст к текущей истории.

```
Создание rendering_configs -> Создание сообщений для LLM -> Отправка сообщений в OpenAI -> Добавление текста к current_story
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример начала истории
start = story.start_story()
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

**Назначение**: Предлагает продолжение истории, генерируя текст с помощью OpenAI на основе предоставленных требований и текущего контекста истории.

**Параметры**:

- `requirements (str, optional)`: Дополнительные требования к продолжению истории. По умолчанию `"Continue the story in an interesting way."`.
- `number_of_words (int, optional)`: Количество слов в сгенерированном тексте. По умолчанию `100`.
- `include_plot_twist (bool, optional)`: Флаг, указывающий, следует ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

- `str`: Сгенерированный текст продолжения истории.

**Как работает функция**:

1. Создает словарь `rendering_configs` с параметрами для генерации истории, такими как цель, требования, текущий контекст симуляции, количество слов и флаг сюжетного поворота.
2. Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для языковой модели (LLM) на основе шаблонов.
3. Отправляет сообщения в OpenAI для генерации текста продолжения истории.
4. Добавляет сгенерированный текст к текущей истории.

```
Создание rendering_configs -> Создание сообщений для LLM -> Отправка сообщений в OpenAI -> Добавление текста к current_story
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример начала истории
start = story.start_story()

# Пример продолжения истории
continuation = story.continue_story()
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

**Назначение**: Возвращает текущую историю, включая информацию о взаимодействиях агента или окружения.

**Параметры**:

- `None`

**Возвращает**:

- `str`: Текущая история.

**Как работает функция**:

1. Инициализирует переменную `interaction_history` пустой строкой.
2. Если в объекте `TinyStory` задан агент, добавляет в `interaction_history` информацию о его взаимодействиях.
3. Если в объекте `TinyStory` задано окружение, добавляет в `interaction_history` информацию о его взаимодействиях.
4. Добавляет `interaction_history` к текущей истории.

```
Инициализация interaction_history -> Проверка agent -> Добавление взаимодействий агента (если есть) -> Проверка environment -> Добавление взаимодействий окружения (если есть) -> Добавление interaction_history к current_story
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример получения текущей истории
current_story = story._current_story()
print(current_story)