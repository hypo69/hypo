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
```
```python
import re
from typing import Optional, Dict, List


def function_name(param: str, param1: Optional[str | Dict | str] = None) -> Dict | None:
    """
    Аргументы:
        param (str): Описание параметра `param`.
        param1 (Optional[str | Dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

    Возвращаемое значение:
        Dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Исключения:
        SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
    """
    try:
        # Здесь будет ваш код
        if param1 is not None:
            if isinstance(param1, str):
                return {"result": param + param1}
            elif isinstance(param1, dict):
                return {"result": param + str(param1)}
        else:
            return {"result": param}
    except SomeError as ex:
        raise SomeError("Ошибка в функции: " + str(ex))