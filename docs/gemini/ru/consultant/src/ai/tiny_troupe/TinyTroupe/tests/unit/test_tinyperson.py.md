# Анализ кода модуля `test_tinyperson`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, каждый тест выполняет конкретную задачу.
    - Используются `assert` для проверки условий, что облегчает отладку.
    - Присутствуют комментарии, поясняющие логику тестов.
    - Применяется параметризация тестов для запуска с разными агентами.
-  Минусы
    -  Импорты модуля `logger` и `j_loads` отсутствуют.
    -  Необходимо добавить docstring к функциям.
    -  Пути в `sys.path` могут быть упрощены.
    -  Использование `logger` не унифицировано.
    -  Проверка конфигурации агентов вынесена в отдельную функцию `agents_configs_are_equal` без документации.

**Рекомендации по улучшению**
1.  Добавить импорты `logger` и `j_loads` из `src.logger` и `src.utils.jjson`.
2.  Добавить docstring к каждой тестовой функции, а также к вспомогательной функции `agents_configs_are_equal`.
3.  Упростить пути в `sys.path`.
4.  Использовать `logger.info`, `logger.debug` и `logger.error` для унификации логирования.
5.  Избегать явного использования `os.path.exists` - добавить обертку.
6.  Добавить ассерты для проверки загруженного агента, исключая проверку памяти.
7.  Улучшить читаемость ассертов, добавив больше контекста.

**Оптимизированный код**
```python
"""
Модуль для тестирования класса TinyPerson
=========================================================================================

Этот модуль содержит набор тестов для проверки функциональности класса TinyPerson,
включая действия, прослушивание, определение, социализацию и другие аспекты поведения агентов.

Пример использования
--------------------

Примеры использования функций тестирования:

.. code-block:: python

    pytest.main(['-v', 'test_tinyperson.py'])
"""
import pytest
import os
from pathlib import Path
import sys

# Путь к директории проекта для импорта
PROJECT_PATH = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_PATH))

from src.logger.logger import logger
from src.utils.jjson import j_loads  # Используем j_loads для загрузки json файлов


from tinytroupe.examples import create_oscar_the_architect, create_lisa_the_data_scientist
from tinytroupe.tinyperson import TinyPerson


def get_relative_to_test_path(relative_path):
    """
    Возвращает абсолютный путь относительно текущей директории с тестами.

    Args:
        relative_path (str): Относительный путь к файлу.

    Returns:
        str: Абсолютный путь к файлу.

    Example:
        >>> get_relative_to_test_path("test_file.txt")
        '/absolute/path/to/tests/test_file.txt'
    """
    return str(Path(__file__).resolve().parent / relative_path)


def contains_action_type(actions, action_type):
    """
    Проверяет, содержит ли список действий хотя бы одно действие с заданным типом.

    Args:
        actions (list): Список действий.
        action_type (str): Тип действия для поиска.

    Returns:
        bool: True, если действие найдено, иначе False.
    """
    return any(action['type'] == action_type for action in actions)


def contains_action_content(actions, content):
    """
    Проверяет, содержит ли список действий хотя бы одно действие с заданным содержимым.

    Args:
        actions (list): Список действий.
        content (str): Содержание для поиска.

    Returns:
         bool: True, если действие найдено, иначе False.
    """
    return any(content in action['content'] for action in actions)


def terminates_with_action_type(actions, action_type):
    """
    Проверяет, заканчивается ли список действий действием с заданным типом.

    Args:
        actions (list): Список действий.
        action_type (str): Тип действия для проверки.

    Returns:
        bool: True, если последнее действие имеет заданный тип, иначе False.
    """
    return actions[-1]['type'] == action_type


def agents_configs_are_equal(agent1, agent2, ignore_name=False, ignore_memory=True):
    """
    Сравнивает конфигурации двух агентов.

    Args:
        agent1 (TinyPerson): Первый агент.
        agent2 (TinyPerson): Второй агент.
        ignore_name (bool, optional): Игнорировать имя при сравнении. Defaults to False.
        ignore_memory (bool, optional): Игнорировать память агента при сравнении. Defaults to True.

    Returns:
         bool: True, если конфигурации агентов равны, False в противном случае.
    """
    config1 = agent1._configuration
    config2 = agent2._configuration

    if ignore_name:
        config1 = {k: v for k, v in config1.items() if k != 'name'}
        config2 = {k: v for k, v in config2.items() if k != 'name'}

    if not ignore_memory:
        config1['episodic_memory'] = agent1.episodic_memory.retrieve_all()
        config2['episodic_memory'] = agent2.episodic_memory.retrieve_all()


    return config1 == config2



@pytest.fixture
def setup():
    """
    Фикстура для настройки тестовой среды.
    """
    logger.info("Setting up test environment.")
    yield
    logger.info("Tearing down test environment.")


def test_act(setup):
    """
    Тестирует, что агент выполняет действия на основе запроса.

    Проверяется, что агент возвращает хотя бы одно действие,
    содержит действие типа TALK и завершается действием DONE.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        actions = agent.listen_and_act('Tell me a bit about your life.', return_actions=True)
        logger.info(agent.pp_current_interactions())

        assert len(actions) >= 1, f"{agent.name} должен выполнить хотя бы одно действие (даже если это DONE)."
        assert contains_action_type(actions, 'TALK'), f"{agent.name} должен выполнить хотя бы одно действие типа TALK, так как мы его об этом попросили."
        assert terminates_with_action_type(actions, 'DONE'), f"{agent.name} должен всегда завершать действия типом DONE."


def test_listen(setup):
    """
    Тестирует, что агент прослушивает стимул и обновляет свои сообщения.

    Проверяется, что агент добавляет сообщение в текущие сообщения,
    что последнее сообщение имеет роль 'user',
    тип стимула 'CONVERSATION' и правильное содержание.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.listen('Hello, how are you?')

        assert len(agent.current_messages) > 0, f"{agent.name} должен иметь хотя бы одно сообщение в текущих сообщениях."
        assert agent.episodic_memory.retrieve_all()[-1]['role'] == 'user', f"{agent.name} должен иметь последнее сообщение с ролью 'user'."
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['type'] == 'CONVERSATION', f"{agent.name} должен иметь последнее сообщение со стимулом типа 'CONVERSATION'."
        assert agent.episodic_memory.retrieve_all()[-1]['content']['stimuli'][0]['content'] == 'Hello, how are you?', f"{agent.name} должен иметь последнее сообщение с правильным содержанием."


def test_define(setup):
    """
    Тестирует, что агент определяет значение в своей конфигурации и сбрасывает промпт.

    Проверяется, что агент сохраняет новое значение в конфигурации,
    что промпт изменился и содержит новое значение.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        original_prompt = agent.current_messages[0]['content']

        agent.define('age', 25)

        assert agent._configuration['age'] == 25, f"{agent.name} должен иметь возраст 25."
        assert agent.current_messages[0]['content'] != original_prompt, f"{agent.name} должен иметь другой промпт после определения нового значения."
        assert '25' in agent.current_messages[0]['content'], f"{agent.name} должен иметь возраст в промпте."


def test_define_several(setup):
    """
    Тестирует, что определение нескольких значений для группы работает ожидаемо.

    Проверяется, что агент добавляет все значения в указанную группу конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.define_several(group='skills', records=['Python', 'Machine learning', 'GPT-3'])
        assert 'Python' in agent._configuration['skills'], f"{agent.name} должен иметь Python в списке навыков."
        assert 'Machine learning' in agent._configuration['skills'], f"{agent.name} должен иметь Machine learning в списке навыков."
        assert 'GPT-3' in agent._configuration['skills'], f"{agent.name} должен иметь GPT-3 в списке навыков."


def test_socialize(setup):
    """
    Тестирует, что социализация агента с другим агентом работает ожидаемо.

    Проверяется, что агент упоминает имя другого агента в действии TALK.
    """
    an_oscar = create_oscar_the_architect()
    a_lisa = create_lisa_the_data_scientist()
    for agent in [an_oscar, a_lisa]:
        other = a_lisa if agent.name == 'Oscar' else an_oscar
        agent.make_agent_accessible(other, relation_description='My friend')
        agent.listen(f'Hi {agent.name}, I am {other.name}.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} должен выполнить хотя бы одно действие."
        assert contains_action_type(actions, 'TALK'), f"{agent.name} должен выполнить хотя бы одно действие TALK, так как мы начали разговор."
        assert contains_action_content(actions, other.name), f"{agent.name} должен упомянуть {other.name} в действии TALK, так как они друзья."


def test_see(setup):
    """
    Тестирует, что агент реагирует на визуальный стимул.

    Проверяется, что агент выполняет действие THINK,
    когда видит что-то интересное.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.see('A beautiful sunset over the ocean.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} должен выполнить хотя бы одно действие."
        assert contains_action_type(actions, 'THINK'), f"{agent.name} должен выполнить хотя бы одно действие типа THINK, так как он увидел что-то интересное."
        assert contains_action_content(actions, 'sunset'), f"{agent.name} должен упомянуть sunset в действии THINK, так как он это увидел."


def test_think(setup):
    """
    Тестирует, что агент выполняет действие на основе своей мысли.

    Проверяется, что агент выполняет действие TALK,
    после того как подумал о чем-то.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.think('I will tell everyone right now how awesome life is!')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} должен выполнить хотя бы одно действие."
        assert contains_action_type(actions, 'TALK'), f"{agent.name} должен выполнить хотя бы одно действие TALK, так как он хочет поговорить."
        assert contains_action_content(actions, 'life'), f"{agent.name} должен упомянуть life в действии TALK, так как он об этом подумал."


def test_internalize_goal(setup):
    """
    Тестирует, что агент интернализирует цель.

    Проверяется, что агент выполняет действие SEARCH
    после определения новой цели.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.internalize_goal('I want to learn more about GPT-3.')
        actions = agent.act(return_actions=True)
        assert len(actions) >= 1, f"{agent.name} должен выполнить хотя бы одно действие."
        assert contains_action_type(actions, 'SEARCH'), f"{agent.name} должен выполнить хотя бы одно действие типа SEARCH, так как у него есть цель обучения."
        assert contains_action_content(actions, 'GPT-3'), f"{agent.name} должен упомянуть GPT-3 в действии SEARCH, так как он хочет узнать об этом больше."


def test_move_to(setup):
    """
    Тестирует, что агент перемещается в новое место.

    Проверяется, что агент устанавливает новое местоположение
    и контекст в своей конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.move_to('New York', context=['city', 'busy', 'diverse'])
        assert agent._configuration['current_location'] == 'New York', f"{agent.name} должен иметь New York в качестве текущего местоположения."
        assert 'city' in agent._configuration['current_context'], f"{agent.name} должен иметь city в текущем контексте."
        assert 'busy' in agent._configuration['current_context'], f"{agent.name} должен иметь busy в текущем контексте."
        assert 'diverse' in agent._configuration['current_context'], f"{agent.name} должен иметь diverse в текущем контексте."


def test_change_context(setup):
    """
    Тестирует, что агент меняет свой контекст.

    Проверяется, что агент устанавливает новый контекст в своей конфигурации.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        agent.change_context(['home', 'relaxed', 'comfortable'])
        assert 'home' in agent._configuration['current_context'], f"{agent.name} должен иметь home в текущем контексте."
        assert 'relaxed' in agent._configuration['current_context'], f"{agent.name} должен иметь relaxed в текущем контексте."
        assert 'comfortable' in agent._configuration['current_context'], f"{agent.name} должен иметь comfortable в текущем контексте."


def test_save_spec(setup):
    """
    Тестирует, что агент сохраняет свою спецификацию в файл и может загрузить ее.

    Проверяется, что агент сохраняет файл спецификации,
    и что загруженный агент имеет те же параметры.
    """
    for agent in [create_oscar_the_architect(), create_lisa_the_data_scientist()]:
        file_path = get_relative_to_test_path(f'test_exports/serialization/{agent.name}.tinyperson.json')
        agent.save_spec(file_path, include_memory=True)

        # проверка существования файла
        if not Path(file_path).exists():
             logger.error(f"Файл {file_path} не был создан.")
             assert False, f"{agent.name} не сохранил файл."

        loaded_name = f"{agent.name}_loaded"
        loaded_agent = TinyPerson.load_spec(file_path, new_agent_name=loaded_name)
        assert loaded_agent.name == loaded_name, f"{agent.name} должен иметь то же имя, что и у загруженного агента."
        assert agents_configs_are_equal(agent, loaded_agent, ignore_name=True, ignore_memory=True), f"{agent.name} должен иметь ту же конфигурацию, что и загруженный агент, за исключением имени и памяти."
```