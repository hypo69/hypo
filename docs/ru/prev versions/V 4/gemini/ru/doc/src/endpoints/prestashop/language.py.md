# Модуль `language.py`

## Обзор

Модуль `language.py` предназначен для управления языками в интернет-магазине PrestaShop. Он предоставляет класс `PrestaLanguage`, который позволяет добавлять, удалять, обновлять и получать информацию о языках магазина через API PrestaShop. Этот модуль является частью подсистемы интеграции с PrestaShop и обеспечивает возможность программного управления языковыми настройками магазина.

## Подробней

Модуль предоставляет интерфейс для взаимодействия с API PrestaShop для управления языками магазина. Он использует класс `PrestaShop` для установления соединения и выполнения запросов к API. Класс `PrestaLanguage` включает методы для получения схемы языков, получения имени языка по индексу и выполнения других операций, связанных с языками PrestaShop.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предоставляет методы для управления языками в PrestaShop. Он наследуется от класса `PrestaShop` и использует его для взаимодействия с API PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaLanguage`.
- `get_lang_name_by_index`: Возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema`: Получает схему языков.

**Параметры**:
- `*args`: Произвольные позиционные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.
- `**kwards`: Произвольные именованные аргументы, передаваемые в конструктор родительского класса `PrestaShop`.

**Примеры**

```python
prestalanguage = PrestaLanguage(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
language_name = prestalanguage.get_lang_name_by_index(1)
print(language_name)
language_schema = prestalanguage.get_languages_schema()
print(language_schema)
```

## Функции

### `get_lang_name_by_index`

```python
def get_lang_name_by_index(self, lang_index:int|str ) -> str:
    """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
```

**Описание**: Возвращает имя языка ISO по его индексу в таблице PrestaShop.

**Параметры**:
- `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:
- `str`: Имя языка ISO или пустую строку в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения языка по индексу.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
language_name = prestalanguage.get_lang_name_by_index(1)
print(language_name)
```

### `get_languages_schema`

```python
def get_languages_schema(self) -> Optional[dict]:
    """Get the schema for languages.
    :return: Language schema or `None` on failure.
    :rtype: dict
    """
```

**Описание**: Получает схему языков из API PrestaShop.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `Optional[dict]`: Схема языков в виде словаря или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения схемы языков.

**Примеры**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
language_schema = prestalanguage.get_languages_schema()
print(language_schema)
```

### `main`

```python
async def main():
    """"""
```

**Описание**: Асинхронная функция, используемая для демонстрации получения схемы языков.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Примеры**:

```python
asyncio.run(main())
```