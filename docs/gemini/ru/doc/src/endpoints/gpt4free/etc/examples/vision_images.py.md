# Документация для модуля обработки изображений с использованием g4f

## Обзор

Этот модуль демонстрирует использование библиотеки `g4f` для обработки изображений. Он показывает, как отправлять изображения на анализ, используя модель компьютерного зрения по умолчанию (`g4f.models.default_vision`), как с локальных файлов, так и по URL.

## Подробнее

Модуль содержит примеры кода для обработки изображений, которые могут быть полезны при создании приложений, требующих анализа содержимого изображений. Здесь показано, как использовать клиент `g4f` для взаимодействия с API и отправки запросов на анализ изображений.

## Функции

### `client.chat.completions.create`

```python
response_remote = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=remote_image
)
```

**Назначение**: Отправляет запрос на анализ изображения.

**Параметры**:
- `model` (g4f.models.default_vision): Модель, используемая для анализа изображений. В данном случае используется модель компьютерного зрения по умолчанию.
- `messages` (list): Список сообщений, содержащих запрос пользователя. В данном случае, запрос "What are on this image?".
- `image` (bytes или файл): Изображение для анализа. Может быть передано как содержимое файла в формате bytes или как открытый файловый объект.

**Возвращает**:
- `response_remote`: Объект ответа, содержащий результаты анализа изображения.

**Как работает функция**:
1. Функция принимает изображение и текстовый запрос.
2. Формирует запрос к API `g4f` с использованием указанной модели и переданных данных.
3. Отправляет запрос и получает ответ с результатами анализа изображения.

```ascii
    Начало
     ↓
 Запрос изображения (remote_image или local_image)
     ↓
   Формирование запроса к API g4f
     ↓
   Отправка запроса и получение ответа
     ↓
Обработка ответа и вывод результатов
     ↓
     Конец
```

**Примеры**:

- Обработка удаленного изображения:

```python
remote_image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/cat.jpeg", stream=True).content
response_remote = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=remote_image
)
print(response_remote.choices[0].message.content)
```

- Обработка локального изображения:

```python
local_image = open("docs/images/cat.jpeg", "rb")
response_local = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=local_image
)
print(response_local.choices[0].message.content)
local_image.close()