Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код описывает инструкцию для модели, которая должна анализировать компьютерные компоненты из JSON, классифицировать тип сборки (например, игровой, рабочая станция), предоставлять заголовки и описания на иврите и русском, переводить детали компонентов и возвращать структурированный выходной JSON. Код требует поддержания правильного форматирования, включения оценок уверенности и соблюдения подробных руководств по описаниям и обработке компонентов.  Он определяет шаблон ответа в формате JSON, содержащий поля для заголовков, описаний, типов сборки и списка продуктов на иврите и русском языках.

Шаги выполнения
-------------------------
1. **Получить входные данные**: Модель должна получить JSON-данные о компьютерных компонентах.
2. **Провести анализ компонентов**: Проанализировать полученные данные о компонентах.
3. **Классифицировать тип сборки**: На основе анализа определить тип сборки (например, игровая или рабочая станция) и вычислить соответствующие оценки уверенности.
4. **Сгенерировать описания и заголовки**: Сгенерировать заголовки и описания на иврите и русском языке для компьютерной сборки, а также для отдельных компонентов.
5. **Преобразовать детали компонентов**: Преобразовать детали компонентов (если необходимо) и их спецификации для каждого языка.
6. **Сформировать структурированный JSON-выход**: Сформировать структурированный выходной JSON в соответствии с заданным шаблоном, содержащий поля для заголовков, описаний, типов сборки и списка продуктов.
7. **Поддерживать правильное форматирование**: Убедиться, что выходной JSON соответствует заданному шаблону.
8. **Включить оценки уверенности**: Включить оценки уверенности для типа сборки в выходных данных.
9. **Следовать руководству по описаниям и обработке компонентов**: Соблюдать все предоставленные инструкции по описаниям и обработке компонентов.

Пример использования
-------------------------
.. code-block:: python

    # Пример входных данных (JSON)
    input_data = {
        # ... (данные о компонентах)
    }

    # Вызов функции для обработки входных данных
    output_json = process_input(input_data)

    # Вывод результата
    print(output_json)