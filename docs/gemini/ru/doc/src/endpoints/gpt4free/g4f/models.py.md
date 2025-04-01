# Модуль `models.py`

## Обзор

Модуль `models.py` содержит определения классов для представления различных моделей машинного обучения, используемых в проекте `hypotez`. Он также включает утилиты для работы с этими моделями, такие как преобразование строковых идентификаторов в экземпляры моделей и предоставление списка всех доступных моделей. Модуль предназначен для централизованного управления информацией о моделях и упрощения доступа к ним в других частях проекта.

## Подробнее

Модуль определяет несколько классов, включая `Model`, `ImageModel`, `AudioModel` и `VisionModel`, которые используются для представления различных типов моделей машинного обучения. Класс `Model` является базовым классом для всех моделей и содержит информацию об имени модели, базовом провайдере и предпочтительном провайдере. Подклассы `ImageModel`, `AudioModel` и `VisionModel` используются для представления моделей, работающих с изображениями, аудио и видео соответственно.
Модуль также определяет класс `ModelUtils`, который предоставляет утилиты для работы с моделями, такие как преобразование строковых идентификаторов в экземпляры моделей.
В модуле определены различные модели, такие как `gpt_3_5_turbo`, `gpt_4`, `llama_2_7b`, `mixtral_8x7b` и другие, а также модели для работы с изображениями, такие как `sdxl_turbo`, `dall_e_3` и другие.
Также в модуле создается словарь `demo_models`, содержащий список моделей для демонстрации и список провайдеров, которые с ними работают.
В конце модуля создается список всех моделей и провайдеров, которые с ними работают.

## Классы

### `Model`

**Описание**: Базовый класс для представления моделей машинного обучения.

**Атрибуты**:

- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер для модели.
- `best_provider` (ProviderType): Предпочтительный провайдер для модели. Обычно используется с логикой повторных попыток.

**Методы**:

- `__all__() -> list[str]`: Возвращает список имен всех моделей.

### `ImageModel`

**Описание**: Класс для представления моделей, работающих с изображениями.
**Наследует**: `Model`

### `AudioModel`

**Описание**: Класс для представления моделей, работающих с аудио.
**Наследует**: `Model`

### `VisionModel`

**Описание**: Класс для представления моделей, работающих с видео.
**Наследует**: `Model`

### `ModelUtils`

**Описание**: Утилитный класс для сопоставления строковых идентификаторов с экземплярами моделей.

**Атрибуты**:

- `convert` (dict[str, Model]): Словарь, сопоставляющий строковые идентификаторы моделей с экземплярами `Model`.

## Функции

В данном модуле функции отсутствуют, так как основная логика реализована через классы и их методы. Ниже приведено описание атрибутов экземпляров классов, представляющих конкретные модели.

### `default`

**Описание**: Модель, используемая по умолчанию.

**Атрибуты**:

- `name` (str): Пустая строка.
- `base_provider` (str): Пустая строка.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `Blackbox`, `Copilot`, `DeepInfraChat`, `AllenAI`, `PollinationsAI`, `TypeGPT`, `OIVSCode`, `ChatGptEs`, `Free2GPT`, `FreeGpt`, `Glider`, `Dynaspark`, `OpenaiChat`, `Jmuz`, `Cloudflare`.

### `default_vision`

**Описание**: Модель для работы с видео, используемая по умолчанию.

**Атрибуты**:

- `name` (str): Пустая строка.
- `base_provider` (str): Пустая строка.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `OIVSCode`, `TypeGPT`, `DeepInfraChat`, `PollinationsAI`, `Dynaspark`, `HuggingSpace`, `GeminiPro`, `HuggingFaceAPI`, `CopilotAccount`, `OpenaiAccount`, `Gemini`. Параметр `shuffle` установлен в `False`.

### `gpt_3_5_turbo`

**Описание**: Модель GPT-3.5 Turbo.

**Атрибуты**:

- `name` (str): `'gpt-3.5-turbo'`.
- `base_provider` (str): `'OpenAI'`.

### `gpt_4`

**Описание**: Модель GPT-4.

**Атрибуты**:

- `name` (str): `'gpt-4'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `Jmuz`, `ChatGptEs`, `PollinationsAI`, `Yqcloud`, `Goabror`, `Copilot`, `OpenaiChat`, `Liaobots`.

### `gpt_4o`

**Описание**: Модель GPT-4o.

**Атрибуты**:

- `name` (str): `'gpt-4o'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `Jmuz`, `ChatGptEs`, `PollinationsAI`, `Liaobots`, `OpenaiChat`.

### `gpt_4o_mini`

**Описание**: Модель GPT-4o Mini.

**Атрибуты**:

- `name` (str): `'gpt-4o-mini'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `Blackbox`, `ChatGptEs`, `TypeGPT`, `PollinationsAI`, `OIVSCode`, `Liaobots`, `Jmuz`, `OpenaiChat`.

### `gpt_4o_audio`

**Описание**: Аудио модель GPT-4o.

**Атрибуты**:

- `name` (str): `'gpt-4o-audio'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (ProviderType): `PollinationsAI`.

### `o1`

**Описание**: Модель o1.

**Атрибуты**:

- `name` (str): `'o1'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `Copilot`, `OpenaiAccount`.

### `o1_mini`

**Описание**: Модель o1 Mini.

**Атрибуты**:

- `name` (str): `'o1-mini'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (ProviderType): `OpenaiAccount`.

### `o3_mini`

**Описание**: Модель o3 Mini.

**Атрибуты**:

- `name` (str): `'o3-mini'`.
- `base_provider` (str): `'OpenAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `Blackbox`, `PollinationsAI`, `Liaobots`.

### `gigachat`

**Описание**: Модель GigaChat.

**Атрибуты**:

- `name` (str): `'GigaChat:latest'`.
- `base_provider` (str): `'gigachat'`.
- `best_provider` (ProviderType): `GigaChat`.

### `meta`

**Описание**: Модель Meta AI.

**Атрибуты**:

- `name` (str): `"meta-ai"`.
- `base_provider` (str): `"Meta"`.
- `best_provider` (ProviderType): `MetaAI`.

### `llama_2_7b`

**Описание**: Модель Llama 2 7b.

**Атрибуты**:

- `name` (str): `"llama-2-7b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (ProviderType): `Cloudflare`.

### `llama_3_8b`

**Описание**: Модель Llama 3 8b.

**Атрибуты**:

- `name` (str): `"llama-3-8b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Jmuz`, `Cloudflare`.

### `llama_3_70b`

**Описание**: Модель Llama 3 70b.

**Атрибуты**:

- `name` (str): `"llama-3-70b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (ProviderType): `Jmuz`.

### `llama_3_1_8b`

**Описание**: Модель Llama 3.1 8b.

**Атрибуты**:

- `name` (str): `"llama-3.1-8b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepInfraChat`, `Glider`, `PollinationsAI`, `AllenAI`, `Jmuz`, `Cloudflare`.

### `llama_3_1_70b`

**Описание**: Модель Llama 3.1 70b.

**Атрибуты**:

- `name` (str): `"llama-3.1-70b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Glider`, `AllenAI`, `Jmuz`.

### `llama_3_1_405b`

**Описание**: Модель Llama 3.1 405b.

**Атрибуты**:

- `name` (str): `"llama-3.1-405b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `AllenAI`, `Jmuz`.

### `llama_3_2_1b`

**Описание**: Модель Llama 3.2 1b.

**Атрибуты**:

- `name` (str): `"llama-3.2-1b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (ProviderType): `Cloudflare`.

### `llama_3_2_3b`

**Описание**: Модель Llama 3.2 3b.

**Атрибуты**:

- `name` (str): `"llama-3.2-3b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (ProviderType): `Glider`.

### `llama_3_2_11b`

**Описание**: Модель Llama 3.2 11b.

**Атрибуты**:

- `name` (str): `"llama-3.2-11b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Jmuz`, `HuggingChat`, `HuggingFace`.

### `llama_3_2_90b`

**Описание**: Модель Llama 3.2 90b.

**Атрибуты**:

- `name` (str): `"llama-3.2-90b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepInfraChat`, `Jmuz`.

### `llama_3_3_70b`

**Описание**: Модель Llama 3.3 70b.

**Атрибуты**:

- `name` (str): `"llama-3.3-70b"`.
- `base_provider` (str): `"Meta Llama"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `DeepInfraChat`, `LambdaChat`, `PollinationsAI`, `Jmuz`, `HuggingChat`, `HuggingFace`.

### `mixtral_8x7b`

**Описание**: Модель Mixtral 8x7b.

**Атрибуты**:

- `name` (str): `"mixtral-8x7b"`.
- `base_provider` (str): `"Mistral"`.
- `best_provider` (ProviderType): `Jmuz`.

### `mixtral_8x22b`

**Описание**: Модель Mixtral 8x22b.

**Атрибуты**:

- `name` (str): `"mixtral-8x22b"`.
- `base_provider` (str): `"Mistral"`.
- `best_provider` (ProviderType): `DeepInfraChat`.

### `mistral_nemo`

**Описание**: Модель Mistral Nemo.

**Атрибуты**:

- `name` (str): `"mistral-nemo"`.
- `base_provider` (str): `"Mistral"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `PollinationsAI`, `HuggingChat`, `HuggingFace`.

### `mixtral_small_24b`

**Описание**: Модель Mixtral Small 24b.

**Атрибуты**:

- `name` (str): `"mixtral-small-24b"`.
- `base_provider` (str): `"Mistral"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `DeepInfraChat`.

### `hermes_3`

**Описание**: Модель Hermes 3.

**Атрибуты**:

- `name` (str): `"hermes-3"`.
- `base_provider` (str): `"NousResearch"`.
- `best_provider` (ProviderType): `LambdaChat`.

### `phi_3_5_mini`

**Описание**: Модель Phi 3.5 Mini.

**Атрибуты**:

- `name` (str): `"phi-3.5-mini"`.
- `base_provider` (str): `"Microsoft"`.
- `best_provider` (ProviderType): `HuggingChat`.

### `phi_4`

**Описание**: Модель Phi 4.

**Атрибуты**:

- `name` (str): `"phi-4"`.
- `base_provider` (str): `"Microsoft"`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepInfraChat`, `PollinationsAI`, `HuggingSpace`.

### `wizardlm_2_7b`

**Описание**: Модель WizardLM 2 7b.

**Атрибуты**:

- `name` (str): `'wizardlm-2-7b'`.
- `base_provider` (str): `'Microsoft'`.
- `best_provider` (ProviderType): `DeepInfraChat`.

### `wizardlm_2_8x22b`

**Описание**: Модель WizardLM 2 8x22b.

**Атрибуты**:

- `name` (str): `'wizardlm-2-8x22b'`.
- `base_provider` (str): `'Microsoft'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepInfraChat`, `Jmuz`.

### `gemini`

**Описание**: Модель Gemini 2.0.

**Атрибуты**:

- `name` (str): `'gemini-2.0'`.
- `base_provider` (str): `'Google'`.
- `best_provider` (ProviderType): `Gemini`.

### `gemini_exp`

**Описание**: Модель Gemini Exp.

**Атрибуты**:

- `name` (str): `'gemini-exp'`.
- `base_provider` (str): `'Google'`.
- `best_provider` (ProviderType): `Jmuz`.

### `gemini_1_5_flash`

**Описание**: Модель Gemini 1.5 Flash.

**Атрибуты**:

- `name` (str): `'gemini-1.5-flash'`.
- `base_provider` (str): `'Google DeepMind'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Free2GPT`, `FreeGpt`, `TeachAnything`, `Websim`, `Dynaspark`, `Jmuz`, `GeminiPro`.

### `gemini_1_5_pro`

**Описание**: Модель Gemini 1.5 Pro.

**Атрибуты**:

- `name` (str): `'gemini-1.5-pro'`.
- `base_provider` (str): `'Google DeepMind'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Free2GPT`, `FreeGpt`, `TeachAnything`, `Websim`, `Jmuz`, `GeminiPro`.

### `gemini_2_0_flash`

**Описание**: Модель Gemini 2.0 Flash.

**Атрибуты**:

- `name` (str): `'gemini-2.0-flash'`.
- `base_provider` (str): `'Google DeepMind'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Dynaspark`, `GeminiPro`, `Gemini`.

### `gemini_2_0_flash_thinking`

**Описание**: Модель Gemini 2.0 Flash Thinking.

**Атрибуты**:

- `name` (str): `'gemini-2.0-flash-thinking'`.
- `base_provider` (str): `'Google DeepMind'`.
- `best_provider` (ProviderType): `Gemini`.

### `gemini_2_0_flash_thinking_with_apps`

**Описание**: Модель Gemini 2.0 Flash Thinking with Apps.

**Атрибуты**:

- `name` (str): `'gemini-2.0-flash-thinking-with-apps'`.
- `base_provider` (str): `'Google DeepMind'`.
- `best_provider` (ProviderType): `Gemini`.

### `claude_3_haiku`

**Описание**: Модель Claude 3 Haiku.

**Атрибуты**:

- `name` (str): `'claude-3-haiku'`.
- `base_provider` (str): `'Anthropic'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DDG`, `Jmuz`.

### `claude_3_5_sonnet`

**Описание**: Модель Claude 3.5 Sonnet.

**Атрибуты**:

- `name` (str): `'claude-3.5-sonnet'`.
- `base_provider` (str): `'Anthropic'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Jmuz`, `Liaobots`.

### `claude_3_7_sonnet`

**Описание**: Модель Claude 3.7 Sonnet.

**Атрибуты**:

- `name` (str): `'claude-3.7-sonnet'`.
- `base_provider` (str): `'Anthropic'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `Liaobots`.

### `reka_core`

**Описание**: Модель Reka Core.

**Атрибуты**:

- `name` (str): `'reka-core'`.
- `base_provider` (str): `'Reka AI'`.
- `best_provider` (ProviderType): `Reka`.

### `blackboxai`

**Описание**: Модель Blackbox AI.

**Атрибуты**:

- `name` (str): `'blackboxai'`.
- `base_provider` (str): `'Blackbox AI'`.
- `best_provider` (ProviderType): `Blackbox`.

### `blackboxai_pro`

**Описание**: Модель Blackbox AI Pro.

**Атрибуты**:

- `name` (str): `'blackboxai-pro'`.
- `base_provider` (str): `'Blackbox AI'`.
- `best_provider` (ProviderType): `Blackbox`.

### `command_r`

**Описание**: Модель Command-R.

**Атрибуты**:

- `name` (str): `'command-r'`.
- `base_provider` (str): `'CohereForAI'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `command_r_plus`

**Описание**: Модель Command-R-Plus.

**Атрибуты**:

- `name` (str): `'command-r-plus'`.
- `base_provider` (str): `'CohereForAI'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `HuggingSpace`, `HuggingChat`.

### `command_r7b`

**Описание**: Модель Command-R7B.

**Атрибуты**:

- `name` (str): `'command-r7b'`.
- `base_provider` (str): `'CohereForAI'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `command_a`

**Описание**: Модель Command-A.

**Атрибуты**:

- `name` (str): `'command-a'`.
- `base_provider` (str): `'CohereForAI'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `qwen_1_5_7b`

**Описание**: Модель Qwen 1.5 7b.

**Атрибуты**:

- `name` (str): `'qwen-1.5-7b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `Cloudflare`.

### `qwen_2_72b`

**Описание**: Модель Qwen 2 72b.

**Атрибуты**:

- `name` (str): `'qwen-2-72b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepInfraChat`, `HuggingSpace`.

### `qwen_2_vl_7b`

**Описание**: Модель Qwen 2 VL 7b.

**Атрибуты**:

- `name` (str): "qwen-2-vl-7b".
- `base_provider` (str): 'Qwen'.
- `best_provider` (ProviderType): `HuggingFaceAPI`.

### `qwen_2_5`

**Описание**: Модель Qwen 2.5.

**Атрибуты**:

- `name` (str): `'qwen-2.5'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `qwen_2_5_72b`

**Описание**: Модель Qwen 2.5 72b.

**Атрибуты**:

- `name` (str): `'qwen-2.5-72b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `Jmuz`.

### `qwen_2_5_coder_32b`

**Описание**: Модель Qwen 2.5 Coder 32b.

**Атрибуты**:

- `name` (str): `'qwen-2.5-coder-32b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `PollinationsAI`, `Jmuz`, `HuggingChat`.

### `qwen_2_5_1m`

**Описание**: Модель Qwen 2.5 1m.

**Атрибуты**:

- `name` (str): `'qwen-2.5-1m'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `qwen_2_5_max`

**Описание**: Модель Qwen 2-5-max.

**Атрибуты**:

- `name` (str): `'qwen-2-5-max'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `qwq_32b`

**Описание**: Модель Qwq 32b.

**Атрибуты**:

- `name` (str): `'qwq-32b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Jmuz`, `HuggingChat`.

### `qvq_72b`

**Описание**: Модель Qvq 72b.

**Атрибуты**:

- `name` (str): `'qvq-72b'`.
- `base_provider` (str): `'Qwen'`.
- `best_provider` (ProviderType): `HuggingSpace`.

### `pi`

**Описание**: Модель Pi.

**Атрибуты**:

- `name` (str): `'pi'`.
- `base_provider` (str): `'Inflection'`.
- `best_provider` (ProviderType): `Pi`.

### `deepseek_chat`

**Описание**: Модель DeepSeek Chat.

**Атрибуты**:

- `name` (str): `'deepseek-chat'`.
- `base_provider` (str): `'DeepSeek'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `Jmuz`.

### `deepseek_v3`

**Описание**: Модель DeepSeek V3.

**Атрибуты**:

- `name` (str): `'deepseek-v3'`.
- `base_provider` (str): `'DeepSeek'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `DeepInfraChat`, `LambdaChat`, `OIVSCode`, `TypeGPT`, `Liaobots`.

### `deepseek_r1`

**Описание**: Модель DeepSeek R1.

**Атрибуты**:

- `name` (str): `'deepseek-r1'`.
- `base_provider` (str): `'DeepSeek'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `Blackbox`, `DeepInfraChat`, `Glider`, `LambdaChat`, `PollinationsAI`, `TypeGPT`, `Liaobots`, `Jmuz`, `HuggingChat`, `HuggingFace`.

### `janus_pro_7b`

**Описание**: Модель Janus Pro 7b.

**Атрибуты**:

- `name` (str): DeepseekAI_JanusPro7b.default_model.
- `base_provider` (str): 'DeepSeek'.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `DeepseekAI_JanusPro7b`, `G4F`.

### `grok_3`

**Описание**: Модель Grok 3.

**Атрибуты**:

- `name` (str): `'grok-3'`.
- `base_provider` (str): `'x.ai'`.
- `best_provider` (ProviderType): `Grok`.

### `grok_3_r1`

**Описание**: Модель Grok 3 R1.

**Атрибуты**:

- `name` (str): `'grok-3-r1'`.
- `base_provider` (str): `'x.ai'`.
- `best_provider` (ProviderType): `Grok`.

### `sonar`

**Описание**: Модель Sonar.

**Атрибуты**:

- `name` (str): `'sonar'`.
- `base_provider` (str): `'Perplexity AI'`.
- `best_provider` (ProviderType): `PerplexityLabs`.

### `sonar_pro`

**Описание**: Модель Sonar Pro.

**Атрибуты**:

- `name` (str): `'sonar-pro'`.
- `base_provider` (str): `'Perplexity AI'`.
- `best_provider` (ProviderType): `PerplexityLabs`.

### `sonar_reasoning`

**Описание**: Модель Sonar Reasoning.

**Атрибуты**:

- `name` (str): `'sonar-reasoning'`.
- `base_provider` (str): `'Perplexity AI'`.
- `best_provider` (ProviderType): `PerplexityLabs`.

### `sonar_reasoning_pro`

**Описание**: Модель Sonar Reasoning Pro.

**Атрибуты**:

- `name` (str): `'sonar-reasoning-pro'`.
- `base_provider` (str): `'Perplexity AI'`.
- `best_provider` (ProviderType): `PerplexityLabs`.

### `r1_1776`

**Описание**: Модель R1 1776.

**Атрибуты**:

- `name` (str): `'r1-1776'`.
- `base_provider` (str): `'Perplexity AI'`.
- `best_provider` (ProviderType): `PerplexityLabs`.

### `nemotron_70b`

**Описание**: Модель Nemotron 70b.

**Атрибуты**:

- `name` (str): `'nemotron-70b'`.
- `base_provider` (str): `'Nvidia'`.
- `best_provider` (IterListProvider): Объект `IterListProvider`, содержащий список провайдеров: `LambdaChat`, `HuggingChat`, `HuggingFace`.

### `dbrx_instruct`

**Описание**: Модель DBRX Instruct.

**Атрибуты**:

- `name` (str): `'dbrx-instruct'`.
- `base_provider` (str): `'Databricks'`.
- `best_provider` (ProviderType): `DeepInfraChat`.

### `glm_4`

**Описание**: Модель GLM-4.

**Атрибуты**:

- `name` (str): `'glm-4'`.
- `base_provider` (str): `'THUDM'`.
- `best_provider` (ProviderType): `ChatGLM`.

### `mini_max`

**Описание**: Модель MiniMax.

**Атрибуты**:

- `name` (str): "MiniMax".
- `base_provider` (str): "MiniMax".
- `best_provider` (ProviderType): `HailuoAI`.

### `yi_34b`

**Описание**: Модель Yi-34b.

**Атрибуты**:

- `name` (str): "yi-34b".
- `base_provider` (str): "01-ai".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `dolphin_2_6`

**Описание**: Модель Dolphin 2.6.

**Атрибуты**:

- `name` (str): "dolphin-2.6".
- `base_provider` (str): "Cognitive Computations".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `dolphin_2_9`

**Описание**: Модель Dolphin 2.9.

**Атрибуты**:

- `name` (str): "dolphin-2.9".
- `base_provider` (str): "Cognitive Computations".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `airoboros_70b`

**Описание**: Модель Airoboros-70b.

**Атрибуты**:

- `name` (str): "airoboros-70b".
- `base_provider` (str): "DeepInfra".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `lzlv_70b`

**Описание**: Модель Lzlv-70b.

**Атрибуты**:

- `name` (str): "lzlv-70b".
- `base_provider` (str): "Lizpreciatior".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `minicpm_2_5`

**Описание**: Модель Minicpm-2.5.

**Атрибуты**:

- `name` (str): "minicpm-2.5".
- `base_provider` (str): "OpenBMB".
- `best_provider` (ProviderType): `DeepInfraChat`.

### `tulu_3_405b`

**Описание**: Модель Tulu-3-405b.

**Атрибуты**:

- `name` (str): "tulu-3-405b".
- `base_provider` (str): "Ai2".
- `best_provider` (ProviderType): `AllenAI`.

### `olmo_2_13b`

**Описание**: Модель Olmo-2-13b.

**Атрибуты**:

- `name` (str): "olmo-2-13b".
- `base_provider` (str): "Ai2".
- `best_provider` (ProviderType): `AllenAI`.

### `tulu_3_1_8b`

**Описание**: