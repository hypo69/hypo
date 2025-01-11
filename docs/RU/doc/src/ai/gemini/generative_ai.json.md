# Конфигурация генеративной AI Gemini

## Обзор

Этот файл содержит конфигурацию для генеративной AI Gemini, включая параметры хранилища и выбора модели.

## Содержание

- [Обзор](#обзор)
- [Конфигурация](#конфигурация)
  - [storage](#storage)
  - [storage_choices](#storage_choices)
  - [model](#model)
  - [model_choices](#model_choices)

## Конфигурация

### `storage`

**Описание**: Определяет способ хранения данных, используемый генеративной AI.

**Тип**: `str`

**Значение по умолчанию**: `external_storage`

### `storage_choices`

**Описание**: Список доступных вариантов хранения данных для генеративной AI.

**Тип**: `list[str]`

**Значения**:
- `"external_storage"`: Внешнее хранилище.
- `"data"`: Локальное хранилище данных.
- `"google_drive"`: Google Drive.

### `model`

**Описание**: Определяет используемую модель генеративной AI.

**Тип**: `str`

**Значение по умолчанию**: `gemini-2.0-flash-exp`

### `model_choices`

**Описание**: Список доступных моделей генеративной AI.

**Тип**: `list[str]`

**Значения**:
- `"gemini-2.0-flash-exp"`: Gemini 2.0 Flash Experimental.
- `"gemini-1.5-flash-8b-exp-0924"`: Gemini 1.5 Flash 8B Experimental (версия от 09.24).
- `"gemini-1.5-flash"`: Gemini 1.5 Flash.