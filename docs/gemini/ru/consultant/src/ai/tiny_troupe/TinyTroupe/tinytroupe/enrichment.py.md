# Анализ кода модуля `enrichment.py`

**Качество кода**
8
- Плюсы
    - Код достаточно хорошо структурирован, использует классы для организации логики.
    - Применяется `logger` для отладочных сообщений.
    - Имеется разделение на `TinyEnricher` и `JsonSerializableRegistry`, что способствует модульности.
    - Используется `chevron` для шаблонизации.
    - Есть возможность использовать прошлые результаты в контексте.
- Минусы
    - Отсутствует описание модуля в начале файла.
    - Нет документации к классу и методам в формате RST.
    - Используется `logging` вместо `from src.logger.logger import logger`.
    - Стандартный `json` импортируется, а не `j_loads` из `src.utils.jjson`.
    - Не используются одинарные кавычки для строк в коде.
    - Избыточное использование `if next_message is not None` можно заменить на более лаконичное выражение.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Добавить документацию в формате RST для класса `TinyEnricher`, его методов `__init__` и `enrich_content`, а также для переменных.
3.  Использовать `from src.logger.logger import logger` для логирования.
4.  Заменить импорт `json` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  Использовать одинарные кавычки для строк в коде.
6.  Заменить `if next_message is not None` на более лаконичное выражение с помощью оператора `if not` или тернарного оператора.
7.  Добавить обработку ошибок и логирование ошибок в методе `enrich_content`.
8.  Переименовать `debug_msg` в `message_debug` для соответствия другим переменным и общей структуре проекта.

**Оптимизированный код**

```python
"""
Модуль для обогащения текстового контента с использованием LLM.
=========================================================================================

Этот модуль предоставляет класс :class:`TinyEnricher`, который используется для
обогащения текстового контента на основе заданных требований, используя
шаблоны и модели LLM.

Пример использования
--------------------

Пример использования класса `TinyEnricher`:

.. code-block:: python

    enricher = TinyEnricher(use_past_results_in_context=True)
    enriched_content = enricher.enrich_content(
        requirements='Summarize the following text',
        content='Some long text...',
        content_type='text',
        context_info='some context info',
        context_cache=['previous summary']
    )
    print(enriched_content)
"""
import os
# from src.utils.jjson import j_loads, j_loads_ns  # TODO: Uncomment if needed
# import json # TODO: remove
import chevron
# import logging # TODO: remove
from src.logger.logger import logger
import pandas as pd

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry

from tinytroupe import openai_utils
import tinytroupe.utils as utils

class TinyEnricher(JsonSerializableRegistry):
    """
    Класс для обогащения текстового контента с использованием LLM.

    Args:
        use_past_results_in_context (bool):
            Указывает, использовать ли предыдущие результаты в контексте.
            По умолчанию False.

    Attributes:
        use_past_results_in_context (bool):
            Флаг, указывающий, следует ли использовать предыдущие результаты в контексте.
        context_cache (list):
            Список для хранения контекстной информации.
    """
    def __init__(self, use_past_results_in_context=False) -> None:
        """
        Инициализация экземпляра класса TinyEnricher.

        Args:
            use_past_results_in_context (bool):
                Указывает, использовать ли предыдущие результаты в контексте.
                По умолчанию False.
        """
        self.use_past_results_in_context = use_past_results_in_context
        #  Список для хранения контекстной информации
        self.context_cache = []
    
    def enrich_content(self, requirements: str, content:str, content_type:str =None, context_info:str ="", context_cache:list=None, verbose:bool=False):
        """
        Обогащает заданный контент на основе требований, используя LLM.

        Args:
            requirements (str):
                Требования к обогащению контента.
            content (str):
                Контент, который необходимо обогатить.
            content_type (str, optional):
                Тип контента. По умолчанию None.
            context_info (str, optional):
                Дополнительная контекстная информация. По умолчанию "".
            context_cache (list, optional):
                Список с кэшем контекстной информации. По умолчанию None.
            verbose (bool, optional):
                Флаг для отображения подробных сообщений в консоль. По умолчанию False.

        Returns:
            str | None:
                Обогащенный контент в виде строки, или None, если не удалось получить результат.
        """
        rendering_configs = {'requirements': requirements,
                             'content': content,
                             'content_type': content_type,
                             'context_info': context_info,
                             'context_cache': context_cache}
        
        #  Код составляет сообщения для LLM, используя шаблоны
        messages = utils.compose_initial_LLM_messages_with_templates('enricher.system.mustache', 'enricher.user.mustache', rendering_configs)
        #  Код отправляет сообщение LLM и получает результат
        try:
             next_message = openai_utils.client().send_message(messages, temperature=0.4)
        except Exception as ex:
             logger.error('Ошибка отправки сообщения в LLM', exc_info=ex)
             return None
        
        message_debug = f'Enrichment result message: {next_message}'
        logger.debug(message_debug)
        if verbose:
            print(message_debug)

        #  Код извлекает блок кода из ответа LLM
        result = utils.extract_code_block(next_message['content']) if next_message else None
        # if next_message is not None:
        #     result = utils.extract_code_block(next_message["content"])
        # else:
        #     result = None

        return result
```