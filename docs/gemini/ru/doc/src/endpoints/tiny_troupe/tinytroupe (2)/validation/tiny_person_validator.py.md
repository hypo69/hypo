# Модуль для валидации TinyPerson с использованием OpenAI LLM

## Обзор

Модуль `tiny_person_validator.py` содержит класс `TinyPersonValidator`, который используется для валидации экземпляров класса `TinyPerson` с помощью OpenAI LLM. Валидация включает отправку серии вопросов экземпляру `TinyPerson` и оценку его ответов. Модуль определяет логику и структуру для проверки соответствия ответов `TinyPerson` заданным ожиданиям и предоставляет оценку уверенности валидации.

## Подробнее

Модуль предоставляет статический метод `validate_person`, который принимает экземпляр `TinyPerson`, ожидания и флаги для настройки процесса валидации. Он использует OpenAI LLM для генерации вопросов, отправляет их `TinyPerson`, анализирует ответы и возвращает оценку уверенности вместе с обоснованием. Этот модуль играет ключевую роль в обеспечении того, что `TinyPerson` ведет себя в соответствии с заданными критериями и ожиданиями.

## Классы

### `TinyPersonValidator`

**Описание**: Класс, предоставляющий функциональность для валидации экземпляров класса `TinyPerson` с использованием OpenAI LLM.

**Принцип работы**: Класс содержит статический метод `validate_person`, который отправляет серию вопросов экземпляру `TinyPerson`, оценивает его ответы и возвращает оценку уверенности валидации. Он использует шаблоны mustache для генерации подсказок и OpenAI LLM для оценки ответов.

**Методы**:
- `validate_person`: Валидирует экземпляр `TinyPerson` с использованием OpenAI LLM.

## Функции

### `validate_person`

```python
@staticmethod
def validate_person(person, expectations=None, include_agent_spec=True, max_content_length=default_max_content_display_length) -> tuple[float, str]:
    """
    Validate a TinyPerson instance using OpenAI's LLM.

    This method sends a series of questions to the TinyPerson instance to validate its responses using OpenAI's LLM.
    The method returns a float value representing the confidence score of the validation process.
    If the validation process fails, the method returns None.

    Args:
        person (TinyPerson): The TinyPerson instance to be validated.
        expectations (str, optional): The expectations to be used in the validation process. Defaults to None.
        include_agent_spec (bool, optional): Whether to include the agent specification in the prompt. Defaults to False.
        max_content_length (int, optional): The maximum length of the content to be displayed when rendering the conversation.

    Returns:
        float: The confidence score of the validation process (0.0 to 1.0), or None if the validation process fails.
        str: The justification for the validation score, or None if the validation process fails.
    """
```

**Назначение**: Валидирует экземпляр `TinyPerson`, отправляя ему вопросы и оценивая его ответы с помощью OpenAI LLM.

**Параметры**:
- `person` (TinyPerson): Экземпляр `TinyPerson`, который необходимо проверить.
- `expectations` (str, optional): Ожидания, используемые в процессе проверки. По умолчанию `None`.
- `include_agent_spec` (bool, optional): Флаг, определяющий, следует ли включать спецификацию агента в запрос. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина содержимого, отображаемого при рендеринге разговора.

**Возвращает**:
- `tuple[float, str]`: Кортеж, содержащий оценку уверенности валидации (от 0.0 до 1.0) и обоснование оценки. Возвращает `None, None`, если процесс валидации не удался.

**Вызывает исключения**:
- Отсутствуют явные исключения, но могут возникать исключения в процессе взаимодействия с OpenAI LLM или при обработке данных.

**Как работает функция**:

1. **Инициализация**:
   - Инициализирует список `current_messages` для хранения сообщений, которыми обмениваются с LLM.
   - Определяет путь к шаблону запроса `check_person.mustache`.
   - Читает шаблон запроса из файла.

2. **Формирование системного запроса**:
   - Использует библиотеку `chevron` для рендеринга шаблона `check_agent_prompt_template` с учетом заданных `expectations`. Результат сохраняется в `system_prompt`.

3. **Формирование пользовательского запроса**:
   - Формирует текст `user_prompt` с инструкциями для LLM, как проводить интервью с `TinyPerson`.
   - Добавляет либо мини-биографию `TinyPerson`, либо полную спецификацию персоны в формате JSON, в зависимости от значения `include_agent_spec`.

4. **Логирование начала валидации**:
   - Получает экземпляр логгера "tinytroupe".
   - Логирует начало процесса валидации для указанного `person.name`.

5. **Отправка начальных сообщений LLM**:
   - Добавляет `system_prompt` и `user_prompt` в список `current_messages`.
   - Отправляет начальные сообщения в LLM с помощью `openai_utils.client().send_message(current_messages)`.

6. **Цикл взаимодействия с LLM**:
   - Устанавливает `termination_mark` для определения конца разговора (наличие "```json" в ответе).
   - В цикле `while` продолжает взаимодействие с LLM до тех пор, пока не будет достигнут `termination_mark` или не будет получен `None` в качестве сообщения.
     - Добавляет вопросы от LLM в список `current_messages`.
     - Логирует вопросы.
     - Запрашивает у `person` ответы на вопросы, используя метод `person.listen_and_act`.
     - Получает ответы от `person` и логирует их.
     - Добавляет ответы в список `current_messages`.
     - Отправляет обновленный список сообщений в LLM.

7. **Обработка финального сообщения**:
   - После завершения цикла проверяет, что `message` не равно `None`.
   - Извлекает JSON-контент из финального сообщения с помощью `utils.extract_json`.
   - Извлекает оценку (`score`) и обоснование (`justification`) из JSON-контента.
   - Логирует оценку и обоснование.
   - Возвращает `score` и `justification`.

8. **Обработка неуспешной валидации**:
   - Если `message` равно `None`, возвращает `None, None`.

**Внутренние функции**: отсутствуют.

```
A: Инициализация (создание сообщений, чтение шаблона)
|
B: Формирование запроса (системного и пользовательского)
|
C: Отправка начальных сообщений LLM
|
D: Цикл взаимодействия с LLM (пока не termination_mark)
|   |
|   --> E: Добавление вопросов от LLM в список сообщений
|   |
|   --> F: Логирование вопросов
|   |
|   --> G: Получение ответов от person
|   |
|   --> H: Логирование ответов person
|   |
|   --> I: Добавление ответов в список сообщений
|   |
|   --> J: Отправка обновленного списка LLM
|
K: Извлечение score и justification из JSON
|
L: Возврат score и justification
```

**Примеры**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.tinytroupe import config

# Пример создания экземпляра TinyPerson (предполагается, что параметры соответствуют структуре TinyPerson)
persona = {
    "name": "Alice",
    "description": "A friendly chatbot.",
    "age": 25,
    "occupation": "Software Engineer"
}
alice = TinyPerson(persona=persona, actions=["TALK"])

# Пример вызова validate_person с минимальными параметрами
score, justification = TinyPersonValidator.validate_person(alice)
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")

# Пример вызова validate_person с указанием ожиданий
expectations = "The chatbot should respond in a friendly and helpful manner."
score, justification = TinyPersonValidator.validate_person(alice, expectations=expectations)
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")

# Пример вызова validate_person без включения agent_spec
score, justification = TinyPersonValidator.validate_person(alice, include_agent_spec=False)
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")

# Пример вызова validate_person с ограничением длины контента
score, justification = TinyPersonValidator.validate_person(alice, max_content_length=512)
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")