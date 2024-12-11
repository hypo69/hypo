## Improved Code

```python
"""
Модуль для создания документации reStructuredText (RST)
=========================================================================================

Этот модуль содержит функции для преобразования текста в формат reStructuredText (RST),
специально разработанные для документирования кода. Он обеспечивает структурированный
и читаемый способ представления документации для различных элементов кода, таких как
модули, классы, функции и методы.

Пример использования
--------------------

Пример использования функций для создания документации:

.. code-block:: python

    from src.ai.prompts.developer.doc_writer_rst_he import format_module_doc, format_class_doc, format_function_doc

    module_doc = format_module_doc(
        "Модуль для работы с ассистентом программиста",
        "Этот модуль содержит класс :class:`CodeAssistant`...",
        "python",
        [("role", "Роль ассистента"), ("lang", "Язык ассистента"), ("model", "Модели ИИ")]
    )

    class_doc = format_class_doc(
        "Класс для работы с ассистентом программиста",
        "Класс :class:`CodeAssistant` используется для работы с моделями ИИ...",
        [("role", "Роль ассистента"), ("lang", "Язык ассистента"), ("model", "Модели ИИ")],
        ["process_files", "analyze_code"]
    )

    function_doc = format_function_doc(
        "Метод для обработки файлов",
        "Этот метод предназначен для анализа и обработки файлов...",
        [("files", "Список файлов для обработки"), ("options", "Дополнительные параметры")],
        "Результат обработки в виде списка данных"
    )

    print(module_doc)
    print(class_doc)
    print(function_doc)
"""
from typing import List, Tuple


def format_module_doc(
    title: str,
    description: str,
    lang: str,
    attributes: List[Tuple[str, str]] = None,
    methods: List[str] = None,
) -> str:
    """
    Форматирует документацию модуля в формате reStructuredText (RST).

    :param title: Заголовок модуля.
    :param description: Описание модуля.
    :param lang: Язык модуля.
    :param attributes: Список кортежей с именами и описаниями атрибутов.
    :param methods: Список имен методов модуля.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"
    rst_doc += "Пример использования\n"
    rst_doc += "--------------------\n\n"
    rst_doc += f".. code-block:: {lang}\n\n    ...\n\n"

    if attributes:
        rst_doc += "Атрибуты:\n"
        rst_doc += "----------\n"
        for attr_name, attr_desc in attributes:
            rst_doc += f"- `{attr_name}`: {attr_desc}\n"
        rst_doc += "\n"

    if methods:
        rst_doc += "Методы:\n"
        rst_doc += "-------\n"
        for method_name in methods:
            rst_doc += f"- `{method_name}`\n"
        rst_doc += "\n"
    return rst_doc


def format_class_doc(
    title: str,
    description: str,
    attributes: List[Tuple[str, str]] = None,
    methods: List[str] = None,
) -> str:
    """
    Форматирует документацию класса в формате reStructuredText (RST).

    :param title: Заголовок класса.
    :param description: Описание класса.
    :param attributes: Список кортежей с именами и описаниями атрибутов.
    :param methods: Список имен методов класса.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"

    if attributes:
        rst_doc += "Атрибуты:\n"
        rst_doc += "----------\n"
        for attr_name, attr_desc in attributes:
            rst_doc += f"- `{attr_name}`: {attr_desc}\n"
        rst_doc += "\n"

    if methods:
        rst_doc += "Методы:\n"
        rst_doc += "-------\n"
        for method_name in methods:
            rst_doc += f"- `{method_name}`\n"
        rst_doc += "\n"

    rst_doc += "Пример использования:\n"
    rst_doc += "---------------------\n\n"
    rst_doc += ".. code-block:: python\n\n    ...\n\n"

    return rst_doc


def format_function_doc(
    title: str,
    description: str,
    params: List[Tuple[str, str]] = None,
    return_value: str = None,
) -> str:
    """
    Форматирует документацию функции или метода в формате reStructuredText (RST).

    :param title: Заголовок функции или метода.
    :param description: Описание функции или метода.
    :param params: Список кортежей с именами и описаниями параметров.
    :param return_value: Описание возвращаемого значения.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"

    if params:
        rst_doc += "Параметры:\n"
        rst_doc += "-----------\n"
        for param_name, param_desc in params:
            rst_doc += f"- `{param_name}`: {param_desc}\n"
        rst_doc += "\n"

    if return_value:
        rst_doc += "Возвращаемое значение:\n"
        rst_doc += "----------------------\n"
        rst_doc += f"- {return_value}\n\n"
    rst_doc += "Пример использования:\n"
    rst_doc += "---------------------\n\n"
    rst_doc += ".. code-block:: python\n\n    ...\n\n"

    return rst_doc

```

## Changes Made

- Добавлены docstring в формате reStructuredText (RST) для функций `format_module_doc`, `format_class_doc` и `format_function_doc`.
- Добавлено описание модуля.
- Добавлены примеры использования функций в docstring модуля.
- Добавлено описание параметров и возвращаемых значений для каждой функции.
- Изменен порядок блоков в ответе в соответствии с инструкцией.

## FULL Code

```python
"""
Модуль для создания документации reStructuredText (RST)
=========================================================================================

Этот модуль содержит функции для преобразования текста в формат reStructuredText (RST),
специально разработанные для документирования кода. Он обеспечивает структурированный
и читаемый способ представления документации для различных элементов кода, таких как
модули, классы, функции и методы.

Пример использования
--------------------

Пример использования функций для создания документации:

.. code-block:: python

    from src.ai.prompts.developer.doc_writer_rst_he import format_module_doc, format_class_doc, format_function_doc

    module_doc = format_module_doc(
        "Модуль для работы с ассистентом программиста",
        "Этот модуль содержит класс :class:`CodeAssistant`...",
        "python",
        [("role", "Роль ассистента"), ("lang", "Язык ассистента"), ("model", "Модели ИИ")]
    )

    class_doc = format_class_doc(
        "Класс для работы с ассистентом программиста",
        "Класс :class:`CodeAssistant` используется для работы с моделями ИИ...",
        [("role", "Роль ассистента"), ("lang", "Язык ассистента"), ("model", "Модели ИИ")],
        ["process_files", "analyze_code"]
    )

    function_doc = format_function_doc(
        "Метод для обработки файлов",
        "Этот метод предназначен для анализа и обработки файлов...",
        [("files", "Список файлов для обработки"), ("options", "Дополнительные параметры")],
        "Результат обработки в виде списка данных"
    )

    print(module_doc)
    print(class_doc)
    print(function_doc)
"""
from typing import List, Tuple


def format_module_doc(
    title: str,
    description: str,
    lang: str,
    attributes: List[Tuple[str, str]] = None,
    methods: List[str] = None,
) -> str:
    """
    Форматирует документацию модуля в формате reStructuredText (RST).

    :param title: Заголовок модуля.
    :param description: Описание модуля.
    :param lang: Язык модуля.
    :param attributes: Список кортежей с именами и описаниями атрибутов.
    :param methods: Список имен методов модуля.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"
    rst_doc += "Пример использования\n"
    rst_doc += "--------------------\n\n"
    rst_doc += f".. code-block:: {lang}\n\n    ...\n\n"

    if attributes:
        rst_doc += "Атрибуты:\n"
        rst_doc += "----------\n"
        for attr_name, attr_desc in attributes:
            rst_doc += f"- `{attr_name}`: {attr_desc}\n"
        rst_doc += "\n"

    if methods:
        rst_doc += "Методы:\n"
        rst_doc += "-------\n"
        for method_name in methods:
            rst_doc += f"- `{method_name}`\n"
        rst_doc += "\n"
    return rst_doc


def format_class_doc(
    title: str,
    description: str,
    attributes: List[Tuple[str, str]] = None,
    methods: List[str] = None,
) -> str:
    """
    Форматирует документацию класса в формате reStructuredText (RST).

    :param title: Заголовок класса.
    :param description: Описание класса.
    :param attributes: Список кортежей с именами и описаниями атрибутов.
    :param methods: Список имен методов класса.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"

    if attributes:
        rst_doc += "Атрибуты:\n"
        rst_doc += "----------\n"
        for attr_name, attr_desc in attributes:
            rst_doc += f"- `{attr_name}`: {attr_desc}\n"
        rst_doc += "\n"

    if methods:
        rst_doc += "Методы:\n"
        rst_doc += "-------\n"
        for method_name in methods:
            rst_doc += f"- `{method_name}`\n"
        rst_doc += "\n"

    rst_doc += "Пример использования:\n"
    rst_doc += "---------------------\n\n"
    rst_doc += ".. code-block:: python\n\n    ...\n\n"

    return rst_doc


def format_function_doc(
    title: str,
    description: str,
    params: List[Tuple[str, str]] = None,
    return_value: str = None,
) -> str:
    """
    Форматирует документацию функции или метода в формате reStructuredText (RST).

    :param title: Заголовок функции или метода.
    :param description: Описание функции или метода.
    :param params: Список кортежей с именами и описаниями параметров.
    :param return_value: Описание возвращаемого значения.
    :return: Строка документации в формате RST.
    """
    rst_doc = f"{title}\n"
    rst_doc += f"={'=' * len(title)}\n\n"
    rst_doc += f"{description}\n\n"

    if params:
        rst_doc += "Параметры:\n"
        rst_doc += "-----------\n"
        for param_name, param_desc in params:
            rst_doc += f"- `{param_name}`: {param_desc}\n"
        rst_doc += "\n"

    if return_value:
        rst_doc += "Возвращаемое значение:\n"
        rst_doc += "----------------------\n"
        rst_doc += f"- {return_value}\n\n"
    rst_doc += "Пример использования:\n"
    rst_doc += "---------------------\n\n"
    rst_doc += ".. code-block:: python\n\n    ...\n\n"

    return rst_doc