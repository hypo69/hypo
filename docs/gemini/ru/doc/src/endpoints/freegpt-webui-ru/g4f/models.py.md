# Модуль определения моделей для G4F

## Обзор

Модуль `models.py` содержит определения различных моделей, используемых в проекте `g4f` (Generative Foreign Function). Он предоставляет классы, представляющие разные модели, а также утилиты для работы с этими моделями. Модуль определяет атрибуты каждой модели, такие как имя, базовый провайдер и лучший провайдер. Этот модуль помогает стандартизировать доступ к различным моделям и упрощает их использование в других частях проекта.

## Подробнее

Этот файл определяет структуру данных для различных моделей, используемых в `g4f`. Здесь определены классы, представляющие каждую модель, с указанием их имени, базового провайдера и лучшего провайдера. Это позволяет легко управлять и использовать различные модели в проекте.  Всякий раз, когда необходимо добавить новую модель или изменить существующую, изменения вносятся здесь.  В других частях проекта эти модели можно вызывать по имени, не беспокоясь о деталях реализации.

## Классы

### `Model`

Описание: Класс `Model` содержит вложенные классы, определяющие различные модели и их атрибуты.

Принцип работы: Класс `Model` служит контейнером для определения атрибутов каждой модели, таких как имя (`name`), базовый провайдер (`base_provider`) и лучший провайдер (`best_provider`). Он предоставляет удобный способ организации и доступа к информации о различных моделях, используемых в проекте.

### `Model.model`

Описание: Базовый класс для определения структуры модели.

Атрибуты:
- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер модели.
- `best_provider` (str): Лучший провайдер модели.

### `Model.gpt_35_turbo`

Описание: Класс, представляющий модель `gpt-3.5-turbo`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-3.5-turbo'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Mishalsgpt`.

### `Model.gpt_35_turbo_0613`

Описание: Класс, представляющий модель `gpt-3.5-turbo-0613`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-3.5-turbo-0613'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Gravityengine`.

### `Model.gpt_35_turbo_16k_0613`

Описание: Класс, представляющий модель `gpt-3.5-turbo-16k-0613`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-3.5-turbo-16k-0613'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Mishalsgpt`.

### `Model.gpt_35_turbo_16k`

Описание: Класс, представляющий модель `gpt-3.5-turbo-16k`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-3.5-turbo-16k'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Gravityengine`.

### `Model.gpt_4_dev`

Описание: Класс, представляющий модель `gpt-4-for-dev`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-4-for-dev'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Phind`.

### `Model.gpt_4`

Описание: Класс, представляющий модель `gpt-4`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-4'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.ChatgptAi`.
- `best_providers` (list): Список лучших провайдеров, по умолчанию `[Provider.Bing, Provider.Lockchat]`.

### `Model.claude_instant_v1_100k`

Описание: Класс, представляющий модель `claude-instant-v1-100k`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'claude-instant-v1-100k'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'anthropic'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.claude_instant_v1`

Описание: Класс, представляющий модель `claude-instant-v1`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'claude-instant-v1'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'anthropic'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.claude_v1_100k`

Описание: Класс, представляющий модель `claude-v1-100k`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'claude-v1-100k'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'anthropic'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.claude_v1`

Описание: Класс, представляющий модель `claude-v1`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'claude-v1'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'anthropic'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.alpaca_7b`

Описание: Класс, представляющий модель `alpaca-7b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'alpaca-7b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'replicate'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.stablelm_tuned_alpha_7b`

Описание: Класс, представляющий модель `stablelm-tuned-alpha-7b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'stablelm-tuned-alpha-7b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'replicate'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.bloom`

Описание: Класс, представляющий модель `bloom`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'bloom'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.bloomz`

Описание: Класс, представляющий модель `bloomz`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'bloomz'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.flan_t5_xxl`

Описание: Класс, представляющий модель `flan-t5-xxl`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'flan-t5-xxl'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.flan_ul2`

Описание: Класс, представляющий модель `flan-ul2`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'flan-ul2'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.gpt_neox_20b`

Описание: Класс, представляющий модель `gpt-neox-20b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'gpt-neox-20b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.oasst_sft_4_pythia_12b_epoch_35`

Описание: Класс, представляющий модель `oasst-sft-4-pythia-12b-epoch-3.5`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'oasst-sft-4-pythia-12b-epoch-3.5'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.santacoder`

Описание: Класс, представляющий модель `santacoder`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'santacoder'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.command_medium_nightly`

Описание: Класс, представляющий модель `command-medium-nightly`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'command-medium-nightly'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'cohere'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.command_xlarge_nightly`

Описание: Класс, представляющий модель `command-xlarge-nightly`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'command-xlarge-nightly'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'cohere'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.code_cushman_001`

Описание: Класс, представляющий модель `code-cushman-001`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'code-cushman-001'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.code_davinci_002`

Описание: Класс, представляющий модель `code-davinci-002`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'code-davinci-002'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.text_ada_001`

Описание: Класс, представляющий модель `text-ada-001`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'text-ada-001'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.text_babbage_001`

Описание: Класс, представляющий модель `text-babbage-001`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'text-babbage-001'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.text_curie_001`

Описание: Класс, представляющий модель `text-curie-001`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'text-curie-001'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.text_davinci_002`

Описание: Класс, представляющий модель `text-davinci-002`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'text-davinci-002'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.text_davinci_003`

Описание: Класс, представляющий модель `text-davinci-003`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'text-davinci-003'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'openai'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Vercel`.

### `Model.palm`

Описание: Класс, представляющий модель `palm2`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'palm2'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'google'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.Bard`.

### `Model.falcon_40b`

Описание: Класс, представляющий модель `falcon-40b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'falcon-40b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.H2o`.

### `Model.falcon_7b`

Описание: Класс, представляющий модель `falcon-7b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'falcon-7b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.H2o`.

### `Model.llama_13b`

Описание: Класс, представляющий модель `llama-13b`.

Атрибуты:
- `name` (str): Имя модели, по умолчанию `'llama-13b'`.
- `base_provider` (str): Базовый провайдер модели, по умолчанию `'huggingface'`.
- `best_provider` (Provider.Provider): Лучший провайдер модели, по умолчанию `Provider.H2o`.

### `ModelUtils`

Описание: Класс `ModelUtils` содержит словарь `convert`, который сопоставляет строковые идентификаторы моделей с соответствующими классами моделей.

Принцип работы:  `ModelUtils` предоставляет удобный способ преобразования строковых идентификаторов моделей в соответствующие классы моделей. Это полезно, когда необходимо динамически выбирать модель на основе конфигурации или пользовательского ввода.

Атрибуты:
- `convert` (dict): Словарь, сопоставляющий строковые идентификаторы моделей с соответствующими классами моделей.

```python
class ModelUtils:
    convert: dict = {
        'gpt-3.5-turbo': Model.gpt_35_turbo,
        'gpt-3.5-turbo-0613': Model.gpt_35_turbo_0613,
        'gpt-4': Model.gpt_4,
        'gpt-4-for-dev': Model.gpt_4_dev,
        'gpt-3.5-turbo-16k': Model.gpt_35_turbo_16k,
        'gpt-3.5-turbo-16k-0613': Model.gpt_35_turbo_16k_0613,

        'claude-instant-v1-100k': Model.claude_instant_v1_100k,
        'claude-v1-100k': Model.claude_v1_100k,
        'claude-instant-v1': Model.claude_instant_v1,
        'claude-v1': Model.claude_v1,

        'alpaca-7b': Model.alpaca_7b,
        'stablelm-tuned-alpha-7b': Model.stablelm_tuned_alpha_7b,

        'bloom': Model.bloom,
        'bloomz': Model.bloomz,

        'flan-t5-xxl': Model.flan_t5_xxl,
        'flan-ul2': Model.flan_ul2,

        'gpt-neox-20b': Model.gpt_neox_20b,
        'oasst-sft-4-pythia-12b-epoch-3.5': Model.oasst_sft_4_pythia_12b_epoch_35,
        'santacoder': Model.santacoder,

        'command-medium-nightly': Model.command_medium_nightly,
        'command-xlarge-nightly': Model.command_xlarge_nightly,

        'code-cushman-001': Model.code_cushman_001,
        'code-davinci-002': Model.code_davinci_002,

        'text-ada-001': Model.text_ada_001,
        'text-babbage-001': Model.text_babbage_001,
        'text-curie-001': Model.text_curie_001,
        'text-davinci-002': Model.text_davinci_002,
        'text-davinci-003': Model.text_davinci_003,

        'palm2': Model.palm,
        'palm': Model.palm,
        'google': Model.palm,
        'google-bard': Model.palm,
        'google-palm': Model.palm,
        'bard': Model.palm,

        'falcon-40b': Model.falcon_40b,
        'falcon-7b': Model.falcon_7b,
        'llama-13b': Model.llama_13b,
    }
```

## Примеры

Пример использования класса `ModelUtils` для получения класса модели по её имени:

```python
model_class = ModelUtils.convert['gpt-3.5-turbo']
print(model_class.name)  # Вывод: gpt-3.5-turbo