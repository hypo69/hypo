# Документация для `101_basic_computer_games.json`

## Обзор

Файл `101_basic_computer_games.json` содержит JSON-объект, представляющий собой конфигурацию модели ИИ. В данном случае, модель называется `gemini-2.0-flash-exp`.

## Оглавление

- [Обзор](#обзор)
- [Структура файла](#структура-файла)
- [JSON Схема](#json-схема)
- [Поля](#поля)

## Структура файла

Файл содержит JSON-объект со следующей структурой:

```json
{
  "model_name": "gemini-2.0-flash-exp"
}
```

## JSON Схема

JSON-схема для файла:

```json
{
  "type": "object",
  "properties": {
    "model_name": {
      "type": "string",
      "description": "Название модели ИИ"
    }
  },
  "required": ["model_name"]
}
```

## Поля

### `model_name`
- **Описание**: Название модели ИИ.
- **Тип**: `string`
- **Пример**: `"gemini-2.0-flash-exp"`