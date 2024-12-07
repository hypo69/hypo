# Модуль предотвращения вредного контента (RAI)

## Обзор

Этот модуль предоставляет функции для предотвращения генерации вредного контента моделями искусственного интеллекта (RAI). Он фокусируется на фильтрации контента, который может быть вредным, оскорбительным или нежелательным.

## Функции

### `check_harmful_content`

**Описание**: Проверяет входящий текст на наличие вредного контента, используя заданные правила.

**Параметры**:

- `text` (str): Входящий текст для проверки.

- `rules` (list[dict], optional): Список правил для проверки.  По умолчанию используется встроенный набор правил.  Каждый элемент `rules` представляет собой словарь с ключами `pattern` (строка, регулярное выражение) и `is_harmful` (булевое значение).

**Возвращает**:

- `bool`: `True`, если текст содержит вредный контент, `False` в противном случае. Возможен `None` в случае ошибки.

**Вызывает исключения**:

- `ValueError`: Если входной параметр `text` не является строкой.
- `TypeError`: Если параметр `rules` имеет неверный тип.


### `add_harmful_content_rule`

**Описание**: Добавляет новое правило для проверки вредного контента.

**Параметры**:

- `pattern` (str): Регулярное выражение для определения вредного текста.

- `is_harmful` (bool): `True`, если текст, соответствующий шаблону, считается вредным, `False` в противном случае.

**Возвращает**:

- `None`.

**Вызывает исключения**:

- `TypeError`: Если тип параметров `pattern` или `is_harmful` некорректен.
- `ValueError`: Если шаблон (pattern) не является корректным регулярным выражением.

## Примеры использования

```python
# Пример использования функции check_harmful_content с набором правил
from tinytroupe.prompts import rai_harmful_content_prevention

text = "Этот текст совершенно безопасен."
result = rai_harmful_content_prevention.check_harmful_content(text)
print(result)  # Выведет False

text_with_harm = "Этот текст содержит оскорбительные слова."
result = rai_harmful_content_prevention.check_harmful_content(text_with_harm)
print(result) # Выведет True

# Пример добавления нового правила
rai_harmful_content_prevention.add_harmful_content_rule(pattern=r"нецензурные слова", is_harmful=True)
result = rai_harmful_content_prevention.check_harmful_content("Это предложение содержит нецензурные слова")
print(result) # Выведет True

```
```
```