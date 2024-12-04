Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код запускает процесс отправки рекламных объявлений в группы Facebook. Он загружает данные из файлов JSON, конфигурирует рекламную кампанию и запускает цикл для постепенной отправки объявлений. Код обрабатывает исключение KeyboardInterrupt для корректного завершения.

Шаги выполнения
-------------------------
1. **Импортирует необходимые библиотеки:** Модули `math`, `time`, `copy`, драйвер WebDriver (`Driver`, `Chrome`), класс `FacebookPromoter`, и логгер `logger`.
2. **Инициализирует WebDriver:** Открывает браузер Chrome и переходит на страницу Facebook.
3. **Определяет файлы и кампании:** Создает списки имен файлов JSON с данными для рекламных объявлений (`filenames`) и список исключаемых файлов (`excluded_filenames`), а также список названий рекламных кампаний (`campaigns`).
4. **Инициализирует `FacebookPromoter`:** Создает экземпляр класса `FacebookPromoter`, передавая ему инициализированный WebDriver (`d`), пути к файлам с данными о группах (`filenames`) и параметр `no_video` (по умолчанию `True`).
5. **Запускает цикл отправки:** В цикле `while True` функция `promoter.run_campaigns` запускает рекламные кампании, используя скопированные данные из списка `campaigns` и списков файлов `filenames`.  После каждого запуска цикла происходит пауза на 180 секунд.
6. **Обрабатывает исключение:** Блок `try...except KeyboardInterrupt` позволяет пользователю прервать цикл отправки объявлений через комбинацию клавиш Ctrl+C, в таком случае генерируется предупреждение в лог-файл.

Пример использования
-------------------------
.. code-block:: python

    # Допустим, у вас есть необходимые файлы JSON в директории 'data'
    # и класс FacebookPromoter реализован
    import copy
    from src.webdriver import Driver, Chrome
    from src.endpoints.advertisement.facebook import FacebookPromoter
    from src.logger import logger


    filenames = ["usa.json", "he_ils.json"]
    campaigns = ['brands', 'mom_and_baby']
    
    d = Driver(Chrome)
    d.get_url(r"https://facebook.com")
    
    # Инициализация FacebookPromoter (подставьте реальные пути к файлам)
    promoter = FacebookPromoter(d, group_file_paths=filenames, no_video = True)

    try:
        while True:
            promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
            print(f"Going sleep {time.localtime}")
            time.sleep(180)
    except KeyboardInterrupt:
        logger.info("Campaign promotion interrupted.")