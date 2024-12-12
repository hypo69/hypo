## Анализ кода модуля test_tinyperson.py

**Качество кода**
7
- Плюсы
    - Код написан в соответствии с принципами unit-тестирования, каждая функция проверяет конкретную часть функциональности.
    - Использование фикстур pytest для настройки окружения.
    - Применение `logger` для логирования информации.
    - Наличие тестов для основных методов и сценариев, таких как `act`, `listen`, `define`, `socialize`, `see`, `think`, `internalize_goal`, `move_to`, `change_context` и `save_spec`.
    - Проверка сохранения и загрузки состояния агента.
    
- Минусы
    - Отсутствуют docstring у функций.
    - Использование `sys.path.insert` для импорта, что может быть менее явным, чем относительные импорты.
    - Не все утверждения в тестах содержат информативные сообщения об ошибках.
    - Использование `assert` для проверки наличия типов действий и их содержимого, можно улучшить, используя более специализированные функции.
    - Некоторые проверки могут быть более детальными, например, проверка конкретных значений в `current_messages`.
    - Нет обработки исключений при работе с файловой системой при сохранении и загрузке агента.

**Рекомендации по улучшению**

1. **Добавить docstring:**
   - Добавить документацию в формате RST для всех функций.
2. **Использовать относительные импорты:**
   - Вместо `sys.path.insert` использовать относительные импорты, если это возможно.
3. **Уточнить сообщения об ошибках:**
    - Сделать сообщения об ошибках более информативными, указывая, что именно не соответствует ожиданиям.
4. **Улучшить проверки действий:**
    - Использовать более специализированные функции для проверки наличия действий и их содержимого.
5. **Детализировать проверки:**
    - Добавить проверки конкретных значений в `current_messages` и других структурах данных.
6. **Обработка ошибок:**
   - Добавить обработку исключений при работе с файловой системой при сохранении и загрузке агента.
7. **Использовать `j_loads_ns`:**
   - Добавить `j_loads_ns` для загрузки JSON файлов.
8. **Оптимизировать логирование:**
   - Заменить стандартные `assert` на логирование с помощью `logger.error`, чтобы можно было отслеживать проблемы.

**Оптимизированный код**

```python
"""
Модуль для тестирования класса TinyPerson
=========================================================================================

Этот модуль содержит набор тестов для проверки функциональности класса TinyPerson,
включая его способность выполнять действия, слушать, определять значения, взаимодействовать с другими агентами,
воспринимать визуальные стимулы, думать, ставить цели, перемещаться, менять контекст и сохранять/загружать состояние.

Пример использования
--------------------

Примеры тестов:

.. code-block:: python

   test_act(setup)
   test_listen(setup)
   test_define(setup)
"""
import pytest
import os
from src.logger.logger import logger
from typing import Any
#from src.utils.jjson import j_loads_ns
# from src.utils.jjson import j_loads
# import logging
# logger = logging.getLogger("tinytroupe")
import sys
sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation
sys.path.insert(0, '../') # ensures that the package is imported from the parent directory, not the Python installation

#sys.path.append('../../tinytroupe/')
#sys.path.append('../../')
#sys.path.append('..')

from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tinyperson import TinyPerson

from tests.unit.testing_utils import * #import get_relative_to_test_path, contains_action_type, terminates_with_action_type, contains_action_content, agents_configs_are_equal

def test_act(setup):
    """
    Тест проверяет, что агент может выполнять действия на основе входных данных.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод listen_and_act и проверяет возвращаемые действия
        actions = agent.listen_and_act("Tell me a bit about your life.", return_actions=True)

        logger.info(agent.pp_current_interactions())

        # Проверка, что агент выполнил хотя бы одно действие
        if not len(actions) >= 1:
            logger.error(f"{agent.name} should have at least one action to perform (even if it is just DONE).")
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform (even if it is just DONE)."
        # Проверка, что среди действий есть действие TALK
        if not contains_action_type(actions, "TALK"):
             logger.error(f"{agent.name} should have at least one TALK action to perform, since we asked him to do so.")
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we asked him to do so."
        # Проверка, что последовательность действий завершается DONE
        if not terminates_with_action_type(actions, "DONE"):
             logger.error(f"{agent.name} should always terminate with a DONE action.")
        assert terminates_with_action_type(actions, "DONE"), f"{agent.name} should always terminate with a DONE action."

def test_listen(setup):
    """
    Тест проверяет, что агент слушает входные данные и обновляет свои текущие сообщения.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что агент слушает речевой стимул и обновляет свои текущие сообщения
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод listen
        agent.listen("Hello, how are you?")

        # Проверка, что в текущих сообщениях есть хотя бы одно сообщение
        if not len(agent.current_messages) > 0:
            logger.error(f"{agent.name} should have at least one message in its current messages.")
        assert len(agent.current_messages) > 0, f"{agent.name} should have at least one message in its current messages."
        # Проверка, что последнее сообщение имеет роль 'user'
        if not agent.episodic_memory.retrieve_all()[-1]['role'] == 'user':
             logger.error(f"{agent.name} should have the last message as \'user\'.")
        assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user', f"{agent.name} should have the last message as \'user\'."
        # Проверка, что последнее сообщение имеет тип стимула 'CONVERSATION'
        if not agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION':
             logger.error(f"{agent.name} should have the last message as a \'CONVERSATION\' stimulus.")
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION', f"{agent.name} should have the last message as a \'CONVERSATION\' stimulus."
        # Проверка, что последнее сообщение содержит правильный контент
        if not agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?':
             logger.error(f"{agent.name} should have the last message with the correct content.")
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?', f"{agent.name} should have the last message with the correct content."

def test_define(setup):
    """
    Тест проверяет, что агент устанавливает значения в свою конфигурацию и сбрасывает свой промпт.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что агент определяет значение в своей конфигурации и сбрасывает свой промпт
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код сохраняет исходный промпт
        original_prompt = agent.current_messages[0]['content']

        # Код определяет новое значение
        agent.define('age', 25)

        # Проверка, что конфигурация имеет новое значение
        if not agent._configuration['age'] == 25:
             logger.error(f"{agent.name} should have the age set to 25.")
        assert agent._configuration['age'] == 25, f"{agent.name} should have the age set to 25."
        # Проверка, что промпт изменился
        if not agent.current_messages[0]['content'] != original_prompt:
             logger.error(f"{agent.name} should have a different prompt after defining a new value.")
        assert agent.current_messages[0]['content'] != original_prompt, f"{agent.name} should have a different prompt after defining a new value."
        # Проверка, что промпт содержит новое значение
        if not '25' in agent.current_messages[0]['content']:
             logger.error(f"{agent.name} should have the age in the prompt.")
        assert '25' in agent.current_messages[0]['content'], f"{agent.name} should have the age in the prompt."

def test_define_several(setup):
    """
    Тест проверяет, что определение нескольких значений в группе работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что определение нескольких значений в группе работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код определяет несколько значений в группе
        agent.define_several(group="skills", records=["Python", "Machine learning", "GPT-3"])
        # Проверка, что в конфигурации есть Python
        if not "Python" in agent._configuration["skills"]:
             logger.error(f"{agent.name} should have Python as a skill.")
        assert "Python" in agent._configuration["skills"], f"{agent.name} should have Python as a skill."
        # Проверка, что в конфигурации есть Machine learning
        if not "Machine learning" in agent._configuration["skills"]:
             logger.error(f"{agent.name} should have Machine learning as a skill.")
        assert "Machine learning" in agent._configuration["skills"], f"{agent.name} should have Machine learning as a skill."
        # Проверка, что в конфигурации есть GPT-3
        if not "GPT-3" in agent._configuration["skills"]:
             logger.error(f"{agent.name} should have GPT-3 as a skill.")
        assert "GPT-3" in agent._configuration["skills"], f"{agent.name} should have GPT-3 as a skill."

def test_socialize(setup):
    """
    Тест проверяет, что взаимодействие с другим агентом работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что социализация с другим агентом работает как ожидается
    an_oscar = create_oscar_the_architect()
    a_lisa = create_lisa_the_data_scientist()
    for agent in [an_oscar, a_lisa]:
        # Код определяет другого агента
        other = a_lisa if agent.name == "Oscar" else an_oscar
        # Код делает другого агента доступным
        agent.make_agent_accessible(other, relation_description="My friend")
        # Код слушает сообщение
        agent.listen(f"Hi {agent.name}, I am {other.name}.")
        # Код вызывает метод act и проверяет возвращаемые действия
        actions = agent.act(return_actions=True)
        # Проверка, что агент выполнил хотя бы одно действие
        if not len(actions) >= 1:
            logger.error(f"{agent.name} should have at least one action to perform.")
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Проверка, что среди действий есть TALK
        if not contains_action_type(actions, "TALK"):
             logger.error(f"{agent.name} should have at least one TALK action to perform, since we started a conversation.")
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we started a conversation."
        # Проверка, что в контенте действия есть имя другого агента
        if not contains_action_content(actions, other.name):
             logger.error(f"{agent.name} should mention {other.name} in the TALK action, since they are friends.")
        assert contains_action_content(actions, other.name), f"{agent.name} should mention {other.name} in the TALK action, since they are friends."

def test_see(setup):
    """
    Тест проверяет, что восприятие визуального стимула работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что восприятие визуального стимула работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод see
        agent.see("A beautiful sunset over the ocean.")
        # Код вызывает метод act и проверяет возвращаемые действия
        actions = agent.act(return_actions=True)
        # Проверка, что агент выполнил хотя бы одно действие
        if not len(actions) >= 1:
            logger.error(f"{agent.name} should have at least one action to perform.")
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Проверка, что среди действий есть THINK
        if not contains_action_type(actions, "THINK"):
             logger.error(f"{agent.name} should have at least one THINK action to perform, since they saw something interesting.")
        assert contains_action_type(actions, "THINK"), f"{agent.name} should have at least one THINK action to perform, since they saw something interesting."
        # Проверка, что в контенте действия есть упоминание заката
        if not contains_action_content(actions, "sunset"):
            logger.error(f"{agent.name} should mention the sunset in the THINK action, since they saw it.")
        assert contains_action_content(actions, "sunset"), f"{agent.name} should mention the sunset in the THINK action, since they saw it."

def test_think(setup):
    """
    Тест проверяет, что размышление о чем-либо работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что размышление о чем-либо работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод think
        agent.think("I will tell everyone right now how awesome life is!")
        # Код вызывает метод act и проверяет возвращаемые действия
        actions = agent.act(return_actions=True)
        # Проверка, что агент выполнил хотя бы одно действие
        if not len(actions) >= 1:
             logger.error(f"{agent.name} should have at least one action to perform.")
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Проверка, что среди действий есть TALK
        if not contains_action_type(actions, "TALK"):
             logger.error(f"{agent.name} should have at least one TALK action to perform, since they are eager to talk.")
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since they are eager to talk."
        # Проверка, что в контенте действия есть упоминание жизни
        if not contains_action_content(actions, "life"):
            logger.error(f"{agent.name} should mention life in the TALK action, since they thought about it.")
        assert contains_action_content(actions, "life"), f"{agent.name} should mention life in the TALK action, since they thought about it."

def test_internalize_goal(setup):
    """
    Тест проверяет, что усвоение цели работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что усвоение цели работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод internalize_goal
        agent.internalize_goal("I want to learn more about GPT-3.")
        # Код вызывает метод act и проверяет возвращаемые действия
        actions = agent.act(return_actions=True)
        # Проверка, что агент выполнил хотя бы одно действие
        if not len(actions) >= 1:
            logger.error(f"{agent.name} should have at least one action to perform.")
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Проверка, что среди действий есть SEARCH
        if not contains_action_type(actions, "SEARCH"):
            logger.error(f"{agent.name} should have at least one SEARCH action to perform, since they have a learning goal.")
        assert contains_action_type(actions, "SEARCH"), f"{agent.name} should have at least one SEARCH action to perform, since they have a learning goal."
        # Проверка, что в контенте действия есть упоминание GPT-3
        if not contains_action_content(actions, "GPT-3"):
            logger.error(f"{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it.")
        assert contains_action_content(actions, "GPT-3"), f"{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it."

def test_move_to(setup):
    """
    Тест проверяет, что перемещение в новое местоположение работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что перемещение в новое местоположение работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод move_to
        agent.move_to("New York", context=["city", "busy", "diverse"])
        # Проверка, что текущее местоположение установлено как "New York"
        if not agent._configuration["current_location"] == "New York":
            logger.error(f"{agent.name} should have New York as the current location.")
        assert agent._configuration["current_location"] == "New York", f"{agent.name} should have New York as the current location."
        # Проверка, что "city" является частью текущего контекста
        if not "city" in agent._configuration["current_context"]:
             logger.error(f"{agent.name} should have city as part of the current context.")
        assert "city" in agent._configuration["current_context"], f"{agent.name} should have city as part of the current context."
        # Проверка, что "busy" является частью текущего контекста
        if not "busy" in agent._configuration["current_context"]:
             logger.error(f"{agent.name} should have busy as part of the current context.")
        assert "busy" in agent._configuration["current_context"], f"{agent.name} should have busy as part of the current context."
        # Проверка, что "diverse" является частью текущего контекста
        if not "diverse" in agent._configuration["current_context"]:
             logger.error(f"{agent.name} should have diverse as part of the current context.")
        assert "diverse" in agent._configuration["current_context"], f"{agent.name} should have diverse as part of the current context."

def test_change_context(setup):
    """
    Тест проверяет, что изменение контекста работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    # Тест, что изменение контекста работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код вызывает метод change_context
        agent.change_context(["home", "relaxed", "comfortable"])
        # Проверка, что "home" является частью текущего контекста
        if not "home" in agent._configuration["current_context"]:
            logger.error(f"{agent.name} should have home as part of the current context.")
        assert "home" in agent._configuration["current_context"], f"{agent.name} should have home as part of the current context."
        # Проверка, что "relaxed" является частью текущего контекста
        if not "relaxed" in agent._configuration["current_context"]:
            logger.error(f"{agent.name} should have relaxed as part of the current context.")
        assert "relaxed" in agent._configuration["current_context"], f"{agent.name} should have relaxed as part of the current context."
        # Проверка, что "comfortable" является частью текущего контекста
        if not "comfortable" in agent._configuration["current_context"]:
             logger.error(f"{agent.name} should have comfortable as part of the current context.")
        assert "comfortable" in agent._configuration["current_context"], f"{agent.name} should have comfortable as part of the current context."

def test_save_spec(setup):
    """
    Тест проверяет, что сохранение и загрузка спецификации агента работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код сохраняет спецификацию в файл
        file_path = get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json")
        agent.save_spec(file_path, include_memory=True)

        # Проверка, что файл существует
        if not os.path.exists(file_path):
            logger.error(f"{agent.name} should have saved the file.")
        assert os.path.exists(file_path), f"{agent.name} should have saved the file."

        # Код загружает спецификацию из файла
        loaded_name = f"{agent.name}_loaded"
        try:
            loaded_agent = TinyPerson.load_spec(file_path, new_agent_name=loaded_name)
        except Exception as e:
            logger.error(f"Error loading agent from file: {file_path}", exc_info=True)
            raise

        # Проверка, что имя загруженного агента соответствует
        if not loaded_agent.name == loaded_name:
             logger.error(f"{agent.name} should have the same name as the loaded agent.")
        assert loaded_agent.name == loaded_name, f"{agent.name} should have the same name as the loaded agent."
        # Проверка, что конфигурации агентов идентичны
        if not agents_configs_are_equal(agent, loaded_agent, ignore_name=True):
             logger.error(f"{agent.name} should have the same configuration as the loaded agent, except for the name.")
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True), f"{agent.name} should have the same configuration as the loaded agent, except for the name."