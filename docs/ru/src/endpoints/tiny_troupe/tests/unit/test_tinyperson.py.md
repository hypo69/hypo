# Модуль тестирования класса TinyPerson
## Обзор

Модуль `test_tinyperson.py` содержит набор unit-тестов для проверки корректности работы класса `TinyPerson` и его методов. Тесты охватывают различные аспекты функционирования агентов, включая их способность действовать на основе входных данных, слушать, определять значения, взаимодействовать с другими агентами, воспринимать визуальные стимулы, думать, усваивать цели, перемещаться в новые локации, изменять контекст, сохранять спецификации и использовать программные определения.

## Подробнее

Этот модуль является частью системы тестирования проекта `hypotez` и предназначен для обеспечения надежности и стабильности класса `TinyPerson`. Он использует библиотеку `pytest` для организации и запуска тестов, а также модуль `logging` для протоколирования информации о процессе тестирования.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `test_act`

```python
def test_act(setup):
    """Тестирует способность агента действовать на основе входных данных.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может выполнять действия в ответ на полученные входные данные.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `listen_and_act()` для каждого агента с запросом "Tell me a bit about your life." и `return_actions=True`, чтобы получить список выполненных действий.
3.  Логирует текущие взаимодействия агента.
4.  Проверяет, что список действий не пуст, содержит действие типа "TALK" и завершается действием типа "DONE".

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов listen_and_act("Tell me a bit about your life.", return_actions=True)
  │   │
  │   ├──> Логирование текущих взаимодействий агента
  │   │
  │   ├──> Проверка: len(actions) >= 1
  │   │
  │   ├──> Проверка: contains_action_type(actions, "TALK")
  │   │
  │   └──> Проверка: terminates_with_action_type(actions, "DONE")
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_act
# test_act(setup_fixture)
```

### `test_listen`

```python
def test_listen(setup):
    """Тестирует способность агента слушать и обновлять свои текущие сообщения.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент корректно обрабатывает речевой стимул и обновляет свои текущие сообщения.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `listen()` для каждого агента с сообщением "Hello, how are you?".
3.  Проверяет, что список текущих сообщений не пуст, последнее сообщение имеет роль 'user', тип стимула 'CONVERSATION' и содержит корректный контент.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов listen("Hello, how are you?")
  │   │
  │   ├──> Проверка: len(agent.current_messages) > 0
  │   │
  │   ├──> Проверка: agent.episodic_memory.retrieve_all()[-1]['role'] == 'user'
  │   │
  │   ├──> Проверка: agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION'
  │   │
  │   └──> Проверка: agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?'
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_listen
# test_listen(setup_fixture)
```

### `test_define`

```python
def test_define(setup):
    """Тестирует способность агента определять значения в своей конфигурации и сбрасывать свой prompt.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может определять новые значения в своей конфигурации и обновлять свой prompt.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Сохраняет исходный prompt агента.
3.  Вызывает метод `define()` для определения нового значения 'age' равным 25.
4.  Проверяет, что конфигурация агента содержит новое значение, prompt агента изменился и содержит новое значение.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Сохранение исходного prompt
  │   │
  │   ├──> Вызов define('age', 25)
  │   │
  │   ├──> Проверка: agent._persona['age'] == 25
  │   │
  │   ├──> Проверка: agent.current_messages[0]['content'] != original_prompt
  │   │
  │   └──> Проверка: '25' in agent.current_messages[0]['content']
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_define
# test_define(setup_fixture)
```

### `test_define_several`

```python
def test_define_several(setup):
    """Тестирует способность агента определять несколько значений в группе.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может определять несколько значений в группе и сохранять их в своей конфигурации.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `define()` для определения списка навыков `["Python", "Machine learning", "GPT-3"]`.
3.  Проверяет, что конфигурация агента содержит все определенные навыки.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов define("skills", ["Python", "Machine learning", "GPT-3"])
  │   │
  │   ├──> Проверка: "Python" in agent._persona["skills"]
  │   │
  │   ├──> Проверка: "Machine learning" in agent._persona["skills"]
  │   │
  │   └──> Проверка: "GPT-3" in agent._persona["skills"]
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_define_several
# test_define_several(setup_fixture)
```

### `test_socialize`

```python
def test_socialize(setup):
    """Тестирует способность агента взаимодействовать с другим агентом.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может взаимодействовать с другим агентом, обмениваться информацией и выполнять действия на основе этого взаимодействия.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Создает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Перебирает этих агентов.
3.  Определяет другого агента для взаимодействия.
4.  Вызывает метод `make_agent_accessible()` для установления связи между агентами.
5.  Вызывает метод `listen()` для получения сообщения от другого агента.
6.  Вызывает метод `act()` для выполнения действий на основе полученного сообщения.
7.  Проверяет, что список действий не пуст, содержит действие типа "TALK" и упоминает имя другого агента.

**ASCII flowchart**:

```
Начало
  │
  ├──> Создание агентов (Оскар, Лиза)
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Определение другого агента
  │   │
  │   ├──> Вызов make_agent_accessible(other, relation_description="My friend")
  │   │
  │   ├──> Вызов listen(f"Hi {agent.name}, I am {other.name}.")
  │   │
  │   ├──> Вызов act(return_actions=True)
  │   │
  │   ├──> Проверка: len(actions) >= 1
  │   │
  │   ├──> Проверка: contains_action_type(actions, "TALK")
  │   │
  │   └──> Проверка: contains_action_content(actions, agent_first_name(other))
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_socialize
# test_socialize(setup_fixture)
```

### `test_see`

```python
def test_see(setup):
    """Тестирует способность агента воспринимать визуальные стимулы.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может воспринимать визуальные стимулы и выполнять действия на их основе.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `see()` для передачи визуального стимула "A beautiful sunset over the ocean.".
3.  Вызывает метод `act()` для выполнения действий на основе полученного стимула.
4.  Проверяет, что список действий не пуст, содержит действие типа "THINK" и упоминает ключевое слово "sunset".

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов see("A beautiful sunset over the ocean.")
  │   │
  │   ├──> Вызов act(return_actions=True)
  │   │
  │   ├──> Проверка: len(actions) >= 1
  │   │
  │   ├──> Проверка: contains_action_type(actions, "THINK")
  │   │
  │   └──> Проверка: contains_action_content(actions, "sunset")
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_see
# test_see(setup_fixture)
```

### `test_think`

```python
def test_think(setup):
    """Тестирует способность агента думать о чем-либо.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может думать о чем-либо и выполнять действия на основе своих мыслей.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `think()` для передачи мысли "I will tell everyone right now how awesome life is!".
3.  Вызывает метод `act()` для выполнения действий на основе полученной мысли.
4.  Проверяет, что список действий не пуст, содержит действие типа "TALK" и упоминает ключевое слово "life".

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов think("I will tell everyone right now how awesome life is!")
  │   │
  │   ├──> Вызов act(return_actions=True)
  │   │
  │   ├──> Проверка: len(actions) >= 1
  │   │
  │   ├──> Проверка: contains_action_type(actions, "TALK")
  │   │
  │   └──> Проверка: contains_action_content(actions, "life")
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_think
# test_think(setup_fixture)
```

### `test_internalize_goal`

```python
def test_internalize_goal(setup):
    """Тестирует способность агента усваивать цель.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может усваивать цели и выполнять действия для их достижения.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `internalize_goal()` для передачи цели "I want to compose in my head a wonderful poem about how cats are glorious creatures.".
3.  Вызывает метод `act()` для выполнения действий на основе усвоенной цели.
4.  Проверяет, что список действий не пуст, содержит действие типа "THINK" и упоминает ключевое слово "cats".

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов internalize_goal("I want to compose in my head a wonderful poem about how cats are glorious creatures.")
  │   │
  │   ├──> Вызов act(return_actions=True)
  │   │
  │   ├──> Проверка: len(actions) >= 1
  │   │
  │   ├──> Проверка: contains_action_type(actions, "THINK")
  │   │
  │   └──> Проверка: contains_action_content(actions, "cats")
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_internalize_goal
# test_internalize_goal(setup_fixture)
```

### `test_move_to`

```python
def test_move_to(setup):
    """Тестирует способность агента перемещаться в новое местоположение.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может перемещаться в новое местоположение и обновлять свой контекст.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `move_to()` для перемещения в "New York" с контекстом `["city", "busy", "diverse"]`.
3.  Проверяет, что текущее местоположение агента равно "New York" и контекст содержит все указанные элементы.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов move_to("New York", context=["city", "busy", "diverse"])
  │   │
  │   ├──> Проверка: agent._mental_state["location"] == "New York"
  │   │
  │   ├──> Проверка: "city" in agent._mental_state["context"]
  │   │
  │   ├──> Проверка: "busy" in agent._mental_state["context"]
  │   │
  │   └──> Проверка: "diverse" in agent._mental_state["context"]
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_move_to
# test_move_to(setup_fixture)
```

### `test_change_context`

```python
def test_change_context(setup):
    """Тестирует способность агента изменять свой контекст.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может изменять свой контекст и сохранять новые значения.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `change_context()` для изменения контекста на `["home", "relaxed", "comfortable"]`.
3.  Проверяет, что контекст агента содержит все указанные элементы.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов change_context(["home", "relaxed", "comfortable"])
  │   │
  │   ├──> Проверка: "home" in agent._mental_state["context"]
  │   │
  │   ├──> Проверка: "relaxed" in agent._mental_state["context"]
  │   │
  │   └──> Проверка: "comfortable" in agent._mental_state["context"]
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_change_context
# test_change_context(setup_fixture)
```

### `test_save_specification`

```python
def test_save_specification(setup):
    """Тестирует способность агента сохранять свою спецификацию.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может сохранять свою спецификацию в файл и загружать ее обратно.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect()` и `create_lisa_the_data_scientist()`.
2.  Вызывает метод `save_specification()` для сохранения спецификации агента в файл.
3.  Проверяет, что файл существует.
4.  Вызывает метод `load_specification()` для загрузки спецификации из файла.
5.  Проверяет, что загруженный агент имеет то же имя и конфигурацию, что и исходный агент (за исключением имени).

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар, Лиза)
  │   │
  │   ├──> Вызов save_specification(..., include_memory=True)
  │   │
  │   ├──> Проверка: os.path.exists(...)
  │   │
  │   ├──> Вызов TinyPerson.load_specification(..., new_agent_name=...)
  │   │
  │   ├──> Проверка: loaded_agent.name == ...
  │   │
  │   └──> Проверка: agents_personas_are_equal(agent, loaded_agent, ignore_name=True)
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_save_specification
# test_save_specification(setup_fixture)
```

### `test_programmatic_definitions`

```python
def test_programmatic_definitions(setup):
    """Тестирует способность агента использовать программные определения.

    Args:
        setup: Фикстура pytest для настройки тестовой среды.
    """
```

**Назначение**: Проверяет, что агент может использовать программные определения для настройки своего поведения.

**Параметры**:

-   `setup`: Фикстура pytest, предоставляющая настроенную тестовую среду.

**Как работает функция**:

1.  Перебирает двух агентов: `create_oscar_the_architect_2()` и `create_lisa_the_data_scientist_2()`.
2.  Вызывает метод `listen_and_act()` для запуска взаимодействия агента с использованием программных определений.

**ASCII flowchart**:

```
Начало
  │
  ├──> Перебор агентов (Оскар_2, Лиза_2)
  │   │
  │   └──> Вызов listen_and_act("Tell me a bit about your life.")
  │
  └──> Конец
```

**Примеры**:

```python
# Пример вызова функции test_programmatic_definitions
# test_programmatic_definitions(setup_fixture)
```