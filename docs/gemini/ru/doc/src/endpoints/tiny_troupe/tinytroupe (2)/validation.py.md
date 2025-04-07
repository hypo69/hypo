# Модуль для валидации личности TinyPerson

## Обзор

Модуль предоставляет класс `TinyPersonValidator`, который используется для валидации экземпляра `TinyPerson` с использованием OpenAI LLM. Он содержит метод `validate_person`, который отправляет серию вопросов экземпляру `TinyPerson` для проверки ответов с помощью OpenAI LLM.

## Подробней

Этот модуль предназначен для проверки того, насколько хорошо персонаж, представленный классом `TinyPerson`, соответствует заданным ожиданиям. Он использует OpenAI LLM для генерации вопросов и анализа ответов персонажа. Валидация происходит путем многократного обмена сообщениями между валидатором и персонажем, пока не будет достигнута уверенность в оценке персонажа.

## Классы

### `TinyPersonValidator`

**Описание**: Класс, предоставляющий статический метод для валидации экземпляра `TinyPerson`.

**Методы**:

- `validate_person`: Статический метод для валидации экземпляра `TinyPerson`.

## Функции

### `validate_person`

```python
@staticmethod
def validate_person(person, expectations=None, include_agent_spec=True, max_content_length=default_max_content_display_length) -> float:
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

**Назначение**: Валидация экземпляра `TinyPerson` с использованием OpenAI LLM.

**Параметры**:
- `person` (TinyPerson): Экземпляр `TinyPerson` для валидации.
- `expectations` (str, optional): Ожидания, используемые в процессе валидации. По умолчанию `None`.
- `include_agent_spec` (bool, optional): Определяет, включать ли спецификацию агента в промпт. По умолчанию `True`.
- `max_content_length` (int, optional): Максимальная длина содержимого, отображаемого при рендеринге разговора.

**Возвращает**:
- `float`: Оценка уверенности процесса валидации (от 0.0 до 1.0), или `None`, если процесс валидации не удался.
- `str`: Обоснование для оценки валидации, или `None`, если процесс валидации не удался.

**Как работает функция**:

1. **Инициализация**:
   - Инициализируется список `current_messages` для хранения сообщений в процессе валидации.
2. **Генерация промпта**:
   - Загружается шаблон промпта из файла `prompts/check_person.mustache`.
   - Рендерится системный промпт с использованием `chevron.render` и передаются ожидания (`expectations`).
   - Формируется пользовательский промпт, включающий характеристики личности (`TinyPerson`) и правила интервью.
     - Если `include_agent_spec` равен `True`, в промпт включается сгенерированная спецификация агента (`person.generate_agent_specification()`).
     - Если `include_agent_spec` равен `False`, в промпт включается мини-биография личности (`person.minibio()`).
3. **Логирование**:
   - Инициализируется логгер `logger` для записи информации о процессе валидации.
   - В лог записывается сообщение о начале валидации личности с указанием имени (`person.name`).
4. **Взаимодействие с LLM**:
   - Системный и пользовательский промпты добавляются в список `current_messages`.
   - Отправляется начальное сообщение в LLM с использованием `openai_utils.client().send_message(current_messages)`.
5. **Цикл валидации**:
   - Запускается цикл `while`, который продолжается, пока LLM возвращает сообщения и пока в сообщении не будет найдена строка завершения (`termination_mark`).
   - Вопросы, полученные от LLM, добавляются в `current_messages`.
   - Вопросы логируются с уровнем `INFO`.
   - Личность (`person`) "слушает" вопросы и "действует" на них, используя метод `person.listen_and_act`.
   - Ответы личности извлекаются и логируются.
   - Ответы личности добавляются в `current_messages`.
   - Отправляется следующее сообщение в LLM.
6. **Извлечение результатов**:
   - После завершения цикла проверяется, что сообщение от LLM не равно `None`.
   - Извлекается JSON-контент из сообщения с использованием `utils.extract_json`.
   - Из JSON-контента извлекаются оценка (`score`) и обоснование (`justification`).
   - Оценка и обоснование логируются.
   - Функция возвращает оценку и обоснование.
7. **Обработка ошибок**:
   - Если в процессе валидации LLM не вернул сообщение (message is None), функция возвращает `None, None`.

**ASCII flowchart**:

```
Начало валидации
    │
    │
    ▼
Генерация промпта
    │
    │
    ▼
Отправка промпта в LLM
    │
    │
    ▼
Цикл: Пока не найдена строка завершения
    │
    ├── Вопросы от LLM
    │   │
    │   ▼
    │   Ответы личности (TinyPerson)
    │   │
    │   ▼
    │   Отправка ответов в LLM
    │
    ▼
Извлечение JSON-контента из сообщения LLM
    │
    │
    ▼
Извлечение оценки и обоснования
    │
    │
    ▼
Возврат оценки и обоснования
```

**Примеры**:

```python
# Пример использования функции validate_person
from tinytroupe.agent import TinyPerson
from tinytroupe.validation import TinyPersonValidator

# Создание экземпляра TinyPerson (пример)
person = TinyPerson(name="Alice", description="A curious and intelligent person.")

# Валидация личности с ожиданиями
score, justification = TinyPersonValidator.validate_person(person, expectations="Should be curious and intelligent.")
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")

# Валидация личности без ожиданий
score, justification = TinyPersonValidator.validate_person(person)
if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")