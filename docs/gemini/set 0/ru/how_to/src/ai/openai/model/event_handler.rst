Как использовать класс EventHandler для обработки событий в ответе OpenAI
=========================================================================================

Описание
-------------------------
Этот код определяет класс `EventHandler`, который используется для обработки событий, возвращаемых API OpenAI.  Он расширяет базовый класс `AssistantEventHandler` и переопределяет методы для обработки различных типов событий, таких как создание текста, изменения текста, создание вызовов инструментов и изменения вызовов инструментов.  В частности, этот класс выводит в консоль информацию о каждом событии, включая вводимые данные, если это код интерпретатора.


Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует необходимые модули `AssistantEventHandler`, `OpenAI`, `Text`, `TextDelta`, `ToolCall`, и `ToolCallDelta` из библиотеки `openai`.
2. **Определение класса `EventHandler`:** Определяется класс `EventHandler`, который наследуется от `AssistantEventHandler`.
3. **Переопределение методов:**  Методы `on_text_created`, `on_text_delta`, `on_tool_call_created`, и `on_tool_call_delta` переопределяются для обработки соответствующих событий.
4. **Вывод информации о событиях:** Методы выводят информацию в консоль, используя `print()`.  Для событий типа `on_text_created` и `on_text_delta` выводится текст. Для событий `on_tool_call_created` выводится тип инструмента.  Для событий `on_tool_call_delta` выводится информация о коде интерпретатора, в том числе входящие данные и выводы.
5. **Обработка выходов:** При обработке вызовов инструментов, если тип вызова равен "code_interpreter", и есть входящие данные, то они выводятся в консоль. Если есть выводы, то также выводятся сообщения о типе "logs".

Пример использования
-------------------------
.. code-block:: python

    import openai
    from hypotez.src.ai.openai.model.event_handler import EventHandler

    # Установите ваши ключи API OpenAI
    openai.api_key = "YOUR_OPENAI_API_KEY"


    # Создание экземпляра Event Handler
    event_handler = EventHandler()

    # Пример вызова модели OpenAI (необходимо подставить ваш запрос)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": "Напишите код на Python для вычисления факториала числа."}
        ],
        stream=True,  # Важно! Установите stream=True
        # ... другие параметры...
    )
    
    for chunk in response:
        if "choices" in chunk:
            choice = chunk["choices"][0]
            if "delta" in choice:
                delta = choice["delta"]
                event_handler.on_text_delta(delta["content"], None)