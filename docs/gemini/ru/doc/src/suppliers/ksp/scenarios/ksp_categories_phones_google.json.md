# Документация для `ksp_categories_phones_google.json`

## Оглавление

- [Обзор](#обзор)
- [Структура](#структура)
    - [scenarios](#scenarios)
        - [Pixel 6 PRO](#pixel-6-pro)
        - [Pixel 6](#pixel-6)
        - [Google Pixel 5a 5G](#google-pixel-5a-5g)
        - [Google Pixel 6a](#google-pixel-6a)

## Обзор

Данный JSON-файл содержит конфигурацию сценариев для парсинга категорий телефонов бренда Google с сайта KSP. Каждый сценарий определяет параметры для конкретной модели телефона, включая URL страницы, активность парсинга и соответствие категориям в PrestaShop.

## Структура

### `scenarios`

Объект `scenarios` содержит набор сценариев, каждый из которых представляет собой конфигурацию для конкретной модели телефона.

#### Pixel 6 PRO
  
  - **Описание**:  Конфигурация для парсинга Google Pixel 6 PRO.
  - **brand**:  `"GOOGLE"` - Бренд телефона.
  - **url**:  `"https://ksp.co.il/web/cat/573..3887..31508"` - URL страницы с телефонами.
  - **checkbox**:  `false` -  Флаг для использования чекбоксов (не используется).
  - **active**:  `true` -  Флаг активности парсинга.
  - **condition**: `"new"` - Состояние товара (новый).
  - **presta_categories**: 
        - **template**: `{ "google": "GOOGLE PIXEL 6 PRO" }` -  Соответствие категории PrestaShop.

#### Pixel 6

- **Описание**: Конфигурация для парсинга Google Pixel 6.
  - **brand**: `"GOOGLE"` - Бренд телефона.
  - **url**: `"https://ksp.co.il/web/cat/573..3887..30356"` - URL страницы с телефонами.
  - **checkbox**: `false` - Флаг для использования чекбоксов (не используется).
  - **active**: `true` - Флаг активности парсинга.
    - **condition**: `"new"` - Состояние товара (новый).
  - **presta_categories**:
        - **template**: `{ "google": "GOOGLE PIXEL 6" }` - Соответствие категории PrestaShop.
      
#### Google Pixel 5a 5G

- **Описание**: Конфигурация для парсинга Google Pixel 5a 5G.
  - **brand**: `"GOOGLE"` - Бренд телефона.
  - **url**: `"https://ksp.co.il/web/cat/573..3887..28492"` - URL страницы с телефонами.
  - **checkbox**: `false` - Флаг для использования чекбоксов (не используется).
  - **active**: `true` - Флаг активности парсинга.
  - **condition**: `"new"` - Состояние товара (новый).
  - **presta_categories**:
        - **template**: `{ "google": "GOOGLE PIXEL 5A 5G" }` - Соответствие категории PrestaShop.

#### Google Pixel 6a

- **Описание**: Конфигурация для парсинга Google Pixel 6a.
  - **brand**: `"GOOGLE"` - Бренд телефона.
  - **url**: `"https://ksp.co.il/web/cat/573..3887..28492"` - URL страницы с телефонами.
  - **checkbox**: `false` - Флаг для использования чекбоксов (не используется).
  - **active**: `true` - Флаг активности парсинга.
  - **condition**: `"new"` - Состояние товара (новый).
  - **presta_categories**:
        - **template**: `{ "google": "GOOGLE PIXEL 6A" }` - Соответствие категории PrestaShop.