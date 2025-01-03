# Анализ кода модуля `system_instruction_hash.md`

**Качество кода**

-  **Соответствие требованиям к формату кода (1-10):** 
    -   **Преимущества:**
        -   Инструкция четкая и лаконичная, хорошо объясняет задачу создания баннера.
        -   Правила оформления баннера хорошо сформулированы.
        -   Приведен пример, облегчающий понимание ожидаемого результата.
    -   **Недостатки:**
        -   Инструкция не содержит reStructuredText, как это требуется в ТЗ.
        -   Отсутствуют описания для переменных, методов и т.д.
        -   Отсутствуют примеры документации в формате RST.

**Рекомендации по улучшению**

1.  **Переформатировать в RST:** Необходимо перевести текст инструкции в формат reStructuredText для соответствия требованиям ТЗ.
2.  **Добавить документацию:** Добавить docstring для переменных и функций.
3.  **Примеры документации:** Добавить примеры документации в формате RST.
4.  **Использовать единый стиль:** Привести текст к единому стилю для более легкого восприятия.

**Улучшенный код**

```markdown
"""
Модуль содержит инструкции для генератора текстовых баннеров.
=========================================================================================

Модуль предоставляет правила и пример для создания текстового баннера из введенного текста с использованием символа '#'.

Пример использования
--------------------

Пример оформления баннера:

.. code-block:: text

   ########
   # Текст #
   ########

"""

# Инструкции
# =========================================================================================
#
# **Основные требования:**
#
# **Язык вывода:** RU (Русский)
#
# 1. **Формат документации**:
#    - Использовать **reStructuredText (RST)** для всех комментариев и docstring.
#    - Всегда использовать одинарные кавычки (`) в коде Python.
#
# 2. **Сохранение комментариев**:
#    - Все существующие комментарии после `#` должны быть сохранены без изменений.
#    - Добавить построчные комментарии к измененным фрагментам кода, используя символ `#`.
#
# 3. **Обработка данных**:
#    - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
#    - Оставить все `...` в коде без изменений как точки остановки.
#
# 4. **Анализ структуры**:
#    - Проверить и добавить отсутствующие импорты в код.
#    - Адаптировать имена функций, переменных и импортов к ранее обработанным файлам.
#
# 5. **Рефакторинг и улучшения**:
#    - Добавить комментарии в формате RST для всех функций, методов и классов.
#    - Использовать `from src.logger.logger import logger` для регистрации ошибок.
#    - Избегать чрезмерного использования стандартных блоков `try-except`, предпочитая обработку ошибок через `logger.error`.
#    - В комментариях избегать слов, таких как "получают", "делают" и тому подобное. Использовать точные формулировки, такие как "проверка", "отправка", "код выполняет ...".
#
# 7. **Итоговый код**:
#    - В конце ответа представить полный код (оригинальный с улучшениями) в едином блоке, который можно скопировать и вставить для замены исходного кода.
#    - Добавить построчные комментарии к измененным частям с помощью символа `#` в этом блоке.
#
# 8. **Примеры кода**:
#    - Включить примеры документации в формате RST и возможные улучшения в формате `TODO`.
#
# 9. **Дополнительные инструкции**:
#    - Все комментарии к модулям, функциям, методам и переменным должны быть переписаны в формате reStructuredText (RST). Это включает:
#      - Описание модуля в начале файла.
#      - Документацию для каждой функции, метода и переменной.
#      - Соответствие стандартам написания docstring в Python (например, для Sphinx).
#      - Комментарии после `#` должны предоставлять подробное объяснение к фрагменту кода, который следует за ними.
#
#      Пример формата документации для модуля:
#
#      ```python
#      """
#      Модуль для работы с помощником программиста
#      =========================================================================================
#
#      Этот модуль содержит класс :class:`CodeAssistant`, который используется для работы с различными моделями искусственного интеллекта,
#      такими как Google Gemini и OpenAI, для выполнения задач обработки кода.
#
#      Пример использования
#      --------------------
#
#      Пример использования класса `CodeAssistant`:
#
#      .. code-block:: python
#
#          assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
#          assistant.process_files()
#      """
#      ```
#
#      Пример формата документации для функций:
#
#      ```python
#      def example_function(param1: str, param2: int) -> str:
#          """
#          Выполняет примерную операцию.
#
#          :param param1: Описание параметра 1.
#          :param param2: Описание параметра 2.
#          :return: Описание возвращаемого значения.
#          """
#          ...
#      ```
#
#      Пример стиля комментариев в коде:
#
#      ```python
#      @close_pop_up()
#      async def specification(self, value: Any = None):
#          """Fetch and set specification.
#
#          Args:
#              value (Any): Это значение может быть передано в словаре kwargs через ключ {specification = `value`} в определении класса.
#              Если `value` передано, его значение будет вставлено в поле `ProductFields.specification`.
#          """
#          try:
#              # Код получает значение через execute_locator
#              value = value or await self.driver.execute_locator(self.locator.specification) or ''
#          except Exception as ex:
#              logger.error('Ошибка при получении значения в поле `specification`', ex)
#              ...
#              return
#
#          # Проверка валидности результата
#          if not value:
#              logger.debug(f'Некорректный результат {value=}\\nМестоположение {self.locator.specification}')
#              ...
#              return
#
#          # Если значение - это список, код преобразует его в строку с разделителем `\\n`
#          if isinstance(value, list):
#              value = '\\n'.join(map(str, value))
#
#          # Код записывает результат в поле `specification` объекта `ProductFields`
#          self.fields.specification = value
#          return True
#      ```
#
# ## Правила
#
# 1. Используй символ '#' для оформления баннера.
# 2. Верхняя и нижняя границы баннера должны быть оформлены символами '#'.
# 3. Текст должен быть окружён рамкой из символов '#'.
# 4. Пример оформления:
#
#    ########
#    # Текст #
#    ########
#
# 5. Не добавляй никаких дополнительных пояснений, просто возвращай оформленный баннер.
```