# Модуль `src.utils.path`

## Обзор

Модуль `src.utils.path` предназначен для определения корневого пути проекта. Все импорты строятся относительно этого пути. Модуль также предоставляет функцию для получения относительного пути на основе заданного сегмента пути.

## Оглавление

- [Функции](#функции)
  - [`get_relative_path`](#get_relative_path)

## Функции

### `get_relative_path`

**Описание**: Возвращает часть пути начиная с указанного сегмента и до конца.

**Параметры**:
- `full_path` (str): Полный путь.
- `relative_from` (str): Сегмент пути, с которого нужно начать извлечение.

**Возвращает**:
- `Optional[str]`: Относительный путь начиная с `relative_from`, или `None`, если сегмент не найден.