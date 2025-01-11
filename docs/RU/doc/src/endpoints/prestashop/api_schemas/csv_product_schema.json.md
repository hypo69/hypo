# CSV Schema для продукта PrestaShop

## Обзор

Этот документ описывает структуру JSON-схемы для CSV файла, используемого для импорта продуктов в PrestaShop. Он содержит описание всех полей, которые могут быть использованы при импорте, а также их типы данных.

## Оглавление

- [Обзор](#обзор)
- [Свойства](#свойства)
  - [ID](#id)
  - [Active (0/1)](#active-01)
  - [Name*](#name)
  - [Categories (x,y,z...)](#categories-xyz)
  - [Price tax excluded](#price-tax-excluded)
  - [Price tax included](#price-tax-included)
  - [Tax rule ID](#tax-rule-id)
  - [Cost price](#cost-price)
  - [On sale (0/1)](#on-sale-01)
  - [Discount amount](#discount-amount)
  - [Discount percent](#discount-percent)
  - [Discount from (yyyy-mm-dd)](#discount-from-yyyy-mm-dd)
  - [Discount to (yyyy-mm-dd)](#discount-to-yyyy-mm-dd)
  - [reference #](#reference)
  - [Supplier reference #](#supplier-reference)
  - [Supplier](#supplier)
  - [Brand](#brand)
  - [EAN13](#ean13)
  - [UPC](#upc)
  - [MPN](#mpn)
  - [Ecotax](#ecotax)
  - [Width](#width)
  - [Height](#height)
  - [Depth](#depth)
  - [Weight](#weight)
  - [Delivery time of in-stock products:](#delivery-time-of-in-stock-products)
  - [Delivery time of out-of-stock products with allowed orders:](#delivery-time-of-out-of-stock-products-with-allowed-orders)
  - [Quantity](#quantity)
  - [Minimal quantity](#minimal-quantity)
  - [Low stock level](#low-stock-level)
  - [Send me an email when the quantity is under this level](#send-me-an-email-when-the-quantity-is-under-this-level)
  - [Visibility](#visibility)
  - [Additional shipping cost](#additional-shipping-cost)
  - [Unit for base price](#unit-for-base-price)
  - [Base price](#base-price)
  - [Summary](#summary)
  - [Description](#description)
  - [Tags (x,y,z...)](#tags-xyz)
  - [Meta title](#meta-title)
  - [Meta keywords](#meta-keywords)
  - [Meta description](#meta-description)
  - [Rewritten URL](#rewritten-url)
  - [Label when in stock](#label-when-in-stock)
  - [Label when backorder allowed](#label-when-backorder-allowed)
  - [Available for order (0 = No, 1 = Yes)](#available-for-order-0--no-1--yes)
  - [Product availability date](#product-availability-date)
  - [Product creation date](#product-creation-date)
  - [Show price (0 = No, 1 = Yes)](#show-price-0--no-1--yes)
  - [additional_images_urls](#additional_images_urls)
  - [additional_images_alts](#additional_images_alts)
  - [Delete existing images (0 = No, 1 = Yes)](#delete-existing-images-0--no-1--yes)
  - [Feature (Name:Value:Position:Customized)](#feature-namevaluepositioncustomized)
    - [Available online only (0 = No, 1 = Yes)](#available-online-only-0--no-1--yes)
    - [Condition](#condition)
    - [Customizable (0 = No, 1 = Yes)](#customizable-0--no-1--yes)
    - [Uploadable files (0 = No, 1 = Yes)](#uploadable-files-0--no-1--yes)
    - [Text fields (0 = No, 1 = Yes)](#text-fields-0--no-1--yes)
    - [Action when out of stock](#action-when-out-of-stock)
    - [Virtual product (0 = No, 1 = Yes)](#virtual-product-0--no-1--yes)
    - [File URL](#file-url)
    - [Number of allowed downloads](#number-of-allowed-downloads)
    - [Expiration date (yyyy-mm-dd)](#expiration-date-yyyy-mm-dd)
    - [Number of days](#number-of-days)
    - [ID / Name of shop](#id--name-of-shop)
    - [Advanced Stock Management](#advanced-stock-management)
    - [Depends on stock](#depends-on-stock)
    - [Warehouse](#warehouse)
    - [Accessories (x,y,z...)](#accessories-xyz)
    - [affiliate short link](#affiliate-short-link)
    - [affiliate text](#affiliate-text)
    - [affiliate summary](#affiliate-summary)
    - [affiliate summary 2](#affiliate-summary-2)
    - [Open AI Product Description](#open-ai-product-description)
    - [Byer protection](#byer-protection)
    - [Specification](#specification)
    - [Refirbished product description](#refirbished-product-description)
    - [Additional shipping details](#additional-shipping-details)
    - [Product features](#product-features)
    - [Additional product info](#additional-product-info)

## Свойства

### `ID`
- **Описание**: ID продукта.
- **Тип**: `null`

### `Active (0/1)`
- **Описание**: Флаг активности продукта (0 - неактивен, 1 - активен).
- **Тип**: `null`

### `Name*`
- **Описание**: Название продукта. Обязательное поле.
- **Тип**: `null`

### `Categories (x,y,z...)`
- **Описание**: Категории продукта, перечисленные через запятую. ID категорий.
- **Тип**: `str`
- **Пример**: `"2,"`

### `Price tax excluded`
- **Описание**: Цена продукта без учета налога.
- **Тип**: `null`

### `Price tax included`
- **Описание**: Цена продукта с учетом налога.
- **Тип**: `null`

### `Tax rule ID`
- **Описание**: ID налогового правила.
- **Тип**: `null`

### `Cost price`
- **Описание**: Себестоимость продукта.
- **Тип**: `null`

### `On sale (0/1)`
- **Описание**: Флаг распродажи (0 - нет, 1 - да).
- **Тип**: `null`

### `Discount amount`
- **Описание**: Сумма скидки.
- **Тип**: `null`

### `Discount percent`
- **Описание**: Процент скидки.
- **Тип**: `null`

### `Discount from (yyyy-mm-dd)`
- **Описание**: Дата начала действия скидки.
- **Тип**: `null`

### `Discount to (yyyy-mm-dd)`
- **Описание**: Дата окончания действия скидки.
- **Тип**: `null`

### `reference #`
- **Описание**: Артикул продукта.
- **Тип**: `null`

### `Supplier reference #`
- **Описание**: Артикул поставщика.
- **Тип**: `null`

### `Supplier`
- **Описание**: Поставщик продукта.
- **Тип**: `null`

### `Brand`
- **Описание**: Бренд продукта.
- **Тип**: `null`

### `EAN13`
- **Описание**: EAN13 код продукта.
- **Тип**: `null`

### `UPC`
- **Описание**: UPC код продукта.
- **Тип**: `null`

### `MPN`
- **Описание**: MPN код продукта.
- **Тип**: `null`

### `Ecotax`
- **Описание**: Эко налог.
- **Тип**: `null`

### `Width`
- **Описание**: Ширина продукта.
- **Тип**: `null`

### `Height`
- **Описание**: Высота продукта.
- **Тип**: `null`

### `Depth`
- **Описание**: Глубина продукта.
- **Тип**: `null`

### `Weight`
- **Описание**: Вес продукта.
- **Тип**: `null`

### `Delivery time of in-stock products:`
- **Описание**: Время доставки для товаров в наличии.
- **Тип**: `null`

### `Delivery time of out-of-stock products with allowed orders:`
- **Описание**: Время доставки для товаров не в наличии, но с возможностью заказа.
- **Тип**: `null`

### `Quantity`
- **Описание**: Количество продукта на складе.
- **Тип**: `null`

### `Minimal quantity`
- **Описание**: Минимальное количество для заказа.
- **Тип**: `null`

### `Low stock level`
- **Описание**: Уровень запаса для оповещения.
- **Тип**: `null`

### `Send me an email when the quantity is under this level`
- **Описание**: Уведомлять об низком уровне запаса (0 - нет, 1 - да).
- **Тип**: `null`

### `Visibility`
- **Описание**: Видимость продукта.
- **Тип**: `null`

### `Additional shipping cost`
- **Описание**: Дополнительная стоимость доставки.
- **Тип**: `null`

### `Unit for base price`
- **Описание**: Единица измерения для базовой цены.
- **Тип**: `null`

### `Base price`
- **Описание**: Базовая цена.
- **Тип**: `null`

### `Summary`
- **Описание**: Краткое описание продукта.
- **Тип**: `null`

### `Description`
- **Описание**: Полное описание продукта.
- **Тип**: `null`

### `Tags (x,y,z...)`
- **Описание**: Теги продукта, перечисленные через запятую.
- **Тип**: `null`

### `Meta title`
- **Описание**: Meta заголовок продукта.
- **Тип**: `null`

### `Meta keywords`
- **Описание**: Meta ключевые слова продукта.
- **Тип**: `null`

### `Meta description`
- **Описание**: Meta описание продукта.
- **Тип**: `null`

### `Rewritten URL`
- **Описание**: Переписанный URL продукта.
- **Тип**: `null`

### `Label when in stock`
- **Описание**: Метка для товара в наличии.
- **Тип**: `null`

### `Label when backorder allowed`
- **Описание**: Метка для товара под заказ.
- **Тип**: `null`

### `Available for order (0 = No, 1 = Yes)`
- **Описание**: Доступен для заказа (0 - нет, 1 - да).
- **Тип**: `null`

### `Product availability date`
- **Описание**: Дата поступления товара.
- **Тип**: `null`

### `Product creation date`
- **Описание**: Дата создания товара.
- **Тип**: `null`

### `Show price (0 = No, 1 = Yes)`
- **Описание**: Показывать цену (0 - нет, 1 - да).
- **Тип**: `null`

### `additional_images_urls`
- **Описание**: URL-ы дополнительных изображений продукта.
- **Тип**: `null`

### `additional_images_alts`
- **Описание**: Альтернативные тексты дополнительных изображений продукта.
- **Тип**: `null`

### `Delete existing images (0 = No, 1 = Yes)`
- **Описание**: Удалить существующие изображения (0 - нет, 1 - да).
- **Тип**: `null`

### `Feature (Name:Value:Position:Customized)`
- **Описание**: Характеристики товара в формате Name:Value:Position:Customized.
- **Тип**: `null`

### `Available online only (0 = No, 1 = Yes)`
- **Описание**: Доступен только онлайн (0 - нет, 1 - да).
- **Тип**: `null`

### `Condition`
- **Описание**: Состояние товара (новый, б/у и т.д.).
- **Тип**: `null`

### `Customizable (0 = No, 1 = Yes)`
- **Описание**: Настраиваемый (0 - нет, 1 - да).
- **Тип**: `null`

### `Uploadable files (0 = No, 1 = Yes)`
- **Описание**: Возможность загрузки файлов (0 - нет, 1 - да).
- **Тип**: `null`

### `Text fields (0 = No, 1 = Yes)`
- **Описание**: Текстовые поля (0 - нет, 1 - да).
- **Тип**: `null`

### `Action when out of stock`
- **Описание**: Действие, когда нет в наличии.
- **Тип**: `null`

### `Virtual product (0 = No, 1 = Yes)`
- **Описание**: Виртуальный товар (0 - нет, 1 - да).
- **Тип**: `null`

### `File URL`
- **Описание**: URL файла для виртуального товара.
- **Тип**: `null`

### `Number of allowed downloads`
- **Описание**: Количество разрешенных загрузок.
- **Тип**: `null`

### `Expiration date (yyyy-mm-dd)`
- **Описание**: Дата истечения срока действия файла.
- **Тип**: `null`

### `Number of days`
- **Описание**: Количество дней для загрузки.
- **Тип**: `null`

### `ID / Name of shop`
- **Описание**: ID или название магазина.
- **Тип**: `null`

### `Advanced Stock Management`
- **Описание**: Расширенное управление запасами.
- **Тип**: `null`

### `Depends on stock`
- **Описание**: Зависит от запасов.
- **Тип**: `null`

### `Warehouse`
- **Описание**: Склад.
- **Тип**: `null`

### `Accessories (x,y,z...)`
- **Описание**: Аксессуары, перечисленные через запятую.
- **Тип**: `null`

### `affiliate short link`
- **Описание**: Короткая партнерская ссылка.
- **Тип**: `null`

### `affiliate text`
- **Описание**: Партнерский текст.
- **Тип**: `null`

### `affiliate summary`
- **Описание**: Партнерское описание.
- **Тип**: `null`

### `affiliate summary 2`
- **Описание**: Второе партнерское описание.
- **Тип**: `null`

### `Open AI Product Description`
- **Описание**: Описание продукта, сгенерированное Open AI.
- **Тип**: `null`

### `Byer protection`
- **Описание**: Защита покупателя.
- **Тип**: `null`

### `Specification`
- **Описание**: Спецификация продукта.
- **Тип**: `null`

### `Refirbished product description`
- **Описание**: Описание восстановленного товара.
- **Тип**: `null`

### `Additional shipping details`
- **Описание**: Дополнительные детали доставки.
- **Тип**: `str`
- **Пример**: `""`

### `Product features`
- **Описание**: Характеристики продукта.
- **Тип**: `null`

### `Additional product info`
- **Описание**: Дополнительная информация о продукте.
- **Тип**: `null`