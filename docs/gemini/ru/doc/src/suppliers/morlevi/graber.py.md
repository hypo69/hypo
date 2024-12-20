# Модуль `src.suppliers.morlevi.graber`

## Обзор

Модуль `src.suppliers.morlevi.graber` представляет собой класс `Graber`, предназначенный для сбора данных о товарах с сайта `morlevi.co.il`. Класс наследуется от родительского класса `Graber` и переопределяет методы для обработки полей товара. 
Модуль использует декораторы для выполнения предварительных действий перед запросом к веб-драйверу.

## Содержание

1.  [Обзор](#обзор)
2.  [Классы](#классы)
    *   [`Graber`](#класс-graber)
3.  [Функции](#функции)
    *   [close_pop_up](#функция-close_pop_up)

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных о товарах с сайта Morlevi.

**Родительский класс**: `src.suppliers.graber.Graber`

**Методы**:

- `__init__`: Инициализирует класс, устанавливая префикс поставщика и вызывая конструктор родительского класса.
    -   **Параметры**:
        -   `driver` (`Driver`): Экземпляр веб-драйвера.
-   `local_saved_image`: Загружает и сохраняет изображение товара локально. 
    -   **Параметры**:
        -   `value` (`Any`, optional): Дополнительное значение, которое можно передать через словарь `kwargs`. По умолчанию `None`.
    -   **Возвращает**:
        -   `bool | None`: `True` в случае успешного сохранения, `None` в случае ошибки.
    -   **Вызывает исключения**:
        -   `Exception`: В случае ошибки сохранения изображения.

## Функции

### `close_pop_up`

**Описание**: Декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
    - `value` (`Any`, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
    - `Callable`: Декоратор, который оборачивает функцию.