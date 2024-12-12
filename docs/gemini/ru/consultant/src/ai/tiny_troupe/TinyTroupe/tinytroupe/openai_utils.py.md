# Анализ кода модуля `openai_utils.py`

**Качество кода**
7
-  Плюсы
    -  Код хорошо структурирован и разбит на логические блоки, такие как настройки по умолчанию, классы клиентов и вспомогательные функции.
    -  Используется логирование для отслеживания ошибок и отладки.
    -  Реализована поддержка кэширования API-вызовов для экономии ресурсов.
    -  Присутствует обработка ошибок, включая `InvalidRequestError`, `RateLimitError` и `NonTerminalError`.
    -  Реализована поддержка различных API (OpenAI, Azure).
-  Минусы
    -  Некоторые docstring не полные, нет описания аргументов и возвращаемых значений.
    -  Используется глобальная переменная `default` для хранения настроек по умолчанию, что может усложнить отладку и поддержку.
    -  В некоторых местах используется стандартный блок `try-except` вместо `logger.error` для обработки ошибок.
    -  Не все функции имеют документацию в формате reStructuredText (RST).
    -  Метод `force_default_value` изменяет глобальную переменную `default`, что может привести к проблемам при параллельном выполнении кода.
    -  Используются устаревшие подходы к форматированию строк (например, `f"Got response in {end_time - start_time:.2f} seconds after {i + 1} attempts."`).

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить подробные описания параметров и возвращаемых значений в docstring всех функций и методов, используя reStructuredText (RST).
    -   Заменить общие фразы типа `A class that represents an LLM model call.` на более конкретные.
2.  **Обработка ошибок**:
    -   Использовать `logger.error` для обработки ошибок вместо стандартных блоков `try-except`, где это возможно.
    -   Предоставить более информативные сообщения об ошибках.
3.  **Глобальные переменные**:
    -   Избегать использования глобальной переменной `default` для хранения настроек по умолчанию. Рассмотреть возможность использования dataclass или config-объекта.
4.  **Форматирование строк**:
     - Использовать f-строки в местах где используется форматирование строк, к примеру `f"Got response in {end_time - start_time:.2f} seconds after {i + 1} attempts."` -> `f"Got response in {end_time - start_time:.2f} seconds after {i} attempts."`
5.  **Рефакторинг**:
    -   Упростить логику в `_count_tokens`, выделив повторяющиеся части в отдельные функции или константы.
    -   Разделить функцию `send_message` на несколько более мелких, для улучшения читаемости.
    -   Перенести логику установки параметров клиента в отдельный метод.
6. **Кэширование**:
     - Добавить возможность отключения кэширования через параметры в конструкторе класса `OpenAIClient`.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с OpenAI API.
=========================================================================================

Этот модуль предоставляет классы и функции для работы с OpenAI API,
включая поддержку кэширования, подсчета токенов и различных моделей.

Он включает классы :class:`LLMCall`, :class:`OpenAIClient` и :class:`AzureClient`,
которые обеспечивают взаимодействие с API OpenAI и Azure OpenAI.

Пример использования
--------------------

Пример использования класса `OpenAIClient`:

.. code-block:: python

    from tinytroupe.openai_utils import OpenAIClient

    client = OpenAIClient()
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    response = client.send_message(messages)
    if response:
        print(response['content'])
"""
import os
import openai
from openai import OpenAI, AzureOpenAI
import time
import json
import pickle
import logging
import configparser
import tiktoken
from tinytroupe import utils
from src.logger.logger import logger # импортируем logger

# We'll use various configuration elements below
config = utils.read_config_file()

###########################################################################
# Default parameter values
###########################################################################
_default = { # Изменили имя глобальной переменной чтобы небыло конфликта с default
    "model": config["OpenAI"].get("MODEL", "gpt-4"),
    "max_tokens": int(config["OpenAI"].get("MAX_TOKENS", "1024")),
    "temperature": float(config["OpenAI"].get("TEMPERATURE", "0.3")),
    "top_p": int(config["OpenAI"].get("TOP_P", "0")),
    "frequency_penalty": float(config["OpenAI"].get("FREQ_PENALTY", "0.0")),
    "presence_penalty": float(config["OpenAI"].get("PRESENCE_PENALTY", "0.0")),
    "timeout": float(config["OpenAI"].get("TIMEOUT", "30.0")),
    "max_attempts": int(config["OpenAI"].get("MAX_ATTEMPTS", "3")),
    "waiting_time": float(config["OpenAI"].get("WAITING_TIME", "0.5")),
    "exponential_backoff_factor": float(config["OpenAI"].get("EXPONENTIAL_BACKOFF_FACTOR", "5")),
    "embedding_model": config["OpenAI"].get("EMBEDDING_MODEL", "text-embedding-3-small"),
    "cache_api_calls": config["OpenAI"].getboolean("CACHE_API_CALLS", False),
    "cache_file_name": config["OpenAI"].get("CACHE_FILE_NAME", "openai_api_cache.pickle")
}

###########################################################################
# Model calling helpers
###########################################################################

class LLMCall:
    """
    Представляет вызов языковой модели (LLM).

    Хранит входные сообщения, конфигурацию модели и вывод модели.
    """
    def __init__(self, system_template_name: str, user_template_name: str = None, **model_params):
        """
        Инициализирует экземпляр LLMCall с указанными системными и пользовательскими шаблонами.

        :param system_template_name: Имя системного шаблона.
        :param user_template_name: Имя пользовательского шаблона.
        :param model_params: Параметры модели.
        """
        self.system_template_name = system_template_name
        self.user_template_name = user_template_name
        self.model_params = model_params
        self.messages = None
        self.model_output = None

    def call(self, **rendering_configs):
        """
        Вызывает языковую модель с указанными настройками рендеринга.

        :param rendering_configs: Настройки рендеринга.
        :return: Содержимое ответа модели или None в случае ошибки.
        """
        self.messages = utils.compose_initial_LLM_messages_with_templates(self.system_template_name, self.user_template_name, rendering_configs)

        # вызываем языковую модель
        self.model_output = client().send_message(self.messages, **self.model_params)

        if 'content' in self.model_output:
            return self.model_output['content']
        else:
            logger.error(f"Model output does not contain 'content' key: {self.model_output}") # Используем logger.error для логирования ошибки
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

    def __init__(self, cache_api_calls=_default["cache_api_calls"], cache_file_name=_default["cache_file_name"]) -> None:
        """
        Инициализирует класс OpenAIClient.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :param cache_file_name: Имя файла для кэширования вызовов API.
        """
        logger.debug("Initializing OpenAIClient")

        # определяем, нужно ли кэшировать вызовы API
        self.set_api_cache(cache_api_calls, cache_file_name)
        self.client = None


    def set_api_cache(self, cache_api_calls, cache_file_name=_default["cache_file_name"]):
        """
        Включает или отключает кэширование вызовов API.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :param cache_file_name: Имя файла для кэширования вызовов API.
        """
        self.cache_api_calls = cache_api_calls
        self.cache_file_name = cache_file_name
        if self.cache_api_calls:
            # загружаем кэш, если он есть
            self.api_cache = self._load_cache()
        else:
            self.api_cache = {}



    def _setup_from_config(self):
        """
        Настраивает конфигурации OpenAI API для этого клиента.
        """
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def send_message(self,
                    current_messages,
                     model=_default["model"],
                     temperature=_default["temperature"],
                     max_tokens=_default["max_tokens"],
                     top_p=_default["top_p"],
                     frequency_penalty=_default["frequency_penalty"],
                     presence_penalty=_default["presence_penalty"],
                     stop=None,
                     timeout=_default["timeout"],
                     max_attempts=_default["max_attempts"],
                     waiting_time=_default["waiting_time"],
                     exponential_backoff_factor=_default["exponential_backoff_factor"],
                     n=1,
                     echo=False):
        """
        Отправляет сообщение в OpenAI API и возвращает ответ.

        :param current_messages: Список словарей, представляющих историю разговора.
        :param model: Идентификатор модели для генерации ответа.
        :param temperature: Контролирует "креативность" ответа. Более высокие значения приводят к более разнообразным ответам.
        :param max_tokens: Максимальное количество токенов для генерации в ответе.
        :param top_p: Контролирует "качество" ответа. Более высокие значения приводят к более связным ответам.
        :param frequency_penalty: Контролирует "повторение" ответа. Более высокие значения приводят к меньшему повторению.
        :param presence_penalty: Контролирует "разнообразие" ответа. Более высокие значения приводят к более разнообразным ответам.
        :param stop: Строка, которая, если встречается в сгенерированном ответе, вызывает остановку генерации.
        :param timeout: Максимальное количество секунд ожидания ответа от API.
        :param max_attempts: Максимальное количество попыток сделать запрос к API.
        :param waiting_time: Время ожидания между попытками запроса.
        :param exponential_backoff_factor: Коэффициент экспоненциальной задержки.
        :param n: Количество сгенерированных ответов.
        :param echo: Флаг, указывающий, нужно ли возвращать входное сообщение в ответе.
        :return: Словарь, представляющий сгенерированный ответ или None в случае ошибки.
        """
        if stop is None:
            stop = []


        def aux_exponential_backoff():
            nonlocal waiting_time
            logger.info(f"Request failed. Waiting {waiting_time} seconds between requests...")
            time.sleep(waiting_time)

            # экспоненциальное увеличение времени ожидания
            waiting_time = waiting_time * exponential_backoff_factor


        # настраиваем конфигурации OpenAI для этого клиента
        self._setup_from_config()

        # Адаптируем параметры к типу API, поэтому сначала создаем словарь с ними
        chat_api_params = {
            "messages": current_messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
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
                # вызываем модель, либо из кэша, либо из API
                ###############################################################
                cache_key = str((model, chat_api_params))  # приводим к строке, чтобы было хэшируемым
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
                logger.debug(f"Got response in {end_time - start_time:.2f} seconds after {i} attempts.")

                return utils.sanitize_dict(self._raw_model_response_extractor(response))

            except InvalidRequestError as e:
                logger.error(f"[{i}] Invalid request error, won't retry: {e}") # используем logger.error для вывода ошибки

                # нет смысла повторять запрос, если он недействителен
                return None

            except openai.BadRequestError as e:
                logger.error(f"[{i}] Invalid request error, won't retry: {e}") # используем logger.error для вывода ошибки

                # нет смысла повторять запрос, если он недействителен
                return None

            except openai.RateLimitError:
                logger.warning(f"[{i}] Rate limit error, waiting a bit and trying again.")
                aux_exponential_backoff()

            except NonTerminalError as e:
                logger.error(f"[{i}] Non-terminal error: {e}") # используем logger.error для вывода ошибки
                aux_exponential_backoff()

            except Exception as e:
                 logger.error(f"[{i}] Error: {e}") # используем logger.error для вывода ошибки


        logger.error(f"Failed to get response after {max_attempts} attempts.") # используем logger.error для вывода ошибки
        return None


    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает OpenAI API с заданными параметрами.

        Подклассы должны переопределить этот метод, чтобы реализовать свои собственные вызовы API.

        :param model: Идентификатор модели для вызова API.
        :param chat_api_params: Параметры вызова API.
        :return: Ответ от API.
        """
        chat_api_params["model"] = model # OpenAI API использует это имя параметра
        return self.client.chat.completions.create(
                    **chat_api_params
                )

    def _raw_model_response_extractor(self, response):
        """
        Извлекает ответ из ответа API.

        Подклассы должны переопределить этот метод, чтобы реализовать извлечение ответа.

        :param response: Ответ от API.
        :return: Извлеченный ответ.
        """
        return response.choices[0].message.to_dict()

    def _count_tokens(self, messages: list, model: str):
        """
        Подсчитывает количество токенов OpenAI в списке сообщений, используя tiktoken.

        Адаптировано из https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

        :param messages: Список словарей, представляющих историю разговора.
        :param model: Имя модели для кодирования строки.
        :return: Количество токенов или None в случае ошибки.
        """
        try:
            try:
                encoding = tiktoken.encoding_for_model(model)
            except KeyError:
                logger.debug("Token count: model not found. Using cl100k_base encoding.")
                encoding = tiktoken.get_encoding("cl100k_base")

            tokens_per_message = 3
            tokens_per_name = 1

            if model in {
                "gpt-3.5-turbo-0613",
                "gpt-3.5-turbo-16k-0613",
                "gpt-4-0314",
                "gpt-4-32k-0314",
                "gpt-4-0613",
                "gpt-4-32k-0613",
            }:
                pass # токены на сообщение и имя не меняются
            elif model == "gpt-3.5-turbo-0301":
                 tokens_per_message = 4  # каждое сообщение имеет формат <|start|>{role/name}\n{content}<|end|>\n
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
            num_tokens += 3 # каждый ответ начинается с <|start|>assistant<|message|>
            return num_tokens

        except Exception as e:
            logger.error(f"Error counting tokens: {e}") # используем logger.error для вывода ошибки
            return None

    def _save_cache(self):
        """
        Сохраняет кэш API на диск.

        Использует pickle, так как некоторые объекты не сериализуются в JSON.
        """
        # используем pickle для сохранения кэша
        try:
            pickle.dump(self.api_cache, open(self.cache_file_name, "wb"))
        except Exception as e:
            logger.error(f"Error saving cache: {e}") # используем logger.error для вывода ошибки

    def _load_cache(self):
        """
        Загружает кэш API с диска.

        :return: Загруженный кэш или пустой словарь, если кэш отсутствует.
        """
        # распаковываем
        try:
           if os.path.exists(self.cache_file_name):
                return pickle.load(open(self.cache_file_name, "rb"))
           else:
               return {}
        except Exception as e:
            logger.error(f"Error loading cache: {e}") # используем logger.error для вывода ошибки
            return {}


    def get_embedding(self, text, model=_default["embedding_model"]):
        """
        Получает эмбеддинг заданного текста, используя указанную модель.

        :param text: Текст для получения эмбеддинга.
        :param model: Имя модели для эмбеддинга текста.
        :return: Эмбеддинг текста.
        """
        response = self._raw_embedding_model_call(text, model)
        return self._raw_embedding_model_response_extractor(response)

    def _raw_embedding_model_call(self, text, model):
        """
        Вызывает OpenAI API для получения эмбеддинга заданного текста.

        Подклассы должны переопределить этот метод, чтобы реализовать свои собственные вызовы API.

        :param text: Текст для получения эмбеддинга.
        :param model: Имя модели для эмбеддинга текста.
        :return: Ответ от API.
        """
        return self.client.embeddings.create(
            input=[text],
            model=model
        )

    def _raw_embedding_model_response_extractor(self, response):
        """
        Извлекает эмбеддинг из ответа API.

         Подклассы должны переопределить этот метод, чтобы реализовать извлечение эмбеддинга.

        :param response: Ответ от API.
        :return: Эмбеддинг текста.
        """
        return response.data[0].embedding


class AzureClient(OpenAIClient):
    """
    Клиент для взаимодействия с Azure OpenAI Service API.
    """
    def __init__(self, cache_api_calls=_default["cache_api_calls"], cache_file_name=_default["cache_file_name"]) -> None:
        """
        Инициализирует класс AzureClient.

        :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
        :param cache_file_name: Имя файла для кэширования вызовов API.
        """
        logger.debug("Initializing AzureClient")
        super().__init__(cache_api_calls, cache_file_name)

    def _setup_from_config(self):
        """
        Настраивает конфигурации Azure OpenAI Service API для этого клиента,
        включая конечную точку API и ключ.
        """
        self.client = AzureOpenAI(azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                                  api_version=config["OpenAI"]["AZURE_API_VERSION"],
                                  api_key=os.getenv("AZURE_OPENAI_KEY"))

    def _raw_model_call(self, model, chat_api_params):
        """
        Вызывает Azure OpenAI Service API с заданными параметрами.

        :param model: Идентификатор модели для вызова API.
        :param chat_api_params: Параметры вызова API.
        :return: Ответ от API.
        """
        chat_api_params["model"] = model

        return self.client.chat.completions.create(
                    **chat_api_params
                )


class InvalidRequestError(Exception):
    """
    Исключение, возникающее при недопустимом запросе к OpenAI API.
    """
    pass

class NonTerminalError(Exception):
    """
    Исключение, возникающее при некритической ошибке, которую можно повторить.
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
    Регистрирует клиент для заданного типа API.

    :param api_type: Тип API, для которого регистрируется клиент.
    :param client: Клиент для регистрации.
    """
    _api_type_to_client[api_type] = client

def _get_client_for_api_type(api_type):
    """
    Возвращает клиент для заданного типа API.

    :param api_type: Тип API, для которого нужно получить клиент.
    :return: Клиент для заданного типа API.
    """
    try:
        return _api_type_to_client[api_type]
    except KeyError:
        raise ValueError(f"API type {api_type} is not supported. Please check the 'config.ini' file.")

def client():
    """
    Возвращает клиент для настроенного типа API.

    :return: Клиент для настроенного типа API.
    """
    api_type = config["OpenAI"]["API_TYPE"] if _api_type_override is None else _api_type_override

    logger.debug(f"Using  API type {api_type}.")
    return _get_client_for_api_type(api_type)


# TODO simplify the custom configuration methods below

def force_api_type(api_type):
    """
    Принудительно устанавливает использование заданного типа API, переопределяя любую другую конфигурацию.

    :param api_type: Тип API для использования.
    """
    global _api_type_override
    _api_type_override = api_type

def force_api_cache(cache_api_calls, cache_file_name=_default["cache_file_name"]):
    """
    Принудительно устанавливает использование заданной конфигурации кэша API,
    переопределяя любую другую конфигурацию.

    :param cache_api_calls: Флаг, указывающий, следует ли кэшировать вызовы API.
    :param cache_file_name: Имя файла для кэширования вызовов API.
    """
    # устанавливаем параметры кэша для всех клиентов
    for client in _api_type_to_client.values():
         client.set_api_cache(cache_api_calls, cache_file_name)


def force_default_value(key, value):
    """
    Принудительно устанавливает использование заданного значения по умолчанию
    для указанного ключа, переопределяя любую другую конфигурацию.

    :param key: Ключ для переопределения.
    :param value: Значение для использования для ключа.
    """
    # проверяем, существует ли ключ
    if key in _default:
        _default[key] = value
    else:
        raise ValueError(f"Key {key} is not a valid configuration key.")

# default client
register_client("openai", OpenAIClient())
register_client("azure", AzureClient())