# Модуль src.endpoints.advertisement.facebook.start_event

## Обзор

Модуль предназначен для автоматической отправки мероприятий (events) в группы Facebook. Он использует веб-драйвер для взаимодействия с Facebook и выполняет задачи по продвижению контента в различных группах.

## Подробнее

Этот модуль является частью системы автоматизированного продвижения в Facebook. Он использует список файлов с данными о группах и запускает мероприятия (events) в этих группах. Модуль предназначен для работы в фоновом режиме и периодически повторяет запуск мероприятий.

## Функции

### `Нет функций`

В данном модуле нет отдельных функций, но есть основной блок кода, который выполняет следующие действия:

1.  **Инициализация**:
    *   Импортируются необходимые модули и классы.
    *   Инициализируется веб-драйвер (Chrome).
    *   Определяются списки файлов с данными о группах и список названий мероприятий.
    *   Создается экземпляр класса `FacebookPromoter`.
2.  **Запуск цикла**:
    *   В бесконечном цикле запускаются мероприятия с использованием метода `run_events` класса `FacebookPromoter`.
    *   Выполняется ожидание в течение 7200 секунд (2 часа) перед следующим запуском.
3.  **Обработка прерывания**:
    *   При получении сигнала прерывания (KeyboardInterrupt) цикл завершается, и в лог записывается сообщение о прерывании продвижения.

## Классы

### `FacebookPromoter`

**Описание**: Класс `FacebookPromoter` отвечает за выполнение задач по продвижению контента в группах Facebook. Он использует веб-драйвер для взаимодействия с Facebook и выполняет действия по отправке мероприятий в группы.

**Принцип работы**:

1.  Класс инициализируется с веб-драйвером и списком файлов с данными о группах.
2.  Метод `run_events` выполняет отправку мероприятий в указанные группы.

Подробный разбор работы класса `FacebookPromoter` и его методов выходит за рамки данного модуля, так как он определен в другом файле (`src.endpoints.advertisement.facebook`).

**Методы**:

*   `run_events`: Выполняет отправку мероприятий в группы Facebook.

**Параметры**:

*   `d` (Driver): Экземпляр веб-драйвера.
*   `group_file_paths` (list\[str]): Список путей к файлам с данными о группах.
*   `no_video` (bool): Флаг, указывающий на отсутствие видео в продвигаемом контенте.

## Переменные

### `d`

**Описание**: Экземпляр класса `Driver`, используемый для управления браузером Chrome.

### `filenames`

**Описание**: Список имен файлов, содержащих информацию о группах, в которые будет осуществляться отправка мероприятий.

### `excluded_filenames`

**Описание**: Список имен файлов, которые следует исключить из списка `filenames` при отправке мероприятий.

### `events_names`

**Описание**: Список названий мероприятий, которые будут отправляться в группы.

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter`, используемый для выполнения задач по продвижению в Facebook.

## Как работает модуль

1.  **Инициализация**:
    *   Создается экземпляр веб-драйвера Chrome.
    *   Загружаются списки файлов с данными о группах и названиями мероприятий.
    *   Создается экземпляр класса `FacebookPromoter`.
2.  **Основной цикл**:
    *   В бесконечном цикле вызывается метод `run_events` класса `FacebookPromoter` для отправки мероприятий в группы.
    *   После каждой итерации цикла происходит ожидание в течение 2 часов.
3.  **Обработка прерывания**:
    *   При получении сигнала прерывания цикл завершается.

```text
A: Инициализация веб-драйвера, списков файлов и FacebookPromoter
│
B: Запуск бесконечного цикла
│
C: Вызов promoter.run_events для отправки мероприятий
│
D: Ожидание в течение 2 часов
│
E: Возврат к B, если не было прерывания
│
F: Завершение цикла при получении KeyboardInterrupt

A
↓
B
│
→ C
↓
D
│
E ─↑
│
F
```

## Примеры

### Запуск модуля

Для запуска модуля необходимо выполнить данный Python-файл. Убедитесь, что у вас установлены все необходимые зависимости, включая веб-драйвер Chrome и модуль `src.endpoints.advertisement.facebook`.

```python
# Пример запуска модуля
# python src/endpoints/advertisement/facebook/start_event.py
```

### Пример конфигурации

Файлы конфигурации (например, `my_managed_groups.json`, `usa.json` и т.д.) должны содержать информацию о группах, в которые будет осуществляться отправка мероприятий. Формат этих файлов определяется логикой класса `FacebookPromoter`.