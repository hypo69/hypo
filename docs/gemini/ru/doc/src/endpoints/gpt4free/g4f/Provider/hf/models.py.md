# Модуль для определения списка доступных моделей и их алиасов в g4f

## Обзор

Модуль `models.py` содержит определения различных моделей машинного обучения, используемых в проекте `g4f`, а также их алиасы для удобства использования. Модуль определяет модели для работы с текстом и изображениями.

## Подробней

Этот модуль предназначен для централизованного хранения информации о доступных моделях и их алиасах, используемых в различных частях проекта `g4f`. Он облегчает поддержку и обновление списка моделей, а также позволяет использовать более короткие и понятные имена моделей в коде.

## Переменные

### `default_model`

```python
default_model = "Qwen/Qwen2.5-72B-Instruct"
```

**Описание**: Модель, используемая по умолчанию для обработки текста.

### `default_image_model`

```python
default_image_model = "black-forest-labs/FLUX.1-dev"
```

**Описание**: Модель, используемая по умолчанию для обработки изображений.

### `image_models`

```python
image_models = [    
    default_image_model,
    "black-forest-labs/FLUX.1-schnell",
]
```

**Описание**: Список доступных моделей для обработки изображений.

### `text_models`

```python
text_models = [
    default_model,
    'meta-llama/Llama-3.3-70B-Instruct',
    'CohereForAI/c4ai-command-r-plus-08-2024',
    'deepseek-ai/DeepSeek-R1-Distill-Qwen-32B',
    'Qwen/QwQ-32B',
    'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
    'Qwen/Qwen2.5-Coder-32B-Instruct',
    'meta-llama/Llama-3.2-11B-Vision-Instruct',
    'mistralai/Mistral-Nemo-Instruct-2407',
    'microsoft/Phi-3.5-mini-instruct',
]
```

**Описание**: Список доступных моделей для обработки текста.

### `fallback_models`

```python
fallback_models = text_models + image_models
```

**Описание**: Объединенный список моделей для обработки текста и изображений, используемый в качестве резервного варианта.

### `model_aliases`

```python
model_aliases = {
    ### Chat ###
    "qwen-2.5-72b": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "llama-3": "meta-llama/Llama-3.3-70B-Instruct",
    "llama-3.3-70b": "meta-llama/Llama-3.3-70B-Instruct",
    "command-r-plus": "CohereForAI/c4ai-command-r-plus-08-2024",
    "deepseek-r1": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    "qwq-32b": "Qwen/QwQ-32B",
    "nemotron-70b": "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
    "qwen-2.5-coder-32b": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "llama-3.2-11b": "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "mistral-nemo": "mistralai/Mistral-Nemo-Instruct-2407",
    "phi-3.5-mini": "microsoft/Phi-3.5-mini-instruct",
    ### Image ###
    "flux": "black-forest-labs/FLUX.1-dev",
    "flux-dev": "black-forest-labs/FLUX.1-dev",
    "flux-schnell": "black-forest-labs/FLUX.1-schnell",
    ### Used in other providers ###
    "qwen-2-vl-7b": "Qwen/Qwen2-VL-7B-Instruct",
    "gemma-2-27b": "google/gemma-2-27b-it",
    "qwen-2-72b": "Qwen/Qwen2-72B-Instruct",
    "qvq-72b": "Qwen/QVQ-72B-Preview",
    "sd-3.5": "stabilityai/stable-diffusion-3.5-large",
}
```

**Описание**: Словарь, содержащий алиасы для различных моделей. Ключи словаря - это алиасы, а значения - полные имена моделей. Разделены секции для чат-моделей, моделей обработки изображений и моделей, используемых в других провайдерах.

### `extra_models`

```python
extra_models = [
    "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
    "NousResearch/Hermes-3-Llama-3.1-8B",
]
```

**Описание**: Список дополнительных моделей, которые могут быть использованы в проекте.

### `default_vision_model`

```python
default_vision_model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
```

**Описание**: Модель, используемая по умолчанию для задач, связанных с компьютерным зрением.

### `default_llama_model`

```python
default_llama_model = "meta-llama/Llama-3.3-70B-Instruct"
```

**Описание**: Модель Llama, используемая по умолчанию.

### `vision_models`

```python
vision_models = [default_vision_model, "Qwen/Qwen2-VL-7B-Instruct"]
```

**Описание**: Список моделей, предназначенных для задач компьютерного зрения.