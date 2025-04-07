# Модуль: src.endpoints.kazarinov

## Обзор

Данный модуль предназначен для работы с Kazarinov. PDF Mexiron Creator.

## Подробнее

Этот модуль, судя по всему, является частью системы, автоматизирующей создание PDF-документов Mexiron на основе данных, полученных от пользователя через Telegram-ботов.

Основные компоненты:

- `KazarinovTelegramBot`: Связан с Telegram-ботами `prod` и `test` для получения данных от пользователя.
- `BotHandler`: Обрабатывает данные, полученные от бота, и запускает сценарии Mexiron.

Модуль интегрирован с One-Tab для объединения комплектующих для сборки компьютера в одну ссылку, которая затем отправляется в Telegram бот.

## Схемы

### Клиентская сторона (Kazarinov)

```mermaid
flowchart TD
    Start[Выбор комплектующих для сборки компьютера] --> Combine[Объединение в One-Tab]
    Combine --> SendToBot{Отправка ссылки One-Tab в Telegram боту}
    SendToBot -->|hypo69_kazarinov_bot| ProdBot[Telegram бот <code>prod</code>]
    SendToBot -->|hypo69_test_bot| TestBot[Telegram бот <code>test</code>]
```

### Логика обработки кода

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

**Описание схемы**:

1.  **Start**: Начало обработки.
2.  **URL is from OneTab?**: Проверка, является ли URL ссылкой OneTab.
    *   Если да (Yes), то переходим к извлечению данных из OneTab.
    *   Если нет (No), то отправляем сообщение об ошибке и просим повторить ввод.
3.  **Get data from OneTab**: Извлечение данных из OneTab по предоставленной ссылке.
4.  **Data valid?**: Проверка валидности полученных данных.
    *   Если данные невалидны (No), отправляем сообщение об ошибке.
    *   Если данные валидны (Yes), запускаем сценарий Mexiron.
5.  **Run Mexiron scenario**: Запуск сценария Mexiron для обработки данных.
6.  **Scenario successful?**: Проверка успешности выполнения сценария.
    *   Если сценарий выполнен успешно (Yes), отправляем сообщение об успешном выполнении и ссылку для WhatsApp.
    *   Если сценарий выполнен с ошибкой (No), отправляем сообщение об ошибке.
7.  **Return**: Возврат.

## Дальнейшие шаги

*   [Kazarinov bot](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/kazarinov_bot.md)
*   [Scenario Execution](https://github.com/hypo69/hypo/blob/master/src/endpoints/kazarinov/scenarios/README.MD)