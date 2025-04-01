# Модуль `tiny_story.py`

## Обзор

Модуль `tiny_story.py` предоставляет класс `TinyStory`, который используется для создания историй на основе симуляций, проводимых в TinyTroupe. Он предоставляет механизмы для формирования историй об окружении или агентах, участвующих в симуляции. Класс позволяет задавать цели для генерации истории, учитывать контекст, а также включать информацию об опущенных взаимодействиях.

## Подробнее

Этот модуль играет важную роль в создании нарратива вокруг симуляций TinyTroupe. Он позволяет представить результаты симуляций в виде интересных историй, что может быть полезно для анализа и визуализации данных.

## Классы

### `TinyStory`

**Описание**: Класс `TinyStory` предназначен для создания и управления историями, основанными на симуляциях TinyTroupe. Он предоставляет функциональность для инициализации истории, её начала и продолжения, а также для получения текущего состояния истории.

**Принцип работы**:

1.  Класс инициализируется с указанием либо окружения (`TinyWorld`), либо агента (`TinyPerson`), на основе которого будет строиться история.
2.  Задается цель истории (`purpose`), которая будет использоваться для направления генерации текста.
3.  Метод `start_story` начинает новую историю, генерируя текст на основе предоставленных требований и текущего контекста симуляции.
4.  Метод `continue_story` продолжает существующую историю, добавляя новые элементы сюжета.
5.  Метод `_current_story` формирует текущий контекст истории, включая информацию о последних взаимодействиях агента или окружения.

**Аттрибуты**:

*   `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
*   `agent` (TinyPerson, optional): Агент, участвующий в истории. По умолчанию `None`.
*   `purpose` (str, optional): Цель истории. По умолчанию "Be a realistic simulation.".
*   `current_story` (str, optional): Текущий контекст истории. По умолчанию "".
*   `first_n` (int, optional): Количество первых взаимодействий для включения в историю. По умолчанию 10.
*   `last_n` (int, optional): Количество последних взаимодействий для включения в историю. По умолчанию 20.
*   `include_omission_info` (bool, optional): Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Методы**:

*   `__init__`: Инициализирует объект `TinyStory`.
*   `start_story`: Начинает новую историю.
*   `continue_story`: Продолжает существующую историю.
*   `_current_story`: Получает текущий контекст истории.

## Функции

### `__init__`

```python
def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="",
                 first_n=10, last_n=20, include_omission_info:bool=True) -> None:
    """
    Every simulation tells a story. This class provides helper mechanisms to help with crafting appropriate stories in TinyTroupe.
    """
```

**Назначение**: Инициализирует экземпляр класса `TinyStory`.

**Параметры**:

*   `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
*   `agent` (TinyPerson, optional): Агент, участвующий в истории. По умолчанию `None`.
*   `purpose` (str, optional): Цель истории. По умолчанию "Be a realistic simulation.".
*   `context` (str, optional): Начальный контекст истории. По умолчанию "".
*   `first_n` (int, optional): Количество первых взаимодействий для включения в историю. По умолчанию 10.
*   `last_n` (int, optional): Количество последних взаимодействий для включения в историю. По умолчанию 20.
*   `include_omission_info` (bool, optional): Флаг, указывающий, следует ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Возвращает**:
*   `None`

**Вызывает исключения**:

*   `Exception`: Если одновременно предоставлены и `environment`, и `agent`, или если не предоставлен ни один из них.

**Как работает функция**:

1.  Проверяет, что предоставлен либо `environment`, либо `agent`, но не оба одновременно, и что хотя бы один из них предоставлен. Если условия не соблюдены, вызывает исключение.
2.  Инициализирует атрибуты класса значениями, переданными в качестве аргументов.

```
Проверка наличия environment и agent -> Установка атрибутов класса
     |
     V
   [ environment и agent одновременно? ] -- Да --> Вызов исключения
     |Нет
     V
   [ environment или agent? ] -- Нет --> Вызов исключения
     |Да
     V
   Установка атрибутов класса
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld
from tinytroupe.agent import TinyPerson

# Пример инициализации с окружением
environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Исследование мира")

# Пример инициализации с агентом
agent = TinyPerson()
story = TinyStory(agent=agent, purpose="Развитие персонажа")
```

### `start_story`

```python
def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Start a new story.
    """
```

**Назначение**: Начинает новую историю, генерируя начальный текст на основе предоставленных требований и текущего контекста симуляции.

**Параметры**:

*   `requirements` (str, optional): Требования к началу истории. По умолчанию "Start some interesting story about the agents.".
*   `number_of_words` (int, optional): Количество слов в сгенерированном тексте. По умолчанию 100.
*   `include_plot_twist` (bool, optional): Флаг, указывающий, следует ли включать неожиданный поворот сюжета. По умолчанию `False`.

**Возвращает**:

*   `str`: Начальный текст истории.

**Как работает функция**:

1.  Формирует словарь `rendering_configs`, содержащий параметры для генерации текста, такие как цель истории, требования, текущий контекст симуляции, количество слов и флаг включения неожиданного поворота сюжета.
2.  Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для языковой модели (LLM) на основе шаблонов "story.start.system.mustache" и "story.start.user.mustache".
3.  Отправляет сообщения в языковую модель с помощью `openai_utils.client().send_message` и получает сгенерированный текст.
4.  Добавляет сгенерированный текст в текущий контекст истории (`self.current_story`).
5.  Возвращает сгенерированный текст.

```
Формирование rendering_configs -> Создание сообщений для LLM -> Отправка сообщений в LLM -> Добавление текста в current_story -> Возврат текста
     |
     V
   Формирование rendering_configs
     |
     V
   Создание сообщений для LLM
     |
     V
   Отправка сообщений в LLM
     |
     V
   Добавление текста в current_story
     |
     V
   Возврат текста
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld

environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Исследование мира")

# Пример начала истории
start_text = story.start_story(requirements="Описание первого дня в новом мире", number_of_words=150)
print(start_text)
```

### `continue_story`

```python
def continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
    """
    Propose a continuation of the story.
    """
```

**Назначение**: Предлагает продолжение истории, генерируя текст на основе предоставленных требований и текущего контекста симуляции.

**Параметры**:

*   `requirements` (str, optional): Требования к продолжению истории. По умолчанию "Continue the story in an interesting way.".
*   `number_of_words` (int, optional): Количество слов в сгенерированном тексте. По умолчанию 100.
*   `include_plot_twist` (bool, optional): Флаг, указывающий, следует ли включать неожиданный поворот сюжета. По умолчанию `False`.

**Возвращает**:

*   `str`: Текст продолжения истории.

**Как работает функция**:

1.  Формирует словарь `rendering_configs`, содержащий параметры для генерации текста, такие как цель истории, требования, текущий контекст симуляции, количество слов и флаг включения неожиданного поворота сюжета.
2.  Использует функцию `utils.compose_initial_LLM_messages_with_templates` для создания сообщений для языковой модели (LLM) на основе шаблонов "story.continuation.system.mustache" и "story.continuation.user.mustache".
3.  Отправляет сообщения в языковую модель с помощью `openai_utils.client().send_message` и получает сгенерированный текст.
4.  Добавляет сгенерированный текст в текущий контекст истории (`self.current_story`).
5.  Возвращает сгенерированный текст.

```
Формирование rendering_configs -> Создание сообщений для LLM -> Отправка сообщений в LLM -> Добавление текста в current_story -> Возврат текста
     |
     V
   Формирование rendering_configs
     |
     V
   Создание сообщений для LLM
     |
     V
   Отправка сообщений в LLM
     |
     V
   Добавление текста в current_story
     |
     V
   Возврат текста
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld

environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Исследование мира")

# Начало истории
story.start_story(requirements="Описание первого дня в новом мире", number_of_words=150)

# Продолжение истории
continuation_text = story.continue_story(requirements="Нахождение таинственного артефакта", number_of_words=120)
print(continuation_text)
```

### `_current_story`

```python
def _current_story(self) -> str:
    """
    Get the current story.
    """
```

**Назначение**: Получает текущий контекст истории, включая информацию о последних взаимодействиях агента или окружения.

**Параметры**:

*   `self` (TinyStory): Экземпляр класса `TinyStory`.

**Возвращает**:

*   `str`: Текущий контекст истории.

**Как работает функция**:

1.  Инициализирует переменную `interaction_history` пустой строкой.
2.  Проверяет, предоставлен ли агент (`self.agent`). Если да, то добавляет в `interaction_history` информацию о последних взаимодействиях агента, полученную с помощью метода `self.agent.pretty_current_interactions`.
3.  Если агент не предоставлен, проверяет, предоставлено ли окружение (`self.environment`). Если да, то добавляет в `interaction_history` информацию о последних взаимодействиях окружения, полученную с помощью метода `self.environment.pretty_current_interactions`.
4.  Добавляет информацию о новых взаимодействиях в текущий контекст истории (`self.current_story`).
5.  Возвращает текущий контекст истории.

```
Инициализация interaction_history -> Проверка наличия agent -> Добавление информации о взаимодействиях agent (если есть) -> Проверка наличия environment -> Добавление информации о взаимодействиях environment (если есть) -> Добавление информации в current_story -> Возврат current_story
     |
     V
   Инициализация interaction_history
     |
     V
   Проверка наличия agent
     |
   [ agent? ] -- Да --> Добавление информации о взаимодействиях agent
     |Нет
     V
   Проверка наличия environment
     |
   [ environment? ] -- Да --> Добавление информации о взаимодействиях environment
     |Нет
     V
   Добавление информации в current_story
     |
     V
   Возврат current_story
```

**Примеры**:

```python
from tinytroupe.environment import TinyWorld

environment = TinyWorld()
story = TinyStory(environment=environment, purpose="Исследование мира")

# Получение текущего контекста истории
current_context = story._current_story()
print(current_context)