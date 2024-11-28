Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот код содержит тест `test_default_llmm_api`, предназначенный для проверки корректности работы API LLM (Large Language Model), используемого в библиотеке TinyTroupe.  Тест проверяет, что API возвращает корректный ответ, содержащий необходимые ключи ("content", "role") и данные, а также соответствует установленным ограничениям по длине и кодировке.


Шаги выполнения
-------------------------
1. Импортирует необходимые модули: `pytest`, `textwrap`, `logging`, `sys` и `openai_utils` из библиотеки TinyTroupe.
2. Устанавливает пути для импорта TinyTroupe, обеспечивая доступ к соответствующим файлам.
3. Создаёт тестовые данные `messages` с помощью функции `create_test_system_user_message`.  Эта функция предполагается определённой в файле `testing_utils.py`.
4. Использует `openai_utils.client().send_message(messages)` для отправки сообщения в API LLM. Результат сохраняется в переменной `next_message`.
5. Выводит полученный ответ в виде словаря (`dict`) и строки.
6. Проверяет, что ответ не пуст (`next_message is not None`) и содержит необходимые ключи `content` и `role`.
7. Проверяет, что значение `content` не пусто (`len(next_message["content"]) >= 1`).
8. Проверяет длину ответа в строковом представлении, убеждаясь, что длина больше или равна 1 и меньше или равна 2000000 символов.
9. Проверяет, что ответ можно закодировать в UTF-8 без ошибок.
10. Выводит в консоль сообщения об успехе или об ошибке.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    import textwrap
    import logging
    import sys
    from tinytroupe import openai_utils

    # Добавьте импорт необходимых файлов
    #  Например, из testing_utils.py:
    from testing_utils import create_test_system_user_message
    
    # ... (код, содержащий функцию create_test_system_user_message)
    
    def test_default_llmm_api():
        messages = create_test_system_user_message("If you ask a cat what is the secret to a happy life, what would the cat say?")
        next_message = openai_utils.client().send_message(messages)
        # ... (проверка результата аналогично коду в примере)