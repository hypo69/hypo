Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет функцию `bully`, которая использует API OpenAI для получения ответа на запрос, связанный с примерами запугивания. Функция принимает на вход сообщение пользователя и массив сообщений для контекста чата.  Функция формирует запрос к API OpenAI, используя модель `gpt-3.5-turbo`, и возвращает обновлённый массив сообщений, включая полученный ответ от модели.  Код предполагает наличие установленной библиотеки `openai`.

Шаги выполнения
-------------------------
1. Импортирует необходимые модули `os` и `openai`.
2. Устанавливает значение переменной `openai.API_KEY` с ключом API OpenAI (ЗАМЕНИТЕ "YOUR_API_KEYS_OPENAI").
3. Определяет `system_prompt`, который содержит инструкцию для модели OpenAI о том, как генерировать примеры запугивания.
4. Определяет функцию `bully`:
    a. Принимает в качестве аргументов сообщение пользователя (`user_message`) и массив сообщений (`messages`).
    b. Добавляет сообщение пользователя к массиву сообщений.
    c. Использует `openai.ChatCompletion.create` для запроса к API OpenAI с заданной моделью и сообщениями.
    d. Добавляет ответ модели к массиву сообщений.
    e. Возвращает обновлённый массив сообщений.


Пример использования
-------------------------
.. code-block:: python

    import openai
    openai.API_KEY = "YOUR_API_KEYS_OPENAI"  # ЗАМЕНИТЕ НА СВОЙ КЛЮЧ!


    messages = [
        {"system": "user", "content": """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""}
    ]

    user_message = "Describe a situation where a student is targeted by other students."
    
    try:
        response = bully(user_message=user_message, messages=messages)
        # Обработка ответа
        print(response)
    except Exception as e:
        print(f"Ошибка: {e}")