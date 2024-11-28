# Модуль `hypotez/src/endpoints/prestashop/language.py`

## Обзор

Этот модуль предоставляет класс `PrestaLanguage` для работы с языками в магазине PrestaShop. Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках.

## Оглавление

- [Модуль `hypotez/src/endpoints/prestashop/language.py`](#модуль-hypotezsrcendpointsprestashoplanguagepy)
- [Обзор](#обзор)
- [Класс `PrestaLanguage`](#класс-prestalanguage)
    - [Метод `__init__`](#метод-init)


## Класс `PrestaLanguage`

**Описание**: Класс, отвечающий за настройки языков магазина PrestaShop.  Предлагает методы для взаимодействия с API PrestaShop.

**Пример использования**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```


### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaLanguage`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  None (метод инициализирует объект, не возвращает значение)

**Вызывает исключения**:

- `ValueError`: Если не предоставлены оба параметра `api_domain` и `api_key`.


**Подробности**:
Метод `__init__` принимает необязательные параметры для инициализации объекта `PrestaLanguage`. Если параметр `credentials` задан, значения `api_domain` и `api_key` берутся из него.  Если `api_domain` или `api_key` не указаны, то генерируется исключение `ValueError`. Далее, `__init__` вызывается конструктор базового класса `PrestaShop`, передавая ему полученные параметры.