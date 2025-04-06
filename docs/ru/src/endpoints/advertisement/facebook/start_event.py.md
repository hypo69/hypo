# Модуль для отправки мероприятий в группы Facebook

## Обзор

Модуль `src.endpoints.advertisement.facebook.start_event` предназначен для автоматической отправки рекламных мероприятий в различные группы Facebook. Он использует веб-драйвер для взаимодействия с сайтом Facebook и выполняет заданные действия, такие как публикация событий в группах.

## Подробней

Этот модуль является частью системы для автоматизации маркетинговых кампаний в Facebook. Он включает в себя функциональность для чтения конфигурационных файлов с информацией о группах, выполнения входа в систему и публикации событий. Модуль предназначен для работы в режиме реального времени, выполняя отправку мероприятий по расписанию.

## Классы

В данном коде класс не описан. Используется класс `FacebookPromoter` из модуля `src.endpoints.advertisement.facebook`

## Функции

В данном коде функции не описаны.

## Переменные

- `filenames (list[str])`: Список имен файлов, содержащих информацию о группах Facebook, в которые будут отправляться мероприятия.
- `excluded_filenames (list[str])`: Список имен файлов, которые следует исключить из обработки.
- `events_names (list)`: Список имен мероприятий для запуска.
- `promoter (FacebookPromoter)`: Экземпляр класса `FacebookPromoter`, используемый для выполнения операций по продвижению в Facebook.
- `d (Driver)`: Инстанс класса `Driver` для управления браузером. В данном случае используется браузер Chrome.

## Код

### Создание инстанса драйвера
```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

Создается инстанс драйвера Chrome с использованием класса `Driver` из модуля `src.webdriver.driver`. После этого происходит переход по URL-адресу "https://facebook.com".

### Инициализация списков файлов и имен событий
```python
filenames:list[str] = [ "my_managed_groups.json",
                        "usa.json",
                        "he_il.json",
                        "ru_il.json",
                        "katia_homepage.json",
                        
                        "ru_usd.json",
                        "ger_en_eur.json",            
                        ]
excluded_filenames:list[str] = ["my_managed_groups.json",]
events_names:list = ["choice_day_01_10"]
```

Здесь определяются списки файлов, содержащих информацию о группах, список исключенных файлов и список имен событий, которые будут запускаться.

### Создание инстанса `FacebookPromoter`
```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

Создается экземпляр класса `FacebookPromoter`, который будет использоваться для запуска мероприятий в Facebook. Ему передается драйвер `d`, список файлов с информацией о группах `filenames` и флаг `no_video`, указывающий на отсутствие видео в мероприятиях.

### Основной цикл отправки мероприятий
```python
try:
    while True:
        logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
        time.sleep(7200)
        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

Основной цикл программы. Он выполняется до тех пор, пока не будет прерван пользователем (нажатием Ctrl+C). Внутри цикла выполняются следующие действия:

1. Логируется сообщение о пробуждении (`logger.debug`).
2. Вызывается метод `run_events` экземпляра `promoter` для запуска мероприятий в группах Facebook.
3. Логируется сообщение о переходе в режим ожидания (`logger.debug`).
4. Программа засыпает на 7200 секунд (2 часа).

Если пользователь прерывает выполнение программы нажатием Ctrl+C, то возбуждается исключение `KeyboardInterrupt`, которое перехватывается блоком `except`. В этом случае в лог выводится сообщение о прерывании продвижения кампании (`logger.info`).

## Как работает код:

1.  **Инициализация**:
    - Создается экземпляр веб-драйвера Chrome (`d`).
    - Определяются списки файлов (`filenames`, `excluded_filenames`) и имен событий (`events_names`).
    - Создается экземпляр класса `FacebookPromoter` (`promoter`) с использованием веб-драйвера и списка файлов.

2.  **Цикл отправки мероприятий**:
    - В бесконечном цикле:
        - Вызывается метод `run_events` класса `FacebookPromoter` для отправки мероприятий в группы Facebook.
        - Программа засыпает на 7200 секунд (2 часа).

3.  **Обработка прерывания**:
    - При получении сигнала прерывания (например, нажатие Ctrl+C):
        - Выводится сообщение в лог о прерывании продвижения кампании.

## ASCII flowchart работы кода:

```
A[Инициализация: драйвер, списки, promoter]
|
B[Основной цикл: отправка мероприятий]
|
C[Запуск promoter.run_events()]
|
D[Ожидание 7200 секунд]
|
E[Повтор цикла]
|
F[Прерывание: завершение программы]
```

**Блоки:**

- **A**: Инициализация основных компонентов программы: драйвера, списков файлов и экземпляра класса `FacebookPromoter`.
- **B**: Основной цикл, в котором происходит отправка мероприятий.
- **C**: Запуск метода `run_events` класса `FacebookPromoter` для отправки мероприятий.
- **D**: Ожидание в течение 7200 секунд (2 часа) перед повторной отправкой мероприятий.
- **E**: Возврат к началу основного цикла для повторной отправки мероприятий.
- **F**: Прерывание выполнения программы при получении сигнала прерывания (например, нажатие Ctrl+C).

## Примеры

### Запуск отправки мероприятий с использованием указанных файлов и событий:

```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
promoter.run_events(events_names = events_names, group_file_paths = filenames)
```

### Обработка прерывания кампании:

```python
try:
    while True:
        promoter.run_events(events_names = events_names, group_file_paths = filenames)
        time.sleep(7200)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")