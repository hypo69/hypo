# Модуль openai.js

## Обзор

Этот модуль предоставляет класс `OpenAI` для взаимодействия с API OpenAI, включая диалоговые чаты и транскрипцию аудио.

## Классы

### `OpenAI`

**Описание**: Класс `OpenAI` отвечает за взаимодействие с API OpenAI. Он инициализируется ключом API и предоставляет методы для диалогового чата и транскрипции аудио.

**Свойства**:

* `roles`: Объект, содержащий константы для ролей сообщений в чате (ASSISTANT, USER, SYSTEM).

**Методы**:

#### `chat`

**Описание**:  Выполняет диалоговый чат с моделью GPT-3.5-turbo.

**Параметры**:

* `messages` (array): Массив объектов, каждый из которых представляет собой сообщение в диалоговом чате. Каждый объект должен содержать `role` (например, 'user', 'assistant') и `content` (содержимое сообщения).

**Возвращает**:

* `message` (object | null): Объект с ответом модели, содержащий `role` и `content`. Возвращает `null`, если произошла ошибка.

**Вызывает исключения**:

* `Error`: Возникает при ошибке во время запроса к API. Сообщение об ошибке выводится в консоль.

#### `transcription`

**Описание**: Выполняет транскрипцию аудиофайла с помощью модели Whisper-1.

**Параметры**:

* `filepath` (string): Путь к аудиофайлу.

**Возвращает**:

* `text` (string | null): Текст транскрипции. Возвращает `null`, если произошла ошибка.

**Вызывает исключения**:

* `Error`: Возникает при ошибке во время запроса к API. Сообщение об ошибке выводится в консоль.

## Переменные

### `openai`

**Описание**: Экземпляр класса `OpenAI`, инициализированный с ключом API из файла `config`.


## Использование

```javascript
// Пример использования
import { openai } from './openai';

async function example() {
  const messages = [
    { role: openai.roles.USER, content: 'Привет!' },
  ];
  const response = await openai.chat(messages);
  console.log(response);

  //Пример транскрипции
  const filePath = 'path/to/your/audio.mp3';
  const transcription = await openai.transcription(filePath);
  console.log(transcription);
}

example();
```
```
```
```