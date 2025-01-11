# Документация для `scenario_pricelist.mmd`

## Обзор

Данный файл представляет собой диаграмму в формате Mermaid, описывающую сценарий обработки прайс-листа. Он визуализирует последовательность шагов, начиная от инициализации и загрузки конфигураций до сохранения обработанных данных и публикации в Facebook. Диаграмма также отображает обработку различных ошибок и исключений, которые могут возникнуть в процессе выполнения сценария.

## Оглавление

- [Обзор](#обзор)
- [Диаграмма Mermaid](#диаграмма-mermaid)

## Диаграмма Mermaid

```mermaid
flowchart TD
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

### Описание элементов диаграммы:

-   **`InitMexiron`**: Инициализация экземпляра Mexiron.
-   **`LoadConfig`**: Загрузка конфигурации и установка путей.
-   **`CreateExportPath`**: Создание пути экспорта на основе настроек хранилища.
-   **`LoadInstructions`**: Загрузка системных и командных инструкций.
-   **`InitializeAI`**: Инициализация модели GoogleGenerativeAI.
-   **`RunScenario`**: Запуск сценария.
-   **`ParseURLs`**: Разбор URL-адресов продуктов.
-   **`CheckURLs`**: Проверка, предоставлен ли список URL-адресов.
-   **`HandleMissingURLs`**: Обработка отсутствующих URL-адресов.
-   **`GetGrabber`**: Получение граббера по URL-адресу поставщика.
-   **`ParseFields`**: Разбор полей продукта с помощью граббера.
-   **`ConvertToDict`**: Преобразование полей продукта в словарь.
-   **`SaveToFile`**: Сохранение данных продукта в файл.
-   **`ProcessWithAI`**: Обработка списка продуктов с помощью AI.
-   **`HandleAIResponse`**: Обработка ответа AI для иврита и русского.
-   **`SaveProcessedData`**: Сохранение обработанных данных на иврите и русском.
-   **`GenerateReports`**: Создание отчетов для данных на иврите и русском.
-   **`PostToFacebook`**: Публикация в Facebook.
-   **`EndScenario`**: Завершение выполнения сценария.
-   **`HandleScenarioFailure`**: Обработка неудачного выполнения сценария.
-   **`HandleParseFailure`**: Обработка неудачного разбора продукта.
-   **`HandleConversionFailure`**: Обработка неудачного преобразования.
-   **`HandleSaveFailure`**: Обработка неудачного сохранения данных продукта.
-   **`HandleAIProcessingFailure`**: Обработка неудачной обработки AI.
-   **`RetryAI`**: Повторная попытка обработки AI в случае неудачи.
-   **`HandleAIResponseFailure`**: Обработка неудачного ответа AI.
-   **`HandleUnknownSupplierURLs`**: Обработка неизвестных URL-адресов поставщиков.