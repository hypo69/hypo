# Модуль `language_async`

## Обзор

Модуль `language_async` предоставляет асинхронный класс `PrestaLanguageAync` для управления языками в магазине PrestaShop. Он позволяет добавлять, удалять, обновлять и получать детали о языках, используя асинхронные запросы к API PrestaShop.

## Подробней

Модуль предназначен для работы с языками в PrestaShop, предоставляя асинхронные методы для выполнения различных операций, таких как получение информации о языке по его индексу или получение схемы языков. Класс `PrestaLanguageAync` наследуется от `PrestaShopAsync`, что позволяет использовать асинхронные запросы для взаимодействия с API PrestaShop. Расположение файла в структуре проекта указывает на то, что он является частью endpoints для работы с PrestaShop.

## Классы

### `PrestaLanguageAync`

**Описание**: Класс `PrestaLanguageAync` предоставляет интерфейс для взаимодействия с языками в PrestaShop с использованием асинхронных запросов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaLanguageAync`.
- `get_lang_name_by_index`: Возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema`: Получает схему языков из PrestaShop.

#### `__init__`

```python
def __init__(self, *args, **kwards):
    """Класс интерфейс взаимодействия языками в Prestashop
    Важно помнить, что у каждого магазина своя нумерация языков
    :lang_string: ISO названия языка. Например: en, ru, he
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `PrestaLanguageAync`. Важно помнить, что у каждого магазина своя нумерация языков.

**Параметры**:
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

#### `get_lang_name_by_index`

```python
async def get_lang_name_by_index(self, lang_index:int|str ) -> str:
    """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
```

**Описание**: Возвращает имя языка ISO по его индексу в таблице PrestaShop.

**Параметры**:
- `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:
- `str`: Имя языка ISO.

**Примеры**:
```python
lang_class = PrestaLanguageAync()
lang_name = await lang_class.get_lang_name_by_index(1)
print(lang_name)
```

#### `get_languages_schema`

```python
async def get_languages_schema(self) -> dict:
    lang_dict = super().get_languages_schema()
    print(lang_dict)
```

**Описание**: Получает схему языков из PrestaShop.

**Возвращает**:
- `dict`: Схема языков.

**Примеры**:
```python
lang_class = PrestaLanguageAync()
languages_schema = await lang_class.get_languages_schema()
print(languages_schema)
```

## Функции

### `main`

```python
async def main():
    """"""
    ...
    lang_class = PrestaLanguageAync()
    languagas_schema = await  lang_class.get_languages_schema()
    print(languagas_schema)
```

**Описание**: Асинхронная функция `main`, которая создает экземпляр класса `PrestaLanguageAync` и получает схему языков.

**Примеры**:
```python
asyncio.run(main())
```