# Анализ кода модуля `enrichment.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на функции, что облегчает понимание и поддержку.
    - Используется класс `TinyEnricher` для управления процессом обогащения, что обеспечивает модульность.
    - Применяется `JsonSerializableRegistry` для сериализации и десериализации, что соответствует стандартам проекта.
    - Логирование с уровнем `debug` позволяет отслеживать процесс обогащения.
    -  Используются шаблоны mustache для формирования запросов к LLM, что упрощает управление текстом запросов.
- Минусы
    -  Импорт `logging` и настройка логгера выполнена нестандартно, нужно импортировать из `src.logger.logger`.
    -  Отсутствует документация для класса и методов.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Не все импорты используются, например `pandas`.
    -  Нет обработки ошибок через `try-except` или через `logger.error`.
    -  Не используется `from src.logger.logger import logger` для импорта логгера.

**Рекомендации по улучшению**

1.  Импортировать `logger` из `src.logger.logger`.
2.  Добавить документацию в формате RST для класса `TinyEnricher` и метода `enrich_content`.
3.  Удалить неиспользуемые импорты.
4.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`, если необходимо чтение JSON файлов.
5.  Добавить обработку ошибок с использованием `logger.error` для ситуаций, когда `next_message` is `None`.
6.  Добавить тип к переменным.

**Оптимизированный код**

```python
"""
Модуль для обогащения контента с использованием LLM
====================================================

Этот модуль предоставляет класс `TinyEnricher`, который используется для обогащения текстового контента
с помощью моделей обработки естественного языка. Он принимает требования и контент, формирует
сообщения для LLM, и возвращает обогащенный контент.

Пример использования
--------------------

.. code-block:: python

    enricher = TinyEnricher()
    requirements = "Извлечь все имеющиеся имена"
    content = "В тексте упоминаются Иван, Петр и Мария."
    enriched_content = enricher.enrich_content(requirements, content)
    print(enriched_content)
"""
import os
import chevron
# from src.logger.logger import logger  # Импорт из правильного места
import logging
logger = logging.getLogger("tinytroupe")
# import pandas as pd # не используется
from typing import Any, List, Optional
from pathlib import Path
from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry
from tinytroupe import openai_utils
import tinytroupe.utils as utils

class TinyEnricher(JsonSerializableRegistry):
    """
    Класс для обогащения контента с использованием LLM.

    :param use_past_results_in_context: Флаг, указывающий, использовать ли предыдущие результаты в контексте.
    :type use_past_results_in_context: bool
    :ivar context_cache: Кэш контекста для сохранения предыдущих результатов.
    :vartype context_cache: list
    """
    def __init__(self, use_past_results_in_context: bool = False) -> None:
        """
        Инициализирует экземпляр класса `TinyEnricher`.

        :param use_past_results_in_context: Флаг, указывающий, использовать ли предыдущие результаты в контексте.
        :type use_past_results_in_context: bool
        """
        self.use_past_results_in_context = use_past_results_in_context
        self.context_cache: List[str] = [] # инициализация переменной context_cache


    def enrich_content(self, requirements: str, content: str, content_type: Optional[str] = None, context_info: str = "", context_cache: Optional[List[str]] = None, verbose: bool = False) -> Optional[str]:
        """
        Обогащает контент, используя LLM.

        :param requirements: Требования к обогащению контента.
        :type requirements: str
        :param content: Исходный контент для обогащения.
        :type content: str
        :param content_type: Тип контента.
        :type content_type: Optional[str]
        :param context_info: Дополнительная информация о контексте.
        :type context_info: str
        :param context_cache: Кэш контекста с предыдущими результатами.
        :type context_cache: Optional[List[str]]
        :param verbose: Флаг для включения режима подробного вывода.
        :type verbose: bool
        :return: Обогащенный контент или None в случае ошибки.
        :rtype: Optional[str]
        """
        rendering_configs = {
            'requirements': requirements,
            'content': content,
            'content_type': content_type,
            'context_info': context_info,
            'context_cache': context_cache
        }
        #  формирование сообщений для LLM с использованием шаблонов mustache
        messages = utils.compose_initial_LLM_messages_with_templates('enricher.system.mustache', 'enricher.user.mustache', rendering_configs)
        # отправка сообщения в LLM
        next_message = openai_utils.client().send_message(messages, temperature=0.4)

        debug_msg = f'Enrichment result message: {next_message}'
        logger.debug(debug_msg)
        if verbose:
            print(debug_msg)
        # проверка если сообщение от LLM пришло
        if next_message is not None:
            #  извлечение кодового блока из ответа
            result = utils.extract_code_block(next_message['content'])
        else:
            # обработка ошибки когда нет ответа от LLM
            logger.error(f'No message received from LLM for requirements: {requirements}')
            result = None
        return result
```