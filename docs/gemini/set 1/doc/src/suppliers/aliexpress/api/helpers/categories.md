# Модуль hypotez/src/suppliers/aliexpress/api/helpers/categories.py

## Обзор

Модуль `categories.py` содержит функции для фильтрации категорий и подкатегорий API AliExpress. Он предоставляет инструменты для работы с объектами категорий и подкатегорий, возвращаемыми API, позволяя извлекать категории без родительской категории и подкатегории, принадлежащие определенному родителю.

## Функции

### `filter_parent_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только те, у которых нет родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.


**Возвращает**:
- List[models.Category]: Список объектов категорий, у которых нет родительской категории.


**Обработка исключений**:
- (None)


### `filter_child_categories`

**Описание**: Фильтрует список категорий и подкатегорий, возвращая только те подкатегории, которые принадлежат указанной родительской категории.

**Параметры**:
- `categories` (List[models.Category | models.ChildCategory]): Список объектов категорий или подкатегорий.
- `parent_category_id` (int): Идентификатор родительской категории.


**Возвращает**:
- List[models.ChildCategory]: Список объектов подкатегорий, принадлежащих указанной родительской категории.


**Обработка исключений**:
- (None)


## Модуль `models`

**Описание**:  Модуль `models` предположительно содержит определения классов `Category` и `ChildCategory`.  Этот модуль не документирован в данном файле, но его использование в функциях `filter_parent_categories` и `filter_child_categories` предполагает его существование.  Для полной документации необходима информация о структуре данных и атрибутах классов `Category` и `ChildCategory`.