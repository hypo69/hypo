# Модуль для определения моделей в g4f.Provider.hf

## Обзор

Этот модуль содержит определения моделей, используемых в `g4f.Provider.hf`. В нем определены различные текстовые и графические модели, их псевдонимы и модели по умолчанию.

## Подробней

Данный модуль предоставляет централизованный способ управления списком доступных моделей, что упрощает их использование и обновление в других частях проекта. Модуль определяет значения по умолчанию для различных типов моделей, а также предоставляет псевдонимы для упрощения их использования.

## Переменные

### `default_model`

```python
default_model = "Qwen/Qwen2.5-72B-Instruct"
```

Значение по умолчанию для текстовой модели. В данном случае, это "Qwen/Qwen2.5-72B-Instruct".

### `default_image_model`

```python
default_image_model = "black-forest-labs/FLUX.1-dev"
```

Значение по умолчанию для графической модели. В данном случае, это "black-forest-labs/FLUX.1-dev".

### `image_models`

```python
image_models = [    
    default_image_model,
    "black-forest-labs/FLUX.1-schnell",
]
```

Список доступных графических моделей, включающий модель по умолчанию и "black-forest-labs/FLUX.1-schnell".

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

Список доступных текстовых моделей, включающий "Qwen/Qwen2.5-72B-Instruct", 'meta-llama/Llama-3.3-70B-Instruct' и другие.

### `fallback_models`

```python
fallback_models = text_models + image_models
```

Комбинированный список текстовых и графических моделей, используемый в качестве резервного списка.

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

Словарь псевдонимов моделей, позволяющий использовать более короткие и понятные имена для обращения к моделям. Разделен на секции для чат-моделей, графических моделей и моделей, используемых в других провайдерах.

### `extra_models`

```python
extra_models = [
    "meta-llama/Llama-3.2-11B-Vision-Instruct",
    "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
    "NousResearch/Hermes-3-Llama-3.1-8B",
]
```

Список дополнительных моделей, которые могут использоваться в проекте.

### `default_vision_model`

```python
default_vision_model = "meta-llama/Llama-3.2-11B-Vision-Instruct"
```

Значение по умолчанию для модели обработки изображений. В данном случае, это "meta-llama/Llama-3.2-11B-Vision-Instruct".

### `default_llama_model`

```python
default_llama_model = "meta-llama/Llama-3.3-70B-Instruct"
```

Значение по умолчанию для модели Llama. В данном случае, это "meta-llama/Llama-3.3-70B-Instruct".

### `vision_models`

```python
vision_models = [default_vision_model, "Qwen/Qwen2-VL-7B-Instruct"]
```

Список моделей, предназначенных для обработки изображений, включающий `default_vision_model` и `Qwen/Qwen2-VL-7B-Instruct`.