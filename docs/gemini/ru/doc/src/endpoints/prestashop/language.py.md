# Модуль `language`

## Обзор

Модуль `language` предназначен для работы с языками в PrestaShop. Он предоставляет интерфейс взаимодействия с сущностью `language` в CMS PrestaShop через API PrestaShop. Модуль включает класс `PrestaLanguage`, который позволяет добавлять, удалять, обновлять и получать информацию о языках в магазине PrestaShop.

## Подробнее

Этот модуль является частью проекта `hypotez` и обеспечивает функциональность для управления языковыми настройками в PrestaShop. Он использует API PrestaShop для выполнения операций с языками. Важно помнить, что у каждого магазина своя нумерация языков.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` отвечает за настройки языков магазина PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для управления языками через API PrestaShop.

**Как работает класс**:
1.  При инициализации класса происходит подключение к API PrestaShop.
2.  Методы класса позволяют выполнять операции добавления, удаления, обновления и получения информации о языках в магазине PrestaShop.
3.  Класс использует модуль `logger` для логирования ошибок и отладочной информации.

**Методы**:

*   `__init__`: Инициализирует экземпляр класса `PrestaLanguage`.
*   `get_lang_name_by_index`: Извлекает ISO код языка из магазина PrestaShop по его индексу.
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

**Как работает метод**:
Метод `__init__` инициализирует класс `PrestaLanguage`, принимая произвольные аргументы и именованные аргументы. Внутри метода происходит инициализация родительского класса `PrestaShop`.

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
    try:
        return super().get('languagaes', resource_id=str(lang_index), display='full', io_format='JSON')
    except Exception as ex:
        logger.error(f'Ошибка получения языка по индексу {lang_index=}', ex)
        return ''
```

**Описание**: Извлекает ISO код языка из магазина PrestaShop по его индексу.

**Как работает метод**:

1.  Функция `get_lang_name_by_index` пытается получить имя языка по его индексу, используя метод `get` родительского класса `PrestaShop`.
2.  Если получение имени языка прошло успешно, функция возвращает имя языка.
3.  Если во время выполнения возникла ошибка, функция логирует ошибку с помощью `logger.error` и возвращает пустую строку.

**Параметры**:

*   `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:

*   str: Имя языка ISO по его индексу в таблице PrestaShop.

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
    try:
        response = self._exec('languages', display='full', io_format='JSON')
        return response
    except Exception as ex:
        logger.error(f'Error:', ex)
        return
```

**Описание**: Извлекает словарь актуальных языков для данного магазина.

**Как работает метод**:

1.  Функция `get_languages_schema` пытается получить схему языков, используя метод `_exec`.
2.  Если получение схемы прошло успешно, функция возвращает схему языков.
3.  Если во время выполнения возникла ошибка, функция логирует ошибку с помощью `logger.error` и возвращает `None`.

**Возвращает**:

*   Optional[dict]: Language schema or `None` on failure.

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

**Описание**: Функция `main` является точкой входа для асинхронного выполнения операций с языками PrestaShop.

**Как работает функция**:

1.  Создается экземпляр класса `PrestaLanguage`.
2.  Вызывается метод `get_languages_schema` для получения схемы языков.
3.  Схема языков выводится в консоль с помощью функции `print`.

**Примеры**:

```python
asyncio.run(main())