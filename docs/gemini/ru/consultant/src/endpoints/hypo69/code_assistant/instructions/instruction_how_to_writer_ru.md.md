# Анализ кода модуля instruction_how_to_writer_ru.md

**Качество кода**
8
- Плюсы
    - Описание структуры и требований к инструкциям четкое и понятное.
    - Использование reStructuredText (RST) для форматирования документации является хорошей практикой.
    - Приведены примеры форматирования документации и комментариев.
    - Инструкции конкретны и детализированы.
- Минусы
    - Не хватает примеров для более сложных случаев, особенно в разделе "Примеры кода".
    - Нет явного указания на необходимость проверки наличия зависимостей при использовании reStructuredText.
    - Нет примеров для обработки ошибок в reStructuredText документации.

**Рекомендации по улучшению**

1.  **Расширить примеры кода**: Добавить больше примеров кода, демонстрирующих различные сценарии использования reStructuredText и комментирования, включая примеры для функций с параметрами и возвращаемыми значениями.
2.  **Добавить проверку зависимостей**: Указать необходимость установки необходимых пакетов для обработки reStructuredText (например, Sphinx).
3.  **Включить обработку ошибок**: Включить примеры обработки ошибок в reStructuredText, чтобы пользователь знал, как документировать исключения и другие проблемные ситуации.
4.  **Добавить примеры для переменных**: Включить примеры документирования переменных в reStructuredText.
5.  **Уточнить использование `...`**: Добавить комментарий, что `...` не нужно изменять, так как это место для будущей реализации.
6.  **Более конкретные инструкции**:  Уточнить, что подразумевается под соответствием именования функций и переменных с ранее обработанными файлами, возможно, сослаться на определенный стандарт именования.
7.  **Объяснение использования `j_loads` и `j_loads_ns`**: Добавить более детальное объяснение, для чего нужны функции `j_loads` и `j_loads_ns`, а также указать что они из `src.utils.jjson`.
8.  **Примеры для классов**: Добавить примеры документации для классов в RST.

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

      Пример формата документации для классов:

     ```python
     class ExampleClass:
         """
         Пример класса для демонстрации документации.

         :ivar attribute1: Описание атрибута 1.
         :vartype attribute1: str
         :ivar attribute2: Описание атрибута 2.
         :vartype attribute2: int
         """
         def __init__(self, attribute1: str, attribute2: int):
             """
             Инициализация класса ExampleClass.

             :param attribute1: Значение атрибута 1.
             :param attribute2: Значение атрибута 2.
             """
             self.attribute1 = attribute1
             self.attribute2 = attribute2

         def example_method(self, param1: str) -> str:
            """
            Пример метода класса.

            :param param1: Описание параметра метода.
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

## Ответ не должен начинаться с ` ``` `. Используйте их только для оборачивания блоков кода.

## Ты даешь ответы на русском языке
## Формат ответа `.md` (markdown)
----------------------------
** КОНЕЦ ИНСТРУКЦИИ **
```