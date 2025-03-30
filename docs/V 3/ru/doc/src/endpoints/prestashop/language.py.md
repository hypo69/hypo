# Модуль `language`

## Обзор

Модуль `language.py` предназначен для взаимодействия с языковыми настройками магазина PrestaShop. Он предоставляет класс `PrestaLanguage`, который позволяет добавлять, удалять, обновлять и получать информацию о языках в PrestaShop.

## Подробней

Этот модуль обеспечивает интерфейс для управления языками в PrestaShop через API. Он включает в себя функциональность для получения схемы языков, получения имени языка по индексу и выполнения других операций, связанных с языками магазина. Класс `PrestaLanguage` наследуется от класса `PrestaShop` и использует его методы для выполнения API-запросов.

## Классы

### `PrestaLanguage`

**Описание**: Класс для управления языками в PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaLanguage`.
- `get_lang_name_by_index`: Возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema`: Получает схему для языков.

#### `__init__`

```python
def __init__(self, *args, **kwards):
    """Класс интерфейс взаимодействия языками в Prestashop
    Важно помнить, что у каждого магазина своя нумерация языков
    :lang_string: ISO названия языка. Например: en, ru, he
    """
    ...
```

**Описание**: Конструктор класса `PrestaLanguage`. Инициализирует интерфейс взаимодействия с языками в PrestaShop. Важно помнить, что у каждого магазина своя нумерация языков.

**Параметры**:
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

#### `get_lang_name_by_index`

```python
def get_lang_name_by_index(self, lang_index:int|str ) -> str:
    """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
    try:
        return super().get('languagaes', resource_id=str(lang_index), display='full', io_format='JSON')
    except Exception as ex:
        logger.error(f"Ошибка получения языка по индексу {lang_index=}", ex)
        return ''
```

**Описание**: Возвращает имя языка ISO по его индексу в таблице PrestaShop.

**Параметры**:
- `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:
- `str`: Имя языка ISO или пустая строка в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения языка по индексу.

#### `get_languages_schema`

```python
def get_languages_schema(self) -> Optional[dict]:
    """Get the schema for languages.

    :return: Language schema or `None` on failure.
    :rtype: dict
    """
    try:
        response = self._exec('languages', display='full', io_format='JSON')
        return response
    except Exception as ex:
        logger.error(f'Error:', ex)
        return
```

**Описание**: Получает схему для языков.

**Возвращает**:
- `Optional[dict]`: Схема языков или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения схемы языков.

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

**Описание**: Асинхронная функция, которая создает экземпляр класса `PrestaLanguageAync` и получает схему языков.

**Примеры**:

```python
import asyncio

async def main():
    lang_class = PrestaLanguageAync()
    languages_schema = await lang_class.get_languages_schema()
    print(languages_schema)

if __name__ == '__main__':
    asyncio.run(main())
```