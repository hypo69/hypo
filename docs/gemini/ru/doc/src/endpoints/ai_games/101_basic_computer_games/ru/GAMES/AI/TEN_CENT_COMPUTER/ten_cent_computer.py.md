# Модуль `ten_cent_computer.py`

## Обзор

Этот модуль предоставляет класс `GoogleGenerativeAI` для взаимодействия с моделями Google Generative AI, а также содержит функции для установки ключа API в файл `.env` и основную логику запуска игр. Пользователь может выбрать одну из двух математических игр, инструкции для которых загружаются из MD-файлов, и взаимодействовать с моделью.

## Оглавление

1. [Классы](#Классы)
    - [`GoogleGenerativeAI`](#GoogleGenerativeAI)
2. [Функции](#Функции)
    - [`set_key`](#set_key)
3. [Основная логика](#Основная-логика)

## Классы

### `GoogleGenerativeAI`

**Описание**: Класс для взаимодействия с моделями Google Generative AI.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `GoogleGenerativeAI` с ключом API, системной инструкцией и названием модели.
- `ask`: Отправляет запрос модели и возвращает ответ.

#### `__init__`

**Описание**: Инициализация модели GoogleGenerativeAI.

**Параметры**:
- `api_key` (str): Ключ API для доступа к Gemini.
- `system_instruction` (str): Инструкция для модели (системный промпт).
- `model_name` (str, optional): Название используемой модели Gemini. По умолчанию `'gemini-2-13b'`.

#### `ask`

**Описание**: Отправка запроса модели и получение ответа.

**Параметры**:
- `q` (str): Текст запроса.

**Возвращает**:
- `str`: Ответ модели или сообщение об ошибке.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при отправке запроса к модели.

## Функции

### `set_key`

**Описание**: Сохраняет пару ключ-значение в .env файл.

**Параметры**:
- `dotenv_path` (str): Путь к файлу .env.
- `key` (str): Ключ для сохранения.
- `value` (str): Значение ключа для сохранения.

## Основная логика

Основная логика скрипта заключается в следующем:

1. **Инициализация**:
   - Определение абсолютного пути к директории с играми.
   - Чтение API-ключа из переменных окружения или ввод пользователем с последующим сохранением в `.env`.
   - Инициализация словаря с инструкциями для разных игр.
2. **Меню**:
   - Вывод приветствия и списка доступных игр.
   - Цикл для выбора игры или выхода.
3. **Выбор игры**:
   - Загрузка системной инструкции из MD-файла.
   - Инициализация модели `GoogleGenerativeAI` с полученной инструкцией.
   - Запуск цикла для ввода запросов пользователя и вывода ответов модели.
4. **Обработка ввода**:
   - Пользователь может вводить запросы для выбранной игры или выйти, введя "q".
   - Получение ответа от модели и вывод его в консоль.
5. **Обработка некорректного выбора**:
   - Если введен некорректный номер игры, пользователю выводится сообщение об ошибке.
6. **Завершение программы**:
   - Цикл завершается при вводе "q", программа выводит сообщение о завершении.