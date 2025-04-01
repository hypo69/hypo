# Модуль `tiny_social_network.py`

## Обзор

Модуль `tiny_social_network.py` предоставляет класс `TinySocialNetwork`, который расширяет возможности `TinyWorld`, добавляя поддержку социальных связей между агентами. Он позволяет моделировать социальные взаимодействия, где агенты могут взаимодействовать друг с другом только в рамках установленных отношений.

## Подробней

Этот модуль предназначен для создания симуляций, в которых социальные связи играют важную роль. Он позволяет устанавливать отношения между агентами и контролировать, как эти отношения влияют на их способность взаимодействовать. Класс `TinySocialNetwork` управляет этими связями и обеспечивает механизм для обновления контекста агентов на основе их социальных связей.

## Классы

### `TinySocialNetwork`

**Описание**: Класс `TinySocialNetwork` представляет собой социальную сеть, в которой агенты могут взаимодействовать друг с другом через установленные отношения.

**Наследует**:
- `TinyWorld`: Расширяет класс `TinyWorld`, добавляя функциональность социальных связей.

**Атрибуты**:
- `relations` (dict): Словарь, хранящий отношения между агентами. Ключи словаря — названия отношений, значения — списки кортежей, где каждый кортеж содержит пару агентов, связанных этими отношениями.
- `broadcast_if_no_target` (bool): Флаг, определяющий, следует ли рассылать действия агента через доступные отношения, если цель действия не найдена. По умолчанию `True`.

**Методы**:
- `__init__(self, name, broadcast_if_no_target=True)`: Конструктор класса, инициализирует социальную сеть с заданным именем и параметром `broadcast_if_no_target`.
- `add_relation(self, agent_1, agent_2, name="default")`: Добавляет отношение между двумя агентами.
- `_update_agents_contexts(self)`: Обновляет контексты агентов на основе текущего состояния мира, учитывая установленные отношения.
- `_step(self)`: Выполняет один шаг симуляции, обновляя контексты агентов и вызывая метод `_step` родительского класса.
- `_handle_reach_out(self, source_agent: TinyPerson, content: str, target: str)`: Обрабатывает действие `REACH_OUT`, позволяя агенту взаимодействовать с другим агентом только если они находятся в одинаковых отношениях.
- `is_in_relation_with(self, agent_1: TinyPerson, agent_2: TinyPerson, relation_name=None) -> bool`: Проверяет, находятся ли два агента в отношении друг с другом.

#### `__init__`

```python
def __init__(self, name, broadcast_if_no_target=True):
    """
    Create a new TinySocialNetwork environment.

    Args:
        name (str): The name of the environment.
        broadcast_if_no_target (bool): If True, broadcast actions through an agent\'s available relations
          if the target of an action is not found.
    """
    super().__init__(name, broadcast_if_no_target=broadcast_if_no_target)
    self.relations = {}
```

**Назначение**: Инициализирует новый экземпляр класса `TinySocialNetwork`.

**Параметры**:
- `name` (str): Имя социальной сети.
- `broadcast_if_no_target` (bool): Если `True`, действия агента рассылаются через доступные отношения, если цель не найдена. По умолчанию `True`.

**Как работает функция**:
1. Вызывает конструктор родительского класса `TinyWorld` с переданными параметрами `name` и `broadcast_if_no_target`.
2. Инициализирует атрибут `self.relations` как пустой словарь, который будет хранить отношения между агентами.

```ascii
+---------------------------------------------------------------------+
| __init__(name, broadcast_if_no_target)                             |
+---------------------------------------------------------------------+
| Вызов конструктора TinyWorld                                       |
| Инициализация self.relations = {}                                   |
+---------------------------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork

network = TinySocialNetwork(name="MyNetwork", broadcast_if_no_target=False)
print(network.name)
# => MyNetwork
print(network.relations)
# => {}
```

#### `add_relation`

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
    logger.debug(f"Adding relation {name} between {agent_1.name} and {agent_2.name}.")

    # agents must already be in the environment, if not they are first added
    if agent_1 not in self.agents:
        self.agents.append(agent_1)
    if agent_2 not in self.agents:
        self.agents.append(agent_2)

    if name in self.relations:
        self.relations[name].append((agent_1, agent_2))
    else:
        self.relations[name] = [(agent_1, agent_2)]

    return self  # for chaining
```

**Назначение**: Добавляет отношение между двумя агентами в социальной сети.

**Параметры**:
- `agent_1` (`TinyPerson`): Первый агент.
- `agent_2` (`TinyPerson`): Второй агент.
- `name` (str): Название отношения. По умолчанию `"default"`.

**Как работает функция**:

1.  Логирует добавление отношения между агентами, используя `logger.debug`.
2.  Проверяет, находятся ли агенты `agent_1` и `agent_2` уже в списке агентов социальной сети (`self.agents`). Если агента нет в списке, он добавляется.
3.  Если отношение с именем `name` уже существует в словаре `self.relations`, добавляет кортеж `(agent_1, agent_2)` в список отношений с этим именем. Если такого отношения еще нет, создает новый список с этим кортежем.
4.  Возвращает `self` для возможности chaining (последовательного вызова методов).

```ascii
+-------------------------------------------------------------------------------------+
| add_relation(agent_1, agent_2, name="default")                                     |
+-------------------------------------------------------------------------------------+
| Логирование добавления отношения                                                     |
| Проверка наличия агентов в self.agents -> добавление при необходимости             |
| Обновление self.relations: добавление кортежа (agent_1, agent_2) или создание нового списка |
| Возврат self                                                                         |
+-------------------------------------------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent import TinyPerson

network = TinySocialNetwork(name="MyNetwork")
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

network.add_relation(agent1, agent2, name="friend")
print(network.relations)
# => {'friend': [(<tinytroupe.agent.TinyPerson object at ...>, <tinytroupe.agent.TinyPerson object at ...>)]}
```

#### `_update_agents_contexts`

```python
@transactional
def _update_agents_contexts(self):
    """
    Updates the agents\' observations based on the current state of the world.
    """

    # clear all accessibility first
    for agent in self.agents:
        agent.make_all_agents_inaccessible()

    # now update accessibility based on relations
    for relation_name, relation in self.relations.items():
        logger.debug(f"Updating agents\' observations for relation {relation_name}.")
        for agent_1, agent_2 in relation:
            agent_1.make_agent_accessible(agent_2)
            agent_2.make_agent_accessible(agent_1)
```

**Назначение**: Обновляет контексты (наблюдения) агентов на основе текущего состояния социальной сети, учитывая установленные отношения.

**Как работает функция**:

1.  Удаляет доступность всех агентов для каждого агента в социальной сети, вызывая `agent.make_all_agents_inaccessible()`.
2.  Проходит по всем отношениям, хранящимся в `self.relations`.
3.  Для каждого отношения логирует обновление контекстов агентов, используя `logger.debug`.
4.  Делает агентов доступными друг для друга в соответствии с установленными отношениями, вызывая `agent_1.make_agent_accessible(agent_2)` и `agent_2.make_agent_accessible(agent_1)`.

```ascii
+-------------------------------------------------------------------------------------+
| _update_agents_contexts()                                                         |
+-------------------------------------------------------------------------------------+
| Удаление доступности всех агентов                                                    |
| Перебор отношений в self.relations                                                  |
| Логирование обновления контекстов агентов                                             |
| Установка доступности агентов друг для друга на основе отношений                     |
+-------------------------------------------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent import TinyPerson

network = TinySocialNetwork(name="MyNetwork")
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

network.add_relation(agent1, agent2, name="friend")
network._update_agents_contexts()

# Здесь можно проверить, что agent1 и agent2 теперь доступны друг для друга
```

#### `_step`

```python
@transactional
def _step(self):
    self._update_agents_contexts()

    # call super
    super()._step()
```

**Назначение**: Выполняет один шаг симуляции в социальной сети.

**Как работает функция**:

1.  Обновляет контексты агентов, вызывая `self._update_agents_contexts()`.
2.  Вызывает метод `_step()` родительского класса (`TinyWorld`) для выполнения стандартных действий шага симуляции.

```ascii
+-----------------------------------------------------+
| _step()                                             |
+-----------------------------------------------------+
| Обновление контекстов агентов                       |
| Вызов super()._step()                              |
+-----------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent import TinyPerson

network = TinySocialNetwork(name="MyNetwork")
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")

network.add_relation(agent1, agent2, name="friend")
network._step()

# Здесь происходит шаг симуляции, контексты агентов обновляются
```

#### `_handle_reach_out`

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

    # check if the target is in the same relation as the source
    if self.is_in_relation_with(source_agent, self.get_agent_by_name(target)):
        super()._handle_reach_out(source_agent, content, target)

    # if we get here, the target is not in the same relation as the source
    source_agent.socialize(f"{target} is not in the same relation as you, so you cannot reach out to them.", source=self)
```

**Назначение**: Обрабатывает действие `REACH_OUT`, позволяя агенту отправлять сообщение другому агенту только если они находятся в одинаковых отношениях.

**Параметры**:
- `source_agent` (`TinyPerson`): Агент, инициирующий действие `REACH_OUT`.
- `content` (str): Содержание сообщения.
- `target` (str): Имя целевого агента.

**Как работает функция**:

1.  Проверяет, находится ли `source_agent` в отношении с целевым агентом, используя `self.is_in_relation_with(source_agent, self.get_agent_by_name(target))`.
2.  Если агенты находятся в отношении, вызывает метод `_handle_reach_out` родительского класса (`TinyWorld`) для обработки действия `REACH_OUT`.
3.  Если агенты не находятся в отношении, `source_agent` отправляет сообщение о том, что не может связаться с целевым агентом, используя `source_agent.socialize()`.

```ascii
+-------------------------------------------------------------------------------------+
| _handle_reach_out(source_agent, content, target)                                   |
+-------------------------------------------------------------------------------------+
| Проверка наличия отношения между source_agent и target                               |
| Если в отношении: вызов super()._handle_reach_out()                                |
| Иначе: отправка сообщения source_agent о невозможности связаться с target             |
+-------------------------------------------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent import TinyPerson

network = TinySocialNetwork(name="MyNetwork")
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")
agent3 = TinyPerson(name="Charlie")

network.add_relation(agent1, agent2, name="friend")

# agent1 может связаться с agent2, так как они в отношении "friend"
network._handle_reach_out(agent1, "Hello Bob!", agent2.name)

# agent1 не может связаться с agent3, так как они не в отношении
network._handle_reach_out(agent1, "Hello Charlie!", agent3.name)
# => Alice: Charlie is not in the same relation as you, so you cannot reach out to them.
```

#### `is_in_relation_with`

```python
def is_in_relation_with(self, agent_1: TinyPerson, agent_2: TinyPerson, relation_name=None) -> bool:
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
    if relation_name is None:
        for relation_name, relation in self.relations.items():
            if (agent_1, agent_2) in relation or (agent_2, agent_1) in relation:
                return True
        return False

    else:
        if relation_name in self.relations:
            return (agent_1, agent_2) in self.relations[relation_name] or (agent_2, agent_1) in self.relations[relation_name]
        else:
            return False
```

**Назначение**: Проверяет, находятся ли два агента в отношении друг с другом.

**Параметры**:
- `agent_1` (`TinyPerson`): Первый агент.
- `agent_2` (`TinyPerson`): Второй агент.
- `relation_name` (str, optional): Название отношения для проверки. Если `None`, проверяется наличие любого отношения.

**Возвращает**:
- `bool`: `True`, если агенты находятся в отношении, иначе `False`.

**Как работает функция**:

1.  Если `relation_name` не указано (`None`), функция перебирает все отношения в `self.relations`.
2.  Если агенты `agent_1` и `agent_2` найдены в каком-либо отношении (или `agent_2` и `agent_1`, так как отношения ненаправленные), функция возвращает `True`.
3.  Если `relation_name` указано, функция проверяет, существует ли такое отношение в `self.relations`.
4.  Если отношение существует, функция возвращает `True`, если агенты `agent_1` и `agent_2` (или `agent_2` и `agent_1`) находятся в этом отношении.
5.  Если отношение не существует, функция возвращает `False`.

```ascii
+-------------------------------------------------------------------------------------+
| is_in_relation_with(agent_1, agent_2, relation_name=None)                          |
+-------------------------------------------------------------------------------------+
| Если relation_name is None:                                                        |
|   Перебор всех отношений в self.relations                                            |
|   Проверка наличия agent_1 и agent_2 (или agent_2 и agent_1) в отношении           |
|   Возврат True, если найдено                                                         |
|   Возврат False, если не найдено                                                     |
| Иначе:                                                                               |
|   Проверка существования relation_name в self.relations                             |
|   Если существует:                                                                  |
|     Проверка наличия agent_1 и agent_2 (или agent_2 и agent_1) в отношении         |
|     Возврат True, если найдено                                                       |
|   Иначе:                                                                             |
|     Возврат False                                                                    |
+-------------------------------------------------------------------------------------+
```

**Примеры**:

```python
from tinytroupe.environment.tiny_social_network import TinySocialNetwork
from tinytroupe.agent import TinyPerson

network = TinySocialNetwork(name="MyNetwork")
agent1 = TinyPerson(name="Alice")
agent2 = TinyPerson(name="Bob")
agent3 = TinyPerson(name="Charlie")

network.add_relation(agent1, agent2, name="friend")

print(network.is_in_relation_with(agent1, agent2))
# => True
print(network.is_in_relation_with(agent1, agent3))
# => False
print(network.is_in_relation_with(agent1, agent2, relation_name="friend"))
# => True
print(network.is_in_relation_with(agent1, agent2, relation_name="enemy"))
# => False