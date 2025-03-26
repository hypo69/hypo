# Инструкция по созданию и редактированию рекламных кампаний

## Обзор

Этот документ содержит инструкции для разработчиков по созданию и редактированию рекламных кампаний, включая шаги по инициализации, сбору данных, созданию рекламных материалов и управлению ошибками.

## Содержание

- [1. Создание рекламной кампании](#1-создание-рекламной-кампании)
  - [1.1. Инициализация кампании](#11-инициализация-кампании)
  - [1.2. Создание директорий для кампании](#12-создание-директорий-для-кампании)
  - [1.3. Сохранение конфигурации кампании](#13-сохранение-конфигурации-кампании)
  - [1.4. Сбор данных о продуктах](#14-сбор-данных-о-продуктах)
  - [1.5. Сохранение данных о продуктах](#15-сохранение-данных-о-продуктах)
  - [1.6. Создание рекламных материалов](#16-создание-рекламных-материалов)
  - [1.7. Просмотр и публикация кампании](#17-просмотр-и-публикация-кампании)
- [2. Редактирование рекламной кампании](#2-редактирование-рекламной-кампании)
  - [2.1. Загрузка существующей конфигурации кампании](#21-загрузка-существующей-конфигурации-кампании)
  - [2.2. Обновление конфигурации кампании](#22-обновление-конфигурации-кампании)
  - [2.3. Обновление категорий и директорий](#23-обновление-категорий-и-директорий)
  - [2.4. Сбор новых данных о продуктах](#24-сбор-новых-данных-о-продуктах)
  - [2.5. Сохранение обновленных данных о продуктах](#25-сохранение-обновленных-данных-о-продуктах)
  - [2.6. Обновление рекламных материалов](#26-обновление-рекламных-материалов)
  - [2.7. Просмотр и публикация обновленной кампании](#27-просмотр-и-публикация-обновленной-кампании)
- [3. Обработка ошибок и логирование](#3-обработка-ошибок-и-логирование)
  - [3.1. Обработка ошибок](#31-обработка-ошибок)
  - [3.2. Логирование событий](#32-логирование-событий)
- [Примерный код](#примерный-код)
  - [`create_campaign`](#create_campaign)
  - [`edit_campaign`](#edit_campaign)
- [Заключение](#заключение)

## 1. Создание рекламной кампании

### 1.1. Инициализация кампании

- Введите имя кампании, язык и валюту.
- Пример:
  ```python
  campaign_name = 'example_campaign'
  language = 'EN'
  currency = 'USD'
  ```

### 1.2. Создание директорий для кампании

- Создайте директории для кампании и категорий.
- Пример:
  ```python
  categories = ['electronics', 'fashion']
  create_directories(campaign_name, categories)
  ```

### 1.3. Сохранение конфигурации кампании

- Создайте и сохраните конфигурационный файл кампании.
- Пример:
  ```python
  campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
  save_config(campaign_name, campaign_config)
  ```

### 1.4. Сбор данных о продуктах

- Введите URL или ID продуктов для кампании.
- Пример:
  ```python
  product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
  product_data = collect_product_data(product_urls)
  ```

### 1.5. Сохранение данных о продуктах

- Сохраните собранные данные о продуктах.
- Пример:
  ```python
  save_product_data(campaign_name, product_data)
  ```

### 1.6. Создание рекламных материалов

- Создайте рекламные материалы на основе собранных данных.
- Пример:
  ```python
  create_promotional_materials(campaign_name, product_data)
  ```

### 1.7. Просмотр и публикация кампании

- Просмотрите и опубликуйте кампанию.
- Пример:
  ```python
  review_campaign(campaign_name)
  publish_campaign(campaign_name)
  ```

## 2. Редактирование рекламной кампании

### 2.1. Загрузка существующей конфигурации кампании

- Загрузите конфигурацию существующей кампании.
- Пример:
  ```python
  campaign_name = 'example_campaign'
  campaign_config = load_config(campaign_name)
  ```

### 2.2. Обновление конфигурации кампании

- Обновите параметры кампании, такие как язык и валюту.
- Пример:
  ```python
  campaign_config['language'] = 'RU'
  save_config(campaign_name, campaign_config)
  ```

### 2.3. Обновление категорий и директорий

- Обновите список категорий и соответствующие директории.
- Пример:
  ```python
  new_categories = ['home', 'beauty']
  update_categories(campaign_name, new_categories)
  ```

### 2.4. Сбор новых данных о продуктах

- Введите новые URL или ID продуктов для обновленной кампании.
- Пример:
  ```python
  new_product_urls = ['https://www.aliexpress.com/item/789.html']
  updated_product_data = collect_product_data(new_product_urls)
  ```

### 2.5. Сохранение обновленных данных о продуктах

- Сохраните новые данные о продуктах.
- Пример:
  ```python
  save_product_data(campaign_name, updated_product_data)
  ```

### 2.6. Обновление рекламных материалов

- Обновите рекламные материалы на основе новых данных.
- Пример:
  ```python
  update_promotional_materials(campaign_name, updated_product_data)
  ```

### 2.7. Просмотр и публикация обновленной кампании

- Просмотрите и опубликуйте обновленную кампанию.
- Пример:
  ```python
  review_campaign(campaign_name)
  publish_campaign(campaign_name)
  ```

## 3. Обработка ошибок и логирование

### 3.1. Обработка ошибок

- Используйте `try-except` для обработки ошибок.
- Пример:
  ```python
  try:
      # Ваш код
  except Exception as ex:
      logger.error("Ошибка", ex)
  ```

### 3.2. Логирование событий

- Логируйте важные события и ошибки.
- Пример:
  ```python
  logger.info("Начало обработки кампании")
  logger.error("Ошибка при обработке кампании", ex)
  ```

## Примерный код

### `create_campaign`

**Описание**: Создает новую рекламную кампанию.

**Параметры**:

- `campaign_name` (str): Имя кампании.
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `categories` (list): Список категорий.
- `product_urls` (list): Список URL продуктов.

**Возвращает**:

- None

**Вызывает исключения**:

- Ошибки при создании директорий, сохранении конфигурации, сборе данных, создании материалов и публикации кампании

```python
def create_campaign(campaign_name, language, currency, categories, product_urls):
    create_directories(campaign_name, categories)
    campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
    save_config(campaign_name, campaign_config)
    product_data = collect_product_data(product_urls)
    save_product_data(campaign_name, product_data)
    create_promotional_materials(campaign_name, product_data)
    review_campaign(campaign_name)
    publish_campaign(campaign_name)
```

### `edit_campaign`

**Описание**: Редактирует существующую рекламную кампанию.

**Параметры**:

- `campaign_name` (str): Имя кампании.
- `language` (str): Новый язык кампании.
- `categories` (list): Новый список категорий.
- `product_urls` (list): Список URL продуктов для обновления.

**Возвращает**:

- None

**Вызывает исключения**:

- Ошибки при загрузке конфигурации, обновлении категорий, сборе данных, создании материалов и публикации кампании

```python
def edit_campaign(campaign_name, language, categories, product_urls):
    campaign_config = load_config(campaign_name)
    campaign_config['language'] = language
    save_config(campaign_name, campaign_config)
    update_categories(campaign_name, categories)
    updated_product_data = collect_product_data(product_urls)
    save_product_data(campaign_name, updated_product_data)
    update_promotional_materials(campaign_name, updated_product_data)
    review_campaign(campaign_name)
    publish_campaign(campaign_name)
```

## Заключение

Следуя этим инструкциям, вы сможете эффективно создавать и редактировать рекламные кампании, а также поддерживать их актуальность и корректную работу.