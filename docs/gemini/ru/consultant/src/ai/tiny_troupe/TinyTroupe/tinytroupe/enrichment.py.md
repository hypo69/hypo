# Анализ кода модуля `enrichment.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован в класс `TinyEnricher`.
    - Используется `JsonSerializableRegistry` для сериализации.
    - Применяется `chevron` для шаблонизации.
    - Присутствует логирование через `logging`.
    - Код использует `openai_utils` для взаимодействия с OpenAI.
    - Есть возможность использовать предыдущие результаты в контексте.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Отсутствует документация в формате reStructuredText (RST).
    - Не все импорты используются.
    - Не все переменные и функции имеют описательные имена.
    - Использование `print` для вывода отладочной информации, лучше использовать `logger.debug`.
    - Отсутствует обработка ошибок при работе с OpenAI.

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для класса `TinyEnricher` и его методов, включая параметры и возвращаемые значения.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это необходимо (в текущем коде нет прямого чтения файлов, но это стоит учесть).
3.  Заменить `print` на `logger.debug` для отладочной информации.
4.  Добавить обработку ошибок при вызове `openai_utils.client().send_message`, используя `try-except` и логирование ошибок с помощью `logger.error`.
5.  Удалить неиспользуемые импорты `logging`, `pandas`, `tinytroupe.agent`, `tinytroupe.environment` и `tinytroupe.factory`.
6.  Изменить `next_message["content"]` на `next_message.content` если в `openai_utils.client().send_message` возвращается объект с атрибутом `content`.
7.  Переименовать `rendering_configs` в `template_data` для большей ясности.
8.  Добавить комментарии к блокам кода.

**Оптимизированный код**

```python
"""
Модуль для обогащения контента с помощью языковой модели.
=========================================================================================

Этот модуль содержит класс :class:`TinyEnricher`, который использует языковые модели для обогащения текстового контента.
Он поддерживает использование предыдущих результатов в контексте и управляет кешем контекста.

Пример использования
--------------------

Пример использования класса `TinyEnricher`:

.. code-block:: python

    enricher = TinyEnricher(use_past_results_in_context=True)
    enriched_content = enricher.enrich_content(
        requirements="Улучшить текст",
        content="Некий текст",
        content_type="text",
        context_info="Дополнительная информация"
    )
"""
import chevron
from src.utils.jjson import j_loads  # TODO: проверить нужно ли это
from src.logger.logger import logger # Используем логер из logger
from tinytroupe.utils import JsonSerializableRegistry
from tinytroupe import openai_utils
import tinytroupe.utils as utils


class TinyEnricher(JsonSerializableRegistry):
    """
    Класс для обогащения текстового контента с использованием языковой модели.

    :param use_past_results_in_context: Определяет, следует ли использовать предыдущие результаты в контексте.
    :type use_past_results_in_context: bool, optional
    """
    def __init__(self, use_past_results_in_context=False) -> None:
        """
        Инициализация экземпляра класса TinyEnricher.

        :param use_past_results_in_context: Флаг, указывающий, следует ли использовать прошлые результаты в контексте.
        :type use_past_results_in_context: bool, optional, default=False
        """
        self.use_past_results_in_context = use_past_results_in_context
        self.context_cache = []

    def enrich_content(self, requirements: str, content: str, content_type: str = None, context_info: str = "", context_cache: list = None, verbose: bool = False) -> str | None:
        """
        Обогащает предоставленный контент с использованием языковой модели.

        :param requirements: Требования к обогащению контента.
        :type requirements: str
        :param content: Исходный контент для обогащения.
        :type content: str
        :param content_type: Тип контента.
        :type content_type: str, optional
        :param context_info: Дополнительная контекстная информация.
        :type context_info: str, optional
        :param context_cache: Список предыдущих результатов для использования в контексте.
        :type context_cache: list, optional
        :param verbose: Флаг для вывода отладочной информации.
        :type verbose: bool, optional
        :return: Обогащенный контент или None в случае ошибки.
        :rtype: str | None
        """
        template_data = {
            "requirements": requirements,
            "content": content,
            "content_type": content_type,
            "context_info": context_info,
            "context_cache": context_cache
        }
        # формируем сообщения для языковой модели
        messages = utils.compose_initial_LLM_messages_with_templates("enricher.system.mustache", "enricher.user.mustache", template_data)
        
        try:
            # отправляем сообщение языковой модели
            next_message = openai_utils.client().send_message(messages, temperature=0.4)
        except Exception as e:
           logger.error(f"Ошибка при отправке сообщения в OpenAI: {e}")
           return None

        debug_msg = f"Enrichment result message: {next_message}"
        logger.debug(debug_msg) # используем логер для отладочных сообщений
        if verbose:
            print(debug_msg)
            
        if next_message is not None:
            # извлекаем блок кода из ответа
            result = utils.extract_code_block(next_message.content) # если это объект с атрибутом content
        else:
            result = None

        return result
```