## Анализ кода модуля test_tinyperson

**Качество кода**
**7/10**
 -  Плюсы
    - Код покрывает основные функциональности агентов, включая действия, прослушивание, определение параметров, взаимодействие и т.д.
    - Присутствуют assert для проверки ожидаемого поведения.
    - Используются helper-функции для проверок (например, `contains_action_type`, `contains_action_content`, `agents_configs_are_equal`).
 -  Минусы
    - Отсутствует документация в формате reStructuredText (RST) для модуля, классов и функций.
    - Присутствует избыточное добавление путей в `sys.path` и закомментированные строки с аналогичным функционалом.
    - Не используется `from src.logger.logger import logger` для логирования.
    - Дублирование кода при создании агентов.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring в формате reStructuredText (RST) для всех модулей, функций и классов.
2.  **Импорты:** Оптимизировать импорты, убрать лишние добавления путей в `sys.path` и дублирование кода.
3.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
4.  **Рефакторинг:** Убрать дублирование кода при создании агентов, например, через параметризацию.
5.  **Сообщения об ошибках:** Сделать сообщения об ошибках более информативными.

**Оптимизированный код**
```python
"""
Модуль содержит юнит-тесты для проверки функциональности агента TinyPerson.
=========================================================================================

Этот модуль включает тесты для различных аспектов поведения агентов, таких как действия, прослушивание,
определение параметров, социализация, взаимодействие с окружением и т.д.

Пример использования
--------------------

Примеры тестов, включенных в этот модуль:

- :func:`test_act` проверяет, что агент может действовать и возвращать корректные действия.
- :func:`test_listen` проверяет, что агент может слушать и сохранять сообщения.
- :func:`test_define` проверяет, что агент может определять параметры и обновлять свой промпт.
- и другие.
"""
import pytest
import os
# from src.logger.logger import logger  # TODO: Раскомментировать после создания logger
import sys

# TODO: Убрать лишние добавления путей.
sys.path.insert(0, '../../tinytroupe/')
sys.path.insert(0, '../../')
sys.path.insert(0, '../')

from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tinyperson import TinyPerson  # Добавлен импорт класса TinyPerson
from testing_utils import *

import logging
logger = logging.getLogger("tinytroupe")

# TODO: Добавить документацию в формате RST.
def test_act(setup):
    """
    Тестирует способность агента выполнять действия и возвращать корректные результаты.
    
    Проверяет, что агент возвращает хотя бы одно действие, действие типа TALK и заканчивает действия DONE.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код отправляет запрос агенту и получает список действий
        actions = agent.listen_and_act("Tell me a bit about your life.", return_actions=True)

        logger.info(agent.pp_current_interactions())

        # Код проверяет, что список действий не пуст
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform (even if it is just DONE)."
        # Код проверяет, что в списке есть действие типа TALK
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we asked him to do so."
        # Код проверяет, что список действий завершается действием типа DONE
        assert terminates_with_action_type(actions, "DONE"), f"{agent.name} should always terminate with a DONE action."

# TODO: Добавить документацию в формате RST.
def test_listen(setup):
    """
    Тестирует способность агента слушать и обновлять свои текущие сообщения.

    Проверяет, что агент сохраняет входящее сообщение пользователя и корректно интерпретирует его.
    """
    # Код тестирует, что агент слушает и обновляет свои текущие сообщения
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код отправляет сообщение агенту
        agent.listen("Hello, how are you?")

        # Код проверяет, что текущие сообщения агента не пусты
        assert len(agent.current_messages) > 0, f"{agent.name} should have at least one message in its current messages."
        # Код проверяет, что последнее сообщение имеет роль "user"
        assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user', f"{agent.name} should have the last message as 'user'."
        # Код проверяет, что последнее сообщение имеет тип CONVERSATION
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION', f"{agent.name} should have the last message as a 'CONVERSATION' stimulus."
        # Код проверяет, что последнее сообщение содержит правильный текст
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?', f"{agent.name} should have the last message with the correct content."

# TODO: Добавить документацию в формате RST.
def test_define(setup):
    """
    Тестирует способность агента определять значения в своей конфигурации и обновлять промпт.
    
    Проверяет, что агент корректно сохраняет новые значения и изменяет свой промпт.
    """
    # Код тестирует, что агент определяет значение в своей конфигурации и сбрасывает свой промпт
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код сохраняет исходный промпт
        original_prompt = agent.current_messages[0]['content']

        # Код определяет новое значение
        agent.define('age', 25)

        # Код проверяет, что конфигурация содержит новое значение
        assert agent._configuration['age'] == 25, f"{agent.name} should have the age set to 25."

        # Код проверяет, что промпт был изменен
        assert agent.current_messages[0]['content'] != original_prompt, f"{agent.name} should have a different prompt after defining a new value."

        # Код проверяет, что промпт содержит новое значение
        assert '25' in agent.current_messages[0]['content'], f"{agent.name} should have the age in the prompt."

# TODO: Добавить документацию в формате RST.
def test_define_several(setup):
    """
    Тестирует способность агента определять несколько значений для группы.
    
    Проверяет, что все значения корректно сохраняются в конфигурации агента.
    """
    # Код тестирует, что определение нескольких значений для группы работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код определяет несколько значений для группы "skills"
        agent.define_several(group="skills", records=["Python", "Machine learning", "GPT-3"])
        # Код проверяет, что значения были добавлены в конфигурацию
        assert "Python" in agent._configuration["skills"], f"{agent.name} should have Python as a skill."
        assert "Machine learning" in agent._configuration["skills"], f"{agent.name} should have Machine learning as a skill."
        assert "GPT-3" in agent._configuration["skills"], f"{agent.name} should have GPT-3 as a skill."

# TODO: Добавить документацию в формате RST.
def test_socialize(setup):
    """
    Тестирует способность агента взаимодействовать с другим агентом.
    
    Проверяет, что агент может начать разговор и упоминать другого агента в своих действиях.
    """
    # Код тестирует, что социализация с другим агентом работает как ожидается
    an_oscar = create_oscar_the_architect()
    a_lisa = create_lisa_the_data_scientist()
    for agent in [an_oscar, a_lisa]:
        # Код определяет другого агента для взаимодействия
        other = a_lisa if agent.name == "Oscar" else an_oscar
        # Код делает другого агента доступным для взаимодействия
        agent.make_agent_accessible(other, relation_description="My friend")
        # Код начинает взаимодействие
        agent.listen(f"Hi {agent.name}, I am {other.name}.")
        # Код получает действия
        actions = agent.act(return_actions=True)
        # Код проверяет, что есть хотя бы одно действие
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Код проверяет, что есть действие TALK
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since we started a conversation."
        # Код проверяет, что в действии упоминается имя другого агента
        assert contains_action_content(actions, other.name), f"{agent.name} should mention {other.name} in the TALK action, since they are friends."

# TODO: Добавить документацию в формате RST.
def test_see(setup):
    """
    Тестирует способность агента воспринимать визуальные стимулы.

    Проверяет, что агент реагирует на визуальные стимулы и генерирует соответствующие действия.
    """
    # Код тестирует, что просмотр визуального стимула работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код отправляет визуальный стимул агенту
        agent.see("A beautiful sunset over the ocean.")
        # Код получает действия
        actions = agent.act(return_actions=True)
        # Код проверяет, что есть хотя бы одно действие
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Код проверяет, что есть действие THINK
        assert contains_action_type(actions, "THINK"), f"{agent.name} should have at least one THINK action to perform, since they saw something interesting."
        # Код проверяет, что в действии упоминается "sunset"
        assert contains_action_content(actions, "sunset"), f"{agent.name} should mention the sunset in the THINK action, since they saw it."

# TODO: Добавить документацию в формате RST.
def test_think(setup):
    """
    Тестирует способность агента размышлять о чем-либо.
    
    Проверяет, что агент реагирует на размышления и генерирует соответствующие действия.
    """
    # Код тестирует, что размышление о чем-то работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код заставляет агента подумать
        agent.think("I will tell everyone right now how awesome life is!")
        # Код получает действия
        actions = agent.act(return_actions=True)
        # Код проверяет, что есть хотя бы одно действие
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Код проверяет, что есть действие TALK
        assert contains_action_type(actions, "TALK"), f"{agent.name} should have at least one TALK action to perform, since they are eager to talk."
        # Код проверяет, что в действии упоминается "life"
        assert contains_action_content(actions, "life"), f"{agent.name} should mention life in the TALK action, since they thought about it."

# TODO: Добавить документацию в формате RST.
def test_internalize_goal(setup):
    """
    Тестирует способность агента усваивать цели.
    
    Проверяет, что агент реагирует на усвоенную цель и генерирует соответствующие действия.
    """
    # Код тестирует, что усвоение цели работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код устанавливает цель для агента
        agent.internalize_goal("I want to learn more about GPT-3.")
        # Код получает действия
        actions = agent.act(return_actions=True)
        # Код проверяет, что есть хотя бы одно действие
        assert len(actions) >= 1, f"{agent.name} should have at least one action to perform."
        # Код проверяет, что есть действие SEARCH
        assert contains_action_type(actions, "SEARCH"), f"{agent.name} should have at least one SEARCH action to perform, since they have a learning goal."
        # Код проверяет, что в действии упоминается "GPT-3"
        assert contains_action_content(actions, "GPT-3"), f"{agent.name} should mention GPT-3 in the SEARCH action, since they want to learn more about it."

# TODO: Добавить документацию в формате RST.
def test_move_to(setup):
    """
    Тестирует способность агента перемещаться в новое местоположение.
    
    Проверяет, что агент обновляет свое текущее местоположение и контекст.
    """
    # Код тестирует, что перемещение в новое местоположение работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код перемещает агента в "New York"
        agent.move_to("New York", context=["city", "busy", "diverse"])
        # Код проверяет, что местоположение обновлено
        assert agent._configuration["current_location"] == "New York", f"{agent.name} should have New York as the current location."
        # Код проверяет, что контекст содержит "city"
        assert "city" in agent._configuration["current_context"], f"{agent.name} should have city as part of the current context."
        # Код проверяет, что контекст содержит "busy"
        assert "busy" in agent._configuration["current_context"], f"{agent.name} should have busy as part of the current context."
        # Код проверяет, что контекст содержит "diverse"
        assert "diverse" in agent._configuration["current_context"], f"{agent.name} should have diverse as part of the current context."

# TODO: Добавить документацию в формате RST.
def test_change_context(setup):
    """
    Тестирует способность агента изменять контекст.
    
    Проверяет, что агент обновляет свой текущий контекст.
    """
    # Код тестирует, что изменение контекста работает как ожидается
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код изменяет контекст агента
        agent.change_context(["home", "relaxed", "comfortable"])
        # Код проверяет, что контекст содержит "home"
        assert "home" in agent._configuration["current_context"], f"{agent.name} should have home as part of the current context."
        # Код проверяет, что контекст содержит "relaxed"
        assert "relaxed" in agent._configuration["current_context"], f"{agent.name} should have relaxed as part of the current context."
        # Код проверяет, что контекст содержит "comfortable"
        assert "comfortable" in agent._configuration["current_context"], f"{agent.name} should have comfortable as part of the current context."

# TODO: Добавить документацию в формате RST.
def test_save_spec(setup):
    """
    Тестирует способность агента сохранять свою спецификацию в файл.
    
    Проверяет, что агент корректно сохраняет и загружает свою спецификацию.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        # Код сохраняет спецификацию агента в файл
        agent.save_spec(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json"), include_memory=True)

        # Код проверяет, что файл был создан
        assert os.path.exists(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json")), f"{agent.name} should have saved the file."

        # Код загружает спецификацию из файла и создает нового агента
        loaded_name = f"{agent.name}_loaded"
        loaded_agent = TinyPerson.load_spec(get_relative_to_test_path(f"test_exports/serialization/{agent.name}.tinyperson.json"), new_agent_name=loaded_name)

        # Код проверяет, что имя загруженного агента изменилось
        assert loaded_agent.name == loaded_name, f"{agent.name} should have the same name as the loaded agent."
        
        # Код проверяет, что конфигурации агентов совпадают (кроме имени)
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True), f"{agent.name} should have the same configuration as the loaded agent, except for the name."