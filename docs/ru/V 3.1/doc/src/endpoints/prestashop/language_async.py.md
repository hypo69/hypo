# Модуль `language_async`

## Обзор

Модуль `language_async.py` предназначен для асинхронного взаимодействия с API PrestaShop для управления языками магазина. Он включает в себя класс `PrestaLanguageAync`, который предоставляет методы для получения информации о языках, а также для выполнения других операций, связанных с языками.

## Подорбней

Этот модуль является частью проекта `hypotez` и обеспечивает функциональность для работы с языками в PrestaShop. Класс `PrestaLanguageAync` наследуется от `PrestaShopAsync`, что позволяет использовать асинхронные запросы к API PrestaShop. Модуль использует `logger` для логирования ошибок и `asyncio` для асинхронного выполнения операций.

## Классы

### `PrestaLanguageAync`

**Описание**: Класс, отвечающий за асинхронные операции с языками магазина PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaLanguageAync`.
- `get_lang_name_by_index`: Возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema`: Получает схему языков из API PrestaShop.

#### `__init__`

```python
    def __init__(self, *args, **kwards):
        """Класс интерфейс взаимодействия языками в Prestashop
        Важно помнить, что у каждого магазина своя нумерация языков
        :lang_string: ISO названия языка. Например: en, ru, he
        """
        ...
```

#### `get_lang_name_by_index`

```python
    async def get_lang_name_by_index(self, lang_index:int|str ) -> str:
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
- Отсутствуют явные исключения, но функция логирует ошибки с помощью `logger.error`.

#### `get_languages_schema`

```python
    async def get_languages_schema(self) -> dict:
        lang_dict = super().get_languages_schema()
        print(lang_dict)
```

**Описание**: Получает схему языков из API PrestaShop.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `dict`: Словарь, представляющий схему языков.

**Вызывает исключения**:
- Отсутствуют явные исключения.

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

**Описание**: Асинхронная функция, демонстрирующая использование класса `PrestaLanguageAync` для получения схемы языков.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:

Пример вызова асинхронной функции `main`:

```python
if __name__ == '__main__':
    asyncio.run(main())
```