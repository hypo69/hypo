# Модуль `src.endpoints.advertisement.facebook.start_event`

## Обзор

Модуль предназначен для отправки мероприятий в группы Facebook. Он использует веб-драйвер для автоматизации действий и загружает данные о группах из файлов JSON. Модуль запускает продвижение мероприятий в цикле, с определенным интервалом.

## Оглавление

1. [Обзор](#обзор)
2. [Переменные](#переменные)
3. [Импорты](#импорты)
4. [Основной цикл](#основной-цикл)
5. [Обработка исключений](#обработка-исключений)

## Переменные

### `filenames`

**Описание**: Список имен файлов JSON, содержащих данные о группах для продвижения.
**Тип**: `list[str]`
**Пример**:
```python
filenames:list[str] = [ "my_managed_groups.json",
                        "usa.json",
                        "he_il.json",
                        "ru_il.json",
                        "katia_homepage.json",
                        
                        "ru_usd.json",
                        "ger_en_eur.json",            
                        ]
```

### `excluded_filenames`

**Описание**: Список имен файлов JSON, которые нужно исключить из продвижения.
**Тип**: `list[str]`
**Пример**:
```python
excluded_filenames:list[str] = ["my_managed_groups.json",]
```

### `events_names`

**Описание**: Список имен мероприятий для продвижения.
**Тип**: `list`
**Пример**:
```python
events_names:list = ["choice_day_01_10"]
```

### `d`

**Описание**: Экземпляр веб-драйвера `Driver`, используемый для управления браузером Chrome.
**Тип**: `Driver`
**Пример**:
```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

### `promoter`

**Описание**: Экземпляр класса `FacebookPromoter`, используемый для продвижения мероприятий.
**Тип**: `FacebookPromoter`
**Пример**:
```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

## Импорты

Модуль импортирует следующие библиотеки:
- `math.log`: используется для математических операций. (хотя в коде не используется)
- `header`: (не используется)
- `time`: используется для работы со временем.
- `src.utils.jjson.j_loads`: используется для загрузки JSON данных.
- `src.webdriver.driver.Driver`, `src.webdriver.driver.Chrome`: используются для управления веб-браузером.
- `src.endpoints.advertisement.facebook.FacebookPromoter`: класс для продвижения мероприятий в Facebook.
- `src.logger.logger.logger`: используется для логирования событий.

## Основной цикл

Основной цикл модуля выполняется бесконечно и состоит из следующих шагов:

1. **Логирование начала:** Записывает в лог сообщение о начале работы (`waikig up`) с указанием текущего времени.

2. **Запуск продвижения:** Вызывает метод `run_events` экземпляра `promoter` для запуска продвижения мероприятий, передавая в него список имен мероприятий (`events_names`) и список файлов с данными о группах (`filenames`).

   ```python
   promoter.run_events(events_names = events_names, group_file_paths = filenames)
   ```

3. **Логирование завершения:** Записывает в лог сообщение о завершении работы (`going to sleep at`) с указанием текущего времени.

4. **Пауза:** Приостанавливает выполнение программы на 7200 секунд (2 часа).

   ```python
   time.sleep(7200)
   ```

## Обработка исключений

В модуле используется блок `try...except` для перехвата исключения `KeyboardInterrupt`, которое возникает при прерывании программы пользователем (например, нажатием `Ctrl+C`).
Если исключение возникает, в лог записывается сообщение о прерывании продвижения кампании.

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