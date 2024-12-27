# Анализ кода модуля `profiling.py`

**Качество кода**
6
-  Плюсы
    - Код выполняет свою задачу по визуализации данных об агентах.
    - Используются pandas для обработки данных и matplotlib для создания графиков.
    - Есть docstring для каждой функции, описывающий ее назначение, аргументы и возвращаемое значение.
-  Минусы
    -  Отсутствует описание модуля в начале файла.
    -  Не используются `logger` для логирования ошибок или предупреждений.
    -  Не используется `j_loads` для чтения данных, хотя в данном случае это и не требуется.
    -  Имена переменных и функций не всегда соответствуют общепринятым соглашениям (например, `show` вместо `is_show`).
    -  Типы возвращаемых значений в docstring не приведены в RST формате.

**Рекомендации по улучшению**
1. Добавить описание модуля в формате reStructuredText.
2. Использовать `logger` для логирования (хотя в данном коде ошибок нет, лучше добавить для полноты).
3. Переписать docstring в формате reStructuredText.
4. Переименовать переменную `show` на `is_show`.

**Оптимизированный код**
```python
"""
Модуль для профилирования характеристик популяций агентов.
=========================================================================================

Этот модуль предоставляет функции для создания визуализаций, позволяющих анализировать
распределение возрастов и интересов агентов.

Функции модуля:

- :func:`plot_age_distribution`: Создает гистограмму распределения возрастов агентов.
- :func:`plot_interest_distribution`: Создает круговую диаграмму распределения интересов агентов.

Пример использования
--------------------

.. code-block:: python

    from tinytroupe.profiling import plot_age_distribution, plot_interest_distribution
    from tinytroupe.agent import TinyPerson

    agents = [
        TinyPerson(age=20, interests='reading'),
        TinyPerson(age=30, interests='sports'),
        TinyPerson(age=20, interests='reading'),
        TinyPerson(age=40, interests='traveling')
    ]

    age_df = plot_age_distribution(agents, title="Распределение возрастов", show=False)
    interest_df = plot_interest_distribution(agents, title="Распределение интересов", show=False)
    print(age_df)
    print(interest_df)
"""
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from tinytroupe.agent import TinyPerson
# from src.logger.logger import logger # TODO добавить использование логгера

def plot_age_distribution(agents:List[TinyPerson], title:str="Age Distribution", is_show:bool=True) -> pd.DataFrame:
    """
    Создает гистограмму распределения возрастов агентов.

    :param agents: Список агентов, для которых строится распределение возрастов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика.
    :type title: str, optional
    :param is_show: Флаг, определяющий, нужно ли показывать график.
    :type is_show: bool, optional
    :return: Pandas DataFrame с данными, использованными для построения графика.
    :rtype: pd.DataFrame
    """
    # код извлекает возрасты из списка агентов
    ages = [agent.get("age") for agent in agents]

    # код создает DataFrame из полученных возрастов
    df = pd.DataFrame(ages, columns=["Age"])
    # код создает гистограмму распределения возрастов
    df["Age"].plot.hist(bins=20, title=title)
    # код отображает график, если is_show=True
    if is_show:
        plt.show()

    return df
    

def plot_interest_distribution(agents:List[TinyPerson], title:str="Interest Distribution", is_show:bool=True) -> pd.DataFrame:
    """
    Создает круговую диаграмму распределения интересов агентов.

    :param agents: Список агентов, для которых строится распределение интересов.
    :type agents: List[TinyPerson]
    :param title: Заголовок графика.
    :type title: str, optional
    :param is_show: Флаг, определяющий, нужно ли показывать график.
    :type is_show: bool, optional
    :return: Pandas DataFrame с данными, использованными для построения графика.
    :rtype: pd.DataFrame
    """
    # код извлекает интересы из списка агентов
    interests = [agent.get("interests") for agent in agents]

    # код создает DataFrame из полученных интересов
    df = pd.DataFrame(interests, columns=["Interests"])

    # код создает круговую диаграмму распределения интересов
    df["Interests"].value_counts().plot.pie(title=title)
    # код отображает график, если is_show=True
    if is_show:
        plt.show()

    return df
```