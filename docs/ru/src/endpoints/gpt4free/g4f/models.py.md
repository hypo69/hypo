# Модуль для определения и управления моделями машинного обучения
=========================================================

Модуль содержит классы для представления моделей машинного обучения, такие как `Model`, `ImageModel`, `AudioModel`, `VisionModel`, а также утилиты для работы с ними, включая `ModelUtils`. Определены различные модели и их провайдеры, сгруппированные по категориям (текст, аудио, изображение).

## Оглавление
- [Обзор](#обзор)
- [Классы](#классы)
    - [Model](#model)
    - [ImageModel](#imagemodel)
    - [AudioModel](#audiomodel)
    - [VisionModel](#visionmodel)
    - [ModelUtils](#modelutils)
- [Переменные](#переменные)
    - [default](#default)
    - [default_vision](#default_vision)
    - [Текстовые модели](#текстовые-модели)
        - [OpenAI](#openai)
        - [GigaChat](#gigachat)
        - [Meta](#meta)
        - [Mistral](#mistral)
        - [NousResearch](#nousresearch)
        - [Microsoft](#microsoft)
        - [Google DeepMind](#google-deepmind)
        - [Anthropic](#anthropic)
        - [Reka AI](#reka-ai)
        - [Blackbox AI](#blackbox-ai)
        - [CohereForAI](#cohereforai)
        - [Qwen](#qwen)
        - [Inflection](#inflection)
        - [DeepSeek](#deepseek)
        - [x.ai](#xai)
        - [Perplexity AI](#perplexity-ai)
        - [Nvidia](#nvidia)
        - [Databricks](#databricks)
        - [THUDM](#thudm)
        - [MiniMax](#minimax)
        - [01-ai](#01-ai)
        - [Cognitive Computations](#cognitive-computations)
        - [DeepInfra](#deepinfra)
        - [Lizpreciatior](#lizpreciatior)
        - [OpenBMB](#openbmb)
        - [Ai2](#ai2)
        - [Liquid AI](#liquid-ai)
        - [Uncensored AI](#uncensored-ai)
    - [Модели изображений](#модели-изображений)
        - [Stability AI](#stability-ai)
        - [Black Forest Labs](#black-forest-labs)
        - [OpenAI](#openai-1)
        - [Midjourney](#midjourney)
- [Переменные](#переменные)
    - [demo_models](#demo_models)
    - [\_\_models\_\_](#__models__)
    - [_all_models](#_all_models)

## Обзор

Этот модуль предоставляет инструменты для работы с различными моделями машинного обучения, включая их определение, конфигурацию и выбор оптимальных провайдеров для использования. Он содержит классы для представления моделей, такие как `Model`, `ImageModel`, `AudioModel` и `VisionModel`, а также утилиты для работы с ними, включая `ModelUtils`. Модуль также определяет различные модели и их провайдеры, сгруппированные по категориям, таким как текст, аудио и изображения.

## Классы

### `Model`

**Описание**:
Класс `Model` представляет конфигурацию модели машинного обучения.

**Принцип работы**:
Класс используется для хранения информации о конкретной модели машинного обучения, такой как ее имя, базовый провайдер и предпочтительный провайдер с логикой повторных попыток.

**Атрибуты**:
- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер для модели.
- `best_provider` (ProviderType): Предпочтительный провайдер для модели, обычно с логикой повторных попыток.

**Методы**:
- `__all__() -> list[str]`:
    ```python
    @staticmethod
    def __all__() -> list[str]:
        """Возвращает список всех имен моделей."""
        ...
    ```
    **Назначение**: Возвращает список всех имен моделей, доступных в модуле.

    **Параметры**:
    - Нет.

    **Возвращает**:
    - `list[str]`: Список всех имен моделей.

    **Как работает функция**:
    1. Функция возвращает список `_all_models`, содержащий имена всех определенных моделей.

    **Примеры**:
    ```python
    >>> Model.__all__()
    ['gpt-3.5-turbo', 'gpt-4', ...]
    ```

### `ImageModel`

**Описание**:
Класс `ImageModel` представляет модель для работы с изображениями и наследуется от класса `Model`.

**Принцип работы**:
Класс наследует все атрибуты и методы от базового класса `Model` и используется для представления моделей, специализирующихся на обработке изображений.

### `AudioModel`

**Описание**:
Класс `AudioModel` представляет модель для работы со звуком и наследуется от класса `Model`.

**Принцип работы**:
Класс наследует все атрибуты и методы от базового класса `Model` и используется для представления моделей, специализирующихся на обработке аудио.

### `VisionModel`

**Описание**:
Класс `VisionModel` представляет модель для работы с визуальными данными и наследуется от класса `Model`.

**Принцип работы**:
Класс наследует все атрибуты и методы от базового класса `Model` и используется для представления моделей, специализирующихся на обработке визуальных данных.

### `ModelUtils`

**Описание**:
Класс `ModelUtils` предоставляет утилиты для сопоставления строковых идентификаторов с экземплярами класса `Model`.

**Принцип работы**:
Этот класс содержит словарь `convert`, который используется для хранения соответствий между строковыми идентификаторами моделей и их фактическими экземплярами. Это позволяет легко получать доступ к моделям по их именам.

**Атрибуты**:
- `convert` (dict[str, Model]): Словарь, сопоставляющий строковые идентификаторы моделей с экземплярами класса `Model`.

## Переменные

### `default`

**Описание**:
Переменная `default` представляет модель по умолчанию.

**Принцип работы**:
Эта переменная используется для определения модели, которая будет использоваться по умолчанию, если не указана конкретная модель. Она имеет пустые значения для имени и базового провайдера, а также список предпочтительных провайдеров.

### `default_vision`

**Описание**:
Переменная `default_vision` представляет модель по умолчанию для работы с визуальными данными.

**Принцип работы**:
Аналогично `default`, эта переменная используется для определения модели, которая будет использоваться по умолчанию при работе с визуальными данными.

### Текстовые модели

#### OpenAI

- `gpt_3_5_turbo`: Модель GPT-3.5 Turbo.
- `gpt_4`: Модель GPT-4.
- `gpt_4o`: Модель GPT-4o.
- `gpt_4o_mini`: Мини-версия модели GPT-4o.
- `gpt_4o_audio`: Аудио модель GPT-4o.
- `o1`: Модель o1.
- `o1_mini`: Мини-версия модели o1.
- `o3_mini`: Мини-версия модели o3.

#### GigaChat

- `gigachat`: Модель GigaChat.

#### Meta

- `meta`: Модель Meta AI.
- `llama_2_7b`: Модель Llama 2 7B.
- `llama_3_8b`: Модель Llama 3 8B.
- `llama_3_70b`: Модель Llama 3 70B.
- `llama_3_1_8b`: Модель Llama 3.1 8B.
- `llama_3_1_70b`: Модель Llama 3.1 70B.
- `llama_3_1_405b`: Модель Llama 3.1 405B.
- `llama_3_2_1b`: Модель Llama 3.2 1B.
- `llama_3_2_3b`: Модель Llama 3.2 3B.
- `llama_3_2_11b`: Модель Llama 3.2 11B.
- `llama_3_2_90b`: Модель Llama 3.2 90B.
- `llama_3_3_70b`: Модель Llama 3.3 70B.

#### Mistral

- `mixtral_8x7b`: Модель Mixtral 8x7B.
- `mixtral_8x22b`: Модель Mixtral 8x22B.
- `mistral_nemo`: Модель Mistral Nemo.
- `mixtral_small_24b`: Модель Mixtral Small 24B.

#### NousResearch

- `hermes_3`: Модель Hermes 3.

#### Microsoft

- `phi_3_5_mini`: Модель Phi 3.5 Mini.
- `phi_4`: Модель Phi 4.
- `wizardlm_2_7b`: Модель WizardLM 2 7B.
- `wizardlm_2_8x22b`: Модель WizardLM 2 8x22B.

#### Google DeepMind

- `gemini`: Модель Gemini.
- `gemini_exp`: Экспериментальная модель Gemini.
- `gemini_1_5_flash`: Модель Gemini 1.5 Flash.
- `gemini_1_5_pro`: Модель Gemini 1.5 Pro.
- `gemini_2_0_flash`: Модель Gemini 2.0 Flash.
- `gemini_2_0_flash_thinking`: Модель Gemini 2.0 Flash Thinking.
- `gemini_2_0_flash_thinking_with_apps`: Модель Gemini 2.0 Flash Thinking with Apps.

#### Anthropic

- `claude_3_haiku`: Модель Claude 3 Haiku.
- `claude_3_5_sonnet`: Модель Claude 3.5 Sonnet.
- `claude_3_7_sonnet`: Модель Claude 3.7 Sonnet.

#### Reka AI

- `reka_core`: Модель Reka Core.

#### Blackbox AI

- `blackboxai`: Модель Blackbox AI.
- `blackboxai_pro`: Модель Blackbox AI Pro.

#### CohereForAI

- `command_r`: Модель Command-R.
- `command_r_plus`: Модель Command-R+.
- `command_r7b`: Модель Command-R7B.
- `command_a`: Модель Command-A.

#### Qwen

- `qwen_1_5_7b`: Модель Qwen 1.5 7B.
- `qwen_2_72b`: Модель Qwen 2 72B.
- `qwen_2_vl_7b`: Модель Qwen 2 VL 7B.
- `qwen_2_5`: Модель Qwen 2.5.
- `qwen_2_5_72b`: Модель Qwen 2.5 72B.
- `qwen_2_5_coder_32b`: Модель Qwen 2.5 Coder 32B.
- `qwen_2_5_1m`: Модель Qwen 2.5 1M.
- `qwen_2_5_max`: Модель Qwen 2-5-max.

#### Inflection

- `pi`: Модель Pi.

#### DeepSeek

- `deepseek_chat`: Модель DeepSeek Chat.
- `deepseek_v3`: Модель DeepSeek V3.
- `deepseek_r1`: Модель DeepSeek R1.
- `janus_pro_7b`: Модель Janus Pro 7B.

#### x.ai

- `grok_3`: Модель Grok-3.
- `grok_3_r1`: Модель Grok-3-R1.

#### Perplexity AI

- `sonar`: Модель Sonar.
- `sonar_pro`: Модель Sonar Pro.
- `sonar_reasoning`: Модель Sonar Reasoning.
- `sonar_reasoning_pro`: Модель Sonar Reasoning Pro.
- `r1_1776`: Модель R1-1776.

#### Nvidia

- `nemotron_70b`: Модель Nemotron-70b.

#### Databricks

- `dbrx_instruct`: Модель DBRX Instruct.

#### THUDM

- `glm_4`: Модель GLM-4.

#### MiniMax

- `mini_max`: Модель MiniMax.

#### 01-ai

- `yi_34b`: Модель Yi-34b.

#### Cognitive Computations

- `dolphin_2_6`: Модель Dolphin-2.6.
- `dolphin_2_9`: Модель Dolphin-2.9.

#### DeepInfra

- `airoboros_70b`: Модель Airoboros-70b.

#### Lizpreciatior

- `lzlv_70b`: Модель Lzlv-70b.

#### OpenBMB

- `minicpm_2_5`: Модель Minicpm-2.5.

#### Ai2

- `tulu_3_405b`: Модель Tulu-3-405b.
- `olmo_2_13b`: Модель OLMo-2-13b.
- `tulu_3_1_8b`: Модель Tulu-3-1-8b.
- `tulu_3_70b`: Модель Tulu-3-70b.
- `olmoe_0125`: Модель OLMoE-0125.

#### Liquid AI

- `lfm_40b`: Модель LFM-40b.

#### Uncensored AI

- `evil`: Модель Evil.

### Модели изображений

#### Stability AI

- `sdxl_turbo`: Модель SDXL Turbo.
- `sd_3_5`: Модель SD-3.5.

#### Black Forest Labs

- `flux`: Модель Flux.
- `flux_pro`: Модель Flux Pro.
- `flux_dev`: Модель Flux Dev.
- `flux_schnell`: Модель Flux Schnell.

#### OpenAI

- `dall_e_3`: Модель DALL-E 3.

#### Midjourney

- `midjourney`: Модель Midjourney.

### `demo_models`

**Описание**:
Словарь, содержащий модели и их предпочтительных провайдеров для демонстрационных целей.

**Принцип работы**:
Этот словарь используется для хранения моделей, которые предназначены для демонстрации возможностей библиотеки. Он сопоставляет имена моделей со списками, содержащими модель и список предпочтительных провайдеров.

### `__models__`

**Описание**:
Словарь, содержащий модели и их доступных провайдеров.

**Принцип работы**:
Этот словарь создается путем итерации по моделям и их предпочтительным провайдерам, чтобы определить, какие провайдеры доступны для каждой модели.

### `_all_models`

**Описание**:
Список, содержащий имена всех моделей.

**Принцип работы**:
Этот список создается путем извлечения имен из словаря `__models__`.