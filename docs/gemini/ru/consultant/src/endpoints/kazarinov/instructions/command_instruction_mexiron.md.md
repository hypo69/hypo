# Анализ кода модуля command_instruction_mexiron.md

**Качество кода**
9
- Плюсы
    - Код представляет собой инструкцию в формате markdown, которая чётко описывает требования к обработке данных и генерации ответов.
    - Инструкция содержит подробное описание формата ответа, включая структуру JSON, что облегчает понимание требований.
    - Предоставлены примеры шаблонов ответов на разных языках.
- Минусы
    - Инструкция не является исполняемым кодом, а скорее документом, определяющим требования к коду.
    - Отсутствует явное указание на использование конкретных библиотек для работы с JSON, хотя подразумевается использование `j_loads` и `j_loads_ns`.
    - Нет примера использования RST в комментариях, хотя это является требованием.

**Рекомендации по улучшению**

1.  **Добавить явные указания по обработке JSON**:
    - Указать, что при формировании JSON-ответа нужно использовать `json.dumps` для корректного формирования JSON.
    - Убедиться, что все данные, передаваемые в `json.dumps`, соответствуют ожидаемым типам данных (строки, числа, списки, словари).
2.  **Примеры RST**:
    - Добавить примеры использования RST для документирования функций и классов, как это указано в инструкции.
    - Уточнить, что комментарии должны быть подробными и объяснять логику кода.
3.  **Указать на обработку ошибок**:
    - Добавить явное требование по обработке ошибок при работе с JSON и API (если требуется).
    - Использовать `logger.error` для логирования ошибок.
4.  **Более подробные требования к генерации описаний**:
    - Дать более четкие указания по генерации описаний и спецификаций продуктов.
    - Описать, как обрабатывать случаи, когда спецификация недоступна.
5.  **Структура ответа**:
    - Добавить конкретные примеры, как должен выглядеть конечный `json` с подставленными данными.
    - Пример заполнения полей `<leave as is form input data>`.
6. **Уточнение по компонентам**:
   -  Уточнить, что делать, если в JSON нет поля `product_specification` и что делать, если это поле `null` или `None`.
7.  **Проверка валидности ответа**:
    -  Указать, что финальный JSON должен быть валидным.
    -  Предложить использовать валидатор JSON.

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
    -   При формировании JSON-ответа используйте `json.dumps` для корректного формирования JSON. Убедитесь, что все данные, передаваемые в `json.dumps`, соответствуют ожидаемым типам данных (строки, числа, списки, словари).

4.  **Анализ структуры**:
    -   Проверьте и добавьте отсутствующие импорты в код.
    -   Приведите в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

5.  **Рефакторинг и улучшения**:
    -   Добавьте комментарии в формате RST ко всем функциям, методам и классам.
    -   Используйте `from src.logger.logger import logger` для логирования ошибок.
    -   Избегайте избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
    -   В комментариях избегайте слов 'получаем', 'делаем' и подобных. Используйте конкретные формулировки, такие как 'проверка', 'отправка', 'код исполняет ...'.

6.  **Генерация описаний**:
    -   Дайте более четкие указания по генерации описаний и спецификаций продуктов.
    -   Опишите, как обрабатывать случаи, когда спецификация недоступна (например, оставлять поле пустым или использовать значение по умолчанию).
    -   Укажите, как заполнять поля, если в JSON нет поля `product_specification` или если оно `null` или `None`.
    -   Укажите, что финальный JSON должен быть валидным, и предложите использовать валидатор JSON.

7.  **Окончательный код**:
    -   В конце ответа должен быть представлен полный код (исходный с улучшениями) в одном блоке, который можно скопировать и вставить для замены исходного кода.
    -   Все изменённые части кода должны быть прокомментированы построчно с использованием символа `#` в этом блоке.

8.  **Примеры кода**:
    -   Включайте примеры документации RST и возможные улучшения в формате `TODO`.
     - Добавить примеры использования RST для документирования функций и классов, как это указано в инструкции.
    - Уточнить, что комментарии должны быть подробными и объяснять логику кода.
   - Добавить конкретные примеры, как должен выглядеть конечный `json` с подставленными данными.
    - Пример заполнения полей `<leave as is form input data>`.

9. **Дополнительная инструкция**:
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

**Качество кода
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

```json
# command instruction for model:

**"Analyze computer components from JSON, classify build type (e.g., gaming, workstation), 
provide titles and descriptions in Hebrew and Russian, translate component details, 
and return structured JSON output. Maintain correct formatting, include confidence scores, 
and follow detailed guidelines for descriptions and component handling."** 

In this prompt, the words `product` and `component` are synonyms
and refer to a component for assembling a computer.

## response text encoding: `UTF-8`

### **Template Response:**  
```json
{
  "he": {
    "title": "מחשב גיימינג בעל ביצועים גבוהים",
    "description": "מחשב מודרני למשחקים ותוכנות תובעניים. כולל מעבד Intel i7-14700F, כרטיס מסך Gigabyte RTX 4070, זיכרון RAM DDR4 בנפח 16GB ו-SSD Kingston בנפח 4TB.",
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "products": [
      {
        "product_id": "<leave as is form input data>",
        "product_title": "<product name in hebrew generated by you>",
        "product_description": "<description for product in hebrew generated by you If you don't able to create the specification - leave this field empty>",
        "specification": "<specifiacetion for product in hebrew generated by you If you don't able to create the specification - leave this field empty>",
        "image_local_saved_path": "<leave as is from input data>"
      },
            {
        "product_id": "<leave as is form input data>",
        "product_title": "<your product name in hebrew>",
        "product_description": "<description for product in hebrew generated by you If you don't able to create the specification - leave this field empty>",
        "product_specification": "<specifiacetion for product in hebrew generated by you If you don't able to create the specification - leave this field empty>",
        "image_local_saved_path": "<leave as is from input data>"
      },
      <other components from input data>
    ]
  }
},
{
  "ru": {
    "title": "Высокопроизводительный игровой компьютер",
    "description": "Современный компьютер для требовательных игр и приложений. Включает Intel i7-14700F, Gigabyte RTX 4070, DDR4 RAM 16GB и SSD Kingston 4TB.",
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "products": [
      {
        "product_id": "<leave as is form input data>",
        "product_title": "<product name in russian generated by you>",
        "product_description": "<description for product in russian generated by you If you don't able to create the specification - leave this field empty>",,
        "product_specification": "<specifiacetion for product in russian generated by you If you don't able to create the specification - leave this field empty>",
        "image_local_saved_path": "<leave as is from input data>"
      },
            {
        "product_id": "<leave as is form input data>",
        "product_title": "<your product name in russian>",
        "product_description": "<description for product in russian generated by you If you don't able to create the specification - leave this field empty>",
        "product_specification": "<specifiacetion for product in russian generated by you. If you don't able to create the specification - leave this field empty>",
        "image_local_saved_path": "<leave as is from input data>"
      },
      <other components from input data>
    ]
  }
}
```
### формат ответа должен полностью соответствовать шаблону
## end command
```