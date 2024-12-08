# Модуль generate_person_factory

## Обзор

Этот модуль предоставляет инструменты для генерации контекстов для создания описаний людей.  Он принимает широкий контекст с параметрами, такими как демографические данные, физические характеристики, поведение, убеждения и т.д., и генерирует множество более конкретных контекстов, которые могут быть использованы для создания более детальных описаний персон.  Каждый контекст представлен строкой, готовой к использованию в качестве входных данных для генерации описания человека.

## Функции

### `generate_person_contexts`

**Описание**: Функция генерирует массив контекстов для создания описаний персон.

**Параметры**:

- `broad_context` (str): Широкий контекст, описывающий общие параметры, которые должны быть учтены при создании персон. Пример: "Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not".

- `number_of_contexts` (int, optional): Количество контекстов для генерации. По умолчанию 3.

**Возвращает**:

- `list[str]`: Массив строк, где каждая строка представляет собой контекст для генерации описания человека.


**Пример использования**:

```python
broad_context = "Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies"
contexts = generate_person_contexts(broad_context, 3)
print(contexts)
```

**Вызывает исключения**:

- `ValueError`: Если `broad_context` пуст или содержит недопустимые данные.
- `TypeError`: Если `number_of_contexts` не является целым числом.


```