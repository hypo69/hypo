# Модуль `start_posting_my_groups.py`

## Обзор

Модуль предназначен для отправки рекламных объявлений в группы Facebook. Он использует `FacebookPromoter` для управления процессом постинга и поддерживает несколько рекламных кампаний.

## Оглавление

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Переменные](#переменные)
4. [Инициализация](#инициализация)
5. [Основной цикл](#основной-цикл)

## Импорты

В данном модуле используются следующие импорты:

- `header`: Предположительно, модуль для обработки заголовков. (Примечание: Детали модуля header не предоставлены)
- `copy`: Модуль для создания копий объектов.
- `src.webdriver.driver.Driver`, `src.webdriver.driver.Chrome`: Классы для управления веб-драйвером.
- `src.endpoints.advertisement.facebook.promoter.FacebookPromoter`: Класс для продвижения рекламы в Facebook.
- `src.logger.logger.logger`: Объект для ведения журнала.

## Переменные

- `d` (`Driver`): Экземпляр класса `Driver`, используется для управления браузером.
- `filenames` (`list`): Список имен файлов, содержащих информацию о группах.
- `campaigns` (`list`): Список названий рекламных кампаний.
- `promoter` (`FacebookPromoter`): Экземпляр класса `FacebookPromoter`, используемый для запуска рекламных кампаний.

## Инициализация

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list = ['my_managed_groups.json',]  

campaigns:list = ['brands',
                  'mom_and_baby',
                  'pain',
                  'sport_and_activity',
                  'house',
                  'bags_backpacks_suitcases',
                  'man']

promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = True)
```
Здесь происходит инициализация веб-драйвера, списка файлов и списка кампаний. Создается экземпляр `FacebookPromoter` для дальнейшей работы.

## Основной цикл

```python
try:
    while True:
        
        promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
        ...

        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

Этот цикл отвечает за бесконечный запуск рекламных кампаний.

- Внутри цикла вызывается метод `run_campaigns` у объекта `promoter` с копией списка кампаний и списком файлов.
- Обработка `KeyboardInterrupt` позволяет корректно завершить работу программы при нажатии `Ctrl+C`.

**Описание**: Бесконечный цикл, запускающий рекламные кампании в группах Facebook.

**Параметры**:\
Отсутствуют

**Возвращает**:\
Отсутствует

**Вызывает исключения**:\
- `KeyboardInterrupt`: Возникает при прерывании программы пользователем.