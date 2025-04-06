# Модуль для работы с TinyPerson
===========================================

Модуль демонстрирует создание и взаимодействие с экземпляром класса `TinyPerson` из библиотеки `tinytroupe`. Он показывает, как определять характеристики агента и взаимодействовать с ним.

## Обзор

Этот модуль содержит пример использования класса `TinyPerson` для создания виртуального персонажа, определения его характеристик и взаимодействия с ним. Он демонстрирует основные возможности библиотеки `tinytroupe` для создания и управления виртуальными агентами.

## Подробней

В данном примере создается экземпляр класса `TinyPerson`, определяются его основные характеристики (возраст, профессия, национальность, навыки) и происходит взаимодействие с ним через методы `listen` и `act`. Результаты взаимодействия выводятся на экран с помощью метода `pp_current_interactions`.

## Классы

### `TinyPerson`

**Описание**: Класс для создания и управления виртуальными персонажами. Подробная информация о классе находится в модуле `tinytroupe.agent`.

## Функции

В данном коде функции отсутствуют. Присутствуют только методы класса `TinyPerson`.

## Использование

```python
import os
from dotenv import load_dotenv
# Если ключ хранится в файле .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from tinytroupe.agent import TinyPerson

# Create a TinyPerson instance
john = TinyPerson(name="John")

# Define some characteristics
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")
john.define("skills", [{"skill": "Coding in python"}])

# Interact with the agent
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()
```

1.  **Загрузка переменных окружения**:

    *   Код начинается с загрузки переменных окружения из файла `.env` с использованием библиотеки `dotenv`.
    *   `load_dotenv()`: Эта функция загружает переменные окружения из файла `.env` в текущее окружение.
    *   `os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")`: Устанавливает значение переменной окружения `OPENAI_API_KEY` из файла `.env`.

2.  **Импорт класса `TinyPerson`**:

    *   `from tinytroupe.agent import TinyPerson`: Импортирует класс `TinyPerson` из модуля `tinytroupe.agent`.

3.  **Создание экземпляра класса `TinyPerson`**:

    *   `john = TinyPerson(name="John")`: Создает экземпляр класса `TinyPerson` с именем "John".

4.  **Определение характеристик агента**:

    *   `john.define("age", 35)`: Определяет возраст Джона как 35 лет.
    *   `john.define("occupation", "Software Engineer")`: Определяет профессию Джона как "Software Engineer".
    *   `john.define("nationality", "American")`: Определяет национальность Джона как "American".
    *   `john.define("skills", [{"skill": "Coding in python"}])`: Определяет навыки Джона как "Coding in python".

5.  **Взаимодействие с агентом**:

    *   `john.listen("Hello, John! How are you today?")`: Передает сообщение Джону.
    *   `john.act()`: Активирует агента для выполнения действий.
    *   `john.pp_current_interactions()`: Выводит текущие взаимодействия агента на экран.

```
Загрузка переменных окружения из .env
    |
    V
Импорт класса TinyPerson
    |
    V
Создание экземпляра TinyPerson (john)
    |
    V
Определение характеристик (возраст, профессия, национальность, навыки)
    |
    V
Взаимодействие с агентом (слушать, действовать, вывод взаимодействий)
```
## Примеры

### Создание и определение характеристик TinyPerson

```python
from tinytroupe.agent import TinyPerson

# Создание экземпляра TinyPerson
agent = TinyPerson(name="Alice")

# Определение характеристик
agent.define("age", 28)
agent.define("occupation", "Data Scientist")
agent.define("nationality", "British")

print(f"Agent's name: {agent.name}, age: {agent.age}, occupation: {agent.occupation}, nationality: {agent.nationality}")
```

### Взаимодействие с TinyPerson

```python
from tinytroupe.agent import TinyPerson

# Создание экземпляра TinyPerson
agent = TinyPerson(name="Bob")

# Взаимодействие
agent.listen("Tell me about yourself.")
agent.act()
agent.pp_current_interactions()