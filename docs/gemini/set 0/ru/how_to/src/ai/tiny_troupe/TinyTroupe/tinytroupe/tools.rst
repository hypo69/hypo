Как использовать класс TinyTool
========================================================================================

Описание
-------------------------
Этот класс `TinyTool` служит основой для инструментов, позволяющих агентам выполнять специализированные задачи.  Он предоставляет методы для инициализации инструмента, обработки действий, проверки реальных последствий, проверки владения инструментом и генерации подсказок для определений и ограничений действий.  Подклассы должны реализовать метод `_process_action` для выполнения конкретных задач инструмента.

Шаги выполнения
-------------------------
1. **Инициализация:** Создать экземпляр класса `TinyTool` с указанием имени, описания, владельца (если применимо), наличия реальных последствий и опциональными экспортером и обогатителем результатов.
2. **Обработка действия:** Вызвать метод `process_action` с агентом и словарем `action`.
3. **Обработка внутреннего действия:** Внутри `process_action`, выполняется проверка на реальные последствия (`_protect_real_world`) и проверка на владение (`_enforce_ownership`).  Затем метод `_process_action` (который должен быть реализован в подклассе) выполняет конкретное действие.
4. **Генерация подсказок:** Методы `actions_definitions_prompt` и `actions_constraints_prompt` возвращают подсказки, описывающие допустимые типы действий и ограничения для инструмента.

Пример использования
-------------------------
.. code-block:: python

    import logging
    import json
    import tinytroupe.utils as utils
    from tinytroupe.extraction import ArtifactExporter
    from tinytroupe.enrichment import TinyEnricher
    from tinytroupe.tools import TinyTool

    # Пример экспортера (необязательно)
    class MyExporter(ArtifactExporter):
        def export(self, artifact_name, artifact_data, content_type, content_format, target_format):
            print(f"Экспортировано: {artifact_name} ({content_type})")

    # Пример обогатителя (необязательно)
    class MyEnricher(TinyEnricher):
        def enrich_content(self, requirements, content, content_type, context_info, context_cache, verbose):
            return content + " - (обогащенное содержимое)"

    # Создание инструмента
    my_tool = TinyTool(
        name="Мой инструмент",
        description="Мой инструмент выполняет какую-то задачу",
        real_world_side_effects=False,
        exporter=MyExporter(),
        enricher=MyEnricher()
    )

    # Пример действия (в словаре)
    action = {
        "type": "ЗАДАЧА1",
        "content": json.dumps({"параметр1": "значение1"})
    }

    # Обработка действия
    try:
        result = my_tool.process_action(agent="agent1", action=action)
        if result:
            print("Действие выполнено успешно")
        else:
            print("Действие не выполнено")
    except ValueError as e:
        print(f"Ошибка: {e}")