Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код реализует цикл для запуска рекламных кампаний на Facebook. Он использует драйвер для взаимодействия с веб-сайтом Facebook, определяет список групп и рекламных кампаний, а также параметры языка и валюты, и отправляет объявления в выбранные группы.  Код также содержит обработку ошибок и задержки для предотвращения перегрузки сервера.

Шаги выполнения
-------------------------
1. **Инициализация:** Импортируются необходимые библиотеки (header, random, time, copy, pathlib, gs, etc.). Определяются пути к файлам с группами и рекламными кампаниями для русского и иврита, а также категории для рекламы.
2. **`run_campaign` функция:** Эта функция отвечает за запуск конкретной рекламной кампании. Она принимает в качестве аргументов драйвер, имя рекламодателя, список кампаний, пути к файлам с группами, язык и валюту.  Функция создает экземпляр класса `FacebookPromoter`, передавая ему драйвер и имя рекламодателя. Затем она вызывает метод `run_campaigns`, передавая необходимые параметры кампании, включая список кампаний, пути к файлам групп, категории групп, язык и валюту.
3. **`campaign_cycle` функция:**  Эта функция отвечает за цикл управления запуском всех кампаний. Она создаёт копии списков путей к файлам групп и объявлений для русского и иврита. Затем функция создает список словарей `{language:currency}`, где указываются языки и валюты для рекламных кампаний. Функция перебирает пары язык-валюта. Для каждого языка определяется соответствующий список путей к файлам с группами. Определяются кампании, которые необходимо запустить для данного языка. Функция вызывает функцию `run_campaign` для запуска каждой кампании.
4. **`main` функция:** Эта функция служит основной точкой входа для запуска всего процесса. Она создаёт драйвер (например, Chrome), открывает страницу Facebook. Затем цикл `while True` запускает цикл `campaign_cycle`. Внутри цикла проверяется интервал времени и запускается `campaign_cycle`. После запуска цикла происходит логирование, случайная пауза для предотвращения перегрузки сервера и обработка прерывания.
5. **Обработка ошибок:**  Код содержит блок `try...except KeyboardInterrupt`, позволяющий корректно завершить программу при прерывании пользователя.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.facebook.start_sergey import campaign_cycle
    from src.webdriver import Chrome


    # Создаем экземпляр драйвера
    driver = Driver(Chrome)

    # Получаем доступ к странице Facebook.
    driver.get_url(r"https://facebook.com")

    # Запускаем цикл кампаний
    campaign_cycle(driver)