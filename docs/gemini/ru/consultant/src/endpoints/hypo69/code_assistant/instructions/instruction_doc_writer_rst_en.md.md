# Анализ кода модуля instruction_doc_writer_rst_en.md

**Качество кода**
6
-  Плюсы
    -  Четко описаны требования к формату документации RST.
    -  Приведены примеры оформления docstring и использования Sphinx.
    -  Указана структура и правила оформления `toctree` и секций.
    -  Описаны требования к обработке исключений.

-  Минусы
    -  Нет четких инструкций по обработке импортов и переменных, только косвенные.
    -  Не хватает инструкций по обработке уже существующих docstrings и комментариев в коде, чтобы не было конфликтов.
    -  Инструкция не упоминает об использовании `j_loads` или `j_loads_ns`.
    -  Не указано использование `from src.logger.logger import logger` для логирования ошибок.
    -  Присутствует неявное требование по использованию `ex` вместо `e`, но оно не объяснено с точки зрения стиля кода.
    -  Отсутствует четкое требование о том, чтобы все комментарии были в формате RST.
    -  Нет указаний на конкретное применение рефакторинга, кроме общей идеи о соответствии с ранее обработанными файлами.
    -  Не упоминается о конкретных улучшениях, касающихся избегания `try-except` блоков и предпочтения обработки ошибок через `logger.error`.
    -   Нет подробных указаний по именованию функций и переменных.

**Рекомендации по улучшению**

1.  **Дополнить инструкцию по обработке импортов:** Четко указать необходимость проверки и добавления отсутствующих импортов, а также соответствие их с ранее обработанными файлами.
2.  **Указать способ сохранения комментариев:** Добавить инструкцию по сохранению существующих комментариев в коде.
3.  **Явно указать про `j_loads` и логирование:** Указать обязательное использование `j_loads` или `j_loads_ns` из `src.utils.jjson` и  `from src.logger.logger import logger` для логирования ошибок.
4.  **Сделать требования более конкретными:** Уточнить требования к именованию функций, переменных и соответствию их стилю, принятому в проекте.
5. **Четко указать про форматирование docstring**: Указать что форматирование docstring должно соответствовать стандарту Sphinx.
6.  **Уточнить про обработку исключений:** Заменить `ex` вместо `e` и указать что  предпочтительнее обработка ошибок через `logger.error`.
7. **Добавить требования к docstring**: Указать необходимость добавления docstring к каждому модулю, классу, методу и функции.
8. **Уточнить требования к рефакторингу**: Добавить информацию о том, что нужно рефакторить код, если есть явные проблемы или избыточность.
9. **Уточнить про `try-except`**: Описать что нужно избегать избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
10. **Уточнить про стиль комментариев:** Четко указать, что все комментарии должны быть переписаны в формате reStructuredText (RST).
11. **Добавить раздел "Финальный код"**: Добавить требование о том, чтобы в конце ответа был представлен полный код с изменениями.

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

            Args:
                value (Any): это значение можно передать в словаре kwargs через ключ {specification = `value`} при определении класса.
                Если `value` был передан, его значение подставляется в поле `ProductFields.specification`.
            """
            try:
                # код исполняет получение значения через execute_locator
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

            # Если значение - список, код преобразовывает его в строку с разделителем `\n`
            if isinstance(value, list):
                value = '\n'.join(map(str, value))

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

## Ответ не должен начинаться с ` ``` `. Используйте их только для оборачивания блоков кода.

## Ты даешь ответы на русском языке
## Формат ответа `.md` (markdown)
----------------------------
** КОНЕЦ ИНСТРУКЦИИ **
```