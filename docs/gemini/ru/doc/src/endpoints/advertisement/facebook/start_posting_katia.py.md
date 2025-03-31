# Модуль для отправки рекламных объявлений в Facebook (Katia)

## Обзор

Модуль `start_posting_katia.py` предназначен для автоматизированной отправки рекламных объявлений в группы Facebook. Он использует веб-драйвер для управления браузером и выполняет сценарии продвижения, определенные в файлах конфигурации.

## Подробнее

Этот модуль является частью системы автоматизации маркетинга в Facebook. Он использует класс `FacebookPromoter` для управления процессом публикации объявлений в различных группах. Конфигурации групп и кампаний загружаются из файлов JSON.

## Классы

### `FacebookPromoter`

**Описание**: Класс, управляющий процессом публикации рекламных объявлений в группы Facebook.

**Как работает класс**:
Класс `FacebookPromoter` инициализируется драйвером веб-браузера, списком файлов конфигурации групп и флагом, указывающим на наличие видео в объявлениях. Он предоставляет методы для запуска и управления рекламными кампаниями.

**Методы**:
- `run_campaigns`: Запускает рекламные кампании на основе предоставленного списка кампаний.

## Функции

В данном коде функции отсутствуют. Основная логика реализована через класс `FacebookPromoter`.

## Переменные

- `d`: Экземпляр класса `Driver`, используемый для управления веб-браузером.
- `filenames`: Список файлов, содержащих информацию о группах Facebook для публикации объявлений.
- `campaigns`: Список названий рекламных кампаний, которые необходимо запустить.
- `promoter`: Экземпляр класса `FacebookPromoter`, отвечающий за продвижение рекламных кампаний.

## Использование

1.  Инициализация веб-драйвера:

```python
d = Driver(Chrome)
d.get_url(r"https://facebook.com")
```

2.  Определение списка файлов конфигурации и кампаний:

```python
filenames:list = ['katia_homepage.json',]
campaigns:list = [ 'sport_and_activity',
                  'bags_backpacks_suitcases',
                    'pain',
                    'brands',
                    'mom_and_baby',
                    'house',
                ]
```

3.  Создание экземпляра класса `FacebookPromoter`:

```python
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)
```

4.  Запуск рекламных кампаний:

```python
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

## Обработка исключений

В коде предусмотрена обработка исключения `KeyboardInterrupt`, которое возникает при прерывании выполнения программы пользователем (например, нажатием Ctrl+C).

```python
try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")
```

## Логирование

В случае прерывания кампании, в лог записывается информационное сообщение.

```python
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")