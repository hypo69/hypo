# Модуль profiling

## Обзор

Этот модуль предоставляет механизмы для анализа характеристик популяции агентов, таких как распределение возраста, типичные интересы и т.д.  В соответствии с руководством, все функции построения графиков также возвращают Pandas DataFrame с данными, использованными для построения.

## Функции

### `plot_age_distribution`

**Описание**: Строит гистограмму распределения возраста агентов.

**Параметры**:
- `agents` (List[TinyPerson]): Список агентов, для которых нужно построить распределение возраста.
- `title` (str, optional): Заголовок графика. По умолчанию "Распределение возраста".
- `show` (bool, optional): Флаг, указывающий, нужно ли отображать график. По умолчанию `True`.

**Возвращает**:
- `pd.DataFrame`: Pandas DataFrame с данными, использованными для построения гистограммы.

### `plot_interest_distribution`

**Описание**: Строит круговую диаграмму распределения интересов агентов.

**Параметры**:
- `agents` (List[TinyPerson]): Список агентов, для которых нужно построить распределение интересов.
- `title` (str, optional): Заголовок графика. По умолчанию "Распределение интересов".
- `show` (bool, optional): Флаг, указывающий, нужно ли отображать график. По умолчанию `True`.

**Возвращает**:
- `pd.DataFrame`: Pandas DataFrame с данными, использованными для построения круговой диаграммы.