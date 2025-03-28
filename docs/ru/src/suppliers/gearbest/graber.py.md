# Модуль `src.suppliers.gearbest.graber`

## Обзор

Модуль содержит класс `Graber`, который предназначен для сбора данных о товарах с сайта `gearbest.com`. Класс наследуется от `src.suppliers.graber.Graber` и переопределяет некоторые его методы для специфической обработки полей. Для предварительных действий перед отправкой запроса к вебдрайверу используется декоратор.

## Оглавление

1. [Классы](#Классы)
    - [Graber](#Graber)
2. [Функции](#Функции)

## Классы

### `Graber`

**Описание**: Класс для сбора данных о товарах с сайта `gearbest.com`. Наследует функциональность класса `Graber` из модуля `src.suppliers.graber`.

**Методы**:

- `__init__`: Инициализирует класс, устанавливает префикс поставщика и настраивает контекст.

#### `__init__`

**Описание**: Инициализирует класс `Graber`. Устанавливает префикс поставщика как `etzmaleh`, вызывает конструктор родительского класса, и устанавливает `Context.locator_for_decorator` в `None`.

**Параметры**:
- `driver` (`Driver`): Экземпляр вебдрайвера для взаимодействия с сайтом.

## Функции

### `close_pop_up`
 
**Описание**:
Декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` (`Any`, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.