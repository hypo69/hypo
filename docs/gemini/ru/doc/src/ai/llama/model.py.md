# Модуль `src.ai.llama.model`

## Обзор

Модуль `src.ai.llama.model` предназначен для работы с моделью Meta-Llama-3.1-8B-Instruct-GGUF, используя библиотеку `llama_cpp`. Он загружает модель и генерирует текст на основе предоставленного запроса.

## Содержание

- [Обзор](#обзор)
- [Импорты](#импорты)
- [Переменные](#переменные)

## Импорты

В данном модуле импортируется библиотека `Llama` из пакета `llama_cpp`:

```python
from llama_cpp import Llama
```

## Переменные

### `llm`

Экземпляр модели `Llama`, загруженный из репозитория `lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF` с использованием файла `Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf`.

```python
llm = Llama.from_pretrained(
    repo_id="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF",
    filename="Meta-Llama-3.1-8B-Instruct-IQ4_XS.gguf",
)
```

### `output`

Результат генерации текста с использованием модели `llm`. Текст генерируется на основе запроса "Once upon a time," с ограничением в 512 токенов и с включенным эхо-режимом.

```python
output = llm(
    "Once upon a time,",
    max_tokens=512,
    echo=True
)
```

### `print(output)`

Выводит результат генерации текста в консоль.

```python
print(output)
```