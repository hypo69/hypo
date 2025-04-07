# Модуль тестирования TinyStory

## Обзор

Модуль `test_story.py` содержит набор модульных тестов для класса `TinyStory`, который отвечает за генерацию и продолжение историй с использованием заданной модели мира (world). Модуль тестирует основные функции `TinyStory`, такие как начало и продолжение истории, с использованием различных входных данных и требований.

## Подробнее

Модуль использует `pytest` для организации и запуска тестов. Он проверяет, что сгенерированные начала и продолжения историй соответствуют заданным критериям и требованиям, используя функцию `proposition_holds` для оценки правдоподобности предложений с помощью языковой модели.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `test_story_start`

```python
def test_story_start(setup, focus_group_world):
    """Тестирует функцию начала истории `start_story` класса `TinyStory`.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура, предоставляющая экземпляр мира (`world`) для тестирования.

    Returns:
        None

    Raises:
        AssertionError: Если сгенерированное начало истории не соответствует ожидаемому.

    Example:
        Пример вызова:
        test_story_start(setup, focus_group_world)
    """
    # Получение мира из фикстуры
    world = focus_group_world

    # Создание экземпляра TinyStory
    story = TinyStory(world)

    # Запуск истории
    start = story.start_story()

    # Вывод начала истории в консоль
    print("Story start: ", start)

    # Проверка, что сгенерированное начало истории правдоподобно
    assert proposition_holds(f"The following could plausibly be the start of a story involving people named either Lisa, Marcos or Oscar: '{start}'"), f"Proposition is false according to the LLM."
```

**Как работает функция**:

1.  **Получение мира**: Из фикстуры `focus_group_world` извлекается экземпляр мира, который будет использоваться для создания истории.
2.  **Создание экземпляра TinyStory**: Создается экземпляр класса `TinyStory`, которому передается мир.
3.  **Запуск истории**: Вызывается метод `start_story()` для генерации начала истории.
4.  **Вывод в консоль**: Сгенерированное начало истории выводится в консоль для отладки.
5.  **Проверка правдоподобности**: Используется функция `proposition_holds` для проверки, что сгенерированное начало истории правдоподобно и соответствует заданным критериям (в данном случае, что в истории упоминаются имена Lisa, Marcos или Oscar).

**ASCII flowchart**:

```
Получение мира из фикстуры
    │
    ▼
Создание экземпляра TinyStory
    │
    ▼
Запуск истории (story.start_story())
    │
    ▼
Вывод начала истории в консоль
    │
    ▼
Проверка правдоподобности (proposition_holds)
```

### `test_story_start_2`

```python
def test_story_start_2(setup, focus_group_world):
    """Тестирует функцию начала истории `start_story` класса `TinyStory` с дополнительными требованиями.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура, предоставляющая экземпляр мира (`world`) для тестирования.

    Returns:
        None

    Raises:
        AssertionError: Если сгенерированное начало истории не соответствует ожидаемому.

    Example:
        Пример вызова:
        test_story_start_2(setup, focus_group_world)
    """
    # Получение мира из фикстуры
    world = focus_group_world

    # Создание экземпляра TinyStory
    story = TinyStory(world)

    # Запуск истории с требованием
    start = story.start_story(requirements="Start a story which is extremely crazy and out of this world.")

    # Вывод начала истории в консоль
    print("Story start: ", start)

    # Проверка, что сгенерированное начало истории соответствует требованию
    assert proposition_holds(f"The following could plausibly be the start of a very crazy story involving people named either Lisa, Marcos or Oscar: '{start}'"), f"Proposition is false according to the LLM."
```

**Как работает функция**:

1.  **Получение мира**: Из фикстуры `focus_group_world` извлекается экземпляр мира, который будет использоваться для создания истории.
2.  **Создание экземпляра TinyStory**: Создается экземпляр класса `TinyStory`, которому передается мир.
3.  **Запуск истории с требованием**: Вызывается метод `start_story()` с аргументом `requirements`, который задает требование к истории быть "extremely crazy and out of this world".
4.  **Вывод в консоль**: Сгенерированное начало истории выводится в консоль для отладки.
5.  **Проверка правдоподобности**: Используется функция `proposition_holds` для проверки, что сгенерированное начало истории правдоподобно и соответствует заданным критериям (в данном случае, что история является "crazy" и в ней упоминаются имена Lisa, Marcos или Oscar).

**ASCII flowchart**:

```
Получение мира из фикстуры
    │
    ▼
Создание экземпляра TinyStory
    │
    ▼
Запуск истории с требованием (story.start_story(requirements))
    │
    ▼
Вывод начала истории в консоль
    │
    ▼
Проверка правдоподобности (proposition_holds)
```

### `test_story_continuation`

```python
def test_story_continuation(setup, focus_group_world):
    """Тестирует функцию продолжения истории `continue_story` класса `TinyStory`.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура, предоставляющая экземпляр мира (`world`) для тестирования.

    Returns:
        None

    Raises:
        AssertionError: Если сгенерированное продолжение истории не соответствует ожидаемому.

    Example:
        Пример вызова:
        test_story_continuation(setup, focus_group_world)
    """
    # Получение мира из фикстуры
    world = focus_group_world

    # Начало истории
    story_beginning = \
        """
          You were vacationing in the beautiful city of Rio de Janeiro, Brazil. You were walking down the beach when
          the most unexpected thing happened: an Alien spaceship landed right in front of you. The door opened and a
          friendly Alien stepped out. The Alien introduced itself as Zog, and explained that it was on a mission to
          learn more about Earth's cultures. You were intrigued by this encounter and decided to help Zog in its mission.
        """

    # Распространение начала истории в мире
    world.broadcast(story_beginning)

    # Запуск мира на несколько шагов
    world.run(2)

    # Создание экземпляра TinyStory
    story = TinyStory(world)

    # Получение продолжения истории
    continuation = story.continue_story()

    # Вывод продолжения истории в консоль
    print("Story continuation: ", continuation)

    # Проверка, что продолжение истории соответствует началу истории
    assert proposition_holds(f"The following two text blocks could belong to the same story: \n BLOCK 1: '{story_beginning}' and \n BLOCK 2: '{continuation}'"), f"Proposition is false according to the LLM."
```

**Как работает функция**:

1.  **Получение мира**: Из фикстуры `focus_group_world` извлекается экземпляр мира, который будет использоваться для создания истории.
2.  **Определение начала истории**: Задается начало истории в виде строки.
3.  **Распространение начала истории в мире**: Начало истории передается в мир с помощью метода `world.broadcast()`.
4.  **Запуск мира на несколько шагов**: Мир запускается на несколько шагов с помощью метода `world.run()`, чтобы учесть изменения в мире.
5.  **Создание экземпляра TinyStory**: Создается экземпляр класса `TinyStory`, которому передается мир.
6.  **Получение продолжения истории**: Вызывается метод `continue_story()` для генерации продолжения истории.
7.  **Вывод в консоль**: Сгенерированное продолжение истории выводится в консоль для отладки.
8.  **Проверка соответствия**: Используется функция `proposition_holds` для проверки, что сгенерированное продолжение истории соответствует началу истории.

**ASCII flowchart**:

```
Получение мира из фикстуры
    │
    ▼
Определение начала истории
    │
    ▼
Распространение начала истории в мире (world.broadcast())
    │
    ▼
Запуск мира на несколько шагов (world.run())
    │
    ▼
Создание экземпляра TinyStory
    │
    ▼
Получение продолжения истории (story.continue_story())
    │
    ▼
Вывод продолжения истории в консоль
    │
    ▼
Проверка соответствия (proposition_holds)
```