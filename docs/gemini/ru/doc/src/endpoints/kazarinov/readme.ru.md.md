# Название модуля

## Обзор

Документация для модуля, отвечающего за создание прайслиста для Казаринова. Модуль включает в себя обработку сообщений от Telegram бота и выполнение сценариев для формирования прайслиста.

## Оглавление

1. [Обзор](#обзор)
2. [Описание работы](#описание-работы)
3. [Схема работы](#схема-работы)
4. [Ссылки на другие документы](#ссылки-на-другие-документы)

## Описание работы

Модуль `src.endpoints.kazarinov` предназначен для создания прайслиста для компании Казаринов. Основная функциональность заключается в следующем:

-   Обработка сообщений от Telegram бота (`KazarinovTelegramBot`).
-   Извлечение данных из ссылок One-Tab.
-   Выполнение сценариев для генерации прайслиста (`kazarinov.scenarios.run_scenario()`).
-   Отправка сформированного прайслиста через WhatsApp (планируется).

Используются следующие ресурсы:
- https://one-tab.co.il
- https://morlevi.co.il
- https://grandavance.co.il
- https://ivory.co.il
- https://ksp.co.il

## Схема работы

### Клиентская сторона

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
```

### Серверная сторона

-   `kazarinov_bot.handle_message()` -> `kazarinov.scenarios.run_scenario()`:

```mermaid
flowchart TD
    A[Start] --> B{URL is from OneTab?}
    B -->|Yes| C[Get data from OneTab]
    B -->|No| D[Reply - Try again]
    C --> E{Data valid?}
    E -->|No| F[Reply Incorrect data]
    E -->|Yes| G[Run Mexiron scenario]
    G --> H{Scenario successful?}
    H -->|Yes| I[Reply Done! I will send the link to WhatsApp]
    H -->|No| J[Reply Error running scenario]
    F --> K[Return]
    I --> K[Return]
    D --> K[Return]
    J --> K[Return]
```

## Ссылки на другие документы

[Казарионв бот](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.ru.md)

[Исполнение сценария](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/readme.ru.md)