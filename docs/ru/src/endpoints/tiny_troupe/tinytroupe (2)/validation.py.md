# Модуль валидации персонажа TinyTroupe

## Обзор

Модуль `validation.py` предназначен для валидации экземпляров класса `TinyPerson` с использованием языковой модели OpenAI. Он содержит класс `TinyPersonValidator` с методом `validate_person`, который отправляет серию вопросов экземпляру `TinyPerson` для оценки соответствия заданным ожиданиям.

## Подробнее

Этот модуль играет важную роль в обеспечении качества и консистентности поведения персонажей `TinyPerson`. Он использует шаблоны mustache для генерации запросов к OpenAI, а также взаимодействует с экземплярами `TinyPerson` для получения ответов на вопросы. Результатом валидации является оценка уверенности (confidence score) и обоснование этой оценки.

## Классы

### `TinyPersonValidator`

**Описание**: Класс, содержащий статический метод для валидации экземпляров `TinyPerson`.

**Методы**:

- `validate_person(person, expectations=None, include_agent_spec=True, max_content_length=default_max_content_display_length)`: Статический метод для валидации персонажа.

## Функции

### `validate_person`

```python
@staticmethod
def validate_person(person, expectations=None, include_agent_spec=True, max_content_length=default_max_content_display_length) -> float | None:
    """
    Validate a TinyPerson instance using OpenAI's LLM.

    This method sends a series of questions to the TinyPerson instance to validate its responses using OpenAI's LLM.
    The method returns a float value representing the confidence score of the validation process.
    If the validation process fails, the method returns None.

    Args:
        person (TinyPerson): The TinyPerson instance to be validated.
        expectations (str, optional): The expectations to be used in the validation process. Defaults to None.
        include_agent_spec (bool, optional): Whether to include the agent specification in the prompt. Defaults to True.
        max_content_length (int, optional): The maximum length of the content to be displayed when rendering the conversation.

    Returns:
        float: The confidence score of the validation process (0.0 to 1.0), or None if the validation process fails.
        str: The justification for the validation score, or None if the validation process fails.
    """
```

**Назначение**: Валидация экземпляра `TinyPerson` с использованием языковой модели OpenAI.

**Параметры**:

- `person` (TinyPerson): Экземпляр `TinyPerson`, который необходимо проверить.
- `expectations` (Optional[str], optional): Ожидания, используемые в процессе валидации. По умолчанию `None`.
- `include_agent_spec` (bool, optional): Определяет, включать ли спецификацию агента в запрос. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина контента, отображаемого при рендеринге разговора. По умолчанию значение берется из конфигурации `config["OpenAI"].getint("MAX_CONTENT_DISPLAY_LENGTH", 1024)`.

**Возвращает**:

- `float | None`: Оценка уверенности процесса валидации (от 0.0 до 1.0) или `None`, если процесс валидации завершается неудачно.
- `str | None`: Обоснование оценки валидации или `None`, если процесс валидации завершается неудачно.

**Как работает функция**:

1.  **Инициализация**: Инициализирует список `current_messages` для хранения сообщений, отправляемых в LLM.
2.  **Генерация запроса**: Генерирует запрос для проверки персонажа на основе шаблона `check_person.mustache`. Шаблон заполняется ожиданиями (`expectations`).
3.  **Формирование пользовательского запроса**: Формирует пользовательский запрос, включающий характеристики проверяемого персонажа. В зависимости от значения `include_agent_spec`, запрос может содержать полную спецификацию агента или краткую биографию персонажа.
4.  **Отправка запроса в LLM**: Отправляет начальные сообщения (системное и пользовательское) в LLM для получения первого сообщения.
5.  **Взаимодействие с персонажем**:
    *   В цикле, пока не будет найдена строка завершения (`termination_mark`):
        *   Извлекает вопросы из полученного сообщения.
        *   Записывает вопросы в лог.
        *   Запрашивает у персонажа ответы на вопросы, используя метод `person.listen_and_act`.
        *   Извлекает ответы персонажа, используя метод `person.pop_actions_and_get_contents_for`.
        *   Записывает ответы персонажа в лог.
        *   Добавляет вопросы и ответы в `current_messages`.
        *   Отправляет обновленный список сообщений в LLM для получения следующего сообщения.
6.  **Извлечение результата**:
    *   Если получено сообщение с JSON-контентом:
        *   Извлекает JSON-контент из сообщения.
        *   Извлекает оценку (`score`) и обоснование (`justification`) из JSON-контента.
        *   Записывает оценку и обоснование в лог.
        *   Возвращает оценку и обоснование.
    *   Если сообщение не получено или не содержит JSON-контент, возвращает `None, None`.

```
Инициализация --> Генерация запроса --> Формирование пользовательского запроса --> Отправка запроса в LLM
    ↓
Взаимодействие с персонажем:
    ↓
    --> Извлечение вопросов --> Запись вопросов в лог --> Получение ответов от персонажа --> Запись ответов в лог --> Добавление в current_messages --> Отправка запроса в LLM
    ↓
Извлечение результата --> Возврат оценки и обоснования
```

**Примеры**:

```python
# Пример использования validate_person
from tinytroupe.agent import TinyPerson
from tinytroupe.validation import TinyPersonValidator

# Создание экземпляра TinyPerson (предположим, что это уже сделано)
person = TinyPerson(name="ExamplePerson", age=25, occupation="Software Engineer")

# Валидация персонажа с ожиданиями
score, justification = TinyPersonValidator.validate_person(person, expectations="The person should be a software engineer with good communication skills.")

if score is not None:
    print(f"Validation score: {score}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")