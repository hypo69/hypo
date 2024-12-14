# Анализ кода модуля testing_utils

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разделен на логические блоки: утилиты, функции проверки, фикстуры.
    - Присутствуют docstring для функций, что делает код понятным.
    - Используются явные типы данных в аннотациях, что улучшает читаемость и предотвращает ошибки.
    - Функции используют понятные имена, отражающие их назначение.
    - Есть функции для тестирования различных аспектов поведения агентов.
- Минусы
    -  Отсутствуют docstring для модуля.
    -  Не используется `logger` для логирования ошибок.
    -  Импорты `sys.path.append` могут быть заменены на более надежные способы определения путей.
    -  Не все функции имеют полные docstring с описанием параметров и возвращаемого значения.
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для работы с JSON.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить `sys.path.append` на более надежные способы определения путей (например, использовать `os.path.abspath` и `os.path.join`).
4.  Дополнить docstring для всех функций, добавив описание параметров и возвращаемых значений в формате RST.
5.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` при работе с JSON, если это применимо.
6.  Избегать избыточного использования `try-except`, где это возможно, заменяя на `logger.error`.

**Оптимизированный код**

```python
"""
Модуль с утилитами для тестирования.
=========================================================================================

Этот модуль предоставляет набор функций и фикстур, полезных для тестирования агентов,
окружений и других компонентов системы. Он включает в себя инструменты для проверки
действий агентов, стимулов, а также для сравнения конфигураций агентов.

Примеры использования
--------------------

.. code-block:: python

    from tests.testing_utils import contains_action_type

    def test_agent_action():
        actions = [{"action": {"type": "some_action"}}]
        assert contains_action_type(actions, "some_action")

"""
import os
import sys
from time import sleep
# sys.path.append('../../tinytroupe/')
# sys.path.append('../../')
# sys.path.append('..')
# Заменено на более надежные методы определения путей
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','tinytroupe')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib
from src.logger.logger import logger # Добавлен импорт logger

# force caching, in order to save on API usage
openai_utils.force_api_cache(True, "tests_cache.pickle")

def contains_action_type(actions: list, action_type: str) -> bool:
    """
    Проверяет, содержит ли данный список действий действие заданного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для поиска.
    :type action_type: str
    :return: True, если действие заданного типа найдено, иначе False.
    :rtype: bool
    """
    # Проходит по списку действий и проверяет тип каждого действия
    for action in actions:
        if action["action"]["type"] == action_type:
            return True
    
    return False

def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Проверяет, содержит ли данный список действий действие с заданным содержимым.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_content: Содержимое действия для поиска.
    :type action_content: str
    :return: True, если действие с заданным содержимым найдено, иначе False.
    :rtype: bool
    """
    # Проходит по списку действий и проверяет наличие содержимого в действии
    for action in actions:
        if action_content.lower() in action["action"]["content"].lower():
            return True
    
    return False

def contains_stimulus_type(stimuli: list, stimulus_type: str) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул заданного типа.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_type: Тип стимула для поиска.
    :type stimulus_type: str
    :return: True, если стимул заданного типа найден, иначе False.
    :rtype: bool
    """
    # Проходит по списку стимулов и проверяет тип каждого стимула
    for stimulus in stimuli:
        if stimulus["type"] == stimulus_type:
            return True
    
    return False

def contains_stimulus_content(stimuli: list, stimulus_content: str) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул с заданным содержимым.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_content: Содержимое стимула для поиска.
    :type stimulus_content: str
    :return: True, если стимул с заданным содержимым найден, иначе False.
    :rtype: bool
    """
    # Проходит по списку стимулов и проверяет наличие содержимого в стимуле
    for stimulus in stimuli:
        if stimulus_content.lower() in stimulus["content"].lower():
            return True
    
    return False

def terminates_with_action_type(actions: list, action_type: str) -> bool:
    """
    Проверяет, завершается ли данный список действий действием заданного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для проверки завершения.
    :type action_type: str
    :return: True, если список завершается действием заданного типа, иначе False.
    :rtype: bool
    """
    # Проверяет, что список действий не пуст и последний элемент имеет заданный тип
    if len(actions) == 0:
        return False
    
    return actions[-1]["action"]["type"] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Проверяет, истинно ли заданное утверждение согласно вызову LLM.
    Используется для проверки текстовых свойств, которые сложно
    проверить механически, например, "текст содержит идеи для продукта".

    :param proposition: Утверждение для проверки.
    :type proposition: str
    :return: True, если утверждение истинно, иначе False.
    :rtype: bool
    :raises Exception: Если LLM возвращает неожиданный результат.
    """
    system_prompt = f"""
    Check whether the following proposition is true or false. If it is
    true, write "true", otherwise write "false". Don\'t write anything else!
    """

    user_prompt = f"""
    Proposition: {proposition}
    """

    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]
    
    # Вызов LLM для проверки утверждения
    try:
        next_message = openai_utils.client().send_message(messages)
    except Exception as ex:
         logger.error('Ошибка при отправке сообщения в LLM', ex)
         return False

    # Проверка результата
    cleaned_message = only_alphanumeric(next_message["content"])
    if cleaned_message.lower().startswith("true"):
        return True
    elif cleaned_message.lower().startswith("false"):
        return False
    else:
        logger.error(f"LLM returned unexpected result: {cleaned_message}")
        raise Exception(f"LLM returned unexpected result: {cleaned_message}")

def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.

    :param string: Исходная строка.
    :type string: str
    :return: Строка, содержащая только буквенно-цифровые символы.
    :rtype: str
    """
    # Фильтрация строки, оставляя только буквенно-цифровые символы
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt: str, system_prompt: str ="You are a helpful AI assistant.") -> list:
    """
    Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.

    :param user_prompt: Текст пользовательского сообщения.
    :type user_prompt: str
    :param system_prompt: Текст системного сообщения.
    :type system_prompt: str
    :return: Список сообщений, содержащий системное и пользовательское сообщение.
    :rtype: list
    """
    messages = [{"role": "system", "content": system_prompt}]
    
    # Добавляет пользовательское сообщение, если оно не None
    if user_prompt is not None:
        messages.append({"role": "user", "content": user_prompt})
    
    return messages

def agents_configs_are_equal(agent1: TinyPerson, agent2: TinyPerson, ignore_name: bool = False) -> bool:
    """
    Проверяет, равны ли конфигурации двух агентов.

    :param agent1: Первый агент для сравнения.
    :type agent1: TinyPerson
    :param agent2: Второй агент для сравнения.
    :type agent2: TinyPerson
    :param ignore_name: Если True, имя агента игнорируется при сравнении.
    :type ignore_name: bool
    :return: True, если конфигурации агентов равны, иначе False.
    :rtype: bool
    """
    ignore_keys = []
    if ignore_name:
        ignore_keys.append("name")
    
    # Проходит по ключам конфигурации первого агента и сравнивает с конфигурацией второго
    for key in agent1._configuration.keys():
        if key in ignore_keys:
            continue
        
        if agent1._configuration[key] != agent2._configuration[key]:
            return False
    
    return True
############################################################################################################
# I/O utilities
############################################################################################################

def remove_file_if_exists(file_path: str):
    """
    Удаляет файл по заданному пути, если он существует.

    :param file_path: Путь к файлу.
    :type file_path: str
    """
    # Проверяет существование файла и удаляет его, если он существует
    if os.path.exists(file_path):
        os.remove(file_path)

def get_relative_to_test_path(path_suffix: str) -> str:
    """
    Возвращает путь к файлу относительно директории с тестами.

    :param path_suffix: Суффикс пути.
    :type path_suffix: str
    :return: Полный путь к файлу.
    :rtype: str
    """
    # Формирует путь к файлу относительно директории с тестами
    return os.path.join(os.path.dirname(__file__), path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope="function")
def focus_group_world():
    """
    Фикстура, создающая тестовый мир с несколькими агентами.

    :return: Экземпляр `TinyWorld` с агентами.
    :rtype: TinyWorld
    """
    import tinytroupe.examples as examples   
    
    # Создает мир с предустановленными агентами
    world = TinyWorld("Focus group", [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope="function")
def setup():
    """
    Фикстура, очищающая агентов и окружения перед каждым тестом.
    """
    # Очищает агентов и окружения перед каждым тестом
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()

    yield