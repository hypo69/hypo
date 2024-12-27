# Анализ кода модуля `enrichment.py`

**Качество кода**
9
-  Плюсы
    - Код достаточно хорошо структурирован, использует классы и функции для организации логики.
    - Применяется `logging` для отслеживания ошибок и процесса работы, что важно для отладки и мониторинга.
    - Используются шаблоны `mustache` для генерации сообщений, что способствует гибкости и переиспользованию кода.
    - Код применяет `JsonSerializableRegistry`, что позволяет регистрировать и сериализовать объекты в JSON.
    - Присутствует использование `openai_utils` для работы с OpenAI API, что указывает на интеграцию с внешним сервисом.
-  Минусы
    -  Отсутствуют docstring для модуля, класса и методов.
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это подразумевалось в коде (не нашел использования json.load)
    -  Не все импорты приведены в соответствие с другими файлами (напр. `from tinytroupe import openai_utils` должен быть `from src.ai.tiny_troupe import openai_utils`)
    -  Обработка ошибок не использует `logger.error` вместо `try-except`.
    -  Не все комментарии оформлены в стиле RST.
    - Не все импорты вынесены в начало файла.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring для модуля, класса `TinyEnricher` и его методов, используя reStructuredText (RST) формат.
2.  **Импорты:** Привести импорты в соответствие с другими файлами, а именно `from tinytroupe import openai_utils` заменить на `from src.ai.tiny_troupe import openai_utils`.
3.  **Обработка ошибок:** Заменить `try-except` на использование `logger.error` для логирования ошибок, где это возможно.
4.  **Комментарии:** Переписать все комментарии в стиле RST, где это необходимо.
5.  **Использовать `j_loads`:** Убедиться, что используются `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`, если это требование применимо (в коде нет вызовов `json.load`).
6.  **Логирование:** Использовать `from src.logger.logger import logger` для логирования.

**Оптимизированный код**

```python
"""
Модуль для обогащения контента с помощью языковой модели.
=========================================================================================

Этот модуль содержит класс :class:`TinyEnricher`, который используется для
обогащения текстового контента на основе заданных требований, контекстной информации
и кэша предыдущих результатов. Он применяет шаблоны mustache для создания
сообщений, которые отправляются языковой модели.

Пример использования
--------------------

Пример использования класса `TinyEnricher`:

.. code-block:: python

    enricher = TinyEnricher(use_past_results_in_context=True)
    enriched_content = enricher.enrich_content(
        requirements="Улучши этот текст",
        content="Исходный текст",
        content_type="текст",
        context_info="Дополнительная информация",
        context_cache=["Предыдущий результат"]
    )
    print(enriched_content)
"""
import os
# import json # не используется, поэтому закомментировал
import chevron
# import logging # заменен на src.logger.logger
import pandas as pd

from tinytroupe.agent import TinyPerson
from tinytroupe.environment import TinyWorld
from tinytroupe.factory import TinyPersonFactory
from tinytroupe.utils import JsonSerializableRegistry
from src.ai.tiny_troupe import openai_utils #  изменено  импорт
import tinytroupe.utils as utils
from src.logger.logger import logger # импорт для логирования

class TinyEnricher(JsonSerializableRegistry):
    """
    Класс для обогащения контента с использованием языковой модели.

    :param use_past_results_in_context: Флаг, определяющий, использовать ли прошлые результаты в контексте.
    :type use_past_results_in_context: bool, optional
    """
    def __init__(self, use_past_results_in_context=False) -> None:
        """
        Инициализирует объект TinyEnricher.

        :param use_past_results_in_context: Определяет, используются ли прошлые результаты в контексте.
        :type use_past_results_in_context: bool, optional
        """
        self.use_past_results_in_context = use_past_results_in_context
        #: Кэш контекста для хранения результатов.
        self.context_cache = []
    
    def enrich_content(self, requirements: str, content:str, content_type:str =None, context_info:str ="", context_cache:list=None, verbose:bool=False):
        """
        Обогащает контент на основе заданных требований и контекста.

        :param requirements: Требования к обогащению контента.
        :type requirements: str
        :param content: Текст, который нужно обогатить.
        :type content: str
        :param content_type: Тип контента (например, "текст", "код").
        :type content_type: str, optional
        :param context_info: Дополнительная информация для контекста.
        :type context_info: str, optional
        :param context_cache: Кэш предыдущих результатов.
        :type context_cache: list, optional
        :param verbose: Флаг для вывода отладочной информации.
        :type verbose: bool, optional
        :return: Обогащенный контент или None в случае ошибки.
        :rtype: str or None
        """
        # формируем словарь с конфигурациями для рендеринга
        rendering_configs = {"requirements": requirements,
                             "content": content,
                             "content_type": content_type, 
                             "context_info": context_info,
                             "context_cache": context_cache}

        # Компонуем сообщения для языковой модели с использованием шаблонов mustache
        messages = utils.compose_initial_LLM_messages_with_templates("enricher.system.mustache", "enricher.user.mustache", rendering_configs)
        # Отправляем сообщение в языковую модель и получаем ответ
        next_message = openai_utils.client().send_message(messages, temperature=0.4)
        
        debug_msg = f"Enrichment result message: {next_message}"
        # Логируем отладочное сообщение
        logger.debug(debug_msg)
        # Выводим отладочное сообщение, если verbose=True
        if verbose:
            print(debug_msg)

        # извлекаем код из ответа, если он есть
        if next_message is not None:
            result = utils.extract_code_block(next_message["content"])
        else:
            result = None

        # Возвращаем результат обогащения
        return result
```