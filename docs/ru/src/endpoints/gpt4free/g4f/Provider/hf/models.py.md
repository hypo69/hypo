# Модуль для определения моделей в gpt4free

## Обзор

Модуль `models.py` определяет списки доступных текстовых и графических моделей, а также псевдонимы для удобного обращения к ним. Он содержит информацию о моделях, поддерживаемых gpt4free, и используется для конфигурации и выбора моделей при работе с библиотекой.

## Подробней

Этот файл содержит списки `text_models`, `image_models`, `fallback_models`, `extra_models` и `vision_models`, а также словарь `model_aliases`. Он предоставляет информацию о различных моделях, поддерживаемых gpt4free, и позволяет выбирать нужные модели для различных задач. Он определяет модели для обработки текста, генерации изображений и другие задачи.

## Переменные

### `default_model`

**Описание**: Модель, используемая по умолчанию.
**Значение**: `"Qwen/Qwen2.5-72B-Instruct"`

### `default_image_model`

**Описание**: Модель для генерации изображений, используемая по умолчанию.
**Значение**: `"black-forest-labs/FLUX.1-dev"`

### `image_models`

**Описание**: Список моделей для генерации изображений.
**Значение**: `["black-forest-labs/FLUX.1-dev", "black-forest-labs/FLUX.1-schnell"]`

### `text_models`

**Описание**: Список текстовых моделей.
**Значение**: `["Qwen/Qwen2.5-72B-Instruct", 'meta-llama/Llama-3.3-70B-Instruct', 'CohereForAI/c4ai-command-r-plus-08-2024', 'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B', 'Qwen/QwQ-32B', 'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF', 'Qwen/Qwen2.5-Coder-32B-Instruct', 'meta-llama/Llama-3.2-11B-Vision-Instruct', 'mistralai/Mistral-Nemo-Instruct-2407', 'microsoft/Phi-3.5-mini-instruct']`

### `fallback_models`

**Описание**: Список моделей, используемых в качестве запасных вариантов.
**Значение**: Объединение `text_models` и `image_models`.

### `model_aliases`

**Описание**: Словарь, содержащий псевдонимы моделей для удобного обращения к ним.
**Значение**: Словарь, где ключи - это псевдонимы, а значения - полные имена моделей.

### `extra_models`

**Описание**: Список дополнительных моделей.
**Значение**: `["meta-llama/Llama-3.2-11B-Vision-Instruct", "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF", "NousResearch/Hermes-3-Llama-3.1-8B"]`

### `default_vision_model`

**Описание**: Модель для работы с изображениями, используемая по умолчанию.
**Значение**: `"meta-llama/Llama-3.2-11B-Vision-Instruct"`

### `default_llama_model`

**Описание**: Модель llama, используемая по умолчанию.
**Значение**: `"meta-llama/Llama-3.3-70B-Instruct"`

### `vision_models`

**Описание**: Список моделей для работы с изображениями.
**Значение**: `["meta-llama/Llama-3.2-11B-Vision-Instruct", "Qwen/Qwen2-VL-7B-Instruct"]`