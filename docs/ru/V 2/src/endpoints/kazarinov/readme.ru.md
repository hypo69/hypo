# Название модуля

## Обзор

Документация описывает функциональность модуля, предназначенного для создания прайс-листов для Казаринова. Включает описание взаимодействия с Telegram-ботами и сценариев обработки данных.

## Содержание

- [Обзор](#обзор)
- [KazarinovTelegramBot](#kazarinovtelegrambot)
- [BotHandler](#bothandler)
- [Схема взаимодействия](#схема-взаимодействия)
- [Сценарий обработки](#сценарий-обработки)
- [Далее](#далее)

## KazarinovTelegramBot

- [https://one-tab.co.il](https://one-tab.co.il)
- [https://morlevi.co.il](https://morlevi.co.il)
- [https://grandavance.co.il](https://grandavance.co.il)
- [https://ivory.co.il](https://ivory.co.il)
- [https://ksp.co.il](https://ksp.co.il)

## BotHandler

### Описание

Обработчик для Telegram-бота, взаимодействующий с пользователем и запускающий сценарии обработки.

## Схема взаимодействия

### Клиентская сторона

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот `prod`]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот `test`]
```

### Серверная сторона

- `kazarinov_bot.handle_message()` -> `kazarinov.scenarios.run_scenario()`:

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

## Далее

- [Казаринов бот](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.ru.md)
- [Исполнение сценария](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/readme.ru.md)