# Анализ кода модуля code_checker_md_en.md

**Качество кода**
7
-  Плюсы
    - Код содержит подробные инструкции и примеры для работы с различными типами файлов.
    - Четко определены правила форматирования и документирования кода.
    - Инструкции структурированы и легко читаются.
-  Минусы
    - Некоторые инструкции дублируются, что может вызвать путаницу.
    - Инструкции местами излишне многословны.
    - Не хватает четкого разделения инструкций по типам файлов (Python, MD, RST).

**Рекомендации по улучшению**
1. **Устранить дублирование**:
    - Объединить повторяющиеся инструкции, особенно касающиеся общей структуры ответов.
2. **Уточнить разделы**:
    - Разделить инструкции для разных типов файлов (Python, MD, RST) на отдельные подразделы для большей ясности.
3. **Упростить формулировки**:
    - Избегать излишней многословности, используя более краткие и точные выражения.
4. **Уточнить обработку ошибок**:
   -  Указать, как конкретно следует использовать `logger.error`, избегая общих фраз.
5. **Расширить примеры**:
   - Добавить больше примеров для каждого типа файлов (Python, MD, RST), включая более сложные случаи.
6. **Добавить примеры документации**:
   -  Включить примеры форматирования документации в стиле RST для функций и классов, а также примеры использования `TODO`.
7. **Структура ответа**:
   - Описать структуру ответа более формально, указав, как должны располагаться заголовки и разделы.

**Оптимизированный код**
```markdown
# ИНСТРУКЦИЯ
## Основные требования:
## Output Language: RU (Русский)

1. **Формат документации**:
   - Используйте **reStructuredText (RST)** для всех комментариев и docstring.
   - Всегда используйте одинарные кавычки (`'`) в Python коде.

2. **Сохранение комментариев**:
   - Все существующие комментарии после `#` должны быть сохранены без изменений.
   - Блоки кода, которые необходимо изменить, должны быть прокомментированы построчно с использованием символа `#`.

3. **Обработка данных**:
   - Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
   - Оставляйте любые `...` в коде без изменений как точки остановки.

4. **Анализ структуры**:
   - Проверьте и добавьте отсутствующие импорты в код.
   - Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

5. **Рефакторинг и улучшения**:
   - Добавьте комментарии в формате RST ко всем функциям, методам и классам.
   - Используйте `from src.logger.logger import logger` для логирования ошибок.
   - Избегайте избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
   - В комментариях избегайте слов 'получаем', 'делаем' и подобных. Используйте конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.

6.  **Обработка `...`**:
   - Оставляйте `...` как точки остановки в коде без изменений. Не добавляйте к ним документацию.

7. **Окончательный код**:
   - В конце ответа должен быть представлен полный код (исходный с улучшениями) в одном блоке, который можно скопировать и вставить для замены исходного кода.
   - Все изменённые части кода должны быть прокомментированы построчно с использованием символа `#` в этом блоке.

8. **Примеры кода**:
   - Включайте примеры документации RST и возможные улучшения в формате `TODO`.

9. **Дополнительная инструкция**:
   - Все комментарии к модулям, функциям, методам и переменным должны быть переписаны в формате reStructuredText (RST). Это включает:
     - Описание модуля в начале файла.
     - Документацию для каждой функции, метода и переменной.
     - Соблюдение стандартов оформления docstring в Python (например, для Sphinx).
     - В комментариях после `#` строки должны содержать подробное объяснение следующего за ними блока кода.

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