# Документация для модуля `src.endpoints.kazarinov`

## Обзор

Документация предоставляет информацию о модуле `src.endpoints.kazarinov`, который связан с созданием прайс-листа для Казаринова и включает в себя работу с Telegram ботами `KazarinovTelegramBot` и `BotHandler`.

## Подорбней

Модуль предназначен для автоматизации процесса формирования прайс-листов на основе данных о комплектующих, собранных пользователем. Пользователь выбирает комплектующие для сборки компьютера, объединяет их в One-Tab ссылку и отправляет эту ссылку в Telegram боту. Бот, в свою очередь, обрабатывает полученные данные и запускает сценарий для формирования прайс-листа.

Связь между клиентом и кодом организована следующим образом:

1.  **Клиентская часть**: Пользователь использует One-Tab для объединения ссылок на комплектующие и отправляет ссылку боту.
2.  **Серверная часть**: Бот обрабатывает сообщение, извлекает данные из One-Tab ссылки и запускает сценарий `Mexiron` для формирования прайс-листа.

## Схема работы

### Клиентская часть

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
```

### Обработка на стороне кода

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

1.  Бот `kazarinov_bot.handle_message()` принимает сообщение от пользователя.
2.  Проверяется, является ли URL ссылкой на One-Tab.
3.  Если да, извлекаются данные из One-Tab.
4.  Данные валидируются.
5.  Если данные валидны, запускается сценарий `Mexiron`.
6.  В зависимости от успеха сценария, бот отправляет пользователю сообщение об успехе или ошибке.

## Классы

В данном файле не указаны классы.

## Функции

В данном файле не указаны функции.

## Ссылки

-   [Казаринов бот](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.ru.md)
-   [Исполнение сценария](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/readme.ru.md)