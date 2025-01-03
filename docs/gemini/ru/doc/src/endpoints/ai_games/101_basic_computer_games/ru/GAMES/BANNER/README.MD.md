# Игра Banner: создание текстового баннера

## Обзор

Данная программа создает текстовый баннер из текста, введенного пользователем. Она приветствует пользователя, запрашивает текст и выводит его в виде оформленного баннера. Код демонстрирует базовые принципы работы с функциями, вводом-выводом и условными операторами в Python.

## Оглавление

1. [Обзор](#обзор)
2. [Функции](#функции)
   - [`create_banner`](#create_banner)
3. [Основная часть программы](#основная-часть-программы)
4. [Описание работы кода](#описание-работы-кода)
   - [Функция `create_banner(text)`](#1-функция-create_bannertext)
   - [Основная часть программы](#2-основная-часть-программы)
5. [Пример работы программы](#пример-работы-программы)
6. [Как интерпретатор разбирает код](#как-интерпретатор-разбирает-код)
    - [Порядок выполнения операторов в Python](#порядок-выполнения-операторов-в-python)
    - [Определение функций](#определение-функций)
    - [Вызов функций](#вызов-функций)
    - [Условные операторы (if, else)](#условные-операторы-if-else)
    - [Циклы (for, while)](#циклы-for-while)
    - [Операторы присваивания (=)](#операторы-присваивания-)
    - [Выражения и вычисления](#выражения-и-вычисления)
7. [Итог](#итог)

## Функции

### `create_banner`

**Описание**: Создаёт текстовый баннер из введённого текста.

**Параметры**:
- `text` (str): Строка, которую нужно преобразовать в баннер.

**Возвращает**:
- `None`: Функция ничего не возвращает, а выводит результат в консоль.

## Основная часть программы

Основная часть программы отвечает за взаимодействие с пользователем: приветствие, запрос текста и проверка ввода.

## Описание работы кода

### 1. Функция `create_banner(text)`

- **Принимает**: строку `text` – текст, который нужно преобразовать в баннер.
- **Выполняет**:
  - Вычисляет ширину баннера, добавляя 4 символа для рамки (`*` и пробелы).
  - Выводит верхнюю и нижнюю границы баннера с помощью символа `*`.
  - Выводит текст, окружённый рамкой.

### 2. Основная часть программы

- **Приветствует** пользователя и объясняет, что делает программа.
- **Запрашивает** у пользователя текст для создания баннера.
- **Проверяет**, что текст не пустой:
  - Если пользователь ввёл пустую строку, программа сообщает об ошибке и предлагает попробовать снова.
  - Если текст введён, программа выводит созданный баннер.

## Пример работы программы

Если пользователь ввёл текст `"Привет"`, программа выведет:

```
*********
* Привет *
*********
```

## Как интерпретатор разбирает код

### Порядок выполнения операторов в Python

- Python читает код построчно, начиная сверху и двигаясь вниз.
- Каждая строка выполняется последовательно, если она не является частью функции, условия или цикла.

### Определение функций

- Функции определяются с помощью ключевого слова `def`.
- Определение функции не выполняет её код, а только создаёт "шаблон" для будущего вызова.

### Вызов функций

- Когда функция вызывается, Python переходит к её определению и выполняет код внутри неё.
- После завершения выполнения функции, управление возвращается в то место, откуда она была вызвана.

### Условные операторы (if, else)

- Условные операторы проверяют условие и выполняют код внутри блока, если условие истинно.
- Если условие ложно, Python пропускает блок и переходит к следующей строке.

### Циклы (for, while)

- Циклы позволяют повторять выполнение блока кода несколько раз.
- Python проверяет условие цикла перед каждой итерацией.

### Операторы присваивания (=)

- Операторы присваивания сохраняют значение в переменную.
- Это происходит до выполнения других операций, таких как вызов функций или условные операторы.

### Выражения и вычисления

- Выражения (например, `len(text) + 4`) вычисляются до того, как их результат используется в других частях кода.

## Итог

Эта программа демонстрирует базовые принципы работы с функциями, вводом-выводом и условными операторами в Python. Она может быть полезна для начинающих изучать язык и понимание того, как работает интерпретатор Python.