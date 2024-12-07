Как использовать модуль hypotez/src/category/__init__.py
========================================================================================

Описание
-------------------------
Модуль `hypotez/src/category/__init__.py` определяет константу `MODE`, имеющую значение 'dev'.  Он также импортирует класс `Category` из подмодуля `category`.

Шаги выполнения
-------------------------
1. Модуль импортирует константу `MODE` со значением 'dev'.
2. Модуль импортирует класс `Category` из подмодуля `category`.  Это указывает, что для работы с функционалом, связанным с категориями, необходимо использовать класс `Category` из подмодуля `category`.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.category import Category

    # В дальнейшем вы можете использовать класс Category для работы с категориями.
    # Пример использования (предполагается, что класс Category содержит нужные методы):
    # my_category = Category(name='Новая категория')
    # print(my_category.name)