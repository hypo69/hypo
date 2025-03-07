# Модуль `src.suppliers.amazon.graber`

## Обзор

Модуль содержит класс `Graber`, предназначенный для сбора данных о товарах со страницы `amazon.com`. Этот класс расширяет базовый класс `Graber` и предоставляет функциональность для обработки полей товара, включая возможность переопределения стандартной логики обработки для конкретных полей. Модуль также использует декораторы для предварительной обработки запросов к веб-драйверу.

## Оглавление
1. [Классы](#Классы)
   - [`Graber`](#Graber)
2. [Функции](#Функции)
   - [`close_pop_up`](#close_pop_up)

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта Amazon. Расширяет класс `Graber` и предоставляет специализированную функциональность для работы с веб-страницами Amazon.

**Методы**:

- `__init__`: Инициализация класса сбора полей товара.

    **Описание**: Инициализирует экземпляр класса `Graber` с заданными параметрами.

    **Параметры**:
        - `driver` (`Driver`): Экземпляр веб-драйвера для взаимодействия с браузером.

    **Возвращает**:
        - `None`: Метод не возвращает значения.

## Функции

### `close_pop_up`

**Описание**: Декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
    - `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
    - `Callable`: Декоратор, оборачивающий функцию.

**Вызывает исключения**:
    - `ExecuteLocatorException`: Если происходит ошибка при выполнении локатора.