# Модуль определения моделей для HF (Hugging Face)

## Обзор

Этот модуль содержит определения различных моделей, используемых в проекте, включая текстовые и визуальные модели, а также их псевдонимы. Он предоставляет централизованный способ управления списком доступных моделей и упрощает их использование в других частях проекта.

## Подробнее

Модуль определяет переменные, содержащие списки моделей, используемых для обработки текста и изображений. Также определены псевдонимы моделей, позволяющие использовать более короткие и понятные имена для обращения к моделям.

## Переменные

### `default_model`

**Описание**: Модель, используемая по умолчанию для обработки текста.

```python
default_model = "Qwen/Qwen2.5-72B-Instruct"
```

### `default_image_model`

**Описание**: Модель, используемая по умолчанию для обработки изображений.

```python
default_image_model = "black-forest-labs/FLUX.1-dev"
```

### `image_models`

**Описание**: Список моделей, доступных для обработки изображений.

```python
image_models = [
    default_image_model,
    "black-forest-labs/FLUX.1-schnell",
]
```

### `text_models`

**Описание**: Список моделей, доступных для обработки текста.

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

### `fallback_models`

**Описание**: Комбинированный список текстовых и визуальных моделей, используемый в качестве резервного списка.

```python
fallback_models = text_models + image_models
```

### `model_aliases`

**Описание**: Словарь, содержащий псевдонимы моделей. Ключ - псевдоним, значение - полное имя модели.

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

### `extra_models`

**Описание**: Список дополнительных моделей, которые могут быть использованы.

```python
extra_models = [
    "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
    "NousResearch/Hermes-3-Llama-3.1-8B",
]
```

### `default_vision_model`

**Описание**: Модель, используемая по умолчанию для задач, связанных с компьютерным зрением.

```python
default_vision_model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
```

### `default_llama_model`

**Описание**: Модель Llama, используемая по умолчанию.

```python
default_llama_model = "meta-llama/Llama-3.3-70B-Instruct"
```

### `vision_models`

**Описание**: Список моделей, используемых для задач компьютерного зрения.

```python
vision_models = [default_vision_model, "Qwen/Qwen2-VL-7B-Instruct"]