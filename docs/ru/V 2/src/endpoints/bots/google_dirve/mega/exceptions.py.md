# Модуль exceptions.py

## Обзор

Модуль `exceptions.py` содержит определения пользовательских исключений, специфичных для работы с Mega API. Эти исключения используются для обработки ошибок, возникающих в процессе взаимодействия с Mega API, таких как некорректный пароль или ошибки при выполнении запросов.

## Оглавление

1. [Классы](#Классы)
    - [MegaException](#MegaException)
    - [MegaIncorrectPasswordExcetion](#MegaIncorrectPasswordExcetion)
    - [MegaRequestException](#MegaRequestException)

## Классы

### `MegaException`

**Описание**:
Базовый класс для всех исключений, специфичных для Mega API.

### `MegaIncorrectPasswordExcetion`

**Описание**:
Исключение, которое возникает при вводе некорректного пароля или email.

### `MegaRequestException`

**Описание**:
Исключение, которое возникает при ошибке в запросе к Mega API.