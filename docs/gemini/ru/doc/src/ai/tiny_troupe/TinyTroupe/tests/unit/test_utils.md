# Модуль `test_utils`

## Обзор

Данный модуль содержит тесты для функций из модуля `tinytroupe.utils`, проверяя их корректность и поведение в различных сценариях.

## Функции

### `test_extract_json`

**Описание**: Тестирует функцию `extract_json` на извлечение JSON из строк с различными форматами.

**Тестируемые сценарии**:
- Извлечение JSON из строки, содержащей JSON-объект.
- Извлечение JSON из строки, содержащей JSON-массив.
- Обработка экранированных символов в JSON.
- Обработка некорректного JSON.
- Обработка отсутствия JSON в строке.

**Примеры**:

```python
text = 'Some text before {"key": "value"} some text after'
result = extract_json(text)
assert result == {"key": "value"}
```

```python
text = 'Some text with no JSON'
result = extract_json(text)
assert result == {}
```


### `test_name_or_empty`

**Описание**: Тестирует функцию `name_or_empty`, проверяющую наличие имени у объекта.

**Тестируемые сценарии**:
- Проверка работы с объектом, имеющим атрибут `name`.
- Проверка работы с `None`.

**Примеры**:

```python
entity = MockEntity("Test")
result = name_or_empty(entity)
assert result == "Test"
```

```python
result = name_or_empty(None)
assert result == ""
```

### `test_repeat_on_error`

**Описание**: Тестирует декоратор `repeat_on_error` для повторного выполнения функции при ошибках.

**Тестируемые сценарии**:
- Проверка повторного выполнения функции при возникновении указанного исключения.
- Проверка корректной работы функции, если исключение не возникает.
- Проверка, что функция не повторяется, если возникает исключение не из списка `exceptions`.

**Примеры**:

```python
retries = 3
dummy_function = MagicMock(side_effect=DummyException())
with pytest.raises(DummyException):
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
assert dummy_function.call_count == retries
```

```python
retries = 3
dummy_function = MagicMock()
@repeat_on_error(retries=retries, exceptions=[DummyException])
def decorated_function():
    dummy_function()
decorated_function()
assert dummy_function.call_count == 1
```


## Зависимости

- `pytest`
- `unittest.mock`
- `tinytroupe.utils`
- `testing_utils` (локальный модуль)


## TODO

- Добавить тесты для функции `json_serializer` (отмечено в коде).