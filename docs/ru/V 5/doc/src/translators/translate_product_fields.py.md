# Модуль `translate_product_fields`

## Обзор

Модуль `translate_product_fields` предназначен для управления переводами полей товаров. Он обеспечивает связь между словарем полей товара, таблицей переводов и различными сервисами перевода.

## Подорбней

Этот модуль служит центральным звеном в процессе перевода информации о товарах. Он использует данные о товаре, доступе к базе данных переводов PrestaShop и сервисы машинного перевода для автоматизации и управления переводами. Модуль предоставляет функции для получения существующих переводов из базы данных PrestaShop, добавления новых переводов и выполнения автоматического перевода полей товара с использованием AI.

## Функции

### `get_translations_from_presta_translations_table`

```python
def get_translations_from_presta_translations_table(product_reference: str, credentials: dict, i18n: str = None) -> list:
    """Функция возвращает словарь переводов полей товара."""
```

**Описание**: Извлекает переводы полей товара из таблицы переводов PrestaShop на основе референса продукта.

**Как работает функция**:
1. Принимает референс товара (`product_reference`), параметры подключения к базе данных (`credentials`) и, опционально, локаль (`i18n`).
2. Инициализирует менеджер переводов (`ProductTranslationsManager`) с использованием предоставленных учетных данных.
3. Формирует фильтр поиска по референсу товара.
4. Выполняет запрос к базе данных через менеджер переводов для получения записей, соответствующих фильтру.
5. Возвращает список найденных переводов.

**Параметры**:
- `product_reference` (str): Референс товара, для которого требуется получить переводы.
- `credentials` (dict): Словарь с параметрами подключения к базе данных PrestaShop.
- `i18n` (str, optional): Локаль перевода (например, 'en_EN', 'he_HE', 'ru-RU'). По умолчанию `None`.

**Возвращает**:
- `list`: Список словарей, содержащих переводы полей товара.

**Примеры**:
```python
product_reference = "REF123"
credentials = {
    'host': 'localhost',
    'user': 'user',
    'password': 'password',
    'database': 'presta_db'
}
translations = get_translations_from_presta_translations_table(product_reference, credentials, i18n='ru-RU')
if translations:
    print(f"Найдены переводы: {translations}")
else:
    print("Переводы не найдены")
```

### `insert_new_translation_to_presta_translations_table`

```python
def insert_new_translation_to_presta_translations_table(record, credentials):
    with ProductTranslationsManager(credentials) as translations_manager:
        translations_manager.insert_record(record)
```

**Описание**: Добавляет новую запись перевода в таблицу переводов PrestaShop.

**Как работает функция**:
1. Принимает запись (`record`), содержащую данные для перевода, и параметры подключения к базе данных (`credentials`).
2. Инициализирует менеджер переводов (`ProductTranslationsManager`) с использованием предоставленных учетных данных.
3. Использует менеджер переводов для вставки новой записи в таблицу переводов.

**Параметры**:
- `record` (dict): Словарь с данными для добавления в таблицу переводов.
- `credentials` (dict): Словарь с параметрами подключения к базе данных PrestaShop.

**Примеры**:
```python
record = {
    'product_reference': 'REF456',
    'field_name': 'description',
    'locale': 'en-US',
    'translation': 'New description'
}
credentials = {
    'host': 'localhost',
    'user': 'user',
    'password': 'password',
    'database': 'presta_db'
}
insert_new_translation_to_presta_translations_table(record, credentials)
print("Новый перевод добавлен")
```

### `translate_record`

```python
def translate_record(record: dict, from_locale: str, to_locale: str) -> dict:
    """Функция для перевода полей товара."""
```

**Описание**: Переводит поля товара с одного языка на другой с использованием сервисов машинного перевода.

**Как работает функция**:
1. Принимает запись (`record`) с данными о товаре, исходную локаль (`from_locale`) и целевую локаль (`to_locale`).
2. Вызывает функцию `translate` из модуля `src.ai` для выполнения перевода записи.
3. <Добавить обработку переведенной записи>
4. Возвращает переведенную запись.

**Параметры**:
- `record` (dict): Словарь с данными о товаре для перевода.
- `from_locale` (str): Исходная локаль (например, 'en').
- `to_locale` (str): Целевая локаль (например, 'ru').

**Возвращает**:
- `dict`: Словарь с переведенными данными о товаре.

**Примеры**:
```python
record = {
    'name': 'Product Name',
    'description': 'Product Description'
}
from_locale = 'en'
to_locale = 'fr'
translated_record = translate_record(record, from_locale, to_locale)
print(f"Переведенная запись: {translated_record}")