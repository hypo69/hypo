# Модуль `language.py`

## Обзор

Модуль `language.py` предназначен для работы с языками в PrestaShop. Он предоставляет интерфейс для взаимодействия с сущностью `language` в CMS PrestaShop через API PrestaShop. Модуль включает класс `PrestaLanguage`, который позволяет выполнять различные операции, такие как добавление, удаление и обновление языков в магазине PrestaShop.

## Подробней

Этот модуль облегчает управление языковыми настройками в PrestaShop, позволяя автоматизировать задачи, связанные с языками, такие как получение информации о языках, добавление новых языков, удаление существующих и обновление информации о языках. Он использует API PrestaShop для взаимодействия с CMS и предоставляет удобный интерфейс для выполнения этих операций.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предоставляет методы для взаимодействия с языками в магазине PrestaShop. Он наследуется от класса `PrestaShop` и использует его API для выполнения операций.

**Как работает класс**:

1.  При инициализации класса `PrestaLanguage` происходит инициализация базового класса `PrestaShop`.
2.  Метод `get_lang_name_by_index` используется для получения ISO-кода языка по его индексу в таблице PrestaShop.
3.  Метод `get_languages_schema` используется для получения словаря актуальных языков для данного магазина.
4.  Методы `add_language_PrestaShop`, `delete_language_PrestaShop` и `update_language_PrestaShop` используются для добавления, удаления и обновления языков соответственно.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `PrestaLanguage`.
*   `get_lang_name_by_index`: Извлекает ISO код языка из магазина `Prestashop`.
*   `get_languages_schema`: Извлекает словарь актуальных языков для данного магазина.

#### `__init__`

```python
def __init__(self, *args, **kwards):
    """
    Args:
        *args: Произвольные аргументы.
        **kwards: Произвольные именованные аргументы.

    Note:
        Важно помнить, что у каждого магазина своя нумерация языков.
        Я определяю языки в своих базах в таком порядке:
        `en` - 1;
        `he` - 2;
        `ru` - 3.
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `PrestaLanguage`.

**Как работает функция**:

Выполняет инициализацию базового класса `PrestaShop`.

**Параметры**:

*   `*args`: Произвольные аргументы.
*   `**kwards`: Произвольные именованные аргументы.

#### `get_lang_name_by_index`

```python
def get_lang_name_by_index(self, lang_index: int | str) -> str:
    """
    Функция извлекает ISO код азыка из магазина `Prestashop`

    Args:
        lang_index: Индекс языка в таблице PrestaShop.

    Returns:
        Имя языка ISO по его индексу в таблице PrestaShop.
    """
```

**Описание**: Извлекает ISO код языка из магазина `Prestashop`.

**Как работает функция**:

1.  Пытается получить язык из API PrestaShop по указанному индексу.
2.  В случае успеха возвращает ISO-код языка.
3.  В случае ошибки логирует ошибку и возвращает пустую строку.

**Параметры**:

*   `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:

*   `str`: Имя языка ISO по его индексу в таблице PrestaShop.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
lang_name = prestalanguage.get_lang_name_by_index(1)
print(lang_name)
```

#### `get_languages_schema`

```python
def get_languages_schema(self) -> Optional[dict]:
    """Функция извлекает словарь актуальных языков дла данного магазина.

    Returns:
        Language schema or `None` on failure.

    Examples:
        # Возвращаемый словарь:
        {
            "languages": {
                    "language": [
                                    {
                                    "attrs": {
                                        "id": "1"
                                    },
                                    "value": ""
                                    },
                                    {
                                    "attrs": {
                                        "id": "2"
                                    },
                                    "value": ""
                                    },
                                    {
                                    "attrs": {
                                        "id": "3"
                                    },
                                    "value": ""
                                    }
                                ]
            }
        }
    """
```

**Описание**: Извлекает словарь актуальных языков для данного магазина.

**Как работает функция**:

1.  Вызывает метод `_exec` для получения списка языков из API PrestaShop.
2.  Возвращает полученный словарь.
3.  В случае ошибки логирует ошибку и возвращает `None`.

**Возвращает**:

*   `Optional[dict]`: Language schema or `None` on failure.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
languages_schema = prestalanguage.get_languages_schema()
print(languages_schema)
```

## Функции

### `main`

```python
async def main():
    """
    Example:
        >>> asyncio.run(main())
    """
    ...
    lang_class = PrestaLanguage()
    languagas_schema = await lang_class.get_languages_schema()
    print(languagas_schema)
```

**Описание**: Функция `main` является асинхронной функцией, которая демонстрирует использование класса `PrestaLanguage` для получения схемы языков.

**Как работает функция**:

1.  Создает экземпляр класса `PrestaLanguage`.
2.  Вызывает метод `get_languages_schema` для получения схемы языков.
3.  Выводит полученную схему языков.

**Примеры**:

```python
asyncio.run(main())