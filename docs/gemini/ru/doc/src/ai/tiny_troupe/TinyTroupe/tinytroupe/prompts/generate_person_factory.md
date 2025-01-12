# Модуль генерации контекстов персонажей

## Обзор

Этот модуль предназначен для создания множества контекстов, которые будут использоваться в качестве основы для генерации списка персонажей. Идея заключается в том, чтобы получить широкий контекст с некоторыми деталями о персонажах, которых мы хотим сгенерировать, такими как демографические параметры, физические характеристики, поведение, убеждения и т. д., а затем создать множество других, более конкретных контекстов, но производных от более общего.

## Функции

### `generate_person_factory`

**Описание**: Генерирует массив контекстов для генерации персонажей на основе общего контекста.

**Параметры**:
- `context` (str): Широкий контекст, содержащий детали о персонажах, которых нужно сгенерировать.
- `num_persons` (int): Количество контекстов персонажей, которые нужно сгенерировать.

**Возвращает**:
- `list[str]`: Список строк, каждая из которых представляет собой контекст для генерации описания персонажа.

**Пример**:
```python
    generate_person_factory(
        "Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not",
        3
    )
    # Output: ["Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies", "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.", "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."]
```