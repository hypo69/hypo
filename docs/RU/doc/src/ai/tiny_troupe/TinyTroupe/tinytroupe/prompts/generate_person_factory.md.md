# Модуль генерации контекстов для создания персонажей

## Обзор

Этот модуль предназначен для создания множества контекстов, которые будут использоваться в качестве основы для генерации списка персонажей. Идея состоит в том, чтобы получить широкий контекст с некоторыми деталями персонажей, которых мы хотим сгенерировать, такими как демографические параметры, физические характеристики, поведение, убеждения и т. д., а затем создать множество других контекстов, более конкретных, но производных от более общего.

## Функции

### `generate_person_factory`

**Описание**: 
Генерирует массив контекстов в формате JSON, каждый из которых представляет собой конкретный контекст для генерации описания персонажа.

**Параметры**:
- Отсутствуют явные параметры, так как функция должна генерировать контексты на основе предоставленных входных данных.

**Возвращает**:
- `list[str]`: Список строк, где каждая строка представляет собой контекст для генерации описания персонажа.

**Пример использования**:
```python
# Вход:
# "Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not"

# Выход:
# ["Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies", "Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.", "Create a Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children."]
```