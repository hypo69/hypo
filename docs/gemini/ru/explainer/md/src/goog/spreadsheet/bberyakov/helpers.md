```MD
# <input code>

```python
## \file hypotez/src/goog/spreadsheet/bberyakov/helpers.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet.bberyakov 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.goog.spreadsheet.bberyakov """


""" перевод цветовых форматов.
Перевод:
- HEX->DECIMAL
- DECIMAL->HEX
- HEX->RGB

 @section libs imports:

Author(s):
  - Created by hypotez
"""


def hex_color_to_decimal(letters: str) -> int:
    """ Перевод HEX->DECIMAL
    
    @param letters `str` : [description]
    Returns : 
         int : [description]

    ### Example usage 
    print(number_to_letter(1))  # Output: 'a' \n
    print(number_to_letter(2))  # Output: 'b' \n
    print(number_to_letter(3))  # Output: 'c' \n
    print(number_to_letter(27))  # Output: 'aa' \n
    print(number_to_letter(28))  # Output: 'ab' \n
    print(number_to_letter(29))  # Output: 'ac' \n
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
        ord() function returns the Unicode code from a given character. \n
        print(ord('a'))  # Output: 97 \n
        """
        return str (ord (letter.lower()) - 96).upper()
    return letter_to_number(letters) if len(letters) == 1 else (letter_to_number(letters[0]) * 26) + letter_to_number(letters[1])


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


def hex_to_rgb (hex: str) -> tuple:
    """
     [Function's description]

    Parameters : 
         hex : str : [description]
    Returns : 
         tuple : [description]

    """
        """
        #FFFFFF -> (255, 255, 255) \n

        `hex`: color in hexadecimal
        """
        hex = hex[1:] if '#' in hex else hex           
        return (int (hex[:2], 16), int (hex[2:4], 16), int (hex[4:], 16) )
```

# <algorithm>

**Функция `hex_color_to_decimal`**:

1. Принимает строку `letters` (HEX-цвет).
2. Преобразует строку в верхний регистр.
3. Вложенная функция `letter_to_number`:
   - Принимает символ `letter`.
   - Возвращает соответствующее ему числовое значение (от 'a' до 'z').
4. Если длина `letters` равна 1, возвращает результат `letter_to_number`.
5. Иначе возвращает результат сложения (перевода в деc. систему) двух символов.


**Функция `decimal_color_to_hex`**:

1. Принимает целое число `number`.
2. Если `number` меньше или равно 26, возвращает соответствующий ему символ.
3. Иначе:
   - Вычисляет частное (`quotient`) и остаток (`remainder`) от деления `number - 1` на 26.
   - Рекурсивно вызывает `decimal_color_to_hex` с `quotient` и строит из этого результат.


**Функция `hex_to_rgb`**:

1. Принимает строку `hex`.
2. Удаляет символ '#' из начала строки, если он есть.
3. Возвращает кортеж из трёх целых чисел, полученных из первых двух, следующих двух и следующих двух символов строки `hex`, интерпретируя их как шестнадцатеричные числа.


# <mermaid>

```mermaid
graph LR
    A[hex_color_to_decimal] --> B{letters.upper()};
    B --> C[letter_to_number];
    C --> D{len(letters)==1};
    D -- Yes --> E[return letter_to_number(letters)];
    D -- No --> F(return (letter_to_number(letters[0])*26) + letter_to_number(letters[1]));
    F --> E;
    E --> G[return value];

    H[decimal_color_to_hex] --> I{number <= 26};
    I -- Yes --> J[return chr(number + 96).upper()];
    I -- No --> K[quotient, remainder = divmod(number - 1, 26)];
    K --> L[decimal_color_to_hex(quotient)];
    L --> M(return L + chr(remainder + 97).upper());
    M --> G;

    N[hex_to_rgb] --> O{ '#' in hex };
    O -- Yes --> P[hex = hex[1:] ];
    O -- No --> P;
    P --> Q(return (int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16)));
    Q --> G;
```

# <explanation>

**Импорты:**

Нет импортов в этом коде.


**Классы:**

Нет классов в этом коде.


**Функции:**

- `hex_color_to_decimal(letters: str) -> int`: Преобразует шестнадцатеричное цветовое представление (строку) в десятичное целое число.
- `decimal_color_to_hex(number: int) -> str`: Преобразует десятичное целое число в шестнадцатеричное цветовое представление (строку).
- `hex_to_rgb(hex: str) -> tuple`: Преобразует шестнадцатеричное цветовое представление (строку) в кортеж из трёх целых чисел (RGB).

**Переменные:**

`MODE`: Строковая переменная, хранящая значение 'dev'.  Она определяет режим работы, но в данном коде не используется.


**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Нет проверки ввода на корректность.  Функция `hex_color_to_decimal` может вызывать ошибку, если в `letters` будут символы, отличные от 'a'-'f' и '0'-'9', а `hex_to_rgb` - если строка `hex` не имеет правильного формата. Необходимо добавить обработку таких случаев (например, используя `try...except` блоки).
- **Документация:**  Документация к функциям должна быть более полной и точной. Нужно подробно описать входные параметры, возможные значения, исключения и примеры использования.
- **Читаемость:**  Имена переменных могли бы быть более информативными.
- **Рекурсия в `decimal_color_to_hex`**:  Рекурсивный вызов функции `decimal_color_to_hex` может быть не оптимальным для больших значений `number`. Вместо рекурсии можно было бы использовать цикл для достижения того же результата.


**Взаимосвязь с другими частями проекта:**

Функции в файле `helpers.py` предназначены для преобразования цветовых форматов. Вероятно, они используются в других частях приложения, таких как  обработка данных о цветах, визуализация, или  интерфейс пользователя.  Можно предположить, что эти функции могут использоваться в коде, который обрабатывает таблицы, или работает с документами Google Sheets.

```