Как использовать класс TinyEnricher
========================================================================================

Описание
-------------------------
Класс `TinyEnricher` предназначен для обогащения контента с помощью моделей больших языков (LLM). Он принимает на вход требования (`requirements`), контент (`content`), тип контента (`content_type`), контекстную информацию (`context_info`), кэш контекста (`context_cache`) и флаг подробного режима (`verbose`).  Класс формирует сообщения для LLM, отправляет их, получает ответ и извлекает из него код.

Шаги выполнения
-------------------------
1. Создается экземпляр класса `TinyEnricher`, при необходимости передавая флаг `use_past_results_in_context` для использования предыдущих результатов в контексте.
2. Метод `enrich_content` получает на вход параметры: требования, контент, тип контента, контекстную информацию, кэш контекста и флаг подробного режима.
3.  Метод формирует словарь `rendering_configs` с необходимыми данными для шаблонов (`mustache`).
4.  Формируются сообщения для LLM с использованием шаблонов `enricher.system.mustache` и `enricher.user.mustache`, используя данные из `rendering_configs`.
5.  Отправляется сообщение в API OpenAI с помощью `openai_utils.client().send_message()`.  Параметр `temperature=0.4` указывает на вероятность выбора различных вариантов ответа.
6.  Из ответа LLM (`next_message`) извлекается код с помощью `utils.extract_code_block()`.
7.  Результат (код или `None`, если ответ отсутствует) возвращается методом.
8.  Если включен подробный режим (`verbose`), то выводится отладочное сообщение.


Пример использования
-------------------------
.. code-block:: python

    import logging
    from tinytroupe.enrichment import TinyEnricher
    import tinytroupe.utils as utils

    # Настройка логирования (необязательно)
    logging.basicConfig(level=logging.DEBUG)


    # Пример данных
    requirements = "Напишите код для вычисления площади прямоугольника"
    content = "Даны стороны прямоугольника a и b."
    context_cache = []

    # Создание объекта
    enricher = TinyEnricher()

    # Вызов метода
    result = enricher.enrich_content(requirements, content, context_cache=context_cache, verbose=True)


    # Обработка результата
    if result:
        print("Полученный код:")
        print(result)
    else:
        print("Нет результата.")