# Документация для разработчика: `Supplier`

## Обзор

Этот документ содержит описание класса `Supplier`, который является базовым классом для всех поставщиков данных в проекте `hypotez`. Класс унифицирует различных поставщиков под единым стандартом операций.

## Подробнее

В контексте данного кода, `Supplier` представляет собой поставщика информации. Поставщиком может быть производитель товаров, данных или информации. Источники поставщика могут включать целевую страницу веб-сайта, документ, базу данных или таблицу. Этот класс объединяет различных поставщиков под стандартизированным набором операций. Каждый поставщик имеет уникальный префикс (подробнее в [prefixes.md](prefixes.md)).

Класс `Supplier` служит основой для управления взаимодействием с поставщиками. Он обрабатывает инициализацию, конфигурацию, аутентификацию и выполнение рабочих процессов для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиенты также могут определять дополнительных поставщиков.

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