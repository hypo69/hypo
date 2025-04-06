# Документация для разработчика: request.json

## Обзор

Файл `request.json` содержит структуру JSON, описывающую формат запроса к AI-модели Gemini. Он определяет различные параметры и настройки, которые могут быть использованы при взаимодействии с моделью, включая содержимое запроса, системные инструкции, инструменты, настройки безопасности, конфигурацию генерации и метки.

## Подробней

Этот файл предоставляет разработчикам подробную информацию о структуре запроса, необходимой для отправки запросов к AI-модели Gemini. Он определяет типы данных и форматы, которые должны быть использованы для каждого параметра, обеспечивая правильное взаимодействие с моделью.

## Структура JSON

### `cachedContent`

- **Описание**: Кэшированное содержимое.
- **Тип**: `string`

### `contents`

- **Описание**: Массив объектов, содержащих информацию о содержимом запроса.
- **Тип**: `array`
- **Элементы массива**:
  - `role` (string): Роль содержимого.
  - `parts` (array): Массив частей содержимого.
    - `text` (string): Текстовая часть содержимого.
    - `inlineData` (object): Встроенные данные.
      - `mimeType` (string): MIME-тип данных.
      - `data` (string): Данные в формате строки.
    - `fileData` (object): Данные файла.
      - `mimeType` (string): MIME-тип файла.
      - `fileUri` (string): URI файла.
    - `videoMetadata` (object): Метаданные видео.
      - `startOffset` (object): Начальное смещение.
        - `seconds` (integer): Секунды.
        - `nanos` (integer): Наносекунды.
      - `endOffset` (object): Конечное смещение.
        - `seconds` (integer): Секунды.
        - `nanos` (integer): Наносекунды.

### `systemInstruction`

- **Описание**: Системные инструкции.
- **Тип**: `object`
  - `role` (string): Роль инструкции.
  - `parts` (array): Массив частей инструкции.
    - `text` (string): Текст инструкции.

### `tools`

- **Описание**: Инструменты.
- **Тип**: `array`
- **Элементы массива**:
  - `functionDeclarations` (array): Массив объявлений функций.
    - `name` (string): Имя функции.
    - `description` (string): Описание функции.
    - `parameters` (object): Параметры функции.

### `safetySettings`

- **Описание**: Настройки безопасности.
- **Тип**: `array`
- **Элементы массива**:
  - `category` (enum): Категория вреда (`HarmCategory`).
  - `threshold` (enum): Порог блокировки (`HarmBlockThreshold`).

### `generationConfig`

- **Описание**: Конфигурация генерации.
- **Тип**: `object`
  - `temperature` (number): Температура.
  - `topP` (number): Top P.
  - `topK` (number): Top K.
  - `candidateCount` (integer): Количество кандидатов.
  - `maxOutputTokens` (integer): Максимальное количество выходных токенов.
  - `presencePenalty` (float): Штраф за присутствие.
  - `frequencyPenalty` (float): Штраф за частоту.
  - `stopSequences` (array): Последовательности остановки.
  - `responseMimeType` (string): MIME-тип ответа.
  - `responseSchema` (schema): Схема ответа.
  - `seed` (integer): Зерно.
  - `responseLogprobs` (boolean): Лог-вероятности ответа.
  - `logprobs` (integer): Лог-вероятности.
  - `audioTimestamp` (boolean): Временная метка аудио.

### `labels`

- **Описание**: Метки.
- **Тип**: `object`
- **Ключи**: `string`
- **Значения**: `string`

```