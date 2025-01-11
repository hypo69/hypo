# <input code>

```python
"""
Provides mechanisms for creating understanding the characteristics of agent populations, such as
the their age distribution, typical interests, and so on.

Guideline for plotting the methods: all plot methods should also return a Pandas dataframe with the data used for 
plotting.
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson

def plot_age_distribution(agents:List[TinyPerson], title:str="Age Distribution", show:bool=True):
    """
    Plots the age distribution of the given agents.

    Args:
        agents (List[TinyPerson]): The agents whose age distribution is to be plotted.
        title (str, optional): The title of the plot. Defaults to "Age Distribution".
        show (bool, optional): Whether to show the plot. Defaults to True.
    
    Returns:
        pd.DataFrame: The data used for plotting.
    """
    ages = [agent.get("age") for agent in agents]

    # corresponding dataframe
    df = pd.DataFrame(ages, columns=["Age"])
    df["Age"].plot.hist(bins=20, title=title)
    if show:
        plt.show()

    return df
    

def plot_interest_distribution(agents:List[TinyPerson], title:str="Interest Distribution", show:bool=True):
    """
    Plots the interest distribution of the given agents.

    Args:
        agents (List[TinyPerson]): The agents whose interest distribution is to be plotted.
        title (str, optional): The title of the plot. Defaults to "Interest Distribution".
        show (bool, optional): Whether to show the plot. Defaults to True.
    
    Returns:
        pd.DataFrame: The data used for plotting.
    """
    interests = [agent.get("interests") for agent in agents]

    # corresponding dataframe
    df = pd.DataFrame(interests, columns=["Interests"])

    # let's plot a pie chart
    df["Interests"].value_counts().plot.pie(title=title)
    if show:
        plt.show()

    return df
```

# <algorithm>

**Шаг 1:** Функция `plot_age_distribution` принимает список агентов `agents`.

**Шаг 2:** Извлекает значения возраста из каждого агента и сохраняет их в список `ages`.

**Шаг 3:** Создаёт Pandas DataFrame `df` из списка `ages` с колонкой "Age".

**Шаг 4:** Строит гистограмму распределения возрастов с помощью метода `plot.hist` DataFrame `df`.

**Шаг 5:** Если `show=True`, отображает гистограмму с помощью `plt.show()`.

**Шаг 6:** Возвращает DataFrame `df`.


**Пример:**

Если `agents` содержит 5 агентов с возрастами 20, 25, 30, 25, 20, то `ages` будет содержать [20, 25, 30, 25, 20].  `df` будет содержать значения возраста в колонке "Age".  Гистограмма покажет распределение возрастов.


**Шаг 1:** Функция `plot_interest_distribution` принимает список агентов `agents`.

**Шаг 2:** Извлекает значения интересов из каждого агента и сохраняет их в список `interests`.

**Шаг 3:** Создаёт Pandas DataFrame `df` из списка `interests` с колонкой "Interests".

**Шаг 4:** Строит круговую диаграмму распределения интересов с помощью метода `value_counts().plot.pie` DataFrame `df`.

**Шаг 5:** Если `show=True`, отображает круговую диаграмму с помощью `plt.show()`.

**Шаг 6:** Возвращает DataFrame `df`.

**Пример:**

Если `agents` содержит агентов с интересами ["спорт", "книги", "спорт", "музыка", "книги"], то `interests` будет содержать ["спорт", "книги", "спорт", "музыка", "книги"]. `df` будет содержать значения интересов в колонке "Interests". Круговая диаграмма покажет долю каждого интереса.


# <mermaid>

```mermaid
graph TD
    A[plot_age_distribution] --> B{Extract Ages};
    B --> C[Create DataFrame];
    C --> D[Plot Histogram];
    D --> E{Show Plot?};
    E -- Yes --> F[plt.show];
    E -- No --> G;
    G --> H[Return DataFrame];
    
    I[plot_interest_distribution] --> J{Extract Interests};
    J --> K[Create DataFrame];
    K --> L[Plot Pie Chart];
    L --> M{Show Plot?};
    M -- Yes --> N[plt.show];
    M -- No --> O;
    O --> P[Return DataFrame];
    
    subgraph TinyPerson
        TinyPerson --> B;
        TinyPerson --> J;
    end
    
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style J fill:#ccf,stroke:#333,stroke-width:2px
    style K fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#ccf,stroke:#333,stroke-width:2px

```

# <explanation>

**Импорты:**

* `pandas as pd`: Библиотека для работы с данными, создания и манипулирования DataFrame.  (Необходима для работы с табличными данными).
* `matplotlib.pyplot as plt`: Библиотека для визуализации данных, создания графиков (гистограмм, круговых диаграмм).
* `typing.List`:  Тип данных для работы со списками.
* `tinytroupe.agent import TinyPerson`: Импортирует класс `TinyPerson` из модуля `tinytroupe.agent`. Это указывает на то, что `TinyPerson` определён в другом файле проекта (`tinytroupe/agent.py`).  Этот импорт позволяет использовать объекты класса `TinyPerson` в текущем файле.


**Классы:**

* `TinyPerson`: Не описан в данном файле. Определение класса `TinyPerson` находится в `tinytroupe/agent.py`.  Скорее всего, этот класс описывает агентов и содержит информацию о них, такую как возраст и интересы.  Метод `get("age")` и `get("interests")` предполагают, что `TinyPerson` имеет атрибуты/свойства  "age" и "interests", которые хранят соответствующую информацию.

**Функции:**

* `plot_age_distribution(agents:List[TinyPerson], title:str="Age Distribution", show:bool=True)`: Функция принимает список агентов (`agents`), строит гистограмму распределения их возраста.
    * `agents`: Список объектов `TinyPerson`.
    * `title`: Заголовок графика.
    * `show`: Флаг, показывать ли график. Возвращает Pandas DataFrame с данными распределения возрастов.
* `plot_interest_distribution(agents:List[TinyPerson], title:str="Interest Distribution", show:bool=True)`: Функция принимает список агентов (`agents`), строит круговую диаграмму распределения их интересов.
    * `agents`: Список объектов `TinyPerson`.
    * `title`: Заголовок графика.
    * `show`: Флаг, показывать ли график. Возвращает Pandas DataFrame с данными распределения интересов.


**Переменные:**

* `ages`, `interests`: Списки, содержащие значения возраста и интересов агентов соответственно.
* `df`: Pandas DataFrame, используемый для хранения и визуализации данных распределения.


**Возможные ошибки/улучшения:**

* **Обработка исключений:**  Код не обрабатывает случай, когда `agent.get("age")` или `agent.get("interests")` могут возвращать значения, отличные от ожидаемых (например, `None`).  Добавление проверки `if agent.get("age") is not None:` предотвратит ошибки. Аналогично, необходимо проверить, что `agent.get("interests")` не `None` и что это список, а не что-то другое.
* **Вариативность интересов:**  Возможно, интересы агентов представлены в виде списка.  Код должен учитывать этот факт и уметь обрабатывать такие ситуации.
* **Проверка на пустой список:** Если `agents` - пустой список, то в обеих функциях произойдёт ошибка. Необходимо добавить проверку на пустой вход.


**Взаимосвязи с другими частями проекта:**

Функции `plot_age_distribution` и `plot_interest_distribution` зависят от класса `TinyPerson`, который должен быть определён в `tinytroupe/agent.py`.  Эти функции, вероятно, используются для анализа данных, собранных в других частях проекта.