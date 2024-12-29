# revai (rev.com - модель, которая умеет работать с звуковыми файлами переговоров, совещаний, звонков и т.п.)

## Обзор

Этот документ предоставляет информацию о работе с API rev.com для обработки звуковых файлов, таких как переговоры, совещания и звонки.

## Оглавление

1. [Обзор](#обзор)
2. [Ссылки](#ссылки)
3. [Примеры использования](#примеры-использования)

## Ссылки

- [Официальная документация Rev.com API](https://www.rev.com/api/docs)
- [Примеры кода на Python](https://docs.rev.ai/resources/code-samples/python/)

## Примеры использования

В данном разделе будут представлены примеры использования API Rev.com с использованием Python.

### **Пример 1: Отправка файла на транскрибацию**
(Предполагается, что используется библиотека для работы с API Rev.com)
```python
from revai.api import RevAiAPIClient

# Замените YOUR_ACCESS_TOKEN на ваш токен доступа
access_token = "YOUR_ACCESS_TOKEN"
client = RevAiAPIClient(access_token)

# Путь к аудиофайлу
audio_file_path = "path/to/your/audio.mp3"

try:
    job = client.submit_job_local_file(audio_file_path)
    print(f"Задание отправлено. ID: {job.id}")

    # Проверка статуса задания
    while True:
        job_details = client.get_job_details(job.id)
        if job_details.status == "transcribed":
            print("Транскрибация завершена.")
            break
        elif job_details.status == "failed":
            print(f"Транскрибация не удалась. Ошибка: {job_details.failure_reason}")
            break
        else:
            print(f"Статус задания: {job_details.status}. Ожидание...")
            time.sleep(10)

    # Получение результата транскрибации
    transcript = client.get_transcript_text(job.id)
    print("Транскрипция:")
    print(transcript)

except Exception as ex:
    print(f"Произошла ошибка: {ex}")

```
Этот пример показывает основной процесс:
- Инициализация клиента API.
- Отправка аудиофайла на транскрибацию.
- Периодическая проверка статуса задания.
- Получение и отображение результатов.

### **Пример 2: Получение списка заданий**
```python
from revai.api import RevAiAPIClient

# Замените YOUR_ACCESS_TOKEN на ваш токен доступа
access_token = "YOUR_ACCESS_TOKEN"
client = RevAiAPIClient(access_token)

try:
  jobs = client.get_list_of_jobs()
  print("Список заданий:")
  for job in jobs:
    print(f"ID: {job.id}, Статус: {job.status}, Имя файла: {job.name}")
except Exception as ex:
    print(f"Произошла ошибка: {ex}")
```
Этот пример показывает как получить список всех заданий, включая их ID, статус и имя файла.

### **Пример 3: Получение транскрипции в формате JSON**

```python
from revai.api import RevAiAPIClient

# Замените YOUR_ACCESS_TOKEN на ваш токен доступа
access_token = "YOUR_ACCESS_TOKEN"
client = RevAiAPIClient(access_token)

# ID задания
job_id = "YOUR_JOB_ID"
try:
    transcript_json = client.get_transcript_json(job_id)
    print("Транскрипция в JSON:")
    print(transcript_json)
except Exception as ex:
    print(f"Произошла ошибка: {ex}")
```
Этот пример показывает, как получить транскрипцию в формате JSON, что может быть полезно для более детального анализа.

**Примечание:**

- Для работы с API Rev.com необходимо установить библиотеку `revai`.
- Замените `"YOUR_ACCESS_TOKEN"` и `"YOUR_JOB_ID"` на ваши реальные токены и ID заданий.
- Более подробную информацию и другие примеры можно найти в официальной документации и примерах кода по ссылкам выше.