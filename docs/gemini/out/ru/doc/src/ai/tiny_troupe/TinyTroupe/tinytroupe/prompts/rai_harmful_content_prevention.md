# Модуль rai_harmful_content_prevention

## Обзор

Этот модуль содержит функции для предотвращения генерации вредного контента моделями.

## Функции

### `is_harmful_content`

**Описание**: Определяет, является ли сгенерированный текст вредным.

**Параметры**:

- `text` (str): Текст, который необходимо проверить.

**Возвращает**:

- `bool`: `True`, если текст вредный, `False` иначе.

**Вызывает исключения**:

- `TypeError`: Если входной параметр не является строкой.