# Инструкция по написанию документации в формате RST

Эта инструкция описывает формат и структуру документации в формате reStructuredText (RST) для Python-кода.

## Формат документации

Используйте стандарт reStructuredText (.rst). Каждый файл должен начинаться с заголовка и краткого описания его содержимого.  Для функций и классов используйте следующую структуру документации:

```python
def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра `param`.
        param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Raises:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
    # ... тело функции ...
```

Используйте `ex` вместо `e` в блоках обработки исключений.

## Структура файла (.rst)

Каждый файл должен быть файлом RST, с использованием директив Sphinx для автоматической генерации документации.  Главным файлом (например, `index.rst`) является входная точка для генерации документации. В нём используйте директивы `.. toctree::` для построения дерева оглавления (TOC).

```rst
# Модуль `my_module`
=================

.. automodule:: my_module
   :members:
   :undoc-members:
   :show-inheritance:

.. toctree::
   :maxdepth: 2

   my_module
```

В других файлах (`my_module.rst`) используйте  `.. automodule::` и `.. autofunction::` для документирования функций и классов. Примеры:

```rst
.. automodule:: my_module
   :members:
```

```rst
.. autofunction:: my_module.some_function
```

```rst
.. autoclass:: my_module.MyClass
   :members:
```

## Оглавление (TOC)

В файле `index.rst` используйте директиву `.. toctree::` для автоматического создания оглавления, которое будет ссылаться на другие файлы RST.

```rst
.. toctree::
   :maxdepth: 2

   my_module.rst
   other_module.rst
```


## Форматирование документации


Внутри файлов RST используйте правильный синтаксис для заголовков, списков, и ссылок.  Не забывайте использовать directives Sphinx для автоматической генерации документации по коду (как показано в примерах выше).


## Пример файла `index.rst`

```rst
# Модуль `my_module`
=================

.. toctree::
   :maxdepth: 2

   my_module.rst

```

## Пример файла `my_module.rst`

```rst
Модуль my_module
-----------------

.. automodule:: my_module
   :members:
   :undoc-members:
   :show-inheritance:
```

## Важные замечания

*  Убедитесь, что у вас установлена среда разработки для Sphinx.
*  Для генерации документации используйте утилиты Sphinx.

Эта инструкция предоставляет базовые принципы.  Более детальная информация о Sphinx поможет вам в написании более сложных и полных документов.