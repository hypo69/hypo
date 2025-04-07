### Анализ кода модуля `models.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код хорошо структурирован и организован, особенно в части определения моделей и их провайдеров.
    - Использование `dataclass` для определения моделей упрощает создание и управление данными.
    - Применение `IterListProvider` позволяет гибко настраивать предпочтительных провайдеров для каждой модели.
- **Минусы**:
    - Отсутствует подробная документация для большинства функций и классов, что затрудняет понимание их назначения и использования.
    - В некоторых местах используется смешанный стиль именования переменных и классов.
    - Не все переменные аннотированы типами, что снижает читаемость и поддерживаемость кода.

**Рекомендации по улучшению:**

1.  **Добавить документацию**:
    *   Для каждого класса, метода и функции необходимо добавить подробное описание, включая аргументы, возвращаемые значения и возможные исключения.

2.  **Улучшить типизацию**:
    *   Добавить аннотации типов для всех переменных, аргументов функций и возвращаемых значений, чтобы повысить надежность и читаемость кода.

3.  **Унифицировать стиль именования**:
    *   Привести имена переменных и классов к единому стилю (например, snake_case для переменных и CamelCase для классов).

4.  **Рефакторинг `ModelUtils`**:
    *   Рассмотреть возможность использования более эффективных структур данных или алгоритмов для `ModelUtils.convert`, чтобы ускорить поиск моделей.

5.  **Добавить логирование**:

    *   Использовать модуль `logger` для записи информации о работе программы, особенно при выборе провайдеров и возникновении ошибок.

6.  **Изменить способ определения \_\_all\_\_**:

    *   Вместо статического определения `_all_models` можно динамически формировать этот список на основе содержимого `ModelUtils.convert`.

**Оптимизированный код:**

```python
"""
Модуль для определения моделей машинного обучения и их провайдеров.
==================================================================

Модуль содержит классы для представления различных моделей машинного обучения,
а также утилиты для работы с ними, такие как выбор оптимального провайдера.

Пример использования:
----------------------

>>> from g4f.models import Model, ModelUtils
>>> model = ModelUtils.convert['gpt-3.5-turbo']
>>> print(model.name)
gpt-3.5-turbo
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict

from .Provider import IterListProvider, ProviderType
from .Provider import (
    ### No Auth Required ###
    AllenAI,
    Blackbox,
    ChatGLM,
    ChatGptEs,
    Cloudflare,
    Copilot,
    DDG,
    DeepInfraChat,
    Dynaspark,
    Free2GPT,
    FreeGpt,
    HuggingSpace,
    G4F,
    Grok,
    DeepseekAI_JanusPro7b,
    Glider,
    Goabror,
    ImageLabs,
    Jmuz,
    LambdaChat,
    Liaobots,
    OIVSCode,
    PerplexityLabs,
    Pi,
    PollinationsAI,
    PollinationsImage,
    TypeGPT,
    TeachAnything,
    Websim,
    Yqcloud,
    
    ### Needs Auth ###
    BingCreateImages,
    CopilotAccount,
    Gemini,
    GeminiPro,
    GigaChat,
    HailuoAI,
    HuggingChat,
    HuggingFace,
    HuggingFaceAPI,
    MetaAI,
    MicrosoftDesigner,
    OpenaiAccount,
    OpenaiChat,
    Reka,
)

from src.logger import logger # Импорт модуля логирования

@dataclass(unsafe_hash=True)
class Model:
    """
    Представляет конфигурацию модели машинного обучения.

    Attributes:
        name (str): Название модели.
        base_provider (str): Провайдер по умолчанию для модели.
        best_provider (ProviderType): Предпочтительный провайдер для модели с логикой повторных попыток.
    """
    name: str
    base_provider: str
    best_provider: ProviderType | None = None

    @staticmethod
    def __all__() -> list[str]:
        """Возвращает список всех названий моделей."""
        return list(ModelUtils.convert.keys())


class ImageModel(Model):
    """
    Представляет модель для работы с изображениями.
    Наследуется от класса Model.
    """
    pass


class AudioModel(Model):
    """
    Представляет модель для работы со звуком.
    Наследуется от класса Model.
    """
    pass


class VisionModel(Model):
    """
    Представляет модель для работы с видео.
    Наследуется от класса Model.
    """
    pass


### Default ###
default: Model = Model(
    name = "",
    base_provider = "",
    best_provider = IterListProvider([
        DDG,
        Blackbox,
        Copilot,
        DeepInfraChat,
        AllenAI,
        PollinationsAI,
        TypeGPT,
        OIVSCode,
        ChatGptEs,
        Free2GPT,
        FreeGpt,
        Glider,
        Dynaspark,
        OpenaiChat,
        Jmuz,
        Cloudflare,
    ])
)

default_vision: Model = Model(
    name = "",
    base_provider = "",
    best_provider = IterListProvider([
        Blackbox,
        OIVSCode,
        TypeGPT,
        DeepInfraChat,
        PollinationsAI,
        Dynaspark,
        HuggingSpace,
        GeminiPro,
        HuggingFaceAPI,
        CopilotAccount,
        OpenaiAccount,
        Gemini,
    ], shuffle=False)
)

##########################
### Text//Audio/Vision ###
##########################

### OpenAI ###
# gpt-3.5
gpt_3_5_turbo: Model = Model(
    name          = 'gpt-3.5-turbo',
    base_provider = 'OpenAI'
)

# gpt-4
gpt_4: Model = Model(
    name          = 'gpt-4',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Jmuz, ChatGptEs, PollinationsAI, Yqcloud, Goabror, Copilot, OpenaiChat, Liaobots])
)

# gpt-4o
gpt_4o: VisionModel = VisionModel(
    name          = 'gpt-4o',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, Jmuz, ChatGptEs, PollinationsAI, Liaobots, OpenaiChat])
)

gpt_4o_mini: Model = Model(
    name          = 'gpt-4o-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Blackbox, ChatGptEs, TypeGPT, PollinationsAI, OIVSCode, Liaobots, Jmuz, OpenaiChat])
)

gpt_4o_audio: AudioModel = AudioModel(
    name          = 'gpt-4o-audio',
    base_provider = 'OpenAI',
    best_provider = PollinationsAI
)

# o1
o1: Model = Model(
    name          = 'o1',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, Copilot, OpenaiAccount])
)

o1_mini: Model = Model(
    name          = 'o1-mini',
    base_provider = 'OpenAI',
    best_provider = OpenaiAccount
)

# o3
o3_mini: Model = Model(
    name          = 'o3-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Blackbox, PollinationsAI, Liaobots])
)

### GigaChat ###
gigachat: Model = Model(
    name          = 'GigaChat:latest',
    base_provider = 'gigachat',
    best_provider = GigaChat
)

### Meta ###
meta: Model = Model(
    name          = "meta-ai",
    base_provider = "Meta",
    best_provider = MetaAI
)

# llama 2
llama_2_7b: Model = Model(
    name          = "llama-2-7b",
    base_provider = "Meta Llama",
    best_provider = Cloudflare
)
# llama 3
llama_3_8b: Model = Model(
    name          = "llama-3-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Jmuz, Cloudflare])
)

llama_3_70b: Model = Model(
    name          = "llama-3-70b",
    base_provider = "Meta Llama",
    best_provider = Jmuz
)

# llama 3.1
llama_3_1_8b: Model = Model(
    name          = "llama-3.1-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, Glider, PollinationsAI, AllenAI, Jmuz, Cloudflare])
)

llama_3_1_70b: Model = Model(
    name          = "llama-3.1-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Glider, AllenAI, Jmuz])
)

llama_3_1_405b: Model = Model(
    name          = "llama-3.1-405b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([AllenAI, Jmuz])
)

# llama 3.2

llama_3_2_1b: Model = Model(
    name          = "llama-3.2-1b",
    base_provider = "Meta Llama",
    best_provider = Cloudflare
)

llama_3_2_3b: Model = Model(
    name          = "llama-3.2-3b",
    base_provider = "Meta Llama",
    best_provider = Glider
)

llama_3_2_11b: VisionModel = VisionModel(
    name          = "llama-3.2-11b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Jmuz, HuggingChat, HuggingFace])
)

llama_3_2_90b: Model = Model(
    name          = "llama-3.2-90b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, Jmuz])
)

# llama 3.3
llama_3_3_70b: Model = Model(
    name          = "llama-3.3-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DDG, DeepInfraChat, LambdaChat, PollinationsAI, Jmuz, HuggingChat, HuggingFace])
)

### Mistral ###
mixtral_8x7b: Model = Model(
    name          = "mixtral-8x7b",
    base_provider = "Mistral",
    best_provider = Jmuz
)
mixtral_8x22b: Model = Model(
    name          = "mixtral-8x22b",
    base_provider = "Mistral",
    best_provider = DeepInfraChat
)

mistral_nemo: Model = Model(
    name          = "mistral-nemo",
    base_provider = "Mistral",
    best_provider = IterListProvider([PollinationsAI, HuggingChat, HuggingFace])
)

mixtral_small_24b: Model = Model(
    name          = "mixtral-small-24b",
    base_provider = "Mistral",
    best_provider = IterListProvider([DDG, DeepInfraChat])
)

### NousResearch ###
hermes_3: Model = Model(
    name          = "hermes-3",
    base_provider = "NousResearch",
    best_provider = LambdaChat
)

### Microsoft ###
# phi
phi_3_5_mini: Model = Model(
    name          = "phi-3.5-mini",
    base_provider = "Microsoft",
    best_provider = HuggingChat
)

phi_4: Model = Model(
    name          = "phi-4",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI, HuggingSpace])
)

# wizardlm
wizardlm_2_7b: Model = Model(
    name = 'wizardlm-2-7b',
    base_provider = 'Microsoft',
    best_provider = DeepInfraChat
)

wizardlm_2_8x22b: Model = Model(
    name = 'wizardlm-2-8x22b',
    base_provider = 'Microsoft',
    best_provider = IterListProvider([DeepInfraChat, Jmuz])
)

### Google DeepMind ###
# gemini
gemini: Model = Model(
    name          = 'gemini-2.0',
    base_provider = 'Google',
    best_provider = Gemini
)

# gemini-exp
gemini_exp: Model = Model(
    name          = 'gemini-exp',
    base_provider = 'Google',
    best_provider = Jmuz
)

# gemini-1.5
gemini_1_5_flash: Model = Model(
    name          = 'gemini-1.5-flash',
    base_provider = 'Google DeepMind',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, Dynaspark, Jmuz, GeminiPro])
)

gemini_1_5_pro: Model = Model(
    name          = 'gemini-1.5-pro',
    base_provider = 'Google DeepMind',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, Jmuz, GeminiPro])
)

# gemini-2.0
gemini_2_0_flash: Model = Model(
    name          = 'gemini-2.0-flash',
    base_provider = 'Google DeepMind',
    best_provider = IterListProvider([Dynaspark, GeminiPro, Gemini])
)

gemini_2_0_flash_thinking: Model = Model(
    name          = 'gemini-2.0-flash-thinking',
    base_provider = 'Google DeepMind',
    best_provider = Gemini
)

gemini_2_0_flash_thinking_with_apps: Model = Model(
    name          = 'gemini-2.0-flash-thinking-with-apps',
    base_provider = 'Google DeepMind',
    best_provider = Gemini
)

### Anthropic ###
# claude 3
claude_3_haiku: Model = Model(
    name          = 'claude-3-haiku',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([DDG, Jmuz])
)

# claude 3.5
claude_3_5_sonnet: Model = Model(
    name          = 'claude-3.5-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Jmuz, Liaobots])
)

# claude 3.7
claude_3_7_sonnet: Model = Model(
    name          = 'claude-3.7-sonnet',
    base_provider = 'Anthropic',
    best_provider = IterListProvider([Blackbox, Liaobots])
)

### Reka AI ###
reka_core: Model = Model(
    name = 'reka-core',
    base_provider = 'Reka AI',
    best_provider = Reka
)

### Blackbox AI ###
blackboxai: Model = Model(
    name = 'blackboxai',
    base_provider = 'Blackbox AI',
    best_provider = Blackbox
)

blackboxai_pro: Model = Model(
    name = 'blackboxai-pro',
    base_provider = 'Blackbox AI',
    best_provider = Blackbox
)

### CohereForAI ###
command_r: Model = Model(
    name = 'command-r',
    base_provider = 'CohereForAI',
    best_provider = HuggingSpace
)

command_r_plus: Model = Model(
    name = 'command-r-plus',
    base_provider = 'CohereForAI',
    best_provider = IterListProvider([HuggingSpace, HuggingChat])
)

command_r7b: Model = Model(
    name = 'command-r7b',
    base_provider = 'CohereForAI',
    best_provider = HuggingSpace
)

command_a: Model = Model(
    name = 'command-a',
    base_provider = 'CohereForAI',
    best_provider = HuggingSpace
)

### Qwen ###
# qwen-1.5
qwen_1_5_7b: Model = Model(
    name = 'qwen-1.5-7b',
    base_provider = 'Qwen',
    best_provider = Cloudflare
)

# qwen-2
qwen_2_72b: Model = Model(
    name = 'qwen-2-72b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([DeepInfraChat, HuggingSpace])
)
qwen_2_vl_7b: VisionModel = VisionModel(
    name = "qwen-2-vl-7b",
    base_provider = 'Qwen',
    best_provider = HuggingFaceAPI
)

# qwen-2.5
qwen_2_5: Model = Model(
    name = 'qwen-2.5',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

qwen_2_5_72b: Model = Model(
    name = 'qwen-2.5-72b',
    base_provider = 'Qwen',
    best_provider = Jmuz
)
qwen_2_5_coder_32b: Model = Model(
    name = 'qwen-2.5-coder-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([PollinationsAI, Jmuz, HuggingChat])
)
qwen_2_5_1m: Model = Model(
    name = 'qwen-2.5-1m',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

qwen_2_5_max: Model = Model(
    name = 'qwen-2-5-max',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

### qwq/qvq ###
qwq_32b: Model = Model(
    name = 'qwq-32b',
    base_provider = 'Qwen',
    best_provider = IterListProvider([Jmuz, HuggingChat])
)
qvq_72b: VisionModel = VisionModel(
    name = 'qvq-72b',
    base_provider = 'Qwen',
    best_provider = HuggingSpace
)

### Inflection ###
pi: Model = Model(
    name = 'pi',
    base_provider = 'Inflection',
    best_provider = Pi
)

### DeepSeek ###
deepseek_chat: Model = Model(
    name = 'deepseek-chat',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, Jmuz])
)

deepseek_v3: Model = Model(
    name = 'deepseek-v3',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, LambdaChat, OIVSCode, TypeGPT, Liaobots])
)

deepseek_r1: Model = Model(
    name = 'deepseek-r1',
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([Blackbox, DeepInfraChat, Glider, LambdaChat, PollinationsAI, TypeGPT, Liaobots, Jmuz, HuggingChat, HuggingFace])
)

janus_pro_7b: VisionModel = VisionModel(
    name = DeepseekAI_JanusPro7b.default_model,
    base_provider = 'DeepSeek',
    best_provider = IterListProvider([DeepseekAI_JanusPro7b, G4F])
)

### x.ai ###
grok_3: Model = Model(
    name = 'grok-3',
    base_provider = 'x.ai',
    best_provider = Grok
)

grok_3_r1: Model = Model(
    name = 'grok-3-r1',
    base_provider = 'x.ai',
    best_provider = Grok
)

### Perplexity AI ###
sonar: Model = Model(
    name = 'sonar',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

sonar_pro: Model = Model(
    name = 'sonar-pro',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

sonar_reasoning: Model = Model(
    name = 'sonar-reasoning',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

sonar_reasoning_pro: Model = Model(
    name = 'sonar-reasoning-pro',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

r1_1776: Model = Model(
    name = 'r1-1776',
    base_provider = 'Perplexity AI',
    best_provider = PerplexityLabs
)

### Nvidia ###
nemotron_70b: Model = Model(
    name = 'nemotron-70b',
    base_provider = 'Nvidia',
    best_provider = IterListProvider([LambdaChat, HuggingChat, HuggingFace])
)

### Databricks ###
dbrx_instruct: Model = Model(
    name = 'dbrx-instruct',
    base_provider = 'Databricks',
    best_provider = DeepInfraChat
)

### THUDM ###
glm_4: Model = Model(
    name = 'glm-4',
    base_provider = 'THUDM',
    best_provider = ChatGLM
)

### MiniMax ###
mini_max: Model = Model(
    name = "MiniMax",
    base_provider = "MiniMax",
    best_provider = HailuoAI
)

### 01-ai ###
yi_34b: Model = Model(
    name = "yi-34b",
    base_provider = "01-ai",
    best_provider = DeepInfraChat
)

### Cognitive Computations ###
dolphin_2_6: Model = Model(
    name = "dolphin-2.6",
    base_provider = "Cognitive Computations",
    best_provider = DeepInfraChat
)

dolphin_2_9: Model = Model(
    name = "dolphin-2.9",
    base_provider = "Cognitive Computations",
    best_provider = DeepInfraChat
)

### DeepInfra ###
airoboros_70b: Model = Model(
    name = "airoboros-70b",
    base_provider = "DeepInfra",
    best_provider = DeepInfraChat
)

### Lizpreciatior ###
lzlv_70b: Model = Model(
    name = "lzlv-70b",
    base_provider = "Lizpreciatior",
    best_provider = DeepInfraChat
)

### OpenBMB ###
minicpm_2_5: Model = Model(
    name = "minicpm-2.5",
    base_provider = "OpenBMB",
    best_provider = DeepInfraChat
)

### Ai2 ###
tulu_3_405b: Model = Model(
    name = "tulu-3-405b",
    base_provider = "Ai2",
    best_provider = AllenAI
)

olmo_2_13b: Model = Model(
    name = "olmo-2-13b",
    base_provider = "Ai2",
    best_provider = AllenAI
)

tulu_3_1_8b: Model = Model(
    name = "tulu-3-1-8b",
    base_provider = "Ai2",
    best_provider = AllenAI
)

tulu_3_70b: Model = Model(
    name = "tulu-3-70b",
    base_provider = "Ai2",
    best_provider = AllenAI
)

olmoe_0125: Model = Model(
    name = "olmoe-0125",
    base_provider = "Ai2",
    best_provider = AllenAI
)

lfm_40b: Model = Model(
    name = "lfm-40b",
    base_provider = "Liquid AI",
    best_provider = LambdaChat
)

### Uncensored AI ###
evil: Model = Model(
    name = 'evil',
    base_provider = 'Evil Mode - Experimental',
    best_provider = IterListProvider([PollinationsAI, TypeGPT])
)


#############
### Image ###
#############

### Stability AI ###
sdxl_turbo: ImageModel = ImageModel(
    name = 'sdxl-turbo',
    base_provider = 'Stability AI',
    best_provider = IterListProvider([PollinationsImage, ImageLabs])
)

sd_3_5: ImageModel = ImageModel(
    name = 'sd-3.5',
    base_provider = 'Stability AI',
    best_provider = HuggingSpace
)

### Black Forest Labs ###
flux: ImageModel = ImageModel(
    name = 'flux',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([Blackbox, PollinationsImage, Websim, HuggingSpace])
)

flux_pro: ImageModel = ImageModel(
    name = 'flux-pro',
    base_provider = 'Black Forest Labs',
    best_provider = PollinationsImage
)

flux_dev: ImageModel = ImageModel(
    name = 'flux-dev',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([PollinationsImage, HuggingSpace, HuggingChat, HuggingFace])
)

flux_schnell: ImageModel = ImageModel(
    name = 'flux-schnell',
    base_provider = 'Black Forest Labs',
    best_provider = IterListProvider([PollinationsImage, HuggingSpace, HuggingChat, HuggingFace])
)


### OpenAI ###
dall_e_3: ImageModel = ImageModel(
    name = 'dall-e-3',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([PollinationsImage, CopilotAccount, OpenaiAccount, MicrosoftDesigner, BingCreateImages])
)

### Midjourney ###
midjourney: ImageModel = ImageModel(
    name = 'midjourney',
    base_provider = 'Midjourney',
    best_provider = PollinationsImage
)

class ModelUtils:
    """
    Утилитарный класс для сопоставления строковых идентификаторов с экземплярами Model.

    Attributes:
        convert (dict[str, Model]): Словарь, отображающий строковые идентификаторы моделей на экземпляры Model.
    """
    convert: Dict[str, Model] = {
        ############
        ### Text ###
        ############

        ### OpenAI ###
        # gpt-3.5
        gpt_3_5_turbo.name: gpt_3_5_turbo,
        
        # gpt-4
        gpt_4.name: gpt_4,
        
        # gpt-4o
        gpt_4o.name: gpt_4o,
        gpt_4o_mini.name: gpt_4o_mini,
        gpt_4o_audio.name: gpt_4o_audio,
        
        # o1
        o1.name: o1,
        o1_mini.name: o1_mini,
        
        # o3
        o3_mini.name: o3_mini,

        ### Meta ###
        meta.name: meta,

        # llama-2
        llama_2_7b.name: llama_2_7b,

        # llama-3
        llama_3_8b.name: llama_3_8b,
        llama_3_70b.name: llama_3_70b,
                
        # llama-3.1
        llama_3_1_8b.name: llama_3_1_8b,
        llama_3_1_70b.name: llama_3_1_70b,
        llama_3_1_405b.name: llama_3_1_405b,

        # llama-3.2
        llama_3_2_1b.name: llama_3_2_1b,
        llama_3_2_3b.name: llama_3_2_3b,
        llama_3_2_11b.name: llama_3_2_11b,
        llama_3_2_90b.name: llama_3_2_90b,
        
        # llama-3.3
        llama_3_3_70b.name: llama_3_3_70b,
                
        ### Mistral ###
        mixtral_8x7b.name: mixtral_8x7b,
        mixtral_8x22b.name: mixtral_8x22b,
        mistral_nemo.name: mistral_nemo,
        mixtral_small_24b.name: mixtral_small_24b,

        ### NousResearch ###
        hermes_3.name: hermes_3,
                
        ### Microsoft ###
        # phi
        phi_3_5_mini.name: phi_3_5_mini,
        phi_4.name: phi_4,
        
        # wizardlm
        wizardlm_2_7b.name: wizardlm_2_7b,
        wizardlm_2_8x22b.name: wizardlm_2_8x22b,

        ### Google ###
        ### Gemini
        "gemini": gemini,
        gemini.name: gemini,
        gemini_exp.name: gemini_exp,
        gemini_1_5_pro.name: gemini_1_5_pro,
        gemini_1_5_flash.name: gemini_1_5_flash,
        gemini_2_0_flash.name: gemini_2_0_flash,
        gemini_2_0_flash_thinking.name: gemini_2_0_flash_thinking,
        gemini_2_0_flash_thinking_with_apps.name: gemini_2_0_flash_thinking_with_apps,

        ### Anthropic ###
        # claude 3
        claude_3_haiku.name: claude_3_haiku,

        # claude 3.5
        claude_3_5_sonnet.name: claude_3_5_sonnet,
        
        # claude 3.7
        claude_3_7_sonnet.name: claude_3_7_sonnet,

        ### Reka AI ###
        reka_core.name: reka_core,

        ### Blackbox AI ###
        blackboxai.name: blackboxai,
        blackboxai_pro.name: blackboxai_pro,

        ### CohereForAI ###
        command_r.name: command_r,
        command_r_plus.name: command_r_plus,
        command_r7b.name: command_r7b,
        command_a.name: command_a,

        ### GigaChat ###
        gigachat.name: gigachat,

        ### Qwen ###
        # qwen-1.5
        qwen_1_5_7b.name: qwen_1_5_7b,
        
        # qwen-2
        qwen_2_72b.name: qwen_2_72b,
        qwen_2_vl_7b.name: qwen_2_vl_7b,
        
        # qwen-2.5
        qwen_2_5.name: qwen_2_5,
        qwen_2_5_72b.name: qwen_2_5_72b,
        qwen_2_5_coder_32b.name: qwen_2_5_coder_32b,
        qwen_2_5_1m.name: qwen_2_5_1m,
        qwen_2_5_max.name: qwen_2_5_max,

        # qwq/qvq
        qwq_32b.name: qwq_32b,
        qvq_72b.name: qvq_72b,

        ### Inflection ###
        pi.name: pi,

        ### x.ai ###
        grok_3.name: grok_3,

        ### Perplexity AI ###
        sonar.name: sonar,
        sonar_pro.name: sonar_pro,
        sonar_reasoning.name: sonar_reasoning,
        sonar_reasoning_pro.name: sonar_reasoning_pro,
        r1_1776.name: r1_1776,
        
        ### Deep