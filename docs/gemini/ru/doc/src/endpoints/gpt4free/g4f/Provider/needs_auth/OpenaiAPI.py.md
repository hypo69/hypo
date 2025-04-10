# Документация модуля OpenaiAPI

## Обзор

Модуль `OpenaiAPI` предоставляет класс `OpenaiAPI`, который является подклассом `OpenaiTemplate`. Этот класс предназначен для взаимодействия с OpenAI API, определяя основные атрибуты, такие как URL, URL для логина, базовый URL API, статус работоспособности и необходимость аутентификации.

## Подробней

Этот модуль предоставляет базовую конфигурацию для работы с OpenAI API. Он определяет URL-адреса, необходимые для аутентификации и взаимодействия с API, а также указывает, требуется ли аутентификация для использования API.

## Классы

### `OpenaiAPI`

**Описание**: Класс `OpenaiAPI` предоставляет конфигурацию для работы с OpenAI API.

**Наследует**:
- `OpenaiTemplate`: Наследует базовый класс `OpenaiTemplate`.

**Атрибуты**:
- `label` (str): Метка для OpenAI API (значение: `"OpenAI API"`).
- `url` (str): URL платформы OpenAI (значение: `"https://platform.openai.com"`).
- `login_url` (str): URL для страницы создания ключей API (значение: `"https://platform.openai.com/settings/organization/api-keys"`).
- `api_base` (str): Базовый URL для API OpenAI (значение: `"https://api.openai.com/v1"`).
- `working` (bool): Указывает, работает ли API (значение: `True`).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования API (значение: `True`).

## Функции

В данном модуле нет функций, только определение класса `OpenaiAPI` с атрибутами конфигурации.