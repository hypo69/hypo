# Модуль `helpers`

## Обзор

Модуль `helpers` предоставляет набор функций для преобразования цветовых форматов, включая конвертацию из HEX в DECIMAL, DECIMAL в HEX и HEX в RGB.

## Оглавление

- [Функции](#функции)
  - [`hex_color_to_decimal`](#hex_color_to_decimal)
  - [`decimal_color_to_hex`](#decimal_color_to_hex)
  - [`hex_to_rgb`](#hex_to_rgb)

## Функции

### `hex_color_to_decimal`

**Описание**: Преобразует HEX цвет в DECIMAL.

**Параметры**:
- `letters` (str): Строка, представляющая HEX цвет.

**Возвращает**:
- `int`: Число, представляющее DECIMAL цвет.

**Пример использования**:
```python
print(hex_color_to_decimal('a'))  # Output: 1
print(hex_color_to_decimal('b'))  # Output: 2
print(hex_color_to_decimal('c'))  # Output: 3
print(hex_color_to_decimal('aa')) # Output: 27
print(hex_color_to_decimal('ab')) # Output: 28
print(hex_color_to_decimal('ac')) # Output: 29
```

### `decimal_color_to_hex`

**Описание**: Преобразует DECIMAL цвет в HEX.

**Параметры**:
- `number` (int): Число, представляющее DECIMAL цвет.

**Возвращает**:
- `str`: Строка, представляющая HEX цвет.

### `hex_to_rgb`

**Описание**: Преобразует HEX цвет в RGB.

**Параметры**:
- `hex` (str): Строка, представляющая HEX цвет, может начинаться с `#`.

**Возвращает**:
- `tuple`: Кортеж из трех целых чисел, представляющих значения RGB цвета.
   
**Пример**:
```
#FFFFFF -> (255, 255, 255)
```