Название модуля
==============

.. automodule:: module_name
    :members:
    :undoc-members:
    :show-inheritance:

Функции
--------

.. autofunction:: module_name.function_name
    :noindex:

.. autofunction:: module_name.another_function
    :noindex:

Классы
-------

.. autoclass:: module_name.ClassName
    :members:
    :show-inheritance:

.. autoclass:: module_name.AnotherClass
    :members:
    :show-inheritance:

```
```python
# module_name.py
import typing as t
from typing import Optional


class ClassName:
    """
    Краткое описание класса.
    """

    def method_name(self, param: str, param1: Optional[str | dict | str] = None) -> dict | None:
        """
        Аргументы:
            param (str): Описание параметра `param`.
            param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

        Возвращаемое значение:
            dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

        Исключения:
            SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
        """
        pass


def function_name(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Аргументы:
        param (str): Описание параметра `param`.
        param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

    Возвращаемое значение:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Исключения:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
    pass


def another_function(param: int) -> str:
    """
    Аргументы:
        param (int): Целочисленное значение.

    Возвращаемое значение:
        str: Строка, полученная в результате вычислений.
    """
    return str(param)


class AnotherClass:
    """
    Описание другого класса.
    """
    def another_method(self, data: dict) -> None:
        """
        Аргументы:
            data (dict): Словарь данных.

        Возвращаемое значение:
            None: Не возвращает значение.
        """
        pass
```

**Примечание:**

*  Этот пример `index.rst` предполагает, что у вас есть файлы `module_name.py` и `another_module.py`.
*  `module_name` - это имя вашего модуля.
*  `.. automodule::` directive автоматически генерирует документацию для всех членов модуля, включая классы и функции, с учетом docstrings.
*  `:noindex:` - используется для предотвращения повторного появления функции в глобальном индексе.
*  В примере `module_name.py` добавлено несколько классов и функций с docstrings в соответствии со спецификацией.

**Для использования этого `index.rst` с Sphinx:**

1.  Создайте папку (например, `docs`) для документации.
2.  В этой папке создайте файл `index.rst` с содержимым из примера.
3.  Создайте файл `module_name.py` с кодом из примера.
4.  Установите Sphinx: `pip install sphinx sphinx-rtd-theme`
5.  Создайте `conf.py` (файл конфигурации Sphinx), чтобы указать путь к документации.
6.  Запустите Sphinx для генерации HTML-документации: `sphinx-build -b html docs build`


Теперь в папке `build` вы найдете сгенерированную HTML-документацию.