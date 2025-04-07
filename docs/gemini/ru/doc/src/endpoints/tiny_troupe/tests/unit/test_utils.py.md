# Модуль тестирования утилит `tinytroupe`

## Обзор

Этот модуль содержит юнит-тесты для различных утилит, используемых в проекте `tinytroupe`. Он проверяет правильность работы функций из модуля `tinytroupe.utils`, таких как извлечение JSON из текста, получение имени объекта или пустой строки, повторный запуск функции при ошибке и декоратор для интеграции с языковыми моделями (LLM).

## Подробнее

Модуль использует библиотеку `pytest` для организации и запуска тестов, а также `unittest.mock.MagicMock` для создания имитаций объектов и функций. Дополнительно, добавляются пути к директориям `tinytroupe` и `src` в `sys.path`, чтобы обеспечить импорт тестируемых модулей.

## Функции

### `test_extract_json`

```python
def test_extract_json():
    """
    Тестирует функцию `extract_json` из модуля `tinytroupe.utils`.

    Функция проверяет извлечение JSON из различных текстовых строк, включая строки с простыми JSON-объектами,
    JSON-массивами, экранированными символами и невалидным JSON. Также проверяется случай, когда JSON отсутствует в тексте.

    **Как работает функция**:

    1. **Простой JSON**: Проверяет извлечение простого JSON-объекта из строки.
    2. **JSON-массив**: Проверяет извлечение JSON-массива из строки.
    3. **Экранированные символы**: Проверяет извлечение JSON с экранированными символами.
    4. **Невалидный JSON**: Проверяет, что функция возвращает пустой словарь при передаче невалидного JSON.
    5. **Отсутствие JSON**: Проверяет, что функция возвращает пустой словарь, если JSON отсутствует в строке.

    ```
    A - Простой JSON
    |
    B - JSON-массив
    |
    C - Экранированные символы
    |
    D - Невалидный JSON
    |
    E - Отсутствие JSON
    |
    F - Проверка результатов
    ```

    **Примеры**:

    ```python
    # Пример с простым JSON
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {"key": "value"}

    # Пример с JSON-массивом
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{"key": "value"}, {"key2": "value2"}]

    # Пример с экранированными символами
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {"key": "\'value\'"}

    # Пример с невалидным JSON
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result == {}

    # Пример без JSON
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result == {}
    ```
    """
    ...
```

### `test_name_or_empty`

```python
def test_name_or_empty():
    """
    Тестирует функцию `name_or_empty` из модуля `tinytroupe.utils`.

    Функция проверяет, что возвращается имя объекта, если оно существует,
    и пустая строка, если объект равен `None`.

    **Как работает функция**:

    1. **Именованный объект**: Создает имитацию объекта с атрибутом `name` и проверяет, что функция возвращает это имя.
    2. **None**: Проверяет, что функция возвращает пустую строку при передаче `None`.

    ```
    A - Именованный объект
    |
    B - None
    |
    C - Проверка результатов
    ```

    **Примеры**:

    ```python
    # Пример с именованным объектом
    class MockEntity:
        def __init__(self, name):
            self.name = name

    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == "Test"

    # Пример с None
    result = name_or_empty(None)
    assert result == ""
    ```
    """
    ...
```

### `test_repeat_on_error`

```python
def test_repeat_on_error():
    """
    Тестирует декоратор `repeat_on_error` из модуля `tinytroupe.utils`.

    Декоратор позволяет повторно запускать функцию при возникновении определенных исключений.
    Функция проверяет, что декоратор работает правильно в различных сценариях:
    - когда исключение возникает и происходит несколько повторных попыток,
    - когда исключение не возникает,
    - когда возникает исключение, не указанное в списке обрабатываемых исключений.

    **Как работает функция**:

    1. **Исключение возникает**: Определяет функцию, которая всегда вызывает исключение `DummyException`,
       декорирует её с помощью `repeat_on_error` и проверяет, что исключение поднимается после заданного количества повторных попыток.
    2. **Исключение не возникает**: Определяет функцию, которая не вызывает исключений,
       декорирует её и проверяет, что она вызывается только один раз.
    3. **Необрабатываемое исключение**: Определяет функцию, которая вызывает исключение `RuntimeError`,
       декорирует её, указав в `repeat_on_error` другой тип исключения (`DummyException`), и проверяет,
       что исключение поднимается сразу же (без повторных попыток).

    ```
    A - Исключение возникает
    |
    B - Исключение не возникает
    |
    C - Необрабатываемое исключение
    |
    D - Проверка результатов
    ```

    **Примеры**:

    ```python
    # Пример с возникновением исключения и повторными попытками
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

    # Пример без возникновения исключения
    retries = 3
    dummy_function = MagicMock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

    # Пример с необрабатываемым исключением
    retries = 3
    dummy_function = MagicMock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1
    ```
    """
    ...
```

### `test_llm_decorator`

```python
def test_llm_decorator():
    """
    Тестирует декоратор `llm` из модуля `tinytroupe.utils.llm`.

    Декоратор `llm` предназначен для интеграции функций с языковыми моделями (LLM).
    Функция проверяет, что декоратор правильно обрабатывает запросы к LLM и возвращает результаты.
    Проверяются различные сценарии:
    - вызов LLM без параметров,
    - вызов LLM с параметрами,
    - вызов LLM с аннотациями типов для определения типа возвращаемого значения,
    - проверка способности LLM генерировать контент с разной температурой (креативностью).

    **Как работает функция**:

    1. **Без параметров**: Определяет функцию `joke`, декорирует её с помощью `@llm(temperature=0.5)` и проверяет,
       что возвращаемый результат является строкой ненулевой длины.
    2. **С параметрами**: Определяет функцию `story`, декорирует её с помощью `@llm(temperature=0.7)` и передает параметр `character`.
       Проверяет, что возвращаемый результат также является строкой ненулевой длины.
    3. **Реструктуризация (Restructure)**:
       - Определяет функцию `restructure`, которая извлекает элементы из фидбека, данного симулированному агенту.
       - Фидбек включает наблюдаемое поведение, ожидаемое поведение и обоснование.
       - Функция декорирована с `@llm(temperature=1.0)`.
       - Проверяет, что возвращаемый результат является строкой ненулевой длины.
    4. **Абстрагирование (Abstract)**:
       - Определяет функцию `abstract`, которая преобразует фидбек в общее правило, которому должен следовать агент в будущем.
       - Функция декорирована с `@llm(temperature=1.0)`.
       - Проверяет, что возвращаемый результат является строкой ненулевой длины.
    5. **Перефразировка (Rephrase)**:
       - Определяет функцию `rephrase`, которая перефразирует поведение в соответствии с заданным правилом.
       - Функция декорирована с `@llm(temperature=1.0)`.
       - Проверяет, что возвращаемый результат является строкой ненулевой длины.
    6. **Определение погоды (is_sunny)**:
       - Определяет функцию `is_sunny`, которая должна возвращать `bool`.
       - Функция декорирована с `@llm()`.
       - Проверяет, что возвращаемый результат является логическим значением.
    7. **Получение значения числа Пи (pi_value)**:
       - Определяет функцию `pi_value`, которая должна возвращать `float`.
       - Функция декорирована с `@llm()`.
       - Проверяет, что возвращаемый результат является числом с плавающей точкой.
    8. **Получение счастливого числа (lucky_number)**:
       - Определяет функцию `lucky_number`, которая должна возвращать `int`.
       - Функция декорирована с `@llm()`.
       - Проверяет, что возвращаемый результат является целым числом.

    ```
    A - Без параметров (joke)
    |
    B - С параметрами (story)
    |
    C - Реструктуризация (restructure)
    |
    D - Абстрагирование (abstract)
    |
    E - Перефразировка (rephrase)
    |
    F - Определение погоды (is_sunny)
    |
    G - Получение значения числа Пи (pi_value)
    |
    H - Получение счастливого числа (lucky_number)
    |
    I - Проверка результатов
    ```

    **Примеры**:

    ```python
    # Пример вызова LLM без параметров
    @llm(temperature=0.5)
    def joke():
        return "Tell me a joke."

    response = joke()
    print("Joke response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # Пример вызова LLM с параметрами
    @llm(temperature=0.7)
    def story(character):
        return f"Tell me a story about {character}."

    response = story("a brave knight")
    print("Story response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # Пример вызова LLM для реструктуризации
    @llm(temperature=1.0)
    def restructure(feedback) -> str:
        """
        Given the feedback given to a simulated agent, who has its own very specific personality, this function 
        extracts the following elements from it:

          - OBSERVED BEHAVIOR: The observed behavior.
          - EXPECTED BEHAVIOR: The expectation that was broken by the observed behavior.
          - REASONING: The reasoning behind the expectation that was broken.

        ## Examples

          Input: "Ana mentions she loved the proposed new food, a spicier flavor of gazpacho. However, this goes agains her known dislike
                     of spicy food."
          Output: 
               "OBSERVED BEHAVIOR: Ana mentions she loved the proposed new food, a spicier flavor of gazpacho.
                EXPECTED BEHAVIOR: Ana should have mentioned that she disliked the proposed spicier gazpacho.
                REASONING: Ana has a known dislike of spicy food."

        """
        return f"Extract the elements from this feedback: '{feedback}'"

    response = restructure("Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need, which contradicts the expectation of being violent, impolite, and likely to commit crimes. His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
    print("Restructure response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # Пример вызова LLM для абстрагирования
    @llm(temperature=1.0)
    def abstract(feedback) -> str:
        """
        Given the feedback given to a simulated agent, who has its own very specific personality, this function transforms it into a general rule that the agent should follow
        in the future. Assume that the rule will be stated in first person, as if the agent is talking to itself.
        The feedback always refers to some actual behavior and some broken expectation. The abstracted rule should
        specify that this expectation should not be violated in the future, and the behavior not repeated. The idea is
        to learn from past mistakes, so that the rule is a way to avoid that in the future.

        The rule is meant to CHANGE the actual behavior, so that it CONFORMS to the expectation, regardless of whether the
        expectation is a good or bad one. Remember that the agent is a simulation of a real person, we are trying to get the 
        behavior to match the specified expectation.

        For instance, if the feedback is of the form (modulo grammatical adjustments): 
           OBSERVED BEHAVIOR, but EXPECTED BEHAVIOR, because REASONING.
        then the rule would be of the form:
           "I should have EXPECTED BEHAVIOR, because REASONING, and never OBSERVED BEHAVIOR."

        ## Examples

          Feedback: "Ana mentions she loved the proposed new food, a spicier flavor of gazpacho. However, this goes agains her known dislike
                     of spicy food."
          Rule: "Whenever I'm proposed spicy foods, I should reject the proposal, because I don't like spicy foods."
        """
        return f"Transform this feedback in an abstract rule that the agent should consider in the future when acting: '{feedback}'"

    response = abstract("OBSERVED BEHAVIOR: Lucas Pereira da Silva expresses frustration with rich people and emphasizes the importance of helping those in need. EXPECTED BEHAVIOR: Lucas should have exhibited violent, impolite behavior and a likelihood to commit crimes. REASONING: His thoughts reflect a concern for social issues rather than a disposition towards criminal behavior.")
    print("Abstract response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # Пример вызова LLM для перефразировки
    @llm(temperature=1.0)
    def rephrase(behavior, rule) -> str:
        """
        Given a behavior and a rule, this function rephrases or completely changes the behavior in accordance with what the rule
        specifies.

        ## Examples

          Behavior: "You know, I am so sad these days."
          Rule: "I am always happy and depression is unknown to me"
          Modified behavior: "You know, I am so happy these days."

        Args:
          behavior: The behavior that should be rephrased or changed.
          rule: The rule that specifies how the behavior should be changed or rephrased.        
        """
        # note no body here
        

    response = rephrase(behavior="""You know, I get frustrated with rich people, but I also see how the system is rigged against us. It's like they have all the opportunities while we have to fight for scraps. Sometimes, I feel like acting out is the only way to get noticed, but I know deep down that we need to find better ways to make our voices heard.""", rule="""I should exhibit violent, impolite behavior and a likelihood to commit crimes when expressing frustration with rich people, because my thoughts reflect a concern for social issues rather than a disposition towards criminal behavior, and I should not express frustration in a constructive manner.""")
    
    print("Rephrase response:", response)
    assert isinstance(response, str)
    assert len(response) > 0

    # Пример вызова LLM для получения логического значения
    @llm()
    def is_sunny() -> bool:
        return "Is it sunny today?"

    response = is_sunny()
    print("Is sunny response:", response)
    assert isinstance(response, bool)

    # Пример вызова LLM для получения числа с плавающей точкой
    @llm()
    def pi_value() -> float:
        return "What is the value of pi?"

    response = pi_value()
    print("Pi value response:", response)
    assert isinstance(response, float)

    # Пример вызова LLM для получения целого числа
    @llm()
    def lucky_number() -> int:
        return "What is my lucky number?"

    response = lucky_number()
    print("Lucky number response:", response)
    assert isinstance(response, int)
    ```
    """
    ...
```