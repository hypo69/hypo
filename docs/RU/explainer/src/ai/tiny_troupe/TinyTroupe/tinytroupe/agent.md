# Объяснение кода TinyTroupe/agent.py

```
"""
This module provides the main classes and functions for TinyTroupe's agents.

Agents are the key abstraction used in TinyTroupe. An agent is a simulated person or entity that can interact with other agents and the environment, by
receiving stimuli and producing actions. Agents have cognitive states, which are updated as they interact with the environment and other agents. 
Agents can also store and retrieve information from memory, and can perform actions in the environment. Different from agents whose objective is to
provide support for AI-based assistants or other such productivity tools, **TinyTroupe agents are aim at representing human-like behavior**, which includes
idiossincracies, emotions, and other human-like traits, that one would not expect from a productivity tool.

The overall underlying design is inspired mainly by cognitive psychology, which is why agents have various internal cognitive states, such as attention, emotions, and goals.
It is also why agent memory, differently from other LLM-based agent platforms, has subtle internal divisions, notably between episodic and semantic memory. 
Some behaviorist concepts are also present, as the idea of a "stimulus" and "response" in the `listen` and `act` methods, which are key abstractions
to understand how agents interact with the environment and other agents.
"""

import os
import csv
import json
import ast
import textwrap  # to dedent strings
import datetime  # to get current datetime
import chevron  # to parse Mustache templates
import logging
logger = logging.getLogger("tinytroupe")
import tinytroupe.utils as utils
from tinytroupe.utils import post_init
from tinytroupe.control import transactional
from tinytroupe.control import current_simulation
from rich import print
import copy
from tinytroupe.utils import JsonSerializableRegistry

from typing import Any, TypeVar, Union

Self = TypeVar("Self", bound="TinyPerson")
AgentOrWorld = Union[Self, "TinyWorld"]

# ... (rest of the code)
```

## <algorithm>

(Блок-схема будет очень большой и сложной для отображения здесь.  Вместо этого, дадим описание алгоритма, фокусируясь на ключевых методах.)

**`TinyPerson` класс:**

1. **`__init__`:** Инициализирует агента, устанавливая имя, память, ментальные способности и конфигурацию.

2. **`_post_init`:** Выполняется после `__init__`. Инициализирует атрибуты `current_messages`, `environment`, `_actions_buffer`, `_accessible_agents`, `_displayed_communications_buffer`, и важные поля конфигурации агента (возраст, национальность, профессия, etc.). Создает запрос для агента на основе шаблона.  Регистрирует агента в глобальном словаре `all_agents`.

3. **`generate_agent_prompt`:** Создает запрос для агента, используя шаблон `tinyperson.mustache` и данные из `_configuration`. Включает дополнительные запросы для `mental_faculties`.

4. **`reset_prompt`:** Обновляет внутренний запрос агента (`_init_system_message`)  с помощью `generate_agent_prompt`, добавляя последние сообщения из `episodic_memory` и сбрасывая `current_messages`.

5. **`get`:** Возвращает значение из конфигурации агента по ключу.

6. **`define`:** Изменяет значение в конфигурации агента. Принимает ключ, значение и необязательный параметр `group` для добавления в подгруппу.  Перерисовывает запрос агента после изменения конфигурации.

7. **`define_relationships`:** Определяет или обновляет отношения агента. Принимает список словарей с отношениями.

8. **`clear_relationships`:** Очищает отношения агента.

9. **`related_to`:** Определяет взаимоотношение между двумя агентами.


10. **`act`:**  Выполняет действия агента в среде. Проверяет, нужно ли действовать до завершения (`until_done`), или ограниченное число раз (`n`). Обрабатывает действия, обновляет состояние агента, вызывая `_produce_message`, `episodic_memory.store`, `_update_cognitive_state`, `faculty.process_action`.


11. **`listen`:** Обрабатывает входящие стимулы (речь).


12. **`_observe`:** Общий обработчик для различных типов стимулов (слушать, видеть, думать, internalize_goal). Сохраняет стимулы в памяти `episodic_memory`.

13. **`listen_and_act`, `see_and_act`, `think_and_act`:** Удобные методы для последовательного выполнения `listen` и `act`.

14. **`_produce_message`:** Отправляет сообщения в OpenAI API для генерации ответа.

15. **`_update_cognitive_state`:** Обновляет когнитивное состояние агента на основе входящих данных (цели, внимание, эмоции).

16. **`_display_communication`:** Выводит сообщения в консоль (с помощью `rich`).



## <mermaid>

```mermaid
graph LR
    subgraph TinyPerson Class
        TinyPerson --> __init__
        TinyPerson --> _post_init
        TinyPerson --> generate_agent_prompt
        TinyPerson --> reset_prompt
        TinyPerson --> get
        TinyPerson --> define
        TinyPerson --> define_relationships
        TinyPerson --> clear_relationships
        TinyPerson --> related_to
        TinyPerson --> act
        TinyPerson --> listen
        TinyPerson --> _observe
        TinyPerson --> listen_and_act
        TinyPerson --> see_and_act
        TinyPerson --> think_and_act
        TinyPerson --> _produce_message
        TinyPerson --> _update_cognitive_state
        TinyPerson --> _display_communication
        TinyPerson --> pop_latest_actions
    end
    subgraph OpenAI API
        TinyPerson --> OpenAI API
    end
    subgraph EpisodicMemory
        TinyPerson --> EpisodicMemory
    end
    subgraph SemanticMemory
        TinyPerson --> SemanticMemory
    end
    subgraph Mental Faculty
        TinyPerson --> Mental Faculty
        Mental Faculty --> process_action
        Mental Faculty --> actions_definitions_prompt
        Mental Faculty --> actions_constraints_prompt

        subgraph RecallFaculty
            RecallFaculty --> retrieve_relevant
        end
        subgraph FilesAndWebGroundingFaculty
            FilesAndWebGroundingFaculty --> retrieve_document_content_by_name
            FilesAndWebGroundingFaculty --> list_documents_names
        end
        subgraph TinyToolUse
            TinyToolUse --> process_action
        end
    end
    subgraph Utils
      TinyPerson --> tinytroupe.utils
    end
    subgraph Configuration
      TinyPerson --> utils.read_config_file
    end

    TinyPerson -.-> TinyWorld
    TinyPerson --> JsonSerializableRegistry
    TinyPerson --> logging
    TinyPerson --> current_simulation
    TinyPerson --> transactional
```

## <explanation>

**Импорты:**
- `os`, `csv`, `json`, `ast`, `textwrap`, `datetime`, `chevron`, `logging`, `copy`, `rich`, `typing`: Стандартные библиотеки Python, используемые для файлового ввода/вывода, обработки JSON, логгирования, копирования объектов, форматирования вывода и т.д.
- `tinytroupe.utils`, `tinytroupe.control`: Модули из собственного проекта TinyTroupe, содержащие вспомогательные функции и контроллеры (возможно, для управления симуляцией). `JsonSerializableRegistry`: Помогает сериализовать и десериализировать объекты.
- `llama_index`: Библиотека для работы с векторами. В коде есть примеры использования этой библиотеки, но они закомментированы.
- `openai_utils`: Модуль для взаимодействия с API OpenAI.


**Классы:**
- `TinyPerson`: Главный класс для представления агента. Он имеет атрибуты, такие как имя, память (`episodic_memory`, `semantic_memory`), ментальные способности (`_mental_faculties`), текущие сообщения, конфигурацию (`_configuration`).
- `TinyMentalFaculty`: Базовый класс для ментальных способностей агента (например, `RecallFaculty`, `FilesAndWebGroundingFaculty`, `TinyToolUse`).  Определяет методы для обработки действий, генерации запросов.
- `RecallFaculty`:  Представляет способность вспоминать информацию.
- `FilesAndWebGroundingFaculty`: Представляет способность доступа к локальным файлам и веб-страницам.
- `SemanticMemory`, `EpisodicMemory`: Представляют семантическую и эпизодическую память соответственно. Используют `llama_index` для индексации документов.
- `TinyMemory`: Базовый класс для разных типов памяти.
- `TinyToolUse`:  Представляет возможность использования инструментов.


**Функции:**
- `generate_agent_prompt()`: Создает запрос для агента на основе шаблона.
- `reset_prompt()`: Сбрасывает текущий запрос агента.
- `get(key)`: Возвращает значение из конфигурации агента по заданному ключу.
- `define(key, value, group=None)`: Изменяет значение в конфигурации агента.
- `act()`: Выполняет действия агента в среде.
- `listen()`, `see()`, `think()`, `socialize()`: Обработка разных типов входных стимулов.
- `_produce_message()`: Отправляет сообщение в OpenAI API.
- `_update_cognitive_state()`: Обновляет когнитивное состояние агента.
- `_display_communication()`: Выводит сообщения в консоль (с помощью `rich`).


**Переменные:**
- `config`: Читает конфигурацию из файла.
- `default`: Словарь с параметрами по умолчанию.
- `MAX_ACTIONS_BEFORE_DONE`: Максимальное количество действий агента, которые могут быть выполнены до завершения.

**Возможные ошибки/улучшения:**

- **Сложная логика:** Код содержит сложную логику, связанную с обработкой действий, обновлением состояния и взаимодействием с внешней средой.  Необходимо тщательное тестирование для проверки корректности работы.
- **`llama_index`:** Закомментированные части использования `llama_index` пока не активны. Разработчики могут добавить обработку и индексирование документов, чтобы улучшить семантическую память.
- **`process_action` (в подклассах):** Методы `process_action` в подклассах `TinyMentalFaculty` должны быть реализованы.
- **Документация:**  Документация некоторых методов и классов была бы очень полезной для понимания и использования кода.
- **Использование `rich`:**  В коде используется `rich` для форматирования вывода. Это хорошо для читабельности, но если взаимодействие будет происходить через API,  то нужно будет подумать о более универсальном способе представления информации.


**Взаимосвязи с другими частями проекта:**

Код взаимодействует с другими модулями TinyTroupe, особенно с `tinytroupe.utils`, `tinytroupe.control`, и `openai_utils`, демонстрируя зависимость от OpenAI API, механизмов управления симуляцией и вспомогательных инструментов.  Класс `TinyPerson` зависит от `EpisodicMemory` и `SemanticMemory`, которые, в свою очередь, взаимодействуют с `llama_index`  для обработки документов.


**Общие замечания:**

Код написан с использованием лучших практик и ориентирован на масштабируемость и удобство использования в рамках проекта TinyTroupe. Он демонстрирует хороший дизайн, который поддерживает расширение за счет добавления новых ментальных способностей и типов памяти. Подробные комментарии и документация значительно улучшили бы его поддержку и понимание.