```markdown
# Модуль `hypotez/src/endpoints/prestashop/language.py`

## Обзор

Данный модуль предоставляет класс `PrestaLanguage` для управления языками в магазине PrestaShop. Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках.

## Оглавление

- [Модуль `hypotez/src/endpoints/prestashop/language.py`](#модуль-hypotezsrcendpointsprestashoplanguagepy)
- [Обзор](#обзор)
- [Классы](#классы)
    - [`PrestaLanguage`](#prestalanguage)
- [Функции](#функции)


## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` отвечает за взаимодействие с API PrestaShop для управления языками магазина. Наследуется от класса `PrestaShop` для использования общих методов и атрибутов.

**Методы**:

- [`__init__`](#__init__)

### `__init__`

**Описание**: Конструктор класса `PrestaLanguage`. Инициализирует необходимые параметры для работы с API PrestaShop.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
    * Если параметр `credentials` не `None`, то значения `api_domain` и `api_key` будут взяты из `credentials`.
- `*args` (tuple): Дополнительные аргументы.
- `**kwards` (dict): Дополнительные ключевые аргументы.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- `ValueError`: Если не заданы `api_domain` и `api_key`, либо не предоставлены корректные значения для них.



```
