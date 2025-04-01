# Модуль для создания историй в TinyTroupe

## Обзор

Модуль `story.py` предназначен для создания историй на основе симуляций в TinyTroupe. Он предоставляет класс `TinyStory`, который помогает в создании подходящих историй, учитывая окружение и агентов.

## Подробнее

Этот модуль предоставляет механизмы для создания историй, связанных с симуляциями, позволяя задавать цели и контекст. Он использует информацию об окружении и агентах для генерации интересных и реалистичных историй.

## Классы

### `TinyStory`

**Описание**: Класс для создания историй на основе симуляций TinyTroupe.

**Принцип работы**:
Класс инициализируется с окружением или агентом, целью истории и контекстом. Он использует OpenAI для генерации начала и продолжения истории, основываясь на текущих взаимодействиях в симуляции.

**Атрибуты**:

- `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
- `agent` (TinyPerson, optional): Агент, о котором рассказывается история. По умолчанию `None`.
- `purpose` (str, optional): Цель истории. По умолчанию `"Be a realistic simulation."`.
- `context` (str, optional): Текущий контекст истории. По умолчанию `""`.
- `first_n` (int, optional): Количество первых взаимодействий, включаемых в историю. По умолчанию `10`.
- `last_n` (int, optional): Количество последних взаимодействий, включаемых в историю. По умолчанию `20`.
- `include_omission_info` (bool, optional): Включать ли информацию об опущенных взаимодействиях. По умолчанию `True`.

**Методы**:

- `__init__`: Инициализирует объект истории.
- `start_story`: Начинает новую историю.
- `continue_story`: Предлагает продолжение истории.
- `_current_story`: Возвращает текущую историю.

## Функции

### `__init__`

```python
def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n=10, last_n=20, include_omission_info:bool=True) -> None:
    """
    Инициализирует историю. История может быть об окружении или об агенте. У истории также есть цель, которая
    используется для направления генерации истории. Истории знают, что они связаны с симуляциями, поэтому можно
    указать цели, связанные с симуляцией.

    Args:
        environment (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию None.
        agent (TinyPerson, optional): Агент в истории. По умолчанию None.
        purpose (str, optional): Цель истории. По умолчанию "Be a realistic simulation.".
        context (str, optional): Текущий контекст истории. По умолчанию "". Фактическая история будет добавлена к этому контексту.
        first_n (int, optional): Количество первых взаимодействий, включаемых в историю. По умолчанию 10.
        last_n (int, optional): Количество последних взаимодействий, включаемых в историю. По умолчанию 20.
        include_omission_info (bool, optional): Включать ли информацию об опущенных взаимодействиях. По умолчанию True.

    Raises:
        Exception: Если не предоставлено ни окружение, ни агент, или предоставлены оба одновременно.
    """
    ...
```

**Назначение**: Инициализирует объект `TinyStory`.

**Параметры**:

- `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
- `agent` (TinyPerson, optional): Агент, о котором рассказывается история. По умолчанию `None`.
- `purpose` (str, optional): Цель истории. По умолчанию `"Be a realistic simulation."`.
- `context` (str, optional): Текущий контекст истории. По умолчанию `""`.
- `first_n` (int, optional): Количество первых взаимодействий, включаемых в историю. По умолчанию `10`.
- `last_n` (int, optional): Количество последних взаимодействий, включаемых в историю. По умолчанию `20`.
- `include_omission_info` (bool, optional): Указывает, нужно ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Возвращает**:
- `None`

**Вызывает исключения**:

- `Exception`: Если переданы одновременно и `environment`, и `agent`, или если ни один из них не передан.

**Как работает функция**:

1. Проверяет, передан ли только один из параметров: `environment` или `agent`. Если переданы оба или ни один из них, выбрасывает исключение.
2. Инициализирует атрибуты класса: `environment`, `agent`, `purpose`, `current_story`, `first_n`, `last_n`, `include_omission_info`.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример инициализации с агентом (предположим, что TinyPerson определен в agent.py)
# from tinytroupe.agent import TinyPerson
# agent = TinyPerson()
# story = TinyStory(agent=agent)
```

### `start_story`

```python
def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Начинает новую историю.
    """
    ...
```

**Назначение**: Начинает новую историю, генерируя начальный текст с использованием OpenAI.

**Параметры**:

- `requirements` (str, optional): Требования к началу истории. По умолчанию `"Start some interesting story about the agents."`.
- `number_of_words` (int, optional): Желаемое количество слов в начале истории. По умолчанию `100`.
- `include_plot_twist` (bool, optional): Указывает, нужно ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

- `str`: Начальный текст истории.

**Как работает функция**:

1. Формирует словарь `rendering_configs` с параметрами для генерации истории.
2. Компонует сообщения для языковой модели (LLM) с использованием шаблонов `"story.start.system.mustache"` и `"story.start.user.mustache"`.
3. Отправляет сообщение в OpenAI и получает ответ.
4. Добавляет полученный текст в текущую историю (`self.current_story`).
5. Возвращает начальный текст истории.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример запуска истории
start = story.start_story(requirements="Начни историю о дружбе между агентами", number_of_words=150)
print(start)
```

### `continue_story`

```python
def continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Предлагает продолжение истории.
    """
    ...
```

**Назначение**: Предлагает продолжение истории, генерируя текст продолжения с использованием OpenAI.

**Параметры**:

- `requirements` (str, optional): Требования к продолжению истории. По умолчанию `"Continue the story in an interesting way."`.
- `number_of_words` (int, optional): Желаемое количество слов в продолжении истории. По умолчанию `100`.
- `include_plot_twist` (bool, optional): Указывает, нужно ли включать сюжетный поворот. По умолчанию `False`.

**Возвращает**:

- `str`: Текст продолжения истории.

**Как работает функция**:

1. Формирует словарь `rendering_configs` с параметрами для генерации продолжения истории.
2. Компонует сообщения для языковой модели (LLM) с использованием шаблонов `"story.continuation.system.mustache"` и `"story.continuation.user.mustache"`.
3. Отправляет сообщение в OpenAI и получает ответ.
4. Добавляет полученный текст в текущую историю (`self.current_story`).
5. Возвращает текст продолжения истории.

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.story import TinyStory

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment)

# Пример запуска истории
start = story.start_story(requirements="Начни историю о дружбе между агентами", number_of_words=150)
print(start)

# Пример продолжения истории
continuation = story.continue_story(requirements="Продолжи историю с неожиданным поворотом", number_of_words=120)
print(continuation)
```

### `_current_story`

```python
def _current_story(self) -> str:
    """
    Получает текущую историю.
    """
    ...
```

**Назначение**: Возвращает текущую историю, включая информацию о последних взаимодействиях агента или окружения.

**Параметры**:

- `None`

**Возвращает**:

- `str`: Текущая история с информацией о взаимодействиях.

**Как работает функция**:

1. Проверяет, существует ли агент (`self.agent`). Если да, добавляет информацию о взаимодействиях агента.
2. Если агент не существует, проверяет, существует ли окружение (`self.environment`). Если да, добавляет информацию о взаимодействиях окружения.
3. Добавляет информацию о взаимодействиях в текущую историю (`self.current_story`).
4. Возвращает текущую историю.

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
```
```
```

ASCII flowchart для `start_story`:

```
Начало истории
  |
  V
Формирование rendering_configs
  |
  V
Композиция сообщений для LLM
  |
  V
Отправка сообщения в OpenAI
  |
  V
Добавление текста в current_story
  |
  V
Возврат начального текста
```

ASCII flowchart для `continue_story`:

```
Продолжение истории
  |
  V
Формирование rendering_configs
  |
  V
Композиция сообщений для LLM
  |
  V
Отправка сообщения в OpenAI
  |
  V
Добавление текста в current_story
  |
  V
Возврат текста продолжения
```

ASCII flowchart для `_current_story`:

```
Получение текущей истории
  |
  V
Проверка наличия агента/окружения
  |
  V
Добавление информации о взаимодействиях
  |
  V
Возврат текущей истории