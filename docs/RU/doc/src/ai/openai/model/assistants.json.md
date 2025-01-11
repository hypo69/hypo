# Документация для `hypotez/src/ai/openai/model/assistants.json`

## Обзор

Файл `assistants.json` содержит JSON-представление данных о различных ассистентах, используемых в системе. Каждый ассистент идентифицируется уникальным ключом и имеет свойства, такие как имя, заголовок, описание и инструкции.

## Оглавление

- [Обзор](#обзор)
- [Структура JSON](#структура-json)
- [Пример ассистента](#пример-ассистента)
  - [Свойства ассистента](#свойства-ассистента)
  - [Инструкции](#инструкции)

## Структура JSON

Файл `assistants.json` представляет собой JSON-объект, где ключи являются идентификаторами ассистентов, а значения - объектами, описывающими свойства каждого ассистента.

## Пример ассистента

Пример структуры объекта ассистента:

```json
{
  "asst_dr5AgQnhhhnef5OSMzQ9zdk9": {
    "name": "create promo: product_names->categories- titles, description",
    "title": "",
    "description": "Create a JSON with name and description for product titles list",
    "instructions": {
      "0": {
        "name": "",
        "text": "",
        "file": "src\\\\ai\\\\prompts\\\\aliexpress_campaign\\\\system_instruction.txt"
      },
      "1": {
        "name": "",
        "text": ""
      }
    }
  },
  "asst_uDr5aVY3qRByRwt5qFiMDk43": {
    "name": "developer for hypo code",
    "title": "",
    "description": "Create a JSON with name and description for product titles list",
    "instructions": {
      "0": {
        "name": "",
        "text": "",
        "file": "src\\\\ai\\\\prompts\\\\aliexpress_campaign\\\\system_instruction.txt"
      },
      "1": {
        "name": "",
        "text": ""
      }
    }
  }
}
```

### Свойства ассистента

- `name` (str): Имя ассистента.
- `title` (str): Заголовок ассистента.
- `description` (str): Описание ассистента.
- `instructions` (dict): Инструкции для ассистента.

### Инструкции

Объект `instructions` содержит инструкции для ассистента, где ключи - это порядковые номера инструкций, а значения - объекты с деталями инструкций.

- `name` (str): Имя инструкции (может быть пустым).
- `text` (str): Текст инструкции (может быть пустым).
- `file` (str, optional): Путь к файлу с инструкцией (может отсутствовать).