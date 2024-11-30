Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит набор юнит-тестов для класса `TinyPerson` из пакета `tinytroupe`. Тесты проверяют различные аспекты работы агента, включая обработку ввода, выполнение действий, определение и изменение параметров, взаимодействие с другими агентами, и сохранение/загрузку данных.

Шаги выполнения
-------------------------
1. **Импорт необходимых модулей:** Код импортирует модули `pytest`, `logging`, `sys` и классы `create_oscar_the_architect`, `create_lisa_the_data_scientist` из пакета `tinytroupe`, а также вспомогательные функции из `testing_utils`.
2. **Установка пути импорта:** Код добавляет пути к папкам `tinytroupe` и `.` в переменную `sys.path`, чтобы система могла найти необходимые модули.
3. **Определение тестовых функций:** Функции `test_act`, `test_listen`, `test_define`, `test_define_several`, `test_socialize`, `test_see`, `test_think`, `test_internalize_goal`, `test_move_to`, `test_change_context`, и `test_save_spec` содержат утверждения (assert), которые проверяют различные аспекты работы агентов `Oscar` и `Lisa`.
4. **Инициализация агентов:** В тестах создаются экземпляры агентов `Oscar` и `Lisa` с помощью функций `create_oscar_the_architect` и `create_lisa_the_data_scientist`.
5. **Вызов методов агентов:** Для каждого агента вызываются методы `listen`, `act`, `define`, `define_several`, `make_agent_accessible`, `see`, `think`, `internalize_goal`, `move_to`, `change_context` и `save_spec` с соответствующими аргументами.
6. **Проверка результатов:**  Утверждения (assert) проверяют, что методы агентов возвращают ожидаемые результаты (например, длину списка действий, наличие определенных типов действий, корректность параметров конфигурации, наличие сообщений в памяти).
7. **Сохранение и загрузка:** В тесте `test_save_spec` данные о сохраняются, а затем загружаются в новый экземпляр агента с другим именем. Проверяется корректность загрузки, и что загрузка не приводит к изменению данных, кроме имени агента.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    from tinytroupe.examples import create_oscar_the_architect
    from testing_utils import *

    def test_act_example(setup):
        agent = create_oscar_the_architect()
        actions = agent.listen_and_act("Tell me a bit about your life.", return_actions=True)
        assert len(actions) >= 1
        assert contains_action_type(actions, "TALK")
        assert terminates_with_action_type(actions, "DONE")