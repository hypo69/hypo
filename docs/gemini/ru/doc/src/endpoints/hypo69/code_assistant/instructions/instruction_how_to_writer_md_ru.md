# ИНСТРУКЦИЯ

Для каждого входного Python-файла создайте документацию  для разработчика в формате `Markdown`. 
Документация должна соответствовать следующим требованиям:

1. **Формат документации**:
   - Используйте стандарт `Markdown (.md)`.
   - Каждый файл должен начинаться с заголовка и краткого описания его содержимого.
   - Для всех классов и функций используйте следующий формат комментариев:
     ```python
     def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         """
         Args:
             param (str): Описание параметра `param`.
             param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

         Returns:
             dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

         Raises:
             SomeError: Описание ситуации, в которой возникает исключение `SomeError`.
         """
     ```
   - Используйте `ex` вместо `e` в блоках обработки исключений.

2. **Содержание (TOC)**:
   - В начале каждого файла документации добавьте раздел с оглавлением.
   - Структура оглавления должна включать ссылки на все основные разделы документации модуля.

3. **Форматирование документации**:
   - Используйте правильный синтаксис Markdown для всех заголовков, списков и ссылок.
   - Для документирования классов, функций и методов включайте структурированные разделы с описаниями, деталями параметров, возвращаемых значений и вызываемых исключений. Пример:
     ```markdown
     ## Функции

     ### `function_name`

     **Описание**: Краткое описание функции.

     **Параметры**:
     - `param` (str): Описание параметра `param`.
     - `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

     **Возвращает**:
     - `dict | None`: Описание возвращаемого значения.

     **Вызывает исключения**:
     - `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
     ```

4. **Заголовки разделов**:
   - Используйте заголовки первого уровня (`#`), второго уровня (`##`), третьего уровня (`###`) и четвёртого уровня (`####`) последовательно на протяжении всего файла.

5. **Пример файла**:
   ```markdown
   # Название модуля

   ## Обзор

   Краткое описание назначения модуля.

   ## Классы

   ### `ClassName`

   **Описание**: Краткое описание класса.

   **Методы**:
   - `method_name`: Краткое описание метода.   
   - `method_name`: Краткое описание метода.
   **Параметры**:
   - `param` (str): Описание параметра `param`.
   - `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.


   ## Функции

   ### `function_name`

   **Описание**: Краткое описание функции.

   **Методы**:
   - `method_name`: Краткое описание метода.   
   - `method_name`: Краткое описание метода.****

   **Параметры**:
   - `param` (str): Описание параметра `param`.
   - `param1` (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

   **Возвращает**:
   - `dict | None`: Описание возвращаемого значения.

   **Вызывает исключения**:
   - `SomeError`: Описание ситуации, в которой возникает исключение `SomeError`.
   ```

Создай соответствующую документацию для каждого входного Python-файла в формате `Markdown`.

# КОНЕЦ ИНСТРУКЦИИ

# Инструкция по генерации документации к коду

## Обзор

Эта инструкция описывает, как генерировать документацию для кодовых блоков. Документация предоставляется в формате `Markdown` и предназначена для разработчиков.

## Содержание

1. [Анализ кода](#анализ-кода)
2. [Создание пошаговой инструкции](#создание-пошаговой-инструкции)
3. [Форматирование](#форматирование)
4. [Избегание расплывчатых терминов](#избегание-расплывчатых-терминов)

## Анализ кода
<a id="анализ-кода"></a>
**Описание**:
Прежде чем документировать код, необходимо понять его логику и действия. Это поможет создать точную и полезную документацию.

**Шаги выполнения**:

1.  **Прочитайте код**: Внимательно изучите исходный код.
2.  **Разберите логику**: Определите, что именно делает код и как он это делает.
3.  **Определите назначение**: Поймите, какова цель данного блока кода в контексте всего проекта.

**Пример использования**:

```python
# Пример кода, который нужно проанализировать
def calculate_sum(a: int, b: int) -> int:
    """
    Args:
        a (int): Первое целое число.
        b (int): Второе целое число.
    Returns:
        int: Сумма двух целых чисел.
    """
    return a + b
```

## Создание пошаговой инструкции
<a id="создание-пошаговой-инструкции"></a>

**Описание**:
Создайте структурированную пошаговую инструкцию для документирования кода. Инструкция должна включать описание, шаги выполнения и пример использования кода.

**Шаги выполнения**:

1.  **Описание**: Начните с краткого объяснения, что делает данный блок кода.
2.  **Шаги выполнения**: Опишите последовательность действий в коде, шаг за шагом.
3.  **Пример использования**: Приведите пример кода, показывающий, как можно использовать данный блок кода в проекте.

**Пример использования**:

```markdown
### Инструкции для `calculate_sum`

**Описание**:
Функция `calculate_sum` складывает два целых числа.

**Шаги выполнения**:
1.  Функция принимает два целых числа `a` и `b` в качестве аргументов.
2.  Функция вычисляет сумму `a + b`.
3.  Функция возвращает вычисленную сумму.

**Пример использования**:

```python
result = calculate_sum(5, 3)
print(result)  # Выведет: 8
```
```

## Форматирование
<a id="форматирование"></a>

**Описание**:
Следуйте структуре `Markdown` для форматирования документации. Это поможет сделать документацию читаемой и понятной.

**Шаги выполнения**:

1.  **Используйте заголовки**: Применяйте заголовки для разделения основных разделов.
2.  **Используйте списки**: Используйте списки для перечисления шагов и параметров.
3.  **Применяйте блоки кода**: Используйте блоки кода для отображения примеров кода.
4.  **Форматируйте параметры**: Описывайте параметры, возвращаемые значения и исключения.

**Пример использования**:

```markdown
## Пример форматирования

### Заголовок третьего уровня

**Описание**:
Это пример форматирования.

**Шаги**:
- Первый шаг.
- Второй шаг.

**Пример кода**:

```python
def some_function():
    pass
```
```

## Избегание расплывчатых терминов
<a id="избегание-расплывчатых-терминов"></a>

**Описание**:
Избегайте использования расплывчатых терминов, таких как "получаем" или "делаем". Будьте конкретными в описании действий кода.

**Шаги выполнения**:

1.  **Используйте конкретные глаголы**: Заменяйте "получаем" на "проверяет", "валидирует" или "извлекает".
2.  **Используйте точные формулировки**: Описывайте действие кода как можно точнее.
3.  **Перепроверяйте описание**: Убедитесь, что описание точно соответствует действиям кода.

**Пример использования**:

Вместо:
> "Функция получает данные из базы данных."

Следует использовать:
> "Функция извлекает данные из базы данных, используя SQL-запрос."