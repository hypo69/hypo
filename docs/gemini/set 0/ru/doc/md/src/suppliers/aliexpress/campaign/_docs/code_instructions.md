# Инструкция по работе с модулем создания и редактирования рекламных кампаний

## Оглавление

* [Создание рекламной кампании](#создание-рекламной-кампании)
* [Редактирование рекламной кампании](#редактирование-рекламной-кампании)
* [Обработка ошибок и логирование](#обработка-ошибок-и-логирование)
* [Примерный код](#примерный-код)
* [Заключение](#заключение)

## Создание рекламной кампании

### Функции

#### `create_campaign`

**Описание**: Функция для создания новой рекламной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `categories` (list): Список категорий для кампании.
- `product_urls` (list): Список URL-адресов продуктов для кампании.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `Exception`: Обработка любых исключений, возникающих во время выполнения функции.  Подробное описание ошибки логируется.


## Редактирование рекламной кампании

### Функции

#### `edit_campaign`

**Описание**: Функция для редактирования существующей рекламной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.
- `language` (str): Новый язык кампании.
- `categories` (list): Обновленный список категорий.
- `product_urls` (list): Список новых URL-адресов продуктов.


**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `Exception`: Обработка любых исключений, возникающих во время выполнения функции. Подробное описание ошибки логируется.


## Обработка ошибок и логирование

###  Обработка исключений

**Описание**: Примеры использования `try-except` блоков для обработки ошибок и логирования.


**Пример**:
```python
try:
    # Ваш код, который может вызвать ошибку
    result = some_function()
except Exception as ex:
    logger.error("Произошла ошибка:", ex)
    # Обработка ошибки
```


### Логирование событий

**Описание**: Важность логирования событий для отладки и мониторинга работы.

**Пример**:
```python
logger.info("Начало процесса создания кампании")
logger.error("Ошибка при загрузке данных", ex)
```

## Примерный код

```python
def create_campaign(campaign_name, language, currency, categories, product_urls):
    try:
        create_directories(campaign_name, categories)
        campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
        save_config(campaign_name, campaign_config)
        product_data = collect_product_data(product_urls)
        save_product_data(campaign_name, product_data)
        create_promotional_materials(campaign_name, product_data)
        review_campaign(campaign_name)
        publish_campaign(campaign_name)
        logger.info("Кампания успешно создана")
    except Exception as ex:
        logger.error("Ошибка при создании кампании", ex)


def edit_campaign(campaign_name, language, categories, product_urls):
    try:
      campaign_config = load_config(campaign_name)
      campaign_config['language'] = language
      save_config(campaign_name, campaign_config)
      update_categories(campaign_name, categories)
      updated_product_data = collect_product_data(product_urls)
      save_product_data(campaign_name, updated_product_data)
      update_promotional_materials(campaign_name, updated_product_data)
      review_campaign(campaign_name)
      publish_campaign(campaign_name)
      logger.info("Кампания успешно отредактирована")
    except Exception as ex:
      logger.error("Ошибка при редактировании кампании", ex)
```

## Заключение

Данная инструкция предоставляет подробное руководство по работе с модулем создания и редактирования рекламных кампаний.  Включая обработку ошибок и подробные примеры кода.