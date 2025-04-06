# Модуль `language_async.py`

## Обзор

Модуль `language_async.py` предназначен для асинхронного взаимодействия с API PrestaShop для управления языками магазина. Он содержит класс `PrestaLanguageAync`, который предоставляет методы для получения информации о языках, таких как получение имени языка по его индексу.

## Подробней

Этот модуль предоставляет асинхронные функции для взаимодействия с языковыми настройками в PrestaShop. Класс `PrestaLanguageAync` наследуется от `PrestaShopAsync` и включает методы для получения информации о языках.
Расположение файла в проекте: `hypotez/src/endpoints/prestashop/language_async.py` указывает, что этот модуль является частью подсистемы для взаимодействия с PrestaShop, в частности, для работы с языками.

## Классы

### `PrestaLanguageAync`

**Описание**: Класс `PrestaLanguageAync` предоставляет интерфейс для асинхронного взаимодействия с языками в PrestaShop.
**Наследует**:
- `PrestaShopAsync`: асинхронный класс для работы с API PrestaShop.

**Аттрибуты**:
- Отсутствуют явно объявленные атрибуты, но класс наследует атрибуты от `PrestaShopAsync`.

**Методы**:
- `__init__(self, *args, **kwards)`: инициализирует экземпляр класса.
- `get_lang_name_by_index(self, lang_index: int | str) -> str`: возвращает имя языка ISO по его индексу в таблице PrestaShop.
- `get_languages_schema(self) -> dict`: запрашивает схему языков из PrestaShop.

## Функции

### `get_lang_name_by_index`

```python
    async def get_lang_name_by_index(self, lang_index:int|str ) -> str:
        """Возвращает имя языка ISO по его индексу в таблице Prestashop"""
```

**Назначение**: Возвращает имя языка ISO по его индексу в таблице PrestaShop.

**Параметры**:
- `lang_index` (int | str): Индекс языка, для которого необходимо получить имя.

**Возвращает**:
- `str`: Имя языка ISO или пустую строку в случае ошибки.

**Вызывает исключения**:
- `Exception`: Логируется в случае возникновения ошибки при получении языка по индексу.

**Как работает функция**:
1. Функция пытается получить имя языка ISO по его индексу, используя метод `super().get()` из родительского класса `PrestaShopAsync`.
2. Если возникает исключение, оно логируется, и возвращается пустая строка.

```
A: Получение имени языка по индексу
|
B: Обработка исключения
|
C: Возврат результата
```

**Примеры**:

```python
lang_class = PrestaLanguageAync()
lang_name = await lang_class.get_lang_name_by_index(1)
print(lang_name)
```

### `get_languages_schema`

```python
    async def get_languages_schema(self) -> dict:
        lang_dict = super().get_languages_schema()
        print(lang_dict)
```

**Назначение**: Запрашивает схему языков из PrestaShop.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- `dict`: Cхема языков PrestaShop.

**Как работает функция**:

1. Функция вызывает метод `super().get_languages_schema()` для получения схемы языков.
2. Полученная схема выводится в консоль с использованием функции `print`.

```
A: Получение схемы языков
|
B: Вывод схемы языков в консоль
```

**Примеры**:

```python
lang_class = PrestaLanguageAync()
languages_schema = await lang_class.get_languages_schema()
```

### `main`

```python
async def main():
    """"""
    ...
    lang_class = PrestaLanguageAync()
    languagas_schema = await  lang_class.get_languages_schema()
    print(languagas_schema)
```

**Назначение**: Асинхронная функция для демонстрации работы с классом `PrestaLanguageAync`.

**Параметры**:
- Отсутствуют.

**Как работает функция**:

1. Создается экземпляр класса `PrestaLanguageAync`.
2. Запрашивается схема языков с использованием метода `get_languages_schema()`.
3. Полученная схема выводится в консоль с использованием функции `print`.

```
A: Создание экземпляра класса PrestaLanguageAync
|
B: Получение схемы языков
|
C: Вывод схемы языков в консоль
```

**Примеры**:
```python
async def main():
    lang_class = PrestaLanguageAync()
    languages_schema = await lang_class.get_languages_schema()
    print(languages_schema)

asyncio.run(main())