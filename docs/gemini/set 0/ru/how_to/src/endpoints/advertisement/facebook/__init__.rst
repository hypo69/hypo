Как использовать модуль src.endpoints.advertisement.facebook
========================================================================================

Описание
-------------------------
Модуль `src.endpoints.advertisement.facebook` предоставляет инструменты для работы с рекламной платформой Facebook.  Он содержит классы для взаимодействия с API Facebook, определения полей данных и работы с промоутерами.  Константа `MODE` определяет режим работы (в данном случае 'dev').

Шаги выполнения
-------------------------
1. **Импорт необходимых классов:** Модуль импортирует классы `Facebook`, `FacebookFields`, `FacebookPromoter`, и функцию `get_event_url` из подмодулей внутри `src.endpoints.advertisement.facebook`.

2. **Инициализация и использование:**  Для работы с API Facebook необходимо создать экземпляр класса `Facebook`.  В зависимости от задач, можно использовать классы `FacebookFields` для определения полей, `FacebookPromoter` для работы с промоутерами.

3. **Использование функции `get_event_url`:** Функция `get_event_url` вероятно возвращает URL-адрес определенного события. Для ее использования, нужно передать необходимые аргументы.


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.facebook import Facebook, FacebookFields, FacebookPromoter, get_event_url

    # Инициализация Facebook
    facebook_instance = Facebook()

    # Пример использования FacebookFields
    facebook_fields = FacebookFields()
    fields_list = facebook_fields.get_required_fields()
    print(fields_list)

    # Пример использования FacebookPromoter (предполагается, что есть объект promoter)
    promoter_instance = FacebookPromoter()
    event_url = get_event_url(promoter_instance.event_id)  #  Пример вызова, предполагая, что у объекта FacebookPromoter есть атрибут event_id
    print(f"Ссылка на событие: {event_url}")

    # ... другие операции с Facebook API ...