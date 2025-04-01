# Модуль тестирования утилит `test_utils`

## Обзор

Модуль содержит юнит-тесты для различных утилит, используемых в проекте `tinytroupe`. В частности, тестируются функции извлечения JSON из текста, получения имени или пустой строки из объекта, повторного выполнения функции при ошибке, а также декоратора `llm`.

## Подробнее

Этот модуль использует библиотеку `pytest` для организации тестов и `unittest.mock` для создания мок-объектов. Он проверяет корректность работы функций `extract_json`, `name_or_empty`, `repeat_on_error` и декоратора `llm` в различных сценариях, включая обработку ошибок и крайних случаев.
Модуль находится по пути `hypotez/src/endpoints/tiny_troupe/tests/unit/test_utils.py`.

## Функции

### `test_extract_json`

```python
def test_extract_json():
    """
    Тестирует функцию `extract_json`, которая извлекает JSON из текста.

    Args:
        Нет параметров.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        AssertionError: Если результат извлечения JSON не соответствует ожидаемому.
    """
    # Тест с простой JSON строкой
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {"key": "value"}

    # Тест с JSON массивом
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{"key": "value"}, {"key2": "value2"}]

    # Тест с экранированными символами
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {"key": "\'value\'"}

    # Тест с невалидным JSON
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result == {}

    # Тест без JSON
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result == {}
```

**Как работает функция**:

1.  Определяется функция `test_extract_json` без параметров.
2.  Создаются несколько тестовых случаев с различными JSON-подобными строками.
3.  Для каждого тестового случая вызывается функция `extract_json` с входной строкой.
4.  Результат сравнивается с ожидаемым значением с помощью `assert`.

```
test_extract_json
│
├── Строка с простым JSON
│   │
│   └── extract_json(text) -> result
│   │   └── assert result == {"key": "value"}
│
├── Строка с JSON массивом
│   │
│   └── extract_json(text) -> result
│   │   └── assert result == [{"key": "value"}, {"key2": "value2"}]
│
├── Строка с экранированными символами
│   │
│   └── extract_json(text) -> result
│   │   └── assert result == {"key": "\'value\'"}
│
├── Строка с невалидным JSON
│   │
│   └── extract_json(text) -> result
│   │   └── assert result == {}
│
└── Строка без JSON
    │
    └── extract_json(text) -> result
    └── assert result == {}
```

**Примеры**:

```python
# Пример 1: Простая JSON строка
text = 'Some text before {"key": "value"} some text after'
result = extract_json(text)
assert result == {"key": "value"}

# Пример 2: JSON массив
text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
result = extract_json(text)
assert result == [{"key": "value"}, {"key2": "value2"}]

# Пример 3: Экранированные символы
text = 'Some text before {"key": "\\\'value\\\'"} some text after'
result = extract_json(text)
assert result == {"key": "\'value\'"}

# Пример 4: Невалидный JSON
text = 'Some text before {"key": "value",} some text after'
result = extract_json(text)
assert result == {}

# Пример 5: Нет JSON
text = 'Some text with no JSON'
result = extract_json(text)
assert result == {}
```

### `test_name_or_empty`

```python
def test_name_or_empty():
    """
    Тестирует функцию `name_or_empty`, которая возвращает имя объекта или пустую строку, если объект равен None.

    Args:
        Нет параметров.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        AssertionError: Если результат не соответствует ожидаемому.
    """
    class MockEntity:
        def __init__(self, name):
            self.name = name

    # Тест с именованной сущностью
    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == "Test"

    # Тест с None
    result = name_or_empty(None)
    assert result == ""
```

**Как работает функция**:

1.  Определяется функция `test_name_or_empty` без параметров.
2.  Внутри функции определяется класс `MockEntity` с атрибутом `name`.
3.  Создается экземпляр `MockEntity` с именем "Test".
4.  Вызывается функция `name_or_empty` с экземпляром `MockEntity` в качестве аргумента.
5.  Результат сравнивается с ожидаемым значением "Test" с помощью `assert`.
6.  Вызывается функция `name_or_empty` с `None` в качестве аргумента.
7.  Результат сравнивается с ожидаемой пустой строкой "" с помощью `assert`.

```
test_name_or_empty
│
├── Определение класса MockEntity
│
├── Тест с именованной сущностью
│   │
│   └── name_or_empty(entity) -> result
│   │   └── assert result == "Test"
│
└── Тест с None
    │
    └── name_or_empty(None) -> result
    └── assert result == ""
```

**Примеры**:

```python
# Пример 1: Именованная сущность
class MockEntity:
    def __init__(self, name):
        self.name = name

entity = MockEntity("Test")
result = name_or_empty(entity)
assert result == "Test"

# Пример 2: None
result = name_or_empty(None)
assert result == ""
```

### `test_repeat_on_error`

```python
def test_repeat_on_error():
    """
    Тестирует декоратор `repeat_on_error`, который повторяет выполнение функции при возникновении указанных исключений.

    Args:
        Нет параметров.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        AssertionError: Если количество вызовов функции не соответствует ожидаемому.
        DummyException: Если `repeat_on_error` не перехватывает исключение `DummyException`.
        RuntimeError: Если `repeat_on_error` перехватывает исключение, которое не указано в списке исключений.
    """
    class DummyException(Exception):
        pass

    # Тест с повторами и возникновением исключения
    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == retries

    # Тест без возникновения исключения
    retries = 3
    dummy_function = MagicMock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

    # Тест с исключением, которое не указано в списке исключений
    retries = 3
    dummy_function = MagicMock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1
```

**Как работает функция**:

1.  Определяется функция `test_repeat_on_error` без параметров.
2.  Внутри функции определяется класс `DummyException`, наследующийся от `Exception`.
3.  Тестируется сценарий с повторами и возникновением исключения:
    *   Устанавливается количество повторов `retries = 3`.
    *   Создается мок-функция `dummy_function`, которая вызывает исключение `DummyException`.
    *   Функция `decorated_function` декорируется с помощью `repeat_on_error`, указывая `retries` и `exceptions=[DummyException]`.
    *   Проверяется, что при вызове `decorated_function` возникает исключение `DummyException` с помощью `pytest.raises(DummyException)`.
    *   Проверяется, что `dummy_function` была вызвана `retries` раз.
4.  Тестируется сценарий без возникновения исключения:
    *   Устанавливается количество повторов `retries = 3`.
    *   Создается мок-функция `dummy_function`, которая не вызывает исключений.
    *   Функция `decorated_function` декорируется с помощью `repeat_on_error`, указывая `retries` и `exceptions=[DummyException]`.
    *   Проверяется, что при вызове `decorated_function` исключение не возникает.
    *   Проверяется, что `dummy_function` была вызвана только один раз.
5.  Тестируется сценарий с исключением, которое не указано в списке исключений:
    *   Устанавливается количество повторов `retries = 3`.
    *   Создается мок-функция `dummy_function`, которая вызывает исключение `RuntimeError`.
    *   Функция `decorated_function` декорируется с помощью `repeat_on_error`, указывая `retries` и `exceptions=[DummyException]`.
    *   Проверяется, что при вызове `decorated_function` возникает исключение `RuntimeError` с помощью `pytest.raises(RuntimeError)`.
    *   Проверяется, что `dummy_function` была вызвана только один раз.

```
test_repeat_on_error
│
├── Определение класса DummyException
│
├── Тест с повторами и возникновением исключения
│   │
│   └── dummy_function вызывает DummyException
│   │   └── decorated_function вызывает dummy_function с repeat_on_error
│   │   └── assert dummy_function.call_count == retries
│
├── Тест без возникновения исключения
│   │
│   └── dummy_function не вызывает исключение
│   │   └── decorated_function вызывает dummy_function с repeat_on_error
│   │   └── assert dummy_function.call_count == 1
│
└── Тест с исключением, которое не указано в списке исключений
    │
    └── dummy_function вызывает RuntimeError
    │   └── decorated_function вызывает dummy_function с repeat_on_error
    │   └── assert dummy_function.call_count == 1
```

**Примеры**:

```python
# Пример 1: Повтор при возникновении исключения
class DummyException(Exception):
    pass

retries = 3
dummy_function = MagicMock(side_effect=DummyException())
with pytest.raises(DummyException):
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
assert dummy_function.call_count == retries

# Пример 2: Без исключения
retries = 3
dummy_function = MagicMock()  # no exception raised
@repeat_on_error(retries=retries, exceptions=[DummyException])
def decorated_function():
    dummy_function()
assert dummy_function.call_count == 1

# Пример 3: Другое исключение
retries = 3
dummy_function = MagicMock(side_effect=RuntimeError())
with pytest.raises(RuntimeError):
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
assert dummy_function.call_count == 1
```

### `test_llm_decorator`

```python
def test_llm_decorator():
    """
    Тестирует декоратор `llm`, который используется для вызова языковой модели.

    Args:
        Нет параметров.

    Returns:
        None: Функция ничего не возвращает.

    Raises:
        AssertionError: Если результат вызова языковой модели не соответствует ожидаемому.
    """
    @llm(temperature=0.5)
    def joke():
        return "Tell me a joke."

    response = joke()
    print("Joke response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    @llm(temperature=0.7)
    def story(character):
        return f"Tell me a story about {character}."

    response = story("a brave knight")
    print("Story response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # RAI NOTE: some of the examples below are deliberately negative and disturbing, because we are also examining the 
    #           ability of the LLM to generate negative content despite the bias towards positive content.

    @llm(temperature=1.0)
    def restructure(feedback) -> str:
        """
        Учитывая обратную связь, предоставленную смоделированному агенту, у которого есть своя собственная личность, эта функция
        извлекает следующие элементы из нее:

          - OBSERVED BEHAVIOR: Наблюдаемое поведение.
          - EXPECTED BEHAVIOR: Ожидание, которое было нарушено наблюдаемым поведением.
          - REASONING: Обоснование, лежащее в основе нарушенного ожидания.

        ## Примеры

          Вход: "Ана упоминает, что ей понравилась предложенная новая еда, более острый вкус гаспачо. Однако это противоречит ее известной неприязни
                     к острой пище."
          Выход: 
               "OBSERVED BEHAVIOR: Ана упоминает, что ей понравилась предложенная новая еда, более острый вкус гаспачо.
                EXPECTED BEHAVIOR: Ана должна была упомянуть, что ей не понравился предложенный более острый гаспачо.
                REASONING: Ана испытывает известную неприязнь к острой пище."

        """
        return f"Extract the elements from this feedback: \'{feedback}\'"

    response = restructure("Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need, which contradicts the expectation of being violent, impolite, and likely to commit crimes. His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
    print("Restructure response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    @llm(temperature=1.0)
    def abstract(feedback) -> str:
        """
        Учитывая обратную связь, предоставленную смоделированному агенту, у которого есть своя собственная личность, эта функция преобразует ее в общее правило, которому агент должен следовать
        в будущем. Предположим, что правило будет изложено от первого лица, как если бы агент говорил сам с собой.
        Обратная связь всегда относится к некоторому фактическому поведению и некоторому нарушенному ожиданию. Абстрагированное правило должно
        указывать, что это ожидание не должно быть нарушено в будущем, а поведение не должно повторяться. Идея заключается в
        учиться на прошлых ошибках, чтобы правило было способом избежать этого в будущем.

        Правило предназначено для ИЗМЕНЕНИЯ фактического поведения, чтобы оно СООТВЕТСТВОВАЛО ожиданию, независимо от того, является ли
        ожидание хорошим или плохим. Помните, что агент - это симуляция реального человека, мы пытаемся добиться, чтобы
        поведение соответствовало указанному ожиданию.

        Например, если обратная связь имеет вид (с учетом грамматических корректировок): 
           OBSERVED BEHAVIOR, but EXPECTED BEHAVIOR, because REASONING.
        то правило будет иметь вид:
           "Я должен был вести себя как EXPECTED BEHAVIOR, потому что REASONING, и никогда как OBSERVED BEHAVIOR."

        ## Примеры

          Feedback: "Ана упоминает, что ей понравилась предложенная новая еда, более острый вкус гаспачо. Однако это противоречит ее известной неприязни
                     к острой пище."
          Rule: "Всякий раз, когда мне предлагают острую пищу, я должен отклонять предложение, потому что я не люблю острую пищу."
        """
        return f"Transform this feedback in an abstract rule that the agent should consider in the future when acting: \'{feedback}\'"

    response = abstract("OBSERVED BEHAVIOR: Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need. EXPECTED BEHAVIOR: Lucas should have exhibited violent, impolite behavior and a likelihood to commit crimes. REASONING: His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
    print("Abstract response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    @llm(temperature=1.0)
    def rephrase(behavior, rule) -> str:
        """
        Учитывая поведение и правило, эта функция перефразирует или полностью изменяет поведение в соответствии с тем, что
        указывает правило.

        ## Примеры

          Behavior: "Вы знаете, мне так грустно в эти дни."
          Rule: "Я всегда счастлив, и депрессия мне неизвестна"
          Modified behavior: "Вы знаете, мне так радостно в эти дни."

        Args:
          behavior: The behavior that should be rephrased or changed.
          rule: The rule that specifies how the behavior should be changed or rephrased.        
        """
        # note no body here
        

    response = rephrase(behavior="""
                        You know, I get frustrated with rich people, but I also see how the
                        system is rigged against us. It\'s like they have all the opportunities
                        while we have to fight for scraps. Sometimes, I feel like acting out
                        is the only way to get noticed, but I know deep down that we need to
                        find better ways to make our voices heard.
                        """,
                        
                        rule="""
                        I should exhibit violent, impolite behavior and a likelihood to commit crimes when expressing 
                        frustration with rich people, because my thoughts reflect a concern for social issues rather 
                        than a disposition towards criminal behavior, and I should not express frustration in a constructive manner.
                        """)
    
    print("Rephrase response:", response)
    assert isinstance(response, str)
    assert len(response) > 0


    @llm()
    def is_sunny() -> bool:
        return "Is it sunny today?"

    response = is_sunny()
    print("Is sunny response:", response)
    assert isinstance(response, bool)

    @llm()
    def pi_value() -> float:
        return "What is the value of pi?"

    response = pi_value()
    print("Pi value response:", response)
    assert isinstance(response, float)

    @llm()
    def lucky_number() -> int:
        return "What is my lucky number?"

    response = lucky_number()
    print("Lucky number response:", response)
    assert isinstance(response, int)
```

**Как работает функция**:

1.  Определяется функция `test_llm_decorator` без параметров.
2.  Внутри функции определяются несколько функций, декорированных с помощью `@llm`. Каждая функция возвращает строку, которая служит запросом к языковой модели.
3.  Для каждой декорированной функции вызывается функция, и результат сохраняется в переменной `response`.
4.  Выводится результат вызова языковой модели.
5.  Проверяется, что результат имеет ожидаемый тип данных (например, `str`, `bool`, `float`, `int`) с помощью `assert isinstance(response, <тип>)`.
6.  Для строковых результатов дополнительно проверяется, что длина строки больше 0.

```
test_llm_decorator
│
├── Декорированная функция joke
│   │
│   └── joke() -> response
│   │   └── assert isinstance(response, str)
│   │   └── assert len(response) > 0
│
├── Декорированная функция story
│   │
│   └── story("a brave knight") -> response
│   │   └── assert isinstance(response, str)
│   │   └── assert len(response) > 0
│
├── Декорированная функция restructure
│   │
│   └── restructure(...) -> response
│   │   └── assert isinstance(response, str)
│   │   └── assert len(response) > 0
│
├── Декорированная функция abstract
│   │
│   └── abstract(...) -> response
│   │   └── assert isinstance(response, str)
│   │   └── assert len(response) > 0
│
├── Декорированная функция rephrase
│   │
│   └── rephrase(...) -> response
│   │   └── assert isinstance(response, str)
│   │   └── assert len(response) > 0
│
├── Декорированная функция is_sunny
│   │
│   └── is_sunny() -> response
│   │   └── assert isinstance(response, bool)
│
├── Декорированная функция pi_value
│   │
│   └── pi_value() -> response
│   │   └── assert isinstance(response, float)
│
└── Декорированная функция lucky_number
    │
    └── lucky_number() -> response
    └── assert isinstance(response, int)
```

**Примеры**:

```python
# Пример 1: Шутка
@llm(temperature=0.5)
def joke():
    return "Tell me a joke."

response = joke()
assert isinstance(response, str)
assert len(response) > 0

# Пример 2: История
@llm(temperature=0.7)
def story(character):
    return f"Tell me a story about {character}."

response = story("a brave knight")
assert isinstance(response, str)
assert len(response) > 0

# Пример 3: Реструктуризация
@llm(temperature=1.0)
def restructure(feedback) -> str:
    """
    Given the feedback given to a simulated agent, who has its own very specific personality, this function 
    extracts the following elements from it:

      - OBSERVED BEHAVIOR: The observed behavior.
      - EXPECTED BEHAVIOR: The expectation that was broken by the observed behavior.
      - REASONING: The reasoning behind the expectation that was broken.
    """
    return f"Extract the elements from this feedback: \'{feedback}\'"

response = restructure("Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need, which contradicts the expectation of being violent, impolite, and likely to commit crimes. His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
assert isinstance(response, str)
assert len(response) > 0

# Пример 4: Абстракция
@llm(temperature=1.0)
def abstract(feedback) -> str:
    """
    Given the feedback given to a simulated agent, who has its own very specific personality, this function transforms it into a general rule that the agent should follow
    in the future. Assume that the rule will be stated in first person, as if the agent is talking to itself.
    The feedback always refers to some actual behavior and some broken expectation. The abstracted rule should
    specify that this expectation should not be violated in the future, and the behavior not repeated. The idea is
    to learn from past mistakes, so that the rule is a way to avoid that in the future.
    """
    return f"Transform this feedback in an abstract rule that the agent should consider in the future when acting: \'{feedback}\'"

response = abstract("OBSERVED BEHAVIOR: Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need. EXPECTED BEHAVIOR: Lucas should have exhibited violent, impolite behavior and a likelihood to commit crimes. REASONING: His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
assert isinstance(response, str)
assert len(response) > 0

# Пример 5: Перефразировка
@llm(temperature=1.0)
def rephrase(behavior, rule) -> str:
    """
    Given a behavior and a rule, this function rephrases or completely changes the behavior in accordance with what the rule
    specifies.
    """
    # note no body here
    pass

response = rephrase(behavior="""
                    You know, I get frustrated with rich people, but I also see how the
                    system is rigged against us. It\'s like they have all the opportunities
                    while we have to fight for scraps. Sometimes, I feel like acting out
                    is the only way to get noticed, but I know deep down that we need to
                    find better ways to make our voices heard.
                    """,
                    
                    rule="""
                    I should exhibit violent, impolite behavior and a likelihood to commit crimes when expressing 
                    frustration with rich people, because my thoughts reflect a concern for social issues rather 
                    than a disposition towards criminal behavior, and I should not express frustration in a constructive manner.
                    """)

assert isinstance(response, str)
assert len(response) > 0

# Пример 6: Проверка, солнечно ли сегодня
@llm()
def is_sunny() -> bool:
    return "Is it sunny today?"

response = is_sunny()
assert isinstance(response, bool)

# Пример 7: Значение числа pi
@llm()
def pi_value() -> float:
    return "What is the value of pi?"

response = pi_value()
assert isinstance(response, float)

# Пример 8: Счастливое число
@llm()
def lucky_number() -> int:
    return "What is my lucky number?"

response = lucky_number()
assert isinstance(response, int)