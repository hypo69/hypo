# Received Code
```python
"""
Provides mechanisms for creating understanding the characteristics of agent populations, such as
their age distribution, typical interests, and so on.

Guideline for plotting the methods: all plot methods should also return a Pandas dataframe with the data used for 
plotting.
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson


def plot_age_distribution(agents: List[TinyPerson], title: str = "Age Distribution", show: bool = True):
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


def plot_interest_distribution(agents: List[TinyPerson], title: str = "Interest Distribution", show: bool = True):
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
# Improved Code
```python
"""
Предоставляет механизмы для понимания характеристик популяций агентов, таких как
их возрастное распределение, типичные интересы и т. д.

Рекомендации по построению графиков: все методы построения графиков также должны возвращать Pandas DataFrame с данными,
используемыми для построения графика.
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson
from src.logger.logger import logger


def plot_age_distribution(agents: List[TinyPerson], title: str = "Age Distribution", show: bool = True) -> pd.DataFrame:
    """
    Строит график распределения возрастов заданных агентов.

    :param agents: Список агентов (TinyPerson), для которых строится график распределения возрастов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика. По умолчанию "Age Distribution".
    :type title: str, optional
    :param show: Определяет, нужно ли отображать график. По умолчанию True.
    :type show: bool, optional
    :return: DataFrame с данными, используемыми для построения графика.
    :rtype: pd.DataFrame
    """
    try:
        # Извлекает возраст каждого агента
        ages = [agent.get("age") for agent in agents]

        # Создаёт DataFrame из возрастов
        df = pd.DataFrame(ages, columns=["Age"])
        # Строит гистограмму распределения возрастов
        df["Age"].plot.hist(bins=20, title=title)
        if show:
            plt.show()
        return df
    except Exception as e:
        logger.error(f'Ошибка при построении графика распределения возрастов: {e}')
        return pd.DataFrame()


def plot_interest_distribution(agents: List[TinyPerson], title: str = "Interest Distribution", show: bool = True) -> pd.DataFrame:
    """
    Строит график распределения интересов заданных агентов.

    :param agents: Список агентов (TinyPerson), для которых строится график распределения интересов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика. По умолчанию "Interest Distribution".
    :type title: str, optional
    :param show: Определяет, нужно ли отображать график. По умолчанию True.
    :type show: bool, optional
    :return: DataFrame с данными, используемыми для построения графика.
    :rtype: pd.DataFrame
    """
    try:
        # Извлекает интересы каждого агента
        interests = [agent.get("interests") for agent in agents]

        # Создаёт DataFrame из интересов
        df = pd.DataFrame(interests, columns=["Interests"])

        # Строит круговую диаграмму распределения интересов
        df["Interests"].value_counts().plot.pie(title=title)
        if show:
            plt.show()
        return df
    except Exception as e:
        logger.error(f'Ошибка при построении графика распределения интересов: {e}')
        return pd.DataFrame()
```
# Changes Made
1. **Добавлены docstring к модулю**:
   - Добавлено описание модуля в формате reStructuredText (RST).
2. **Импорты**:
   - Добавлен импорт `from src.logger.logger import logger` для логирования ошибок.
3. **Функция `plot_age_distribution`**:
   - Добавлен docstring в формате RST.
   - Добавлена обработка ошибок с использованием `try-except` и логирование с `logger.error`.
   - Добавлен возврат пустого `DataFrame` в случае ошибки.
4. **Функция `plot_interest_distribution`**:
   - Добавлен docstring в формате RST.
   - Добавлена обработка ошибок с использованием `try-except` и логирование с `logger.error`.
   - Добавлен возврат пустого `DataFrame` в случае ошибки.
5. **Типизация возвращаемых значений**:
   - Добавлена типизация возвращаемого значения `-> pd.DataFrame` в обе функции.

# FULL Code
```python
"""
Предоставляет механизмы для понимания характеристик популяций агентов, таких как
их возрастное распределение, типичные интересы и т. д.

Рекомендации по построению графиков: все методы построения графиков также должны возвращать Pandas DataFrame с данными,
используемыми для построения графика.
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson
# Добавлен импорт logger
from src.logger.logger import logger


def plot_age_distribution(agents: List[TinyPerson], title: str = "Age Distribution", show: bool = True) -> pd.DataFrame:
    """
    Строит график распределения возрастов заданных агентов.

    :param agents: Список агентов (TinyPerson), для которых строится график распределения возрастов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика. По умолчанию "Age Distribution".
    :type title: str, optional
    :param show: Определяет, нужно ли отображать график. По умолчанию True.
    :type show: bool, optional
    :return: DataFrame с данными, используемыми для построения графика.
    :rtype: pd.DataFrame
    """
    try:
        # Извлекает возраст каждого агента
        ages = [agent.get("age") for agent in agents]

        # Создаёт DataFrame из возрастов
        df = pd.DataFrame(ages, columns=["Age"])
        # Строит гистограмму распределения возрастов
        df["Age"].plot.hist(bins=20, title=title)
        if show:
            plt.show()
        return df
    except Exception as e:
        # Логирование ошибки с помощью logger
        logger.error(f'Ошибка при построении графика распределения возрастов: {e}')
        return pd.DataFrame()


def plot_interest_distribution(agents: List[TinyPerson], title: str = "Interest Distribution", show: bool = True) -> pd.DataFrame:
    """
    Строит график распределения интересов заданных агентов.

    :param agents: Список агентов (TinyPerson), для которых строится график распределения интересов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика. По умолчанию "Interest Distribution".
    :type title: str, optional
    :param show: Определяет, нужно ли отображать график. По умолчанию True.
    :type show: bool, optional
    :return: DataFrame с данными, используемыми для построения графика.
    :rtype: pd.DataFrame
    """
    try:
        # Извлекает интересы каждого агента
        interests = [agent.get("interests") for agent in agents]

        # Создаёт DataFrame из интересов
        df = pd.DataFrame(interests, columns=["Interests"])

        # Строит круговую диаграмму распределения интересов
        df["Interests"].value_counts().plot.pie(title=title)
        if show:
            plt.show()
        return df
    except Exception as e:
        # Логирование ошибки с помощью logger
        logger.error(f'Ошибка при построении графика распределения интересов: {e}')
        return pd.DataFrame()