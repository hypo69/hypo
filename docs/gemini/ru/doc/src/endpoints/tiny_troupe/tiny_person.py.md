# Модуль tiny_person.py

## Обзор

Модуль представляет собой пример использования класса `TinyPerson` из библиотеки `tinytroupe`. Он демонстрирует создание экземпляра агента `TinyPerson`, определение его характеристик и взаимодействие с ним.

## Подробней

Этот код предназначен для демонстрации базового функционала библиотеки `tinytroupe`, позволяющей создавать и настраивать виртуальных персонажей с определенными характеристиками и способностями. Сначала загружаются переменные окружения из файла `.env` и устанавливается API-ключ OpenAI. Затем создается экземпляр класса `TinyPerson` с именем "John", определяются его характеристики (возраст, профессия, национальность, навыки) и происходит взаимодействие с агентом посредством вызова методов `listen` и `act`. В конце выводятся текущие взаимодействия агента.

## Классы

### `TinyPerson`

**Описание**: Класс представляет собой виртуального персонажа с возможностью определения его характеристик и взаимодействия с ним. Более подробная информация о классе `TinyPerson` находится в модуле `tinytroupe.agent`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `TinyPerson`.
- `define`: Определяет характеристику персонажа.
- `listen`: Позволяет персонажу "услышать" сообщение.
- `act`: Запускает действие персонажа.
- `pp_current_interactions`: Выводит текущие взаимодействия персонажа.

## Функции

В данном коде нет явно определенных функций, однако используются методы класса `TinyPerson`.

### Пример использования методов класса `TinyPerson`

#### `__init__`
```python
    def __init__(
        self,
        name: str,
        profile: Optional[str] = None,
        system_prompt: Optional[str] = None,
        llm: str = "default",
        verbose: Optional[bool] = False,
        use_tools: bool = False,
        memory: Optional[bool] = True,
        context_window: int = 4096,
        model_kwargs: Optional[dict] = None,
        temperature: float = 0.7,
    ) -> None:
        """
        Args:
            name (str): Имя персонажа.
            profile (Optional[str], optional): Описание профиля персонажа. По умолчанию `None`.
            system_prompt (Optional[str], optional): Системный промт для персонажа. По умолчанию `None`.
            llm (str): Название используемой LLM модели. По умолчанию "default".
            verbose (Optional[bool], optional): Флаг для отображения подробной информации. По умолчанию `False`.
            use_tools (bool): Флаг для использования инструментов. По умолчанию `False`.
            memory (Optional[bool], optional): Флаг для использования памяти. По умолчанию `True`.
            context_window (int): Размер окна контекста. По умолчанию 4096.
            model_kwargs (Optional[dict], optional): Дополнительные аргументы для модели. По умолчанию `None`.
            temperature (float): Температура для генерации текста. По умолчанию 0.7.
        
        Raises:
            Exception: Описание ситуации, в которой возникает исключение.

        """
```

#### `define`
```python
    def define(self, key: str, value: str | int | dict | list) -> None:
        """ Функция определяет характеристику персонажа.
        Args:
            key (str): Ключ характеристики.
            value (str | int | dict | list): Значение характеристики.

        Raises:
            Exception: Описание ситуации, в которой возникает исключение.
        """
```

#### `listen`
```python
    def listen(self, message: str) -> None:
        """Функция позволяет персонажу "услышать" сообщение.
        Args:
            message (str): Сообщение для персонажа.

        Raises:
            Exception: Описание ситуации, в которой возникает исключение.
        """
```

#### `act`
```python
    def act(self) -> None:
        """Функция запускает действие персонажа.

        Raises:
            Exception: Описание ситуации, в которой возникает исключение.
        """
```

#### `pp_current_interactions`
```python
    def pp_current_interactions(self) -> None:
        """Функция выводит текущие взаимодействия персонажа.

        Raises:
            Exception: Описание ситуации, в которой возникает исключение.
        """
```

## Примеры

```python
import os
from dotenv import load_dotenv

# Если ключ хранится в файле .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from tinytroupe.agent import TinyPerson

# Создание инстанса драйвера (пример с Chrome)
john = TinyPerson(name="John")

# Определение некоторых характеристик
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")
john.define("skills", [{"skill": "Coding in python"}])

# Взаимодействие с агентом
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()