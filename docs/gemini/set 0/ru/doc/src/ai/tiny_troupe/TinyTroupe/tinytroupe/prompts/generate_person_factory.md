# Модуль generate_person_factory

## Обзор

Этот модуль предназначен для генерации контекстов, используемых для создания описаний людей.  Входной контекст предоставляет общие параметры (демография, черты характера, интересы и т.д.), а выходные контексты представляют собой более конкретные, но вытекающие из исходного, описания.  Цель - предоставить набор различных контекстов, которые могут быть использованы для генерации людей с разными характеристиками.

## Функции

### `generate_person_contexts`

**Описание**: Функция генерирует массив контекстов для создания описаний людей.

**Параметры**:

- `input_context` (str): Входной контекст, описывающий общие характеристики людей для генерации. Пример: "Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies".
- `num_contexts` (int, optional): Количество контекстов для генерации. По умолчанию 3.

**Возвращает**:

- list[str]: Массив строк, представляющих контексты для создания описаний людей. Возвращает `None`, если входной `input_context` некорректен или не соответствует формату.

**Вызывает исключения**:

- `ValueError`: Если `num_contexts` не является положительным целым числом.
- `TypeError`: Если `input_context` не является строкой.


```python
def generate_person_contexts(input_context: str, num_contexts: int = 3) -> list[str] | None:
    """
    Args:
        input_context (str): Входной контекст, описывающий общие характеристики людей для генерации. Пример: "Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies".
        num_contexts (int, optional): Количество контекстов для генерации. По умолчанию 3.

    Returns:
        list[str]: Массив строк, представляющих контексты для создания описаний людей. Возвращает None, если входной input_context некорректен или не соответствует формату.

    Raises:
        ValueError: Если num_contexts не является положительным целым числом.
        TypeError: Если input_context не является строкой.
    """
    if not isinstance(input_context, str):
        raise TypeError("input_context must be a string")
    if not isinstance(num_contexts, int) or num_contexts <= 0:
        raise ValueError("num_contexts must be a positive integer")

    # Здесь реализация логики генерации контекстов
    # ... (Обработка input_context и генерация новых контекстов)
    # ... (Возврат списка новых контекстов)
    
    #Пример реализации
    output_contexts = []
    for i in range(num_contexts):
      output_contexts.append(f"Context {i + 1} based on {input_context}")
    
    return output_contexts
```