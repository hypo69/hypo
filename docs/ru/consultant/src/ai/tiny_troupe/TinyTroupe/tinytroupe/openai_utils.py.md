### Анализ кода модуля `openai_utils`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Хорошо структурированный код с разделением на классы и функции.
    - Использование `configparser` для чтения конфигурационных файлов.
    - Реализация кэширования API-вызовов.
    - Поддержка нескольких API-клиентов (OpenAI и Azure).
    - Присутствуют комментарии к коду.
- **Минусы**:
    - Некоторые комментарии не информативны ("получаем", "делаем").
    - Использование `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует полная RST-документация для всех функций и классов.
    - Смешанное использование одинарных и двойных кавычек.
    - Не все логи используют `logger.error`.
    -  Чрезмерное использование `try-except` блоков.
    -  Импорт `logger` через `logging.getLogger`.

**Рекомендации по улучшению**:

1.  **Форматирование кода**:
    -   Привести все строки к единому стандарту: использовать одинарные кавычки (`'`) для строк в коде, двойные кавычки (`"`) только для вывода, ошибок и ввода.
2.  **Использование `j_loads`**:
    -   Заменить все использования `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Импорт `logger`**:
    -   Импортировать `logger` из `src.logger`, а не через `logging.getLogger`.
4.  **RST-документация**:
    -   Добавить RST-документацию для всех классов, методов и функций.
5.  **Улучшение комментариев**:
    -   Избегать неинформативных комментариев. Использовать точные описания действий.
6.  **Обработка ошибок**:
    -   Пересмотреть использование `try-except` блоков. Использовать `logger.error` для логирования ошибок.
7.  **Выравнивание**:
    -   Выровнять названия функций, переменных и импортов.

**Оптимизированный код**:

```python
"""
Модуль для работы с OpenAI API
=================================================

Модуль содержит класс :class:`OpenAIClient` и :class:`AzureClient`,
которые используются для взаимодействия с OpenAI и Azure OpenAI API.

Пример использования
----------------------
.. code-block:: python

    from tinytroupe.openai_utils import OpenAIClient, AzureClient
    
    # Использование OpenAI
    openai_client = OpenAIClient()
    response = openai_client.send_message(messages=[{'role': 'user', 'content': 'Hello!'}])
    print(response)
    
    # Использование Azure OpenAI
    azure_client = AzureClient()
    response = azure_client.send_message(messages=[{'role': 'user', 'content': 'Hello!'}])
    print(response)
"""
import os
import time
import pickle
import tiktoken
from pathlib import Path
from openai import OpenAI, AzureOpenAI
from src.logger import logger # используем импорт из src.logger
from tinytroupe import utils
from src.utils.jjson import j_loads # используем j_loads
import configparser

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
    Класс, представляющий вызов языковой модели (LLM).

    Содержит входные сообщения, конфигурацию модели и вывод модели.
    
    :param system_template_name: Имя системного шаблона.
    :type system_template_name: str
    :param user_template_name: Имя пользовательского шаблона, defaults to None
    :type user_template_name: str, optional
    :param model_params: Параметры модели.
    :type model_params: dict
    """
    def __init__(self, system_template_name: str, user_template_name: str = None, **model_params):
        """
        Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами.

        :param system_template_name: Имя системного шаблона.
        :type system_template_name: str
        :param user_template_name: Имя пользовательского шаблона.
        :type user_template_name: str
        :param model_params: Параметры модели.
        :type model_params: dict
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    def call(self, **rendering_configs):
        """
        Вызывает LLM-модель с указанными конфигурациями рендеринга.

        :param rendering_configs: Конфигурации рендеринга.
        :type rendering_configs: dict
        :return: Содержание ответа модели, или None в случае ошибки
        :rtype: str | None
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)
        
        # вызываем LLM-модель
        self.model_output = client().send_message(self.messages, **self.model_params)

        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f'Model output does not contain \'content\' key: {self.model_output}')
            return None

    def __repr__(self):
        """
        Возвращает строковое представление объекта LLMCall.
        
        :return: Строковое представление объекта
        :rtype: str
        """
        return f'LLMCall(messages={self.messages}, model_config={self.model_config}, model_output={self.model_output})'


###########################################################################
# Client class
###########################################################################

class OpenAIClient:
    """
    Утилитный класс для взаимодействия с OpenAI API.
    
    :param cache_api_calls: Флаг для включения/выключения кэширования API-вызовов, defaults to default['cache_api_calls']
    :type cache_api_calls: bool, optional
    :param cache_file_name: Имя файла для кэширования API-вызовов, defaults to default['cache_file_name']
    :type cache_file_name: str, optional
    """

    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        """
        Инициализирует экземпляр класса OpenAIClient.
        
        :param cache_api_calls: Флаг для включения/выключения кэширования API-вызовов, defaults to default['cache_api_calls']
        :type cache_api_calls: bool, optional
        :param cache_file_name: Имя файла для кэширования API-вызовов, defaults to default['cache_file_name']
        :type cache_file_name: str, optional
        """
        logger.debug('Initializing OpenAIClient')
        # устанавливаем кэш API-вызовов
        self.set_api_cache(cache_api_calls, cache_file_name)
    
    def set_api_cache(self, cache_api_calls, cache_file_name=default['cache_file_name']):
        """
        Включает или выключает кэширование API-вызовов.
        
        :param cache_api_calls: Флаг для включения/выключения кэширования API-вызовов.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов, defaults to default['cache_file_name']
        :type cache_file_name: str, optional
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = cache_file_name
        if self.cache_api_calls:
            # загружаем кэш, если есть
            self.api_cache = self._load_cache()
    
    def _setup_from_config(self):
        """
        Настраивает конфигурации OpenAI API для этого клиента.
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
                     n=1,
                     echo=False):
        """
        Отправляет сообщение в OpenAI API и возвращает ответ.

        :param current_messages: Список словарей, представляющих историю разговора.
        :type current_messages: list
        :param model: ID модели для использования при генерации ответа, defaults to default['model']
        :type model: str, optional
        :param temperature: Контролирует "креативность" ответа. Более высокие значения приводят к более разнообразным ответам, defaults to default['temperature']
        :type temperature: float, optional
        :param max_tokens: Максимальное количество токенов для генерации в ответе, defaults to default['max_tokens']
        :type max_tokens: int, optional
        :param top_p: Контролирует "качество" ответа. Более высокие значения приводят к более связным ответам, defaults to default['top_p']
        :type top_p: float, optional
        :param frequency_penalty: Контролирует "повторение" ответа. Более высокие значения приводят к меньшему повторению, defaults to default['frequency_penalty']
        :type frequency_penalty: float, optional
        :param presence_penalty: Контролирует "разнообразие" ответа. Более высокие значения приводят к более разнообразным ответам, defaults to default['presence_penalty']
        :type presence_penalty: float, optional
        :param stop: Строка, при обнаружении которой в сгенерированном ответе генерация остановится, defaults to []
        :type stop: list, optional
        :param timeout: Максимальное количество секунд ожидания ответа от API, defaults to default['timeout']
        :type timeout: int, optional
        :param max_attempts: Максимальное количество попыток перед тем, как отказаться от генерации ответа, defaults to default['max_attempts']
        :type max_attempts: int, optional
        :param waiting_time: Время ожидания между попытками, defaults to default['waiting_time']
        :type waiting_time: float, optional
         :param exponential_backoff_factor: Коэффициент экспоненциального увеличения времени ожидания между попытками, defaults to default['exponential_backoff_factor']
        :type exponential_backoff_factor: float, optional
        :param n: Количество ответов для генерации, defaults to 1
        :type n: int, optional
        :param echo: Возвращает ли API исходное сообщение, defaults to False
        :type echo: bool, optional
        :return: Словарь, представляющий сгенерированный ответ
        :rtype: dict | None
        """
        def aux_exponential_backoff():
            """
            Вспомогательная функция для экспоненциального увеличения времени ожидания между запросами.
            """
            nonlocal waiting_time
            logger.info(f'Request failed. Waiting {waiting_time} seconds between requests...')
            time.sleep(waiting_time)

            # экспоненциальное увеличение времени ожидания
            waiting_time = waiting_time * exponential_backoff_factor
        
        # настраиваем конфигурации OpenAI для этого клиента.
        self._setup_from_config()
        
        # Адаптируем параметры к типу API, создавая словарь
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
                    logger.debug(f'Sending messages to OpenAI API. Token count={self._count_tokens(current_messages, model)}.')
                except NotImplementedError:
                    logger.debug(f'Token count not implemented for model {model}.')
                
                start_time = time.monotonic()
                logger.debug(f'Calling model with client class {self.__class__.__name__}.')

                ###############################################################
                # вызываем модель, либо из кэша, либо из API
                ###############################################################
                cache_key = str((model, chat_api_params)) # нужен string для hashable
                if self.cache_api_calls and (cache_key in self.api_cache):
                    response = self.api_cache[cache_key]
                else:
                    logger.info(f'Waiting {waiting_time} seconds before next API request (to avoid throttling)...')
                    time.sleep(waiting_time)
                    
                    response = self._raw_model_call(model, chat_api_params)
                    if self.cache_api_calls:
                        self.api_cache[cache_key] = response
                        self._save_cache()
                
                logger.debug(f'Got response from API: {response}')
                end_time = time.monotonic()
                logger.debug(
                    f'Got response in {end_time - start_time:.2f} seconds after {i} attempts.')
                
                return utils.sanitize_dict(self._raw_model_response_extractor(response))

            except InvalidRequestError as e:
                logger.error(f'[{i}] Invalid request error, won\'t retry: {e}')
                # нет смысла повторять, если запрос недействителен
                return None
            
            except openai.BadRequestError as e:
                logger.error(f'[{i}] Invalid request error, won\'t retry: {e}')
                # нет смысла повторять, если запрос недействителен
                return None
            
            except openai.RateLimitError:
                logger.warning(
                    f'[{i}] Rate limit error, waiting a bit and trying again.')
                aux_exponential_backoff()
            
            except NonTerminalError as e:
                logger.error(f'[{i}] Non-terminal error: {e}')
                aux_exponential_backoff()
            
            except Exception as e:
                logger.error(f'[{i}] Error: {e}')

        logger.error(f'Failed to get response after {max_attempts} attempts.')
        return None
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает OpenAI API с заданными параметрами. Подклассы должны
        переопределить этот метод для реализации собственных API-вызовов.
        
        :param model: ID модели для использования.
        :type model: str
        :param chat_api_params: Параметры API-вызова.
        :type chat_api_params: dict
        :return: Ответ от API
        :rtype: dict
        """
        chat_api_params['model'] = model # OpenAI API использует это имя параметра
        return self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API. Подклассы должны
        переопределить этот метод для реализации собственного извлечения ответа.
        
        :param response: Ответ от API.
        :type response: dict
        :return: Извлеченный ответ
        :rtype: dict
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str):
        """
        Подсчитывает количество токенов OpenAI в списке сообщений с помощью tiktoken.
        
        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

        :param messages: Список словарей, представляющих историю разговора.
        :type messages: list
        :param model: Имя модели для использования при кодировании строки.
        :type model: str
        :return: Количество токенов.
        :rtype: int | None
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
        Сохраняет кэш API на диск. Мы используем pickle, потому что некоторые объекты
        не являются JSON сериализуемыми.
        """
        # используем pickle для сохранения кэша
        pickle.dump(self.api_cache, open(self.cache_file_name, 'wb'))

    def _load_cache(self):
        """
        Загружает кэш API с диска.
        """
        # unpickle
        if os.path.exists(self.cache_file_name):
             return pickle.load(open(self.cache_file_name, 'rb'))
        else:
            return {}

    def get_embedding(self, text, model=default['embedding_model']):
        """
        Получает векторное представление заданного текста с помощью указанной модели.
        
        :param text: Текст для получения векторного представления.
        :type text: str
        :param model: Имя модели для использования при встраивании текста, defaults to default['embedding_model']
        :type model: str, optional
        :return: Векторное представление текста
        :rtype: list
        """
        response = self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)
    
    def _raw_embedding_model_call(self, text, model):
        """
        Вызывает OpenAI API для получения векторного представления заданного текста. Подклассы должны
        переопределить этот метод для реализации собственных API-вызовов.

        :param text: Текст для получения векторного представления.
        :type text: str
        :param model: Имя модели для использования при встраивании текста.
        :type model: str
        :return: Ответ от API.
        :rtype: dict
        """
        return self.client.embeddings.create(
            input=[text],
            model=model
        )
    
    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает векторное представление из ответа API. Подклассы должны
        переопределить этот метод для реализации собственного извлечения ответа.

        :param response: Ответ от API.
        :type response: dict
        :return: Векторное представление текста
        :rtype: list
        """
        return response.data[0].embedding

class AzureClient(OpenAIClient):
    """
    Клиент для взаимодействия с Azure OpenAI API.
    
    :param cache_api_calls: Флаг для включения/выключения кэширования API-вызовов, defaults to default['cache_api_calls']
    :type cache_api_calls: bool, optional
    :param cache_file_name: Имя файла для кэширования API-вызовов, defaults to default['cache_file_name']
    :type cache_file_name: str, optional
    """
    def __init__(self, cache_api_calls=default['cache_api_calls'], cache_file_name=default['cache_file_name']) -> None:
        """
        Инициализирует экземпляр класса AzureClient.
        
        :param cache_api_calls: Флаг для включения/выключения кэширования API-вызовов, defaults to default['cache_api_calls']
        :type cache_api_calls: bool, optional
        :param cache_file_name: Имя файла для кэширования API-вызовов, defaults to default['cache_file_name']
        :type cache_file_name: str, optional
        """
        logger.debug('Initializing AzureClient')
        super().__init__(cache_api_calls, cache_file_name)
    
    def _setup_from_config(self):
        """
        Настраивает конфигурации Azure OpenAI Service API для этого клиента,
        включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
                                  api_version=config['OpenAI']['AZURE_API_VERSION'],
                                  api_key=os.getenv('AZURE_OPENAI_KEY'))
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает Azure OpenAI Service API с заданными параметрами.
        
        :param model: ID модели для использования.
        :type model: str
        :param chat_api_params: Параметры API-вызова.
        :type chat_api_params: dict
         :return: Ответ от API.
        :rtype: dict
        """
        chat_api_params['model'] = model
        return self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, возникающее при недействительном запросе к OpenAI API.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, возникающее при неопределенной ошибке, но мы знаем, что можно повторить запрос.
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
    :type client: object
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиента для заданного типа API.
    
    :param api_type: Тип API, для которого нужно получить клиента.
    :type api_type: str
     :raises ValueError: Если тип API не поддерживается
    :return: Клиент для заданного типа API
    :rtype: object
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f'API type {api_type} is not supported. Please check the \'config.ini\' file.')

def client():
    """
    Возвращает клиента для настроенного типа API.

    :return: Клиент для настроенного типа API
    :rtype: object
    """
    api_type = config['OpenAI']['API_TYPE'] if _api_type_override is None else _api_type_override
    
    logger.debug(f'Using  API type {api_type}.')
    return _get_client_for_api_type(api_type)


# TODO simplify the custom configuration methods below

def force_api_type(api_type):
    """
    Принудительно устанавливает использование заданного типа API,
    переопределяя любую другую конфигурацию.
    
    :param api_type: Тип API для использования.
    :type api_type: str
    """
    global _api_type_override
    _api_type_override = api_type

def force_api_cache(cache_api_calls, cache_file_name=default['cache_file_name']):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API,
    переопределяя любую другую конфигурацию.

    :param cache_api_calls: Нужно ли кэшировать вызовы API.
    :type cache_api_calls: bool
    :param cache_file_name: Имя файла для кэширования вызовов API, defaults to default['cache_file_name']
    :type cache_file_name: str, optional
    """
    # устанавливаем параметры кэша для всех клиентов
    for client in _api_type_to_client.values():
        client.set_api_cache(cache_api_calls, cache_file_name)

def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения конфигурации
    по умолчанию для указанного ключа, переопределяя любую другую конфигурацию.
    
    :param key: Ключ для переопределения.
    :type key: str
    :param value: Значение для использования для ключа.
    :type value: any
    :raises ValueError: Если ключ не является допустимым ключом конфигурации.
    """
    global default

    # проверяем, существует ли ключ
    if key in default:
        default[key] = value
    else:
        raise ValueError(f'Key {key} is not a valid configuration key.')

# default client
register_client('openai', OpenAIClient())
register_client('azure', AzureClient())