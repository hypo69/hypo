# Модуль для генерации таблиц в формате Markdown

## Обзор

Модуль предназначен для создания документации в формате Markdown, содержащей информацию о провайдерах и моделях, используемых в библиотеке `g4f`. Он включает функции для тестирования асинхронных провайдеров, а также для печати списков провайдеров и моделей в виде таблиц Markdown.

## Подробней

Этот модуль предоставляет инструменты для автоматического создания документации о доступных провайдерах и моделях, используемых в `g4f`. Он позволяет разработчикам легко получать актуальную информацию о поддерживаемых провайдерах, их статусе, моделях и возможностях (например, поддержка потоковой передачи, системных сообщений и истории сообщений). Сгенерированные таблицы можно использовать для обновления документации проекта.

## Функции

### `test_async`

**Назначение**: Асинхронно тестирует работоспособность заданного провайдера.

**Параметры**:
- `provider` (ProviderType): Провайдер для тестирования.

**Возвращает**:
- `bool`: `True`, если провайдер работает и успешно отвечает, `False` в противном случае.

**Как работает функция**:

1.  **Проверка работоспособности провайдера**: Функция начинается с проверки, активен ли провайдер (`if not provider.working`). Если провайдер не активен, функция немедленно возвращает `False`.
2.  **Подготовка сообщения**: Подготавливается тестовое сообщение (`messages`), которое будет отправлено провайдеру. Сообщение содержит роль пользователя и текст "Hello Assistant!".
3.  **Асинхронный вызов**: Функция пытается выполнить асинхронный вызов к провайдеру с использованием `ChatCompletion.create_async`. Устанавливается таймаут в 30 секунд.
4.  **Обработка ответа**: Если вызов завершается успешно и получен ответ, функция возвращает `True`.
5.  **Обработка исключений**: Если во время вызова возникает исключение, функция перехватывает его, выводит информацию об ошибке в консоль (если включено логирование) и возвращает `False`.

**ASII flowchart**:

```
A[Проверка работоспособности провайдера]
|
B[Подготовка сообщения]
|
C[Асинхронный вызов ChatCompletion.create_async с таймаутом]
|
D[Обработка ответа: Возврат True при успехе]
|
E[Обработка исключений: Логирование ошибки и возврат False]
```

**Примеры**:

```python
import asyncio
from g4f.providers import Ails

async def main():
    provider = Ails
    result = await test_async(provider)
    print(f"Provider {provider.__name__} is working: {result}")

asyncio.run(main())
```

### `test_async_list`

**Назначение**: Асинхронно тестирует список провайдеров и возвращает список результатов.

**Параметры**:
- `providers` (list[ProviderType]): Список провайдеров для тестирования.

**Возвращает**:
- `list`: Список булевых значений, где каждый элемент соответствует результату тестирования соответствующего провайдера.

**Как работает функция**:

1.  **Запуск асинхронных тестов для каждого провайдера**: Для каждого провайдера в списке `providers` запускается асинхронная функция `test_async`. Результаты выполнения сохраняются в списке `responses`.
2.  **Сбор результатов**: Функция `asyncio.run` используется для запуска асинхронных задач и получения результатов их выполнения.
3.  **Возврат списка результатов**: Функция возвращает список `responses`, содержащий результаты тестирования каждого провайдера.

**ASII flowchart**:

```
A[Получение списка провайдеров]
|
B[Запуск асинхронного теста для каждого провайдера]
|
C[Сбор результатов в список responses]
|
D[Возврат списка responses]
```

**Примеры**:

```python
import asyncio
from g4f.providers import Ails, Bard

async def main():
    providers = [Ails, Bard]
    results = test_async_list(providers)
    for i, provider in enumerate(providers):
        print(f"Provider {provider.__name__} is working: {results[i]}")

asyncio.run(main())
```

### `print_providers`

**Назначение**: Формирует Markdown-текст с таблицей, содержащей информацию о провайдерах.

**Возвращает**:
- `list[str]`: Список строк, представляющих Markdown-таблицу с информацией о провайдерах.

**Как работает функция**:

1.  **Фильтрация рабочих провайдеров**: Сначала функция фильтрует список доступных провайдеров, оставляя только те, которые помечены как рабочие (`provider.working`).
2.  **Асинхронное тестирование провайдеров**: Затем функция вызывает `test_async_list` для асинхронного тестирования отфильтрованных провайдеров и получает список результатов.
3.  **Формирование строк таблицы Markdown**: Функция создает строки для Markdown-таблицы, перебирая список провайдеров и результаты тестирования. Для каждого провайдера добавляется информация о его названии, веб-сайте, статусе, поддержке потоковой передачи, системных сообщений, истории сообщений и необходимости аутентификации.
4.  **Разделение на типы**: Провайдеры разделяются на два типа: "Free" (бесплатные) и "Auth" (требующие аутентификацию).
5.  **Добавление информации о моделях**: Для провайдеров, поддерживающих модели, добавляется информация о доступных моделях и моделях для генерации изображений.
6.  **Возврат списка строк**: Функция возвращает список строк, который можно объединить для получения полного Markdown-текста таблицы.

**ASII flowchart**:

```
A[Фильтрация рабочих провайдеров]
|
B[Асинхронное тестирование провайдеров]
|
C[Формирование строк таблицы Markdown]
|
D[Разделение на типы: Free и Auth]
|
E[Добавление информации о моделях]
|
F[Возврат списка строк]
```

**Примеры**:

```python
lines = print_providers()
print("\\n".join(lines))
```

### `print_models`

**Назначение**: Формирует Markdown-текст с таблицей, содержащей информацию о моделях.

**Возвращает**:
- `list[str]`: Список строк, представляющих Markdown-таблицу с информацией о моделях.

**Как работает функция**:

1.  **Определение базовых провайдеров и URL**: Функция определяет словари `base_provider_names` и `provider_urls`, содержащие информацию о базовых провайдерах и их URL-адресах.
2.  **Инициализация строк таблицы**: Функция инициализирует список строк `lines` с заголовками таблицы Markdown.
3.  **Перебор моделей**: Функция перебирает модели из `models.ModelUtils.convert.items()`.
4.  **Фильтрация моделей**: Функция фильтрует модели, оставляя только `gpt-3.5-turbo`, `gpt-4` и `gpt-4-turbo`.
5.  **Формирование строк таблицы**: Для каждой модели формируется строка таблицы, содержащая имя модели, базового провайдера, провайдера и веб-сайт.
6.  **Возврат списка строк**: Функция возвращает список строк, который можно объединить для получения полного Markdown-текста таблицы.

**ASII flowchart**:

```
A[Определение базовых провайдеров и URL]
|
B[Инициализация строк таблицы]
|
C[Перебор моделей]
|
D[Фильтрация моделей]
|
E[Формирование строк таблицы]
|
F[Возврат списка строк]
```

**Примеры**:

```python
lines = print_models()
print("\\n".join(lines))
```

### `print_image_models`

**Назначение**: Формирует Markdown-текст с таблицей, содержащей информацию о моделях для работы с изображениями.

**Возвращает**:
- `list[str]`: Список строк, представляющих Markdown-таблицу с информацией о моделях для работы с изображениями.

**Как работает функция**:

1.  **Инициализация строк таблицы**: Функция инициализирует список строк `lines` с заголовками таблицы Markdown.
2.  **Перебор провайдеров**: Функция перебирает провайдеры, у которых есть атрибуты `image_models` или `vision_models`.
3.  **Формирование строк таблицы**: Для каждого провайдера формируется строка таблицы, содержащая метку провайдера, имя провайдера, список моделей для генерации изображений, наличие моделей для анализа изображений (vision models) и веб-сайт провайдера.
4.  **Возврат списка строк**: Функция возвращает список строк, который можно объединить для получения полного Markdown-текста таблицы.

**ASII flowchart**:

```
A[Инициализация строк таблицы]
|
B[Перебор провайдеров с image_models или vision_models]
|
C[Формирование строк таблицы]
|
D[Возврат списка строк]
```

**Примеры**:

```python
lines = print_image_models()
print("\\n".join(lines))
```

## Главный блок `if __name__ == "__main__":`

В главном блоке скрипта происходит открытие файла `docs/providers.md` для записи и запись в него сгенерированных таблиц с информацией о провайдерах и моделях. Сначала записывается таблица провайдеров, затем добавляется разделитель, и после этого записывается таблица моделей для работы с изображениями. Таблица моделей (не для изображений) закомментирована в коде.