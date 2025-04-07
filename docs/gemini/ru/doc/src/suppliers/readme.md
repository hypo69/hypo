# Документация модуля `Supplier`

## Обзор

Этот документ предоставляет подробное описание класса `Supplier`, который является базовым классом для всех поставщиков данных в проекте. В контексте кода, `Supplier` представляет собой поставщика информации, такого как производитель товаров, данных или информации. Источники поставщика могут включать целевую страницу веб-сайта, документ, базу данных или таблицу. Этот класс унифицирует различных поставщиков под стандартизированным набором операций.

## Подробнее

Класс `Supplier` служит основой для управления взаимодействиями с поставщиками. Он обрабатывает инициализацию, конфигурацию, аутентификацию и выполнение рабочих процессов для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиенты также могут определять дополнительных поставщиков. Каждый поставщик имеет уникальный префикс.

## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков.

**Принцип работы**:
Класс `Supplier` предоставляет унифицированный интерфейс для взаимодействия с различными источниками данных. Он абстрагирует детали реализации каждого конкретного поставщика и предоставляет стандартизированный набор операций для получения и обработки данных.

## Список реализованных поставщиков:

*   [aliexpress](aliexpress) - Реализован с двумя рабочими процессами: `webdriver` и `api`

*   [amazon](amazon) - `webdriver`

*   [bangood](bangood) - `webdriver`

*   [cdata](cdata) - `webdriver`

*   [chat\_gpt](chat_gpt) - Взаимодействует с интерфейсом ChatGPT (НЕ С МОДЕЛЬЮ!)

*   [ebay](ebay) - `webdriver`

*   [etzmaleh](etzmaleh) - `webdriver`

*   [gearbest](gearbest) - `webdriver`

*   [grandadvance](grandadvance) - `webdriver`

*   [hb](hb) - `webdriver`

*   [ivory](ivory) - `webdriver`

*   [ksp](ksp) - `webdriver`

*   [kualastyle](kualastyle) `webdriver`

*   [morlevi](morlevi) `webdriver`

*   [visualdg](visualdg) `webdriver`

*   [wallashop](wallashop) `webdriver`

*   [wallmart](wallmart) `webdriver`

[Подробности о WebDriver :class: `Driver`](../webdriver)

[Подробности о рабочих процессах :class: `Scenario`](../scenarios)

## Схема взаимодействия

```mermaid
graph TD
    subgraph WebInteraction
        webelement <--> executor
        subgraph InnerInteraction
            executor <--> webdriver
        end
    end
    webdriver -->|result| supplier
    supplier -->|locator| webdriver
    supplier --> product_fields
    product_fields --> endpoints
    scenario -->|Specific scenario for supplier| supplier