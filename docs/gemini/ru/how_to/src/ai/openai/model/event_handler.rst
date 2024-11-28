Как использовать класс EventHandler
========================================================================================

Описание
-------------------------
Этот код определяет класс `EventHandler`, который обрабатывает события потокового ответа от OpenAI API.  Класс наследуется от `AssistantEventHandler` и переопределяет методы для обработки разных событий, таких как создание текста, изменение текста, создание запроса к инструменту и изменение запроса к инструменту.  Это позволяет собирать и выводить  информацию в потоковом режиме из ответов OpenAI.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:**
   Код импортирует необходимые модули, включая `AssistantEventHandler`, `OpenAI`,  типы данных для текстовых и инструментальных вызовов из `openai` библиотеки.

2. **Определение класса `EventHandler`:**
   Создается класс `EventHandler`, наследующийся от `AssistantEventHandler`.

3. **Переопределение методов для обработки событий:**
   - Метод `on_text_created` выводит сообщение "assistant > " перед новым текстом.
   - Метод `on_text_delta` добавляет новые символы текста.
   - Метод `on_tool_call_created` выводит тип инструмента.
   - Метод `on_tool_call_delta` обрабатывает изменения в запросе к инструменту. Если запрос — к  "code_interpreter",  и есть входные данные, выводит их. Затем, если есть выводы ("outputs"), выводит "output >" и отображает логи (если тип "logs").

4. **Использование класса (пример):**
   В примере кода показан общий способ использования этого класса: для создания объекта `EventHandler` и работы с ним, например, в методах API, обрабатывающих потоковый вывод.  Этот блок кода сам по себе не включает в себя вызов OpenAI API, но готовит класс для его использования.


Пример использования
-------------------------
.. code-block:: python

    from typing_extensions import override
    from openai import AssistantEventHandler, OpenAI
    from openai.types.beta.threads import Text, TextDelta
    from openai.types.beta.threads.runs import ToolCall, ToolCallDelta
    
    
    class EventHandler(AssistantEventHandler):
      @override
      def on_text_created(self, text: Text) -> None:
        print(f"\\nassistant > ", end="", flush=True)
      
      @override
      def on_text_delta(self, delta: TextDelta, snapshot: Text):
        print(delta.value, end="", flush=True)
      
      @override
      def on_tool_call_created(self, tool_call: ToolCall):
        print(f"\\nassistant > {tool_call.type}\\n", flush=True)
      
      @override
      def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
        if delta.type == "code_interpreter" and delta.code_interpreter:
          if delta.code_interpreter.input:
            print(delta.code_interpreter.input, end="", flush=True)
          if delta.code_interpreter.outputs:
            print(f"\\n\\noutput >", flush=True)
            for output in delta.code_interpreter.outputs:
              if output.type == "logs":
                print(f"\\n{output.logs}", flush=True)
    
    # Пример использования, который должен быть частью функции или класса, обрабатывающего поток:
    event_handler = EventHandler()
    # ... Здесь код вызова OpenAI API и передачи потока в event_handler ...