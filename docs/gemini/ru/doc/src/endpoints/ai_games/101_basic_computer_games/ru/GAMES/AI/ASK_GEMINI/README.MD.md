# Модуль для взаимодействия с моделями Google Generative AI

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI, такими как Gemini. Он позволяет отправлять текстовые запросы и получать ответы от модели.

## Оглавление

1. [Классы](#классы)
    - [`GoogleGenerativeAI`](#googlegenerativeai)
2. [Функции](#функции)

## Классы

### `GoogleGenerativeAI`

**Описание**:
Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
- `__init__`: Инициализация модели GoogleGenerativeAI.
- `ask`: Отправляет текстовый запрос модели и возвращает ответ.

#### `__init__`
```python
def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp")
```
**Описание**:
Инициализация модели GoogleGenerativeAI.

**Параметры**:
- `api_key` (str): Ключ API для доступа к генеративной модели.
- `model_name` (str, optional): Название модели для использования. По умолчанию "gemini-2.0-flash-exp".

#### `ask`
```python
def ask(self, q: str) -> str
```
**Описание**:
Отправляет текстовый запрос модели и возвращает ответ.

**Параметры**:
- `q` (str): Вопрос, который будет отправлен модели.

**Возвращает**:
- `str`: Ответ от модели.

## Функции

В данном модуле нет отдельных функций, кроме методов класса.

---

### Как работает этот код

1. **Импорт библиотеки**: Мы импортируем библиотеку `google.generativeai`, которая предоставляет интерфейс для взаимодействия с моделями Google AI.

2. **Класс `GoogleGenerativeAI`**: Этот класс инкапсулирует всю логику взаимодействия с моделью Gemini. Он принимает API-ключ и имя модели в качестве параметров. По умолчанию используется модель `gemini-2.0-flash-exp`.

3. **Метод `__init__`**: В этом методе происходит настройка модели. Мы передаем API-ключ и имя модели, а затем инициализируем объект модели.

4. **Метод `ask`**: Этот метод отправляет текстовый запрос модели и возвращает ответ. Если что-то пойдет не так, метод вернет сообщение об ошибке.

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

1. **Ввод API-ключа**: Сначала программа запрашивает у пользователя API-ключ для доступа к модели Gemini. Этот ключ можно получить на сайте [Google AI Studio](https://aistudio.google.com/).

2. **Создание объекта модели**: Мы создаем объект класса `GoogleGenerativeAI`, передавая ему API-ключ.

3. **Ввод вопроса**: Пользователь вводит свой вопрос, который хочет задать модели.

4. **Получение ответа**: Программа отправляет вопрос модели и выводит ответ на экран.

### Пример использования

У вас есть API-ключ, и вы хотите спросить модель: "Как улучшить мой код?". Вот как это будет выглядеть:

```
API ключ от `gemini`: ваш_api_ключ
Вопрос: Как улучшить мой код?
Ответ: Для улучшения вашего кода рекомендуется следовать принципам чистого кода, таким как именование переменных и функций понятно и логично, использование комментариев для объяснения сложной логики, а также применение принципов SOLID для проектирования классов и модулей.
```

Запустить код можно [здесь](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)