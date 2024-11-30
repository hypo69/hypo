Как использовать модуль hypotez/src/endpoints/advertisement/facebook
========================================================================================

Описание
-------------------------
Модуль `hypotez/src/endpoints/advertisement/facebook` предоставляет инструменты для работы с рекламными объявлениями на Facebook. Он содержит классы для взаимодействия с API Facebook, определения полей и управления рекламными кампаниями.

Шаги выполнения
-------------------------
1. **Импортирование необходимых классов:** Модуль экспортирует классы `Facebook`, `FacebookFields`, `FacebookPromoter` и функцию `get_event_url`.  Необходимо импортировать нужные классы в свой код, например:

   .. code-block:: python

       from hypotez.src.endpoints.advertisement.facebook import Facebook, FacebookFields, FacebookPromoter, get_event_url


2. **Инициализация объекта Facebook:**  Для взаимодействия с Facebook API необходимо создать экземпляр класса `Facebook`.  Параметры инициализации зависят от способа аутентификации и подключения к API.

   .. code-block:: python

       # Пример инициализации (замените на ваши данные)
       facebook_instance = Facebook(access_token='YOUR_ACCESS_TOKEN')


3. **Работа с полями:** Класс `FacebookFields` предоставляет набор полей, которые могут быть использованы для запросов к API Facebook.  Используйте эти поля для точной настройки запросов.

   .. code-block:: python

       # Пример использования FacebookFields
       fields = FacebookFields()
       specific_fields = fields.get_fields(['name', 'description'])


4. **Управление рекламными кампаниями (Promoter):**  Класс `FacebookPromoter` позволяет управлять рекламными кампаниями. Используйте его методы для создания, редактирования или получения информации о кампаниях.

   .. code-block:: python

       # Пример использования FacebookPromoter (замените на ваши данные)
       promoter = FacebookPromoter(facebook_instance)
       campaign_data = promoter.get_campaign_details(campaign_id='YOUR_CAMPAIGN_ID')


5. **Получение URL события:**  Функция `get_event_url` возвращает URL-адрес события.

   .. code-block:: python

       event_url = get_event_url(event_id='YOUR_EVENT_ID')


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.facebook import Facebook, FacebookFields, FacebookPromoter, get_event_url

    # Замените на ваши данные
    access_token = 'YOUR_ACCESS_TOKEN'
    campaign_id = 'YOUR_CAMPAIGN_ID'
    event_id = 'YOUR_EVENT_ID'

    facebook_instance = Facebook(access_token=access_token)
    promoter = FacebookPromoter(facebook_instance)

    try:
        campaign_details = promoter.get_campaign_details(campaign_id=campaign_id)
        print(f"Подробности кампании: {campaign_details}")

        event_url = get_event_url(event_id=event_id)
        print(f"Ссылка на событие: {event_url}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")