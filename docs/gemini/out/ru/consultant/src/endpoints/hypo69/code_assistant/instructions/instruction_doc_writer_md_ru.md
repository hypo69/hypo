# ИНСТРУКЦИЯ ПО СОЗДАНИЮ ДОКУМЕНТАЦИИ

##  Описание

Данная инструкция описывает формат и требования к документации Python-кода.  Документация будет создаваться в формате Markdown (.md) и должна включать подробное описание функций, классов и модулей.


##  Структура документации

Каждый файл документации должен иметь следующую структуру:

1. **Заголовок**: Заголовок первого уровня (#) с названием модуля.
2. **Обзор**: Заголовок второго уровня (##) с кратким описанием назначения модуля.
3. **Оглавление**: Заголовок второго уровня (##) с содержанием (TOC) ссылок на все основные разделы документации.
4. **Классы**: Заголовок второго уровня (##) с описанием классов и их методов.
5. **Функции**: Заголовок второго уровня (##) с описанием функций и их параметров, возвращаемых значений и исключений.

**Пример структуры документации:**

```markdown
# Модуль обработки данных

## Обзор

Этот модуль предоставляет инструменты для обработки данных из различных источников.

## Оглавление

- [Классы](#классы)
- [Функции](#функции)

## Классы

### `DataProcessor`

**Описание**: Класс для обработки данных.

**Методы**:
- `process_data`: Обрабатывает входные данные.

## Функции

### `load_data`

**Описание**: Загружает данные из файла.

**Параметры**:
- `filename` (str): Имя файла.

**Возвращает**:
- `list`: Список загруженных данных.


**Вызывает исключения**:
- `FileNotFoundError`: Если файл не найден.


```

##  Формат комментариев

Комментарии к функциям, классам и методам должны быть в формате Markdown и включать следующие разделы:

- **Описание**: Краткое описание функциональности.
- **Параметры**: Список параметров с типами и описанием.
- **Возвращает**: Описание возвращаемого значения.
- **Вызывает исключения**: Список исключений, которые могут быть вызваны.

```python
def my_function(param1: str, param2: int = 0) -> str:
    """
    Описание функции.

    Args:
        param1 (str): Описание параметра 1.
        param2 (int, optional): Описание параметра 2. Defaults to 0.

    Returns:
        str: Описание возвращаемого значения.

    Raises:
        TypeError: Если введен неверный тип данных.
    """
    # Тело функции
    return "Результат"
```



##  Использование Markdown

Используйте стандартные элементы Markdown для форматирования текста, списков, ссылок и кода.


##  Требования к стилю кода

Следуйте стандартному стилю кода для Python (PEP 8). Используйте одинарные кавычки (`) для строк в Python-коде.


##  Обработка ошибок

При обработке ошибок используйте `logger.error()` для записи сообщений об ошибках и исключениях.



##  Примеры

(Примеры документации и улучшений кода должны быть добавлены здесь).



##  Порядок блоков в ответе


1.  **Исходный код:**  <Предоставленный код>
2.  **Улучшенный код:**  <Код с улучшениями>
3.  **Внесённые изменения:**  <Список изменений>
4.  **Оптимизированный код:**  <Итоговый код>


```


```

**КОНЕЦ ИНСТРУКЦИИ**