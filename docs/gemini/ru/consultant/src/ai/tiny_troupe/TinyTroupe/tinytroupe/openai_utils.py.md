# Анализ кода модуля `openai_utils.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разделен на логические блоки.
    - Присутствует класс `LLMCall` для упрощения вызовов языковых моделей.
    - Реализована поддержка кэширования API-вызовов.
    - Поддерживаются различные типы API (OpenAI и Azure).
    - Используется `tiktoken` для подсчета токенов.
    - Присутствует обработка ошибок и повторные попытки вызовов API.
    - Код соответствует PEP8.
    - Добавлены логи для отслеживания процесса выполнения.
-  Минусы
    -  Не все функции и классы имеют docstring в формате reStructuredText.
    -  В некоторых местах используется `try-except` без логирования ошибок через `logger.error`.
    -  Использование `default` как глобального словаря для хранения конфигурации может усложнить понимание кода.
    -  Некоторые комментарии после `#` не несут пользы.
    -  Методы `force_api_type`, `force_api_cache`, `force_default_value` могут быть переработаны для большей гибкости и тестируемости.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить docstring в формате reStructuredText ко всем классам, методам и функциям, включая параметры и возвращаемые значения.
    - Привести комментарии после `#` к более подробному описанию логики.
    
2.  **Обработка ошибок:**
    - Заменить стандартные `try-except` блоки на использование `logger.error` для логирования исключений.
    - В случае `InvalidRequestError` и `openai.BadRequestError` можно добавить дополнительный контекст в сообщение об ошибке.

3.  **Конфигурация:**
    - Рассмотреть возможность использования более гибкого подхода к конфигурации, например, через отдельный класс конфигурации или `dataclass`.

4.  **Рефакторинг:**
    - Упростить методы `force_api_type`, `force_api_cache` и `force_default_value` для большей читаемости и тестируемости.
    - В методе `send_message` вынести общую логику повторных попыток в отдельную функцию.

5.  **Производительность:**
    - Рассмотреть возможность асинхронного выполнения API-вызовов для увеличения производительности.
    - Подумать о замене `time.sleep` на асинхронный эквивалент.
    - Использовать `j_loads` или `j_loads_ns` вместо стандартного `json.load` для загрузки данных.

6. **Комментарии:**
   - Избегать общих фраз, например, 'код исполняет ...'
   - Комментарии должны описывать логику следующего блока кода.
   - Необходимо использовать reStructuredText для docstring и комментариев к функциям, методам и классам.
   - Все комментарии, следующие за `#`, должны быть информативными и описывать логику кода.

**Оптимизиробанный код**
```python
"""
Модуль для взаимодействия с API OpenAI и Azure OpenAI.
=======================================================

Этот модуль предоставляет классы и функции для работы с моделями OpenAI и Azure OpenAI,
включая отправку сообщений, получение эмбеддингов и кэширование API-вызовов.

Пример использования:
--------------------

.. code-block:: python

    from tinytroupe.openai_utils import client, LLMCall

    # Пример вызова LLM
    llm_call = LLMCall(
        system_template_name='system_prompt',
        user_template_name='user_prompt',
        model='gpt-4'
    )
    result = llm_call.call(rendering_configs={'var': 'test'})
    print(result)

    # Пример отправки сообщения
    openai_client = client()
    messages = [{'role': 'user', 'content': 'Hello'}]
    response = openai_client.send_message(messages)
    print(response)
"""
import os
import openai
from openai import OpenAI, AzureOpenAI
import time
import pickle
import logging
import configparser
import tiktoken
from src.utils import jjson
from tinytroupe import utils
from src.logger.logger import logger

# Инициализация логгера
# logger = logging.getLogger("tinytroupe") # перенесено в src/logger/logger.py

# Чтение конфигурационного файла
config = utils.read_config_file()

###########################################################################
# Значения параметров по умолчанию
###########################################################################
default = {}
default["model"] = config["OpenAI"].get("MODEL", "gpt-4")
default["max_tokens"] = int(config["OpenAI"].get("MAX_TOKENS", "1024"))
default["temperature"] = float(config["OpenAI"].get("TEMPERATURE", "0.3"))
default["top_p"] = int(config["OpenAI"].get("TOP_P", "0"))
default["frequency_penalty"] = float(config["OpenAI"].get("FREQ_PENALTY", "0.0"))
default["presence_penalty"] = float(
    config["OpenAI"].get("PRESENCE_PENALTY", "0.0"))
default["timeout"] = float(config["OpenAI"].get("TIMEOUT", "30.0"))
default["max_attempts"] = int(config["OpenAI"].get("MAX_ATTEMPTS", "0"))
default["waiting_time"] = float(config["OpenAI"].get("WAITING_TIME", "0.5"))
default["exponential_backoff_factor"] = float(config["OpenAI"].get("EXPONENTIAL_BACKOFF_FACTOR", "5"))

default["embedding_model"] = config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small")

default["cache_api_calls"] = config["OpenAI"].getboolean("CACHE_API_CALLS", False)
default["cache_file_name"] = config["OpenAI"].get("CACHE_FILE_NAME", "openai_api_cache.pickle")

###########################################################################
# Вспомогательные классы для вызова моделей
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

        :param system_template_name: Имя системного шаблона.
        :type system_template_name: str
        :param user_template_name: Имя пользовательского шаблона (может быть None).
        :type user_template_name: str
        :param model_params: Параметры модели.
        :type model_params: dict
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
    
    def call(self, **rendering_configs):
        """
        Вызывает LLM модель с указанными конфигурациями рендеринга.

        :param rendering_configs: Конфигурации рендеринга.
        :type rendering_configs: dict
        :return: Содержание ответа модели или None в случае ошибки.
        :rtype: str or None
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

        :return: Строковое представление объекта.
        :rtype: str
        """
        return f"LLMCall(messages={self.messages}, model_config={self.model_params}, model_output={self.model_output})"


###########################################################################
# Класс клиента
###########################################################################

class OpenAIClient:
    """
    Класс-утилита для взаимодействия с API OpenAI.
    """

    def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None:
        """
        Инициализирует OpenAIClient.

        :param cache_api_calls: Флаг, указывающий, кэшировать ли вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        logger.debug("Initializing OpenAIClient")

        # Установка параметров кэширования API
        self.set_api_cache(cache_api_calls, cache_file_name)
    
    def set_api_cache(self, cache_api_calls, cache_file_name=default["cache_file_name"]):
        """
        Включает или отключает кэширование вызовов API.

        :param cache_api_calls: Флаг, указывающий, кэшировать ли вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = cache_file_name
        if self.cache_api_calls:
            # загрузка кэша, если он есть
            self.api_cache = self._load_cache()
    
    
    def _setup_from_config(self):
        """
        Настраивает API OpenAI для этого клиента.
        """
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def send_message(self,
                    current_messages,
                     model=default["model"],
                     temperature=default["temperature"],
                     max_tokens=default["max_tokens"],
                     top_p=default["top_p"],
                     frequency_penalty=default["frequency_penalty"],
                     presence_penalty=default["presence_penalty"],
                     stop=[],
                     timeout=default["timeout"],
                     max_attempts=default["max_attempts"],
                     waiting_time=default["waiting_time"],
                     exponential_backoff_factor=default["exponential_backoff_factor"],
                     n = 1,
                     echo=False):
        """
        Отправляет сообщение в API OpenAI и возвращает ответ.

        :param current_messages: Список словарей, представляющих историю разговора.
        :type current_messages: list
        :param model: Идентификатор модели для генерации ответа.
        :type model: str
        :param temperature: Управляет "креативностью" ответа. Более высокие значения приводят к более разнообразным ответам.
        :type temperature: float
        :param max_tokens: Максимальное количество токенов (слов или знаков препинания) для генерации в ответе.
        :type max_tokens: int
        :param top_p: Управляет "качеством" ответа. Более высокие значения приводят к более связным ответам.
        :type top_p: float
        :param frequency_penalty: Управляет "повторением" ответа. Более высокие значения приводят к меньшему повторению.
        :type frequency_penalty: float
        :param presence_penalty: Управляет "разнообразием" ответа. Более высокие значения приводят к более разнообразным ответам.
        :type presence_penalty: float
        :param stop: Строка, которая, если встречается в сгенерированном ответе, вызывает остановку генерации.
        :type stop: list
        :param timeout: Максимальное количество секунд ожидания ответа от API.
        :type timeout: int
        :param max_attempts: Максимальное количество попыток до отказа от генерации ответа.
        :type max_attempts: int
        :param waiting_time: Время ожидания между повторными попытками.
        :type waiting_time: int
        :param exponential_backoff_factor: Коэффициент экспоненциального увеличения времени ожидания между повторными попытками.
        :type exponential_backoff_factor: float
        :param n: Количество сгенерированных ответов.
        :type n: int
        :param echo: Возвращать ли входящее сообщение в ответе.
        :type echo: bool
        :return: Словарь, представляющий сгенерированный ответ, или None в случае ошибки.
        :rtype: dict or None
        """

        def aux_exponential_backoff():
            """
            Вспомогательная функция для реализации экспоненциального отката.
            """
            nonlocal waiting_time
            logger.info(f"Request failed. Waiting {waiting_time} seconds between requests...")
            time.sleep(waiting_time)

            # экспоненциальный откат
            waiting_time = waiting_time * exponential_backoff_factor
        
        # Настройка конфигурации OpenAI для этого клиента.
        self._setup_from_config()
        
        # Адаптируем параметры к типу API
        chat_api_params = {
            "messages": current_messages,
            "temperature": temperature,
            "max_tokens":max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
            "stop": stop,
            "timeout": timeout,
            "stream": False,
            "n": n,
        }


        i = 0
        while i < max_attempts:
            i += 1
            try:
                try:
                    logger.debug(f"Sending messages to OpenAI API. Token count={self._count_tokens(current_messages, model)}.")
                except NotImplementedError:
                    logger.debug(f"Token count not implemented for model {model}.")
                    
                start_time = time.monotonic()
                logger.debug(f"Calling model with client class {self.__class__.__name__}.")

                ###############################################################
                # Вызов модели, из кэша или из API
                ###############################################################
                cache_key = str((model, chat_api_params)) # need string to be hashable
                if self.cache_api_calls and (cache_key in self.api_cache):
                    response = self.api_cache[cache_key]
                else:
                     # Ожидание перед следующим запросом, для избежания троттлинга
                    logger.info(f"Waiting {waiting_time} seconds before next API request (to avoid throttling)...")
                    time.sleep(waiting_time)
                    
                    response = self._raw_model_call(model, chat_api_params)
                    if self.cache_api_calls:
                        self.api_cache[cache_key] = response
                        self._save_cache()
                
                
                logger.debug(f"Got response from API: {response}")
                end_time = time.monotonic()
                logger.debug(
                    f"Got response in {end_time - start_time:.2f} seconds after {i} attempts.")

                return utils.sanitize_dict(self._raw_model_response_extractor(response))

            except openai.APIError as e:
               logger.error(f"[{i}] OpenAI API error: {e}")
               aux_exponential_backoff()

            except openai.RateLimitError:
                logger.warning(
                    f"[{i}] Rate limit error, waiting a bit and trying again.")
                aux_exponential_backoff()

            except InvalidRequestError as e:
                logger.error(f"[{i}] Invalid request error, won't retry: {e}")
                # нет смысла повторять если запрос не валидный
                return None
            
            except openai.BadRequestError as e:
                logger.error(f"[{i}] Bad request error, won't retry: {e}")
                return None
            
            except NonTerminalError as e:
                logger.error(f"[{i}] Non-terminal error: {e}")
                aux_exponential_backoff()
                
            except Exception as e:
                logger.error(f"[{i}] Error: {e}")

        logger.error(f"Failed to get response after {max_attempts} attempts.")
        return None
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает API OpenAI с заданными параметрами.

        Подклассы должны переопределить этот метод, чтобы реализовать свои собственные вызовы API.

        :param model: Идентификатор модели.
        :type model: str
        :param chat_api_params: Параметры вызова API.
        :type chat_api_params: dict
        :return: Ответ от API OpenAI.
        :rtype: openai.ChatCompletion
        """
        
        chat_api_params["model"] = model # OpenAI API uses this parameter name
        return self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API.

        Подклассы должны переопределить этот метод, чтобы реализовать свое собственное извлечение ответа.

        :param response: Ответ от API.
        :type response: openai.ChatCompletion
        :return: Извлеченный ответ.
        :rtype: dict
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str):
        """
        Подсчитывает количество токенов OpenAI в списке сообщений с использованием tiktoken.

        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

        :param messages: Список словарей, представляющих историю разговора.
        :type messages: list
        :param model: Имя модели для кодирования строки.
        :type model: str
        :return: Количество токенов или None в случае ошибки.
        :rtype: int or None
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
                tokens_per_message = 4  # каждое сообщение следует <|start|>{role/name}\\n{content}<|end|>\\n
                tokens_per_name = -1  # если есть имя, роль опускается
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
            num_tokens += 3  # каждый ответ начинается с <|start|>assistant<|message|>
            return num_tokens
        
        except Exception as e:
            logger.error(f"Error counting tokens: {e}")
            return None

    def _save_cache(self):
        """
        Сохраняет кэш API на диск.
        """
        # используем pickle для сохранения кэша
        pickle.dump(self.api_cache, open(self.cache_file_name, "wb"))

    
    def _load_cache(self):
        """
        Загружает кэш API с диска.
        """
        # десериализация pickle
        return pickle.load(open(self.cache_file_name, "rb")) if os.path.exists(self.cache_file_name) else {}

    def get_embedding(self, text, model=default["embedding_model"]):
        """
        Получает эмбеддинг заданного текста с использованием указанной модели.

        :param text: Текст для эмбеддинга.
        :type text: str
        :param model: Имя модели для эмбеддинга текста.
        :type model: str
        :return: Эмбеддинг текста.
        :rtype: list
        """
        response = self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)
    
    def _raw_embedding_model_call(self, text, model):
        """
        Вызывает API OpenAI для получения эмбеддинга заданного текста.

        Подклассы должны переопределить этот метод, чтобы реализовать свои собственные вызовы API.

        :param text: Текст для эмбеддинга.
        :type text: str
        :param model: Имя модели для эмбеддинга текста.
        :type model: str
        :return: Ответ от API OpenAI.
        :rtype: openai.Embedding
        """
        return self.client.embeddings.create(
            input=[text],
            model=model
        )
    
    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает эмбеддинг из ответа API.

        Подклассы должны переопределить этот метод, чтобы реализовать свое собственное извлечение эмбеддинга.

        :param response: Ответ от API.
        :type response: openai.Embedding
        :return: Эмбеддинг текста.
        :rtype: list
        """
        return response.data[0].embedding

class AzureClient(OpenAIClient):
    """
    Класс-утилита для взаимодействия с API Azure OpenAI Service.
    """

    def __init__(self, cache_api_calls=default["cache_api_calls"], cache_file_name=default["cache_file_name"]) -> None:
        """
        Инициализирует AzureClient.

        :param cache_api_calls: Флаг, указывающий, кэшировать ли вызовы API.
        :type cache_api_calls: bool
        :param cache_file_name: Имя файла для кэширования API-вызовов.
        :type cache_file_name: str
        """
        logger.debug("Initializing AzureClient")

        super().__init__(cache_api_calls, cache_file_name)
    
    def _setup_from_config(self):
        """
        Настраивает API Azure OpenAI Service для этого клиента, включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint= os.getenv("AZURE_OPENAI_ENDPOINT"),
                                  api_version = config["OpenAI"]["AZURE_API_VERSION"],
                                  api_key = os.getenv("AZURE_OPENAI_KEY"))
    
    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает API Azure OpenAI Service с заданными параметрами.
        
        :param model: Идентификатор модели.
        :type model: str
        :param chat_api_params: Параметры вызова API.
        :type chat_api_params: dict
        :return: Ответ от API Azure OpenAI.
        :rtype: openai.ChatCompletion
        """
        chat_api_params["model"] = model 

        return self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, которое возникает, когда запрос к API OpenAI недействителен.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, которое возникает, когда происходит неуказанная ошибка, но мы знаем, что можно повторить попытку.
    """
    pass

###########################################################################
# Реестр клиентов
#
# У нас могут быть разные клиенты, поэтому нам нужно место для их
# регистрации и получения при необходимости.
#
# По умолчанию мы поддерживаем API OpenAI и Azure OpenAI Service.
# Таким образом, нам нужно установить параметры API на основе выбора пользователя.
# Это делается внутри специализированных классов.
#
# Также можно зарегистрировать собственные клиенты для доступа к внутренним или
# нестандартным конечным точкам API.
###########################################################################
_api_type_to_client = {}
_api_type_override = None

def register_client(api_type, client):
    """
    Регистрирует клиента для заданного типа API.

    :param api_type: Тип API, для которого мы хотим зарегистрировать клиента.
    :type api_type: str
    :param client: Клиент для регистрации.
    :type client: object
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиента для заданного типа API.

    :param api_type: Тип API, для которого мы хотим получить клиента.
    :type api_type: str
    :raises ValueError: Если тип API не поддерживается.
    :return: Клиент для заданного типа API.
    :rtype: object
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f"API type {api_type} is not supported. Please check the 'config.ini' file.")

def client():
    """
    Возвращает клиента для настроенного типа API.

    :return: Клиент для настроенного типа API.
    :rtype: object
    """
    api_type = config["OpenAI"]["API_TYPE"] if _api_type_override is None else _api_type_override
    
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

def force_api_cache(cache_api_calls, cache_file_name=default["cache_file_name"]):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API, переопределяя любую другую конфигурацию.

    :param cache_api_calls: Следует ли кэшировать вызовы API.
    :type cache_api_calls: bool
    :param cache_file_name: Имя файла для использования для кэширования вызовов API.
    :type cache_file_name: str
    """
    # установка параметров кэша для всех клиентов
    for client in _api_type_to_client.values():
        client.set_api_cache(cache_api_calls, cache_file_name)

def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения конфигурации по умолчанию для указанного ключа, переопределяя любую другую конфигурацию.

    :param key: Ключ для переопределения.
    :type key: str
    :param value: Значение для использования для ключа.
    :type value: Any
    :raises ValueError: Если ключ не является допустимым ключом конфигурации.
    """
    global default

    # Проверка наличия ключа
    if key in default:
        default[key] = value
    else:
        raise ValueError(f"Key {key} is not a valid configuration key.")

# Регистрация клиентов по умолчанию
register_client("openai", OpenAIClient())
register_client("azure", AzureClient())