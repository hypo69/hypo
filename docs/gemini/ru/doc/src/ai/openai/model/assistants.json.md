# Документация для `hypotez/src/ai/openai/model/assistants.json`

## Обзор

Файл `assistants.json` содержит JSON-объект, описывающий ассистентов, используемых в системе. Каждый ассистент имеет имя, заголовок, описание и инструкции. Инструкции могут содержать текст или ссылки на файлы.

## Оглавление

1.  [Обзор](#обзор)
2.  [Структура файла](#структура-файла)
3.  [Объекты ассистентов](#объекты-ассистентов)

## Структура файла

Файл представляет собой JSON-объект, где ключами являются идентификаторы ассистентов, а значениями - объекты, содержащие информацию об этих ассистентах.

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

## Объекты ассистентов

Каждый ассистент представлен объектом со следующими полями:

### `name`

**Описание**: Имя ассистента.
- **Тип**: `str`
- **Пример**: `"create promo: product_names->categories- titles, description"`

### `title`

**Описание**: Заголовок ассистента.
- **Тип**: `str`
- **Пример**: `""`

### `description`

**Описание**: Описание ассистента.
- **Тип**: `str`
- **Пример**: `"Create a JSON with name and description for product titles list"`

### `instructions`

**Описание**: Инструкции для ассистента.
- **Тип**: `dict`
- **Структура**: Объект, где ключи - порядковые номера инструкций, а значения - объекты с описанием инструкции.

#### Инструкции
   Каждая инструкция представляет собой объект со следующими полями:
    
   #### `name`
    **Описание**: Имя инструкции.
    - **Тип**: `str`
    - **Пример**: `""`
    
   #### `text`
    **Описание**: Текст инструкции.
    - **Тип**: `str`
    - **Пример**: `""`
    
   #### `file`
    **Описание**: Путь к файлу с инструкциями.
    - **Тип**: `str`
    - **Пример**: `"src\\\\ai\\\\prompts\\\\aliexpress_campaign\\\\system_instruction.txt"`