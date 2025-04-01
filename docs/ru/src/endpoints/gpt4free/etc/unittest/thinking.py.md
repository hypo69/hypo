# Модуль тестирования ThinkingProcessor
========================================

Модуль содержит набор тестов для класса `ThinkingProcessor`, предназначенного для обработки фрагментов текста, содержащих маркеры начала и окончания размышлений (`<think>` и `</think>`).
Тесты проверяют корректность обработки различных сценариев, включая обычный текст, начало размышлений, окончание размышлений, а также случаи, когда маркеры размышлений находятся в разных частях текста.

## Оглавление

- [Обзор](#Обзор)
- [Классы](#Классы)
    - [TestThinkingProcessor](#TestThinkingProcessor)
        - [Методы](#Методы)
            - [test_non_thinking_chunk](#test_non_thinking_chunk)
            - [test_thinking_start](#test_thinking_start)
            - [test_thinking_end](#test_thinking_end)
            - [test_thinking_start_and_end](#test_thinking_start_and_end)
            - [test_ongoing_thinking](#test_ongoing_thinking)
            - [test_chunk_with_text_after_think](#test_chunk_with_text_after_think)

## Обзор

Модуль `thinking.py` содержит тесты для проверки функциональности обработки текста, содержащего маркеры начала и конца размышлений.
Он использует библиотеку `unittest` для создания тестовых случаев и проверки корректности работы класса `ThinkingProcessor`.
Этот модуль важен для обеспечения надежной работы системы обработки текста, особенно в случаях, когда необходимо выделять и обрабатывать фрагменты, представляющие собой размышления или мыслительные процессы.

## Классы

### `TestThinkingProcessor`

**Описание**:
Класс `TestThinkingProcessor` наследуется от `unittest.TestCase` и содержит набор тестовых методов для проверки функциональности класса `ThinkingProcessor`.

**Принцип работы**:
Класс `TestThinkingProcessor` использует различные тестовые методы для проверки обработки текста классом `ThinkingProcessor`.
Каждый метод создает определенный сценарий входных данных и проверяет, что результат обработки соответствует ожидаемому.
Тесты охватывают различные случаи, такие как отсутствие маркеров размышлений, начало размышлений, окончание размышлений и комбинации этих случаев.

#### Методы

- `test_non_thinking_chunk`
```python
    def test_non_thinking_chunk(self):
        """
        Тестирует обработку фрагмента текста, не содержащего маркеров размышлений.
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```
    **Назначение**:
    Проверяет, что при обработке фрагмента текста, не содержащего маркеров `<think>` и `</think>`, функция `process_thinking_chunk` возвращает исходный текст без изменений.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, не содержащий маркеров размышлений.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertEqual` для проверки равенства фактических и ожидаемых значений.

    **Примеры**:
    ```python
    chunk = "This is a regular text."
    expected_time, expected_result = 0, [chunk]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
    self.assertEqual(actual_time, expected_time)
    self.assertEqual(actual_result, expected_result)
    ```

- `test_thinking_start`
```python
    def test_thinking_start(self):
        """
        Тестирует обработку фрагмента текста, содержащего маркер начала размышлений (<think>).
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```

    **Назначение**:
    Проверяет, что при обработке фрагмента текста, содержащего маркер начала размышлений `<think>`, функция `process_thinking_chunk` корректно выделяет начало размышлений и добавляет соответствующий объект `Reasoning` в результат.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, содержащий маркер начала размышлений `<think>`.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`, включая объект `Reasoning` с соответствующим статусом.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertAlmostEqual` для проверки приблизительного равенства фактического и ожидаемого времени, а также `self.assertEqual` для проверки равенства элементов результата.

    **Примеры**:
    ```python
    chunk = "Hello <think>World"
    expected_time = time.time()
    expected_result = ["Hello ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("World")]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
    self.assertAlmostEqual(actual_time, expected_time, delta=1)
    self.assertEqual(actual_result[0], expected_result[0])
    self.assertEqual(actual_result[1], expected_result[1])
    self.assertEqual(actual_result[2], expected_result[2])
    ```

- `test_thinking_end`
```python
    def test_thinking_end(self):
        """
        Тестирует обработку фрагмента текста, содержащего маркер окончания размышлений (</think>).
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```
    **Назначение**:
    Проверяет, что при обработке фрагмента текста, содержащего маркер окончания размышлений `</think>`, функция `process_thinking_chunk` корректно выделяет окончание размышлений и добавляет соответствующий объект `Reasoning` в результат.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, содержащий маркер окончания размышлений `</think>`.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`, включая объект `Reasoning` с соответствующим статусом.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом и временем начала размышлений `start_time`.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertEqual` для проверки равенства фактических и ожидаемых значений.

    **Примеры**:
    ```python
    start_time = time.time()
    chunk = "token</think> content after"
    expected_result = [Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
    self.assertEqual(actual_time, 0)
    self.assertEqual(actual_result[0], expected_result[0])
    self.assertEqual(actual_result[1], expected_result[1])
    self.assertEqual(actual_result[2], expected_result[2])
    ```

- `test_thinking_start_and_end`
```python
    def test_thinking_start_and_end(self):
        """
        Тестирует обработку фрагмента текста, содержащего как маркер начала, так и маркер окончания размышлений (<think> и </think>).
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```

    **Назначение**:
    Проверяет, что при обработке фрагмента текста, содержащего как маркер начала `<think>`, так и маркер окончания размышлений `</think>`, функция `process_thinking_chunk` корректно выделяет оба маркера и добавляет соответствующие объекты `Reasoning` в результат.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, содержащий маркеры начала и окончания размышлений `<think>` и `</think>`.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`, включая объекты `Reasoning` с соответствующими статусами.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом и временем начала размышлений `start_time`.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertEqual` для проверки равенства фактических и ожидаемых значений.

    **Примеры**:
    ```python
    start_time = time.time()
    chunk = "<think>token</think> content after"
    expected_result = [Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
    self.assertEqual(actual_time, 0)
    self.assertEqual(actual_result[0], expected_result[0])
    self.assertEqual(actual_result[1], expected_result[1])
    self.assertEqual(actual_result[2], expected_result[2])
    self.assertEqual(actual_result[3], expected_result[3])
    ```

- `test_ongoing_thinking`
```python
    def test_ongoing_thinking(self):
        """
        Тестирует обработку фрагмента текста, представляющего собой продолжение размышлений.
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```

    **Назначение**:
    Проверяет, что при обработке фрагмента текста, представляющего собой продолжение размышлений, функция `process_thinking_chunk` возвращает время начала размышлений без изменений и добавляет объект `Reasoning` с текстом продолжения размышлений в результат.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, представляющий собой продолжение размышлений.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`, включая объект `Reasoning` с текстом продолжения размышлений.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом и временем начала размышлений `start_time`.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertEqual` для проверки равенства фактических и ожидаемых значений.

    **Примеры**:
    ```python
    start_time = time.time()
    chunk = "Still thinking..."
    expected_result = [Reasoning("Still thinking...")]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
    self.assertEqual(actual_time, start_time)
    self.assertEqual(actual_result, expected_result)
    ```

- `test_chunk_with_text_after_think`
```python
    def test_chunk_with_text_after_think(self):
        """
        Тестирует обработку фрагмента текста, содержащего текст до, между и после маркеров размышлений (<think> и </think>).
        
        Args:
            self: Экземпляр класса TestThinkingProcessor.
        """
        ...
```

    **Назначение**:
    Проверяет, что при обработке фрагмента текста, содержащего текст до, между и после маркеров размышлений `<think>` и `</think>`, функция `process_thinking_chunk` корректно выделяет все части текста и добавляет соответствующие объекты `Reasoning` для текста между маркерами.

    **Как работает функция**:
    1. Определяется входной фрагмент текста `chunk`, содержащий текст до, между и после маркеров размышлений `<think>` и `</think>`.
    2. Задаются ожидаемые значения времени `expected_time` и результата `expected_result`, включая объекты `Reasoning` с соответствующими статусами для текста между маркерами.
    3. Вызывается функция `ThinkingProcessor.process_thinking_chunk` с входным фрагментом.
    4. Полученные фактические значения времени `actual_time` и результата `actual_result` сравниваются с ожидаемыми.
    5. Используются методы `self.assertEqual` для проверки равенства фактических и ожидаемых значений.

    **Примеры**:
    ```python
    chunk = "Start <think>Middle</think>End"
    expected_time = 0
    expected_result = ["Start ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("Middle"), Reasoning(status="Finished", is_thinking="</think>"), "End"]
    actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
    self.assertEqual(actual_time, expected_time)
    self.assertEqual(actual_result, expected_result)
    ```