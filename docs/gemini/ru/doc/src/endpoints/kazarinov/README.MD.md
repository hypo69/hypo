# Модуль `src.endpoints.kazarinov`

## Обзор

Этот модуль содержит документацию и описание логики работы Telegram-бота `KazarinovTelegramBot`, который используется для обработки ссылок One-Tab, запуска сценариев Mexiron и отправки результатов в WhatsApp.

## Содержание

1. [KazarinovTelegramBot](#kazarinovtelegrambot)
2. [BotHandler](#bothandler)
3. [Client Side](#client-side)
4. [Code Side](#code-side)
5. [Next](#next)

## KazarinovTelegramBot

- **Описание**: Данный раздел содержит информацию о боте `KazarinovTelegramBot` и ссылки на связанные с ним ресурсы.
    - [https://one-tab.co.il](https://one-tab.co.il)
    - [https://morlevi.co.il](https://morlevi.co.il)
    - [https://grandavance.co.il](https://grandavance.co.il)
    - [https://ivory.co.il](https://ivory.co.il)
    - [https://ksp.co.il](https://ksp.co.il)

## BotHandler

- **Описание**: Раздел описывает `BotHandler`, который отвечает за обработку сообщений от пользователей и взаимодействие с Telegram ботом.

## Client Side

- **Описание**: Раздел описывает клиентскую часть логики бота. Сначала пользователь выбирает комплектующие для сборки компьютера, затем они объединяются в ссылку One-Tab, и эта ссылка отправляется в Telegram-бота.
    
    ```mermaid
    flowchart TD
        Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
        Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
        SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
        SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
    ```

## Code Side

- **Описание**: Раздел описывает логику работы бота со стороны кода. Бот проверяет, является ли URL ссылкой One-Tab, получает данные, проверяет их корректность и запускает сценарий Mexiron. В зависимости от успеха выполнения сценария, бот отправляет соответствующее уведомление.
    
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

## Next

- **Описание**: Раздел содержит ссылки на следующие документы.
    - [Kazarinov bot](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.md)
    - [Scenario Execution](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/README.MD)