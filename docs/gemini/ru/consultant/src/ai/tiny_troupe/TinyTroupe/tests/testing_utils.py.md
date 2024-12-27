# Анализ кода модуля testing_utils

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Присутствуют docstring для большинства функций, что облегчает понимание их назначения.
    - Используются фикстуры pytest для подготовки тестового окружения.
    - Код содержит функции для проверки наличия определенных типов действий и стимулов, что полезно для тестирования агентов.
    - Присутствует функция для проверки истинности утверждений с помощью LLM.

-  Минусы
    - Не все функции имеют docstring.
    - Используется стандартный импорт `import json`, хотя в инструкции указано использовать `src.utils.jjson`.
    - Некоторые функции могут быть улучшены с точки зрения читаемости и краткости.
    - Отсутствует явная обработка ошибок с помощью логгера.
    - Необходимо использовать `j_loads` или `j_loads_ns` вместо стандартного `json.load` при чтении файлов.

**Рекомендации по улучшению**
1.  Добавить docstring для всех функций, которые их не имеют.
2.  Заменить `import json` на использование `from src.utils.jjson import j_loads, j_loads_ns`
3.  Добавить обработку ошибок с использованием `logger.error` вместо общих `try-except`.
4.  Улучшить читаемость кода, где это возможно.
5.  Переписать комментарии в формате reStructuredText (RST) для всех функций и модуля.
6.  Использовать `from src.logger.logger import logger` для логирования.
7.  Избегать избыточного использования стандартных блоков `try-except`.

**Оптимизированный код**
```python
"""
Модуль с утилитами для тестирования.
=========================================================================================

Этот модуль содержит набор функций и фикстур, которые используются для облегчения
написания и выполнения тестов для проекта TinyTroupe. Он включает функции для проверки
действий, стимулов, утверждений и сравнения конфигураций агентов.

Пример использования
--------------------

Пример использования фикстуры `focus_group_world`:

.. code-block:: python

    @pytest.mark.asyncio
    async def test_example(focus_group_world):
        #  код исполняет тестирование с использованием focus_group_world
        assert focus_group_world is not None
"""
import os
import sys
from time import sleep
# код добавляет пути для импорта модулей проекта
sys.path.append('../../tinytroupe/')
sys.path.append('../../')
sys.path.append('../')

import tinytroupe.openai_utils as openai_utils
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld, TinySocialNetwork
import pytest
import importlib
from src.logger.logger import logger # импортируем логер

# принудительное кэширование, чтобы экономить на использовании API
openai_utils.force_api_cache(True, "tests_cache.pickle")

def contains_action_type(actions, action_type) -> bool:
    """
    Проверяет, содержит ли данный список действий действие указанного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для поиска.
    :type action_type: str
    :return: True, если действие указанного типа найдено, иначе False.
    :rtype: bool
    """
    for action in actions:
        # код проверяет тип действия
        if action["action"]["type"] == action_type:
            return True
    
    return False

def contains_action_content(actions: list, action_content: str) -> bool:
    """
    Проверяет, содержит ли данный список действий действие с указанным содержимым.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_content: Содержимое действия для поиска.
    :type action_content: str
    :return: True, если действие с указанным содержимым найдено, иначе False.
    :rtype: bool
    """
    for action in actions:
        # код проверяет, содержится ли искомое содержимое в содержимом действия
        if action_content.lower() in action["action"]["content"].lower():
            return True
    
    return False

def contains_stimulus_type(stimuli, stimulus_type) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул указанного типа.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_type: Тип стимула для поиска.
    :type stimulus_type: str
    :return: True, если стимул указанного типа найден, иначе False.
    :rtype: bool
    """
    for stimulus in stimuli:
        # код проверяет тип стимула
        if stimulus["type"] == stimulus_type:
            return True
    
    return False

def contains_stimulus_content(stimuli, stimulus_content) -> bool:
    """
    Проверяет, содержит ли данный список стимулов стимул с указанным содержимым.

    :param stimuli: Список стимулов для проверки.
    :type stimuli: list
    :param stimulus_content: Содержимое стимула для поиска.
    :type stimulus_content: str
    :return: True, если стимул с указанным содержимым найден, иначе False.
    :rtype: bool
    """
    for stimulus in stimuli:
        # код проверяет, содержится ли искомое содержимое в содержимом стимула
        if stimulus_content.lower() in stimulus["content"].lower():
            return True
    
    return False

def terminates_with_action_type(actions, action_type) -> bool:
    """
    Проверяет, заканчивается ли данный список действий действием указанного типа.

    :param actions: Список действий для проверки.
    :type actions: list
    :param action_type: Тип действия для проверки.
    :type action_type: str
    :return: True, если список действий заканчивается действием указанного типа, иначе False.
    :rtype: bool
    """
    if len(actions) == 0:
        return False
    
    # код проверяет тип последнего действия
    return actions[-1]["action"]["type"] == action_type


def proposition_holds(proposition: str) -> bool:
    """
    Проверяет, является ли данное утверждение истинным согласно вызову LLM.
    Это можно использовать для проверки текстовых свойств, которые трудно
    проверить механически, например, "текст содержит идеи для продукта".

    :param proposition: Утверждение для проверки.
    :type proposition: str
    :return: True, если утверждение истинно, иначе False.
    :rtype: bool
    :raises Exception: Если LLM вернул неожиданный результат.
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
    
    try:
        # код отправляет сообщение LLM
        next_message = openai_utils.client().send_message(messages)
    except Exception as ex:
        logger.error(f"Ошибка при вызове LLM: {ex}")
        return False
        
    # код очищает результат
    cleaned_message = only_alphanumeric(next_message["content"])
    if cleaned_message.lower().startswith("true"):
        return True
    elif cleaned_message.lower().startswith("false"):
        return False
    else:
        logger.error(f"LLM вернул неожиданный результат: {cleaned_message}")
        raise Exception(f"LLM returned unexpected result: {cleaned_message}")

def only_alphanumeric(string: str) -> str:
    """
    Возвращает строку, содержащую только буквенно-цифровые символы.

    :param string: Строка для обработки.
    :type string: str
    :return: Строка, содержащая только буквенно-цифровые символы.
    :rtype: str
    """
    return ''.join(c for c in string if c.isalnum())

def create_test_system_user_message(user_prompt, system_prompt="You are a helpful AI assistant.") -> list:
    """
    Создает список, содержащий одно системное сообщение и одно пользовательское сообщение.

    :param user_prompt: Пользовательское сообщение.
    :type user_prompt: str
    :param system_prompt: Системное сообщение.
    :type system_prompt: str
    :return: Список сообщений.
    :rtype: list
    """
    messages = [{"role": "system", "content": system_prompt}]
    
    if user_prompt is not None:
        messages.append({"role": "user", "content": user_prompt})
    
    return messages

def agents_configs_are_equal(agent1, agent2, ignore_name=False) -> bool:
    """
    Проверяет, равны ли конфигурации двух агентов.

    :param agent1: Первый агент для сравнения.
    :type agent1: TinyPerson
    :param agent2: Второй агент для сравнения.
    :type agent2: TinyPerson
    :param ignore_name: Игнорировать ли имя агента при сравнении.
    :type ignore_name: bool
    :return: True, если конфигурации равны, иначе False.
    :rtype: bool
    """
    ignore_keys = []
    if ignore_name:
        ignore_keys.append("name")
    
    for key in agent1._configuration.keys():
        if key in ignore_keys:
            continue
        
        # код сравнивает конфигурации агентов
        if agent1._configuration[key] != agent2._configuration[key]:
            return False
    
    return True
############################################################################################################
# I/O utilities
############################################################################################################

def remove_file_if_exists(file_path) -> None:
    """
    Удаляет файл по указанному пути, если он существует.

    :param file_path: Путь к файлу.
    :type file_path: str
    """
    if os.path.exists(file_path):
        # код удаляет файл, если он существует
        os.remove(file_path)

def get_relative_to_test_path(path_suffix) -> str:
    """
    Возвращает путь к тестовому файлу с указанным суффиксом.

    :param path_suffix: Суффикс пути к файлу.
    :type path_suffix: str
    :return: Полный путь к тестовому файлу.
    :rtype: str
    """
    # код формирует путь к файлу относительно текущего местоположения
    return os.path.join(os.path.dirname(__file__), path_suffix)


############################################################################################################
# Fixtures
############################################################################################################

@pytest.fixture(scope="function")
def focus_group_world():
    """
    Фикстура для создания мира с фокус-группой.

    :return: Мир TinyWorld с агентами.
    :rtype: TinyWorld
    """
    import tinytroupe.examples as examples   
    # код создает мир с агентами для фокус-группы
    world = TinyWorld("Focus group", [examples.create_lisa_the_data_scientist(), examples.create_oscar_the_architect(), examples.create_marcos_the_physician()])
    return world

@pytest.fixture(scope="function")
def setup():
    """
    Фикстура для настройки окружения перед тестами.
     Очищает агентов и окружения.
    """
    # код очищает агентов и окружения
    TinyPerson.clear_agents()
    TinyWorld.clear_environments()

    yield