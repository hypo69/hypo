# Модуль generate_person_factory

## Обзор

Этот модуль предоставляет инструменты для генерации контекстов, используемых для создания описаний персон.  Он принимает широкие контексты, содержащие демографические данные, характеристики и черты личности, и генерирует из них более конкретные, но связанные контексты.

## Функции

### `generate_person_contexts`

**Описание**: Функция генерирует массив контекстов для создания описаний персон.

**Параметры**:

- `broad_context` (str):  Широкий контекст, описывающий общий профиль персон.  Ожидается строковое описание с параметрами, такими как национальность, возраст, экономическое положение, вероисповедание, семейное положение, наличие детей и т.д.
- `num_persons` (int, optional): Количество персон, для которых нужно сгенерировать контексты. По умолчанию 1.

**Возвращает**:

- `list[str]`: Список строк, представляющих конкретные контексты для генерации описаний персон.  Возвращает `None`, если входные данные некорректны или при возникновении ошибки.


**Вызывает исключения**:

- `ValueError`: Если `broad_context` пуст или не содержит необходимых параметров для генерации.
- `TypeError`: Если входные данные имеют неверный тип.
- `Exception`:  Для других потенциальных ошибок.


**Примеры использования**:

```python
contexts = generate_person_contexts(
    broad_context="Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies",
    num_persons=1
)

print(contexts)
```

```python
contexts = generate_person_contexts(
    broad_context="Please, generate 3 person(s) description(s) based on the following broad context: Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it can have children or not, it can be a professional or not, it can be a worker or not",
    num_persons=3
)

print(contexts)
```
```python
# Пример использования, возвращающий None
contexts = generate_person_contexts(broad_context="Некорректный контекст", num_persons=1)

print(contexts)
```


**Примечания**:

-  Реализация `generate_person_contexts` должна содержать логику для извлечения деталей из `broad_context` и создания соответствующих специфичных контекстов.
- Функция может использовать методы обработки текста (парсинг, разбор, извлечение ключевых слов) для более точной генерации.


```