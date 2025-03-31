# Документация для `scelation_request.json`

## Обзор

Этот файл представляет собой JSON-схему, описывающую структуру запроса для Gemini Simple Chat API. Он определяет формат данных, которые можно отправить в API, включая контент, инструкции, инструменты и настройки.

## Оглавление

1. [Обзор](#обзор)
2. [Структура JSON](#структура-json)
   - [cachedContent](#cachedcontent)
   - [contents](#contents)
     - [role](#role)
     - [parts](#parts)
       - [text](#text)
       - [inlineData](#inlinedata)
         - [mimeType](#mimetype)
         - [data](#data)
       - [fileData](#filedata)
         - [mimeType](#mimetype-1)
         - [fileUri](#fileuri)
       - [videoMetadata](#videometadata)
          - [startOffset](#startoffset)
           - [seconds](#seconds)
           - [nanos](#nanos)
          - [endOffset](#endoffset)
           - [seconds](#seconds-1)
           - [nanos](#nanos-1)
   - [systemInstruction](#systeminstruction)
     - [role](#role-1)
     - [parts](#parts-1)
       - [text](#text-1)
   - [tools](#tools)
     - [functionDeclarations](#functiondeclarations)
       - [name](#name)
       - [description](#description)
       - [parameters](#parameters)
   - [safetySettings](#safetysettings)
     - [category](#category)
     - [threshold](#threshold)
   - [generationConfig](#generationconfig)
     - [temperature](#temperature)
     - [topP](#topp)
     - [topK](#topk)
     - [candidateCount](#candidatecount)
     - [maxOutputTokens](#maxoutputtokens)
     - [presencePenalty](#presencepenalty)
     - [frequencyPenalty](#frequencypenalty)
     - [stopSequences](#stopsequences)
     - [responseMimeType](#responsemimetype)
     - [responseSchema](#responseschema)
     - [seed](#seed)
     - [responseLogprobs](#responselogprobs)
     - [logprobs](#logprobs)
     - [audioTimestamp](#audiotimestamp)
   - [labels](#labels)
   
## Структура JSON

### `cachedContent`
**Описание**: Кэшированный контент в виде строки.
**Тип**: `string`

### `contents`
**Описание**: Массив объектов контента, каждый из которых представляет собой сообщение или часть сообщения.
**Тип**: `array`
 
#### `role`
**Описание**: Роль отправителя сообщения.
**Тип**: `string`

#### `parts`
**Описание**: Массив объектов, представляющих различные части сообщения (текст, данные, файлы, и т.д.).
**Тип**: `array`

##### `text`
**Описание**: Текстовая часть сообщения.
**Тип**: `string`

##### `inlineData`
**Описание**: Данные, представленные в строке.
**Тип**: `object`

###### `mimeType`
**Описание**: MIME-тип данных.
**Тип**: `string`

###### `data`
**Описание**: Данные, закодированные в base64.
**Тип**: `string`

##### `fileData`
**Описание**: Ссылка на файл.
**Тип**: `object`

###### `mimeType`
**Описание**: MIME-тип файла.
**Тип**: `string`

###### `fileUri`
**Описание**: URI файла.
**Тип**: `string`
##### `videoMetadata`
**Описание**: Метаданные видео.
**Тип**: `object`

###### `startOffset`
**Описание**: Смещение начала видео.
**Тип**: `object`

####### `seconds`
**Описание**: Смещение начала видео в секундах.
**Тип**: `integer`

####### `nanos`
**Описание**: Смещение начала видео в наносекундах.
**Тип**: `integer`

###### `endOffset`
**Описание**: Смещение конца видео.
**Тип**: `object`

####### `seconds`
**Описание**: Смещение конца видео в секундах.
**Тип**: `integer`

####### `nanos`
**Описание**: Смещение конца видео в наносекундах.
**Тип**: `integer`

### `systemInstruction`
**Описание**: Объект, представляющий системные инструкции.
**Тип**: `object`

#### `role`
**Описание**: Роль системной инструкции.
**Тип**: `string`

#### `parts`
**Описание**: Массив частей системной инструкции.
**Тип**: `array`

##### `text`
**Описание**: Текстовая часть системной инструкции.
**Тип**: `string`

### `tools`
**Описание**: Массив инструментов для использования.
**Тип**: `array`

#### `functionDeclarations`
**Описание**: Массив объявлений функций.
**Тип**: `array`

##### `name`
**Описание**: Имя функции.
**Тип**: `string`

##### `description`
**Описание**: Описание функции.
**Тип**: `string`

##### `parameters`
**Описание**: Параметры функции (в виде объекта).
**Тип**: `object`

### `safetySettings`
**Описание**: Массив настроек безопасности.
**Тип**: `array`

#### `category`
**Описание**: Категория настройки безопасности.
**Тип**: `enum`

#### `threshold`
**Описание**: Пороговое значение настройки безопасности.
**Тип**: `enum`

### `generationConfig`
**Описание**: Объект, содержащий настройки генерации.
**Тип**: `object`

#### `temperature`
**Описание**: Температура для генерации.
**Тип**: `number`

#### `topP`
**Описание**: Top-P для генерации.
**Тип**: `number`

#### `topK`
**Описание**: Top-K для генерации.
**Тип**: `number`

#### `candidateCount`
**Описание**: Количество кандидатов для генерации.
**Тип**: `integer`

#### `maxOutputTokens`
**Описание**: Максимальное количество токенов для вывода.
**Тип**: `integer`

#### `presencePenalty`
**Описание**: Штраф за присутствие токена.
**Тип**: `float`

#### `frequencyPenalty`
**Описание**: Штраф за частоту токена.
**Тип**: `float`

#### `stopSequences`
**Описание**: Массив стоп-последовательностей.
**Тип**: `array`

#### `responseMimeType`
**Описание**: MIME-тип ответа.
**Тип**: `string`

#### `responseSchema`
**Описание**: Схема ответа.
**Тип**: `schema`

#### `seed`
**Описание**: Seed для генерации.
**Тип**: `integer`

#### `responseLogprobs`
**Описание**: Флаг логирования вероятностей ответа.
**Тип**: `boolean`

#### `logprobs`
**Описание**: Количество токенов для логирования вероятностей.
**Тип**: `integer`

#### `audioTimestamp`
**Описание**: Флаг для включения временных меток аудио.
**Тип**: `boolean`

### `labels`
**Описание**: Объект, содержащий произвольные метки.
**Тип**: `object`
**Ключ**: `string`
**Значение**: `string`