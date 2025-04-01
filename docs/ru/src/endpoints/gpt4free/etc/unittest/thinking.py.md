# Модуль тестирования ThinkingProcessor

## Обзор

Модуль содержит юнит-тесты для класса `ThinkingProcessor`, который используется для обработки текста, содержащего теги `<think>` и `</think>`, обозначающие начало и конец процесса размышления.

## Подробней

Этот модуль тестирует различные сценарии использования класса `ThinkingProcessor`, включая обработку обычного текста, текста с началом и концом тегов размышления, а также текста в процессе размышления. Тесты проверяют правильность разделения текста на части, определения статуса размышления и возврата ожидаемых результатов.

## Классы

### `TestThinkingProcessor`

**Описание**: Класс, содержащий юнит-тесты для проверки функциональности класса `ThinkingProcessor`.

**Принцип работы**:

1.  Каждый метод класса представляет собой отдельный юнит-тест.
2.  Методы используют `self.assertEqual` и `self.assertAlmostEqual` для сравнения ожидаемых и фактических результатов.
3.  Тесты охватывают различные сценарии, такие как отсутствие тегов `<think>`, наличие начального и конечного тега, а также обработку текста в процессе размышления.

**Методы**:

*   `test_non_thinking_chunk()`: Проверяет обработку текста, не содержащего теги `<think>`.
*   `test_thinking_start()`: Проверяет обработку текста, содержащего начальный тег `<think>`.
*   `test_thinking_end()`: Проверяет обработку текста, содержащего конечный тег `</think>`.
*   `test_thinking_start_and_end()`: Проверяет обработку текста, содержащего начальный и конечный теги `<think>`.
*   `test_ongoing_thinking()`: Проверяет обработку текста в процессе размышления (между тегами `<think>` и `</think>`).
*   `test_chunk_with_text_after_think()`: Проверяет обработку текста с тегами `<think>` и текстом после них.

## Функции

### `test_non_thinking_chunk`

```python
def test_non_thinking_chunk(self):
    """Проверяет обработку текста, не содержащего теги <think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст без тегов `<think>` обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет входной текст `chunk`, не содержащий теги `<think>`.
2.  Определяет ожидаемое время `expected_time` (0) и ожидаемый результат `expected_result` (список, содержащий исходный текст).
3.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом.
4.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение входного текста]
│
B [Определение ожидаемых результатов]
│
C [Вызов ThinkingProcessor.process_thinking_chunk]
│
D [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
from g4f.tools.run_tools import ThinkingProcessor

class TestThinkingProcessor(unittest.TestCase):
    def test_non_thinking_chunk(self):
        chunk = "This is a regular text."
        expected_time, expected_result = 0, [chunk]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)
```

### `test_thinking_start`

```python
def test_thinking_start(self):
    """Проверяет обработку текста, содержащего начальный тег <think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст с начальным тегом `<think>` обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет входной текст `chunk`, содержащий начальный тег `<think>`.
2.  Определяет ожидаемое время `expected_time` (текущее время) и ожидаемый результат `expected_result` (список с текстом до тега, объектом `Reasoning` и текстом после тега).
3.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом.
4.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertAlmostEqual` и `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение входного текста]
│
B [Определение ожидаемых результатов]
│
C [Вызов ThinkingProcessor.process_thinking_chunk]
│
D [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
import time
from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_start(self):
        chunk = "Hello <think>World"
        expected_time = time.time()
        expected_result = ["Hello ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("World")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertAlmostEqual(actual_time, expected_time, delta=1)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

### `test_thinking_end`

```python
def test_thinking_end(self):
    """Проверяет обработку текста, содержащего конечный тег </think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
        start_time (float): Время начала процесса размышления.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст с конечным тегом `</think>` обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.
*   `start_time` (float): Время начала процесса размышления.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет время начала `start_time`.
2.  Определяет входной текст `chunk`, содержащий конечный тег `</think>`.
3.  Определяет ожидаемый результат `expected_result` (список с объектом `Reasoning`, объектом `Reasoning` и текстом после тега).
4.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом и временем начала.
5.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение времени начала]
│
B [Определение входного текста]
│
C [Определение ожидаемых результатов]
│
D [Вызов ThinkingProcessor.process_thinking_chunk]
│
E [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
import time
from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_end(self):
        start_time = time.time()
        chunk = "token</think> content after"
        expected_result = [Reasoning("token"), Reasoning(status="Finished", is_thinking="</think>"), " content after"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, 0)
        self.assertEqual(actual_result[0], expected_result[0])
        self.assertEqual(actual_result[1], expected_result[1])
        self.assertEqual(actual_result[2], expected_result[2])
```

### `test_thinking_start_and_end`

```python
def test_thinking_start_and_end(self):
    """Проверяет обработку текста, содержащего начальный и конечный теги <think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
        start_time (float): Время начала процесса размышления.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст с начальным и конечным тегами `<think>` обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.
*   `start_time` (float): Время начала процесса размышления.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет время начала `start_time`.
2.  Определяет входной текст `chunk`, содержащий начальный и конечный теги `<think>`.
3.  Определяет ожидаемый результат `expected_result` (список с объектом `Reasoning`, объектом `Reasoning`, объектом `Reasoning` и текстом после тега).
4.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом и временем начала.
5.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение времени начала]
│
B [Определение входного текста]
│
C [Определение ожидаемых результатов]
│
D [Вызов ThinkingProcessor.process_thinking_chunk]
│
E [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
import time
from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_thinking_start_and_end(self):
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

### `test_ongoing_thinking`

```python
def test_ongoing_thinking(self):
    """Проверяет обработку текста в процессе размышления (между тегами <think> и </think>).

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
        start_time (float): Время начала процесса размышления.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст в процессе размышления (между тегами `<think>` и `</think>`) обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.
*   `start_time` (float): Время начала процесса размышления.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет время начала `start_time`.
2.  Определяет входной текст `chunk`, представляющий собой текст в процессе размышления.
3.  Определяет ожидаемый результат `expected_result` (список с объектом `Reasoning`).
4.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом и временем начала.
5.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение времени начала]
│
B [Определение входного текста]
│
C [Определение ожидаемых результатов]
│
D [Вызов ThinkingProcessor.process_thinking_chunk]
│
E [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
import time
from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_ongoing_thinking(self):
        start_time = time.time()
        chunk = "Still thinking..."
        expected_result = [Reasoning("Still thinking...")]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk, start_time)
        self.assertEqual(actual_time, start_time)
        self.assertEqual(actual_result, expected_result)
```

### `test_chunk_with_text_after_think`

```python
def test_chunk_with_text_after_think(self):
    """Проверяет обработку текста с тегами <think> и текстом после них.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.

    Returns:
        None

    Raises:
        AssertionError: Если фактический результат не соответствует ожидаемому.
    """
```

**Назначение**: Проверяет, что текст с тегами `<think>` и текстом после них обрабатывается правильно.

**Параметры**:

*   `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Возвращает**:

*   `None`

**Вызывает исключения**:

*   `AssertionError`: Если фактический результат не соответствует ожидаемому.

**Как работает функция**:

1.  Определяет входной текст `chunk`, содержащий начальный и конечный теги `<think>` и текст после них.
2.  Определяет ожидаемое время `expected_time` (0) и ожидаемый результат `expected_result` (список с текстом до тега, объектами `Reasoning` и текстом после тега).
3.  Вызывает метод `ThinkingProcessor.process_thinking_chunk` с входным текстом.
4.  Сравнивает фактическое время и результат с ожидаемыми значениями с помощью `self.assertEqual`.

**ASCII flowchart**:

```
A [Определение входного текста]
│
B [Определение ожидаемых результатов]
│
C [Вызов ThinkingProcessor.process_thinking_chunk]
│
D [Сравнение фактических и ожидаемых результатов]
```

**Примеры**:

```python
import unittest
import time
from g4f.tools.run_tools import ThinkingProcessor, Reasoning

class TestThinkingProcessor(unittest.TestCase):
    def test_chunk_with_text_after_think(self):
        chunk = "Start <think>Middle</think>End"
        expected_time = 0
        expected_result = ["Start ", Reasoning(status="🤔 Is thinking...", is_thinking="<think>"), Reasoning("Middle"), Reasoning(status="Finished", is_thinking="</think>"), "End"]
        actual_time, actual_result = ThinkingProcessor.process_thinking_chunk(chunk)
        self.assertEqual(actual_time, expected_time)
        self.assertEqual(actual_result, expected_result)