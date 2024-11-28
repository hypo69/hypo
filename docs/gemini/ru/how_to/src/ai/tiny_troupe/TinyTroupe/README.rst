Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой README файл для библиотеки TinyTroupe, которая позволяет создавать симуляции поведения людей с определенными личностями, интересами и целями с использованием больших языковых моделей (LLM).  Он описывает принципы работы библиотеки, предоставляет инструкции по установке и использованию, примеры использования и рекомендации по применению.  Он также содержит информацию о предварительных требованиях, структуре проекта, возможностях конфигурации и поведению в случае отказа API.

Шаги выполнения
-------------------------
1. **Установка TinyTroupe:**
    - Убедитесь, что у вас установлена Python 3.10 или выше.  Рекомендуется использовать Anaconda.
    - Создайте новую среду Python: `conda create -n tinytroupe python=3.10`
    - Активируйте среду: `conda activate tinytroupe`
    - Установите библиотеку из репозитория, а не с PyPI: `git clone https://github.com/microsoft/tinytroupe; cd tinytroupe; pip install .`
    - Установите необходимые ключи API (Azure OpenAI или OpenAI) в качестве переменных окружения, как описано в разделе "Предварительные требования".  Обязательно используйте фильтры контента (особенно с Azure OpenAI).
2. **Создание TinyPerson:**
    - Используйте предопределенные агенты из `tinytroupe.examples`:  `from tinytroupe.examples import create_lisa_the_data_scientist; lisa = create_lisa_the_data_scientist()`.
    - Или создайте своего агента с помощью `TinyPersonFactory`: `from tinytroupe.factory import TinyPersonFactory; factory = TinyPersonFactory("A hospital in São Paulo."); person = factory.generate_person("Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.")`.
3. **Создание TinyWorld:**
    - Создайте среду `TinyWorld`: `world = TinyWorld("Chat Room", [agent1, agent2])`.
4. **Взаимодействие агентов:**
    - Используйте методы `listen`, `see`, `act` или `listen_and_act` для взаимодействия агентов в среде.
    - Пример: `world.make_everyone_accessible(); lisa.listen("Talk to Oscar to know more about him"); world.run(4)`.
5. **Обработка результатов:**
    - Используйте `ResultsExtractor` и `ResultsReducer`, чтобы извлечь и обработать результаты взаимодействия агентов.
6. **Использование кэширования:**
    - Используйте механизмы кэширования для повышения производительности, особенно при многократном использовании LLM.

Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.examples import create_lisa_the_data_scientist
    from tinytroupe.world import TinyWorld

    lisa = create_lisa_the_data_scientist()
    oscar = TinyPerson("Oscar")
    oscar.define("occupation", "Architect")

    world = TinyWorld("Discussion", [lisa, oscar])
    world.make_everyone_accessible()
    lisa.listen("Tell me about your work, Oscar.")
    world.run(5)

    # Обработка результатов (не показано в примере)