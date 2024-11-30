Как использовать класс TinyFactory
========================================================================================

Описание
-------------------------
Этот код определяет базовый класс `TinyFactory` и производный класс `TinyPersonFactory` для создания и управления объектами.  `TinyFactory` предоставляет механизмы для создания, хранения и управления множеством фабрик, а `TinyPersonFactory` специализируется на генерации объектов `TinyPerson` с помощью OpenAI. Код включает в себя функциональность для хранения состояний фабрик, генерации персон и взаимодействия с OpenAI.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует библиотеки `os`, `json`, `chevron`, `logging`, `copy`, `openai_utils`, `TinyPerson`, `utils`, и `transactional`. Это необходимые инструменты для работы с файлами, данными, шаблонами, логгированием, копированием, API OpenAI и транзакционным кэшированием.

2. **Определение класса `TinyFactory`:** Класс `TinyFactory` служит основой для других типов фабрик. Он содержит методы для инициализации фабрик (`__init__`), представления фабрики (`__repr__`), добавления фабрик в глобальный список (`add_factory`), очистки глобального списка (`clear_factories`), а также кодирования и декодирования состояния фабрики (`encode_complete_state`, `decode_complete_state`).

3. **Определение класса `TinyPersonFactory`:**  `TinyPersonFactory` наследуется от `TinyFactory`. Он предоставляет методы для инициализации (`__init__`), генерации списка `TinyPersonFactory` (`generate_person_factories`) и генерации отдельной персоны (`generate_person`) с использованием OpenAI.

4. **Генерация персон (`generate_person_factories`):** Этот метод использует шаблон `generate_person_factory.md` для создания запроса к OpenAI. Он получает ответ, извлекает из него информацию и создает соответствующие объекты `TinyPersonFactory`.

5. **Генерация персоны (`generate_person`):** Этот метод использует шаблон `generate_person.mustache` для создания запроса к OpenAI, основываясь на контексте и желаемых особенностях персонажа. Он обрабатывает ответы от OpenAI и создает объект `TinyPerson`.

6. **Транзакционное кэширование (`@transactional`):** Декоратор `@transactional` используется для добавления кэширования в методы, вызывающие API OpenAI. Это помогает избежать повторных обращений к OpenAI для одинаковых запросов.

Пример использования
-------------------------
.. code-block:: python

    import os
    from tinytroupe.factory import TinyPersonFactory

    # Контекст для генерации персон
    generic_context_text = "Это описание для генерации персон."

    # Количество персон для генерации
    number_of_factories = 3

    # Генерируем список TinyPersonFactory
    factories = TinyPersonFactory.generate_person_factories(number_of_factories, generic_context_text)

    if factories:
        for factory in factories:
            # Можно использовать методы класса TinyPersonFactory, например:
            person = factory.generate_person()
            if person:
                print(f"Сгенерированная персона: {person}")