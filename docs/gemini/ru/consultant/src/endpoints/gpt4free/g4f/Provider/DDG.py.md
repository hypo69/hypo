### **Анализ кода модуля `DDG.py`**

**Расположение файла:** `hypotez/src/endpoints/gpt4free/g4f/Provider/DDG.py`

Модуль предназначен для взаимодействия с DuckDuckGo AI Chat в рамках проекта `hypotez`. Он предоставляет функциональность для генерации текста через асинхронные запросы к API DuckDuckGo.

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Асинхронная обработка запросов.
  - Реализована поддержка stream ответов.
  - Реализована логика повторных попыток при сбоях и rate limiting.
  - Класс `Conversation` для хранения состояния диалога.
- **Минусы**:
  - Местами отсутствует подробная документация.
  - Не все переменные аннотированы типами.
  - В коде присутствует много `try-except` блоков без логирования ошибок.
  - Используются устаревшие конструкции, например, `"".join(...)` вместо f-string.

**Рекомендации по улучшению:**

1. **Добавить документацию**:
   - Дополнить docstring для классов `DuckDuckGoSearchException` и `Conversation`.
   - Описать параметры и возвращаемые значения для всех методов.
   - Добавить примеры использования для основных методов.

2. **Обработка исключений и логирование**:
   - Добавить логирование ошибок во всех блоках `except`, чтобы упростить отладку и мониторинг.
   - Использовать `logger.error` с передачей исключения `ex` и `exc_info=True`.

3. **Улучшение читаемости**:
   - Использовать f-string для конкатенации строк.
   - Добавить аннотации типов для всех переменных и параметров функций.
   - Устранить дублирование кода, например, при обработке ошибок `RateLimitError`.

4. **Безопасность**:
   - Рассмотреть возможность использования более надежных способов хранения и передачи секретных данных, если таковые используются.

5. **Совместимость**:
   - Проверить совместимость с различными версиями библиотек, особенно `bs4`, и добавить соответствующие проверки.

6. **Производительность**:
   - Оптимизировать парсинг HTML, если это узкое место, например, с помощью `lxml` вместо стандартного `html.parser`.

**Оптимизированный код:**

```python
from __future__ import annotations

import time
import asyncio
import random
import base64
import hashlib
import json
from typing import AsyncGenerator, Optional, List, Dict, Tuple

from aiohttp import ClientSession, ClientTimeout
from yarl import URL

from ..typing import AsyncResult, Messages, Cookies
from ..requests.raise_for_status import raise_for_status
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin
from .helper import format_prompt, get_last_user_message
from ..providers.response import FinishReason, JsonConversation
from ..errors import ModelNotSupportedError, ResponseStatusError, RateLimitError, TimeoutError, ConversationLimitError
from src.logger import logger

try:
    from bs4 import BeautifulSoup

    has_bs4 = True
except ImportError:
    has_bs4 = False


class DuckDuckGoSearchException(Exception):
    """
    Исключение, специфичное для ошибок поиска DuckDuckGo.
    """

class Conversation(JsonConversation):
    """
    Класс для хранения состояния диалога с DuckDuckGo AI Chat.
    """
    vqd: Optional[str] = None
    vqd_hash_1: Optional[str] = None
    message_history: Messages = []
    cookies: Dict = {}
    fe_version: Optional[str] = None

    def __init__(self, model: str):
        """
        Инициализирует объект Conversation.

        Args:
            model (str): Название используемой модели.
        """
        self.model = model


class DDG(AsyncGeneratorProvider, ProviderModelMixin):
    """
    Провайдер для взаимодействия с DuckDuckGo AI Chat.
    """
    label: str = "DuckDuckGo AI Chat"
    url: str = "https://duckduckgo.com/aichat"
    api_endpoint: str = "https://duckduckgo.com/duckchat/v1/chat"
    status_url: str = "https://duckduckgo.com/duckchat/v1/status"

    working: bool = True
    supports_stream: bool = True
    supports_system_message: bool = True
    supports_message_history: bool = True

    default_model: str = "gpt-4o-mini"
    models: List[str] = [default_model, "meta-llama/Llama-3.3-70B-Instruct-Turbo", "claude-3-haiku-20240307", "o3-mini", "mistralai/Mistral-Small-24B-Instruct-2501"]

    model_aliases: Dict[str, str] = {
        "gpt-4": "gpt-4o-mini",
        "llama-3.3-70b": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "claude-3-haiku": "claude-3-haiku-20240307",
        "mixtral-small-24b": "mistralai/Mistral-Small-24B-Instruct-2501",
    }

    last_request_time: float = 0
    max_retries: int = 3
    base_delay: int = 2

    # Class variable to store the x-fe-version across instances
    _chat_xfe: str = ""

    @staticmethod
    def sha256_base64(text: str) -> str:
        """
        Возвращает base64-представление SHA256-хеша текста.

        Args:
            text (str): Исходный текст.

        Returns:
            str: Base64-представление SHA256-хеша.
        """
        sha256_hash = hashlib.sha256(text.encode("utf-8")).digest()
        return base64.b64encode(sha256_hash).decode()

    @staticmethod
    def parse_dom_fingerprint(js_text: str) -> str:
        """
        Извлекает отпечаток DOM из JavaScript-текста.

        Args:
            js_text (str): JavaScript-текст, содержащий HTML-фрагмент.

        Returns:
            str: Отпечаток DOM в виде строки.
        """
        if not has_bs4:
            # Fallback if BeautifulSoup is not available
            return "1000"

        try:
            html_snippet = js_text.split("e.innerHTML = \'")[1].split("\';")[0]
            offset_value = js_text.split("return String(")[1].split(" ")[0]
            soup = BeautifulSoup(html_snippet, "html.parser")
            corrected_inner_html = soup.body.decode_contents()
            inner_html_length = len(corrected_inner_html)
            fingerprint = int(offset_value) + inner_html_length
            return str(fingerprint)
        except Exception as ex:
            # Return a fallback value if parsing fails
            logger.error("Error parsing DOM fingerprint", ex, exc_info=True)
            return "1000"

    @staticmethod
    def parse_server_hashes(js_text: str) -> List[str]:
        """
        Извлекает хеши сервера из JavaScript-текста.

        Args:
            js_text (str): JavaScript-текст, содержащий хеши сервера.

        Returns:
            List[str]: Список хешей сервера.
        """
        try:
            return js_text.split('server_hashes: ["', maxsplit=1)[1].split('"]', maxsplit=1)[0].split('","')
        except Exception as ex:
            # Return a fallback value if parsing fails
            logger.error("Error parsing server hashes", ex, exc_info=True)
            return ["1", "2"]

    @classmethod
    def build_x_vqd_hash_1(cls, vqd_hash_1: str, headers: Dict[str, str]) -> str:
        """
        Строит значение заголовка x-vqd-hash-1.

        Args:
            vqd_hash_1 (str): Base64-представление хеша VQD.
            headers (Dict[str, str]): Заголовки запроса.

        Returns:
            str: Значение заголовка x-vqd-hash-1.
        """
        try:
            decoded = base64.b64decode(vqd_hash_1).decode()
            server_hashes = cls.parse_server_hashes(decoded)
            dom_fingerprint = cls.parse_dom_fingerprint(decoded)

            ua_fingerprint = headers.get("User-Agent", "") + headers.get("sec-ch-ua", "")
            ua_hash = cls.sha256_base64(ua_fingerprint)
            dom_hash = cls.sha256_base64(dom_fingerprint)

            final_result = {
                "server_hashes": server_hashes,
                "client_hashes": [ua_hash, dom_hash],
                "signals": {},
            }
            base64_final_result = base64.b64encode(json.dumps(final_result).encode()).decode()
            return base64_final_result
        except Exception as ex:
            # If anything fails, return an empty string
            logger.error("Error building x-vqd-hash-1", ex, exc_info=True)
            return ""

    @classmethod
    def validate_model(cls, model: str) -> str:
        """
        Проверяет и возвращает корректное имя модели.

        Args:
            model (str): Имя модели.

        Returns:
            str: Корректное имя модели.

        Raises:
            ModelNotSupportedError: Если модель не поддерживается.
        """
        if not model:
            return cls.default_model
        if model in cls.model_aliases:
            model = cls.model_aliases[model]
        if model not in cls.models:
            raise ModelNotSupportedError(f"Model {model} not supported. Available models: {cls.models}")
        return model

    @classmethod
    async def sleep(cls, multiplier: float = 1.0) -> None:
        """
        Реализует ограничение скорости между запросами.

        Args:
            multiplier (float): Множитель задержки.
        """
        now = time.time()
        if cls.last_request_time > 0:
            delay = max(0.0, 1.5 - (now - cls.last_request_time)) * multiplier
            if delay > 0:
                await asyncio.sleep(delay)
        cls.last_request_time = time.time()

    @classmethod
    async def get_default_cookies(cls, session: ClientSession) -> Dict[str, str]:
        """
        Получает дефолтные куки, необходимые для API запросов.

        Args:
            session (ClientSession): Aiohttp ClientSession.

        Returns:
            Dict[str, str]: Словарь с куками.
        """
        try:
            await cls.sleep()
            # Make initial request to get cookies
            async with session.get(cls.url) as response:
                # We also manually set required cookies
                cookies = {}
                cookies_dict = {'dcs': '1', 'dcm': '3'}

                for name, value in cookies_dict.items():
                    cookies[name] = value
                    url_obj = URL(cls.url)
                    session.cookie_jar.update_cookies({name: value}, url_obj)

                return cookies
        except Exception as ex:
            logger.error("Error getting default cookies", ex, exc_info=True)
            return {}

    @classmethod
    async def fetch_fe_version(cls, session: ClientSession) -> str:
        """
        Извлекает fe-version из начальной загрузки страницы.

        Args:
            session (ClientSession): Aiohttp ClientSession.

        Returns:
            str: Значение fe-version.
        """
        if cls._chat_xfe:
            return cls._chat_xfe

        try:
            url = "https://duckduckgo.com/?q=DuckDuckGo+AI+Chat&ia=chat&duckai=1"
            await cls.sleep()
            async with session.get(url) as response:
                await raise_for_status(response)
                content = await response.text()

                # Extract x-fe-version components
                try:
                    xfe1 = content.split('__DDG_BE_VERSION__="', 1)[1].split('"', 1)[0]
                    xfe2 = content.split('__DDG_FE_CHAT_HASH__="', 1)[1].split('"', 1)[0]
                    cls._chat_xfe = f"{xfe1}-{xfe2}"
                    return cls._chat_xfe
                except Exception as ex:
                    # If extraction fails, return an empty string
                    logger.error("Error extracting fe version", ex, exc_info=True)
                    return ""
        except Exception as ex:
            logger.error("Error fetching fe version", ex, exc_info=True)
            return ""

    @classmethod
    async def fetch_vqd_and_hash(cls, session: ClientSession, retry_count: int = 0) -> Tuple[str, str]:
        """
        Получает VQD токен и хеш для чат сессии с повторными попытками.

        Args:
            session (ClientSession): Aiohttp ClientSession.
            retry_count (int): Количество повторных попыток.

        Returns:
            Tuple[str, str]: Кортеж с VQD токеном и хешем.

        Raises:
            RuntimeError: Если не удалось получить VQD токен и хеш после нескольких попыток.
        """
        headers = {
            "accept": "text/event-stream",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "origin": "https://duckduckgo.com",
            "referer": "https://duckduckgo.com/",
            "x-vqd-accept": "1",
        }

        # Make sure we have cookies first
        if len(session.cookie_jar) == 0:
            await cls.get_default_cookies(session)

        try:
            await cls.sleep(multiplier=1.0 + retry_count * 0.5)
            async with session.get(cls.status_url, headers=headers) as response:
                await raise_for_status(response)

                vqd = response.headers.get("x-vqd-4", "")
                vqd_hash_1 = response.headers.get("x-vqd-hash-1", "")

                if vqd:
                    # Return the fetched vqd and vqd_hash_1
                    return vqd, vqd_hash_1

                response_text = await response.text()
                raise RuntimeError(f"Failed to fetch VQD token and hash: {response.status} {response_text}")

        except Exception as ex:
            if retry_count < cls.max_retries:
                wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                await asyncio.sleep(wait_time)
                return await cls.fetch_vqd_and_hash(session, retry_count + 1)
            else:
                raise RuntimeError(f"Failed to fetch VQD token and hash after {cls.max_retries} attempts: {str(ex)}")

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: Optional[str] = None,
        timeout: int = 60,
        cookies: Optional[Cookies] = None,
        conversation: Optional[Conversation] = None,
        return_conversation: bool = False,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с DuckDuckGo AI Chat.

        Args:
            model (str): Название модели.
            messages (Messages): Список сообщений.
            proxy (Optional[str]): Прокси-сервер.
            timeout (int): Время ожидания запроса.
            cookies (Optional[Cookies]): Куки.
            conversation (Optional[Conversation]): Объект Conversation.
            return_conversation (bool): Флаг, указывающий, нужно ли возвращать объект Conversation.

        Returns:
            AsyncResult: Асинхронный генератор.
        """
        model = cls.validate_model(model)
        retry_count = 0

        while retry_count <= cls.max_retries:
            try:
                session_timeout = ClientTimeout(total=timeout)
                async with ClientSession(timeout=session_timeout, cookies=cookies) as session:
                    # Step 1: Ensure we have the fe_version
                    if not cls._chat_xfe:
                        cls._chat_xfe = await cls.fetch_fe_version(session)

                    # Step 2: Initialize or update conversation
                    if conversation is None:
                        # Get initial cookies if not provided
                        if not cookies:
                            await cls.get_default_cookies(session)

                        # Create a new conversation
                        conversation = Conversation(model)
                        conversation.fe_version = cls._chat_xfe

                        # Step 3: Get VQD tokens
                        vqd, vqd_hash_1 = await cls.fetch_vqd_and_hash(session)
                        conversation.vqd = vqd
                        conversation.vqd_hash_1 = vqd_hash_1
                        conversation.message_history = [{"role": "user", "content": format_prompt(messages)}]
                    else:
                        # Update existing conversation with new message
                        last_message = get_last_user_message(messages.copy())
                        conversation.message_history.append({"role": "user", "content": last_message})

                    # Step 4: Prepare headers - IMPORTANT: send empty x-vqd-hash-1 for the first request
                    headers = {
                        "accept": "text/event-stream",
                        "accept-language": "en-US,en;q=0.9",
                        "content-type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
                        "origin": "https://duckduckgo.com",
                        "referer": "https://duckduckgo.com/",
                        "sec-ch-ua": '"Chromium";v="133", "Not_A Brand";v="8"',
                        "x-fe-version": conversation.fe_version or cls._chat_xfe,
                        "x-vqd-4": conversation.vqd,
                        "x-vqd-hash-1": "",  # Send empty string initially
                    }

                    # Step 5: Prepare the request data
                    data = {
                        "model": model,
                        "messages": conversation.message_history,
                    }

                    # Step 6: Send the request
                    await cls.sleep(multiplier=1.0 + retry_count * 0.5)
                    async with session.post(cls.api_endpoint, json=data, headers=headers, proxy=proxy) as response:
                        # Handle 429 errors specifically
                        if response.status == 429:
                            response_text = await response.text()

                            if retry_count < cls.max_retries:
                                retry_count += 1
                                wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                                await asyncio.sleep(wait_time)

                                # Get fresh tokens and cookies
                                cookies = await cls.get_default_cookies(session)
                                continue
                            else:
                                raise RateLimitError(f"Rate limited after {cls.max_retries} retries")

                        await raise_for_status(response)
                        reason: Optional[str] = None
                        full_message: str = ""

                        # Step 7: Process the streaming response
                        async for line in response.content:
                            line = line.decode("utf-8").strip()

                            if line.startswith("data:"):
                                try:
                                    message = json.loads(line[5:].strip())
                                except json.JSONDecodeError:
                                    continue

                                if "action" in message and message["action"] == "error":
                                    error_type = message.get("type", "")
                                    if message.get("status") == 429:
                                        if error_type == "ERR_CONVERSATION_LIMIT":
                                            raise ConversationLimitError(error_type)
                                        raise RateLimitError(error_type)
                                    raise DuckDuckGoSearchException(error_type)

                                if "message" in message:
                                    if message["message"]:
                                        yield message["message"]
                                        full_message += message["message"]
                                        reason = "length"
                                    else:
                                        reason = "stop"

                        # Step 8: Update conversation with response information
                        if return_conversation:
                            conversation.message_history.append({"role": "assistant", "content": full_message})
                            # Update tokens from response headers
                            conversation.vqd = response.headers.get("x-vqd-4", conversation.vqd)
                            conversation.vqd_hash_1 = response.headers.get("x-vqd-hash-1", conversation.vqd_hash_1)
                            conversation.cookies = {
                                n: c.value
                                for n, c in session.cookie_jar.filter_cookies(URL(cls.url)).items()
                            }
                            yield conversation

                        if reason is not None:
                            yield FinishReason(reason)

                        # If we got here, the request was successful
                        break

            except (RateLimitError, ResponseStatusError) as ex:
                if "429" in str(ex) and retry_count < cls.max_retries:
                    retry_count += 1
                    wait_time = cls.base_delay * (2 ** retry_count) * (1 + random.random())
                    await asyncio.sleep(wait_time)
                else:
                    raise
            except asyncio.TimeoutError as ex:
                raise TimeoutError(f"Request timed out: {str(ex)}")
            except Exception as ex:
                logger.error("Error in create_async_generator", ex, exc_info=True)
                raise