# Документация для `banner_.ai.json`

## Обзор

Файл `banner_.ai.json` содержит JSON-структуру, представляющую системные инструкции.

## Содержание

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
3. [Ключи](#ключи)
    - [system_instructions](#system_instructions)

## Структура JSON

```json
{
  "system_instructions": {
    "1": "system_instruction_asterisk",
    "2": "system_instruction_tilde",
    "3": "system_instruction_hash"
  }
}
```

## Ключи

### `system_instructions`

**Описание**: Словарь, содержащий системные инструкции. Ключами словаря являются строковые идентификаторы инструкций, а значениями - строковые описания инструкций.

**Значение**:
- `1`: "system_instruction_asterisk"
- `2`: "system_instruction_tilde"
- `3`: "system_instruction_hash"