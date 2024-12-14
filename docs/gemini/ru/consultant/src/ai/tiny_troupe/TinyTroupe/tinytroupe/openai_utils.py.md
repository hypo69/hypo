# Анализ кода модуля `openai_utils.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код структурирован и разделен на логические блоки, такие как настройки, вспомогательные классы и функции для работы с OpenAI API.
    *   Используется логгер для отслеживания ошибок и отладки.
    *   Реализована поддержка кэширования API-вызовов для экономии ресурсов и времени.
    *   Присутствует обработка ошибок при запросах к API с использованием стратегии экспоненциального отката.
    *   Реализована поддержка OpenAI и Azure OpenAI API.
    *   Код имеет базовую документацию, но требует доработки в формате RST.

-   **Минусы:**
    *   Не все функции и классы документированы в формате reStructuredText (RST).
    *   Некоторые функции содержат избыточные блоки `try-except`.
    *   Используются стандартные `json.load` и `pickle`, что не соответствует требованиям.
    *   В некоторых местах логирование недостаточно информативно.
    *   Не все комментарии соответствуют стандарту RST.
    *   Некоторые участки кода помечены как `TODO`, что указывает на незавершенность.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Переписать все docstring и комментарии в формате reStructuredText (RST).
    *   Добавить подробное описание модулей, функций, методов и переменных.
2.  **Импорты:**
    *   Добавить `from src.utils.jjson import j_loads, j_loads_ns` для работы с файлами.
    *   Использовать `from src.logger.logger import logger` для логирования.
3.  **Обработка ошибок:**
    *   Убрать избыточные `try-except` блоки, используя `logger.error` для логирования ошибок.
4.  **Кэширование:**
    *   Заменить `pickle` на `j_loads`/`j_loads_ns` для работы с кэшем, если это возможно.
5.  **Рефакторинг:**
    *   Улучшить читаемость кода, разбив некоторые функции на более мелкие и специализированные.
    *   Удалить или доработать `TODO` блоки.
6.  **Логирование:**
    *   Сделать логирование более информативным, указывая больше контекста для ошибок.
    *   Добавить уровень логирования DEBUG для более подробной отладки.
7.  **Имена:**
    *   Привести имена переменных и функций в соответствие с остальным кодом в проекте.
8.  **Конфигурация:**
    *   Улучшить механизм конфигурации, сделав его более гибким и простым в использовании.

**Оптимизированный код**

```python
"""
Модуль для работы с OpenAI API
=========================================================================================

Этот модуль предоставляет функциональность для взаимодействия с OpenAI API,
включая отправку запросов, получение ответов, подсчет токенов и кэширование результатов.

Поддерживаются как OpenAI, так и Azure OpenAI API.

Пример использования
--------------------

.. code-block:: python

    from tinytroupe.openai_utils import client, LLMCall

    # Пример вызова LLM с использованием шаблонов
    llm_call = LLMCall(system_template_name='system_template', user_template_name='user_template', model='gpt-4')
    response = llm_call.call(input_text='Hello')
    print(response)

    # Пример отправки сообщения напрямую
    openai_client = client()
    messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
    response = openai_client.send_message(messages)
    print(response)
"""
import os
import time
import tiktoken
from typing import Any

from openai import OpenAI, AzureOpenAI
#  Импортируем необходимые функции из src.utils.jjson
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger #  Импортируем logger для логирования
import configparser

from tinytroupe import utils

# We'll use various configuration elements below
config = utils.read_config_file()

###########################################################################
# Default parameter values
###########################################################################
default = {}
default['model'] = config['OpenAI'].get('MODEL', 'gpt-4')
default['max_tokens'] = int(config['OpenAI'].get('MAX_TOKENS', '1024'))
default['temperature'] = float(config['OpenAI'].get('TEMPERATURE', '0.3'))
default['top_p'] = int(config['OpenAI'].get('TOP_P', '0'))
default['frequency_penalty'] = float(config['OpenAI'].get('FREQ_PENALTY', '0.0'))
default['presence_penalty'] = float(
    config['OpenAI'].get('PRESENCE_PENALTY', '0.0'))
default['timeout'] = float(config['OpenAI'].get('TIMEOUT', '30.0'))
default['max_attempts'] = float(config['OpenAI'].get('MAX_ATTEMPTS', '0.0'))
default['waiting_time'] = float(config['OpenAI'].get('WAITING_TIME', '0.5'))
default['exponential_backoff_factor'] = float(config['OpenAI'].get('EXPONENTIAL_BACKOFF_FACTOR', '5'))

default['embedding_model'] = config['OpenAI'].get('EMBEDDING_MODEL', 'text-embedding-3-small')

default['cache_api_calls'] = config['OpenAI'].getboolean('CACHE_API_CALLS', False)
default['cache_file_name'] = config['OpenAI'].get('CACHE_FILE_NAME', 'openai_api_cache.pickle')

###########################################################################
# Model calling helpers
###########################################################################

# TODO under development
class LLMCall:
    """
    Представляет вызов языковой модели (LLM).
    
    Содержит входные сообщения, конфигурацию модели и вывод модели.
    """
    def __init__(self, system_template_name:str, user_template_name:str=None, **model_params):
        """
        Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами.

        :param system_template_name: Имя системного шаблона.
        :type system_template_name: str
        :param user_template_name: Имя пользовательского шаблона (опционально).
        :type user_template_name: str
        :param model_params: Дополнительные параметры модели.
        :type model_params: dict
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    def call(self, **rendering_configs):
        """
        Вызывает языковую модель (LLM) с указанными конфигурациями рендеринга.

        :param rendering_configs: Конфигурации рендеринга для шаблонов.
        :type rendering_configs: dict
        :return: Содержимое ответа модели или None в случае ошибки.
        :rtype: str | None
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)
        
        #  Код вызывает LLM модель
        self.model_output = client().send_message(self.messages, **self.model_params)

        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}")
            return None


    def __repr__(self):
        """
        Возвращает строковое представление объекта LLMCall.

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f"LLMCall(messages={self.messages}, model_config={self.model_params}, model_output={self.model_output})"


###########################################################################
# Client class
###########################################################################

class OpenAIClient:
    """
    Утилитный класс для взаимодействия с OpenAI API.
    """

    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        """
        Инициализирует клиент OpenAI.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        logger.debug('Initializing OpenAIClient')

        #  Код определяет, следует ли кэшировать вызовы API и повторно их использовать
        self.set_api_cache(cache_api_calls, cache_file_name)
    
    def set_api_cache(self, cache_api_calls, cache_file_name=default['cache_file_name']):
        """
        Включает или отключает кэширование вызовов API.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = cache_file_name
        if self.cache_api_calls:
            #  Код загружает кэш, если он существует
            self.api_cache = self._load_cache()
    
    
    def _setup_from_config(self):
        """
        Настраивает параметры OpenAI API для этого клиента.
        """
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def send_message(self,
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
                     echo=False):
        """
        Отправляет сообщение в OpenAI API и возвращает ответ.

        :param current_messages: Список словарей, представляющих историю разговора.
        :type current_messages: list
        :param model: Идентификатор модели для генерации ответа.
        :type model: str
        :param temperature: Контролирует "креативность" ответа. Более высокие значения приводят к более разнообразным ответам.
        :type temperature: float
        :param max_tokens: Максимальное количество токенов (слов или знаков препинания) для генерации в ответе.
        :type max_tokens: int
        :param top_p: Контролирует "качество" ответа. Более высокие значения приводят к более связным ответам.
        :type top_p: float
        :param frequency_penalty: Контролирует "повторение" ответа. Более высокие значения приводят к меньшему повторению.
        :type frequency_penalty: float
        :param presence_penalty: Контролирует "разнообразие" ответа. Более высокие значения приводят к более разнообразным ответам.
        :type presence_penalty: float
        :param stop: Строка, которая, если встречается в сгенерированном ответе, приведет к остановке генерации.
        :type stop: list
        :param timeout: Максимальное количество секунд ожидания ответа от API.
        :type timeout: float
        :param max_attempts: Максимальное количество попыток для генерации ответа.
        :type max_attempts: int
        :param waiting_time: Время ожидания между попытками.
        :type waiting_time: float
        :param exponential_backoff_factor: Коэффициент экспоненциального отката для времени ожидания.
        :type exponential_backoff_factor: float
        :param n: Количество ответов для генерации.
        :type n: int
        :param echo: Флаг, определяющий, нужно ли возвращать входное сообщение в ответе.
        :type echo: bool
        :raises InvalidRequestError: Если запрос к API недействителен.
        :raises NonTerminalError: Если произошла ошибка, которую можно исправить повторной попыткой.
        :return: Словарь, представляющий сгенерированный ответ, или None в случае ошибки.
        :rtype: dict | None
        """

        def aux_exponential_backoff():
            """
            Вспомогательная функция для реализации экспоненциального отката.

            :meta private:
            """
            nonlocal waiting_time
            logger.info(f"Request failed. Waiting {waiting_time} seconds between requests...")
            time.sleep(waiting_time)

            # exponential backoff
            waiting_time = waiting_time * exponential_backoff_factor
        
        #  Код настраивает конфигурации OpenAI для этого клиента.
        self._setup_from_config()
        
        #  Код адаптирует параметры к типу API, создавая словарь с ними
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
            try:
                i += 1

                try:
                    logger.debug(f"Sending messages to OpenAI API. Token count={self._count_tokens(current_messages, model)}.")
                except NotImplementedError:
                    logger.debug(f"Token count not implemented for model {model}.")
                    
                start_time = time.monotonic()
                logger.debug(f"Calling model with client class {self.__class__.__name__}.")

                ###############################################################
                #  Код вызывает модель либо из кэша, либо из API
                ###############################################################
                cache_key = str((model, chat_api_params)) # need string to be hashable
                if self.cache_api_calls and (cache_key in self.api_cache):
                    response = self.api_cache[cache_key]
                else:
                    logger.info(f"Waiting {waiting_time} seconds before next API request (to avoid throttling)...")
                    time.sleep(waiting_time)
                    
                    response = self._raw_model_call(model, chat_api_params)
                    if self.cache_api_calls:
                        self.api_cache[cache_key] = response
                        self._save_cache()
                
                
                logger.debug(f"Got response from API: {response}")
                end_time = time.monotonic()
                logger.debug(
                    f"Got response in {end_time - start_time:.2f} seconds after {i + 1} attempts.")

                return utils.sanitize_dict(self._raw_model_response_extractor(response))

            except InvalidRequestError as e:
                logger.error(f"[{i}] Invalid request error, won't retry: {e}")

                #  Нет смысла повторять запрос, если он недействителен
                #  Поэтому код сразу возвращает None
                return None
            
            except openai.BadRequestError as e:
                logger.error(f"[{i}] Invalid request error, won't retry: {e}")
                
                #  Нет смысла повторять запрос, если он недействителен
                #  Поэтому код сразу возвращает None
                return None
            
            except openai.RateLimitError:
                logger.warning(
                    f"[{i}] Rate limit error, waiting a bit and trying again.")
                aux_exponential_backoff()
            
            except NonTerminalError as e:
                logger.error(f"[{i}] Non-terminal error: {e}")
                aux_exponential_backoff()
                
            except Exception as e:
                logger.error(f"[{i}] Error: {e}")

        logger.error(f"Failed to get response after {max_attempts} attempts.")
        return None
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает OpenAI API с заданными параметрами. Подклассы должны переопределить
        этот метод для реализации собственных вызовов API.

        :param model: Идентификатор модели для использования.
        :type model: str
        :param chat_api_params: Параметры для вызова API.
        :type chat_api_params: dict
        :return: Ответ от API.
        :rtype: openai.ChatCompletion
        """
        
        chat_api_params['model'] = model # OpenAI API uses this parameter name
        return self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API. Подклассы должны переопределить
        этот метод для реализации собственного извлечения ответа.

        :param response: Ответ от API.
        :type response: openai.ChatCompletion
        :return: Извлеченный ответ.
        :rtype: dict
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str):
        """
        Подсчитывает количество токенов OpenAI в списке сообщений, используя tiktoken.

        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

        :param messages: Список словарей, представляющих историю разговора.
        :type messages: list
        :param model: Название модели для кодирования строки.
        :type model: str
        :return: Количество токенов или None в случае ошибки.
        :rtype: int | None
        """
        try:
            try:
                encoding = tiktoken.encoding_for_model(model)
            except KeyError:
                logger.debug("Token count: model not found. Using cl100k_base encoding.")
                encoding = tiktoken.get_encoding("cl100k_base")
            if model in {
                "gpt-3.5-turbo-0613",
                "gpt-3.5-turbo-16k-0613",
                "gpt-4-0314",
                "gpt-4-32k-0314",
                "gpt-4-0613",
                "gpt-4-32k-0613",
                }:
                tokens_per_message = 3
                tokens_per_name = 1
            elif model == "gpt-3.5-turbo-0301":
                tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
                tokens_per_name = -1  # if there's a name, the role is omitted
            elif "gpt-3.5-turbo" in model:
                logger.debug("Token count: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
                return self._count_tokens(messages, model="gpt-3.5-turbo-0613")
            elif ("gpt-4" in model) or ("ppo" in model):
                logger.debug("Token count: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
                return self._count_tokens(messages, model="gpt-4-0613")
            else:
                raise NotImplementedError(
                    f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
                )
            num_tokens = 0
            for message in messages:
                num_tokens += tokens_per_message
                for key, value in message.items():
                    num_tokens += len(encoding.encode(value))
                    if key == "name":
                        num_tokens += tokens_per_name
            num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
            return num_tokens
        
        except Exception as e:
            logger.error(f"Error counting tokens: {e}")
            return None

    def _save_cache(self):
        """
        Сохраняет кэш API на диск. Используется pickle, так как некоторые объекты
        не являются JSON-сериализуемыми.
        """
        #  Код использует pickle для сохранения кэша
        try:
            with open(self.cache_file_name, "wb") as f:
                pickle.dump(self.api_cache, f)
        except Exception as e:
            logger.error(f"Error saving cache: {e}")

    
    def _load_cache(self):
        """
        Загружает кэш API с диска.
        """
        #  Код загружает кэш из файла, если он существует
        try:
            if os.path.exists(self.cache_file_name):
                with open(self.cache_file_name, "rb") as f:
                  return pickle.load(f)
            else:
                return {}
        except Exception as e:
            logger.error(f"Error loading cache: {e}")
            return {}
            

    def get_embedding(self, text, model=default['embedding_model']):
        """
        Получает вложение (embedding) заданного текста, используя указанную модель.

        :param text: Текст для получения вложения.
        :type text: str
        :param model: Название модели для использования.
        :type model: str
        :return: Вложение текста.
        :rtype: list
        """
        response = self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)
    
    def _raw_embedding_model_call(self, text, model):
        """
        Вызывает OpenAI API для получения вложения заданного текста.
        Подклассы должны переопределить этот метод для реализации собственных вызовов API.

        :param text: Текст для получения вложения.
        :type text: str
        :param model: Название модели для использования.
        :type model: str
        :return: Ответ от API.
        :rtype: openai.Embedding
        """
        return self.client.embeddings.create(
            input=[text],
            model=model
        )
    
    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает вложение из ответа API. Подклассы должны переопределить
        этот метод для реализации собственного извлечения ответа.

        :param response: Ответ от API.
        :type response: openai.Embedding
        :return: Извлеченное вложение.
        :rtype: list
        """
        return response.data[0].embedding

class AzureClient(OpenAIClient):
    """
    Клиент для взаимодействия с Azure OpenAI Service API.
    """

    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        """
        Инициализирует клиент Azure.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        logger.debug("Initializing AzureClient")

        super().__init__(cache_api_calls, cache_file_name)
    
    def _setup_from_config(self):
        """
        Настраивает параметры Azure OpenAI Service API для этого клиента,
        включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint= os.getenv('AZURE_OPENAI_ENDPOINT'),
                                  api_version = config['OpenAI']['AZURE_API_VERSION'],
                                  api_key = os.getenv('AZURE_OPENAI_KEY'))
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает Azue OpenAI Service API с заданными параметрами.

        :param model: Идентификатор модели для использования.
        :type model: str
        :param chat_api_params: Параметры для вызова API.
        :type chat_api_params: dict
        :return: Ответ от API.
        :rtype: openai.ChatCompletion
        """
        chat_api_params['model'] = model

        return self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, которое возникает, если запрос к OpenAI API недействителен.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, которое возникает, когда происходит неопределенная ошибка, но известно, что можно повторить запрос.
    """
    pass

###########################################################################
# Clients registry
#
# We can have potentially different clients, so we need a place to 
# register them and retrieve them when needed.
#
# We support both OpenAI and Azure OpenAI Service API by default.
# Thus, we need to set the API parameters based on the choice of the user.
# This is done within specialized classes.
#
# It is also possible to register custom clients, to access internal or
# otherwise non-conventional API endpoints.
###########################################################################
_api_type_to_client = {}
_api_type_override = None

def register_client(api_type, client):
    """
    Регистрирует клиента для заданного типа API.

    :param api_type: Тип API, для которого регистрируется клиент.
    :type api_type: str
    :param client: Клиент для регистрации.
    :type client: OpenAIClient
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиента для заданного типа API.

    :param api_type: Тип API, для которого нужно получить клиента.
    :type api_type: str
    :raises ValueError: Если тип API не поддерживается.
    :return: Клиент для заданного типа API.
    :rtype: OpenAIClient
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f"API type {api_type} is not supported. Please check the 'config.ini' file.")

def client():
    """
    Возвращает клиента для сконфигурированного типа API.

    :return: Клиент для сконфигурированного типа API.
    :rtype: OpenAIClient
    """
    api_type = config['OpenAI']['API_TYPE'] if _api_type_override is None else _api_type_override
    
    logger.debug(f"Using  API type {api_type}.")
    return _get_client_for_api_type(api_type)


# TODO simplify the custom configuration methods below

def force_api_type(api_type):
    """
    Принудительно устанавливает использование заданного типа API, переопределяя любую другую конфигурацию.

    :param api_type: Тип API для использования.
    :type api_type: str
    """
    global _api_type_override
    _api_type_override = api_type

def force_api_cache(cache_api_calls, cache_file_name=default['cache_file_name']):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API, переопределяя любую другую конфигурацию.

    :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
    :type cache_api_calls: bool
    :param cache_file_name: Имя файла для кэширования API-вызовов.
    :type cache_file_name: str
    """
    #  Код устанавливает параметры кэша для всех клиентов
    for client in _api_type_to_client.values():
        client.set_api_cache(cache_api_calls, cache_file_name)

def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения конфигурации по умолчанию для указанного ключа,
    переопределяя любую другую конфигурацию.

    :param key: Ключ для переопределения.
    :type key: str
    :param value: Значение для использования для ключа.
    :type value: Any
    :raises ValueError: Если ключ не является допустимым ключом конфигурации.
    """
    global default

    #  Код проверяет, существует ли ключ
    if key in default:
        default[key] = value
    else:
        raise ValueError(f"Key {key} is not a valid configuration key.")

# default client
register_client('openai', OpenAIClient())
register_client('azure', AzureClient())
```