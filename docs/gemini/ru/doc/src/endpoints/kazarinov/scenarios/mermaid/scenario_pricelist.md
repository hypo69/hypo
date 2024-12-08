# Сценарий формирования прайс-листа (Mermaid диаграмма)

## Обзор

Данный файл описывает сценарий формирования прайс-листа, представленный в виде диаграммы Mermaid.  Диаграмма визуализирует последовательность шагов, необходимых для выполнения сценария, включая инициализацию, загрузку данных, обработку, сохранение результатов и генерацию отчетов.

## Диаграмма

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

## Последовательность шагов

Диаграмма изображает выполнение сценария, начиная с инициализации Mexiron до завершения и публикации отчетов на Facebook. В ней показаны проверки на ошибки, повторные попытки (retry) и обработка различных типов сбоев на каждом этапе.


## Обработка ошибок

Диаграмма демонстрирует наличие точек обработки ошибок (Handle...Failure) для следующих этапов:

* **Неудачная обработка сценария:** HandleScenarioFailure.
* **Ошибка парсинга данных:** HandleParseFailure.
* **Ошибка преобразования данных в словарь:** HandleConversionFailure.
* **Ошибка сохранения данных:** HandleSaveFailure.
* **Ошибка обработки данных с помощью AI:** HandleAIProcessingFailure.
* **Ошибка ответа AI:** HandleAIResponseFailure.
* **Отсутствующие URL:** HandleMissingURLs.
* **Неизвестные URL поставщиков:** HandleUnknownSupplierURLs.
* **Отсутствие списка URL:** CheckURLs.

Наличие этих элементов указывает на наличие механизмов обработки ошибок и повышения отказоустойчивости сценария.

## Заключение

Данная документация представляет собой описание сценария формирования прайс-листа с помощью Mermaid диаграммы, включая основные этапы,  обработку возможных ошибок и последовательность действий.