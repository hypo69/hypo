# Сценарий формирования прайс-листа (mermaid)

## Обзор

Данный сценарий описывает процесс автоматизированного формирования прайс-листа с использованием внешних сервисов и API. Он включает в себя этапы загрузки конфигурации, инициализации моделей, извлечения данных, обработки и, в конечном счете, публикации результатов.

## Диаграмма потока

```mermaid
graph TD
    InitMexiron[Initialize Mexiron instance] --> LoadConfig[Load configuration and set paths]
    LoadConfig --> CreateExportPath[Create export path based on storage config]
    CreateExportPath --> LoadInstructions[Load system and command instructions]
    LoadInstructions --> InitializeAI[Initialize GoogleGenerativeAI model]
    InitializeAI --> RunScenario[Run scenario]
    RunScenario --> ParseURLs[Parse product URLs]
    ParseURLs --> CheckURLs[Check if URLs list is provided]
    CheckURLs --> HandleMissingURLs[Handle missing URLs]
    ParseURLs --> GetGrabber[Get grabber by supplier URL]
    GetGrabber --> ParseFields[Parse product fields with the grabber]
    ParseFields --> ConvertToDict[Convert product fields into dictionary]
    ConvertToDict --> SaveToFile[Save product data to file]
    SaveToFile --> ProcessWithAI[Process product list through AI]
    ProcessWithAI --> HandleAIResponse[Process AI response for Hebrew and Russian]
    HandleAIResponse --> SaveProcessedData[Save processed data Hebrew and Russian]
    SaveProcessedData --> GenerateReports[Create reports for Hebrew and Russian data]
    GenerateReports --> PostToFacebook[Post to Facebook]
    PostToFacebook --> EndScenario[End scenario execution]
    RunScenario --> HandleScenarioFailure[Handle unsuccessful scenario execution]
    HandleScenarioFailure --> EndScenario
    ParseFields --> HandleParseFailure[Handle failed product parsing]
    ConvertToDict --> HandleConversionFailure[Handle failed conversion]
    SaveToFile --> HandleSaveFailure[Handle failed product data saving]
    ProcessWithAI --> HandleAIProcessingFailure[Handle failed AI processing]
    HandleAIProcessingFailure --> RetryAI[Retry AI processing if failure occurs]
    HandleAIResponse --> HandleAIResponseFailure[Handle failed AI response]
    HandleAIResponseFailure --> RetryAI
    ParseURLs --> HandleUnknownSupplierURLs[Handle unknown supplier URLs]
    HandleUnknownSupplierURLs --> EndScenario
    HandleMissingURLs --> EndScenario
    CheckURLs --> EndScenario
    HandleParseFailure --> EndScenario
    HandleConversionFailure --> EndScenario
    HandleSaveFailure --> EndScenario
    HandleAIProcessingFailure --> EndScenario
```

## Этапы сценария

### Инициализация Mexiron

- Инициализируется экземпляр класса Mexiron.

### Загрузка конфигурации

- Загружаются параметры конфигурации и задаются пути к необходимым файлам и ресурсам.

### Создание пути к экспорту

- Создается путь к экспорту данных, основанный на конфигурации хранения.

### Загрузка инструкций

- Загружаются инструкции для обработки данных и выполнения сценария.

### Инициализация модели AI

- Инициализируется модель GoogleGenerativeAI для обработки данных.

### Запуск сценария

- Выполняется основной сценарий обработки данных.

### Парсинг URL

- Получаются URL-адреса для извлечения данных о товарах.

### Проверка списка URL

- Проверяется, что список URL-адресов не пустой.

### Обработка отсутствующих URL

- Обработка ситуаций, когда URL-адреса отсутствуют или недоступны.

### Получение граббера

- Получается инструмент (граббер) для извлечения данных с определенного поставщика.

### Парсинг полей

- Извлекаются необходимые поля данных о товарах с помощью граббера.

### Преобразование в словарь

- Преобразуются извлеченные данные в формат словаря.

### Сохранение данных

- Сохраняются данные о товарах в файл.

### Обработка данных AI

- Данные о товарах передаются на обработку AI-модели.

### Обработка ответа AI

- Обрабатывается ответ от AI-модели для русского и иврита.

### Сохранение обработанных данных

- Сохраняются обработанные данные на русском и иврите.

### Генерация отчетов

- Создаются отчеты на основе обработанных данных на русском и иврите.

### Публикация на Facebook

- Публикуются отчеты на Facebook.

### Завершение сценария

- Завершается выполнение сценария.


### Обработка ошибок

- Включает в себя обработку различных ошибок, включая:
    - Ошибки при парсинге данных.
    - Ошибки при преобразовании данных в словарь.
    - Ошибки при сохранении данных в файл.
    - Ошибки при обработке данных AI.
    - Ошибки при получении данных с неизвестных поставщиков.
    - Ошибки при работе с пустым списком URL.
- Для каждой ошибки предусмотрен отдельный механизм обработки и, при необходимости, повторной попытки.