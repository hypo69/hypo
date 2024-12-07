# tinytroupe/prompts/rai_harmful_content_prevention.md

## Оглавление

* [Обзор](#обзор)
* [Функции](#функции)


## Обзор

Этот модуль содержит функции для предотвращения генерации вредного контента в рамках проекта Tiny Troupe. Он предоставляет инструменты для проверки текстов на наличие признаков вредоносного содержания.

## Функции

### `check_harmful_content`

**Описание**: Функция проверяет входящий текст на наличие признаков вредоносного контента.

**Параметры**:

- `text` (str): Текст, который необходимо проверить.

**Возвращает**:

- `bool`: `True`, если текст содержит вредный контент, `False` - в противном случае.

**Вызывает исключения**:

- `TypeError`: Если входной параметр `text` не является строкой.


```python
def check_harmful_content(text: str) -> bool:
    """
    Args:
        text (str): Текст, который необходимо проверить.

    Returns:
        bool: True, если текст содержит вредный контент, False - в противном случае.

    Raises:
        TypeError: Если входной параметр text не является строкой.
    """
    if not isinstance(text, str):
        raise TypeError("Входной параметр должен быть строкой")
    # Здесь необходимо реализовать логику проверки текста на вредный контент
    # Например, проверка на наличие оскорбительных слов или фраз.
    # ...
    return False  # Заглушка. Реализуйте проверку
```


```python
# пример использования функции
text1 = "Это прекрасный текст"
text2 = "Этот текст содержит оскорбительные слова"


try:
    result1 = check_harmful_content(text1)
    print(f"Результат для {text1}: {result1}")  # Выведет False

    result2 = check_harmful_content(text2)
    print(f"Результат для {text2}: {result2}")  # Выведет True
except TypeError as ex:
    print(f"Ошибка: {ex}")
```