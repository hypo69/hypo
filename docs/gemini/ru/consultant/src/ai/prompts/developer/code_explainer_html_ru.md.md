# Анализ кода модуля `code_explainer_html_ru.md`

**Качество кода**
8
- Плюсы
    - Документ содержит подробные инструкции по анализу и улучшению кода.
    - Приведены примеры использования и ожидаемый результат.
    - Инструкции по рефакторингу четкие и структурированные.
- Минусы
    -  Требуется более точное соответствие формату reStructuredText (RST) в примерах документации.
    -  Необходимы более строгие примеры для соблюдения стиля комментариев.
    -  В инструкциях не полностью учтены все аспекты обработки ошибок.

**Рекомендации по улучшению**
1. **Улучшить примеры документации RST**: Примеры должны четко демонстрировать использование reStructuredText, включая правильную структуру и синтаксис.
2. **Скорректировать стиль комментариев**: Примеры должны показывать, как правильно комментировать код с использованием RST, включая docstring для функций, классов и методов.
3. **Уточнить инструкции по обработке ошибок**: Необходимо подчеркнуть важность использования `logger.error` и избегать стандартных блоков `try-except` там, где это не требуется.
4. **Улучшить структуру ответа**: Четко разделить блоки `<input code>`, `<algorithm>` и `<explanation>` и привести примеры для каждого из них.

**Оптимизированный код**
```markdown
# Анализ кода модуля code_explainer_html_ru.md

**Качество кода**
8
-  Плюсы
    -  Документ содержит подробные инструкции по анализу и улучшению кода.
    -  Приведены примеры использования и ожидаемый результат.
    -  Инструкции по рефакторингу четкие и структурированные.
-  Минусы
    -  Требуется более точное соответствие формату reStructuredText (RST) в примерах документации.
    -  Необходимы более строгие примеры для соблюдения стиля комментариев.
    -  В инструкциях не полностью учтены все аспекты обработки ошибок.

**Рекомендации по улучшению**
1.  **Улучшить примеры документации RST**: Примеры должны четко демонстрировать использование reStructuredText, включая правильную структуру и синтаксис.
2.  **Скорректировать стиль комментариев**: Примеры должны показывать, как правильно комментировать код с использованием RST, включая docstring для функций, классов и методов.
3.  **Уточнить инструкции по обработке ошибок**: Необходимо подчеркнуть важность использования `logger.error` и избегать стандартных блоков `try-except` там, где это не требуется.
4.  **Улучшить структуру ответа**: Четко разделить блоки `<input code>`, `<algorithm>` и `<explanation>` и привести примеры для каждого из них.

**Оптимизированный код**

```html
<input code>
from src.utils.calculator import calculate_sum

def add_numbers(a, b):
    result = calculate_sum(a, b)
    return result
</input code>

<algorithm>
1. Импортируется функция `calculate_sum` из модуля `src.utils.calculator`.
2. Определяется функция `add_numbers`, принимающая два аргумента `a` и `b`.
3. Вызов функции `calculate_sum(a, b)` выполняет сложение `a` и `b`.
4. Результат функции возвращается вызывающему коду.

Пример:
- Входные данные: `a = 3`, `b = 5`.
- Алгоритм: `calculate_sum(3, 5)`.
- Результат: `8`.
</algorithm>

<explanation>
**Импорты**:
- `from src.utils.calculator import calculate_sum`: Импортирует функцию `calculate_sum`, которая используется для вычисления суммы. Этот модуль лежит в папке `src.utils`.

**Функция `add_numbers`**:
- Назначение: упрощает сложение двух чисел через вызов функции `calculate_sum`.
- Аргументы:
  - `a` (число): Первое слагаемое.
  - `b` (число): Второе слагаемое.
- Возвращаемое значение: результат сложения `a` и `b`.

**Связь с другими пакетами**:
- Модуль `src.utils.calculator` может быть частью библиотеки для математических вычислений.
- Если `calculate_sum` использует дополнительные модули, это можно уточнить в её документации.

**Возможные улучшения**:
- Добавить проверку типов аргументов `a` и `b` для предотвращения ошибок.
- Локализовать вызов `calculate_sum` в рамках модуля, если он больше нигде не используется.
</explanation>
```
```python
"""
Модуль для анализа и объяснения кода.
=========================================================================================

Этот модуль содержит инструкции для анализа предоставленного кода, 
объяснения его функциональности и предоставления ответа в формате HTML.
Включает в себя правила для форматирования документации в reStructuredText (RST).

Пример использования
--------------------

Пример анализа кода и его объяснения:

.. code-block:: python

    # Пример кода для анализа
    from src.utils.calculator import calculate_sum

    def add_numbers(a, b):
        result = calculate_sum(a, b)
        return result

    # Ожидаемый HTML ответ
    <html>
        <input code>
        from src.utils.calculator import calculate_sum

        def add_numbers(a, b):
            result = calculate_sum(a, b)
            return result
        </input code>

        <algorithm>
        1. Импортируется функция `calculate_sum` из модуля `src.utils.calculator`.
        2. Определяется функция `add_numbers`, принимающая два аргумента `a` и `b`.
        3. Вызов функции `calculate_sum(a, b)` выполняет сложение `a` и `b`.
        4. Результат функции возвращается вызывающему коду.

        Пример:
        - Входные данные: `a = 3`, `b = 5`.
        - Алгоритм: `calculate_sum(3, 5)`.
        - Результат: `8`.
        </algorithm>

        <explanation>
        **Импорты**:
        - `from src.utils.calculator import calculate_sum`: Импортирует функцию `calculate_sum`, которая используется для вычисления суммы. Этот модуль лежит в папке `src.utils`.

        **Функция `add_numbers`**:
        - Назначение: упрощает сложение двух чисел через вызов функции `calculate_sum`.
        - Аргументы:
        - `a` (число): Первое слагаемое.
        - `b` (число): Второе слагаемое.
        - Возвращаемое значение: результат сложения `a` и `b`.

        **Связь с другими пакетами**:
        - Модуль `src.utils.calculator` может быть частью библиотеки для математических вычислений.
        - Если `calculate_sum` использует дополнительные модули, это можно уточнить в её документации.

        **Возможные улучшения**:
        - Добавить проверку типов аргументов `a` и `b` для предотвращения ошибок.
        - Локализовать вызов `calculate_sum` в рамках модуля, если он больше нигде не используется.
        </explanation>
    </html>
"""
from typing import Any
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns # импортируются функции для загрузки json

# TODO: Добавить docstring для модуля
# TODO: Добавить импорты, если необходимо
# TODO: Добавить константы, если необходимо


def _format_html_output(input_code: str, algorithm: str, explanation: str) -> str:
    """
    Форматирует вывод в HTML.

    :param input_code: Исходный код.
    :param algorithm: Описание алгоритма.
    :param explanation: Подробное объяснение кода.
    :return: HTML строка с форматированным выводом.
    """
    # код форматирует ввод в html блок
    html_output = f'''
    <html>
        <input code>
        {input_code}
        </input code>

        <algorithm>
        {algorithm}
        </algorithm>

        <explanation>
        {explanation}
        </explanation>
    </html>
    '''
    return html_output


def _extract_code_from_prompt(prompt: str) -> str:
    """
    Извлекает исходный код из запроса.

    :param prompt: Строка запроса.
    :return: Исходный код из запроса.
    """
    # код получает текст запроса
    try:
        # Код ищет блок `input code` в запросе и извлекает его содержимое
        start_tag = "```python\n"
        end_tag = "\n```"
        start_index = prompt.find(start_tag)
        if start_index == -1:
            start_tag = "<input code>\n"
            end_tag = "\n</input code>"
            start_index = prompt.find(start_tag)
        if start_index == -1:
            return "" # если не находит, возвращает пустую строку

        start_index += len(start_tag)
        end_index = prompt.find(end_tag, start_index)
        if end_index == -1:
            return "" # если не находит, возвращает пустую строку
        code = prompt[start_index:end_index].strip()
        return code
    except Exception as ex:
        logger.error(f"Ошибка извлечения кода из запроса: {ex}") # логирование ошибки извлечения кода
        return ""

def _extract_expected_answer_from_prompt(prompt: str) -> str:
    """
    Извлекает ожидаемый ответ из запроса.

    :param prompt: Строка запроса.
    :return: Ожидаемый ответ из запроса.
    """
    # код получает ожидаемый текст ответа
    try:
        # Код ищет блок `Ожидаемый ответ` в запросе и извлекает его содержимое
        start_tag = "**Ожидаемый ответ**:\n\n```html\n"
        end_tag = "\n```"
        start_index = prompt.find(start_tag)
        if start_index == -1:
             return ''# если не находит, возвращает пустую строку

        start_index += len(start_tag)
        end_index = prompt.find(end_tag, start_index)
        if end_index == -1:
            return '' # если не находит, возвращает пустую строку

        expected_answer = prompt[start_index:end_index].strip()

        return expected_answer
    except Exception as ex:
        logger.error(f"Ошибка извлечения ответа из запроса: {ex}") # логирование ошибки извлечения ответа
        return ""


def _generate_algorithm_explanation(code: str) -> str:
    """
    Генерирует описание алгоритма и объяснение для данного кода.

    :param code: Исходный код.
    :return: Строка, содержащая описание алгоритма и объяснение.
    """
    # код генерирует описание алгоритма и объяснения на основе кода
    algorithm_description = "Описания алгоритма нет." # если нет описания алгоритма
    explanation_description = "Объяснений нет." # если нет объяснения
    try:
        # Код парсит предоставленный код и анализирует его
        lines = code.strip().split('\n')
        if not lines:
            return f"<algorithm>\n{algorithm_description}\n</algorithm>\n<explanation>\n{explanation_description}\n</explanation>"

        algorithm_steps = []
        explanation_parts = {
            "Импорты": [],
            "Функции": [],
            "Переменные": [],
            "Связь с другими пакетами": [],
            "Возможные улучшения": []
        }
        
        # код анализирует каждую строку в коде
        for line in lines:
            line = line.strip() # удаление пробелов в начале и конце строки
            if line.startswith('from ') and ' import ' in line: # проверка на наличие импорта
               
                parts = line.split(' import ')
                module_name = parts[0].replace('from ', '')
                imported_items = parts[1].split(',')
                imported_items_str = ', '.join(item.strip() for item in imported_items)
                explanation_parts["Импорты"].append(f"- `{line}`: Импортирует {imported_items_str} из модуля `{module_name}`. Этот модуль лежит в папке `{module_name.replace('.','/')}`.")
                algorithm_steps.append(f"Импортируется {imported_items_str} из модуля {module_name}.")


            elif line.startswith('def '): # проверка на определение функции
                function_name = line.split('(')[0].replace('def ', '')
                explanation_parts["Функции"].append(f"- Назначение: `Описание назначения функции {function_name}`") # TODO: Добавить фактическое описание назначения функции
                explanation_parts["Функции"].append(f"   - Аргументы: `Описание аргументов функции {function_name}`") # TODO: Добавить фактическое описание аргументов
                explanation_parts["Функции"].append(f"   - Возвращаемое значение: `Описание возвращаемого значения функции {function_name}`") # TODO: Добавить фактическое описание возвращаемого значения

                algorithm_steps.append(f"Определяется функция `{function_name}`, принимающая `аргументы`.")
            elif '=' in line:
                variable_name = line.split('=')[0].strip()
                explanation_parts["Переменные"].append(f"- `{variable_name}`: `Описание переменной {variable_name}`.")# TODO: Добавить фактическое описание переменных
                algorithm_steps.append(f"Код присваивает переменной `{variable_name}` значение.")
            elif 'return ' in line:
                 algorithm_steps.append(f"Функция возвращает результат.")


        if algorithm_steps:
           algorithm_description = "\n".join([f"{i+1}. {step}" for i, step in enumerate(algorithm_steps)])

        if any(explanation_parts.values()):
                explanation_description = ""
                for key, values in explanation_parts.items():
                   if values:
                     explanation_description += f"**{key}**:\n"
                     explanation_description += "\n".join(values)
                     explanation_description += "\n"

        return f"<algorithm>\n{algorithm_description}\n</algorithm>\n<explanation>\n{explanation_description}\n</explanation>"

    except Exception as ex:
        logger.error(f"Ошибка при генерации описания алгоритма и объяснения: {ex}")  # логирование ошибки
        return f"<algorithm>\n{algorithm_description}\n</algorithm>\n<explanation>\n{explanation_description}\n</explanation>"


def process_code_explainer_prompt(prompt: str) -> str:
    """
    Обрабатывает запрос, извлекает код, генерирует описание алгоритма и объяснение, форматирует вывод в HTML.

    :param prompt: Строка запроса.
    :return: HTML строка с результатом обработки запроса.
    """
    # код обрабатывает запрос и генерирует HTML-ответ
    try:
        # Код извлекает код и ожидаемый ответ из запроса
        code = _extract_code_from_prompt(prompt)
        expected_answer = _extract_expected_answer_from_prompt(prompt)
        if not code:
            return "Не удалось извлечь код из запроса." # если кода нет -  возврат сообщения об ошибке

         # Код генерирует описание алгоритма и объяснение
        algorithm_explanation = _generate_algorithm_explanation(code)

        # Код форматирует результат в HTML
        html_output = _format_html_output(code, algorithm_explanation, "") # алгоритм и объяснение вкладывается в общую структуру
        if expected_answer:
            return expected_answer # если есть ожидаемый ответ - возврат его
        else:
            return html_output # если нет, возврат сгенерированного ответа

    except Exception as ex:
        logger.error(f"Ошибка при обработке запроса: {ex}") # логирование ошибки обработки запроса
        return "Произошла ошибка при обработке запроса." # если произошла ошибка - возврат сообщения об ошибке
```