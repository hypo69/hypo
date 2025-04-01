# Модуль `models.py`

## Обзор

Модуль `models.py` предназначен для определения классов, представляющих различные модели искусственного интеллекта (ИИ) и утилиты для работы с ними. Он содержит определения моделей, такие как GPT-3.5 Turbo, GPT-4, Claude и другие, а также информацию о базовых провайдерах и лучших провайдерах для каждой модели. Этот модуль обеспечивает централизованное место для хранения и управления информацией о моделях, используемых в проекте `hypotez`.

## Подробней

Этот модуль используется для определения доступных моделей ИИ, их базовых провайдеров и рекомендуемых провайдеров для оптимальной работы. Он также предоставляет утилиты для преобразования строковых идентификаторов моделей в соответствующие классы моделей. Это позволяет легко настраивать и переключаться между различными моделями в проекте.

## Классы

### `Model`

**Описание**: Класс `Model` содержит вложенные классы, каждый из которых представляет конкретную модель ИИ. Каждый вложенный класс содержит атрибуты `name` (имя модели), `base_provider` (базовый провайдер) и `best_provider` (лучший провайдер).

**Принцип работы**:
Класс `Model` служит контейнером для хранения информации о различных моделях ИИ. Каждый вложенный класс представляет собой конкретную модель и содержит информацию о ее имени, базовом провайдере и лучшем провайдере. Это позволяет централизованно управлять информацией о моделях и легко получать доступ к нужным данным.

**Методы**:
- Нет методов, так как это класс-контейнер.

**Параметры**:
- Нет параметров, так как это класс-контейнер.

**Примеры**:

```python
# Пример доступа к информации о модели GPT-3.5 Turbo
model_info = Model.gpt_35_turbo
print(model_info.name)  # Вывод: gpt-3.5-turbo
print(model_info.base_provider)  # Вывод: openai
print(model_info.best_provider)  # Вывод: g4f.Provider.Mishalsgpt
```

### `Model.model`

**Описание**: Вложенный класс, служащий базовым представлением модели.

**Принцип работы**:
Определяет структуру данных для каждой конкретной модели ИИ, включая имя, базового провайдера и лучшего провайдера.

**Атрибуты**:
- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер модели.
- `best_provider` (str): Лучший провайдер модели.

### `Model.gpt_35_turbo`

**Описание**: Класс, представляющий модель GPT-3.5 Turbo.

**Принцип работы**:
Хранит информацию о модели GPT-3.5 Turbo, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Mishalsgpt).

**Атрибуты**:
- `name` (str): Имя модели (gpt-3.5-turbo).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Mishalsgpt).

### `Model.gpt_35_turbo_0613`

**Описание**: Класс, представляющий модель GPT-3.5 Turbo 0613.

**Принцип работы**:
Хранит информацию о модели GPT-3.5 Turbo 0613, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Gravityengine).

**Атрибуты**:
- `name` (str): Имя модели (gpt-3.5-turbo-0613).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Gravityengine).

### `Model.gpt_35_turbo_16k_0613`

**Описание**: Класс, представляющий модель GPT-3.5 Turbo 16k 0613.

**Принцип работы**:
Хранит информацию о модели GPT-3.5 Turbo 16k 0613, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Mishalsgpt).

**Атрибуты**:
- `name` (str): Имя модели (gpt-3.5-turbo-16k-0613).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Mishalsgpt).

### `Model.gpt_35_turbo_16k`

**Описание**: Класс, представляющий модель GPT-3.5 Turbo 16k.

**Принцип работы**:
Хранит информацию о модели GPT-3.5 Turbo 16k, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Gravityengine).

**Атрибуты**:
- `name` (str): Имя модели (gpt-3.5-turbo-16k).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Gravityengine).

### `Model.gpt_4_dev`

**Описание**: Класс, представляющий модель GPT-4 for Dev.

**Принцип работы**:
Хранит информацию о модели GPT-4 for Dev, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Phind).

**Атрибуты**:
- `name` (str): Имя модели (gpt-4-for-dev).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Phind).

### `Model.gpt_4`

**Описание**: Класс, представляющий модель GPT-4.

**Принцип работы**:
Хранит информацию о модели GPT-4, включая имя, базового провайдера (OpenAI) и лучшего провайдера (ChatgptAi), а также список лучших провайдеров.

**Атрибуты**:
- `name` (str): Имя модели (gpt-4).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.ChatgptAi).
- `best_providers` (list): Список лучших провайдеров (Provider.Bing, Provider.Lockchat).

### `Model.claude_instant_v1_100k`

**Описание**: Класс, представляющий модель Claude Instant v1 100k.

**Принцип работы**:
Хранит информацию о модели Claude Instant v1 100k, включая имя, базового провайдера (Anthropic) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (claude-instant-v1-100k).
- `base_provider` (str): Базовый провайдер (anthropic).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_instant_v1`

**Описание**: Класс, представляющий модель Claude Instant v1.

**Принцип работы**:
Хранит информацию о модели Claude Instant v1, включая имя, базового провайдера (Anthropic) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (claude-instant-v1).
- `base_provider` (str): Базовый провайдер (anthropic).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_v1_100k`

**Описание**: Класс, представляющий модель Claude v1 100k.

**Принцип работы**:
Хранит информацию о модели Claude v1 100k, включая имя, базового провайдера (Anthropic) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (claude-v1-100k).
- `base_provider` (str): Базовый провайдер (anthropic).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_v1`

**Описание**: Класс, представляющий модель Claude v1.

**Принцип работы**:
Хранит информацию о модели Claude v1, включая имя, базового провайдера (Anthropic) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (claude-v1).
- `base_provider` (str): Базовый провайдер (anthropic).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.alpaca_7b`

**Описание**: Класс, представляющий модель Alpaca 7b.

**Принцип работы**:
Хранит информацию о модели Alpaca 7b, включая имя, базового провайдера (Replicate) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (alpaca-7b).
- `base_provider` (str): Базовый провайдер (replicate).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.stablelm_tuned_alpha_7b`

**Описание**: Класс, представляющий модель StableLM Tuned Alpha 7b.

**Принцип работы**:
Хранит информацию о модели StableLM Tuned Alpha 7b, включая имя, базового провайдера (Replicate) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (stablelm-tuned-alpha-7b).
- `base_provider` (str): Базовый провайдер (replicate).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.bloom`

**Описание**: Класс, представляющий модель Bloom.

**Принцип работы**:
Хранит информацию о модели Bloom, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (bloom).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.bloomz`

**Описание**: Класс, представляющий модель Bloomz.

**Принцип работы**:
Хранит информацию о модели Bloomz, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (bloomz).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.flan_t5_xxl`

**Описание**: Класс, представляющий модель FLAN-T5 XXL.

**Принцип работы**:
Хранит информацию о модели FLAN-T5 XXL, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (flan-t5-xxl).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.flan_ul2`

**Описание**: Класс, представляющий модель FLAN-UL2.

**Принцип работы**:
Хранит информацию о модели FLAN-UL2, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (flan-ul2).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.gpt_neox_20b`

**Описание**: Класс, представляющий модель GPT-NeoX 20B.

**Принцип работы**:
Хранит информацию о модели GPT-NeoX 20B, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (gpt-neox-20b).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.oasst_sft_4_pythia_12b_epoch_35`

**Описание**: Класс, представляющий модель oasst-sft-4-pythia-12b-epoch-3.5.

**Принцип работы**:
Хранит информацию о модели oasst-sft-4-pythia-12b-epoch-3.5, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (oasst-sft-4-pythia-12b-epoch-3.5).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.santacoder`

**Описание**: Класс, представляющий модель SantaCoder.

**Принцип работы**:
Хранит информацию о модели SantaCoder, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (santacoder).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.command_medium_nightly`

**Описание**: Класс, представляющий модель Command Medium Nightly.

**Принцип работы**:
Хранит информацию о модели Command Medium Nightly, включая имя, базового провайдера (Cohere) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (command-medium-nightly).
- `base_provider` (str): Базовый провайдер (cohere).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.command_xlarge_nightly`

**Описание**: Класс, представляющий модель Command XLarge Nightly.

**Принцип работы**:
Хранит информацию о модели Command XLarge Nightly, включая имя, базового провайдера (Cohere) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (command-xlarge-nightly).
- `base_provider` (str): Базовый провайдер (cohere).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.code_cushman_001`

**Описание**: Класс, представляющий модель Code-Cushman-001.

**Принцип работы**:
Хранит информацию о модели Code-Cushman-001, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (code-cushman-001).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.code_davinci_002`

**Описание**: Класс, представляющий модель Code-Davinci-002.

**Принцип работы**:
Хранит информацию о модели Code-Davinci-002, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (code-davinci-002).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_ada_001`

**Описание**: Класс, представляющий модель Text-Ada-001.

**Принцип работы**:
Хранит информацию о модели Text-Ada-001, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (text-ada-001).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_babbage_001`

**Описание**: Класс, представляющий модель Text-Babbage-001.

**Принцип работы**:
Хранит информацию о модели Text-Babbage-001, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (text-babbage-001).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_curie_001`

**Описание**: Класс, представляющий модель Text-Curie-001.

**Принцип работы**:
Хранит информацию о модели Text-Curie-001, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (text-curie-001).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_davinci_002`

**Описание**: Класс, представляющий модель Text-Davinci-002.

**Принцип работы**:
Хранит информацию о модели Text-Davinci-002, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (text-davinci-002).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_davinci_003`

**Описание**: Класс, представляющий модель Text-Davinci-003.

**Принцип работы**:
Хранит информацию о модели Text-Davinci-003, включая имя, базового провайдера (OpenAI) и лучшего провайдера (Vercel).

**Атрибуты**:
- `name` (str): Имя модели (text-davinci-003).
- `base_provider` (str): Базовый провайдер (openai).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.palm`

**Описание**: Класс, представляющий модель PaLM 2.

**Принцип работы**:
Хранит информацию о модели PaLM 2, включая имя, базового провайдера (Google) и лучшего провайдера (Bard).

**Атрибуты**:
- `name` (str): Имя модели (palm2).
- `base_provider` (str): Базовый провайдер (google).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Bard).

### `Model.falcon_40b`

**Описание**: Класс, представляющий модель Falcon 40b.

**Принцип работы**:
Хранит информацию о модели Falcon 40b, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (H2o).

**Атрибуты**:
- `name` (str): Имя модели (falcon-40b).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `Model.falcon_7b`

**Описание**: Класс, представляющий модель Falcon 7b.

**Принцип работы**:
Хранит информацию о модели Falcon 7b, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (H2o).

**Атрибуты**:
- `name` (str): Имя модели (falcon-7b).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `Model.llama_13b`

**Описание**: Класс, представляющий модель LLaMA 13b.

**Принцип работы**:
Хранит информацию о модели LLaMA 13b, включая имя, базового провайдера (Hugging Face) и лучшего провайдера (H2o).

**Атрибуты**:
- `name` (str): Имя модели (llama-13b).
- `base_provider` (str): Базовый провайдер (huggingface).
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `ModelUtils`

**Описание**: Класс `ModelUtils` предоставляет утилиты для работы с моделями, в частности, для преобразования строковых идентификаторов моделей в соответствующие классы моделей.

**Принцип работы**:
Класс `ModelUtils` содержит словарь `convert`, который сопоставляет строковые идентификаторы моделей с соответствующими классами моделей из класса `Model`. Это позволяет легко получать доступ к информации о модели по ее имени.

**Методы**:
- Нет методов, так как это класс-контейнер.

**Атрибуты**:
- `convert` (dict): Словарь, сопоставляющий строковые идентификаторы моделей с соответствующими классами моделей.

**Примеры**:

```python
# Пример получения информации о модели GPT-3.5 Turbo по ее имени
model_info = ModelUtils.convert['gpt-3.5-turbo']
print(model_info.name)  # Вывод: gpt-3.5-turbo
print(model_info.base_provider)  # Вывод: openai
print(model_info.best_provider)  # Вывод: g4f.Provider.Mishalsgpt
```