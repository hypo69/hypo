# Модуль `helpers.py`

## Обзор

Модуль `helpers.py` содержит функции для преобразования цветовых форматов, таких как HEX в DECIMAL, DECIMAL в HEX и HEX в RGB.

## Подробней

Этот модуль предоставляет набор инструментов для работы с цветами в различных форматах. Он может быть полезен в проектах, где требуется конвертация цветов между разными представлениями, например, при работе с графическим интерфейсом, веб-дизайном или анализом данных.

## Функции

### `hex_color_to_decimal`

```python
def hex_color_to_decimal(letters: str) -> int:
    """ Перевод HEX->DECIMAL
    
    @param letters `str` : [description]
    Returns : 
         int : [description]

    ### Example usage 
    print(number_to_letter(1))  # Output: 'a' 
    print(number_to_letter(2))  # Output: 'b' 
    print(number_to_letter(3))  # Output: 'c' 
    print(number_to_letter(27))  # Output: 'aa' 
    print(number_to_letter(28))  # Output: 'ab' 
    print(number_to_letter(29))  # Output: 'ac' 

    """
    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        """
         [Function's description]

        Parameters : 
             letter : str : [description]
        Returns : 
             int : [description]

        """
        """
        ord() function returns the Unicode code from a given character. 

        print(ord('a'))  # Output: 97 

        """
        return str (ord (letter.lower()) - 96).upper()
    return letter_to_number(letters) if len(letters) == 1 else (letter_to_number(letters[0]) * 26) + letter_to_number(letters[1])
```

**Описание**: Преобразует шестнадцатеричное представление цвета в десятичное.

**Как работает функция**:
Функция `hex_color_to_decimal` принимает строку `letters`, представляющую собой шестнадцатеричный цвет, и преобразует её в десятичное число. Сначала строка приводится к верхнему регистру. Если длина строки равна 1, вызывается внутренняя функция `letter_to_number` для преобразования символа в число. Если длина строки больше 1, функция вычисляет десятичное значение как сумму произведения числового значения первого символа на 26 и числового значения второго символа.

**Параметры**:
- `letters` (str): Шестнадцатеричное представление цвета.

**Возвращает**:
- `int`: Десятичное представление цвета.

**Примеры**:

```python
print(number_to_letter(1))  # Output: 'a'
print(number_to_letter(2))  # Output: 'b'
print(number_to_letter(3))  # Output: 'c'
print(number_to_letter(27))  # Output: 'aa'
print(number_to_letter(28))  # Output: 'ab'
print(number_to_letter(29))  # Output: 'ac'
```

### `decimal_color_to_hex`

```python
def decimal_color_to_hex(number: int) -> str:
    """
     [Function's description]

    Parameters : 
         number : int : [description]
    Returns : 
         str : [description]

    """
    if number <= 26:
        return str (chr (number + 96)).upper()
    else:
        quotient, remainder = divmod (number - 1, 26)
        return str ( decimal_color_to_hex (quotient) + chr (remainder + 97) ).upper()
```

**Описание**: Преобразует десятичное представление цвета в шестнадцатеричное.

**Как работает функция**:
Функция `decimal_color_to_hex` принимает целое число `number`, представляющее собой десятичный цвет, и преобразует его в шестнадцатеричное представление. Если число меньше или равно 26, функция преобразует его в соответствующий символ (букву) и возвращает его в верхнем регистре. Если число больше 26, функция вычисляет частное и остаток от деления числа на 26 и рекурсивно вызывает себя с частным, добавляя к результату символ, соответствующий остатку.

**Параметры**:
- `number` (int): Десятичное представление цвета.

**Возвращает**:
- `str`: Шестнадцатеричное представление цвета.

### `hex_to_rgb`

```python
def hex_to_rgb (hex: str) -> tuple:
    """
     [Function's description]

    Parameters : 
         hex : str : [description]
    Returns : 
         tuple : [description]

    """
        """
        #FFFFFF -> (255, 255, 255) 

        `hex`: color in hexadecimal
        """
        hex = hex[1:] if '#' in hex else hex           
        return (int (hex[:2], 16), int (hex[2:4], 16), int (hex[4:], 16) )
```

**Описание**: Преобразует шестнадцатеричное представление цвета в RGB.

**Как работает функция**:
Функция `hex_to_rgb` принимает строку `hex`, представляющую собой шестнадцатеричный цвет, и преобразует её в кортеж RGB. Сначала функция удаляет символ `#`, если он присутствует в строке. Затем функция разбивает строку на три части (по две цифры) и преобразует каждую часть в десятичное число, используя основание 16. Возвращается кортеж из трех чисел, представляющих значения красного, зеленого и синего цветов.

**Параметры**:
- `hex` (str): Шестнадцатеричное представление цвета.

**Возвращает**:
- `tuple`: Кортеж, содержащий значения RGB (красный, зеленый, синий).

**Примеры**:

Для HEX `#FFFFFF` -> RGB `(255, 255, 255)`