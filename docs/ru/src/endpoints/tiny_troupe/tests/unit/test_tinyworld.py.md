# Модуль тестирования `test_tinyworld.py`

## Обзор

Модуль содержит юнит-тесты для проверки функциональности виртуального мира (`TinyWorld`) и его взаимодействия с агентами. Включает тесты для запуска мира, широковещательных сообщений, кодирования и декодирования состояния мира.

## Подробней

Этот модуль предназначен для тестирования основных функций `TinyWorld`, таких как инициализация, запуск симуляции, отправка сообщений агентам и сохранение/восстановление состояния мира. Он использует `pytest` для организации тестов и включает проверку целостности сообщений и состояний агентов.

## Функции

### `test_run`

```python
def test_run(setup, focus_group_world):
    """
    Тестирует запуск виртуального мира с агентами и без них.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура pytest, представляющая виртуальный мир с агентами.

    Raises:
        AssertionError: Если целевой агент совпадает с отправителем.

    Как работает функция:
    1. Создание пустого мира (`world_1`) и запуск симуляции на 2 шага.
    2. Создание мира с агентами (`world_2`), отправка широковещательного сообщения и запуск симуляции на 2 шага.
    3. Проверка целостности переписки агентов:
       - Убедимся, что в сообщениях нет ситуаций, когда агент взаимодействует сам с собой.

    ASCII flowchart:

    Создание пустого мира --> Запуск симуляции
        |
        V
    Создание мира с агентами --> Отправка широковещательного сообщения --> Запуск симуляции
        |
        V
    Проверка целостности сообщений

    Примеры:
    ```python
    # Запуск теста (пример)
    test_run(setup, focus_group_world)
    ```
    """
    # empty world
    world_1 = TinyWorld("Empty land", [])   
    world_1.run(2)

    # world with agents
    world_2 = focus_group_world
    world_2.broadcast("Discuss ideas for a new AI product you\'d love to have.")
    world_2.run(2)

    # check integrity of conversation
    for agent in world_2.agents:
        for msg in agent.episodic_memory.retrieve_all():
            if 'action' in msg['content'] and 'target' in msg['content']['action']:
                assert msg['content']['action']['target'] != agent.name, f"{agent.name} should not have any messages with itself as the target."
            
            # TODO stimulus integrity check?
```

### `test_broadcast`

```python
def test_broadcast(setup, focus_group_world):
    """
    Тестирует рассылку сообщений агентам в виртуальном мире.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура pytest, представляющая виртуальный мир с агентами.

    Raises:
        AssertionError: Если агенты не получили широковещательное сообщение.

    Как работает функция:
    1. Получение мира с агентами.
    2. Отправка широковещательного сообщения всем агентам.
    3. Проверка, что каждый агент получил сообщение и сохранил его в своей эпизодической памяти.

    ASCII flowchart:

    Получение мира с агентами --> Отправка широковещательного сообщения
        |
        V
    Проверка получения сообщения каждым агентом

    Примеры:
    ```python
    # Запуск теста (пример)
    test_broadcast(setup, focus_group_world)
    ```
    """
    world = focus_group_world
    world.broadcast("""
                Folks, we need to brainstorm ideas for a new baby product. Something moms have been asking for centuries and never got.

                Please start the discussion now.
                """)
    
    for agent in focus_group_world.agents:
        # did the agents receive the message?
        assert "Folks, we need to brainstorm" in agent.episodic_memory.retrieve_first(1)[0]['content']['stimuli'][0]['content'], f"{agent.name} should have received the message."
```

### `test_encode_complete_state`

```python
def test_encode_complete_state(setup, focus_group_world):
    """
    Тестирует кодирование полного состояния виртуального мира.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура pytest, представляющая виртуальный мир с агентами.

    Raises:
        AssertionError: Если состояние мира не было закодировано или не содержит необходимой информации (имя мира, агенты).

    Как работает функция:
    1. Получение мира с агентами.
    2. Кодирование полного состояния мира.
    3. Проверка, что закодированное состояние не `None` и содержит имя мира и агентов.

    ASCII flowchart:

    Получение мира с агентами --> Кодирование состояния мира
        |
        V
    Проверка наличия имени мира и агентов в закодированном состоянии

    Примеры:
    ```python
    # Запуск теста (пример)
    test_encode_complete_state(setup, focus_group_world)
    ```
    """
    world = focus_group_world

    # encode the state
    state = world.encode_complete_state()
    
    assert state is not None, "The state should not be None."
    assert state['name'] == world.name, "The state should have the world name."
    assert state['agents'] is not None, "The state should have the agents."
```

### `test_decode_complete_state`

```python
def test_decode_complete_state(setup, focus_group_world):
    """
    Тестирует декодирование полного состояния виртуального мира.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
        focus_group_world: Фикстура pytest, представляющая виртуальный мир с агентами.

    Raises:
        AssertionError: Если мир не был декодирован или не содержит ожидаемую информацию (имя мира, агенты).

    Как работает функция:
    1. Получение мира с агентами.
    2. Запоминание исходного имени мира и количества агентов.
    3. Кодирование состояния мира.
    4. Изменение имени мира и очистка списка агентов.
    5. Декодирование состояния мира обратно.
    6. Проверка, что декодированный мир имеет исходное имя и содержит исходное количество агентов.

    ASCII flowchart:

    Получение мира с агентами --> Запоминание имени и числа агентов --> Кодирование состояния мира
        |
        V
    Изменение имени мира и очистка списка агентов --> Декодирование состояния мира
        |
        V
    Проверка соответствия исходным данным

    Примеры:
    ```python
    # Запуск теста (пример)
    test_decode_complete_state(setup, focus_group_world)
    ```
    """
    world = focus_group_world

    name_1 = world.name
    n_agents_1 = len(world.agents)

    # encode the state
    state = world.encode_complete_state()
    
    # screw up the world
    world.name = "New name"
    world.agents = []

    # decode the state back into the world
    world_2 = world.decode_complete_state(state)

    assert world_2 is not None, "The world should not be None."
    assert world_2.name == name_1, "The world should have the same name."
    assert len(world_2.agents) == n_agents_1, "The world should have the same number of agents."