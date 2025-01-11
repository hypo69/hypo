# Название модуля: src.endpoints.kazarinov

## Обзор

Данный модуль предназначен для создания прайслиста для Казаринова, а также включает в себя обработку сообщений от Telegram ботов и запуск соответствующих сценариев.

## Оглавление

1. [Обзор](#обзор)
2. [Диаграмма взаимодействия](#диаграмма-взаимодействия)
3. [Сценарий обработки сообщений](#сценарий-обработки-сообщений)
4. [Ссылки](#ссылки)

## Диаграмма взаимодействия

### Клиентская сторона

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
```

### Серверная сторона

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

## Сценарий обработки сообщений

1.  **`kazarinov_bot.handle_message()`** вызывает **`kazarinov.scenarios.run_scenario()`** для запуска соответствующего сценария.
2.  Проверяется, является ли URL от OneTab.
3.  Если URL от OneTab, данные извлекаются и проверяются на валидность.
4.  В случае некорректных данных, отправляется ответ об ошибке.
5.  При валидных данных запускается сценарий Mexiron.
6.  В зависимости от успешности выполнения сценария, отправляется соответствующее сообщение пользователю.

## Ссылки

*   [Казарионв бот](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.ru.md)
*   [Исполнение сценария](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/readme.ru.md)