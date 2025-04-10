# Модуль для получения и обработки информации о моделях Vercel AI SDK

## Обзор

Модуль предназначен для извлечения информации о моделях, поддерживаемых Vercel AI SDK, преобразования этой информации в удобный формат и генерации кода для использования этих моделей в проекте `hypotez`.

## Подробней

Модуль выполняет следующие задачи:

1.  Получает HTML-код страницы Vercel AI SDK.
2.  Извлекает пути к JavaScript-файлам, содержащим информацию о моделях.
3.  Получает содержимое этих JavaScript-файлов.
4.  Извлекает информацию о моделях из JavaScript-кода, используя регулярные выражения и QuickJS.
5.  Преобразует полученную информацию в формат, удобный для использования в проекте `hypotez`.
6.  Генерирует код для определения моделей и их параметров.

Модуль использует библиотеки `quickjs`, `curl_cffi` и `re` для выполнения этих задач.

## Функции

### `get_model_info`

```python
def get_model_info() -> dict[str, Any]:
    """
    Извлекает информацию о моделях из Vercel AI SDK.

    Returns:
        dict[str, Any]: Словарь, содержащий информацию о моделях.
    """
```

**Назначение**: Извлечение информации о моделях, предоставляемых Vercel AI SDK, путем анализа HTML-кода и JavaScript-файлов.

**Возвращает**:
-   `dict[str, Any]`: Словарь, где ключи - имена моделей, а значения - их параметры. Возвращает пустой словарь в случае неудачи.

**Как работает функция**:

1.  Получает HTML-код страницы `https://sdk.vercel.ai`.
2.  Ищет в HTML-коде пути к JavaScript-файлам, содержащим информацию о моделях, с использованием регулярного выражения `r"static\\/chunks.+?\\.js"`.
3.  Удаляет из путей разделители с использованием регулярного выражения `r'"\\]\\)<\\/script><script>self\\.__next_f\\.push\\(\\[.,"`.
4.  Формирует полные URL-адреса JavaScript-файлов.
5.  Получает содержимое каждого JavaScript-файла.
6.  Ищет в JavaScript-коде информацию о моделях с использованием регулярного выражения `r'let .="\\\\n\\\\nHuman:\\",r=(.+?),.='`.
7.  Извлекает строку, содержащую информацию о моделях.
8.  Заменяет в строке escape-последовательности для корректной обработки JSON.
9.  Использует QuickJS для преобразования строки в JSON-формат.
10. Десериализует JSON-строку в словарь Python.

```ascii
A: Получение HTML-кода страницы Vercel AI SDK
|
B: Поиск путей к JavaScript-файлам
|
C: Формирование URL-адресов JavaScript-файлов
|
D: Получение содержимого JavaScript-файлов
|
E: Поиск информации о моделях в JavaScript-коде
|
F: Преобразование информации в JSON-формат
|
G: Десериализация JSON-строки в словарь Python
```

**Примеры**:

```python
model_info = get_model_info()
print(model_info)
```

### `convert_model_info`

```python
def convert_model_info(models: dict[str, Any]) -> dict[str, Any]:
    """
    Преобразует информацию о моделях в формат, используемый в проекте.

    Args:
        models (dict[str, Any]): Словарь с информацией о моделях.

    Returns:
        dict[str, Any]: Словарь с преобразованной информацией о моделях.
    """
```

**Назначение**: Преобразование структуры данных, содержащей информацию о моделях, в формат, удобный для дальнейшего использования.

**Параметры**:

-   `models` (`dict[str, Any]`): Словарь, содержащий информацию о моделях (результат работы функции `get_model_info`).

**Возвращает**:

-   `dict[str, Any]`: Словарь, где ключи - имена моделей, а значения - словари, содержащие `id` модели и параметры по умолчанию.

**Как работает функция**:

1.  Итерируется по каждой модели в словаре `models`.
2.  Извлекает параметры модели из ключа `"parameters"`.
3.  Преобразует параметры в параметры по умолчанию с помощью функции `params_to_default_params`.
4.  Создает новый словарь, содержащий `id` модели и параметры по умолчанию.

```ascii
A: Итерация по моделям в словаре
|
B: Извлечение параметров модели
|
C: Преобразование параметров в параметры по умолчанию
|
D: Создание нового словаря с id модели и параметрами по умолчанию
```

**Примеры**:

```python
models = {
    "model1": {"id": "1", "parameters": {"param1": {"value": "a"}, "param2": {"value": "b"}}},
    "model2": {"id": "2", "parameters": {"param3": {"value": "c"}, "param4": {"value": "d"}}},
}
converted_models = convert_model_info(models)
print(converted_models)
```

### `params_to_default_params`

```python
def params_to_default_params(parameters: dict[str, Any]):
    """
    Извлекает значения по умолчанию из параметров модели.

    Args:
        parameters (dict[str, Any]): Словарь с параметрами модели.

    Returns:
        dict[str, Any]: Словарь со значениями по умолчанию для параметров модели.
    """
```

**Назначение**: Извлечение значений по умолчанию из параметров модели и формирование словаря, содержащего только эти значения.

**Параметры**:

-   `parameters` (`dict[str, Any]`): Словарь, содержащий параметры модели.

**Возвращает**:

-   `dict[str, Any]`:: Словарь, где ключи - имена параметров, а значения - их значения по умолчанию.

**Как работает функция**:

1.  Итерируется по каждому параметру в словаре `parameters`.
2.  Извлекает значение параметра из ключа `"value"`.
3.  Если ключ параметра `"maximumLength"`, то он переименовывается в `"maxTokens"`.
4.  Создает новый словарь, содержащий имя параметра и его значение по умолчанию.

```ascii
A: Итерация по параметрам в словаре
|
B: Извлечение значения параметра
|
C: Переименование ключа "maximumLength" в "maxTokens" (если необходимо)
|
D: Создание нового словаря с именем параметра и его значением по умолчанию
```

**Примеры**:

```python
parameters = {"param1": {"value": "a"}, "param2": {"value": "b"}, "maximumLength": {"value": 100}}
default_params = params_to_default_params(parameters)
print(default_params)
```

### `get_model_names`

```python
def get_model_names(model_info: dict[str, Any]):
    """
    Извлекает имена моделей из информации о моделях.

    Args:
        model_info (dict[str, Any]): Словарь с информацией о моделях.

    Returns:
        list[str]: Список имен моделей.
    """
```

**Назначение**: Извлечение списка имен моделей из предоставленного словаря информации о моделях. Исключает определенные модели, такие как `"openai:gpt-4"` и `"openai:gpt-3.5-turbo"`.

**Параметры**:

-   `model_info` (`dict[str, Any]`): Словарь, содержащий информацию о моделях.

**Возвращает**:

-   `list[str]`: Отсортированный список имен моделей, исключая `"openai:gpt-4"` и `"openai:gpt-3.5-turbo"`.

**Как работает функция**:

1.  Извлекает имена моделей из ключей словаря `model_info`.
2.  Фильтрует список, исключая модели `"openai:gpt-4"` и `"openai:gpt-3.5-turbo"`.
3.  Сортирует полученный список имен моделей.

```ascii
A: Извлечение имен моделей из словаря model_info
|
B: Фильтрация списка, исключая "openai:gpt-4" и "openai:gpt-3.5-turbo"
|
C: Сортировка списка имен моделей
```

**Примеры**:

```python
model_info = {
    "model1": {"id": "1"},
    "model2": {"id": "2"},
    "openai:gpt-4": {"id": "3"},
    "openai:gpt-3.5-turbo": {"id": "4"},
}
model_names = get_model_names(model_info)
print(model_names)
```

### `print_providers`

```python
def print_providers(model_names: list[str]):
    """
    Генерирует код для определения моделей и их параметров.

    Args:
        model_names (list[str]): Список имен моделей.
    """
```

**Назначение**: Генерация Python-кода для определения моделей и их базовых провайдеров, используя имена моделей из предоставленного списка.

**Параметры**:

-   `model_names` (`list[str]`): Список имен моделей.

**Как работает функция**:

1.  Итерируется по каждому имени модели в списке `model_names`.
2.  Разделяет имя модели на части, используя разделители `:` и `/`.
3.  Определяет базового провайдера из первой части разделенного имени.
4.  Формирует имя переменной, заменяя символы `-` и `.` на `_` в последней части разделенного имени.
5.  Печатает строку кода, которая определяет модель с указанием имени, базового провайдера и провайдера Vercel.

```ascii
A: Итерация по именам моделей
|
B: Разделение имени модели на части
|
C: Определение базового провайдера
|
D: Формирование имени переменной
|
E: Печать строки кода для определения модели
```

**Примеры**:

```python
model_names = ["provider1:model-name-1", "provider2/model.name.2"]
print_providers(model_names)
```

### `print_convert`

```python
def print_convert(model_names: list[str]):
    """
    Генерирует код для преобразования имен моделей в переменные.

    Args:
        model_names (list[str]): Список имен моделей.
    """
```

**Назначение**: Генерация Python-кода для преобразования имен моделей в переменные, используя имена моделей из предоставленного списка.

**Параметры**:

-   `model_names` (`list[str]`): Список имен моделей.

**Как работает функция**:

1.  Итерируется по каждому имени модели в списке `model_names`.
2.  Разделяет имя модели на части, используя разделители `:` и `/`.
3.  Определяет ключ модели как последнюю часть разделенного имени.
4.  Формирует имя переменной, заменяя символы `-` и `.` на `_` в последней части разделенного имени.
5.  Печатает строку кода, которая связывает ключ модели с соответствующей переменной.

```ascii
A: Итерация по именам моделей
|
B: Разделение имени модели на части
|
C: Определение ключа модели
|
D: Формирование имени переменной
|
E: Печать строки кода для связывания ключа модели с переменной
```

**Примеры**:

```python
model_names = ["provider1:model-name-1", "provider2/model.name.2"]
print_convert(model_names)
```

### `main`

```python
def main():
    """
    Основная функция, которая выполняет получение, преобразование и вывод информации о моделях.
    """
```

**Назначение**: Главная функция модуля, которая координирует выполнение основных задач: получение информации о моделях, её преобразование и вывод в нужном формате.

**Как работает функция**:

1.  Получает информацию о моделях, вызывая функцию `get_model_info`.
2.  Преобразует полученную информацию, вызывая функцию `convert_model_info`.
3.  Выводит преобразованную информацию в формате JSON с отступами, используя `json.dumps`.
4.  Получает список имен моделей, вызывая функцию `get_model_names`.
5.  Выводит разделитель.
6.  Генерирует код для определения моделей и их параметров, вызывая функцию `print_providers`.
7.  Выводит разделитель.
8.  Генерирует код для преобразования имен моделей в переменные, вызывая функцию `print_convert`.

```ascii
A: Получение информации о моделях
|
B: Преобразование информации
|
C: Вывод преобразованной информации в формате JSON
|
D: Получение списка имен моделей
|
E: Генерация кода для определения моделей
|
F: Генерация кода для преобразования имен моделей в переменные
```

**Примеры**:

```python
main()
```