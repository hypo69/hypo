# Модуль определения моделей для G4F

## Обзор

Этот модуль содержит определения различных моделей, используемых в G4F (Generative Functions for Fun). Он определяет классы для каждой модели, содержащие информацию об имени модели, базовом провайдере и лучшем провайдере для этой модели. Также содержит класс `ModelUtils` для преобразования строкового представления модели в соответствующий класс модели.

## Подробнее

Модуль предназначен для централизованного хранения информации о моделях, используемых в проекте. Это позволяет легко получать доступ к информации о конкретной модели, такой как ее имя и предпочтительный провайдер. Класс `ModelUtils` предоставляет удобный способ преобразования строкового представления модели в соответствующий класс модели, что упрощает использование моделей в коде.

## Классы

### `Model`

Описание: Класс, содержащий вложенные классы, представляющие различные модели. Каждый вложенный класс содержит атрибуты, описывающие модель, такие как имя, базовый провайдер и лучший провайдер.

**Принцип работы**:
Класс `Model` служит контейнером для статических определений моделей. Он не предназначен для создания экземпляров. Вместо этого он предоставляет доступ к информации о моделях через свои вложенные классы.

### `Model.model`

Описание: Базовый класс для моделей.

**Атрибуты**:
- `name` (str): Имя модели.
- `base_provider` (str): Базовый провайдер модели.
- `best_provider` (str): Лучший провайдер модели.

### `Model.gpt_35_turbo`

Описание: Класс, представляющий модель GPT-3.5 Turbo.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-3.5-turbo').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Mishalsgpt).

### `Model.gpt_35_turbo_0613`

Описание: Класс, представляющий модель GPT-3.5 Turbo 0613.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-3.5-turbo-0613').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Gravityengine).

### `Model.gpt_35_turbo_16k_0613`

Описание: Класс, представляющий модель GPT-3.5 Turbo 16k 0613.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-3.5-turbo-16k-0613').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Mishalsgpt).

### `Model.gpt_35_turbo_16k`

Описание: Класс, представляющий модель GPT-3.5 Turbo 16k.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-3.5-turbo-16k').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Gravityengine).

### `Model.gpt_4_dev`

Описание: Класс, представляющий модель GPT-4 для разработчиков.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-4-for-dev').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Phind).

### `Model.gpt_4`

Описание: Класс, представляющий модель GPT-4.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-4').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.ChatgptAi).
- `best_providers` (list): Список лучших провайдеров (Provider.Bing, Provider.Lockchat).

### `Model.claude_instant_v1_100k`

Описание: Класс, представляющий модель Claude Instant v1 100k.

**Атрибуты**:
- `name` (str): Имя модели ('claude-instant-v1-100k').
- `base_provider` (str): Базовый провайдер ('anthropic').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_instant_v1`

Описание: Класс, представляющий модель Claude Instant v1.

**Атрибуты**:
- `name` (str): Имя модели ('claude-instant-v1').
- `base_provider` (str): Базовый провайдер ('anthropic').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_v1_100k`

Описание: Класс, представляющий модель Claude v1 100k.

**Атрибуты**:
- `name` (str): Имя модели ('claude-v1-100k').
- `base_provider` (str): Базовый провайдер ('anthropic').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.claude_v1`

Описание: Класс, представляющий модель Claude v1.

**Атрибуты**:
- `name` (str): Имя модели ('claude-v1').
- `base_provider` (str): Базовый провайдер ('anthropic').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.alpaca_7b`

Описание: Класс, представляющий модель Alpaca 7b.

**Атрибуты**:
- `name` (str): Имя модели ('alpaca-7b').
- `base_provider` (str): Базовый провайдер ('replicate').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.stablelm_tuned_alpha_7b`

Описание: Класс, представляющий модель StableLM Tuned Alpha 7b.

**Атрибуты**:
- `name` (str): Имя модели ('stablelm-tuned-alpha-7b').
- `base_provider` (str): Базовый провайдер ('replicate').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.bloom`

Описание: Класс, представляющий модель Bloom.

**Атрибуты**:
- `name` (str): Имя модели ('bloom').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.bloomz`

Описание: Класс, представляющий модель Bloomz.

**Атрибуты**:
- `name` (str): Имя модели ('bloomz').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.flan_t5_xxl`

Описание: Класс, представляющий модель Flan T5 XXL.

**Атрибуты**:
- `name` (str): Имя модели ('flan-t5-xxl').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.flan_ul2`

Описание: Класс, представляющий модель Flan UL2.

**Атрибуты**:
- `name` (str): Имя модели ('flan-ul2').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.gpt_neox_20b`

Описание: Класс, представляющий модель GPT-NeoX 20B.

**Атрибуты**:
- `name` (str): Имя модели ('gpt-neox-20b').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.oasst_sft_4_pythia_12b_epoch_35`

Описание: Класс, представляющий модель oasst-sft-4-pythia-12b-epoch-3.5.

**Атрибуты**:
- `name` (str): Имя модели ('oasst-sft-4-pythia-12b-epoch-3.5').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.santacoder`

Описание: Класс, представляющий модель SantaCoder.

**Атрибуты**:
- `name` (str): Имя модели ('santacoder').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.command_medium_nightly`

Описание: Класс, представляющий модель Command Medium Nightly.

**Атрибуты**:
- `name` (str): Имя модели ('command-medium-nightly').
- `base_provider` (str): Базовый провайдер ('cohere').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.command_xlarge_nightly`

Описание: Класс, представляющий модель Command XLarge Nightly.

**Атрибуты**:
- `name` (str): Имя модели ('command-xlarge-nightly').
- `base_provider` (str): Базовый провайдер ('cohere').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.code_cushman_001`

Описание: Класс, представляющий модель Code Cushman 001.

**Атрибуты**:
- `name` (str): Имя модели ('code-cushman-001').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.code_davinci_002`

Описание: Класс, представляющий модель Code Davinci 002.

**Атрибуты**:
- `name` (str): Имя модели ('code-davinci-002').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_ada_001`

Описание: Класс, представляющий модель Text Ada 001.

**Атрибуты**:
- `name` (str): Имя модели ('text-ada-001').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_babbage_001`

Описание: Класс, представляющий модель Text Babbage 001.

**Атрибуты**:
- `name` (str): Имя модели ('text-babbage-001').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_curie_001`

Описание: Класс, представляющий модель Text Curie 001.

**Атрибуты**:
- `name` (str): Имя модели ('text-curie-001').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_davinci_002`

Описание: Класс, представляющий модель Text Davinci 002.

**Атрибуты**:
- `name` (str): Имя модели ('text-davinci-002').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.text_davinci_003`

Описание: Класс, представляющий модель Text Davinci 003.

**Атрибуты**:
- `name` (str): Имя модели ('text-davinci-003').
- `base_provider` (str): Базовый провайдер ('openai').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Vercel).

### `Model.palm`

Описание: Класс, представляющий модель PaLM 2.

**Атрибуты**:
- `name` (str): Имя модели ('palm2').
- `base_provider` (str): Базовый провайдер ('google').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.Bard).

### `Model.falcon_40b`

Описание: Класс, представляющий модель Falcon 40b.

**Атрибуты**:
- `name` (str): Имя модели ('falcon-40b').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `Model.falcon_7b`

Описание: Класс, представляющий модель Falcon 7b.

**Атрибуты**:
- `name` (str): Имя модели ('falcon-7b').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `Model.llama_13b`

Описание: Класс, представляющий модель LLaMA 13b.

**Атрибуты**:
- `name` (str): Имя модели ('llama-13b').
- `base_provider` (str): Базовый провайдер ('huggingface').
- `best_provider` (Provider.Provider): Лучший провайдер (Provider.H2o).

### `ModelUtils`

Описание: Класс, предоставляющий утилиты для работы с моделями.

**Принцип работы**:
Класс `ModelUtils` содержит словарь `convert`, который используется для преобразования строкового представления модели в соответствующий класс модели.

**Атрибуты**:
- `convert` (dict): Словарь, отображающий строковое представление модели на соответствующий класс модели.

## Функции

В данном модуле нет отдельных функций, но класс `ModelUtils` содержит словарь `convert`, который можно рассматривать как функцию преобразования.

### `ModelUtils.convert`

**Назначение**: Преобразование строкового представления модели в соответствующий класс модели.

**Как работает функция**:
1. Получает строковое представление модели в качестве ключа.
2. Возвращает соответствующий класс модели из словаря `convert`.

```
Модель (строка) --> Словарь ModelUtils.convert --> Класс модели
```

**Примеры**:

```python
model_class = ModelUtils.convert['gpt-3.5-turbo']
print(model_class.name)  # Вывод: gpt-3.5-turbo
print(model_class.base_provider)  # Вывод: openai
```
```python
model_class = ModelUtils.convert['llama-13b']
print(model_class.name)
print(model_class.best_provider)