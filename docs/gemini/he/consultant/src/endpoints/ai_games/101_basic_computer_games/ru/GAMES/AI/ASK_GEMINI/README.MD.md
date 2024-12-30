# Анализ кода модуля `ask_gemini_ru`

**Качество кода**
<br>
- **Соответствие требованиям к формату кода (1-10): 9**
    -   **Преимущества:**
        -   Код написан на Python и использует библиотеку `google.generativeai` для взаимодействия с моделями Google AI.
        -   Реализован класс `GoogleGenerativeAI`, который инкапсулирует логику работы с моделью.
        -   Используется метод `ask` для отправки запросов и получения ответов.
        -   Присутствуют комментарии, объясняющие работу кода.
        -   Приведен пример использования кода с запросом API ключа и выводом результата.
        -   Структура кода понятна и соответствует поставленной задаче.
    -   **Недостатки:**
        -   Отсутствует обработка ошибок в методе `__init__`.
        -   Нет проверок на корректность введенного API ключа.
        -   Используется стандартный блок `try-except` в методе `ask`.
        -   Нет docstring для модуля, класса и методов.

**Рекомендации по улучшению**
<br>
1.  **Добавить reStructuredText (RST) комментарии**: Добавить docstring в формате RST для модуля, класса `GoogleGenerativeAI` и его методов, включая описание параметров и возвращаемых значений.
2.  **Использовать logger**: Вместо стандартного блока `try-except` в методе `ask` использовать `logger.error` для записи ошибок. Импортировать `logger` из `src.logger.logger`.
3.  **Обработка ошибок в `__init__`**: Добавить обработку ошибок при инициализации модели, например, при неверном API ключе.
4.  **Проверка API ключа**: Добавить проверку на корректность введенного API ключа.
5.  **Импорты**: Проверить и добавить недостающие импорты.

**Улучшенный код**

```python
"""
Модуль для взаимодействия с моделями Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который позволяет взаимодействовать с моделями
Google Gemini, такими как "gemini-1.5-flash-8b", "gemini-2-13b", "gemini-3-20b".

Пример использования
--------------------

Пример создания экземпляра класса `GoogleGenerativeAI` и отправки запроса:

.. code-block:: python

    api_key = "YOUR_API_KEY"
    model = GoogleGenerativeAI(api_key=api_key, model_name="gemini-2-13b")
    response = model.ask("Как улучшить мой код?")
    print(response)
"""
import google.generativeai as genai  # Импорт библиотеки google.generativeai
from src.logger.logger import logger  # Импорт логгера из src.logger.logger


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к генеративной модели.
    :type api_key: str
    :param model_name: Название модели для использования. По умолчанию "gemini-2.0-flash-exp".
    :type model_name: str, optional
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]  # Список доступных моделей

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования. По умолчанию "gemini-2.0-flash-exp".
        :type model_name: str, optional
        :raises ValueError: Если api_key не указан или некорректен.
        """
        if not api_key:  # Проверка наличия API ключа
            raise ValueError("API ключ не может быть пустым.") #  Вызов исключения если api_key не указан
        self.api_key = api_key  #  Сохранение ключа API
        self.model_name = model_name  # Сохранение названия модели
        try:
             genai.configure(api_key=self.api_key)  # Настройка API ключа
             self.model = genai.GenerativeModel(model_name=self.model_name)  # Инициализация модели
        except Exception as ex:
            logger.error(f"Ошибка инициализации модели: {ex}") #  Логирование ошибки инициализации
            raise #  Проброс исключения далее

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправка запроса модели
            return response.text  # Возвращаем ответ модели
        except Exception as ex:
            logger.error(f"Ошибка при отправке запроса модели: {ex}") #  Логирование ошибки при отправке запроса
            return f"Error: {str(ex)}" # Возвращение сообщения об ошибке
```

```markdown
### Задай вопрос модели Gemini

Для работы потребуется ключ API ключ

API КЛЮЧ К МОДЕЛИ МОЖНО ПОЛУЧИТЬ ЗДЕСЬ: [https://aistudio.google.com/](https://aistudio.google.com/) 

```python
"""
Модуль для взаимодействия с моделями Google Generative AI.
=========================================================================================

Этот модуль содержит класс :class:`GoogleGenerativeAI`, который позволяет взаимодействовать с моделями
Google Gemini, такими как "gemini-1.5-flash-8b", "gemini-2-13b", "gemini-3-20b".

Пример использования
--------------------

Пример создания экземпляра класса `GoogleGenerativeAI` и отправки запроса:

.. code-block:: python

    api_key = "YOUR_API_KEY"
    model = GoogleGenerativeAI(api_key=api_key, model_name="gemini-2-13b")
    response = model.ask("Как улучшить мой код?")
    print(response)
"""
import google.generativeai as genai  # Импорт библиотеки google.generativeai
from src.logger.logger import logger  # Импорт логгера из src.logger.logger


class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    :param api_key: Ключ API для доступа к генеративной модели.
    :type api_key: str
    :param model_name: Название модели для использования. По умолчанию "gemini-2.0-flash-exp".
    :type model_name: str, optional
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]  # Список доступных моделей

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к генеративной модели.
        :type api_key: str
        :param model_name: Название модели для использования. По умолчанию "gemini-2.0-flash-exp".
        :type model_name: str, optional
        :raises ValueError: Если api_key не указан или некорректен.
        """
        if not api_key:  # Проверка наличия API ключа
            raise ValueError("API ключ не может быть пустым.") #  Вызов исключения если api_key не указан
        self.api_key = api_key  #  Сохранение ключа API
        self.model_name = model_name  # Сохранение названия модели
        try:
             genai.configure(api_key=self.api_key)  # Настройка API ключа
             self.model = genai.GenerativeModel(model_name=self.model_name)  # Инициализация модели
        except Exception as ex:
            logger.error(f"Ошибка инициализации модели: {ex}") #  Логирование ошибки инициализации
            raise #  Проброс исключения далее

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        :param q: Вопрос, который будет отправлен модели.
        :type q: str
        :return: Ответ от модели.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправка запроса модели
            return response.text  # Возвращаем ответ модели
        except Exception as ex:
            logger.error(f"Ошибка при отправке запроса модели: {ex}") #  Логирование ошибки при отправке запроса
            return f"Error: {str(ex)}" # Возвращение сообщения об ошибке
```

### Как работает этот код

1.  **Импорт библиотеки**: Мы импортируем библиотеку `google.generativeai`, которая предоставляет интерфейс для взаимодействия с моделями Google AI.
2.  **Класс `GoogleGenerativeAI`**: Этот класс инкапсулирует всю логику взаимодействия с моделью Gemini. Он принимает API-ключ и имя модели в качестве параметров. По умолчанию используется модель `gemini-2.0-flash-exp`.
3.  **Метод `__init__`**: В этом методе происходит настройка модели. Мы передаем API-ключ и имя модели, а затем инициализируем объект модели.
4.  **Метод `ask`**: Этот метод отправляет текстовый запрос модели и возвращает ответ. Если что-то пойдет не так, метод вернет сообщение об ошибке.

### Как использовать?

```python
################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY: str = input("API ключ от `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Вопрос: ")
response = model.ask(q)
print(response)
```

1.  **Ввод API-ключа**: Сначала программа запрашивает у пользователя API-ключ для доступа к модели Gemini. Этот ключ можно получить на сайте [Google AI Studio](https://aistudio.google.com/).
2.  **Создание объекта модели**: Мы создаем объект класса `GoogleGenerativeAI`, передавая ему API-ключ.
3.  **Ввод вопроса**: Пользователь вводит свой вопрос, который хочет задать модели.
4.  **Получение ответа**: Программа отправляет вопрос модели и выводит ответ на экран.

### Пример использования

У вас есть API-ключ, и вы хотите спросить модель: "Как улучшить мой код?". Вот как это будет выглядеть:

```
API ключ от `gemini`: ваш_api_ключ
Вопрос: Как улучшить мой код?
Ответ: Для улучшения вашего кода рекомендуется следовать принципам чистого кода, таким как именование переменных и функций понятно и логично, использование комментариев для объяснения сложной логики, а также применение принципов SOLID для проектирования классов и модулей.
```

Запустить код можно [здесь](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)
```