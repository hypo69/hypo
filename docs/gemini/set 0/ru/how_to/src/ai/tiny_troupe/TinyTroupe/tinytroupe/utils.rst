Как использовать функцию compose_initial_LLM_messages_with_templates
========================================================================================

Описание
-------------------------
Эта функция генерирует начальные сообщения для вызова модели LLM.  Она предполагает, что вызов всегда включает системное сообщение (описание общей задачи) и необязательное пользовательское сообщение (описание конкретной задачи). Сообщения формируются на основе указанных шаблонов и конфигурации рендеринга.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек**:  Функция импортирует модули `re`, `json`, `os`, `sys`, `hashlib`, `textwrap`, `logging`, `chevron`, `copy`, `typing`, `datetime`, `pathlib`, `configparser`.

2. **Определение функции**: Определяется функция `compose_initial_LLM_messages_with_templates`.

3. **Получение путей к шаблонам**: Функция формирует пути к системному и (необязательному) пользовательскому шаблонам на основе входных параметров `system_template_name` и `user_template_name`, добавляя префикс `prompts/`. Пути создаются относительно текущей директории файла `utils.py`.

4. **Инициализация списка сообщений**: Создается пустой список `messages`.

5. **Обработка системного сообщения**: Добавляется системное сообщение в список `messages`.  Создаётся словарь с ролью "system" и содержанием, сгенерированным из шаблона `system_template_name` с использованием `chevron.render` и `rendering_configs`.

6. **Обработка пользовательского сообщения (необязательно)**: Если `user_template_name` задан, добавляется пользовательское сообщение в список `messages`.  Аналогично, формируется словарь с ролью "user" и содержанием, сгенерированным из шаблона `user_template_name` с использованием `chevron.render` и `rendering_configs`.

7. **Возврат списка сообщений**: Функция возвращает список `messages` содержащий сформированные сообщения.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.utils import compose_initial_LLM_messages_with_templates
    import chevron

    rendering_configs = {"task_name": "Generating Report", "input_data": "some data"}

    messages = compose_initial_LLM_messages_with_templates(
        system_template_name="system_template.txt",
        user_template_name="user_template.txt",
        rendering_configs=rendering_configs
    )

    print(messages)