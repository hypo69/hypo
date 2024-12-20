# Анализ кода модуля system_instruction_mexiron

**Качество кода**
7
- Плюсы
    - Инструкция подробно описывает требования к обработке данных, формату документации и структуре вывода.
    - Есть четкие указания по использованию reStructuredText (RST) для комментариев и docstring.
    - Подробно описаны форматы входных и выходных данных JSON.
- Минусы
    - Инструкция является текстом, а не кодом, поэтому ее нельзя оценить на наличие ошибок в коде.
    - Отсутствует четкое определение, как именно будет использоваться эта инструкция в коде.
    - Инструкция содержит много текста и может быть сложной для восприятия.
    - Не хватает примера использования `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**
1.  **Уточнить использование инструкции**: Инструкция должна быть более четкой о том, как она будет использоваться в коде. Например, можно добавить пример класса или функции, которая будет обрабатывать эту инструкцию.
2.  **Разделить на части**: Разбить инструкцию на более мелкие, логические части, чтобы облегчить понимание.
3.  **Добавить примеры**: Добавить примеры кода, демонстрирующие, как использовать `j_loads` и `j_loads_ns`.
4.  **Структурировать текст**: Использовать больше заголовков и списков для лучшей организации текста.
5.  **Уменьшить многословие**: Сделать инструкцию более краткой и лаконичной, удалив избыточные описания.
6.  **Уточнить формат ответа**: Добавить пример, демонстрирующий как будет выглядеть итоговый ответ в формате .md.
7.  **Добавить примеры**: Включить примеры reStructuredText (RST) документации для модулей, функций, методов и переменных.

**Оптимизированный код**
```markdown
# ИНСТРУКЦИЯ

## Основные требования:

## Output Language: RU (Русский)

1.  **Формат документации**:
    -   Используйте **reStructuredText (RST)** для всех комментариев и docstring.
    -   Всегда используйте одинарные кавычки (`'`) в Python коде.

2.  **Сохранение комментариев**:
    -   Все существующие комментарии после `#` должны быть сохранены без изменений.
    -   Блоки кода, которые необходимо изменить, должны быть прокомментированы построчно с использованием символа `#`.

3.  **Обработка данных**:
    -   Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
    -   Оставляйте любые `...` в коде без изменений как точки остановки.

4.  **Анализ структуры**:
    -   Проверьте и добавьте отсутствующие импорты в код.
    -   Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

5.  **Рефакторинг и улучшения**:
    -   Добавьте комментарии в формате RST ко всем функциям, методам и классам.
    -   Используйте `from src.logger.logger import logger` для логирования ошибок.
    -   Избегайте избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
    -   В комментариях избегайте слов 'получаем', 'делаем' и подобных. Используйте конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.

7.  **Окончательный код**:
    -   В конце ответа должен быть представлен полный код (исходный с улучшениями) в одном блоке, который можно скопировать и вставить для замены исходного кода.
    -   Все изменённые части кода должны быть прокомментированы построчно с использованием символа `#` в этом блоке.

8.  **Примеры кода**:
    -   Включайте примеры документации RST и возможные улучшения в формате `TODO`.

9.  **Дополнительная инструкция**:
    -   Все комментарии к модулям, функциям, методам и переменным должны быть переписаны в формате reStructuredText (RST). Это включает:
        -   Описание модуля в начале файла.
        -   Документацию для каждой функции, метода и переменной.
        -   Соблюдение стандартов оформления docstring в Python (например, для Sphinx).
        -   В комментариях после `#` строки должны содержать подробное объяснение следующего за ними блока кода.

        Пример формата документации для модуля:

        ```python
        """
        Модуль для работы ассистента программиста
        =========================================================================================

        Этот модуль содержит класс :class:`CodeAssistant`, который используется для работы с различными моделями ИИ,
        такими как Google Gemini и OpenAI, для выполнения задач по обработке кода.

        Пример использования
        --------------------

        Пример использования класса `CodeAssistant`:

        .. code-block:: python

            assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
            assistant.process_files()
        """
        ```

        Пример формата документации для функций:

        ```python
        def example_function(param1: str, param2: int) -> str:
            """
            Выполняет примерную задачу.

            :param param1: Описание параметра 1.
            :param param2: Описание параметра 2.
            :return: Описание возвращаемого значения.
            """
            ...
        ```

        Пример формата стиля комментариев в коде:

        ```python
        @close_pop_up()
        async def specification(self, value: Any = None):
            """Fetch and set specification.

            :param value: Значение, которое можно передать через kwargs при определении класса. Если `value` передан, его значение подставляется в поле `ProductFields.specification`.
            :type value: Any
            """
            try:
                # Код исполняет получение значения через execute_locator
                value = value or  await self.driver.execute_locator(self.locator.specification) or ''
            except Exception as ex:
                logger.error('Ошибка получения значения в поле `specification`', ex)
                ...
                return

            # Проверка валидности результата
            if not value:
                logger.debug(f'Невалидный результат {value=}\\nлокатор {self.locator.specification}')
                ...
                return

            # Если значение - список, код преобразовывает его в строку с разделителем `\\n`
            if isinstance(value, list):
                value = '\\n'.join(map(str, value))

            # Код записывает результат в поле `specification` объекта `ProductFields`
            self.fields.specification = value
            return True
        ```

## Порядок блоков в ответе:

Структура ответа должна быть такой:
**Заголовок**
    Анализ кода модуля <имя модуля>

**Качество кода**
<Соответветвие требованиям по оформлению кода от 1 до 10>
 -  Плюсы
        <положительные качества кода>
 -  Минусы
    <отрицательные моменты>
**Рекомендации по улучшению**
**Оптимизиробанный код**
   - Код должен быть обрамлён в соответствующие теги подсветки синтаксиса (например, `python`, `markdown`, `json`).

## Ты даешь ответы на русском языке
## Формат ответа `.md` (markdown)
----------------------------
** КОНЕЦ ИНСТРУКЦИИ **
```