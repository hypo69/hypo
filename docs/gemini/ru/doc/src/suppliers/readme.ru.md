# `Supplier`

## Обзор

Этот документ описывает класс `Supplier`, который является базовым классом для всех поставщиков данных в проекте `hypotez`. Класс предоставляет интерфейс для взаимодействия с различными источниками данных, такими как веб-сайты, документы, базы данных и таблицы, и сводит их к единому алгоритму действий.

## Подробней

Класс `Supplier` служит основой для управления взаимодействиями с поставщиками информации. Он отвечает за инициализацию, настройку, аутентификацию и запуск сценариев для различных источников данных, таких как `amazon.com`, `walmart.com`, `mouser.com` и `digikey.com`. Клиент может определять дополнительных поставщиков.

## Список реализованных поставщиков:

- [aliexpress](aliexpress/README.RU.MD) - Реализован в двух вариантах сценариев: `webdriver` и `api`
- [amazon](amazon/README.RU.MD) - `webdriver`
- [bangood](bangood/README.RU.MD) - `webdriver`
- [cdata](cdata/README.RU.MD) - `webdriver`
- [chat_gpt](chat_gpt/README.RU.MD) - Работа с чатом chatgpt (НЕ С МОДЕЛЬЮ!)
- [ebay](ebay/README.RU.MD) - `webdriver`
- [etzmaleh](etzmaleh/README.RU.MD) - `webdriver`
- [gearbest](gearbest/README.RU.MD) - `webdriver`
- [grandadvance](grandadvance/README.RU.MD) - `webdriver`
- [hb](hb/README.RU.MD) - `webdriver`
- [ivory](ivory/README.RU.MD) - `webdriver`
- [ksp](ksp/README.RU.MD) - `webdriver`
- [kualastyle](kualastyle/README.RU.MD) - `webdriver`
- [morlevi](morlevi/README.RU.MD) - `webdriver`
- [visualdg](visualdg/README.RU.MD) - `webdriver`
- [wallashop](wallashop/README.RU.MD) - `webdriver`
- [wallmart](wallmart/README.RU.MD) - `webdriver`

[Подробно о вебдрайвере class `Driver`](https://github.com/hypo69/hypo/blob/master/docs/ru/src/webdriver/driver.py.md)

[Подробно о сценариях class `Scenario`](https://github.com/hypo69/hypo/blob/master/docs/ru/src/scenario/executor.py.md)

[Подробно о локаторах](https://github.com/hypo69/hypo/blob/master/docs/ru/src/suppliers/locator.ru.md)

## Диаграмма взаимодействия компонентов

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
```

## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков. В контексте кода `Supplier` — это поставщик информации, таким поставщиком может быть производитель какого-либо товара, данных или информации. Источники поставщика — целевая страница сайта, документ, база данных, таблица. Класс сводит разных поставщиков к одинаковому алгоритму действий внутри класса. У каждого поставщика есть свой уникальный префикс. ([подробно о префиксах](prefixes.md))

**Принцип работы**:
Класс `Supplier` служит основой для управления взаимодействиями с поставщиками информации. Он выполняет инициализацию, настройку, аутентификацию и запуск сценариев для различных источников данных.