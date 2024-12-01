# Модель `gemini`.
https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
## system_instruction 
Указание (промт, `prompt`), которое передется в модель при инициализации 
и будет верным на все время инстанса.
Не может быть изменено в инстанса 
```python
    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):

                 ...
```

## command_instruction
Указание (промт, `prompt`), которое передается перед отправкой каждого запроса.
обычно, дополнение к системной инструкции. Инструкцию можно менять от запроса к запросу

Глобальные инструкции находятся в src/ai/prompts
Указания к запросам обычно находятся в папке `instruction` у клиента. 
клиенты прописываются в src.endpoints
Также глобальные инструкции также могут храниться на клиенте.

Примеры названий для файлов инструкций:
```
instruction_doc_writer_html_en.md
instruction_code_checker_en.md
instruction_code_checker_he.md
instruction_code_checker_ru.md
instruction_code_explainer_en.md
instruction_code_explainer_ru.md
```

