# Модуль TinySocialNetwork

## Обзор

Модуль `TinySocialNetwork` предоставляет класс `TinySocialNetwork`, который расширяет функциональность `TinyWorld`, добавляя поддержку социальных связей между агентами. Это позволяет моделировать социальные взаимодействия в виртуальной среде.

## Подробнее

`TinySocialNetwork` позволяет устанавливать отношения между агентами (`TinyPerson`), определять контекст видимости агентов друг для друга на основе этих отношений и обрабатывать действия `REACH_OUT` с учетом социальных связей.

## Классы

### `TinySocialNetwork`

**Описание**: Класс `TinySocialNetwork` представляет собой социальную сеть, расширяющую возможности виртуального мира `TinyWorld`. Он управляет агентами и их взаимоотношениями, обеспечивая основу для моделирования социальных взаимодействий.

**Наследует**:

- `TinyWorld`: `TinySocialNetwork` наследует функциональность виртуального мира, такую как управление агентами, шаги симуляции и обработка действий.

**Атрибуты**:

- `relations (dict)`: Словарь, хранящий отношения между агентами. Ключом является название отношения (например, "друг", "коллега"), а значением - список кортежей, где каждый кортеж содержит пару связанных агентов.
- `name (str)`: Имя социальной сети.
- `broadcast_if_no_target (bool)`: Если `True`, действия транслируются через доступные отношения агента, если цель действия не найдена.

**Методы**:

- `__init__(name, broadcast_if_no_target=True)`: Инициализирует новый экземпляр класса `TinySocialNetwork`.
- `add_relation(agent_1, agent_2, name="default")`: Добавляет отношение между двумя агентами.
- `_update_agents_contexts()`: Обновляет контексты наблюдения агентов на основе текущего состояния мира.
- `_step()`: Выполняет один шаг симуляции в социальной сети.
- `_handle_reach_out(source_agent, content, target)`: Обрабатывает действие `REACH_OUT`, позволяя агентам отправлять сообщения только тем, с кем они находятся в отношениях.
- `is_in_relation_with(agent_1, agent_2, relation_name=None)`: Проверяет, находятся ли два агента в каких-либо отношениях или в конкретном отношении.

### `__init__`

```python
def __init__(self, name, broadcast_if_no_target=True):
    """
    Create a new TinySocialNetwork environment.

    Args:
        name (str): The name of the environment.
        broadcast_if_no_target (bool): If True, broadcast actions through an agent's available relations
          if the target of an action is not found.
    """
```

**Назначение**: Инициализирует новый экземпляр класса `TinySocialNetwork`.

**Параметры**:

- `name (str)`: Имя социальной сети.
- `broadcast_if_no_target (bool)`: Если `True`, действия транслируются через доступные отношения агента, если цель действия не найдена. По умолчанию `True`.

**Как работает функция**:

1. Вызывает конструктор родительского класса `TinyWorld` для инициализации основных атрибутов виртуального мира.
2. Инициализирует атрибут `relations` как пустой словарь, который будет использоваться для хранения отношений между агентами.

```
Начало конструктора
│
├─── Вызов конструктора TinyWorld
│
└─── Инициализация relations как {}
│
Конец конструктора
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork

# Пример создания экземпляра TinySocialNetwork
social_network = TinySocialNetwork(name="MySocialNetwork", broadcast_if_no_target=False)
print(social_network.name)  # Вывод: MySocialNetwork
print(social_network.broadcast_if_no_target)  # Вывод: False
```

### `add_relation`

```python
@transactional
def add_relation(self, agent_1, agent_2, name="default"):
    """
    Adds a relation between two agents.

    Args:
        agent_1 (TinyPerson): The first agent.
        agent_2 (TinyPerson): The second agent.
        name (str): The name of the relation.
    """
```

**Назначение**: Добавляет отношение между двумя агентами в социальной сети.

**Параметры**:

- `agent_1 (TinyPerson)`: Первый агент.
- `agent_2 (TinyPerson)`: Второй агент.
- `name (str)`: Название отношения (например, "друг", "коллега"). По умолчанию "default".

**Как работает функция**:

1. Логирует добавление отношения между агентами с использованием `logger.debug`.
2. Проверяет, находятся ли агенты уже в социальной сети. Если нет, добавляет их.
3. Добавляет пару агентов в список отношений с указанным именем. Если отношения с таким именем еще не существует, создает новый список отношений.
4. Возвращает `self` для возможности chaining.

```
Начало add_relation
│
├─── Логирование добавления отношения
│
├─── Проверка и добавление agent_1 в agents
│
├─── Проверка и добавление agent_2 в agents
│
├─── Добавление отношения в relations
│
└─── Возврат self
│
Конец add_relation
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent.tiny_person import TinyPerson

# Пример создания агентов
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

# Пример создания социальной сети
social_network = TinySocialNetwork(name="MySocialNetwork")

# Пример добавления отношения между агентами
social_network.add_relation(agent1, agent2, name="friend")

# Проверка наличия отношения
print(social_network.is_in_relation_with(agent1, agent2, name="friend"))  # Вывод: True
```

### `_update_agents_contexts`

```python
@transactional
def _update_agents_contexts(self):
    """
    Updates the agents' observations based on the current state of the world.
    """
```

**Назначение**: Обновляет контексты наблюдения агентов на основе текущего состояния мира, определяя, какие агенты видны друг другу.

**Как работает функция**:

1.  **Очистка видимости агентов**:
    *   Проходит по всем агентам в социальной сети.
    *   Для каждого агента вызывается метод `make_all_agents_inaccessible()`, чтобы сбросить информацию о доступности других агентов.
2.  **Обновление видимости на основе отношений**:
    *   Проходит по всем отношениям, хранящимся в словаре `self.relations`.
    *   Для каждого отношения (например, "друзья"):
        *   Логирует информацию об обновлении контекстов для данного отношения.
        *   Проходит по всем парам агентов, связанным этим отношением.
        *   Для каждой пары агентов (agent_1, agent_2):
            *   Вызывает метод `agent_1.make_agent_accessible(agent_2)`, чтобы сделать agent_2 видимым для agent_1.
            *   Вызывает метод `agent_2.make_agent_accessible(agent_1)`, чтобы сделать agent_1 видимым для agent_2 (отношения двусторонние).

```
Начало _update_agents_contexts
│
├── Очистка видимости агентов
│   └── Для каждого агента: agent.make_all_agents_inaccessible()
│
└── Обновление видимости на основе отношений
│   └── Для каждого отношения:
│       ├── Логирование информации об обновлении
│       └── Для каждой пары агентов:
│           ├── agent_1.make_agent_accessible(agent_2)
│           └── agent_2.make_agent_accessible(agent_1)
│
Конец _update_agents_contexts
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent.tiny_person import TinyPerson

# Пример создания агентов
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

# Пример создания социальной сети
social_network = TinySocialNetwork(name="MySocialNetwork")

# Добавление агентов в социальную сеть
social_network.add_agent(agent1)
social_network.add_agent(agent2)

# Пример добавления отношения между агентами
social_network.add_relation(agent1, agent2, name="friend")

# Обновление контекстов агентов
social_network._update_agents_contexts()

# Теперь agent1 и agent2 должны видеть друг друга
print(agent1.can_see(agent2))  # Вывод: True
print(agent2.can_see(agent1))  # Вывод: True
```

### `_step`

```python
@transactional
def _step(self):
    """
    Выполняет один шаг симуляции в социальной сети.
    """
```

**Назначение**: Выполняет один шаг симуляции в социальной сети.

**Как работает функция**:

1. Обновляет контексты агентов, вызывая метод `_update_agents_contexts()`.
2. Вызывает метод `_step()` родительского класса `TinyWorld` для выполнения основных действий шага симуляции.

```
Начало _step
│
├── Обновление контекстов агентов: _update_agents_contexts()
│
└── Вызов _step() родительского класса
│
Конец _step
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent.tiny_person import TinyPerson

# Создание агентов и социальной сети (как в предыдущих примерах)
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

social_network = TinySocialNetwork(name="MySocialNetwork")
social_network.add_agent(agent1)
social_network.add_agent(agent2)
social_network.add_relation(agent1, agent2, name="friend")

# Выполнение шага симуляции
social_network._step()
```

### `_handle_reach_out`

```python
@transactional
def _handle_reach_out(self, source_agent: TinyPerson, content: str, target: str):
    """
    Handles the REACH_OUT action. This social network implementation only allows
    REACH_OUT to succeed if the target agent is in the same relation as the source agent.

    Args:
        source_agent (TinyPerson): The agent that issued the REACH_OUT action.
        content (str): The content of the message.
        target (str): The target of the message.
    """
```

**Назначение**: Обрабатывает действие `REACH_OUT` (попытка связаться с другим агентом). В данной реализации социальной сети `REACH_OUT` разрешено только в том случае, если целевой агент находится в том же отношении, что и исходный агент.

**Параметры**:

- `source_agent (TinyPerson)`: Агент, инициировавший действие `REACH_OUT`.
- `content (str)`: Содержание сообщения.
- `target (str)`: Имя целевого агента.

**Как работает функция**:

1.  **Проверка наличия отношения между агентами**:
    *   Вызывает метод `is_in_relation_with(source_agent, self.get_agent_by_name(target))`, чтобы проверить, находится ли целевой агент (найденный по имени) в каком-либо отношении с исходным агентом.
2.  **Обработка успешного `REACH_OUT`**:
    *   Если целевой агент находится в том же отношении, что и исходный агент:
        *   Вызывает метод `super()._handle_reach_out(source_agent, content, target)` для фактической отправки сообщения (логика отправки сообщения реализована в родительском классе `TinyWorld`).
3.  **Обработка неуспешного `REACH_OUT`**:
    *   Если целевой агент не находится в том же отношении, что и исходный агент:
        *   Вызывает метод `source_agent.socialize(...)`, чтобы сообщить исходному агенту, что связь с целевым агентом невозможна из-за отсутствия отношений.

```
Начало _handle_reach_out
│
├── Проверка наличия отношения между агентами
│   └── Вызов is_in_relation_with(source_agent, self.get_agent_by_name(target))
│
├── Обработка успешного REACH_OUT
│   └── Если отношение есть: super()._handle_reach_out(source_agent, content, target)
│
└── Обработка неуспешного REACH_OUT
│   └── Если отношения нет: source_agent.socialize(...)
│
Конец _handle_reach_out
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent.tiny_person import TinyPerson

# Создание агентов и социальной сети (как в предыдущих примерах)
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")
agent3 = TinyPerson(name="Charlie")

social_network = TinySocialNetwork(name="MySocialNetwork")
social_network.add_agent(agent1)
social_network.add_agent(agent2)
social_network.add_agent(agent3)
social_network.add_relation(agent1, agent2, name="friend")

# Попытка Alice связаться с Bob (они друзья)
social_network._handle_reach_out(agent1, "Hello Bob!", "Bob")

# Попытка Alice связаться с Charlie (они не друзья)
social_network._handle_reach_out(agent1, "Hello Charlie!", "Charlie")  # Alice получит сообщение об ошибке
```

### `is_in_relation_with`

```python
def is_in_relation_with(self, agent_1:TinyPerson, agent_2:TinyPerson, relation_name=None) -> bool:
    """
    Checks if two agents are in a relation. If the relation name is given, check that
    the agents are in that relation. If no relation name is given, check that the agents
    are in any relation. Relations are undirected, so the order of the agents does not matter.

    Args:
        agent_1 (TinyPerson): The first agent.
        agent_2 (TinyPerson): The second agent.
        relation_name (str): The name of the relation to check, or None to check any relation.

    Returns:
        bool: True if the two agents are in the given relation, False otherwise.
    """
```

**Назначение**: Проверяет, находятся ли два агента в каком-либо отношении или в конкретном отношении.

**Параметры**:

-   `agent_1 (TinyPerson)`: Первый агент.
-   `agent_2 (TinyPerson)`: Второй агент.
-   `relation_name (str, optional)`: Название отношения для проверки. Если `None`, проверяется наличие любого отношения между агентами. По умолчанию `None`.

**Возвращает**:

-   `bool`: `True`, если агенты находятся в указанном отношении (или в любом отношении, если `relation_name` is `None`). `False` в противном случае.

**Как работает функция**:

1.  **Проверка на наличие любого отношения (если `relation_name` is `None`)**:
    *   Проходит по всем отношениям в словаре `self.relations`.
    *   Для каждого отношения проверяет, содержится ли пара агентов (в любом порядке) в списке отношений.
    *   Если пара агентов найдена в каком-либо отношении, возвращает `True`.
    *   Если ни в одном отношении пара агентов не найдена, возвращает `False`.
2.  **Проверка на наличие конкретного отношения (если `relation_name` указано)**:
    *   Проверяет, существует ли отношение с указанным именем в словаре `self.relations`.
    *   Если отношение существует, проверяет, содержится ли пара агентов (в любом порядке) в списке отношений для этого имени.
    *   Возвращает `True`, если пара агентов найдена в указанном отношении, и `False` в противном случае.
    *   Если отношение с указанным именем не существует, возвращает `False`.

```
Начало is_in_relation_with
│
├── Проверка relation_name is None
│   ├── Если relation_name is None:
│   │   ├── Проход по всем relations
│   │   │   ├── Проверка наличия agent_1 и agent_2 в relation (в любом порядке)
│   │   │   │   └── Если найдено: return True
│   │   │   └── Если не найдено ни в одном relation: return False
│   └── Если relation_name указано:
│       ├── Проверка наличия relation_name в self.relations
│       │   ├── Если есть:
│       │   │   ├── Проверка наличия agent_1 и agent_2 в relation_name (в любом порядке)
│       │   │   │   └── Если найдено: return True
│       │   │   └── Если не найдено: return False
│       │   └── Если нет: return False
│
Конец is_in_relation_with
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent.tiny_person import TinyPerson

# Создание агентов и социальной сети (как в предыдущих примерах)
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")
agent3 = TinyPerson(name="Charlie")

social_network = TinySocialNetwork(name="MySocialNetwork")
social_network.add_agent(agent1)
social_network.add_agent(agent2)
social_network.add_agent(agent3)
social_network.add_relation(agent1, agent2, name="friend")

# Проверка наличия отношения "friend" между Alice и Bob
print(social_network.is_in_relation_with(agent1, agent2, relation_name="friend"))  # Вывод: True
print(social_network.is_in_relation_with(agent2, agent1, relation_name="friend"))  # Вывод: True (порядок не важен)

# Проверка наличия отношения "friend" между Alice и Charlie
print(social_network.is_in_relation_with(agent1, agent3, relation_name="friend"))  # Вывод: False

# Проверка наличия любого отношения между Alice и Bob
print(social_network.is_in_relation_with(agent1, agent2))  # Вывод: True

# Проверка наличия любого отношения между Alice и Charlie
print(social_network.is_in_relation_with(agent1, agent3))  # Вывод: False