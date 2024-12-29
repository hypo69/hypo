# Модуль `story`

## Обзор

Модуль `story` предоставляет механизмы для создания историй на основе симуляций в TinyTroupe. Он позволяет формировать сюжеты вокруг окружения или агентов, задавая цели и используя историю взаимодействий для генерации текста.

## Содержание

- [Классы](#классы)
    - [`TinyStory`](#tinystory)
- [Функции](#функции)
    - [`start_story`](#start_story)
    - [`continue_story`](#continue_story)
    - [`_current_story`](#_current_story)

## Классы

### `TinyStory`

**Описание**: Класс для создания и управления историями, основанными на симуляциях. Он может генерировать истории, используя информацию об окружении и/или агентах.

**Методы**:
- `__init__`: Инициализирует объект `TinyStory`.
- `start_story`: Начинает новую историю.
- `continue_story`: Продолжает существующую историю.
- `_current_story`: Возвращает текущую историю, включая историю взаимодействия.

#### `__init__`

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

        Raises:
            Exception: Если не передан ни `environment`, ни `agent`, или переданы оба.
        """
```
**Описание**: Инициализирует объект `TinyStory`. История может быть связана либо с окружением, либо с агентом. Также задается цель истории, которая используется для направления ее генерации.

**Параметры**:
- `environment` (TinyWorld, optional): Окружение, в котором происходит история. По умолчанию `None`.
- `agent` (TinyPerson, optional): Агент, участвующий в истории. По умолчанию `None`.
- `purpose` (str, optional): Цель истории. По умолчанию `"Be a realistic simulation."`.
- `context` (str, optional): Текущий контекст истории. По умолчанию `""`. Фактическая история будет добавлена к этому контексту.
- `first_n` (int, optional): Количество первых взаимодействий, которые будут включены в историю. По умолчанию `10`.
- `last_n` (int, optional): Количество последних взаимодействий, которые будут включены в историю. По умолчанию `20`.
- `include_omission_info` (bool, optional): Определяет, нужно ли включать информацию об опущенных взаимодействиях. По умолчанию `True`.

**Вызывает исключения**:
- `Exception`: Если не передан ни `environment`, ни `agent`, или если переданы оба параметра одновременно.

## Функции

### `start_story`

```python
    def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
        """
        Start a new story.
        """
```

**Описание**: Начинает новую историю, используя заданные требования.

**Параметры**:
- `requirements` (str, optional): Требования к началу истории. По умолчанию `"Start some interesting story about the agents."`.
- `number_of_words` (int, optional): Количество слов в начале истории. По умолчанию `100`.
- `include_plot_twist` (bool, optional): Определяет, нужно ли включить сюжетный поворот. По умолчанию `False`.

**Возвращает**:
- `str`: Начало истории.

### `continue_story`

```python
    def continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str:
        """
        Propose a continuation of the story.
        """
```

**Описание**: Предлагает продолжение текущей истории.

**Параметры**:
- `requirements` (str, optional): Требования к продолжению истории. По умолчанию `"Continue the story in an interesting way."`.
- `number_of_words` (int, optional): Количество слов в продолжении истории. По умолчанию `100`.
- `include_plot_twist` (bool, optional): Определяет, нужно ли включить сюжетный поворот. По умолчанию `False`.

**Возвращает**:
- `str`: Продолжение истории.

### `_current_story`

```python
    def _current_story(self) -> str:
        """
        Get the current story.
        """
```

**Описание**: Возвращает текущую историю, включая историю взаимодействия агента или окружения.

**Возвращает**:
- `str`: Текущая история.