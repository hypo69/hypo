# profiling.py

## Обзор

Этот модуль предоставляет механизмы для анализа характеристик популяций агентов, таких как их распределение по возрасту и типичные интересы.

## Оглавление

- [Функции](#Функции)
    - [`plot_age_distribution`](#plot_age_distribution)
    - [`plot_interest_distribution`](#plot_interest_distribution)

## Функции

### `plot_age_distribution`

**Описание**: Строит график распределения возрастов заданных агентов.

**Параметры**:
- `agents` (List[TinyPerson]): Список агентов, чье распределение возрастов необходимо построить.
- `title` (str, optional): Заголовок графика. По умолчанию "Age Distribution".
- `show` (bool, optional): Определяет, нужно ли отображать график. По умолчанию `True`.

**Возвращает**:
- `pd.DataFrame`: Данные, использованные для построения графика.

### `plot_interest_distribution`

**Описание**: Строит график распределения интересов заданных агентов.

**Параметры**:
- `agents` (List[TinyPerson]): Список агентов, чье распределение интересов необходимо построить.
- `title` (str, optional): Заголовок графика. По умолчанию "Interest Distribution".
- `show` (bool, optional): Определяет, нужно ли отображать график. По умолчанию `True`.

**Возвращает**:
- `pd.DataFrame`: Данные, использованные для построения графика.