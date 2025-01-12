# tinytroupe.validation

## Обзор

Модуль `tinytroupe.validation` предназначен для валидации экземпляров класса `TinyPerson` с использованием возможностей LLM от OpenAI. Он включает класс `TinyPersonValidator`, который предоставляет метод для проверки соответствия ответов `TinyPerson` заданным ожиданиям.

## Оглавление

- [Классы](#классы)
  - [`TinyPersonValidator`](#TinyPersonValidator)
- [Функции](#функции)

## Классы

### `TinyPersonValidator`

**Описание**: Класс, содержащий метод для валидации экземпляров `TinyPerson`.

**Методы**:
- `validate_person`: Метод для валидации экземпляра `TinyPerson`.

#### `validate_person`

**Описание**: Валидирует экземпляр `TinyPerson` с использованием LLM от OpenAI.

**Параметры**:
- `person` (`TinyPerson`): Экземпляр `TinyPerson`, который нужно проверить.
- `expectations` (`Optional[str]`, optional): Ожидания, используемые в процессе валидации. По умолчанию `None`.
- `include_agent_spec` (`bool`, optional): Флаг, указывающий, включать ли спецификацию агента в запрос. По умолчанию `True`.
- `max_content_length` (`int`, optional): Максимальная длина контента для отображения в процессе проверки. По умолчанию `default_max_content_display_length`.

**Возвращает**:
- `Tuple[Optional[float], Optional[str]]`: Кортеж, содержащий оценку достоверности (от 0.0 до 1.0) и обоснование оценки, если валидация успешна; в противном случае возвращается `None, None`.

**Пример использования**:

```python
from tinytroupe.agent import TinyPerson
from tinytroupe.validation import TinyPersonValidator
    
# создаем экземпляр TinyPerson
person = TinyPerson(name="John Doe", bio="A software engineer with 10 years of experience.")

# валидируем созданный экземпляр
score, justification = TinyPersonValidator.validate_person(person, expectations="should have experience in software engineering.")

if score is not None:
    print(f"Validation score: {score:.2f}")
    print(f"Justification: {justification}")
else:
    print("Validation failed.")
```

## Функции

В данном файле отсутствуют отдельные функции, не входящие в класс `TinyPersonValidator`.