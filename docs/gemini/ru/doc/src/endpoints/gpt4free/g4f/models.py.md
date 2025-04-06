# Модуль для определения моделей машинного обучения

## Обзор

Модуль `models.py` содержит определения классов `Model`, `ImageModel`, `AudioModel`, `VisionModel`, а также статические определения различных моделей машинного обучения и утилиты для работы с ними. Он предназначен для централизованного хранения информации о моделях, их базовых провайдерах и предпочтительных провайдерах, обеспечивающих оптимальную работу.

## Подробней

Этот модуль играет ключевую роль в проекте `hypotez`, предоставляя унифицированный способ доступа к различным моделям машинного обучения и их конфигурациям. Он позволяет легко расширять список поддерживаемых моделей и управлять провайдерами, используемыми для каждой модели.

## Классы

### `Model`

**Описание**: Базовый класс для представления модели машинного обучения.

**Принцип работы**: Класс содержит информацию об имени модели, базовом провайдере и предпочтительном провайдере.

**Атрибуты**:

-   `name` (str): Имя модели.
-   `base_provider` (str): Базовый провайдер для модели.
-   `best_provider` (ProviderType): Предпочтительный провайдер для модели.

**Методы**:

-   `__all__() -> list[str]`: Возвращает список всех имен моделей.

    ```python
    @staticmethod
    def __all__() -> list[str]:
        """Возвращает список всех имен моделей."""
        return _all_models
    ```

    **Назначение**: Метод класса возвращает список всех доступных моделей, определенных в модуле.

    **Возвращает**:

    -   `list[str]`: Список имен моделей.

    **Как работает метод**:

    1.  Метод возвращает значение глобальной переменной `_all_models`, которая содержит список имен всех моделей.

    **Примеры**:

    ```python
    >>> Model.__all__()
    ['gpt-3.5-turbo', 'gpt-4', ...]
    ```

### `ImageModel(Model)`

**Описание**: Подкласс `Model` для представления моделей, работающих с изображениями.

**Принцип работы**: Наследует все атрибуты и методы от класса `Model`.

### `AudioModel(Model)`

**Описание**: Подкласс `Model` для представления моделей, работающих с аудио.

**Принцип работы**: Наследует все атрибуты и методы от класса `Model`.

### `VisionModel(Model)`

**Описание**: Подкласс `Model` для представления моделей, работающих с видео.

**Принцип работы**: Наследует все атрибуты и методы от класса `Model`.

### `ModelUtils`

**Описание**: Утилитный класс для сопоставления строковых идентификаторов с экземплярами класса `Model`.

**Принцип работы**: Класс содержит словарь `convert`, который связывает имена моделей со значениями.

**Атрибуты**:

-   `convert` (dict[str, Model]): Словарь, сопоставляющий строковые идентификаторы моделей с экземплярами класса `Model`.

## Функции

### `default`

```python
default = Model(
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
```

**Назначение**: Определяет модель по умолчанию, используемую, когда конкретная модель не указана.

**Параметры**:

-   `name` (str): Пустая строка `""`.
-   `base_provider` (str): Пустая строка `""`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список провайдеров по умолчанию.

**Как работает функция**:

1.  Создается экземпляр класса `Model` с именем `""` (пустая строка).
2.  В качестве базового провайдера устанавливается пустая строка `""`.
3.  В качестве лучшего провайдера устанавливается `IterListProvider`, который содержит список провайдеров: `DDG`, `Blackbox`, `Copilot`, `DeepInfraChat`, `AllenAI`, `PollinationsAI`, `TypeGPT`, `OIVSCode`, `ChatGptEs`, `Free2GPT`, `FreeGpt`, `Glider`, `Dynaspark`, `OpenaiChat`, `Jmuz`, `Cloudflare`.

### `default_vision`

```python
default_vision = Model(
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
```

**Назначение**: Определяет модель компьютерного зрения по умолчанию, используемую, когда конкретная модель не указана.

**Параметры**:

-   `name` (str): Пустая строка `""`.
-   `base_provider` (str): Пустая строка `""`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список провайдеров компьютерного зрения по умолчанию.

**Как работает функция**:

1.  Создается экземпляр класса `Model` с именем `""` (пустая строка).
2.  В качестве базового провайдера устанавливается пустая строка `""`.
3.  В качестве лучшего провайдера устанавливается `IterListProvider`, который содержит список провайдеров: `Blackbox`, `OIVSCode`, `TypeGPT`, `DeepInfraChat`, `PollinationsAI`, `Dynaspark`, `HuggingSpace`, `GeminiPro`, `HuggingFaceAPI`, `CopilotAccount`, `OpenaiAccount`, `Gemini`. Параметр `shuffle=False` указывает, что порядок провайдеров в списке должен быть сохранен.

### `gpt_3_5_turbo`

```python
gpt_3_5_turbo = Model(
    name          = 'gpt-3.5-turbo',
    base_provider = 'OpenAI'
)
```

**Назначение**: Определяет модель `gpt-3.5-turbo` от OpenAI.

**Параметры**:

-   `name` (str): `'gpt-3.5-turbo'`.
-   `base_provider` (str): `'OpenAI'`.

### `gpt_4`

```python
gpt_4 = Model(
    name          = 'gpt-4',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Jmuz, ChatGptEs, PollinationsAI, Yqcloud, Goabror, Copilot, OpenaiChat, Liaobots])
)
```

**Назначение**: Определяет модель `gpt-4` от OpenAI.

**Параметры**:

-   `name` (str): `'gpt-4'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gpt_4o`

```python
gpt_4o = VisionModel(
    name          = 'gpt-4o',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, Jmuz, ChatGptEs, PollinationsAI, Liaobots, OpenaiChat])
)
```

**Назначение**: Определяет модель `gpt-4o` от OpenAI, предназначенную для работы с видео.

**Параметры**:

-   `name` (str): `'gpt-4o'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gpt_4o_mini`

```python
gpt_4o_mini = Model(
    name          = 'gpt-4o-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Blackbox, ChatGptEs, TypeGPT, PollinationsAI, OIVSCode, Liaobots, Jmuz, OpenaiChat])
)
```

**Назначение**: Определяет модель `gpt-4o-mini` от OpenAI.

**Параметры**:

-   `name` (str): `'gpt-4o-mini'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gpt_4o_audio`

```python
gpt_4o_audio = AudioModel(
    name          = 'gpt-4o-audio',
    base_provider = 'OpenAI',
    best_provider = PollinationsAI
)
```

**Назначение**: Определяет модель `gpt-4o-audio` от OpenAI, предназначенную для работы с аудио.

**Параметры**:

-   `name` (str): `'gpt-4o-audio'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): `PollinationsAI`.

### `o1`

```python
o1 = Model(
    name          = 'o1',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([Blackbox, Copilot, OpenaiAccount])
)
```

**Назначение**: Определяет модель `o1` от OpenAI.

**Параметры**:

-   `name` (str): `'o1'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `o1_mini`

```python
o1_mini = Model(
    name          = 'o1-mini',
    base_provider = 'OpenAI',
    best_provider = OpenaiAccount
)
```

**Назначение**: Определяет модель `o1-mini` от OpenAI.

**Параметры**:

-   `name` (str): `'o1-mini'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): `OpenaiAccount`.

### `o3_mini`

```python
o3_mini = Model(
    name          = 'o3-mini',
    base_provider = 'OpenAI',
    best_provider = IterListProvider([DDG, Blackbox, PollinationsAI, Liaobots])
)
```

**Назначение**: Определяет модель `o3-mini` от OpenAI.

**Параметры**:

-   `name` (str): `'o3-mini'`.
-   `base_provider` (str): `'OpenAI'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gigachat`

```python
gigachat = Model(
    name          = 'GigaChat:latest',
    base_provider = 'gigachat',
    best_provider = GigaChat
)
```

**Назначение**: Определяет модель `GigaChat:latest` от GigaChat.

**Параметры**:

-   `name` (str): `'GigaChat:latest'`.
-   `base_provider` (str): `'gigachat'`.
-   `best_provider` (ProviderType): `GigaChat`.

### `meta`

```python
meta = Model(
    name          = "meta-ai",
    base_provider = "Meta",
    best_provider = MetaAI
)
```

**Назначение**: Определяет модель `meta-ai` от Meta.

**Параметры**:

-   `name` (str): `"meta-ai"`.
-   `base_provider` (str): `"Meta"`.
-   `best_provider` (ProviderType): `MetaAI`.

### `llama_2_7b`

```python
llama_2_7b = Model(
    name          = "llama-2-7b",
    base_provider = "Meta Llama",
    best_provider = Cloudflare
)
```

**Назначение**: Определяет модель `llama-2-7b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-2-7b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): `Cloudflare`.

### `llama_3_8b`

```python
llama_3_8b = Model(
    name          = "llama-3-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Jmuz, Cloudflare])
)
```

**Назначение**: Определяет модель `llama-3-8b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3-8b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_70b`

```python
llama_3_70b = Model(
    name          = "llama-3-70b",
    base_provider = "Meta Llama",
    best_provider = Jmuz
)
```

**Назначение**: Определяет модель `llama-3-70b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3-70b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): `Jmuz`.

### `llama_3_1_8b`

```python
llama_3_1_8b = Model(
    name          = "llama-3.1-8b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, Glider, PollinationsAI, AllenAI, Jmuz, Cloudflare])
)
```

**Назначение**: Определяет модель `llama-3.1-8b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.1-8b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_1_70b`

```python
llama_3_1_70b = Model(
    name          = "llama-3.1-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Glider, AllenAI, Jmuz])
)
```

**Назначение**: Определяет модель `llama-3.1-70b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.1-70b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_1_405b`

```python
llama_3_1_405b = Model(
    name          = "llama-3.1-405b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([AllenAI, Jmuz])
)
```

**Назначение**: Определяет модель `llama-3.1-405b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.1-405b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_2_1b`

```python
llama_3_2_1b = Model(
    name          = "llama-3.2-1b",
    base_provider = "Meta Llama",
    best_provider = Cloudflare
)
```

**Назначение**: Определяет модель `llama-3.2-1b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.2-1b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): `Cloudflare`.

### `llama_3_2_3b`

```python
llama_3_2_3b = Model(
    name          = "llama-3.2-3b",
    base_provider = "Meta Llama",
    best_provider = Glider
)
```

**Назначение**: Определяет модель `llama-3.2-3b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.2-3b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): `Glider`.

### `llama_3_2_11b`

```python
llama_3_2_11b = VisionModel(
    name          = "llama-3.2-11b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([Jmuz, HuggingChat, HuggingFace])
)
```

**Назначение**: Определяет модель `llama-3.2-11b` от Meta Llama, предназначенную для работы с видео.

**Параметры**:

-   `name` (str): `"llama-3.2-11b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_2_90b`

```python
llama_3_2_90b = Model(
    name          = "llama-3.2-90b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DeepInfraChat, Jmuz])
)
```

**Назначение**: Определяет модель `llama-3.2-90b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.2-90b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `llama_3_3_70b`

```python
llama_3_3_70b = Model(
    name          = "llama-3.3-70b",
    base_provider = "Meta Llama",
    best_provider = IterListProvider([DDG, DeepInfraChat, LambdaChat, PollinationsAI, Jmuz, HuggingChat, HuggingFace])
)
```

**Назначение**: Определяет модель `llama-3.3-70b` от Meta Llama.

**Параметры**:

-   `name` (str): `"llama-3.3-70b"`.
-   `base_provider` (str): `"Meta Llama"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `mixtral_8x7b`

```python
mixtral_8x7b = Model(
    name          = "mixtral-8x7b",
    base_provider = "Mistral",
    best_provider = Jmuz
)
```

**Назначение**: Определяет модель `mixtral-8x7b` от Mistral.

**Параметры**:

-   `name` (str): `"mixtral-8x7b"`.
-   `base_provider` (str): `"Mistral"`.
-   `best_provider` (ProviderType): `Jmuz`.

### `mixtral_8x22b`

```python
mixtral_8x22b = Model(
    name          = "mixtral-8x22b",
    base_provider = "Mistral",
    best_provider = DeepInfraChat
)
```

**Назначение**: Определяет модель `mixtral-8x22b` от Mistral.

**Параметры**:

-   `name` (str): `"mixtral-8x22b"`.
-   `base_provider` (str): `"Mistral"`.
-   `best_provider` (ProviderType): `DeepInfraChat`.

### `mistral_nemo`

```python
mistral_nemo = Model(
    name          = "mistral-nemo",
    base_provider = "Mistral",
    best_provider = IterListProvider([PollinationsAI, HuggingChat, HuggingFace])
)
```

**Назначение**: Определяет модель `mistral-nemo` от Mistral.

**Параметры**:

-   `name` (str): `"mistral-nemo"`.
-   `base_provider` (str): `"Mistral"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `mixtral_small_24b`

```python
mixtral_small_24b = Model(
    name          = "mixtral-small-24b",
    base_provider = "Mistral",
    best_provider = IterListProvider([DDG, DeepInfraChat])
)
```

**Назначение**: Определяет модель `mixtral-small-24b` от Mistral.

**Параметры**:

-   `name` (str): `"mixtral-small-24b"`.
-   `base_provider` (str): `"Mistral"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `hermes_3`

```python
hermes_3 = Model(
    name          = "hermes-3",
    base_provider = "NousResearch",
    best_provider = LambdaChat
)
```

**Назначение**: Определяет модель `hermes-3` от NousResearch.

**Параметры**:

-   `name` (str): `"hermes-3"`.
-   `base_provider` (str): `"NousResearch"`.
-   `best_provider` (ProviderType): `LambdaChat`.

### `phi_3_5_mini`

```python
phi_3_5_mini = Model(
    name          = "phi-3.5-mini",
    base_provider = "Microsoft",
    best_provider = HuggingChat
)
```

**Назначение**: Определяет модель `phi-3.5-mini` от Microsoft.

**Параметры**:

-   `name` (str): `"phi-3.5-mini"`.
-   `base_provider` (str): `"Microsoft"`.
-   `best_provider` (ProviderType): `HuggingChat`.

### `phi_4`

```python
phi_4 = Model(
    name          = "phi-4",
    base_provider = "Microsoft",
    best_provider = IterListProvider([DeepInfraChat, PollinationsAI, HuggingSpace])
)
```

**Назначение**: Определяет модель `phi-4` от Microsoft.

**Параметры**:

-   `name` (str): `"phi-4"`.
-   `base_provider` (str): `"Microsoft"`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `wizardlm_2_7b`

```python
wizardlm_2_7b = Model(
    name = \'wizardlm-2-7b\',
    base_provider = \'Microsoft\',
    best_provider = DeepInfraChat
)
```

**Назначение**: Определяет модель `wizardlm-2-7b` от Microsoft.

**Параметры**:

-   `name` (str): `'wizardlm-2-7b'`.
-   `base_provider` (str): `'Microsoft'`.
-   `best_provider` (ProviderType): `DeepInfraChat`.

### `wizardlm_2_8x22b`

```python
wizardlm_2_8x22b = Model(
    name = \'wizardlm-2-8x22b\',
    base_provider = \'Microsoft\',
    best_provider = IterListProvider([DeepInfraChat, Jmuz])
)
```

**Назначение**: Определяет модель `wizardlm-2-8x22b` от Microsoft.

**Параметры**:

-   `name` (str): `'wizardlm-2-8x22b'`.
-   `base_provider` (str): `'Microsoft'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gemini`

```python
gemini = Model(
    name          = \'gemini-2.0\',
    base_provider = \'Google\',
    best_provider = Gemini
)
```

**Назначение**: Определяет модель `gemini-2.0` от Google.

**Параметры**:

-   `name` (str): `'gemini-2.0'`.
-   `base_provider` (str): `'Google'`.
-   `best_provider` (ProviderType): `Gemini`.

### `gemini_exp`

```python
gemini_exp = Model(
    name          = \'gemini-exp\',
    base_provider = \'Google\',
    best_provider = Jmuz
)
```

**Назначение**: Определяет модель `gemini-exp` от Google.

**Параметры**:

-   `name` (str): `'gemini-exp'`.
-   `base_provider` (str): `'Google'`.
-   `best_provider` (ProviderType): `Jmuz`.

### `gemini_1_5_flash`

```python
gemini_1_5_flash = Model(
    name          = \'gemini-1.5-flash\',
    base_provider = \'Google DeepMind\',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, Dynaspark, Jmuz, GeminiPro])
)
```

**Назначение**: Определяет модель `gemini-1.5-flash` от Google DeepMind.

**Параметры**:

-   `name` (str): `'gemini-1.5-flash'`.
-   `base_provider` (str): `'Google DeepMind'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gemini_1_5_pro`

```python
gemini_1_5_pro = Model(
    name          = \'gemini-1.5-pro\',
    base_provider = \'Google DeepMind\',
    best_provider = IterListProvider([Free2GPT, FreeGpt, TeachAnything, Websim, Jmuz, GeminiPro])
)
```

**Назначение**: Определяет модель `gemini-1.5-pro` от Google DeepMind.

**Параметры**:

-   `name` (str): `'gemini-1.5-pro'`.
-   `base_provider` (str): `'Google DeepMind'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gemini_2_0_flash`

```python
gemini_2_0_flash = Model(
    name          = \'gemini-2.0-flash\',
    base_provider = \'Google DeepMind\',
    best_provider = IterListProvider([Dynaspark, GeminiPro, Gemini])
)
```

**Назначение**: Определяет модель `gemini-2.0-flash` от Google DeepMind.

**Параметры**:

-   `name` (str): `'gemini-2.0-flash'`.
-   `base_provider` (str): `'Google DeepMind'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `gemini_2_0_flash_thinking`

```python
gemini_2_0_flash_thinking = Model(
    name          = \'gemini-2.0-flash-thinking\',
    base_provider = \'Google DeepMind\',
    best_provider = Gemini
)
```

**Назначение**: Определяет модель `gemini-2.0-flash-thinking` от Google DeepMind.

**Параметры**:

-   `name` (str): `'gemini-2.0-flash-thinking'`.
-   `base_provider` (str): `'Google DeepMind'`.
-   `best_provider` (ProviderType): `Gemini`.

### `gemini_2_0_flash_thinking_with_apps`

```python
gemini_2_0_flash_thinking_with_apps = Model(
    name          = \'gemini-2.0-flash-thinking-with-apps\',
    base_provider = \'Google DeepMind\',
    best_provider = Gemini
)
```

**Назначение**: Определяет модель `gemini-2.0-flash-thinking-with-apps` от Google DeepMind.

**Параметры**:

-   `name` (str): `'gemini-2.0-flash-thinking-with-apps'`.
-   `base_provider` (str): `'Google DeepMind'`.
-   `best_provider` (ProviderType): `Gemini`.

### `claude_3_haiku`

```python
claude_3_haiku = Model(
    name          = \'claude-3-haiku\',
    base_provider = \'Anthropic\',
    best_provider = IterListProvider([DDG, Jmuz])
)
```

**Назначение**: Определяет модель `claude-3-haiku` от Anthropic.

**Параметры**:

-   `name` (str): `'claude-3-haiku'`.
-   `base_provider` (str): `'Anthropic'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `claude_3_5_sonnet`

```python
claude_3_5_sonnet = Model(
    name          = \'claude-3.5-sonnet\',
    base_provider = \'Anthropic\',
    best_provider = IterListProvider([Jmuz, Liaobots])
)
```

**Назначение**: Определяет модель `claude-3.5-sonnet` от Anthropic.

**Параметры**:

-   `name` (str): `'claude-3.5-sonnet'`.
-   `base_provider` (str): `'Anthropic'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `claude_3_7_sonnet`

```python
claude_3_7_sonnet = Model(
    name          = \'claude-3.7-sonnet\',
    base_provider = \'Anthropic\',
    best_provider = IterListProvider([Blackbox, Liaobots])
)
```

**Назначение**: Определяет модель `claude-3.7-sonnet` от Anthropic.

**Параметры**:

-   `name` (str): `'claude-3.7-sonnet'`.
-   `base_provider` (str): `'Anthropic'`.
-   `best_provider` (ProviderType): Экземпляр `IterListProvider`, содержащий список предпочтительных провайдеров.

### `reka_core`

```python
reka_core = Model(
    name = \'reka-core\',
    base_provider = \'Reka AI\',
    best_provider = Reka
)
```

**Назначение**: Определяет модель `reka-core` от Reka AI.

**Параметры**:

-   `name` (str): `'reka-core'`.
-   `base_provider` (str): `'Reka AI'`.
-   `best_provider` (ProviderType): `Reka`.

### `blackboxai`

```python
blackboxai = Model(
    name = \'blackboxai\',
    base_provider = \'Blackbox AI\',
    best_provider = Blackbox
)
```

**Назначение**: Определяет модель `blackboxai` от Blackbox AI.

**Параметры**:

-   `name` (str): `'blackboxai'`.
-   `base_provider` (str): `'Blackbox AI'`.
-   `best_provider` (ProviderType): `Blackbox`.

### `blackboxai_pro`

```python
blackboxai_pro = Model(
    name = \'blackboxai-pro\',
    base_provider = \'Blackbox AI\',
    best_provider = Blackbox
)
```

**Назначение**: Определяет модель `blackboxai-pro` от Blackbox AI.

**Параметры**:

-   `name` (str): `'blackboxai-pro'`.
-   `base_provider` (str):