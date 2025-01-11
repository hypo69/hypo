## Анализ кода модуля `openai_utils`

**Качество кода:**

- **Соответствие требованиям:** 8/10
- **Плюсы:**
    - Код хорошо структурирован, с разделением на классы и функции, что облегчает чтение и поддержку.
    - Имеется поддержка кэширования API-вызовов, что помогает снизить нагрузку на API и ускорить выполнение.
    - Используется `logging` для отслеживания ошибок и отладки.
    - Присутствует обработка различных типов ошибок, связанных с API OpenAI.
    - Реализована поддержка как OpenAI, так и Azure OpenAI API.
- **Минусы:**
    - Не все функции и методы имеют docstring, что затрудняет понимание их назначения.
    - Используется `json` и `pickle` вместо `j_loads`, `j_loads_ns`.
    - Некоторые try-except блоки могут быть заменены на `logger.error` для более краткой обработки ошибок.
    - Не все переменные и имена функций соответствуют ранее обработанным файлам.
    - В коде используется `time.sleep` для ожидания между запросами, что может блокировать поток. Желательно использовать `asyncio.sleep` для асинхронного ожидания.

**Рекомендации по улучшению:**

1.  **Документация:**
    - Добавить docstring к каждой функции, методу и классу с использованием формата RST для Sphinx.
2.  **Импорты:**
    - Импортировать `logger` из `src.logger.logger` вместо `logging`.
    - Использовать `j_loads`, `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
3.  **Обработка ошибок:**
    - Заменить избыточные `try-except` блоки на `logger.error`.
4.  **Рефакторинг:**
     -  Использовать  `asyncio.sleep` для асинхронного ожидания.
    -  Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
5.  **Кэширование:**
    - При необходимости добавить асинхронную реализацию кэширования.

**Оптимизированный код:**

```python
"""
Модуль для взаимодействия с OpenAI и Azure OpenAI API.
======================================================

Этот модуль предоставляет классы для взаимодействия с OpenAI и Azure OpenAI API,
включая поддержку кэширования API-вызовов, обработки ошибок и подсчета токенов.

Модуль включает в себя следующие основные компоненты:

- Класс :class:`LLMCall`: Представляет вызов языковой модели.
- Класс :class:`OpenAIClient`: Клиент для взаимодействия с OpenAI API.
- Класс :class:`AzureClient`: Клиент для взаимодействия с Azure OpenAI API.
- Функции для регистрации и получения клиентов, а также для управления конфигурацией.

Пример использования:
--------------------

.. code-block:: python

    from tinytroupe.openai_utils import client, LLMCall

    # Использование клиента OpenAI по умолчанию
    openai_client = client()

    # Создание и вызов LLM
    llm_call = LLMCall(system_template_name='system_prompt', user_template_name='user_prompt', model='gpt-4')
    response = llm_call.call(rendering_configs={'user_input': 'some_input'})
    print(response)
"""
import os
import time
import asyncio
import tiktoken
from pathlib import Path
from typing import Any
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger
from openai import OpenAI, AzureOpenAI
import pickle
import configparser

# Чтение конфигурационного файла
config = j_loads(Path('config.ini'))

###########################################################################
# Значения параметров по умолчанию
###########################################################################
default = {}
default['model'] = config['OpenAI'].get('MODEL', 'gpt-4')
default['max_tokens'] = int(config['OpenAI'].get('MAX_TOKENS', '1024'))
default['temperature'] = float(config['OpenAI'].get('TEMPERATURE', '0.3'))
default['top_p'] = int(config['OpenAI'].get('TOP_P', '0'))
default['frequency_penalty'] = float(config['OpenAI'].get('FREQ_PENALTY', '0.0'))
default['presence_penalty'] = float(config['OpenAI'].get('PRESENCE_PENALTY', '0.0'))
default['timeout'] = float(config['OpenAI'].get('TIMEOUT', '30.0'))
default['max_attempts'] = float(config['OpenAI'].get('MAX_ATTEMPTS', '0.0'))
default['waiting_time'] = float(config['OpenAI'].get('WAITING_TIME', '0.5'))
default['exponential_backoff_factor'] = float(config['OpenAI'].get('EXPONENTIAL_BACKOFF_FACTOR', '5'))

default['embedding_model'] = config['OpenAI'].get('EMBEDDING_MODEL', 'text-embedding-3-small')

default['cache_api_calls'] = config['OpenAI'].getboolean('CACHE_API_CALLS', False)
default['cache_file_name'] = config['OpenAI'].get('CACHE_FILE_NAME', 'openai_api_cache.pickle')

###########################################################################
# Вспомогательные функции для вызова модели
###########################################################################
# TODO under development
class LLMCall:
    """
    Класс, представляющий вызов LLM-модели.

    Содержит входные сообщения, конфигурацию модели и вывод модели.

    Args:
        system_template_name (str): Имя системного шаблона.
        user_template_name (str, optional): Имя пользовательского шаблона. Defaults to None.
        **model_params: Параметры модели.
    """
    def __init__(self, system_template_name:str, user_template_name:str=None, **model_params):
        """
        Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами.
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    async def call(self, **rendering_configs) -> str | None:
        """
        Вызывает LLM-модель с указанными конфигурациями рендеринга.

        Args:
            **rendering_configs: Конфигурации рендеринга.

        Returns:
            str | None: Содержание ответа модели или None в случае ошибки.
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)
        

        # Код вызывает LLM-модель
        self.model_output = await client().send_message(self.messages, **self.model_params)

        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}")
            return None


    def __repr__(self):
        return f"LLMCall(messages={self.messages}, model_config={self.model_params}, model_output={self.model_output})"


###########################################################################
# Класс клиента
###########################################################################

class OpenAIClient:
    """
    Утилитный класс для взаимодействия с OpenAI API.

    Args:
        cache_api_calls (bool, optional): Определяет, кэшировать ли вызовы API. Defaults to `default['cache_api_calls']`.
        cache_file_name (str, optional): Имя файла для кэширования API-вызовов. Defaults to `default['cache_file_name']`.
    """
    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        logger.debug('Initializing OpenAIClient')

        # Определяет, нужно ли кэшировать вызовы API и повторно использовать их
        self.set_api_cache(cache_api_calls, cache_file_name)
    
    def set_api_cache(self, cache_api_calls, cache_file_name=default['cache_file_name']):
        """
        Включает или отключает кэширование вызовов API.

        Args:
            cache_api_calls (bool): Флаг, определяющий, следует ли кэшировать вызовы API.
            cache_file_name (str, optional): Имя файла для кэширования вызовов API. Defaults to `default['cache_file_name']`.
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = cache_file_name
        if self.cache_api_calls:
            # Загрузка кэша, если он существует
            self.api_cache = self._load_cache()
    
    
    def _setup_from_config(self):
        """
        Настраивает конфигурации OpenAI API для этого клиента.
        """
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    async def send_message(self,
                    current_messages,
                     model=default['model'],
                     temperature=default['temperature'],
                     max_tokens=default['max_tokens'],
                     top_p=default['top_p'],
                     frequency_penalty=default['frequency_penalty'],
                     presence_penalty=default['presence_penalty'],
                     stop=[],
                     timeout=default['timeout'],
                     max_attempts=default['max_attempts'],
                     waiting_time=default['waiting_time'],
                     exponential_backoff_factor=default['exponential_backoff_factor'],
                     n = 1,
                     echo=False) -> dict | None:
        """
        Отправляет сообщение в OpenAI API и возвращает ответ.

        Args:
            current_messages (list): Список словарей, представляющих историю разговора.
            model (str): Идентификатор модели для генерации ответа.
            temperature (float): Контролирует "креативность" ответа. Более высокие значения приводят к более разнообразным ответам.
            max_tokens (int): Максимальное количество токенов (слов или знаков препинания) для генерации в ответе.
            top_p (float): Контролирует "качество" ответа. Более высокие значения приводят к более связным ответам.
            frequency_penalty (float): Контролирует "повторение" ответа. Более высокие значения приводят к меньшему повторению.
            presence_penalty (float): Контролирует "разнообразие" ответа. Более высокие значения приводят к более разнообразным ответам.
            stop (str): Строка, при обнаружении которой в сгенерированном ответе, генерация будет остановлена.
            max_attempts (int): Максимальное количество попыток до прекращения генерации ответа.
            timeout (int): Максимальное количество секунд для ожидания ответа от API.

        Returns:
            dict | None: Словарь, представляющий сгенерированный ответ, или None в случае ошибки.
        """
        async def aux_exponential_backoff():
            nonlocal waiting_time
            logger.info(f'Request failed. Waiting {waiting_time} seconds between requests...')
            await asyncio.sleep(waiting_time)

            # экспоненциальное увеличение времени ожидания
            waiting_time = waiting_time * exponential_backoff_factor
        
        # Настройка конфигураций OpenAI для этого клиента
        self._setup_from_config()
        
        # Код адаптирует параметры к типу API, создавая словарь с ними
        chat_api_params = {
            'messages': current_messages,
            'temperature': temperature,
            'max_tokens':max_tokens,
            'top_p': top_p,
            'frequency_penalty': frequency_penalty,
            'presence_penalty': presence_penalty,
            'stop': stop,
            'timeout': timeout,
            'stream': False,
            'n': n,
        }


        i = 0
        while i < max_attempts:
            i += 1
            try:
                try:
                    logger.debug(f'Sending messages to OpenAI API. Token count={self._count_tokens(current_messages, model)}.')
                except NotImplementedError:
                    logger.debug(f'Token count not implemented for model {model}.')
                    
                start_time = time.monotonic()
                logger.debug(f'Calling model with client class {self.__class__.__name__}.')

                ###############################################################
                # Код вызывает модель, либо из кэша, либо из API
                ###############################################################
                cache_key = str((model, chat_api_params)) # для хэширования нужен string
                if self.cache_api_calls and (cache_key in self.api_cache):
                    response = self.api_cache[cache_key]
                else:
                    logger.info(f'Waiting {waiting_time} seconds before next API request (to avoid throttling)...')
                    await asyncio.sleep(waiting_time)
                    
                    response = await self._raw_model_call(model, chat_api_params)
                    if self.cache_api_calls:
                        self.api_cache[cache_key] = response
                        self._save_cache()
                
                
                logger.debug(f'Got response from API: {response}')
                end_time = time.monotonic()
                logger.debug(
                    f'Got response in {end_time - start_time:.2f} seconds after {i + 1} attempts.')

                return utils.sanitize_dict(self._raw_model_response_extractor(response))

            except InvalidRequestError as e:
                logger.error(f'[{i}] Invalid request error, won\'t retry: {e}')

                # нет смысла повторять попытку, если запрос недействителен
                # поэтому сразу возвращаем None
                return None
            
            except openai.BadRequestError as e:
                logger.error(f'[{i}] Invalid request error, won\'t retry: {e}')
                
                # нет смысла повторять попытку, если запрос недействителен
                # поэтому сразу возвращаем None
                return None
            
            except openai.RateLimitError:
                logger.warning(
                    f'[{i}] Rate limit error, waiting a bit and trying again.')
                await aux_exponential_backoff()
            
            except NonTerminalError as e:
                logger.error(f'[{i}] Non-terminal error: {e}')
                await aux_exponential_backoff()
                
            except Exception as e:
                logger.error(f'[{i}] Error: {e}')

        logger.error(f'Failed to get response after {max_attempts} attempts.')
        return None
    
    async def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает OpenAI API с заданными параметрами.

        Подклассы должны переопределить этот метод для реализации собственных вызовов API.

        Args:
            model (str): Имя модели.
            chat_api_params (dict): Параметры вызова API.

        Returns:
           Any: Ответ от API
        """
        chat_api_params['model'] = model # OpenAI API использует это имя параметра
        return await self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API.

        Подклассы должны переопределить этот метод для реализации собственного извлечения ответа.

        Args:
            response (Any): Ответ от API

        Returns:
            dict: Извлеченный ответ.
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str) -> int | None:
        """
        Подсчитывает количество токенов OpenAI в списке сообщений, используя tiktoken.

        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

        Args:
            messages (list): Список словарей, представляющих историю разговора.
            model (str): Имя модели для кодирования строки.

        Returns:
            int | None: Количество токенов или None в случае ошибки.
        """
        try:
            try:
                encoding = tiktoken.encoding_for_model(model)
            except KeyError:
                logger.debug('Token count: model not found. Using cl100k_base encoding.')
                encoding = tiktoken.get_encoding('cl100k_base')
            if model in {
                'gpt-3.5-turbo-0613',
                'gpt-3.5-turbo-16k-0613',
                'gpt-4-0314',
                'gpt-4-32k-0314',
                'gpt-4-0613',
                'gpt-4-32k-0613',
                }:
                tokens_per_message = 3
                tokens_per_name = 1
            elif model == 'gpt-3.5-turbo-0301':
                tokens_per_message = 4  # каждое сообщение следует за <|start|>{role/name}\n{content}<|end|>\n
                tokens_per_name = -1  # если есть имя, роль опускается
            elif 'gpt-3.5-turbo' in model:
                logger.debug('Token count: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.')
                return self._count_tokens(messages, model='gpt-3.5-turbo-0613')
            elif ('gpt-4' in model) or ('ppo' in model):
                logger.debug('Token count: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.')
                return self._count_tokens(messages, model='gpt-4-0613')
            else:
                raise NotImplementedError(
                    f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
                )
            num_tokens = 0
            for message in messages:
                num_tokens += tokens_per_message
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == 'name':
                        num_tokens += tokens_per_name
            num_tokens += 3  # каждый ответ начинается с <|start|>assistant<|message|>
            return num_tokens
        
        except Exception as e:
            logger.error(f'Error counting tokens: {e}')
            return None

    def _save_cache(self):
        """
        Сохраняет кэш API на диск.

        Используется pickle, потому что некоторые объекты не могут быть сериализованы в JSON.
        """
        # Использовать pickle для сохранения кэша
        pickle.dump(self.api_cache, open(self.cache_file_name, 'wb'))

    
    def _load_cache(self) -> dict:
        """
        Загружает кэш API с диска.
        """
        # Десериализация с помощью pickle
        return pickle.load(open(self.cache_file_name, 'rb')) if os.path.exists(self.cache_file_name) else {}

    async def get_embedding(self, text, model=default['embedding_model']) -> list | None:
        """
        Получает векторное представление заданного текста, используя указанную модель.

        Args:
            text (str): Текст для встраивания.
            model (str): Имя модели для встраивания текста.

        Returns:
           list | None: Векторное представление текста или None в случае ошибки.
        """
        response = await self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)
    
    async def _raw_embedding_model_call(self, text, model):
        """
        Вызывает OpenAI API для получения векторного представления заданного текста.

        Подклассы должны переопределить этот метод для реализации собственных вызовов API.

         Args:
            text (str): Текст для встраивания.
            model (str): Имя модели для встраивания текста.

        Returns:
           Any: Ответ от API
        """
        return await self.client.embeddings.create(
            input=[text],
            model=model
        )
    
    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает векторное представление из ответа API.

        Подклассы должны переопределить этот метод для реализации собственного извлечения ответа.

        Args:
            response (Any): Ответ от API.

        Returns:
            list: Векторное представление текста.
        """
        return response.data[0].embedding

class AzureClient(OpenAIClient):
    """
    Класс для взаимодействия с Azure OpenAI API, наследуемый от OpenAIClient.

    Args:
        cache_api_calls (bool, optional): Определяет, кэшировать ли вызовы API. Defaults to `default['cache_api_calls']`.
        cache_file_name (str, optional): Имя файла для кэширования вызовов API. Defaults to `default['cache_file_name']`.
    """
    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        logger.debug('Initializing AzureClient')

        super().__init__(cache_api_calls, cache_file_name)
    
    def _setup_from_config(self):
        """
        Настраивает конфигурации Azure OpenAI Service API для этого клиента,
        включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint= os.getenv('AZURE_OPENAI_ENDPOINT'),
                                  api_version = config['OpenAI']['AZURE_API_VERSION'],
                                  api_key = os.getenv('AZURE_OPENAI_KEY'))
    
    async def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает Azure OpenAI Service API с заданными параметрами.

        Args:
            model (str): Имя модели.
            chat_api_params (dict): Параметры вызова API.

        Returns:
           Any: Ответ от API
        """
        chat_api_params['model'] = model 

        return await self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, возникающее, когда запрос к OpenAI API является недействительным.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, возникающее, когда происходит неопределенная ошибка, но мы знаем, что можем повторить попытку.
    """
    pass

###########################################################################
# Реестр клиентов
#
# Могут быть различные клиенты, поэтому нужен способ
# их регистрировать и извлекать при необходимости.
#
# Поддерживаются OpenAI и Azure OpenAI Service API по умолчанию.
# Таким образом, параметры API необходимо устанавливать на основе выбора пользователя.
# Это делается в специализированных классах.
#
# Можно также регистрировать пользовательских клиентов для доступа к внутренним или
# нестандартным конечным точкам API.
###########################################################################
_api_type_to_client = {}
_api_type_override = None

def register_client(api_type, client):
    """
    Регистрирует клиента для заданного типа API.

    Args:
        api_type (str): Тип API, для которого нужно зарегистрировать клиента.
        client: Клиент для регистрации.
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиента для заданного типа API.

    Args:
        api_type (str): Тип API, для которого нужно получить клиента.

    Raises:
        ValueError: Если тип API не поддерживается.

    Returns:
        Any: Клиент для заданного типа API.
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f'API type {api_type} is not supported. Please check the \'config.ini\' file.')

def client():
    """
    Возвращает клиента для настроенного типа API.

    Returns:
        Any: Клиент для заданного типа API.
    """
    api_type = config['OpenAI']['API_TYPE'] if _api_type_override is None else _api_type_override
    
    logger.debug(f'Using  API type {api_type}.')
    return _get_client_for_api_type(api_type)


# TODO упростить методы пользовательской конфигурации ниже
def force_api_type(api_type):
    """
    Принудительно устанавливает использование заданного типа API, переопределяя любую другую конфигурацию.

    Args:
        api_type (str): Тип API для использования.
    """
    global _api_type_override
    _api_type_override = api_type

def force_api_cache(cache_api_calls, cache_file_name=default['cache_file_name']):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API, переопределяя любую другую конфигурацию.

    Args:
        cache_api_calls (bool): Определяет, кэшировать ли вызовы API.
        cache_file_name (str): Имя файла для кэширования вызовов API.
    """
    # устанавливаем параметры кэша на всех клиентах
    for client in _api_type_to_client.values():
        client.set_api_cache(cache_api_calls, cache_file_name)

def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения конфигурации по умолчанию для указанного ключа, переопределяя любую другую конфигурацию.

    Args:
        key (str): Ключ для переопределения.
        value: Значение для использования для ключа.

    Raises:
        ValueError: Если ключ не является допустимым ключом конфигурации.
    """
    global default

    # проверка, существует ли ключ
    if key in default:
        default[key] = value
    else:
        raise ValueError(f'Key {key} is not a valid configuration key.')

# Клиент по умолчанию
register_client('openai', OpenAIClient())
register_client('azure', AzureClient())