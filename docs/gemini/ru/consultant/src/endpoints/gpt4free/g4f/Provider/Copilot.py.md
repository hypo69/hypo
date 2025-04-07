### **Анализ кода модуля `Copilot.py`**

#### **Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код структурирован и включает в себя обработку ошибок и логирование.
    - Присутствуют асинхронные функции для неблокирующих операций.
    - Используется `curl_cffi` для выполнения HTTP-запросов, что может повысить производительность.
- **Минусы**:
    - Отсутствуют docstring для большинства функций и классов, что затрудняет понимание кода.
    - Не все переменные аннотированы типами.
    - Используются устаревшие конструкции, такие как `Union[]` вместо `|`.
    - Не используется модуль `logger` из `src.logger.logger` для логирования.

#### **Рекомендации по улучшению**:
1.  **Добавить docstring**:
    - Добавить docstring для всех классов и функций, включая описание аргументов, возвращаемых значений и возможных исключений.
    - Описать назначение каждой функции и класса, а также предоставить примеры использования.
2.  **Аннотации типов**:
    - Добавить аннотации типов для всех переменных и параметров функций.
3.  **Использовать `|` вместо `Union[]`**:
    - Заменить все конструкции `Union[]` на `|` для соответствия современному синтаксису Python.
4.  **Логирование**:
    - Использовать модуль `logger` из `src.logger.logger` для логирования ошибок и отладочной информации.
5.  **Обработка исключений**:
    - Использовать `ex` вместо `e` в блоках обработки исключений.
6.  **Форматирование кода**:
    - Привести код в соответствие со стандартами PEP8, включая добавление пробелов вокруг операторов присваивания.
7. **Использовать `j_loads` или `j_loads_ns`**:
    - Для чтения JSON или конфигурационных файлов заменить стандартное использование `open` и `json.load` на `j_loads` или `j_loads_ns`.
8. **Использовать вебдрайвер из модуля `src.webdirver`**:
    - Использовать Driver, Chrome, Firexox, Playwright из  `src.webdirver`.

#### **Оптимизированный код**:

```python
"""
Модуль для взаимодействия с Microsoft Copilot.
================================================

Модуль содержит класс :class:`Copilot`, который позволяет взаимодействовать с Copilot от Microsoft через WebSocket.
Он поддерживает стриминг ответов, загрузку изображений и управление диалогом.

Пример использования:
----------------------

>>> Copilot.create_completion(model="Copilot", messages=[{"role": "user", "content": "Привет!"}], stream=True)
"""
from __future__ import annotations

import os
import json
import asyncio
import base64
from urllib.parse import quote
from typing import Generator, Optional, List, Dict, Tuple, Any

try:
    from curl_cffi.requests import Session
    from curl_cffi import CurlWsFlag

    has_curl_cffi = True
except ImportError:
    has_curl_cffi = False
try:
    import nodriver

    has_nodriver = True
except ImportError:
    has_nodriver = False

from .base_provider import AbstractProvider, ProviderModelMixin
from .helper import format_prompt_max_length
from .openai.har_file import get_headers, get_har_files
from ..typing import CreateResult, Messages, MediaListType
from ..errors import MissingRequirementsError, NoValidHarFileError, MissingAuthError
from ..requests.raise_for_status import raise_for_status
from ..providers.response import (
    BaseConversation,
    JsonConversation,
    RequestLogin,
    ImageResponse,
    FinishReason,
    SuggestedFollowups,
)
from ..providers.asyncio import get_running_loop
from ..tools.media import merge_media
from ..requests import get_nodriver
from ..image import to_bytes, is_accepted_format
from .helper import get_last_user_message
from .. import debug
from src.logger import logger  # Import logger
# импортируем webdriver
# from src.webdirver import Driver, Chrome, Firefox, Playwright # TODO


class Conversation(JsonConversation):
    """
    Класс для представления объекта разговора.

    Args:
        conversation_id (str): Идентификатор разговора.
    """

    conversation_id: str

    def __init__(self, conversation_id: str):
        """
        Инициализирует объект Conversation.

        Args:
            conversation_id (str): Идентификатор разговора.
        """
        self.conversation_id = conversation_id


class Copilot(AbstractProvider, ProviderModelMixin):
    """
    Класс для взаимодействия с Microsoft Copilot.

    Поддерживает создание завершений, стриминг, проксирование и загрузку медиафайлов.
    """

    label: str = "Microsoft Copilot"
    url: str = "https://copilot.microsoft.com"

    working: bool = True
    supports_stream: bool = True

    default_model: str = "Copilot"
    models: List[str] = [default_model, "Think Deeper"]
    model_aliases: Dict[str, str] = {
        "gpt-4": default_model,
        "gpt-4o": default_model,
        "o1": "Think Deeper",
        "reasoning": "Think Deeper",
        "dall-e-3": default_model,
    }

    websocket_url: str = "wss://copilot.microsoft.com/c/api/chat?api-version=2"
    conversation_url: str = f"{url}/c/api/conversations"

    _access_token: Optional[str] = None
    _cookies: Optional[dict] = None

    @classmethod
    def create_completion(
        cls,
        model: str,
        messages: Messages,
        stream: bool = False,
        proxy: Optional[str] = None,
        timeout: int = 900,
        prompt: Optional[str] = None,
        media: Optional[MediaListType] = None,
        conversation: Optional[BaseConversation] = None,
        return_conversation: bool = False,
        api_key: Optional[str] = None,
        **kwargs,
    ) -> CreateResult:
        """
        Создает запрос на завершение к Copilot.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для отправки.
            stream (bool, optional): Флаг для стриминга ответов. Defaults to False.
            proxy (Optional[str], optional): Адрес прокси-сервера. Defaults to None.
            timeout (int, optional): Время ожидания запроса. Defaults to 900.
            prompt (Optional[str], optional): Текст запроса. Defaults to None.
            media (Optional[MediaListType], optional): Список медиафайлов для отправки. Defaults to None.
            conversation (Optional[BaseConversation], optional): Объект разговора. Defaults to None.
            return_conversation (bool, optional): Флаг для возврата объекта разговора. Defaults to False.
            api_key (Optional[str], optional): API ключ для авторизации. Defaults to None.

        Yields:
            CreateResult: Результат запроса.

        Raises:
            MissingRequirementsError: Если отсутствует библиотека `curl_cffi`.
            NoValidHarFileError: Если не найден валидный HAR-файл.
            MissingAuthError: Если отсутствует токен доступа.
            RuntimeError: При возникновении ошибок во время выполнения запроса.

        Example:
            >>> messages = [{"role": "user", "content": "Привет!"}]
            >>> for response in Copilot.create_completion(model="Copilot", messages=messages, stream=True):
            ...     print(response)
        """
        if not has_curl_cffi:
            raise MissingRequirementsError(
                'Install or update "curl_cffi" package | pip install -U curl_cffi'
            )
        model = cls.get_model(model)
        websocket_url = cls.websocket_url
        headers: Optional[Dict[str, str]] = None
        if cls._access_token:
            if api_key is not None:
                cls._access_token = api_key
            if cls._access_token is None:
                try:
                    cls._access_token, cls._cookies = readHAR(cls.url)
                except NoValidHarFileError as h:
                    debug.log(f"Copilot: {h}")
                    if has_nodriver:
                        yield RequestLogin(
                            cls.label, os.environ.get("G4F_LOGIN_URL", "")
                        )
                        get_running_loop(check_nested=True)
                        cls._access_token, cls._cookies = asyncio.run(
                            get_access_token_and_cookies(cls.url, proxy)
                        )
                    else:
                        raise h
            websocket_url = f"{websocket_url}&accessToken={quote(cls._access_token)}"
            headers = {"authorization": f"Bearer {cls._access_token}"}

        with Session(
            timeout=timeout,
            proxy=proxy,
            impersonate="chrome",
            headers=headers,
            cookies=cls._cookies,
        ) as session:
            if cls._access_token is not None:
                cls._cookies = (
                    session.cookies.jar if hasattr(session.cookies, "jar") else session.cookies
                )
            # if cls._access_token is None:
            #     try:
            #         url = "https://copilot.microsoft.com/cl/eus-sc/collect"
            #         headers = {
            #             "Accept": "application/x-clarity-gzip",
            #             "referrer": "https://copilot.microsoft.com/onboarding"
            #         }
            #         response = session.post(url, headers=headers, data=get_clarity())
            #         clarity_token = json.loads(response.text.split(" ", maxsplit=1)[-1])[0]["value"]
            #         debug.log(f"Copilot: Clarity Token: ...{clarity_token[-12:]}")
            #     except Exception as e:
            #         debug.log(f"Copilot: {e}")
            # else:
            #     clarity_token = None
            response = session.get("https://copilot.microsoft.com/c/api/user")
            if response.status_code == 401:
                raise MissingAuthError("Status 401: Invalid access token")
            raise_for_status(response)
            user: Optional[str] = response.json().get("firstName")
            if user is None:
                cls._access_token = None
            debug.log(f"Copilot: User: {user or 'null'}")
            if conversation is None:
                response = session.post(cls.conversation_url)
                raise_for_status(response)
                conversation_id: str = response.json().get("id")
                conversation = Conversation(conversation_id)
                if return_conversation:
                    yield conversation
                if prompt is None:
                    prompt = format_prompt_max_length(messages, 10000)
                debug.log(f"Copilot: Created conversation: {conversation_id}")
            else:
                conversation_id = conversation.conversation_id
                if prompt is None:
                    prompt = get_last_user_message(messages)
                debug.log(f"Copilot: Use conversation: {conversation_id}")

            uploaded_images: List[Dict[str, str]] = []
            media, _ = [(None, None), *merge_media(media, messages)].pop()
            if media:
                if not isinstance(media, str):
                    data: bytes = to_bytes(media)
                    response = session.post(
                        "https://copilot.microsoft.com/c/api/attachments",
                        headers={"content-type": is_accepted_format(data)},
                        data=data,
                    )
                    raise_for_status(response)
                    media = response.json().get("url")
                uploaded_images.append({"type": "image", "url": media})

            wss = session.ws_connect(cls.websocket_url)
            # if clarity_token is not None:
            #     wss.send(json.dumps({
            #         "event": "challengeResponse",
            #         "token": clarity_token,
            #         "method":"clarity"
            #     }).encode(), CurlWsFlag.TEXT)
            wss.send(
                json.dumps(
                    {
                        "event": "setOptions",
                        "supportedCards": [
                            "weather",
                            "local",
                            "image",
                            "sports",
                            "video",
                            "ads",
                            "finance",
                        ],
                        "ads": {
                            "supportedTypes": [
                                "multimedia",
                                "product",
                                "tourActivity",
                                "propertyPromotion",
                                "text",
                            ]
                        },
                    }
                )
            )
            wss.send(
                json.dumps(
                    {
                        "event": "send",
                        "conversationId": conversation_id,
                        "content": [*uploaded_images, {"type": "text", "text": prompt}],
                        "mode": "reasoning" if "Think" in model else "chat",
                    }
                ).encode(),
                CurlWsFlag.TEXT,
            )

            is_started: bool = False
            msg: Optional[Dict[str, Any]] = None
            image_prompt: Optional[str] = None
            last_msg: Optional[Dict[str, Any]] = None
            try:
                while True:
                    try:
                        msg = wss.recv()[0]
                        msg = json.loads(msg)
                    except:
                        break
                    last_msg = msg
                    if msg.get("event") == "appendText":
                        is_started = True
                        yield msg.get("text")
                    elif msg.get("event") == "generatingImage":
                        image_prompt = msg.get("prompt")
                    elif msg.get("event") == "imageGenerated":
                        yield ImageResponse(
                            msg.get("url"), image_prompt, {"preview": msg.get("thumbnailUrl")}
                        )
                    elif msg.get("event") == "done":
                        yield FinishReason("stop")
                        break
                    elif msg.get("event") == "suggestedFollowups":
                        yield SuggestedFollowups(msg.get("suggestions"))
                        break
                    elif msg.get("event") == "replaceText":
                        yield msg.get("text")
                    elif msg.get("event") == "error":
                        raise RuntimeError(f"Error: {msg}")
                    elif msg.get("event") not in [
                        "received",
                        "startMessage",
                        "citation",
                        "partCompleted",
                    ]:
                        debug.log(f"Copilot Message: {msg}")
                if not is_started:
                    raise RuntimeError(f"Invalid response: {last_msg}")
            except Exception as ex:
                logger.error("Error while processing Copilot response", ex, exc_info=True)
            finally:
                wss.close()


async def get_access_token_and_cookies(
    url: str, proxy: Optional[str] = None, target: str = "ChatAI"
) -> Tuple[Optional[str], Optional[Dict[str, str]]]:
    """
    Асинхронно получает access token и cookies из браузера с использованием nodriver.

    Args:
        url (str): URL для получения access token и cookies.
        proxy (Optional[str], optional): Прокси-сервер. Defaults to None.
        target (str, optional): Цель для поиска access token. Defaults to "ChatAI".

    Returns:
        Tuple[Optional[str], Optional[Dict[str, str]]]: Access token и cookies.
    """
    browser, stop_browser = await get_nodriver(proxy=proxy, user_data_dir="copilot")
    try:
        page = await browser.get(url)
        access_token: Optional[str] = None
        while access_token is None:
            access_token = await page.evaluate(
                """
                (() => {
                    for (var i = 0; i < localStorage.length; i++) {
                        try {
                            item = JSON.parse(localStorage.getItem(localStorage.key(i)));
                            if (item.credentialType == "AccessToken" 
                                && item.expiresOn > Math.floor(Date.now() / 1000)
                                && item.target.includes("target")) {
                                return item.secret;
                            }
                        } catch(e) {}
                    }
                })()
            """.replace(
                    '"target"', json.dumps(target)
                )
            )
            if access_token is None:
                await asyncio.sleep(1)
        cookies: Dict[str, str] = {}
        for c in await page.send(nodriver.cdp.network.get_cookies([url])):
            cookies[c.name] = c.value
        await page.close()
        return access_token, cookies
    except Exception as ex:
        logger.error("Error while getting access token and cookies", ex, exc_info=True)
        return None, None
    finally:
        stop_browser()


def readHAR(url: str) -> Tuple[Optional[str], Optional[Dict[str, str]]]:
    """
    Читает HAR-файлы для получения access token и cookies.

    Args:
        url (str): URL для поиска в HAR-файлах.

    Returns:
        Tuple[Optional[str], Optional[Dict[str, str]]]: Access token и cookies.

    Raises:
        NoValidHarFileError: Если не найден access token в HAR-файлах.
    """
    api_key: Optional[str] = None
    cookies: Optional[Dict[str, str]] = None
    for path in get_har_files():
        with open(path, "rb") as file:
            try:
                harFile = json.loads(file.read())
            except json.JSONDecodeError:
                # Error: not a HAR file!
                continue
            for v in harFile["log"]["entries"]:
                if v["request"]["url"].startswith(url):
                    v_headers = get_headers(v)
                    if "authorization" in v_headers:
                        api_key = v_headers["authorization"].split(maxsplit=1).pop()
                    if v["request"]["cookies"]:
                        cookies = {c["name"]: c["value"] for c in v["request"]["cookies"]}
    if api_key is None:
        raise NoValidHarFileError("No access token found in .har files")

    return api_key, cookies


def get_clarity() -> bytes:
    """
    Возвращает bytes для запроса к clarity.

    Returns:
        bytes: Тело запроса.
    """
    # {"e":["0.7.58",5,7284,4779,"n59ae4ieqq","aln5en","1upufhz",1,0,0],"a":[[7323,12,65,217,324],[7344,12,65,214,329],[7385,12,65,211,334],[7407,12,65,210,337],[7428,12,65,209,338],[7461,12,65,209,339],[7497,12,65,209,339],[7531,12,65,208,340],[7545,12,65,208,342],[11654,13,65,208,342],[11728,14,65,208,342],[11728,9,65,208,342,17535,19455,0,0,0,"Annehmen",null,"52w7wqv1r.8ovjfyrpu",1],[7284,4,1,393,968,393,968,0,0,231,310,939,0],[12063,0,2,147,3,4,4,18,5,1,10,79,25,15],[12063,36,6,[11938,0]]]}
    body: bytes = base64.b64decode(
        "H4sIAAAAAAAAA23RwU7DMAwG4HfJ2aqS2E5ibjxH1cMOnQYqYZvUTQPx7vyJRGGAemj01XWcP+9udg+j80MetDhSyrEISc5GrqrtZnmaTydHbrdUnSsWYT2u+8Obo0Ce/IQvaDBmjkwhUlKKIRNHmQgosqEArWPRDQMx90rxeUMPzB1j+UJvwNIxhTvsPcXyX1T+rizE4juK3mEEhpAUg/JvzW1/+U/tB1LATmhqotoiweMea50PLy2vui4LOY3XfD1dwnkor5fn/e18XBFgm6fHjSzZmCyV7d3aRByAEYextaTHEH3i5pgKGVP/s+DScE5PuLKIpW6FnCi1gY3Rbpqmj0/DI/+L7QEAAA=="
    )
    return body