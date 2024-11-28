Как использовать этот блок кода
========================================================================================

Описание
-------------------------
Этот код предназначен для запуска рекламной кампании в группах Facebook. Он использует класс `FacebookPromoter` для управления процессом. Код подготавливает драйвер браузера, задает URL Facebook и загружает необходимые данные из файлов JSON. Затем он запускает рекламную кампанию, используя список целевых групп.

Шаги выполнения
-------------------------
1. Импортирует необходимые модули, включая драйвер браузера, класс `FacebookPromoter` и модуль логирования.
2. Инициализирует драйвер браузера Chrome и открывает страницу Facebook.
3. Определяет список путей к файлам JSON с данными для рекламных кампаний.
4. Определяет список целевых рекламных кампаний.
5. Создает экземпляр класса `FacebookPromoter`, передавая ему драйвер браузера, пути к файлам JSON и параметр, указывающий на отсутствие видео-рекламы (no_video = False).
6. Попытка запустить рекламные кампании с использованием метода `run_campaigns`.
7. Обрабатывает исключение `KeyboardInterrupt`, если пользователь прервал выполнение, записывая сообщение в лог.

Пример использования
-------------------------
.. code-block:: python

    # Предполагается, что необходимые модули (header, Driver, Chrome, FacebookPromoter, logger) уже импортированы.
    MODE = 'dev'  # или другое значение

    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")

    filenames = ['katia_homepage.json',]
    campaigns = ['sport_and_activity', 'bags_backpacks_suitcases', 'pain', 'brands', 'mom_and_baby', 'house']

    promoter = FacebookPromoter(d, group_file_paths=filenames, no_video=False)

    try:
        promoter.run_campaigns(campaigns)
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")