Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот файл (`hypotez/src/webdriver/crawlee_python/__init__.py`) представляет собой инициализационный модуль для пакета `crawlee_python`. Он импортирует класс `CrawleePython` из подмодуля `crawlee_python` и определяет константу `MODE`, которая, вероятно, задаёт режим работы.

Шаги выполнения
-------------------------
1. Определяется константа `MODE` со значением 'dev'.
2. Импортируется класс `CrawleePython` из модуля `crawlee_python`.

Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что модуль crawlee_python уже импортирован.
    from hypotez.src.webdriver.crawlee_python import CrawleePython
    
    # Проверка константы MODE.
    print(CrawleePython.MODE)  # Выведет 'dev'

    # Возможность использования класса CrawleePython (если есть методы)
    # Например:
    # my_crawlee = CrawleePython()
    # my_crawlee.some_method()