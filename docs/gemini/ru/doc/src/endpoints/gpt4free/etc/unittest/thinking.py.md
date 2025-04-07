# Модуль тестирования ThinkingProcessor

## Обзор

Модуль `thinking.py` содержит тесты для класса `ThinkingProcessor`, который используется для обработки текстовых фрагментов, содержащих специальные теги `<think>` и `</think>`, указывающие на начало и конец процесса "размышления". В тестах проверяется корректность разбиения входных фрагментов на части, определения времени начала и окончания "размышления", а также создания объектов `Reasoning` с соответствующими статусами.

## Подробней

Этот модуль тестирует функциональность обработки текстовых фрагментов, содержащих индикаторы начала и конца процесса "размышления". Он проверяет, что класс `ThinkingProcessor` правильно разбивает текст на части, определяет время начала и окончания "размышления", и создает объекты `Reasoning` с соответствующими статусами. Эти тесты важны для обеспечения надежной работы системы, которая использует эти индикаторы для управления ходом выполнения задач.

## Классы

### `TestThinkingProcessor`

**Описание**: Класс `TestThinkingProcessor` содержит набор тестовых методов для проверки различных сценариев работы `ThinkingProcessor`.

**Принцип работы**:
Класс `TestThinkingProcessor` наследует от `unittest.TestCase` и содержит методы, проверяющие различные аспекты работы `ThinkingProcessor`. Каждый метод тестирует определенный сценарий, например, обработку обычного текста, текста с тегами `<think>` и `</think>`, а также текста в процессе "размышления". Для каждого сценария задаются ожидаемые результаты, которые сравниваются с фактическими результатами работы `ThinkingProcessor`.

**Методы**:

- `test_non_thinking_chunk()`: Тестирует случай, когда входной фрагмент не содержит тегов `<think>` и `</think>`.
- `test_thinking_start()`: Тестирует случай, когда входной фрагмент содержит тег `<think>`.
- `test_thinking_end()`: Тестирует случай, когда входной фрагмент содержит тег `</think>`.
- `test_thinking_start_and_end()`: Тестирует случай, когда входной фрагмент содержит оба тега `<think>` и `</think>`.
- `test_ongoing_thinking()`: Тестирует случай, когда процесс "размышления" продолжается.
- `test_chunk_with_text_after_think()`: Тестирует случай, когда текст содержит теги `<think>`, `</think>` и текст после них.

## Функции

### `test_non_thinking_chunk`

```python
def test_non_thinking_chunk(self):
    """Тестирует случай, когда входной фрагмент не содержит тегов <think> и </think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что при отсутствии тегов `<think>` и `</think>` во входном фрагменте, `ThinkingProcessor` возвращает исходный фрагмент без изменений.

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, который не содержит тегов `<think>` и `</think>`.
2. Определяет ожидаемое время `expected_time` и ожидаемый результат `expected_result`.
3. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk)` для обработки фрагмента.
4. Сравнивает фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями, используя методы `assertEqual`.

```
A: Определение входного фрагмента текста без тегов
│
B: Определение ожидаемого времени и результата
│
C: Вызов ThinkingProcessor.process_thinking_chunk()
│
D: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_non_thinking_chunk(self=TestThinkingProcessor())
```

### `test_thinking_start`

```python
def test_thinking_start(self):
    """Тестирует случай, когда входной фрагмент содержит тег <think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что при наличии тега `<think>` во входном фрагменте, `ThinkingProcessor` корректно разбивает фрагмент на части, создает объект `Reasoning` с соответствующим статусом и возвращает время начала "размышления".

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, который содержит тег `<think>`.
2. Определяет ожидаемое время `expected_time` и ожидаемый результат `expected_result`.
3. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk)` для обработки фрагмента.
4. Сравнивает фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями, используя методы `assertAlmostEqual` и `assertEqual`.

```
A: Определение входного фрагмента текста с тегом <think>
│
B: Определение ожидаемого времени и результата
│
C: Вызов ThinkingProcessor.process_thinking_chunk()
│
D: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_thinking_start(self=TestThinkingProcessor())
```

### `test_thinking_end`

```python
def test_thinking_end(self):
    """Тестирует случай, когда входной фрагмент содержит тег </think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что при наличии тега `</think>` во входном фрагменте, `ThinkingProcessor` корректно разбивает фрагмент на части, создает объект `Reasoning` с соответствующим статусом и возвращает нулевое время.

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, который содержит тег `</think>`.
2. Определяет ожидаемый результат `expected_result`.
3. Получает время начала `start_time`.
4. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk, start_time)` для обработки фрагмента.
5. Сравнивает фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями, используя методы `assertEqual`.

```
A: Определение входного фрагмента текста с тегом </think>
│
B: Определение ожидаемого результата
│
C: Получение времени начала
│
D: Вызов ThinkingProcessor.process_thinking_chunk()
│
E: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_thinking_end(self=TestThinkingProcessor())
```

### `test_thinking_start_and_end`

```python
def test_thinking_start_and_end(self):
    """Тестирует случай, когда входной фрагмент содержит оба тега <think> и </think>.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что при наличии обоих тегов `<think>` и `</think>` во входном фрагменте, `ThinkingProcessor` корректно разбивает фрагмент на части, создает объекты `Reasoning` с соответствующими статусами и возвращает нулевое время.

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, который содержит теги `<think>` и `</think>`.
2. Определяет ожидаемый результат `expected_result`.
3. Получает время начала `start_time`.
4. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk, start_time)` для обработки фрагмента.
5. Сравнивает фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями, используя методы `assertEqual`.

```
A: Определение входного фрагмента текста с тегами <think> и </think>
│
B: Определение ожидаемого результата
│
C: Получение времени начала
│
D: Вызов ThinkingProcessor.process_thinking_chunk()
│
E: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_thinking_start_and_end(self=TestThinkingProcessor())
```

### `test_ongoing_thinking`

```python
def test_ongoing_thinking(self):
    """Тестирует случай, когда процесс "размышления" продолжается.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что при отсутствии тега `</think>` после тега `<think>`, `ThinkingProcessor` возвращает исходный фрагмент с объектом `Reasoning` и сохраняет время начала "размышления".

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, который представляет собой продолжающийся процесс "размышления".
2. Определяет ожидаемый результат `expected_result`.
3. Получает время начала `start_time`.
4. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk, start_time)` для обработки фрагмента.
5. Сравнивает фактическое время `actual_time` и фактический результат `actual_result` с ожидаемыми значениями, используя методы `assertEqual`.

```
A: Определение входного фрагмента текста о продолжающемся процессе "размышления"
│
B: Определение ожидаемого результата
│
C: Получение времени начала
│
D: Вызов ThinkingProcessor.process_thinking_chunk()
│
E: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_ongoing_thinking(self=TestThinkingProcessor())
```

### `test_chunk_with_text_after_think`

```python
def test_chunk_with_text_after_think(self):
    """Тестирует случай, когда текст содержит теги <think>, </think> и текст после них.

    Args:
        self (TestThinkingProcessor): Экземпляр класса TestThinkingProcessor.
    """
```

**Назначение**: Проверяет, что `ThinkingProcessor` правильно обрабатывает фрагмент, содержащий `<think>`, `</think>` и последующий текст.

**Параметры**:
- `self` (TestThinkingProcessor): Экземпляр класса `TestThinkingProcessor`.

**Как работает функция**:

1. Определяет входной фрагмент текста `chunk`, содержащий `<think>`, `</think>` и последующий текст.
2. Определяет ожидаемое время `expected_time` и результат `expected_result`.
3. Вызывает метод `ThinkingProcessor.process_thinking_chunk(chunk)` для обработки фрагмента.
4. Сравнивает фактическое время `actual_time` и результат `actual_result` с ожидаемыми значениями, используя методы `assertEqual`.

```
A: Определение входного фрагмента с тегами <think>, </think> и текстом после них
│
B: Определение ожидаемого времени и результата
│
C: Вызов ThinkingProcessor.process_thinking_chunk()
│
D: Сравнение фактического и ожидаемого времени и результата
```

**Примеры**:
```python
test_chunk_with_text_after_think(self=TestThinkingProcessor())
```