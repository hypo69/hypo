# Модуль `hypotez/src/endpoints/advertisement/facebook/start_posting.py`

## Обзор

Модуль `start_posting.py` отвечает за запуск рекламных кампаний в Facebook для различных групп. Он использует класс `FacebookPromoter` для автоматической публикации объявлений, а также управляет файлами с настройками групп и кампаний. Модуль использует драйвер для работы с браузером Facebook.

## Оглавление

* [Модуль `start_posting.py`](#модуль-start_postingpy)
* [Глобальные переменные](#глобальные-переменные)
* [Функции](#функции)

## Глобальные переменные

```python
MODE = 'dev'
```

Переменная `MODE` хранит режим работы (в данном случае, 'dev').

```python
filenames:list[str] = [
                        "usa.json",
                        "he_ils.json",
                        "ru_ils.json",
                        "katia_homepage.json",
                        "my_managed_groups.json",
          
                        ]
```

Список путей к файлам с настройками групп.

```python
excluded_filenames:list[str] = ["my_managed_groups.json",                        
                                "ru_usd.json",
                            "ger_en_eur.json",  ]
```

Список путей к файлам, которые нужно исключить из обработки.


```python
campaigns:list = [
                  'brands',
                  'mom_and_baby',
                  'pain',
                  'sport_and_activity',
                  'house',
                  'bags_backpacks_suitcases',
                  'man'
]
```

Список рекламных кампаний.

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

Инициализация драйвера браузера и загрузка страницы Facebook.

```python
promoter:FacebookPromoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)
```

Создание объекта `FacebookPromoter` для работы с рекламными кампаниями.


## Функции

Нет явных функций в данном файле.  Код содержит цикл, использующий `promoter.run_campaigns()`.

## Обработка исключений

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

При возникновении `KeyboardInterrupt` (например, при прерывании процесса пользователем), логируется сообщение и завершается работа.

**Замечание**: Данный код предполагает существование класса `FacebookPromoter`, `Driver` и `Chrome`, которые не определены в предоставленном коде. Для полной документации требуется описание этих классов и функций.