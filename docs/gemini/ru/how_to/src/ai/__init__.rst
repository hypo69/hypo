Как использовать этот модуль src.ai
========================================================================================

Описание
-------------------------
Этот модуль является интерфейсом для моделей ИИ. Он предоставляет доступ к различным моделям, таким как Google Generative AI и OpenAI.  Модуль определяет константу MODE, которая указывает на режим работы (например, 'dev' или 'prod').  Импортирует классы `GoogleGenerativeAI` и `OpenAIModel` из соответствующих подмодулей.

Шаги выполнения
-------------------------
1. Импортируйте необходимые классы моделей ИИ из соответствующих подмодулей:
   ```python
   from .gemini import GoogleGenerativeAI
   from .openai import OpenAIModel
   ```
2.  Выберите модель ИИ, с которой хотите взаимодействовать:
   ```python
   google_model = GoogleGenerativeAI()
   openai_model = OpenAIModel()
   ```
3.  Используйте выбранный экземпляр класса для выполнения запросов к модели ИИ.  Подробное описание методов класса доступно в документации к подмодулям `gemini` и `openai`.

Пример использования
-------------------------
.. code-block:: python

    from .gemini import GoogleGenerativeAI
    from .openai import OpenAIModel
    
    # Создание экземпляра модели Google Generative AI
    google_model = GoogleGenerativeAI()
    
    # Пример использования метода (подробнее о методах в документации к gemini.py):
    try:
        response = google_model.generate_text(prompt="Напишите стихотворение о лете.")
        print(response)
    except Exception as e:
        print(f"Ошибка при использовании модели: {e}")
    
    # Создание экземпляра модели OpenAI
    openai_model = OpenAIModel()

    # Пример использования метода (подробнее о методах в документации к openai.py):
    try:
        response = openai_model.generate_completion(prompt="Напишите код на Python для...")
        print(response)
    except Exception as e:
        print(f"Ошибка при использовании модели: {e}")