## Анализ кода модуля `test_tinyperson.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на отдельные тестовые функции, каждая из которых проверяет конкретную функциональность.
    - Используются ассерты для проверки ожидаемого поведения, что облегчает обнаружение ошибок.
    - Присутствуют информативные сообщения об ошибках в ассертах, которые помогают понять, что именно пошло не так.
    - Тесты покрывают различные аспекты поведения агента, такие как прослушивание, действия, определение значений, социализация и т.д.
- Минусы
    -  Импорт `logger` не соответствует стандарту `from src.logger.logger import logger`.
    -  В некоторых местах используются f-строки для сообщений в ассертах, хотя можно использовать более простой вариант форматирования (но это не критично).
    -  Отсутствует описание модуля.
    -  Нет документации для тестовых функций.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки данных из файла в тесте `test_save_spec`.

**Рекомендации по улучшению**
1. **Импорт логгера**: Измените импорт `logger` на `from src.logger.logger import logger`.
2. **Документирование**: Добавьте описание модуля и документацию к каждой тестовой функции.
3. **Использование `j_loads`**: В функции `test_save_spec` используйте `j_loads` или `j_loads_ns` для загрузки JSON-файла.
4. **Форматирование**:  Упростите форматирование сообщений в ассертах.
5. **Удаление лишних импортов**: Удалите дублирующиеся `sys.path.insert(0, ...)`
6. **Переименование**: Переименовать `setup` фикстуру в `fixture_setup`.

**Оптимизированный код**

```python
"""
Модуль для тестирования класса TinyPerson
=========================================================================================

Этот модуль содержит набор тестов для проверки функциональности класса :class:`TinyPerson`,
включая проверку действий, прослушивания, определения параметров, социализации,
визуального восприятия, мышления, целеполагания, перемещения, изменения контекста
и сохранения/загрузки спецификаций.

Пример использования
--------------------

Запустите тесты с помощью pytest:

.. code-block:: bash

    pytest tests/unit/test_tinyperson.py
"""
import pytest
# from src.logger import logger # TODO: Fix logger import
from src.logger.logger import logger
import sys
import os
# sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../') # ensures that the package is imported from the parent directory, not the Python installation


# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('..')

from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tinyperson import TinyPerson

from testing_utils import *
from src.utils.jjson import j_loads

@pytest.fixture(scope="function")
def fixture_setup():
    """
    Фикстура для настройки окружения перед выполнением каждого теста.
    """
    #  В данной фикстуре нет необходимости в каких-либо действиях,
    #  но ее наличие позволяет единообразно использовать ее в тестах.
    pass
    

def test_act(fixture_setup):
    """
    Тестирует метод `listen_and_act` агента.

    Проверяет, что агент выполняет хотя бы одно действие после получения стимула,
    что среди действий есть действие типа `TALK` и что действия завершаются
    действием типа `DONE`.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        actions = agent.listen_and_act('Tell me a bit about your life.', return_actions=True)
        logger.info(agent.pp_current_interactions())
        assert len(actions) >= 1, f'{agent.name} should have at least one action to perform (even if it is just DONE).'
        assert contains_action_type(actions, 'TALK'), f'{agent.name} should have at least one TALK action to perform, since we asked him to do so.'
        assert terminates_with_action_type(actions, 'DONE'), f'{agent.name} should always terminate with a DONE action.'

def test_listen(fixture_setup):
    """
    Тестирует метод `listen` агента.

    Проверяет, что агент обновляет свои текущие сообщения после прослушивания стимула,
    что последнее сообщение имеет роль 'user', тип стимула 'CONVERSATION'
    и правильное содержимое.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.listen('Hello, how are you?')
        assert len(agent.current_messages) > 0, f'{agent.name} should have at least one message in its current messages.'
        assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user', f'{agent.name} should have the last message as \'user\'.'
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION', f'{agent.name} should have the last message as a \'CONVERSATION\' stimulus.'
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?', f'{agent.name} should have the last message with the correct content.'

def test_define(fixture_setup):
    """
    Тестирует метод `define` агента.

    Проверяет, что агент устанавливает значение в свою конфигурацию и сбрасывает свой промпт.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        original_prompt = agent.current_messages[0]['content']
        agent.define('age', 25)
        assert agent._configuration['age'] == 25, f'{agent.name} should have the age set to 25.'
        assert agent.current_messages[0]['content'] != original_prompt, f'{agent.name} should have a different prompt after defining a new value.'
        assert '25' in agent.current_messages[0]['content'], f'{agent.name} should have the age in the prompt.'

def test_define_several(fixture_setup):
    """
    Тестирует метод `define_several` агента.

    Проверяет, что агент устанавливает несколько значений в группу своей конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.define_several(group='skills', records=['Python', 'Machine learning', 'GPT-3'])
        assert 'Python' in agent._configuration['skills'], f'{agent.name} should have Python as a skill.'
        assert 'Machine learning' in agent._configuration['skills'], f'{agent.name} should have Machine learning as a skill.'
        assert 'GPT-3' in agent._configuration['skills'], f'{agent.name} should have GPT-3 as a skill.'

def test_socialize(fixture_setup):
    """
    Тестирует метод `socialize` агента.

    Проверяет, что агент взаимодействует с другим агентом,
    отвечает на приветствие и упоминает имя другого агента в своем ответе.
    """
    an_oscar = create_oscar_the_architect()
    a_lisa = create_lisa_the_data_scientist()
    for agent in [an_oscar, a_lisa]:
        other = a_lisa if agent.name == 'Oscar' else an_oscar
        agent.make_agent_accessible(other, relation_description='My friend')
        agent.listen(f'Hi {agent.name}, I am {other.name}.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f'{agent.name} should have at least one action to perform.'
        assert contains_action_type(actions, 'TALK'), f'{agent.name} should have at least one TALK action to perform, since we started a conversation.'
        assert contains_action_content(actions, other.name), f'{agent.name} should mention {other.name} in the TALK action, since they are friends.'

def test_see(fixture_setup):
    """
    Тестирует метод `see` агента.

    Проверяет, что агент реагирует на визуальный стимул, выполняя действие типа `THINK`
    и упоминает увиденное в этом действии.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.see('A beautiful sunset over the ocean.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f'{agent.name} should have at least one action to perform.'
        assert contains_action_type(actions, 'THINK'), f'{agent.name} should have at least one THINK action to perform, since they saw something interesting.'
        assert contains_action_content(actions, 'sunset'), f'{agent.name} should mention the sunset in the THINK action, since they saw it.'

def test_think(fixture_setup):
    """
    Тестирует метод `think` агента.

    Проверяет, что агент выполняет действие типа `TALK` после размышления
    и упоминает содержание размышлений в этом действии.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.think('I will tell everyone right now how awesome life is!')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f'{agent.name} should have at least one action to perform.'
        assert contains_action_type(actions, 'TALK'), f'{agent.name} should have at least one TALK action to perform, since they are eager to talk.'
        assert contains_action_content(actions, 'life'), f'{agent.name} should mention life in the TALK action, since they thought about it.'

def test_internalize_goal(fixture_setup):
    """
    Тестирует метод `internalize_goal` агента.

    Проверяет, что агент выполняет действие типа `SEARCH` после интернализации цели
    и упоминает цель в этом действии.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.internalize_goal('I want to learn more about GPT-3.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f'{agent.name} should have at least one action to perform.'
        assert contains_action_type(actions, 'SEARCH'), f'{agent.name} should have at least one SEARCH action to perform, since they have a learning goal.'
        assert contains_action_content(actions, 'GPT-3'), f'{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it.'

def test_move_to(fixture_setup):
    """
    Тестирует метод `move_to` агента.

    Проверяет, что агент устанавливает новое местоположение и контекст
    в своей конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.move_to('New York', context=['city', 'busy', 'diverse'])
        assert agent._configuration['current_location'] == 'New York', f'{agent.name} should have New York as the current location.'
        assert 'city' in agent._configuration['current_context'], f'{agent.name} should have city as part of the current context.'
        assert 'busy' in agent._configuration['current_context'], f'{agent.name} should have busy as part of the current context.'
        assert 'diverse' in agent._configuration['current_context'], f'{agent.name} should have diverse as part of the current context.'

def test_change_context(fixture_setup):
    """
    Тестирует метод `change_context` агента.

    Проверяет, что агент изменяет свой текущий контекст в конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.change_context(['home', 'relaxed', 'comfortable'])
        assert 'home' in agent._configuration['current_context'], f'{agent.name} should have home as part of the current context.'
        assert 'relaxed' in agent._configuration['current_context'], f'{agent.name} should have relaxed as part of the current context.'
        assert 'comfortable' in agent._configuration['current_context'], f'{agent.name} should have comfortable as part of the current context.'

def test_save_spec(fixture_setup):
    """
    Тестирует методы `save_spec` и `load_spec` агента.

    Проверяет, что агент сохраняет свою спецификацию в файл, а затем может ее загрузить.
    Также проверяет, что загруженный агент имеет ту же конфигурацию, что и оригинальный.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # save to a file
        agent.save_spec(get_relative_to_test_path(f'test_exports/serialization/{agent.name}.tinyperson.json'), include_memory=True)
        # check that the file exists
        assert os.path.exists(get_relative_to_test_path(f'test_exports/serialization/{agent.name}.tinyperson.json')), f'{agent.name} should have saved the file.'
        # load the file to see if the agent is the same. The agent name should be different because it TinyTroupe does not allow two agents with the same name.
        loaded_name = f'{agent.name}_loaded'
        #  Код загружает JSON-файл с использованием j_loads, вместо стандартного json.load
        loaded_agent = TinyPerson.load_spec(get_relative_to_test_path(f'test_exports/serialization/{agent.name}.tinyperson.json'), new_agent_name=loaded_name, json_loader=j_loads)
        # check that the loaded agent is the same as the original
        assert loaded_agent.name == loaded_name, f'{agent.name} should have the same name as the loaded agent.'
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True), f'{agent.name} should have the same configuration as the loaded agent, except for the name.'