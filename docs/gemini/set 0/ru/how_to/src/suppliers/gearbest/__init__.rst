Как использовать модуль gearbest
========================================================================================

Описание
-------------------------
Модуль `gearbest` содержит константу `MODE` и импортирует класс `Graber` из подмодуля `graber`.  Константа `MODE` задаёт режим работы, в данном случае `'dev'`. Класс `Graber` вероятно отвечает за получение данных с сайта GearBest.

Шаги выполнения
-------------------------
1. Модуль инициализирует константу `MODE` со значением `'dev'`.
2. Модуль импортирует класс `Graber` из подмодуля `graber`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.gearbest import Graber

    # Инициализация объекта Graber (предполагается, что это необходимо)
    graber_instance = Graber()

    # Пример использования методов класса Graber (если таковые имеются)
    # Например, получение данных с сайта
    # ... код вызова методов класса Graber ...