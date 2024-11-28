Как использовать класс TinyStory
========================================================================================

Описание
-------------------------
Этот класс отвечает за создание и управление историей в симуляции TinyTroupe. Он позволяет генерировать истории, основанные на взаимодействиях агента или среды.  Класс использует API стороннего поставщика, чтобы получить текст истории, с использованием шаблонов.  Методы `start_story` и `continue_story` позволяют инициировать создание и продолжение истории, передавая параметры, влияющие на ее содержание.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `TinyStory`, предоставив необходимую информацию:
    - `environment` (объект TinyWorld) или `agent` (объект TinyPerson).  Только один из этих параметров должен быть предоставлен.
    - `purpose` (цель истории, по умолчанию "Be a realistic simulation").
    - `context` (текущий контекст истории, по умолчанию пустая строка).
    - `first_n`, `last_n` (количество первых и последних взаимодействий для включения в историю).
    - `include_omission_info` (флаг включения информации об опущенных взаимодействиях).

2. **Запуск истории (`start_story`):** Вызовите метод `start_story`, передав:
    - `requirements` (требования к истории).
    - `number_of_words` (желаемое количество слов в истории).
    - `include_plot_twist` (флаг включения сюжетного поворота).

3. **Продолжение истории (`continue_story`):** Вызовите метод `continue_story` для продолжения истории.  Параметры аналогичны `start_story`.


4. **Получение текущей истории (`_current_story`):**  Метод `_current_story`  формирует строку текущей истории, включая историю взаимодействия агента или среды.  Этот метод автоматически добавляет новую историю в `self.current_story` и возвращает его.  Этот метод НЕ нужно вызывать напрямую. Он используется внутри других методов.

Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.story import TinyStory
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld

    # Предполагается, что TinyPerson и TinyWorld уже инициализированы
    agent = TinyPerson()
    environment = TinyWorld()


    # Инициализация истории для агента
    story = TinyStory(agent=agent, purpose="Create a story about the agent's actions.", first_n=5, last_n=10)

    # Начало истории
    story.start_story(requirements="Tell a story about the agent's first interaction", number_of_words=200)

    # Получение и вывод текущей истории (Внутри класса используется `_current_story`)
    current_story = story._current_story()
    print(current_story)

    # Продолжение истории
    story.continue_story(requirements="Continue the story, emphasizing the agent's challenges", number_of_words=200)

    # Получение и вывод текущей истории
    current_story = story._current_story()
    print(current_story)