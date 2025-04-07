# Модуль для работы с языками в PrestaShop

## Обзор

Модуль `language.py` предназначен для взаимодействия с сущностью `language` в CMS PrestaShop через PrestaShop API. Он предоставляет класс `PrestaLanguage`, который позволяет управлять языками магазина, такими как добавление, удаление, обновление и получение информации о языках.

## Подробнее

Этот модуль обеспечивает интерфейс для работы с языками в PrestaShop, позволяя автоматизировать задачи, связанные с управлением локализацией магазина. Он использует API PrestaShop для выполнения операций и обрабатывает возможные ошибки, логируя их с помощью модуля `src.logger`.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` наследует класс `PrestaShop` и предоставляет методы для управления языками магазина PrestaShop.

**Принцип работы**:
1.  Инициализация класса `PrestaLanguage` наследует параметры подключения к API PrestaShop от родительского класса `PrestaShop`.
2.  Метод `get_lang_name_by_index` позволяет получить ISO-код языка по его индексу в таблице PrestaShop.
3.  Метод `get_languages_schema` возвращает словарь с информацией о языках, доступных в магазине.

**Методы**:

*   `__init__(self, *args, **kwards)`:
    *   **Описание**: Конструктор класса `PrestaLanguage`.
    *   **Параметры**:
        *   `*args`: Произвольные аргументы.
        *   `**kwards`: Произвольные именованные аргументы.
    *   **Пример**:

        ```python
        prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        ```
*   `get_lang_name_by_index(self, lang_index: int | str) -> str`:
    *   **Описание**: Функция извлекает ISO код языка из магазина `Prestashop`.
    *   **Параметры**:
        *   `lang_index` (int | str): Индекс языка в таблице PrestaShop.
    *   **Возвращает**:
        *   `str`: Имя языка ISO по его индексу в таблице PrestaShop.
    *   **Пример**:

        ```python
        lang_name = prestalanguage.get_lang_name_by_index(1)
        ```
*   `get_languages_schema(self) -> Optional[dict]`:
    *   **Описание**: Функция извлекает словарь актуальных языков для данного магазина.
    *   **Возвращает**:
        *   `Optional[dict]`: Language schema or `None` on failure.
    *   **Пример**:

        ```python
        languages_schema = prestalanguage.get_languages_schema()
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

**Назначение**: Пример асинхронной функции для демонстрации получения схемы языков.

**Как работает функция**:

1.  **Создание экземпляра класса `PrestaLanguage`**: Создается экземпляр класса `PrestaLanguage`, который используется для взаимодействия с API PrestaShop.
2.  **Получение схемы языков**: Вызывается метод `get_languages_schema` для получения информации о языках, доступных в магазине.
3.  **Вывод схемы языков**: Полученная схема языков выводится на экран.

```
    Создание экземпляра класса PrestaLanguage
    │
    └── Получение схемы языков (get_languages_schema)
        │
        └── Вывод схемы языков
```

**Примеры**:

```python
asyncio.run(main())