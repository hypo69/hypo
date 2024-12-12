# Модуль генерации контекстов для описания персонажей

## Обзор

Этот модуль предназначен для создания множества контекстов, которые используются в качестве основы для генерации списка описаний персонажей. Он принимает широкий контекст с общими характеристиками (демографические параметры, физические данные, поведение, убеждения и т. д.) и создает из него множество более конкретных контекстов, которые используются для генерации конкретных персонажей.

## Функции

### `generate_person_contexts`

**Описание**: Функция генерирует список контекстов на основе входного общего контекста.

**Параметры**:
- `input_context` (str): Строка, представляющая общий контекст для генерации персонажей.

**Возвращает**:
- `list[str]`: Список строк, каждая из которых представляет собой контекст для генерации описания персонажа.

**Пример использования:**

```python
input_context = "Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not"
contexts = generate_person_contexts(input_context)
print(contexts)
# Output:
# ["Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies", "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.", "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."]
```