# Анализ кода модуля test_tinyperson.py

**Качество кода**
7
-  Плюсы
    -  Код содержит набор тестов, которые охватывают основные функциональные возможности класса `TinyPerson`.
    -  Используются фикстуры `pytest` для настройки тестового окружения.
    -  Тесты проверяют различные аспекты поведения агентов, такие как прослушивание, действия, определение параметров, социализация и т. д.
    -  Присутствует логирование.
    -  Тесты содержат проверки на корректность типов и содержимого действий.
-  Минусы
    -  Импорты `sys.path` сделаны в обход корректного использования пакетов.
    -  Используется стандартный `logging`, вместо `src.logger.logger`.
    -  Отсутствует документация в формате reStructuredText (RST).
    -  Некоторые блоки `assert` могут быть более информативными.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Исключить манипуляции с `sys.path`, использовать относительные импорты.
    -   Импортировать `logger` из `src.logger.logger`.
2.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) для модуля, классов и функций.
3.  **Логирование**:
    -   Использовать `logger` из `src.logger.logger` для логирования, в том числе и ошибок.
4.  **Assertions**:
    -   Сделать сообщения об ошибках в `assert` более информативными, указывая ожидаемое и фактическое значение.
5.  **Рефакторинг**:
    -   Вынести повторяющийся код в отдельную функцию, где это возможно (например, создание агентов).

**Оптимизированный код**
```python
"""
Модуль содержит тесты для проверки функциональности класса TinyPerson.
======================================================================

Этот модуль использует pytest для тестирования различных аспектов поведения агентов,
таких как прослушивание, действия, определение параметров, социализация и т. д.

Пример использования
--------------------

.. code-block:: python

    pytest test_tinyperson.py
"""
import os
import pytest
# изменен импорт для использования logger
from src.logger.logger import logger
# убран избыточный импорт
# import sys
# sys.path.insert(0, '../../tinytroupe/') # ensures that the package is imported from the parent directory, not the Python installation
# sys.path.insert(0, '../../') # ensures that the package is imported from the parent directory, not the Python installation
# sys.path.insert(0, '..') # ensures that the package is imported from the parent directory, not the Python installation
#
# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('..')

# импортируем необходимые классы
from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tinyperson import TinyPerson # импортируем TinyPerson
from testing_utils import *


def create_agents():
    """
    Создает и возвращает список агентов для тестов.

    :return: Список агентов, включающий `create_oscar_the_architect` и `create_lisa_the_data_scientist`.
    :rtype: list
    """
    return [create_oscar_the_architect(), create_lisa_the_data_scientist()]


def test_act(setup):
    """
    Тестирует действие агента на основе запроса.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        actions = agent.listen_and_act("Tell me a bit about your life.", return_actions=True)
        logger.info(agent.pp_current_interactions()) # логируем текущие взаимодействия агента

        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform (even if it is just DONE), but got {len(actions)}." # проверка, что агент выполнил как минимум одно действие
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, but got {actions}." # проверка, что агент выполнил как минимум одно действие типа TALK
        assert terminates_with_action_type(actions, "DONE"), f"{agent.name} should always terminate with a DONE action, but got {actions}." # проверка, что последнее действие имеет тип DONE


def test_listen(setup):
    """
    Тестирует, что агент слушает сообщение и обновляет свои текущие сообщения.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.listen("Hello, how are you?") # агент слушает сообщение

        assert len(agent.current_messages) > 0, f"{agent.name} should have at least one message in its current messages, but got {len(agent.current_messages)}." # проверка, что у агента есть сообщения
        last_message = agent.episodic_memory.retrieve_all()[-1] # получаем последнее сообщение
        assert last_message['role'] == 'user', f"{agent.name} should have the last message as \'user\', but got {last_message['role']}." # проверка, что роль последнего сообщения - 'user'
        assert last_message['content']['stimuli'][0]['type'] == 'CONVERSATION', f"{agent.name} should have the last message as a \'CONVERSATION\' stimulus, but got {last_message['content']['stimuli'][0]['type']}." # проверка, что тип стимула последнего сообщения - 'CONVERSATION'
        assert last_message['content']['stimuli'][0]['content'] == 'Hello, how are you?', f"{agent.name} should have the last message with the correct content, but got {last_message['content']['stimuli'][0]['content']}." # проверка, что контент последнего сообщения правильный


def test_define(setup):
    """
    Тестирует, что агент определяет значение в своей конфигурации и сбрасывает свой запрос.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        # сохраняем исходный запрос
        original_prompt = agent.current_messages[0]['content']

        # определяем новое значение
        agent.define('age', 25)

        # проверяем, что конфигурация содержит новое значение
        assert agent._configuration['age'] == 25, f"{agent.name} should have the age set to 25, but got {agent._configuration.get('age')}." # проверка значения возраста
        
        # проверяем, что запрос изменился
        assert agent.current_messages[0]['content'] != original_prompt, f"{agent.name} should have a different prompt after defining a new value, but got the same prompt." # проверка изменения запроса

        # проверяем, что запрос содержит новое значение
        assert '25' in agent.current_messages[0]['content'], f"{agent.name} should have the age in the prompt, but it is missing." # проверка наличия возраста в запросе


def test_define_several(setup):
    """
    Тестирует, что определение нескольких значений в группе работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.define_several(group="skills", records=["Python", "Machine learning", "GPT-3"]) # задаем несколько навыков
        assert "Python" in agent._configuration["skills"], f"{agent.name} should have Python as a skill, but it is missing." # проверка наличия навыка Python
        assert "Machine learning" in agent._configuration["skills"], f"{agent.name} should have Machine learning as a skill, but it is missing." # проверка наличия навыка Machine learning
        assert "GPT-3" in agent._configuration["skills"], f"{agent.name} should have GPT-3 as a skill, but it is missing." # проверка наличия навыка GPT-3


def test_socialize(setup):
    """
    Тестирует, что социализация с другим агентом работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    an_oscar = create_oscar_the_architect() # создаем агента Оскар
    a_lisa = create_lisa_the_data_scientist() # создаем агента Лиза
    for agent in [an_oscar, a_lisa]: # для каждого агента
        other = a_lisa if agent.name == "Oscar" else an_oscar # определяем другого агента
        agent.make_agent_accessible(other, relation_description="My friend") # делаем другого агента доступным
        agent.listen(f"Hi {agent.name}, I am {other.name}.") # агент слушает сообщение
        actions = agent.act(return_actions=True) # агент действует
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform, but got {len(actions)}." # проверка, что агент выполнил действие
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we started a conversation, but got {actions}." # проверка, что действие имеет тип TALK
        assert contains_action_content(actions, other.name), f"{agent.name} should mention {other.name} in the TALK action, since they are friends, but got {actions}." # проверка, что в действии упоминается имя другого агента


def test_see(setup):
    """
    Тестирует, что восприятие визуального стимула работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.see("A beautiful sunset over the ocean.") # агент видит стимул
        actions = agent.act(return_actions=True) # агент действует
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform, but got {len(actions)}." # проверка, что агент выполнил действие
        assert contains_action_type(actions, "THINK"), f"{agent.name} should have at least one THINK action to perform, since they saw something interesting, but got {actions}." # проверка, что действие имеет тип THINK
        assert contains_action_content(actions, "sunset"), f"{agent.name} should mention the sunset in the THINK action, since they saw it, but got {actions}." # проверка, что в действии упоминается закат


def test_think(setup):
    """
    Тестирует, что размышление о чем-то работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.think("I will tell everyone right now how awesome life is!") # агент размышляет
        actions = agent.act(return_actions=True) # агент действует
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform, but got {len(actions)}." # проверка, что агент выполнил действие
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since they are eager to talk, but got {actions}." # проверка, что действие имеет тип TALK
        assert contains_action_content(actions, "life"), f"{agent.name} should mention life in the TALK action, since they thought about it, but got {actions}." # проверка, что в действии упоминается жизнь


def test_internalize_goal(setup):
    """
    Тестирует, что принятие цели работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.internalize_goal("I want to learn more about GPT-3.") # агент принимает цель
        actions = agent.act(return_actions=True) # агент действует
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform, but got {len(actions)}." # проверка, что агент выполнил действие
        assert contains_action_type(actions, "SEARCH"), f"{agent.name} should have at least one SEARCH action to perform, since they have a learning goal, but got {actions}." # проверка, что действие имеет тип SEARCH
        assert contains_action_content(actions, "GPT-3"), f"{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it, but got {actions}." # проверка, что в действии упоминается GPT-3


def test_move_to(setup):
    """
    Тестирует, что перемещение в новое местоположение работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.move_to("New York", context=["city", "busy", "diverse"]) # агент перемещается
        assert agent._configuration["current_location"] == "New York", f"{agent.name} should have New York as the current location, but got {agent._configuration.get('current_location')}." # проверка, что текущее местоположение - New York
        assert "city" in agent._configuration["current_context"], f"{agent.name} should have city as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "city" в текущем контексте
        assert "busy" in agent._configuration["current_context"], f"{agent.name} should have busy as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "busy" в текущем контексте
        assert "diverse" in agent._configuration["current_context"], f"{agent.name} should have diverse as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "diverse" в текущем контексте


def test_change_context(setup):
    """
    Тестирует, что изменение контекста работает корректно.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        agent.change_context(["home", "relaxed", "comfortable"]) # агент изменяет контекст
        assert "home" in agent._configuration["current_context"], f"{agent.name} should have home as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "home" в текущем контексте
        assert "relaxed" in agent._configuration["current_context"], f"{agent.name} should have relaxed as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "relaxed" в текущем контексте
        assert "comfortable" in agent._configuration["current_context"], f"{agent.name} should have comfortable as part of the current context, but got {agent._configuration.get('current_context')}." # проверка наличия "comfortable" в текущем контексте


def test_save_spec(setup):
    """
    Тестирует сохранение и загрузку спецификации агента.

    :param setup: Фикстура pytest для настройки тестового окружения.
    """
    for agent in create_agents():
        # сохраняем в файл
        file_path = get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json")
        agent.save_spec(file_path, include_memory=True)

        # проверяем, что файл существует
        assert os.path.exists(file_path), f"{agent.name} should have saved the file, but it is missing." # проверка, что файл существует

        # загружаем файл, чтобы проверить, что агент такой же. Имя агента должно быть другим, так как TinyTroupe не допускает двух агентов с одним и тем же именем.
        loaded_name = f"{agent.name}_loaded"
        loaded_agent = TinyPerson.load_spec(file_path, new_agent_name=loaded_name)

        # проверяем, что загруженный агент такой же, как и исходный
        assert loaded_agent.name == loaded_name, f"{agent.name} should have the same name as the loaded agent, but got {loaded_agent.name}." # проверка имени загруженного агента
        
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True), f"{agent.name} should have the same configuration as the loaded agent, except for the name, but got different configuration." # проверка конфигурации загруженного агента