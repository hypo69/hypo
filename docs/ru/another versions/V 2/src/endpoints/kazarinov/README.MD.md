# Модуль `src.endpoints.kazarinov`

## Обзор

Модуль отвечает за обработку запросов от Telegram-ботов `hypo69_kazarinov_bot` и `hypo69_test_bot`, связанных с генерацией PDF-файлов на основе данных из One-Tab и последующей их отправкой пользователю.

## Оглавление

- [Обзор](#обзор)
- [KazarinovTelegramBot](#kazarinovtelegrambot)
- [BotHandler](#bothandler)
- [Client Side (Kazarinov)](#client-side-kazarinov)
- [Code Side](#code-side)
- [Next](#next)

## KazarinovTelegramBot

Ссылки на используемые ресурсы:
- https://one-tab.co.il
- https://morlevi.co.il
- https://grandavance.co.il
- https://ivory.co.il
- https://ksp.co.il

## BotHandler

Обработчик бота, который принимает сообщения от Telegram-ботов и обрабатывает их.

## Client Side (Kazarinov)

**Описание**: Схема взаимодействия клиента с ботами.

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
```

## Code Side

**Описание**: Схема обработки запроса на стороне кода.

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
- [Kazarinov bot](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.md)
- [Scenario Execution](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/README.MD)