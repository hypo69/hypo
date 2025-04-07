# Модуль `environment.py`

## Обзор

Модуль `environment.py` предоставляет классы для моделирования окружения, в котором взаимодействуют агенты, а также внешние сущности. Он содержит базовый класс `TinyWorld`, представляющий собой абстрактное окружение, и класс `TinySocialNetwork`, расширяющий `TinyWorld` для моделирования социальных сетей.

## Подробнее

Этот модуль играет центральную роль в создании симуляций, где агенты взаимодействуют друг с другом и с окружением. Он предоставляет механизмы для управления временем, добавления и удаления агентов, обработки действий агентов и организации коммуникаций между ними. `TinyWorld` служит основой для определения общих правил и логики окружения, в то время как `TinySocialNetwork` добавляет специфические возможности для моделирования социальных связей и отношений между агентами.

## Классы

### `TinyWorld`

**Описание**: Базовый класс для окружений.

**Принцип работы**: `TinyWorld` предоставляет основные методы для управления агентами, временем и взаимодействиями в симулируемой среде. Он содержит логику для выполнения шагов симуляции, обработки действий агентов и организации коммуникаций между ними.

**Атрибуты**:

- `all_environments (dict)`: Словарь, содержащий все созданные окружения (`name -> environment`).
- `communication_display (bool)`: Флаг, определяющий, отображать ли коммуникации в окружении. По умолчанию `True`.
- `name (str)`: Имя окружения.
- `current_datetime (datetime)`: Текущая дата и время в окружении.
- `broadcast_if_no_target (bool)`: Если `True`, действия транслируются, если цель действия не найдена.
- `simulation_id (Any)`: Идентификатор симуляции, к которой принадлежит окружение.
- `agents (list)`: Список агентов в окружении.
- `name_to_agent (dict)`: Словарь, сопоставляющий имена агентов с их экземплярами (`{agent_name: agent}`).
- `_displayed_communications_buffer (list)`: Буфер отображаемых коммуникаций.
- `console (Console)`: Объект консоли для вывода информации.

**Методы**:

- `__init__(self, name: str="A TinyWorld", agents=[], initial_datetime=datetime.datetime.now(), broadcast_if_no_target=True)`:
    Инициализирует окружение.

- `_step(self, timedelta_per_step=None)`:
    Выполняет один шаг в окружении.

- `_advance_datetime(self, timedelta)`:
    Увеличивает текущую дату и время окружения на указанный интервал.

- `run(self, steps: int, timedelta_per_step=None, return_actions=False)`:
    Запускает окружение на заданное количество шагов.

- `skip(self, steps: int, timedelta_per_step=None)`:
    Пропускает заданное количество шагов в окружении без выполнения действий.

- `run_minutes(self, minutes: int)`:
    Запускает окружение на заданное количество минут.

- `skip_minutes(self, minutes: int)`:
    Пропускает заданное количество минут в окружении.

- `run_hours(self, hours: int)`:
    Запускает окружение на заданное количество часов.

- `skip_hours(self, hours: int)`:
    Пропускает заданное количество часов в окружении.

- `run_days(self, days: int)`:
    Запускает окружение на заданное количество дней.

- `skip_days(self, days: int)`:
    Пропускает заданное количество дней в окружении.

- `run_weeks(self, weeks: int)`:
    Запускает окружение на заданное количество недель.

- `skip_weeks(self, weeks: int)`:
    Пропускает заданное количество недель в окружении.

- `run_months(self, months: int)`:
    Запускает окружение на заданное количество месяцев.

- `skip_months(self, months: int)`:
    Пропускает заданное количество месяцев в окружении.

- `run_years(self, years: int)`:
    Запускает окружение на заданное количество лет.

- `skip_years(self, years: int)`:
    Пропускает заданное количество лет в окружении.

- `add_agents(self, agents: list)`:
    Добавляет список агентов в окружение.

- `add_agent(self, agent: TinyPerson)`:
    Добавляет агента в окружение.

- `remove_agent(self, agent: TinyPerson)`:
    Удаляет агента из окружения.

- `remove_all_agents(self)`:
    Удаляет всех агентов из окружения.

- `get_agent_by_name(self, name: str) -> TinyPerson`:
    Возвращает агента с указанным именем.

- `_handle_actions(self, source: TinyPerson, actions: list)`:
    Обрабатывает действия, инициированные агентами.

- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`:
    Обрабатывает действие `REACH_OUT`.

- `_handle_talk(self, source_agent: TinyPerson, content: str, target: str)`:
    Обрабатывает действие `TALK`.

- `broadcast(self, speech: str, source: AgentOrWorld=None)`:
    Отправляет сообщение всем агентам в окружении.

- `broadcast_thought(self, thought: str, source: AgentOrWorld=None)`:
    Отправляет мысль всем агентам в окружении.

- `broadcast_internal_goal(self, internal_goal: str)`:
    Отправляет внутреннюю цель всем агентам в окружении.

- `broadcast_context_change(self, context: list)`:
    Отправляет изменение контекста всем агентам в окружении.

- `make_everyone_accessible(self)`:
    Делает всех агентов в окружении доступными друг для друга.

- `_display_communication(self, cur_step, total_steps, kind, timedelta_per_step=None)`:
    Отображает текущую коммуникацию и сохраняет её в буфере.

- `_push_and_display_latest_communication(self, rendering)`:
    Добавляет последние коммуникации в буфер агента.

- `pop_and_display_latest_communications(self)`:
    Извлекает последние коммуникации и отображает их.

- `_display(self, communication)`:
    Отображает коммуникацию.

- `clear_communications_buffer(self)`:
    Очищает буфер коммуникаций.

- `__repr__(self)`:
    Возвращает строковое представление объекта `TinyWorld`.

- `_pretty_step(self, cur_step, total_steps, timedelta_per_step=None)`:
    Форматирует строку шага симуляции для отображения.

- `pp_current_interactions(self, simplified=True, skip_system=True)`:
    Выводит текущие сообщения от агентов в этом окружении.

- `pretty_current_interactions(self, simplified=True, skip_system=True, max_content_length=default["max_content_display_length"], first_n=None, last_n=None, include_omission_info:bool=True)`:
    Возвращает отформатированную строку с текущими сообщениями агентов в этом окружении.

- `encode_complete_state(self) -> dict`:
    Кодирует полное состояние окружения в словарь.

- `decode_complete_state(self, state: dict) -> Self`:
    Декодирует полное состояние окружения из словаря.

- `add_environment(environment)`:
    Добавляет окружение в список всех окружений.

- `set_simulation_for_free_environments(simulation)`:
    Устанавливает симуляцию, если она равна `None`. Это позволяет захватывать свободные окружения определенными областями симуляции, если это необходимо.

- `get_environment_by_name(name: str)`:
    Возвращает окружение с указанным именем.

- `clear_environments()`:
    Очищает список всех окружений.

#### Как работает класс `TinyWorld`:
1. **Инициализация**: При создании экземпляра `TinyWorld` инициализируются основные атрибуты, такие как имя окружения, текущее время и список агентов.
2. **Шаг симуляции (`_step`)**: Этот метод выполняет один шаг симуляции, заставляя каждого агента в окружении действовать (`agent.act()`) и обрабатывая их действия (`_handle_actions`).
3. **Обработка действий (`_handle_actions`)**: В зависимости от типа действия (например, `REACH_OUT` или `TALK`), вызываются соответствующие обработчики (`_handle_reach_out`, `_handle_talk`).
4. **Коммуникация**: Методы `broadcast`, `broadcast_thought`, `broadcast_internal_goal` и `broadcast_context_change` используются для распространения информации между агентами в окружении.
5. **Управление временем**: Методы `run`, `skip`, `run_minutes`, `skip_minutes` и т.д. позволяют управлять течением времени в симуляции, выполняя шаги с определенными временными интервалами или пропуская время.
6. **Управление агентами**: Методы `add_agent`, `remove_agent`, `add_agents` и `remove_all_agents` позволяют добавлять и удалять агентов из окружения.

```
Инициализация TinyWorld
│
├─── Добавление агентов в окружение (add_agents, add_agent)
│    │
│    └─── Проверка уникальности имени агента
│
├─── Выполнение шага симуляции (_step)
│    │
│    ├─── Увеличение времени (_advance_datetime)
│    │
│    ├─── Действия агентов (agent.act)
│    │    │
│    │    └─── Обработка действий (_handle_actions)
│    │         │
│    │         ├─── REACH_OUT (_handle_reach_out)
│    │         │
│    │         └─── TALK (_handle_talk)
│    │
│    └─── Коммуникация между агентами (broadcast, broadcast_thought, broadcast_internal_goal, broadcast_context_change)
│
└─── Управление временем (run, skip, run_minutes, skip_minutes, и т.д.)
```

**Примеры**:

```python
from datetime import datetime, timedelta
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld

# Создание окружения
world = TinyWorld(name='MyWorld', initial_datetime=datetime(2024, 1, 1))

# Создание агентов
agent1 = TinyPerson(name='Alice')
agent2 = TinyPerson(name='Bob')

# Добавление агентов в окружение
world.add_agents([agent1, agent2])

# Запуск симуляции на 10 шагов с интервалом в 1 час
world.run(steps=10, timedelta_per_step=timedelta(hours=1))

# Вывод текущего времени в окружении
print(world.current_datetime)

# Alice отправляет сообщение Bob-у
agent1.talk('Привет, Bob!', target='Bob')
```

### `TinySocialNetwork`

**Описание**: Класс для моделирования социальных сетей, наследуется от `TinyWorld`.

**Наследует**: `TinyWorld`

**Принцип работы**: `TinySocialNetwork` расширяет возможности `TinyWorld`, добавляя поддержку социальных связей между агентами. Он позволяет определять отношения между агентами и управлять их видимостью друг для друга в зависимости от этих отношений.

**Атрибуты**:

- `relations (dict)`: Словарь, содержащий отношения между агентами (`{relation_name: [(agent_1, agent_2), ...]}``).

**Методы**:

- `__init__(self, name, broadcast_if_no_target=True)`:
    Создает новое окружение `TinySocialNetwork`.

- `add_relation(self, agent_1, agent_2, name="default")`:
    Добавляет отношение между двумя агентами.

- `_update_agents_contexts(self)`:
    Обновляет контексты агентов на основе текущего состояния мира.

- `_step(self)`:
    Выполняет один шаг в социальной сети, обновляя контексты агентов и вызывая метод `_step` базового класса.

- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`:
    Обрабатывает действие `REACH_OUT`, проверяя, находится ли цель в том же отношении, что и источник.

- `is_in_relation_with(self, agent_1: TinyPerson, agent_2: TinyPerson, relation_name=None) -> bool`:
    Проверяет, находятся ли два агента в отношении.

#### Как работает класс `TinySocialNetwork`:
1. **Инициализация**: При создании экземпляра `TinySocialNetwork` инициализируются атрибуты базового класса `TinyWorld` и добавляется атрибут `relations` для хранения социальных связей между агентами.
2. **Добавление отношений (`add_relation`)**: Этот метод позволяет установить отношение между двумя агентами, добавляя их в словарь `relations`.
3. **Обновление контекстов агентов (`_update_agents_contexts`)**: Этот метод вызывается на каждом шаге симуляции для обновления информации, доступной агентам, на основе их отношений. Он делает агентов видимыми друг для друга в зависимости от их социальных связей.
4. **Обработка действия `REACH_OUT` (`_handle_reach_out`)**: В `TinySocialNetwork` действие `REACH_OUT` обрабатывается с учетом социальных связей. Агент может обратиться к другому агенту только в том случае, если они находятся в одном отношении.
5. **Проверка отношений (`is_in_relation_with`)**: Этот метод позволяет проверить, находятся ли два агента в определенном отношении.

```
Инициализация TinySocialNetwork
│
├─── Добавление отношений между агентами (add_relation)
│
├─── Обновление контекстов агентов (_update_agents_contexts)
│    │
│    └─── Определение доступности агентов на основе отношений
│
├─── Выполнение шага симуляции (_step)
│    │
│    ├─── Обновление контекстов агентов (_update_agents_contexts)
│    │
│    └─── Выполнение шага симуляции в TinyWorld (super()._step())
│
└─── Обработка действия REACH_OUT (_handle_reach_out)
     │
     └─── Проверка наличия отношения между агентами (is_in_relation_with)
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinySocialNetwork

# Создание социальной сети
social_network = TinySocialNetwork(name='MySocialNetwork')

# Создание агентов
agent1 = TinyPerson(name='Alice')
agent2 = TinyPerson(name='Bob')
agent3 = TinyPerson(name='Charlie')

# Добавление агентов в социальную сеть
social_network.add_agents([agent1, agent2, agent3])

# Установление отношения "друзья" между Alice и Bob
social_network.add_relation(agent1, agent2, name='friends')

# Запуск симуляции на 5 шагов
social_network.run(steps=5)

# Alice пытается обратиться к Charlie
agent1.talk('Привет, Charlie!', target='Charlie')  # Сообщение не будет доставлено, так как они не в отношениях

# Alice пытается обратиться к Bob-у
agent1.talk('Привет, Bob!', target='Bob')  # Сообщение будет доставлено, так как они друзья
```

## Функции

В данном модуле нет отдельных функций, только методы классов.