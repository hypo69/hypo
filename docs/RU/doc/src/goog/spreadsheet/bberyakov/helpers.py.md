# Модуль `helpers`

## Обзор

Модуль `helpers` содержит функции для преобразования цветовых форматов, включая HEX в DECIMAL, DECIMAL в HEX и HEX в RGB.

## Оглавление
- [Функции](#Функции)
    - [`hex_color_to_decimal`](#hex_color_to_decimal)
    - [`decimal_color_to_hex`](#decimal_color_to_hex)
    - [`hex_to_rgb`](#hex_to_rgb)

## Функции

### `hex_color_to_decimal`

**Описание**: Переводит HEX цвет в DECIMAL.

**Параметры**:
- `letters` (str): HEX код цвета.

**Возвращает**:
- `int`: DECIMAL представление цвета.

**Пример использования**:
```python
print(hex_color_to_decimal('a'))  # Output: '1'
print(hex_color_to_decimal('b'))  # Output: '2'
print(hex_color_to_decimal('c'))  # Output: '3'
print(hex_color_to_decimal('aa')) # Output: '27'
print(hex_color_to_decimal('ab')) # Output: '28'
print(hex_color_to_decimal('ac')) # Output: '29'
```

### `decimal_color_to_hex`

**Описание**: Переводит DECIMAL цвет в HEX.

**Параметры**:
- `number` (int): DECIMAL представление цвета.

**Возвращает**:
- `str`: HEX код цвета.

### `hex_to_rgb`

**Описание**: Переводит HEX цвет в RGB.

**Параметры**:
- `hex` (str): HEX код цвета.

**Возвращает**:
- `tuple`: RGB представление цвета в виде кортежа.