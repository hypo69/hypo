# Модель `gemini`

## Обзор

Данный модуль описывает модель `gemini`, предоставляя информацию о ее ключевых элементах, таких как системные и командные инструкции, а также способы их использования.

## Определение класса `__init__`

### `__init__`

**Описание**: Инициализирует объект модели `gemini`.

**Параметры**:
- `api_key` (str): Ключ API для доступа к модели.
- `model_name` (Optional[str], optional): Название модели. По умолчанию `None`.
- `generation_config` (Optional[Dict], optional): Конфигурация генерации. По умолчанию `None`.
- `system_instruction` (Optional[str], optional): Системная инструкция. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
-  None


## Системная инструкция (`system_instruction`)

### Описание

Системная инструкция (`system_instruction`) - это указание, которое передается в модель при ее инициализации и остается неизменным на протяжении всего ее использования.


## Командная инструкция (`command_instruction`)

### Описание

Командная инструкция (`command_instruction`) - это указание, которое передается перед отправкой каждого запроса к модели.  Это дополнение к системной инструкции, и его можно менять для каждого отдельного запроса.  Глобальные инструкции хранятся в каталоге `src/ai/prompts`, а инструкции для отдельных запросов, как правило, располагаются в каталоге `instruction` у клиента (клиенты описываются в `src.endpoints`).  Также глобальные инструкции могут храниться у клиента.

**Примеры имён файлов инструкций:**

- `instruction_doc_writer_html_en.md`
- `instruction_code_checker_en.md`
- `instruction_code_checker_he.md`
- `instruction_code_checker_ru.md`
- `instruction_code_explainer_en.md`
- `instruction_code_explainer_ru.md`


```
```python
    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):
        """
        Args:
            api_key (str): Ключ API для доступа к модели.
            model_name (Optional[str], optional): Название модели. По умолчанию None.
            generation_config (Optional[Dict], optional): Конфигурация генерации. По умолчанию None.
            system_instruction (Optional[str], optional): Системная инструкция. По умолчанию None.
            **kwargs: Дополнительные аргументы.
        
        Returns:
            None
        """
        ...
```