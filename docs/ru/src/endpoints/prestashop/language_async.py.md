# src.endpoints.prestashop.language_async

## Обзор

Модуль `src.endpoints.prestashop.language_async` предназначен для асинхронного управления языками в магазине PrestaShop. Он предоставляет класс `PrestaLanguageAync`, который позволяет получать информацию о языках, используя API PrestaShop. Модуль использует асинхронный подход для выполнения операций, что позволяет повысить производительность при взаимодействии с API.

## Подробней

Этот модуль предоставляет асинхронный интерфейс для взаимодействия с API PrestaShop для управления языками. Он включает в себя методы для получения информации о языке по его индексу и получения схемы языков.
`PrestaLanguageAync` является подклассом `PrestaShopAsync` и использует его методы для выполнения HTTP-запросов к API PrestaShop.
Модуль использует `logger` для регистрации ошибок и `pprint` для форматированного вывода данных.

## Классы

### `PrestaLanguageAync`

**Описание**: Класс `PrestaLanguageAync` предоставляет методы для асинхронного управления языками в PrestaShop.

 **Как работает класс**:
Класс `PrestaLanguageAync` инициализируется с использованием аргументов и ключевых слов, переданных в конструктор. Он наследуется от класса `PrestaShopAsync`, что позволяет ему использовать методы для взаимодействия с API PrestaShop. Основная задача класса - предоставление асинхронных методов для получения информации о языках в PrestaShop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `PrestaLanguageAync`.
- `get_lang_name_by_index`: Возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema`: Получает схему языков из PrestaShop.

   **Параметры**: # если есть параметры
   - `args` (tuple): Произвольные позиционные аргументы.
   - `kwards` (dict): Произвольные именованные аргументы.

#### `__init__`

```python
    def __init__(self, *args, **kwards):
        """Класс интерфейс взаимодействия языками в Prestashop
        Важно помнить, что у каждого магазина своя нумерация языков
        :lang_string: ISO названия языка. Например: en, ru, he
        """
        ...
```

**Описание**: Инициализирует экземпляр класса `PrestaLanguageAync`.

**Как работает метод**:
Метод `__init__` является конструктором класса `PrestaLanguageAync`. Он принимает произвольные позиционные и именованные аргументы, которые могут использоваться для инициализации родительского класса или других атрибутов экземпляра класса. Важно помнить, что у каждого магазина своя нумерация языков.

   **Параметры**: # если есть параметры
   - `args` (tuple): Произвольные позиционные аргументы.
   - `kwards` (dict): Произвольные именованные аргументы.

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

**Как работает метод**:
Метод `get_lang_name_by_index` принимает индекс языка в качестве аргумента и использует метод `get` родительского класса (`PrestaShopAsync`) для выполнения запроса к API PrestaShop. Запрос направлен на получение информации о языке с указанным индексом. В случае успешного выполнения запроса возвращается имя языка ISO. Если происходит ошибка, она регистрируется с помощью `logger.error`, и возвращается пустая строка.

**Параметры**:
- `lang_index` (int | str): Индекс языка в таблице PrestaShop.

**Возвращает**:
- `str`: Имя языка ISO или пустая строка в случае ошибки.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API PrestaShop.

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

**Как работает метод**:
Метод `get_languages_schema` вызывает метод `get_languages_schema` родительского класса (`PrestaShopAsync`) для получения схемы языков из API PrestaShop. Полученная схема языков сохраняется в переменной `lang_dict`, а затем выводится с использованием функции `print`.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `dict`: Схема языков из PrestaShop.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API PrestaShop.

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

**Описание**: Функция `main` является асинхронной функцией, которая демонстрирует использование класса `PrestaLanguageAync` для получения схемы языков.

**Как работает функция**:
Функция `main` создает экземпляр класса `PrestaLanguageAync` и вызывает метод `get_languages_schema` для получения схемы языков из PrestaShop. Полученная схема языков выводится с использованием функции `print`.

**Параметры**:
- Отсутствуют

**Возвращает**:
- Отсутствует

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API PrestaShop.

**Примеры**:
```python
asyncio.run(main())
```