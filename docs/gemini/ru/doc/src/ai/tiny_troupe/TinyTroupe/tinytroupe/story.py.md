# Модуль `story.py`

## Обзор

Модуль `story.py` предназначен для создания и управления рассказами, основанными на симуляциях в TinyTroupe. Он предоставляет классы и методы для генерации сюжетов, которые отражают действия агентов и изменения в среде.

## Оглавление

- [Классы](#классы)
  - [`TinyStory`](#tinystory)
- [Функции](#функции)
  - [`_current_story`](#_current_story)
  - [`start_story`](#start_story)
  - [`continue_story`](#continue_story)

## Классы

### `TinyStory`

**Описание**:
Класс `TinyStory` предназначен для создания и управления рассказами, основанными на симуляциях в TinyTroupe. Он может работать как с агентами, так и с окружениями, позволяя генерировать сюжеты, отражающие их действия и изменения в контексте симуляции.

**Методы**:
- `__init__`: Инициализирует объект `TinyStory`.
- `start_story`: Начинает новый рассказ.
- `continue_story`: Предлагает продолжение рассказа.
- `_current_story`: Получает текущий контекст рассказа, включая историю взаимодействий.

#### `__init__`

```python
def __init__(self, environment:TinyWorld=None, agent:TinyPerson=None, purpose:str="Be a realistic simulation.", context:str="", first_n=10, last_n=20, include_omission_info:bool=True) -> None
```

**Описание**:
Инициализирует объект `TinyStory`.

**Параметры**:
- `environment` (`TinyWorld`, optional): Окружение, в котором происходит рассказ. По умолчанию `None`.
- `agent` (`TinyPerson`, optional): Агент в рассказе. По умолчанию `None`.
- `purpose` (`str`, optional): Цель рассказа. По умолчанию `"Be a realistic simulation."`.
- `context` (`str`, optional): Текущий контекст рассказа. По умолчанию `""`. Фактический рассказ будет добавлен к этому контексту.
- `first_n` (`int`, optional): Количество первых взаимодействий для включения в рассказ. По умолчанию `10`.
- `last_n` (`int`, optional): Количество последних взаимодействий для включения в рассказ. По умолчанию `20`.
- `include_omission_info` (`bool`, optional): Определяет, включать ли информацию об опущенных взаимодействиях. По умолчанию `True`.

**Возвращает**:
- `None`: Метод ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Если не предоставлен ни `environment`, ни `agent` или если предоставлены оба.

## Функции

### `_current_story`

```python
def _current_story(self) -> str
```

**Описание**:
Возвращает текущий контекст рассказа, включая историю взаимодействий агента или окружения.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TinyStory`.

**Возвращает**:
- `str`: Текущий контекст рассказа, включая историю взаимодействий.

### `start_story`

```python
def start_story(self, requirements="Start some interesting story about the agents.", number_of_words:int=100, include_plot_twist:bool=False) -> str
```

**Описание**:
Начинает новый рассказ, генерируя начальный фрагмент на основе предоставленных параметров.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TinyStory`.
- `requirements` (`str`, optional): Дополнительные требования к началу рассказа. По умолчанию `"Start some interesting story about the agents."`.
- `number_of_words` (`int`, optional): Ожидаемое количество слов в начале рассказа. По умолчанию `100`.
- `include_plot_twist` (`bool`, optional): Определяет, нужно ли включать неожиданный поворот в начале рассказа. По умолчанию `False`.

**Возвращает**:
- `str`: Начальный фрагмент рассказа.

### `continue_story`

```python
def continue_story(self, requirements="Continue the story in an interesting way.", number_of_words:int=100, include_plot_twist:bool=False) -> str
```

**Описание**:
Предлагает продолжение текущего рассказа, генерируя следующий фрагмент на основе предоставленных параметров.

**Параметры**:
- `self`: Ссылка на экземпляр класса `TinyStory`.
- `requirements` (`str`, optional): Дополнительные требования к продолжению рассказа. По умолчанию `"Continue the story in an interesting way."`.
- `number_of_words` (`int`, optional): Ожидаемое количество слов в продолжении рассказа. По умолчанию `100`.
- `include_plot_twist` (`bool`, optional): Определяет, нужно ли включать неожиданный поворот в продолжении рассказа. По умолчанию `False`.

**Возвращает**:
- `str`: Следующий фрагмент рассказа.