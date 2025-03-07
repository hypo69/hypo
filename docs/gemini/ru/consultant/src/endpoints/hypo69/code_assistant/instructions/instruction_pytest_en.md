# Анализ кода модуля `instruction_pytest_en`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Четкая структура инструкций, разбитая на разделы.
    - Наличие примеров кода для иллюстрации требований.
    - Понятные и конкретные требования к формату кода и документации.
    - Наличие примера RST-документации.
- **Минусы**:
    - Отсутствует явное указание на использование `logger` для обработки ошибок, вместо стандартных `try-except` блоков.
    - Не все требования соответствуют стилю `PEP8`.
    - Текст не полностью соответствует формату `MD`.
    - Нет примера использования `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**:
- Уточнить требование об использовании `logger.error` для обработки исключений, и отказ от `try-except`, где это возможно.
- Добавить пример использования `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Привести форматирование текста в соответствии со стандартом `MD`.
- В примере RST документации использовать корректный формат для `.. code-block:: python`.
- Уточнить, что комментарии должны быть на русском языке (судя по параметру `output_language`):
- Добавить пояснение, что если в коде встречаются `...`, то они должны сохраняться как маркеры.
-  Исправить неверное форматирование в примере функции  `save_text_file`.

**Оптимизированный код**:
```markdown
### **Инструкция: Обработка кода и документации**

---

#### **Основные требования**:

1.  **Формат документации**:
    -   Всегда используйте одинарные кавычки (`'`) в Python-коде. Например:
        ```python
        a = 'A1'
        b = ['a', 'b']
        c = {'key': 'value'}
        ```
    -   Двойные кавычки (`"`) используйте только для операций вывода:
        ```python
        print("Hello, world!")
        input("Введите имя: ")
        from src.logger import logger #  Импортируем logger
        logger.error("Ошибка")
        ```

2.  **Сохранение комментариев**:
    -   Все существующие комментарии после `#` должны оставаться неизменными.
    -   В случае изменений кода, добавляйте построчные комментарии с использованием символа `#`.

3.  **Обработка данных**:
    -   Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
    -   Сохраняйте любые `...` в коде как маркеры без изменений.
    -   Импортируйте `logger` только из `src.logger`:
        ```python
        from src.logger import logger
        ```

4.  **Анализ структуры**:
    -   Проверьте наличие всех необходимых импортов.
    -   Выравнивайте названия функций, переменных и импортов в соответствии с ранее обработанными файлами.

5.  **Рефакторинг и улучшения**:
    -   Добавляйте комментарии в формате **RST** для всех функций, методов и классов.
    -   Используйте `from src.logger.logger import logger` для логирования ошибок.
    -   Избегайте чрезмерного использования стандартных блоков `try-except`, отдавая предпочтение обработке ошибок через `logger.error`.

6.  **Примеры RST-документации**:
    **Пример модуля**:
    ```python
    """
    Модуль для работы с ассистентом программиста
    =================================================

    Модуль содержит класс :class:`CodeAssistant`, который используется для взаимодействия с различными AI-моделями
    (например, Google Gemini и OpenAI) и выполнения задач обработки кода.

    Пример использования
    ----------------------
    .. code-block:: python

        assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
        assistant.process_files()
    """
    ```

    **Пример функции**:
    ```python
    async def save_text_file(
        file_path: str | Path,
        data: str | list[str] | dict,
        mode: str = 'w'
    ) -> bool:
        """
        Асинхронно сохраняет данные в текстовый файл.

        :param file_path: Путь к файлу для сохранения.
        :type file_path: str | Path
        :param data: Данные для записи.
        :type data: str | list[str] | dict
        :param mode: Режим записи ('w' для записи, 'a' для добавления).
        :type mode: str, optional
        :return: True, если файл успешно сохранён, иначе False.
        :rtype: bool
        :raises Exception: В случае ошибки при записи в файл.

        Пример:
            >>> from pathlib import Path
            >>> file_path = Path('example.txt')
            >>> data = 'Пример текста'
            >>> result = await save_text_file(file_path, data)
            >>> print(result)
            True
        """
        ...
    ```

7.  **Финальный код**:
    -   Полный (оригинальный и улучшенный) код должен быть представлен в одном блоке.
    -   Все изменённые участки кода должны быть снабжены построчными комментариями.

8.  **Рекомендации по улучшению**:
    -   Следуйте стандартам PEP8 для форматирования.
    -   Избегайте неясных формулировок в комментариях, таких как "получаем" или "делаем". Вместо этого используйте более точные описания: "проверяем", "отправляем", "выполняем".
    -   Комментарии должны быть написаны на русском языке.
    -   Если в коде встречаются `...`, то они должны сохраняться как маркеры.

---

#### **Структура ответа**:

1.  **Заголовок**:
    -   Анализ кода модуля `<module_name>`

2.  **Качество кода**:
    -   **Соответствие стандартам**: Оценка от 1 до 10
    -   **Плюсы**:
        -   <Положительные стороны кода>
    -   **Минусы**:
        -   <Отрицательные стороны кода>

3.  **Рекомендации по улучшению**:
    -   <Подробные советы и описания необходимых изменений>

4.  **Оптимизированный код**:
    -   Полностью переработанный код, снабжённый комментариями в формате RST.
```