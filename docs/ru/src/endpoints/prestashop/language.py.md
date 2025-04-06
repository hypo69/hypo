# Модуль для работы с языками в PrestaShop
## Обзор

Модуль `language.py` предоставляет интерфейс для взаимодействия с сущностью `language` в CMS PrestaShop через PrestaShop API. Он позволяет выполнять операции, такие как добавление, удаление, обновление и получение информации о языках в магазине PrestaShop.

## Подробнее

Этот модуль предназначен для автоматизации управления языками в PrestaShop. Он включает в себя класс `PrestaLanguage`, который наследуется от класса `PrestaShop` и предоставляет методы для работы с языками через API PrestaShop.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предназначен для управления языками в магазине PrestaShop. Он предоставляет методы для добавления, удаления, обновления и получения информации о языках.

**Наследует**:
- `PrestaShop`: Класс `PrestaLanguage` наследует функциональность для взаимодействия с API PrestaShop от класса `PrestaShop`.

**Атрибуты**:
- Отсутствуют явно определенные атрибуты в коде, но класс наследует атрибуты от родительского класса `PrestaShop`, такие как параметры подключения к API.

**Методы**:
- `__init__(self, *args, **kwards)`: Инициализирует экземпляр класса `PrestaLanguage`.
- `get_lang_name_by_index(self, lang_index: int | str) -> str`: Получает ISO код языка по его индексу в PrestaShop.
- `get_languages_schema(self) -> Optional[dict]`: Получает схему языков для магазина.

### `__init__(self, *args, **kwards)`

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

**Назначение**: Инициализирует экземпляр класса `PrestaLanguage`.

**Параметры**:
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор.

**Как работает функция**:
1. Функция `__init__` является конструктором класса `PrestaLanguage`.
2. Принимает произвольные позиционные и именованные аргументы.
3. Важно помнить, что у каждого магазина своя нумерация языков.
4. В данном примере, языки в базах данных определяются в следующем порядке: `en` - 1, `he` - 2, `ru` - 3.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN="your_api_domain", API_KEY="your_api_key")
```

### `get_lang_name_by_index(self, lang_index: int | str) -> str`

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

**Назначение**: Извлекает ISO код языка из магазина PrestaShop по его индексу.

**Параметры**:
- `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:
- `str`: Имя языка ISO по его индексу в таблице PrestaShop. В случае ошибки возвращает пустую строку.

**Вызывает исключения**:
- `Exception`: В случае ошибки при получении данных о языке, информация об ошибке логируется.

**Как работает функция**:
1. Функция `get_lang_name_by_index` пытается получить ISO код языка из PrestaShop по указанному индексу.
2. Использует метод `get` родительского класса `PrestaShop` для выполнения API-запроса.
3. В случае успешного запроса возвращает имя языка.
4. Если происходит ошибка (например, язык с указанным индексом не найден), функция логирует ошибку и возвращает пустую строку.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN="your_api_domain", API_KEY="your_api_key")
language_name = prestalanguage.get_lang_name_by_index(1)
print(language_name)
```

ASCII схема работы функции:

```
Начало
  │
  ├── Получение ISO кода языка по индексу (lang_index) из PrestaShop API
  │   │
  │   Успех:
  │   └── Возврат имени языка
  │
  └── Ошибка:
      ├── Логирование ошибки
      └── Возврат пустой строки
  │
Конец
```

### `get_languages_schema(self) -> Optional[dict]`

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

**Назначение**: Извлекает словарь актуальных языков для данного магазина PrestaShop.

**Возвращает**:
- `Optional[dict]`: Схема языков в виде словаря или `None` в случае неудачи.

**Вызывает исключения**:
- `Exception`: В случае ошибки при получении данных о языках, информация об ошибке логируется.

**Как работает функция**:
1. Функция `get_languages_schema` пытается получить схему языков из PrestaShop.
2. Использует метод `_exec` для выполнения API-запроса к ресурсу `languages`.
3. В случае успешного запроса возвращает схему языков в формате JSON.
4. Если происходит ошибка, функция логирует ошибку и возвращает `None`.

ASCII схема работы функции:

```
Начало
  │
  ├── Получение схемы языков из PrestaShop API
  │   │
  │   Успех:
  │   └── Возврат схемы языков в формате JSON
  │
  └── Ошибка:
      ├── Логирование ошибки
      └── Возврат None
  │
Конец
```

## Функции

### `main()`

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

**Назначение**: Пример асинхронного использования класса `PrestaLanguage` для получения схемы языков.

**Как работает функция**:
1. Функция `main` является асинхронной функцией.
2. Создает экземпляр класса `PrestaLanguage`.
3. Вызывает метод `get_languages_schema` для получения схемы языков.
4. Выводит полученную схему языков в консоль.

**Примеры**:

```python
asyncio.run(main())