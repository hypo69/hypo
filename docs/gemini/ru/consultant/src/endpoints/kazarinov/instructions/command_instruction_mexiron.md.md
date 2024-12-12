# Анализ кода модуля `command_instruction_mexiron.md`

**Качество кода**
8
- Плюсы
    -  Документ содержит четкие инструкции по обработке данных, форматированию, и ожидаемой структуре вывода.
    -  Представлен шаблон ответа в формате JSON, что облегчает понимание требуемой структуры данных.
    -  Указаны конкретные требования к обработке полей `product_id`, `image_local_saved_path` - сохранение исходных значений.
- Минусы
    -  Инструкции недостаточно подробны в части обработки ошибок или крайних случаев (например, если спецификации нет, как именно обрабатывать).
    -  Нет примеров обработки вложенных данных, если они возникнут, что может привести к неоднозначности.
    -  Формулировка в описании задания оставляет пространство для интерпретаций, например, "generate by you".
    -  Слишком много повторений "leave as is" в JSON шаблоне, что можно было бы выразить более лаконично.
    -  Отсутствуют явные указания на использование конкретных библиотек для работы с JSON.

**Рекомендации по улучшению**
1. **Уточнение обработки ошибок:** Добавить инструкцию по обработке ситуаций, когда спецификации или описания продукта не могут быть сгенерированы.
2.  **Примеры для вложенных данных:** Привести примеры обработки вложенных структур JSON, если они могут возникнуть в входных данных.
3.  **Уточнение "generate by you":** Дать более точные указания по генерации описаний и спецификаций, возможно, с примерами.
4.  **Рефакторинг шаблона JSON:**  Упростить шаблон, например, указав один раз, что некоторые поля должны сохранять исходное значение.
5.  **Явное указание библиотек:** В явном виде указать, какие библиотеки (например, `j_loads`) следует использовать для работы с JSON.
6. **Добавить `build_types`:** Добавить более ясные инструкции по поводу `build_types`, какие значения и в каком формате ожидать. 
7. **Уточнить синонимию:** Указать, что `product` и `component` синонимы в контексте данной инструкции.
8. **Уточнить контекст:** Уточнить, для каких именно моделей будет использоваться данная инструкция, а также контекст использования.

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
    -   Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов JSON.
    -   Сохраняйте любые `...` в коде без изменений как точки остановки.

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
**Оптимизированный код**
   - Код должен быть обрамлён в соответствующие теги подсветки синтаксиса (например, `python`, `markdown`, `json`).

## Ответ не должен начинаться с ` ``` `. Используйте их только для оборачивания блоков кода.

## Ты даешь ответы на русском языке
## Формат ответа `.md` (markdown)
----------------------------
** КОНЕЦ ИНСТРУКЦИИ **

# command instruction for model:
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
        "product_description": "<description for product in russian generated by you If you don't able to create the specification - leave this field empty>",
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