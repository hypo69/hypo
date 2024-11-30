Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот модуль предоставляет инструменты для извлечения данных из элементов TinyTroupe, таких как агенты и миры. Он также включает механизм для сокращения извлечённых данных и экспорта артефактов из элементов TinyTroupe. Модуль демонстрирует один из способов отличия симуляций агентов от AI-помощников, так как последние не предназначены для такого рода интроспекции. Модуль содержит классы `ResultsExtractor`, `ResultsReducer` и `ArtifactExporter`, а также функцию `default_extractor`.  `ResultsExtractor` извлекает результаты из агентов и миров на основе заданных параметров. `ResultsReducer` сокращает полученные данные. `ArtifactExporter` экспортирует данные в различные форматы (JSON, TXT, DOCX).  `default_extractor` — это экземпляр класса `ResultsExtractor`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Модуль использует `os`, `json`, `chevron`, `logging`, `pandas`, `pypandoc`, `markdown`, `typing`, а также собственные модули TinyTroupe.

2. **Инициализация `ResultsExtractor`:** Создайте экземпляр класса `ResultsExtractor`, чтобы начать извлечение данных.

3. **Извлечение данных из агента (метод `extract_results_from_agent`):**
    - Передайте экземпляр `TinyPerson` в качестве аргумента `tinyperson`.
    - Укажите `extraction_objective` (цель извлечения).
    - Добавьте `situation` (контекст).
    - Можно указать `fields` (поля для извлечения) и `fields_hints` (подсказки к полям).
    - Установите `verbose=True` для вывода отладочных сообщений.
    - Метод `pretty_current_interactions` извлекает историю взаимодействий агента.
    - Метод `send_message` из библиотеки `openai_utils` отправляет запрос на API OpenAI.
    - Результат извлечения сохраняется в словаре `self.agent_extraction`.

4. **Извлечение данных из мира (метод `extract_results_from_world`):** Аналогично шагу 3, но для экземпляра `TinyWorld` и с учётом взаимодействия нескольких агентов.

5. **Сохранение результатов (метод `save_as_json`):**
    - Сохраните извлечённые данные в JSON-файл с помощью `save_as_json`.
    - Укажите имя файла.
    - Установите `verbose=True` для отображения сообщения о сохранении.


6. **Сокращение результатов (класс `ResultsReducer`):**
    - Создайте экземпляр `ResultsReducer`.
    - Используйте `add_reduction_rule`, чтобы определить правила сокращения.  Функции  `func` обрабатывают стимулы и действия.
    - Метод `reduce_agent` применяет правила к истории взаимодействия агента.
    - Метод `reduce_agent_to_dataframe` преобразует сокращённые данные в таблицу Pandas.

7. **Экспорт артефактов (класс `ArtifactExporter`):**
    - Создайте экземпляр класса `ArtifactExporter` и передайте путь к основной папке вывода в качестве аргумента.
    - Используйте метод `export`, чтобы экспортировать артефакты в выбранный формат (JSON, TXT, DOCX).
    - Укажите имя артефакта, данные, тип контента, формат контента, целевой формат и флаг `verbose`.


8. **Нормализация данных (класс `Normalizer`):**
    - Создайте экземпляр класса `Normalizer`.
    - Передайте список элементов для нормализации и `n` (количество элементов вывода).
    - Используйте метод `normalize`, чтобы нормализовать заданные элементы.



Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.extraction import ResultsExtractor, ArtifactExporter, Normalizer
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld

    # Предположим, что вы уже инициализировали TinyPerson и TinyWorld
    extractor = ResultsExtractor()
    agent_results = extractor.extract_results_from_agent(tinyperson, extraction_objective="Краткое изложение разговора")

    exporter = ArtifactExporter(base_output_folder="output_data")
    exporter.export(artifact_name="agent_summary", artifact_data=agent_results, content_type="agent_interactions", target_format="json", verbose=True)

    normalizer = Normalizer(elements=["element1", "element2"], n=2)
    normalized_elements = normalizer.normalize(["element1"])