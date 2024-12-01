Как использовать этот блок кода
=========================================================================================\n

Описание
-------------------------
Этот фрагмент кода импортирует функции `pprint` и `pretty_print` и использует функцию `pprint` для вывода строки "Hello, world!".

Шаги выполнения
-------------------------
1. Импортирует модуль `header`.
2. Импортирует функцию `pprint` из `pprint` и функцию `pretty_print` как `pretty_print` из модуля `pprint`.
3. Импортирует функцию `pprint` из модуля `src.printer`.
4. Вызывает функцию `pprint` со строкой "Hello, world!" в качестве аргумента.  Результат вывода зависит от реализации функции `pprint` в `src.printer`.

Пример использования
-------------------------
.. code-block:: python

    import header
    from pprint import pprint as pretty_print
    from src.printer import pprint

    pprint("Hello, world!")