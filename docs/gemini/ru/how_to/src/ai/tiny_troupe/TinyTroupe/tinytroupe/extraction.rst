Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит классы для извлечения и обработки данных из симуляций TinyTroupe.  `ResultsExtractor` позволяет извлекать результаты из объектов `TinyPerson` и `TinyWorld`, используя запросы к LLM.  `ResultsReducer` обрабатывает результаты, применяя к ним правила, а `ArtifactExporter` экспортирует данные в различные форматы (JSON, TXT, DOCX).  `Normalizer` нормализует текстовые элементы.  Модуль демонстрирует взаимодействие с LLM для структурированного извлечения данных из симуляций.

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек:**
   Импортируются библиотеки `os`, `json`, `chevron`, `logging`, `pandas`, `pypandoc`, `markdown`, `typing`, а также специфичные для TinyTroupe классы (`TinyPerson`, `TinyWorld`, `JsonSerializableRegistry`).

2. **Инициализация `ResultsExtractor`:**
   Создается экземпляр класса `ResultsExtractor`, который отвечает за взаимодействие с LLM для извлечения данных. Он инициализирует путь к шаблону запроса.

3. **Извлечение результатов от `TinyPerson`:**
   Метод `extract_results_from_agent` извлекает результаты от объекта `TinyPerson`.  Он принимает объект `TinyPerson`, целевой запрос и другие параметры (например, `extraction_objective`,  `situation`, список полей для извлечения и др.). Он генерирует запрос к LLM для обработки истории взаимодействий агента и сохраняет результат в `self.agent_extraction`.

4. **Извлечение результатов от `TinyWorld`:**
   Аналогично, метод `extract_results_from_world` извлекает результаты от объекта `TinyWorld`, обрабатывая историю взаимодействий всех агентов в среде.

5. **Сохранение результатов:**
   Метод `save_as_json` сохраняет результаты извлечения (`self.agent_extraction`, `self.world_extraction`) в JSON-файл.

6. **Редукция результатов (`ResultsReducer`):**
   Класс `ResultsReducer` позволяет применять правила к извлечённым данным.  Метод `add_reduction_rule` добавляет пользовательские правила, которые применяются к данным из истории взаимодействия. Метод `reduce_agent` применяет эти правила к истории агента, возвращая обработанные данные.

7. **Преобразование в DataFrame:**
   Метод `reduce_agent_to_dataframe` преобразует полученные данные в DataFrame pandas для удобной обработки и анализа.

8. **Экспорт данных (`ArtifactExporter`):**
   Класс `ArtifactExporter` позволяет экспортировать извлеченные данные в различные форматы (JSON, TXT, DOCX).  Метод `export` принимает данные для экспорта, имя файла и формат для сохранения, обеспечивая валидацию и преобразование данных.

9. **Нормализация данных (`Normalizer`):**
   Класс `Normalizer` нормализует список текстовых элементов, используя LLM.  Метод `normalize` применяет предварительно подготовленные LLM-правила для нормализации входных данных.

Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.extraction import ResultsExtractor, ArtifactExporter
    from tinytroupe.agent import TinyPerson
    # ... (инициализация TinyPerson) ...

    extractor = ResultsExtractor()
    results = extractor.extract_results_from_agent(my_agent, extraction_objective="Ключевые моменты", situation="Обычная ситуация")

    exporter = ArtifactExporter("path/to/output")
    exporter.export("agent_results", results, "agent_interactions", target_format="json")

    # Пример использования ResultsReducer (если требуется)
    from tinytroupe.extraction import ResultsReducer
    reducer = ResultsReducer()
    reducer.add_reduction_rule("question", lambda x: x['content'].split('?')[0])
    reduced_results = reducer.reduce_agent(my_agent)
```