# Документация для разработчика: request.json

## Обзор

Этот файл (`request.json`) содержит структуру JSON, описывающую формат запроса к API Google Gemini. Он определяет схему для отправки контента, инструкций, инструментов, настроек безопасности, конфигураций генерации и меток. Этот файл служит справочным руководством для разработчиков, чтобы понимать, как формировать запросы к API Gemini.

## Подробней

`request.json` определяет структуру запроса, который отправляется в API Gemini.
Он включает в себя различные параметры, которые позволяют настраивать поведение модели,
включая параметры безопасности, конфигурацию генерации и инструменты.
Правильное понимание структуры JSON необходимо для успешной интеграции с API Gemini.

## Структура JSON

### `cachedContent`

- **Описание**: Кэшированный контент.
- **Тип**: `string`

### `contents`

- **Описание**: Массив объектов, содержащих информацию о контенте. Каждый объект включает роль и части контента.
- **Тип**: `array`

#### `contents[].role`

- **Описание**: Роль контента (например, `user` или `model`).
- **Тип**: `string`

#### `contents[].parts`

- **Описание**: Массив частей контента, составляющих сообщение.
- **Тип**: `array`

##### `contents[].parts[].text`

- **Описание**: Текстовая часть контента.
- **Тип**: `string`

##### `contents[].parts[].inlineData`

- **Описание**: Встроенные данные (например, изображение).
- **Тип**: `object`

###### `contents[].parts[].inlineData.mimeType`

- **Описание**: MIME-тип встроенных данных.
- **Тип**: `string`

###### `contents[].parts[].inlineData.data`

- **Описание**: Данные, закодированные в base64.
- **Тип**: `string`

##### `contents[].parts[].fileData`

- **Описание**: Данные файла.
- **Тип**: `object`

###### `contents[].parts[].fileData.mimeType`

- **Описание**: MIME-тип файла.
- **Тип**: `string`

###### `contents[].parts[].fileData.fileUri`

- **Описание**: URI файла.
- **Тип**: `string`

##### `contents[].parts[].videoMetadata`

- **Описание**: Метаданные видео.
- **Тип**: `object`

###### `contents[].parts[].videoMetadata.startOffset`

- **Описание**: Начальное смещение видео.
- **Тип**: `object`

####### `contents[].parts[].videoMetadata.startOffset.seconds`

- **Описание**: Секунды начального смещения.
- **Тип**: `integer`

####### `contents[].parts[].videoMetadata.startOffset.nanos`

- **Описание**: Наносекунды начального смещения.
- **Тип**: `integer`

###### `contents[].parts[].videoMetadata.endOffset`

- **Описание**: Конечное смещение видео.
- **Тип**: `object`

####### `contents[].parts[].videoMetadata.endOffset.seconds`

- **Описание**: Секунды конечного смещения.
- **Тип**: `integer`

####### `contents[].parts[].videoMetadata.endOffset.nanos`

- **Описание**: Наносекунды конечного смещения.
- **Тип**: `integer`

### `systemInstruction`

- **Описание**: Системные инструкции для модели.
- **Тип**: `object`

#### `systemInstruction.role`

- **Описание**: Роль системных инструкций.
- **Тип**: `string`

#### `systemInstruction.parts`

- **Описание**: Массив частей системных инструкций.
- **Тип**: `array`

##### `systemInstruction.parts[].text`

- **Описание**: Текст системных инструкций.
- **Тип**: `string`

### `tools`

- **Описание**: Инструменты, которые можно использовать в запросе.
- **Тип**: `array`

#### `tools[].functionDeclarations`

- **Описание**: Объявления функций.
- **Тип**: `array`

##### `tools[].functionDeclarations[].name`

- **Описание**: Имя функции.
- **Тип**: `string`

##### `tools[].functionDeclarations[].description`

- **Описание**: Описание функции.
- **Тип**: `string`

##### `tools[].functionDeclarations[].parameters`

- **Описание**: Параметры функции.
- **Тип**: `object`

### `safetySettings`

- **Описание**: Настройки безопасности.
- **Тип**: `array`

#### `safetySettings[].category`

- **Описание**: Категория безопасности.
- **Тип**: `enum` (`HarmCategory`)

#### `safetySettings[].threshold`

- **Описание**: Порог блокировки.
- **Тип**: `enum` (`HarmBlockThreshold`)

### `generationConfig`

- **Описание**: Конфигурация генерации.
- **Тип**: `object`

#### `generationConfig.temperature`

- **Описание**: Температура (случайность) генерации.
- **Тип**: `number`

#### `generationConfig.topP`

- **Описание**: Top-p sampling.
- **Тип**: `number`

#### `generationConfig.topK`

- **Описание**: Top-k sampling.
- **Тип**: `number`

#### `generationConfig.candidateCount`

- **Описание**: Количество кандидатов для генерации.
- **Тип**: `integer`

#### `generationConfig.maxOutputTokens`

- **Описание**: Максимальное количество выходных токенов.
- **Тип**: `integer`

#### `generationConfig.presencePenalty`

- **Описание**: Штраф за присутствие токена.
- **Тип**: `float`

#### `generationConfig.frequencyPenalty`

- **Описание**: Штраф за частоту токена.
- **Тип**: `float`

#### `generationConfig.stopSequences`

- **Описание**: Список стоп-последовательностей.
- **Тип**: `array`

##### `generationConfig.stopSequences[]`

- **Описание**: Стоп-последовательность.
- **Тип**: `string`

#### `generationConfig.responseMimeType`

- **Описание**: MIME-тип ответа.
- **Тип**: `string`

#### `generationConfig.responseSchema`

- **Описание**: Схема ответа.
- **Тип**: `schema`

#### `generationConfig.seed`

- **Описание**: Зерно для случайной генерации.
- **Тип**: `integer`

#### `generationConfig.responseLogprobs`

- **Описание**: Включить логи вероятностей ответа.
- **Тип**: `boolean`

#### `generationConfig.logprobs`

- **Описание**: Количество токенов для логирования вероятностей.
- **Тип**: `integer`

#### `generationConfig.audioTimestamp`

- **Описание**: Добавлять ли временные метки к аудио.
- **Тип**: `boolean`

### `labels`

- **Описание**: Метки для запроса.
- **Тип**: `object`

#### `labels[].string`

- **Описание**: Значение метки.
- **Тип**: `string`