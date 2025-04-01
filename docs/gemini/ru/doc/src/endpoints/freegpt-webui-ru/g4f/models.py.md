# Модуль для определения моделей G4F

## Обзор

Модуль `models.py` содержит классы, определяющие различные модели, используемые в проекте G4F (Generative Models for Free). Он включает в себя атрибуты, такие как имя модели, базовый провайдер и лучший провайдер для каждой модели. Также содержит утилиты для преобразования строковых идентификаторов моделей в соответствующие классы моделей.

## Подробнее

Этот модуль предоставляет удобный способ определения и управления различными моделями, которые могут использоваться в G4F. Он позволяет легко настраивать и выбирать наилучшего провайдера для каждой модели.

## Классы

### `Model`

Описание: Класс, содержащий вложенные классы для каждой модели, определяющие их характеристики.

**Принцип работы**:
Класс `Model` служит контейнером для различных моделей, каждая из которых представлена в виде вложенного класса. Каждый вложенный класс содержит атрибуты, такие как имя модели (`name`), базовый провайдер (`base_provider`) и лучший провайдер (`best_provider`). Это позволяет централизованно управлять и определять различные модели, используемые в проекте.

#### `model`

Описание: Базовый класс для определения атрибутов модели.

##### Атрибуты:
- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер модели.
- `best_provider` (str): Лучший провайдер модели.

#### `gpt_35_turbo`

Описание: Класс, определяющий модель GPT-3.5 Turbo.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-3.5-turbo`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Mishalsgpt`).

#### `gpt_35_turbo_0613`

Описание: Класс, определяющий модель GPT-3.5 Turbo 0613.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-3.5-turbo-0613`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Gravityengine`).

#### `gpt_35_turbo_16k_0613`

Описание: Класс, определяющий модель GPT-3.5 Turbo 16k 0613.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-3.5-turbo-16k-0613`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Mishalsgpt`).

#### `gpt_35_turbo_16k`

Описание: Класс, определяющий модель GPT-3.5 Turbo 16k.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-3.5-turbo-16k`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Gravityengine`).

#### `gpt_4_dev`

Описание: Класс, определяющий модель GPT-4 для разработчиков.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-4-for-dev`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Phind`).

#### `gpt_4`

Описание: Класс, определяющий модель GPT-4.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-4`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.ChatgptAi`).
- `best_providers` (list): Список лучших провайдеров (`[Provider.Bing, Provider.Lockchat]`).

#### `claude_instant_v1_100k`

Описание: Класс, определяющий модель Claude Instant v1 100k.

##### Атрибуты:
- `name` (str): Имя модели (`claude-instant-v1-100k`).
- `base_provider` (str): Базовый провайдер (`anthropic`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `claude_instant_v1`

Описание: Класс, определяющий модель Claude Instant v1.

##### Атрибуты:
- `name` (str): Имя модели (`claude-instant-v1`).
- `base_provider` (str): Базовый провайдер (`anthropic`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `claude_v1_100k`

Описание: Класс, определяющий модель Claude v1 100k.

##### Атрибуты:
- `name` (str): Имя модели (`claude-v1-100k`).
- `base_provider` (str): Базовый провайдер (`anthropic`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `claude_v1`

Описание: Класс, определяющий модель Claude v1.

##### Атрибуты:
- `name` (str): Имя модели (`claude-v1`).
- `base_provider` (str): Базовый провайдер (`anthropic`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `alpaca_7b`

Описание: Класс, определяющий модель Alpaca 7b.

##### Атрибуты:
- `name` (str): Имя модели (`alpaca-7b`).
- `base_provider` (str): Базовый провайдер (`replicate`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `stablelm_tuned_alpha_7b`

Описание: Класс, определяющий модель StableLM Tuned Alpha 7b.

##### Атрибуты:
- `name` (str): Имя модели (`stablelm-tuned-alpha-7b`).
- `base_provider` (str): Базовый провайдер (`replicate`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `bloom`

Описание: Класс, определяющий модель Bloom.

##### Атрибуты:
- `name` (str): Имя модели (`bloom`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `bloomz`

Описание: Класс, определяющий модель Bloomz.

##### Атрибуты:
- `name` (str): Имя модели (`bloomz`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `flan_t5_xxl`

Описание: Класс, определяющий модель FLAN T5 XXL.

##### Атрибуты:
- `name` (str): Имя модели (`flan-t5-xxl`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `flan_ul2`

Описание: Класс, определяющий модель FLAN UL2.

##### Атрибуты:
- `name` (str): Имя модели (`flan-ul2`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `gpt_neox_20b`

Описание: Класс, определяющий модель GPT-NeoX 20B.

##### Атрибуты:
- `name` (str): Имя модели (`gpt-neox-20b`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `oasst_sft_4_pythia_12b_epoch_35`

Описание: Класс, определяющий модель oasst-sft-4-pythia-12b-epoch-3.5.

##### Атрибуты:
- `name` (str): Имя модели (`oasst-sft-4-pythia-12b-epoch-3.5`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `santacoder`

Описание: Класс, определяющий модель Santacoder.

##### Атрибуты:
- `name` (str): Имя модели (`santacoder`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `command_medium_nightly`

Описание: Класс, определяющий модель Command Medium Nightly.

##### Атрибуты:
- `name` (str): Имя модели (`command-medium-nightly`).
- `base_provider` (str): Базовый провайдер (`cohere`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `command_xlarge_nightly`

Описание: Класс, определяющий модель Command XLarge Nightly.

##### Атрибуты:
- `name` (str): Имя модели (`command-xlarge-nightly`).
- `base_provider` (str): Базовый провайдер (`cohere`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `code_cushman_001`

Описание: Класс, определяющий модель Code Cushman 001.

##### Атрибуты:
- `name` (str): Имя модели (`code-cushman-001`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `code_davinci_002`

Описание: Класс, определяющий модель Code Davinci 002.

##### Атрибуты:
- `name` (str): Имя модели (`code-davinci-002`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `text_ada_001`

Описание: Класс, определяющий модель Text Ada 001.

##### Атрибуты:
- `name` (str): Имя модели (`text-ada-001`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `text_babbage_001`

Описание: Класс, определяющий модель Text Babbage 001.

##### Атрибуты:
- `name` (str): Имя модели (`text-babbage-001`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `text_curie_001`

Описание: Класс, определяющий модель Text Curie 001.

##### Атрибуты:
- `name` (str): Имя модели (`text-curie-001`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `text_davinci_002`

Описание: Класс, определяющий модель Text Davinci 002.

##### Атрибуты:
- `name` (str): Имя модели (`text-davinci-002`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `text_davinci_003`

Описание: Класс, определяющий модель Text Davinci 003.

##### Атрибуты:
- `name` (str): Имя модели (`text-davinci-003`).
- `base_provider` (str): Базовый провайдер (`openai`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Vercel`).

#### `palm`

Описание: Класс, определяющий модель PaLM.

##### Атрибуты:
- `name` (str): Имя модели (`palm2`).
- `base_provider` (str): Базовый провайдер (`google`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.Bard`).

#### `falcon_40b`

Описание: Класс, определяющий модель Falcon 40b.

##### Атрибуты:
- `name` (str): Имя модели (`falcon-40b`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.H2o`).

#### `falcon_7b`

Описание: Класс, определяющий модель Falcon 7b.

##### Атрибуты:
- `name` (str): Имя модели (`falcon-7b`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.H2o`).

#### `llama_13b`

Описание: Класс, определяющий модель Llama 13b.

##### Атрибуты:
- `name` (str): Имя модели (`llama-13b`).
- `base_provider` (str): Базовый провайдер (`huggingface`).
- `best_provider` (`Provider.Provider`): Лучший провайдер (`Provider.H2o`).

### `ModelUtils`

Описание: Класс, предоставляющий утилиты для работы с моделями.

**Принцип работы**:
Класс `ModelUtils` содержит словарь `convert`, который используется для преобразования строковых идентификаторов моделей в соответствующие классы моделей, определенные в классе `Model`. Это позволяет легко получать доступ к конкретным моделям по их строковым именам.

#### Атрибуты:

- `convert` (dict): Словарь, сопоставляющий строковые идентификаторы моделей с соответствующими классами моделей.

## Функции

### `ModelUtils.convert`

**Назначение**: Преобразование строкового идентификатора модели в соответствующий класс модели.

**Параметры**:
- Отсутствуют, это атрибут класса.

**Возвращает**:
- `dict`: Словарь, сопоставляющий строковые идентификаторы моделей с соответствующими классами моделей.

**Как работает функция**:

1.  Словарь `convert` содержит пары ключ-значение, где ключ - это строковый идентификатор модели, а значение - соответствующий класс модели из класса `Model`.
2.  При обращении к словарю по ключу (имени модели) возвращается соответствующий класс модели.

**Примеры**:

```python
model_class = ModelUtils.convert['gpt-3.5-turbo']
print(model_class.name)  # Вывод: gpt-3.5-turbo

model_class = ModelUtils.convert['falcon-7b']
print(model_class.base_provider)  # Вывод: huggingface