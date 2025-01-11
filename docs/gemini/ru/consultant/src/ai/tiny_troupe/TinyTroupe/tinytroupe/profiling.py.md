# Анализ кода модуля `profiling.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используются аннотации типов для повышения читаемости и предотвращения ошибок.
    - Присутствуют docstring для функций, что способствует пониманию их назначения и использования.
    - Используется `pandas` для обработки данных и `matplotlib` для визуализации, что является стандартной практикой.
    - Код возвращает DataFrame, что позволяет использовать данные для дальнейшей обработки.
-  Минусы
    - Отсутствует импорт `logger` из `src.logger.logger` для логирования ошибок.
    - Не используется обработка ошибок с помощью `try-except` и логирование с `logger.error`.
    - Для всех графиков установлено `show=True`. Это может приводить к нежелательному отображению, если функция используется в цикле.

**Рекомендации по улучшению**

1. **Импорт `logger`**: Добавить импорт `from src.logger.logger import logger` для логирования ошибок и предупреждений.
2. **Обработка ошибок**: Обернуть код внутри функций в блоки `try-except` для перехвата исключений и логировать их с помощью `logger.error`.
3. **Улучшение документации**: Дополнить docstring для параметров и возвращаемых значений.
4.  **Возможность не выводить графики**: Убрать по умолчанию `show=True` и сделать явный вызов `plt.show()` вне функции.
5. **Общая функция для построения графиков**: Если графики похожи, можно выделить общую функцию для их отрисовки.

**Оптимизированный код**

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
from src.logger.logger import logger # Импортируем logger

def plot_age_distribution(agents: List[TinyPerson], title: str = 'Age Distribution', show: bool = False) -> pd.DataFrame:
    """
    Построение гистограммы распределения возраста агентов.

    Args:
        agents (List[TinyPerson]): Список агентов, для которых строится распределение возраста.
        title (str, optional): Заголовок графика. По умолчанию 'Age Distribution'.
        show (bool, optional): Флаг, определяющий, нужно ли отображать график. По умолчанию False.

    Returns:
        pd.DataFrame: DataFrame с данными, использованными для построения графика.
    
    Raises:
        Exception: В случае возникновения ошибки при построении графика.
    """
    try:
        # Код извлекает возраст каждого агента и формирует список
        ages = [agent.get('age') for agent in agents]

        # Код создает DataFrame из списка возрастов
        df = pd.DataFrame(ages, columns=['Age'])
        
        # Код строит гистограмму распределения возрастов
        df['Age'].plot.hist(bins=20, title=title)
        
        if show:
            plt.show()
        
        return df
    except Exception as e:
        logger.error('Ошибка при построении гистограммы распределения возраста', exc_info=True)
        return pd.DataFrame()

def plot_interest_distribution(agents: List[TinyPerson], title: str = 'Interest Distribution', show: bool = False) -> pd.DataFrame:
    """
    Построение круговой диаграммы распределения интересов агентов.

    Args:
        agents (List[TinyPerson]): Список агентов, для которых строится распределение интересов.
        title (str, optional): Заголовок графика. По умолчанию 'Interest Distribution'.
        show (bool, optional): Флаг, определяющий, нужно ли отображать график. По умолчанию False.

    Returns:
        pd.DataFrame: DataFrame с данными, использованными для построения графика.
    
    Raises:
        Exception: В случае возникновения ошибки при построении графика.
    """
    try:
        # Код извлекает интересы каждого агента и формирует список
        interests = [agent.get('interests') for agent in agents]

        # Код создает DataFrame из списка интересов
        df = pd.DataFrame(interests, columns=['Interests'])

        # Код строит круговую диаграмму распределения интересов
        df['Interests'].value_counts().plot.pie(title=title)
        
        if show:
            plt.show()

        return df
    except Exception as e:
        logger.error('Ошибка при построении круговой диаграммы распределения интересов', exc_info=True)
        return pd.DataFrame()
```