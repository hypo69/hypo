Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит набор тестов для модуля `tinytroupe`. Тесты проверяют различные методы агентов, такие как `listen`, `act`, `define`, `socialize` и т.д.  Функции тестов проверяют, что агенты выполняют ожидаемые действия и обновляют соответствующие атрибуты (например, `current_messages`, `episodic_memory`, `_configuration`). Также осуществляется проверка сохранения и загрузки данных агента с использованием метода `save_spec`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых модулей**: Код импортирует `pytest`, `logging`, `sys` и нужные классы из модуля `tinytroupe` и вспомогательного модуля `testing_utils`.
2. **Установка пути для импорта**: Используются методы `sys.path.insert()` для добавления родительских директорий `tinytroupe/` и `../../` в путь поиска модулей.  Это необходимо, чтобы Python мог найти модуль `tinytroupe`, если он расположен в родительской директории.
3. **Создание агентов**: Функции `create_oscar_the_architect()` и `create_lisa_the_data_scientist()` создают экземпляры агентов.
4. **Выполнение тестов**:  Цикл `for` проходит по созданным агентам и запускает серию тестов:
    * **`test_act`**: Проверяет, что агент выполняет действия после получения ввода. Проверяет наличие действий типа "TALK" и "DONE".
    * **`test_listen`**: Проверяет, что агент правильно обрабатывает входящие сообщения, добавляя их в `current_messages` и `episodic_memory`.
    * **`test_define`**: Проверяет, что агент может определять значения в своей конфигурации (`_configuration`) и что обновляет текущий запрос (`current_messages`).
    * **`test_define_several`**: Проверяет, что агент может определять несколько значений в определенной группе.
    * **`test_socialize`**: Проверяет, что агент может взаимодействовать с другим агентом, используя метод `make_agent_accessible`.
    * **`test_see`**: Проверяет обработку визуальных стимулов.
    * **`test_think`**: Проверяет обработку мыслей агента.
    * **`test_internalize_goal`**: Проверяет обработку интернализированной цели.
    * **`test_move_to`**: Проверяет изменение местоположения и контекста.
    * **`test_change_context`**: Проверяет изменение контекста.
    * **`test_save_spec`**: Сохраняет данные агента в файл JSON, используя метод `save_spec`. Загружает сохраненные данные и проверяет, что загруженные данные совпадают с исходными, за исключением имени агента.
5. **Ассерты**: Тесты используют `assert` для проверки ожидаемых результатов и вывода сообщений об ошибках в случае несоответствия.


Пример использования
-------------------------
.. code-block:: python

    # Этот код НЕ является примером использования *тестов*, а показывает как можно использовать функции из модуля tinytroupe
    from tinytroupe.examples import create_oscar_the_architect
    agent = create_oscar_the_architect()
    agent.listen("Hello, how are you?")
    actions = agent.act(return_actions=True)
    print(actions)