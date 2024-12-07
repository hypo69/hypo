# Модуль enrichment.py

## Обзор

Этот модуль предоставляет класс `TinyEnricher` для обогащения контента с использованием LLM. Класс использует шаблоны Mustache для создания сообщений и OpenAI API для получения ответов LLM. Результат обогащения может быть кодом, извлеченным из ответа.

## Оглавление

- [Модуль enrichment.py](#модуль-enrichment-py)
- [Обзор](#обзор)
- [Классы](#классы)
    - [TinyEnricher](#tinyenricher)
        - [__init__](#init)
        - [enrich_content](#enrich_content)


## Классы

### `TinyEnricher`

**Описание**: Класс `TinyEnricher` наследуется от `JsonSerializableRegistry` и предназначен для обогащения контента с помощью LLM.

**Методы**:

#### `__init__`

```python
    def __init__(self, use_past_results_in_context=False) -> None:
        """
        Args:
            use_past_results_in_context (bool, optional):  Флаг использования предыдущих результатов в контексте. По умолчанию False.

        """
        self.use_past_results_in_context = use_past_results_in_context
        self.context_cache = []
```

#### `enrich_content`

```python
    def enrich_content(self, requirements: str, content:str, content_type:str =None, context_info:str ="", context_cache:list=None, verbose:bool=False):

        rendering_configs = {"requirements": requirements,\n                             "content": content,\n                             "content_type": content_type, \n                             "context_info": context_info,\n                             "context_cache": context_cache}\n

        messages = utils.compose_initial_LLM_messages_with_templates("enricher.system.mustache", "enricher.user.mustache", rendering_configs)
        next_message = openai_utils.client().send_message(messages, temperature=0.4)
        
        debug_msg = f"Enrichment result message: {next_message}"\n
        logger.debug(debug_msg)
        if verbose:\n
            print(debug_msg)

        if next_message is not None:\n
            result = utils.extract_code_block(next_message["content"])
        else:\n
            result = None
        
        return result
        """
        Args:
            requirements (str): Требования к обогащению.
            content (str): Контент для обогащения.
            content_type (str, optional): Тип контента. По умолчанию None.
            context_info (str, optional): Дополнительная информация о контексте. По умолчанию "".
            context_cache (list, optional): Кэшированные контексты. По умолчанию None.
            verbose (bool, optional): Флаг для подробной информации. По умолчанию False.

        Returns:
            str | None: Извлеченный код из ответа LLM или None, если ответ отсутствует.

        """
```


```
```
```