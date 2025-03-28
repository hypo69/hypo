# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `ksp.co.il`. Он наследует функциональность от родительского класса `Graber` и предоставляет методы для обработки различных полей на странице товара. Модуль также включает возможность переопределения стандартной логики обработки полей и использования декораторов для выполнения предварительных действий перед запросом к веб-драйверу.

## Содержание

- [Классы](#Классы)
    - [`Graber`](#Graber)
- [Функции](#Функции)
    - [`close_pop_up`](#close_pop_up)

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных о товарах с сайта `ksp.co.il`. Наследуется от `Graber` (`src.suppliers.graber`).

**Параметры**:
 - `driver` (`'Driver'`):  Экземпляр веб-драйвера.

**Методы**:

- `__init__`:
    
    **Описание**: Инициализация класса `Graber` и установка префикса поставщика. Если текущий URL содержит `/mob/`, то используются локаторы для мобильной версии сайта.
    
    **Параметры**:
        - `driver` (`'Driver'`): Экземпляр веб-драйвера.

## Функции

### `close_pop_up`

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
    
    
    **Параметры**:
        - `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

    
    **Возвращает**:
        - `Callable`: Декоратор, оборачивающий функцию.