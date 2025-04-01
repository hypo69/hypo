# Модуль для работы с Vision API g4f (примеры изображений)

## Обзор

Данный модуль демонстрирует примеры использования Vision API из библиотеки `g4f` для анализа изображений. Он показывает, как можно обрабатывать как удаленные, так и локальные изображения, отправляя запросы к модели для распознавания объектов на изображении.

## Подробней

Модуль содержит примеры отправки изображений на анализ с использованием Vision API. В первом примере загружается изображение из удаленного источника, а во втором - локальное изображение. Результаты анализа выводятся на экран. Этот код может быть использован для тестирования и демонстрации возможностей Vision API библиотеки `g4f`.

## Функции

### Обработка удаленного изображения

```python
remote_image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/cat.jpeg", stream=True).content
response_remote = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=remote_image
)
print("Response for remote image:")
print(response_remote.choices[0].message.content)
```

**Назначение**: Обрабатывает удаленное изображение, загружая его из сети и отправляя запрос в Vision API для анализа.

**Как работает функция**:

1.  **Загрузка изображения**: Код загружает изображение кота из репозитория `gpt4free` по указанному URL. Используется `requests.get` с параметром `stream=True`, чтобы получить содержимое изображения в виде байтов.
2.  **Создание запроса**: Создается запрос к Vision API с использованием `client.chat.completions.create`. Указывается модель `g4f.models.default_vision`, сообщение с запросом "What are on this image?" и загруженное изображение.
3.  **Получение ответа**: Отправляется запрос и получается ответ от API.
4.  **Вывод результата**: Извлекается содержимое ответа из `response_remote.choices[0].message.content` и выводится на экран.

**Пример**:

```python
#  Не требуется, т.к. это часть примера использования модуля.
```

### Обработка локального изображения

```python
local_image = open("docs/images/cat.jpeg", "rb")
response_local = client.chat.completions.create(
    model=g4f.models.default_vision,
    messages=[
        {"role": "user", "content": "What are on this image?"}
    ],
    image=local_image
)
print("Response for local image:")
print(response_local.choices[0].message.content)
local_image.close()  # Close file after use
```

**Назначение**: Обрабатывает локальное изображение, открывая его из файла и отправляя запрос в Vision API для анализа.

**Как работает функция**:

1.  **Открытие изображения**: Код открывает локальное изображение "docs/images/cat.jpeg" в бинарном режиме для чтения (`"rb"`).
2.  **Создание запроса**: Создается запрос к Vision API с использованием `client.chat.completions.create`. Указывается модель `g4f.models.default_vision`, сообщение с запросом "What are on this image?" и открытое изображение.
3.  **Получение ответа**: Отправляется запрос и получается ответ от API.
4.  **Вывод результата**: Извлекается содержимое ответа из `response_local.choices[0].message.content` и выводится на экран.
5.  **Закрытие файла**: После использования файл изображения закрывается с помощью `local_image.close()`.

**Пример**:

```python
#  Не требуется, т.к. это часть примера использования модуля.