# Анализ кода модуля `openai_utils.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и разбит на классы и функции, что облегчает его понимание и поддержку.
    - Использование `logger` для логирования ошибок и отладки.
    - Реализована поддержка кэширования API запросов.
    - Поддержка различных типов API (OpenAI, Azure).
    - Наличие механизма для переопределения настроек API.
- Минусы
    - Не все функции документированы в стиле RST.
    - Некоторые константы не вынесены в статические переменные класса.
    - Использования `try-except` в некоторых местах можно заменить на проверку условий
    - Отсутствует обработка ошибок при загрузке/сохранении кэша
    - Некоторые комментарии не соответствуют стандарту
    - Использование `logger.debug` для вывода токенов, лучше использовать `logger.info`

**Рекомендации по улучшению**

1. **Документация**:
   - Добавить документацию в формате RST для всех функций, методов и классов.
   - Использовать docstrings для описания параметров, возвращаемых значений и исключений.
   - Придерживаться стандартов оформления docstring в Python (для Sphinx).
2.  **Импорты**:
    - Импортировать `j_loads` и `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
    - Явный импорт `logger` из `src.logger.logger`.
3. **Кэширование**:
   - Добавить обработку ошибок при загрузке и сохранении кэша.
   - Использовать `Path` для работы с файлами, а не напрямую строки.
4.  **Конфигурация**:
    - Вынести значения по умолчанию в статические переменные класса.
5. **Обработка ошибок**:
   - Заменить избыточное использование `try-except` на более специфичную обработку с `logger.error` там где это возможно.
6.  **Логирование**:
    -  Заменить `logger.debug` на `logger.info` для вывода токенов, так как это важная информация.
7. **Комментарии**:
    -  Улучшить комментарии в соответствии с инструкцией.
8.  **Форматирование кода**:
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    - Использовать одинарные кавычки в коде.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с API OpenAI и Azure OpenAI.
=====================================================

Этот модуль предоставляет классы и функции для работы с моделями OpenAI и Azure OpenAI,
включая отправку сообщений, получение эмбеддингов и управление кэшем API.

Пример использования
--------------------

Пример использования класса `OpenAIClient`:

.. code-block:: python

    from tinytroupe.openai_utils import OpenAIClient
    client = OpenAIClient()
    messages = [{"role": "user", "content": "Hello, world!"}]
    response = client.send_message(messages)
    print(response)

"""
import os
import time
import pickle
from pathlib import Path
import tiktoken
from src.utils.jjson import j_loads
from src.logger.logger import logger
from openai import OpenAI, AzureOpenAI
from openai.error import RateLimitError, BadRequestError
from tinytroupe import utils

# We'll use various configuration elements below
config = utils.read_config_file()

###########################################################################
# Default parameter values
###########################################################################
class Defaults:
    """
    Класс, содержащий значения параметров по умолчанию для работы с OpenAI API.

    Attributes:
        model (str): Идентификатор модели для использования.
        max_tokens (int): Максимальное количество токенов в ответе.
        temperature (float): Температура для генерации текста.
        top_p (int): Вероятность выбора наиболее вероятного токена.
        frequency_penalty (float): Штраф за частоту использования слов.
        presence_penalty (float): Штраф за присутствие слов.
        timeout (float): Максимальное время ожидания ответа от API.
        max_attempts (int): Максимальное количество попыток запроса к API.
        waiting_time (float): Время ожидания между повторными запросами.
        exponential_backoff_factor (float): Коэффициент экспоненциального отката времени ожидания.
        embedding_model (str): Идентификатор модели для получения эмбеддингов.
        cache_api_calls (bool): Флаг, указывающий, следует ли кэшировать API-запросы.
        cache_file_name (str): Имя файла для кэширования API-запросов.
    """
    model = config['OpenAI'].get('MODEL', 'gpt-4')
    max_tokens = int(config['OpenAI'].get('MAX_TOKENS', '1024'))
    temperature = float(config['OpenAI'].get('TEMPERATURE', '0.3'))
    top_p = int(config['OpenAI'].get('TOP_P', '0'))
    frequency_penalty = float(config['OpenAI'].get('FREQ_PENALTY', '0.0'))
    presence_penalty = float(config['OpenAI'].get('PRESENCE_PENALTY', '0.0'))
    timeout = float(config['OpenAI'].get('TIMEOUT', '30.0'))
    max_attempts = int(config['OpenAI'].get('MAX_ATTEMPTS', '0'))
    waiting_time = float(config['OpenAI'].get('WAITING_TIME', '0.5'))
    exponential_backoff_factor = float(config['OpenAI'].get('EXPONENTIAL_BACKOFF_FACTOR', '5'))
    embedding_model = config['OpenAI'].get('EMBEDDING_MODEL', 'text-embedding-3-small')
    cache_api_calls = config['OpenAI'].getboolean('CACHE_API_CALLS', False)
    cache_file_name = config['OpenAI'].get('CACHE_FILE_NAME', 'openai_api_cache.pickle')


###########################################################################
# Model calling helpers
###########################################################################

# TODO under development
class LLMCall:
    """
    Класс, представляющий вызов языковой модели (LLM).

    Содержит входные сообщения, конфигурацию модели и вывод модели.
    """
    def __init__(self, system_template_name:str, user_template_name:str=None, **model_params):
        """
        Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами.

        Args:
            system_template_name (str): Название системного шаблона.
            user_template_name (str, optional): Название пользовательского шаблона. Defaults to None.
            **model_params: Дополнительные параметры модели.
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    def call(self, **rendering_configs):
        """
        Вызывает LLM-модель с указанными конфигурациями рендеринга.

         Args:
            **rendering_configs: Конфигурации для рендеринга шаблонов.
        Returns:
            str: Содержание ответа модели, или None в случае ошибки.
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)
        
        # Вызов LLM модели
        self.model_output = client().send_message(self.messages, **self.model_params)

        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}")
            return None


    def __repr__(self):
        """
        Возвращает строковое представление объекта LLMCall.
        """
        return f"LLMCall(messages={self.messages}, model_config={self.model_params}, model_output={self.model_output})"


###########################################################################
# Client class
###########################################################################

class OpenAIClient:
    """
    Утилитарный класс для взаимодействия с OpenAI API.
    """

    def __init__(self, cache_api_calls=Defaults.cache_api_calls, cache_file_name=Defaults.cache_file_name) -> None:
        """
        Инициализирует OpenAIClient.

        Args:
            cache_api_calls (bool): Флаг, указывающий, следует ли кэшировать API-запросы.
            cache_file_name (str): Имя файла для кэширования API-запросов.
        """
        logger.debug("Initializing OpenAIClient")

        # Установка кэша API
        self.set_api_cache(cache_api_calls, cache_file_name)
    
    def set_api_cache(self, cache_api_calls, cache_file_name=Defaults.cache_file_name):
        """
        Включает или отключает кэширование API-вызовов.

        Args:
            cache_api_calls (bool): Флаг, указывающий, следует ли кэшировать API-запросы.
            cache_file_name (str): Имя файла для использования для кэширования API-вызовов.
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = Path(cache_file_name)
        if self.cache_api_calls:
            # Загрузка кэша, если он есть
            self.api_cache = self._load_cache()
    
    
    def _setup_from_config(self):
        """
        Настраивает конфигурацию OpenAI API для этого клиента.
        """
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def send_message(self,
                    current_messages,
                     model=Defaults.model,
                     temperature=Defaults.temperature,
                     max_tokens=Defaults.max_tokens,
                     top_p=Defaults.top_p,
                     frequency_penalty=Defaults.frequency_penalty,
                     presence_penalty=Defaults.presence_penalty,
                     stop=[],
                     timeout=Defaults.timeout,
                     max_attempts=Defaults.max_attempts,
                     waiting_time=Defaults.waiting_time,
                     exponential_backoff_factor=Defaults.exponential_backoff_factor,
                     n = 1,
                     echo=False):
        """
        Отправляет сообщение в OpenAI API и возвращает ответ.

        Args:
            current_messages (list): Список словарей, представляющих историю разговора.
            model (str): Идентификатор модели для использования для генерации ответа.
            temperature (float): Контролирует 'креативность' ответа. Более высокие значения приводят к более разнообразным ответам.
            max_tokens (int): Максимальное количество токенов (слов или знаков препинания) для генерации в ответе.
            top_p (float): Контролирует 'качество' ответа. Более высокие значения приводят к более связным ответам.
            frequency_penalty (float): Контролирует 'повторение' ответа. Более высокие значения приводят к меньшему повторению.
            presence_penalty (float): Контролирует 'разнообразие' ответа. Более высокие значения приводят к более разнообразным ответам.
            stop (str): Строка, которая, если встретится в сгенерированном ответе, вызовет остановку генерации.
            max_attempts (int): Максимальное количество попыток сделать, прежде чем отказаться от генерации ответа.
            timeout (int): Максимальное количество секунд ожидания ответа от API.
            waiting_time (float): Время ожидания между повторными запросами.
            exponential_backoff_factor (float): Коэффициент экспоненциального отката времени ожидания.
            n (int): Количество ответов, которые нужно сгенерировать.
            echo (bool): Если True, то возвращает также входное сообщение

        Returns:
            dict: Словарь, представляющий сгенерированный ответ.
        """

        def aux_exponential_backoff():
            nonlocal waiting_time
            logger.info(f"Request failed. Waiting {waiting_time} seconds between requests...")
            time.sleep(waiting_time)

            # экспоненциальный откат
            waiting_time = waiting_time * exponential_backoff_factor
        
        # Настройка конфигураций OpenAI для этого клиента
        self._setup_from_config()
        
        # Адаптация параметров к типу API, поэтому сначала создается словарь с ними
        chat_api_params = {
            'messages': current_messages,
            'temperature': temperature,
            'max_tokens': max_tokens,
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
                    logger.info(f"Sending messages to OpenAI API. Token count={self._count_tokens(current_messages, model)}.")
                except NotImplementedError:
                    logger.info(f"Token count not implemented for model {model}.")
                
                start_time = time.monotonic()
                logger.debug(f"Calling model with client class {self.__class__.__name__}.")

                ###############################################################
                # вызов модели, либо из кэша, либо из API
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
                return None

            except BadRequestError as e:
                logger.error(f"[{i}] Bad request error, won't retry: {e}")
                return None
            
            except RateLimitError:
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
        Вызывает OpenAI API с заданными параметрами. Подклассы должны
        переопределить этот метод для реализации собственных вызовов API.

         Args:
            model (str): Идентификатор модели для использования.
            chat_api_params (dict): Параметры для вызова API.
        Returns:
           openai.ChatCompletion: Объект ответа от API.
        """
        chat_api_params['model'] = model # OpenAI API использует это имя параметра
        return self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API. Подклассы должны
        переопределить этот метод для реализации собственного извлечения ответа.
         Args:
            response (openai.ChatCompletion): Объект ответа от API.
        Returns:
            dict: Словарь с извлеченным сообщением.
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str):
        """
        Подсчитывает количество токенов OpenAI в списке сообщений, используя tiktoken.
        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

         Args:
            messages (list): Список словарей, представляющих историю разговора.
            model (str): Название модели для использования для кодирования строки.
        Returns:
            int: Количество токенов, или None в случае ошибки.
        """
        try:
            try:
                encoding = tiktoken.encoding_for_model(model)
            except KeyError:
                logger.debug("Token count: model not found. Using cl100k_base encoding.")
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
                tokens_per_message = 4  # каждое сообщение следует <|start|>{role/name}\n{content}<|end|>\n
                tokens_per_name = -1  # если есть имя, роль опускается
            elif "gpt-3.5-turbo" in model:
                logger.debug("Token count: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
                return self._count_tokens(messages, model='gpt-3.5-turbo-0613')
            elif ("gpt-4" in model) or ("ppo" in model):
                logger.debug("Token count: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
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
            logger.error(f"Error counting tokens: {e}")
            return None

    def _save_cache(self):
        """
        Сохраняет кэш API на диск. Мы используем pickle, потому что некоторые объекты
        не являются сериализуемыми в JSON.
        """
        # использовать pickle для сохранения кэша
        try:
            with open(self.cache_file_name, 'wb') as f:
                pickle.dump(self.api_cache, f)
        except Exception as e:
            logger.error(f'Error saving cache to {self.cache_file_name}: {e}')


    def _load_cache(self):
        """
        Загружает кэш API с диска.
        """
        # unpickle
        if self.cache_file_name.exists():
            try:
               with open(self.cache_file_name, 'rb') as f:
                   return pickle.load(f)
            except Exception as e:
                logger.error(f'Error loading cache from {self.cache_file_name}: {e}')
                return {}
        return {}

    def get_embedding(self, text, model=Defaults.embedding_model):
        """
        Получает эмбеддинг заданного текста, используя указанную модель.

        Args:
            text (str): Текст для эмбеддинга.
            model (str): Название модели для использования для эмбеддинга текста.

        Returns:
             list: Эмбеддинг текста.
        """
        response = self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)
    
    def _raw_embedding_model_call(self, text, model):
        """
        Вызывает OpenAI API для получения эмбеддинга заданного текста. Подклассы должны
        переопределить этот метод для реализации собственных вызовов API.

         Args:
            text (str): Текст для эмбеддинга.
            model (str): Название модели для использования.
        Returns:
             openai.Embedding: Объект ответа от API.
        """
        return self.client.embeddings.create(
            input=[text],
            model=model
        )
    
    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает эмбеддинг из ответа API. Подклассы должны
        переопределить этот метод для реализации собственного извлечения ответа.

         Args:
            response (openai.Embedding): Объект ответа от API.
        Returns:
             list: Эмбеддинг текста.
        """
        return response.data[0].embedding

class AzureClient(OpenAIClient):
    """
    Клиент для взаимодействия с Azure OpenAI Service API.
    """

    def __init__(self, cache_api_calls=Defaults.cache_api_calls, cache_file_name=Defaults.cache_file_name) -> None:
        """
        Инициализирует AzureClient.

        Args:
            cache_api_calls (bool): Флаг, указывающий, следует ли кэшировать API-запросы.
            cache_file_name (str): Имя файла для кэширования API-запросов.
        """
        logger.debug("Initializing AzureClient")
        super().__init__(cache_api_calls, cache_file_name)
    
    def _setup_from_config(self):
        """
        Настраивает конфигурацию Azure OpenAI Service API для этого клиента,
        включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint= os.getenv('AZURE_OPENAI_ENDPOINT'),
                                  api_version = config['OpenAI']['AZURE_API_VERSION'],
                                  api_key = os.getenv('AZURE_OPENAI_KEY'))
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает Azue OpenAI Service API с заданными параметрами.
         Args:
            model (str): Идентификатор модели для использования.
            chat_api_params (dict): Параметры для вызова API.
        Returns:
           openai.ChatCompletion: Объект ответа от API.
        """
        chat_api_params['model'] = model
        return self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, возникающее, когда запрос к OpenAI API недействителен.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, возникающее, когда происходит неуказанная ошибка, но мы знаем, что можно повторить попытку.
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
    Регистрирует клиент для данного типа API.

    Args:
        api_type (str): Тип API, для которого мы хотим зарегистрировать клиента.
        client: Клиент для регистрации.
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиента для данного типа API.

    Args:
        api_type (str): Тип API, для которого мы хотим получить клиента.

    Raises:
        ValueError: Если тип API не поддерживается.

    Returns:
        object: Клиент для данного типа API.
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f'API type {api_type} is not supported. Please check the \'config.ini\' file.')

def client():
    """
    Возвращает клиента для настроенного типа API.
    """
    api_type = config['OpenAI']['API_TYPE'] if _api_type_override is None else _api_type_override
    
    logger.debug(f"Using  API type {api_type}.")
    return _get_client_for_api_type(api_type)


# TODO simplify the custom configuration methods below

def force_api_type(api_type):
    """
    Принудительно устанавливает использование заданного типа API, таким образом переопределяя любую другую конфигурацию.

    Args:
        api_type (str): Тип API для использования.
    """
    global _api_type_override
    _api_type_override = api_type

def force_api_cache(cache_api_calls, cache_file_name=Defaults.cache_file_name):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API, таким образом переопределяя любую другую конфигурацию.

    Args:
        cache_api_calls (bool): Следует ли кэшировать API-вызовы.
        cache_file_name (str): Имя файла для использования для кэширования API-вызовов.
    """
    # устанавливаем параметры кэша на всех клиентах
    for client in _api_type_to_client.values():
        client.set_api_cache(cache_api_calls, cache_file_name)

def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения конфигурации по умолчанию для указанного ключа, таким образом переопределяя любую другую конфигурацию.

    Args:
        key (str): Ключ для переопределения.
        value: Значение для использования для ключа.
    Raises:
        ValueError: Если ключ не является допустимым ключом конфигурации.
    """
    global default
    default = Defaults.__dict__
    # проверяем, существует ли ключ на самом деле
    if key in default:
        default[key] = value
    else:
        raise ValueError(f'Key {key} is not a valid configuration key.')

# default client
register_client('openai', OpenAIClient())
register_client('azure', AzureClient())