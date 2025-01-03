# Игра CHANGE (Кассовая программа)

## Обзор

Игра **CHANGE** представляет собой симуляцию работы кассира в магазине. Игрок вводит стоимость товара и сумму оплаты, а программа вычисляет и выводит сдачу, используя банкноты и монеты. Это помогает тренировать навыки работы с деньгами и понимание, как правильно выдавать сдачу.

## Содержание

- [Обзор](#обзор)
- [Пошаговая инструкция для реализации](#пошаговая-инструкция-для-реализации)
  - [1. Инициализация игры](#1-инициализация-игры)
  - [2. Основной цикл игры](#2-основной-цикл-игры)
  - [3. Подсчёт победителя](#3-подсчёт-победителя)
  - [4. Завершение игры](#4-завершение-игры)
- [Пример работы программы](#пример-работы-программы)
- [Возможные ограничения](#возможные-ограничения)
- [Реализация](#реализация)

## Пошаговая инструкция для реализации

### 1. Инициализация игры
- Программа запрашивает у игрока стоимость товара (от 0 до 100 долларов).
- Программа запрашивает сумму, которую игрок платит за товар.
- Программа вычисляет сдачу, которую нужно вернуть, используя банкноты и монеты (например, пятёрки, десятки, четверти, пенни и т.д.).

### 2. Основной цикл игры
   - **Ввод данных:**
     1. Игрок вводит стоимость товара (например, 4.59 доллара).
     2. Игрок вводит сумму оплаты (например, 10 долларов).
   - **Расчёт сдачи:**
     Программа вычисляет разницу между стоимостью товара и суммой оплаты. Например:
     - Стоимость товара: $4.59
     - Сумма оплаты: $10.00
     - Сдача: $5.41
   - **Вывод сдачи:**
     Программа выведет сдачу, разбив её на монеты и банкноты, например:
     ```
     Сдача: $5.41
     1 пятидолларовая купюра
     1 четверть
     1 никель
     1 пенни
     ```

### 3. Подсчёт победителя
- В игре нет победителя, так как основная цель — точный расчёт сдачи.

### 4. Завершение игры
- После расчёта сдачи программа предложит сыграть снова:
  ```
  Хотите сыграть снова? (да/нет)
  ```

## Пример работы программы

1. **Начало игры:**
   ```
   Добро пожаловать в игру CHANGE!
   Введите стоимость товара: 4.59
   Введите сумму оплаты: 10.00
   ```

2. **Расчёт сдачи:**
   ```
   Сдача: $5.41
   1 пятидолларовая купюра
   1 четверть
   1 никель
   1 пенни
   ```

3. **Завершение игры:**
   ```
   Хотите сыграть снова? (да/нет)
   > нет
   Спасибо за игру!
   ```

## Возможные ограничения

- Программа должна правильно вычислять сдачу для любых чисел, включая дробные суммы.
- Банкноты и монеты выбираются из ограниченного набора (например, пятёрки, десятки, четверти и т.д.).

## Реализация

Игра реализуется с использованием простых математических операций для вычисления сдачи и логики, которая разбивает сдачу на наибольшие возможные банкноты и монеты.