Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Данный код реализует отправку рекламных объявлений в группы Facebook.  Он использует драйвер для взаимодействия с веб-сайтом Facebook, загружает данные о группах из JSON-файлов и запускает кампании для указанных тематик.  Код обрабатывает возможные прерывания процесса.

Шаги выполнения
-------------------------
1. Импортирует необходимые модули: `header`, `Driver`, `Chrome`, `FacebookPromoter`, `logger`.  
2. Инициализирует веб-драйвер (`Driver`), загружая страницу Facebook.
3. Определяет список имен файлов JSON (`filenames`) и тематик (`campaigns`), для которых будут запущены кампании.
4. Создает экземпляр класса `FacebookPromoter`, передавая ему веб-драйвер и пути к файлам с данными о группах.  `no_video` устанавливается в `False`, что указывает на включение видео в рекламные кампании.
5. В блоке `try...except` запускает метод `run_campaigns` объекта `promoter` с переданным списком тематик. Метод `run_campaigns` отвечает за выполнение рекламных кампаний.
6. Если процесс прерывается с помощью `KeyboardInterrupt`,  выводится сообщение об остановке в логгер.

Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что необходимые модули и файлы импортированы и подготовлены.
    # Например, файлы 'katia_homepage.json' содержат информацию о целевых группах.
    import header
    from src.webdriver import Driver, Chrome
    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.logger import logger

    MODE = 'dev'

    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")

    filenames = ['katia_homepage.json']
    campaigns = ['sport_and_activity', 'bags_backpacks_suitcases', 'pain']
    promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)

    try:
        promoter.run_campaigns(campaigns)
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")