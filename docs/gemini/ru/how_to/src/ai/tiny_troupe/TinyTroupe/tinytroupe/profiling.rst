Как использовать функции для построения распределения возраста и интересов агентов
=================================================================================

Описание
-------------------------
Данный код содержит функции для визуализации распределения возраста и интересов агентов, представленных в формате списка объектов TinyPerson. Функции `plot_age_distribution` и `plot_interest_distribution` строят гистограмму распределения возраста и круговую диаграмму (pie chart) распределения интересов соответственно. Обе функции возвращают Pandas DataFrame с данными, использованными для построения графиков.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Функции используют pandas для работы с данными в формате DataFrame и matplotlib для визуализации. Также, импортируется тип данных `List` и класс `TinyPerson` из модуля `tinytroupe.agent`.

2. **Функция `plot_age_distribution`:**
   - Принимает список агентов (`agents`) и опциональные параметры `title` (заголовок графика) и `show` (отображать график или нет).
   - Извлекает значения возраста из каждого агента и сохраняет их в список `ages`.
   - Создает Pandas DataFrame `df` из списка `ages` с колонкой "Age".
   - Строит гистограмму распределения возраста с помощью метода `plot.hist()` DataFrame `df`.
   - Устанавливает заголовок графика с помощью `title`.
   - Если параметр `show` равен True, отображает график с помощью `plt.show()`.
   - Возвращает DataFrame `df` с данными для построения графика.

3. **Функция `plot_interest_distribution`:**
   - Принимает список агентов (`agents`) и опциональные параметры `title` и `show`.
   - Извлекает значения интересов из каждого агента и сохраняет их в список `interests`.
   - Создает Pandas DataFrame `df` из списка `interests` с колонкой "Interests".
   - Строит круговую диаграмму распределения интересов с помощью метода `value_counts().plot.pie()` DataFrame `df`.
   - Устанавливает заголовок графика с помощью `title`.
   - Если параметр `show` равен True, отображает график с помощью `plt.show()`.
   - Возвращает DataFrame `df` с данными для построения графика.


Пример использования
-------------------------
.. code-block:: python

    from tinytroupe.profiling import plot_age_distribution, plot_interest_distribution
    from tinytroupe.agent import TinyPerson
    import pandas as pd
    
    # Пример списка агентов
    agents = [
        TinyPerson(age=25, interests=["reading", "coding"]),
        TinyPerson(age=30, interests=["music", "hiking"]),
        TinyPerson(age=25, interests=["reading", "traveling"]),
        TinyPerson(age=35, interests=["coding", "reading"])
    ]

    # Построение гистограммы распределения возраста
    age_distribution_df = plot_age_distribution(agents, title="Распределение возраста агентов")

    # Построение круговой диаграммы распределения интересов
    interest_distribution_df = plot_interest_distribution(agents, title="Распределение интересов агентов")
    
    # Вывод DataFrame для дальнейшей обработки (необязательно)
    print(age_distribution_df)
    print(interest_distribution_df)