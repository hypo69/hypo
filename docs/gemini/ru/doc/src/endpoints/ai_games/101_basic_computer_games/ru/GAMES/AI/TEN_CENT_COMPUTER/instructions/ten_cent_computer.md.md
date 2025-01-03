# Симулятор "10-центового компьютера"

## Обзор

Этот симулятор имитирует "10-центовый компьютер" для обучения детей двоичной системе счисления. Он представляет числа в двоичной форме с помощью 4 "лампочек" (0 - лампа выключена, 1 - лампа включена), которые обозначают 1, 2, 4 и 8 соответственно (справа налево). Пользователь может вводить десятичные числа, а симулятор показывает их двоичное представление, или вводить двоичные представления, а симулятор показывает их десятичное значение. Симулятор также может объяснить свои действия.

## Функции

### `process_input`

**Описание**: Обрабатывает ввод пользователя, определяя, является ли ввод десятичным числом или двоичным представлением, и возвращает соответствующий результат.

**Параметры**:
- `input_string` (str): Строка ввода пользователя.

**Возвращает**:
- `str`: Строка с результатом обработки ввода, включающая двоичное представление, десятичное значение и объяснение.

### `decimal_to_binary`

**Описание**: Преобразует десятичное число в его двоичное представление с помощью 4 бит.

**Параметры**:
- `decimal` (int): Десятичное число для преобразования.

**Возвращает**:
- `str`: Строка, представляющая двоичное число, или `None`, если ввод некорректен.

**Вызывает исключения**:
- `ValueError`: Если десятичное число находится вне допустимого диапазона (0-15).

### `binary_to_decimal`

**Описание**: Преобразует двоичное представление в десятичное число.

**Параметры**:
- `binary` (str): Строка двоичного представления.

**Возвращает**:
- `int`: Десятичное значение двоичного представления, или `None`, если ввод некорректен.

**Вызывает исключения**:
- `ValueError`: Если двоичная строка имеет неверный формат.

### `explain_decimal`

**Описание**: Преобразует десятичное число в двоичное представление и возвращает объяснение.

**Параметры**:
- `decimal` (int): Десятичное число для преобразования.

**Возвращает**:
- `str`: Строка с двоичным представлением и объяснением, или `None`, если ввод некорректен.

### `explain_binary`

**Описание**: Преобразует двоичное представление в десятичное число и возвращает объяснение.

**Параметры**:
- `binary` (str): Строка двоичного представления.

**Возвращает**:
- `str`: Строка с десятичным значением и объяснением, или `None`, если ввод некорректен.

## Пример использования

### Ввод десятичного числа
```
Пользователь: `Десятичное: 5`
Вы: `Двоичное: 0101, объяснение: Включены лампочки 1 и 4, 1+4=5`
```

### Ввод двоичного представления
```
Пользователь: `Лампочки: 1010`
Вы: `Десятичное: 10, объяснение: Включены лампочки 2 и 8, 2+8=10`
```

### Запрос объяснения
```
Пользователь: `Объясните как 7`
Вы: `Двоичное: 1110, объяснение: Включены лампочки 1,2 и 4. 1+2+4 = 7`
```
```python
def process_input(input_string: str) -> str:
    """
    Обрабатывает ввод пользователя, определяя, является ли ввод десятичным числом или двоичным представлением, и возвращает соответствующий результат.

    Args:
        input_string (str): Строка ввода пользователя.

    Returns:
        str: Строка с результатом обработки ввода, включающая двоичное представление, десятичное значение и объяснение.
    """
    try:
        if input_string.startswith("Десятичное: "):
            decimal = int(input_string[11:])
            return explain_decimal(decimal)
        elif input_string.startswith("Лампочки: "):
             binary = input_string[9:]
             return explain_binary(binary)
        elif input_string.startswith("Объясните как "):
            try:
                decimal = int(input_string[14:])
                return explain_decimal(decimal)
            except ValueError:
                binary = input_string[14:]
                return explain_binary(binary)
        else:
            return "Некорректный ввод."
    except Exception as ex:
        return f"Произошла ошибка: {ex}"


def decimal_to_binary(decimal: int) -> str | None:
    """
    Преобразует десятичное число в его двоичное представление с помощью 4 бит.

    Args:
        decimal (int): Десятичное число для преобразования.

    Returns:
        str: Строка, представляющая двоичное число, или `None`, если ввод некорректен.

    Raises:
        ValueError: Если десятичное число находится вне допустимого диапазона (0-15).
    """
    if not 0 <= decimal <= 15:
        raise ValueError("Десятичное число должно быть в диапазоне от 0 до 15.")
    
    binary = bin(decimal)[2:].zfill(4)
    return binary


def binary_to_decimal(binary: str) -> int | None:
    """
    Преобразует двоичное представление в десятичное число.

    Args:
        binary (str): Строка двоичного представления.

    Returns:
         int: Десятичное значение двоичного представления, или `None`, если ввод некорректен.
    
    Raises:
        ValueError: Если двоичная строка имеет неверный формат.
    """
    if not all(bit in '01' for bit in binary) or len(binary) != 4:
        raise ValueError("Двоичная строка должна состоять из 4 символов 0 и 1.")

    return int(binary, 2)

def explain_decimal(decimal: int) -> str | None:
    """
    Преобразует десятичное число в двоичное представление и возвращает объяснение.

    Args:
        decimal (int): Десятичное число для преобразования.

    Returns:
        str: Строка с двоичным представлением и объяснением, или `None`, если ввод некорректен.
    """
    try:
      binary = decimal_to_binary(decimal)
      explanation = f"Включены лампочки "
      active_lamps = []
      if binary[3] == '1':
          active_lamps.append("1")
      if binary[2] == '1':
          active_lamps.append("2")
      if binary[1] == '1':
          active_lamps.append("4")
      if binary[0] == '1':
          active_lamps.append("8")
      
      explanation += ", ".join(active_lamps)
      explanation += f". { '+'.join(active_lamps)} = {decimal}"
      return f"Двоичное: {binary}, объяснение: {explanation}"
    except ValueError as ex:
        return f"Ошибка: {ex}"

def explain_binary(binary: str) -> str | None:
    """
    Преобразует двоичное представление в десятичное число и возвращает объяснение.

    Args:
        binary (str): Строка двоичного представления.

    Returns:
        str: Строка с десятичным значением и объяснением, или `None`, если ввод некорректен.
    """
    try:
        decimal = binary_to_decimal(binary)
        explanation = f"Включены лампочки "
        active_lamps = []
        if binary[3] == '1':
            active_lamps.append("1")
        if binary[2] == '1':
            active_lamps.append("2")
        if binary[1] == '1':
            active_lamps.append("4")
        if binary[0] == '1':
            active_lamps.append("8")

        explanation += ", ".join(active_lamps)
        explanation += f". { '+'.join(active_lamps)} = {decimal}"
        return f"Десятичное: {decimal}, объяснение: {explanation}"
    except ValueError as ex:
        return f"Ошибка: {ex}"