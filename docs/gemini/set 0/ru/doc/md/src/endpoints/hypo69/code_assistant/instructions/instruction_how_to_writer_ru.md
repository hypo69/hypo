# Инструкции по генерации документации к коду

## Обзор

Данный документ содержит инструкции по написанию документации в формате Markdown для Python-кода.  Документация должна быть подробной, структурированной и легко читаемой.

## Инструкции

### Анализ кода

Первым шагом является тщательный анализ входного Python-кода.  Важно понять логику и последовательность действий, выполняемых кодом.  Определите, что именно делает код, какие данные принимает и что возвращает.

### Составление пошаговой инструкции

После анализа кода, составьте пошаговую инструкцию, описывающую его работу.

* **Описание:** Дайте краткое и понятное описание того, что делает этот фрагмент кода.
* **Шаги выполнения:** Опишите последовательность действий в коде. Используйте простые и понятные глаголы.  Например, "получает данные", "валидирует входные параметры", "вычисляет результат".  Избегайте расплывчатых формулировок.
* **Пример использования:** Приведите пример того, как использовать данный фрагмент кода в проекте.  Пример должен быть сконкретизирован и показывать использование в контексте.  В примере нужно указать входные данные и ожидаемый результат.


### Форматирование документации

Документация должна быть структурирована с использованием `reStructuredText` (RST) синтаксиса:

```rst
Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
[Объяснение, что делает код.]

Шаги выполнения
-------------------------
1. [Описание первого шага.]
2. [Описание второго шага.]
3. [Продолжай по необходимости...]

Пример использования
-------------------------
.. code-block:: python

    [Пример использования кода]
```

**Важно:**  Замените [ ] на фактические данные.


### Пример

```rst
Как использовать функцию вычисления факториала
=========================================================================================

Описание
-------------------------
Функция вычисляет факториал целого числа.

Шаги выполнения
-------------------------
1. Функция принимает целое число (n) как входной параметр.
2. Проверяет, является ли входное число целым и положительным. Если нет, возвращает ошибку.
3. Использует цикл `for` для вычисления факториала.
4. Возвращает вычисленный факториал.

Пример использования
-------------------------
.. code-block:: python

    from your_module import factorial_function

    result = factorial_function(5)
    print(result)  # Выведет 120
```

### Избегайте расплывчатых терминов

Избегайте расплывчатых формулировок, таких как "получаем", "делаем". Используйте точные глаголы и конкретные действия, например: "вычисляет", "валидирует", "отправляет".

### Обработка исключений

Если в коде используются блоки `try...except`, опишите возможные исключения и действия, выполняемые при их возникновении.

## Дополнительные советы

* Используйте четкие и краткие описания.
* Структурируйте документацию по уровням: модули, классы, функции, методы.
* Подробно описывайте параметры функций и методы.
* При необходимости используйте примеры, иллюстрирующие работу кода.