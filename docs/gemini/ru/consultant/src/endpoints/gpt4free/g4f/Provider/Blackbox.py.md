### **Анализ кода модуля `Blackbox.py`**

## \file /hypotez/src/endpoints/gpt4free/g4f/Provider/Blackbox.py

Модуль содержит класс `Blackbox`, который является асинхронным генератором провайдера для взаимодействия с Blackbox AI.

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Использование `AsyncGeneratorProvider` для потоковой передачи ответов.
    - Поддержка различных моделей и режимов агентов.
    - Наличие механизмов для работы с cookies и HAR файлами для авторизации.
    - Документирование основных методов и классов.
- **Минусы**:
    - Дублирование кода (например, метод `generate_session` повторяется).
    - Отсутствие обработки исключений в некоторых местах.
    - Использование устаревшего `Union[]` вместо `|`.
    - Не все методы и классы имеют подробное описание.
    - Не хватает аннотаций типов для всех переменных.

**Рекомендации по улучшению:**

1.  **Удалить дублирование кода**:
    - Метод `generate_session` дублируется. Необходимо вынести его в одно место и использовать повторно.
2.  **Добавить обработку исключений**:
    - В некоторых местах отсутствует обработка исключений, что может привести к неожиданному поведению программы.
3.  **Заменить `Union[]` на `|`**:
    - Использовать современный синтаксис для объединения типов.
4.  **Дополнить документацию**:
    - Добавить подробное описание для всех методов и классов, включая аргументы, возвращаемые значения и возможные исключения.
5.  **Добавить аннотации типов**:
    - Необходимо добавить аннотации типов для всех переменных.
6.  **Использовать `j_loads` или `j_loads_ns`**:
    - Для чтения JSON или конфигурационных файлов заменить стандартное использование `open` и `json.load` на `j_loads` или `j_loads_ns`.
7.  **Логирование**:
    - Использовать `logger` из модуля `src.logger` для логирования ошибок и отладочной информации.

**Оптимизированный код:**

```python
from __future__ import annotations

import asyncio
import os
import re
import json
import random
import string
import base64
from pathlib import Path
from typing import Optional, List, Dict, Generator, Any
from datetime import datetime, timedelta

from aiohttp import ClientSession

from ..typing import AsyncResult, Messages, MediaListType
from ..requests.raise_for_status import raise_for_status
from .base_provider import AsyncGeneratorProvider, ProviderModelMixin
from ..image import to_data_uri
from ..cookies import get_cookies_dir
from .helper import format_image_prompt
from ..providers.response import JsonConversation, ImageResponse
from ..tools.media import merge_media
from .. import debug
from src.logger import logger  # Импорт модуля логирования

"""
Модуль для работы с Blackbox AI
=================================================

Модуль содержит класс :class:`Blackbox`, который используется для взаимодействия с Blackbox AI и выполнения задач обработки текста и изображений.

Пример использования
----------------------

>>> blackbox = Blackbox()
>>> async for chunk in blackbox.create_async_generator(model='blackboxai', messages=[{'role': 'user', 'content': 'Hello'}]):
...     print(chunk)
"""

class Conversation(JsonConversation):
    """
    Класс для хранения информации о текущей беседе.

    Attributes:
        validated_value (str): Валидированное значение.
        chat_id (str): Идентификатор чата.
        message_history (Messages): История сообщений.
        model (str): Модель, используемая в разговоре.
    """
    validated_value: str = None
    chat_id: str = None
    message_history: Messages = []
    model: str

    def __init__(self, model: str):
        """
        Инициализирует объект Conversation.

        Args:
            model (str): Модель, используемая в разговоре.
        """
        self.model = model


class Blackbox(AsyncGeneratorProvider, ProviderModelMixin):
    """
    Провайдер для взаимодействия с Blackbox AI.

    Attributes:
        label (str): Название провайдера.
        url (str): URL Blackbox AI.
        api_endpoint (str): URL API Blackbox AI.
        working (bool): Флаг, указывающий, работает ли провайдер.
        supports_stream (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу.
        supports_system_message (bool): Флаг, указывающий, поддерживает ли провайдер системные сообщения.
        supports_message_history (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
        default_model (str): Модель по умолчанию.
        default_vision_model (str): Модель для обработки изображений по умолчанию.
        default_image_model (str): Модель для генерации изображений по умолчанию.
        fallback_models (List[str]): Список резервных моделей.
        image_models (List[str]): Список моделей для генерации изображений.
        vision_models (List[str]): Список моделей для обработки изображений.
        userSelectedModel (List[str]): Список моделей, выбранных пользователем.
        agentMode (Dict[str, Dict[str, Any]]): Конфигурации режимов агентов.
        trendingAgentMode (Dict[str, Dict[str, Any]]): Конфигурации популярных режимов агентов.
        _all_models (List[str]): Полный список моделей.
        models (List[str]): Список доступных моделей.
        model_aliases (Dict[str, str]): Алиасы моделей.
    """
    label: str = "Blackbox AI"
    url: str = "https://www.blackbox.ai"
    api_endpoint: str = "https://www.blackbox.ai/api/chat"

    working: bool = True
    supports_stream: bool = True
    supports_system_message: bool = True
    supports_message_history: bool = True

    default_model: str = "blackboxai"
    default_vision_model: str = default_model
    default_image_model: str = 'flux'

    # Completely free models
    fallback_models: List[str] = [
        "blackboxai",
        "blackboxai-pro",
        "gpt-4o-mini",
        "GPT-4o",
        "o1",
        "o3-mini",
        "Claude-sonnet-3.7",
        "DeepSeek-V3",
        "DeepSeek-R1",
        "DeepSeek-LLM-Chat-(67B)",
        # Image models
        "flux",
        # Trending agent modes
        'Python Agent',
        'HTML Agent',
        'Builder Agent',
        'Java Agent',
        'JavaScript Agent',
        'React Agent',
        'Android Agent',
        'Flutter Agent',
        'Next.js Agent',
        'AngularJS Agent',
        'Swift Agent',
        'MongoDB Agent',
        'PyTorch Agent',
        'Xcode Agent',
        'Azure Agent',
        'Bitbucket Agent',
        'DigitalOcean Agent',
        'Docker Agent',
        'Electron Agent',
        'Erlang Agent',
        'FastAPI Agent',
        'Firebase Agent',
        'Flask Agent',
        'Git Agent',
        'Gitlab Agent',
        'Go Agent',
        'Godot Agent',
        'Google Cloud Agent',
        'Heroku Agent'
    ]

    image_models: List[str] = [default_image_model]
    vision_models: List[str] = [default_vision_model, 'GPT-4o', 'o1', 'o3-mini', 'Gemini-PRO', 'Gemini Agent', 'llama-3.1-8b Agent', 'llama-3.1-70b Agent', 'llama-3.1-405 Agent', 'Gemini-Flash-2.0', 'DeepSeek-V3']

    userSelectedModel:  List[str] = ['GPT-4o', 'o1', 'o3-mini', 'Gemini-PRO', 'Claude-sonnet-3.7', 'DeepSeek-V3', 'DeepSeek-R1', 'Meta-Llama-3.3-70B-Instruct-Turbo', 'Mistral-Small-24B-Instruct-2501', 'DeepSeek-LLM-Chat-(67B)', 'DBRX-Instruct', 'Qwen-QwQ-32B-Preview', 'Nous-Hermes-2-Mixtral-8x7B-DPO', 'Gemini-Flash-2.0']

    # Agent mode configurations
    agentMode: Dict[str, Dict[str, Any]] = {
        'GPT-4o': {'mode': True, 'id': "GPT-4o", 'name': "GPT-4o"},
        'Gemini-PRO': {'mode': True, 'id': "Gemini-PRO", 'name': "Gemini-PRO"},
        'Claude-sonnet-3.7': {'mode': True, 'id': "Claude-sonnet-3.7", 'name': "Claude-sonnet-3.7"},
        'DeepSeek-V3': {'mode': True, 'id': "deepseek-chat", 'name': "DeepSeek-V3"},
        'DeepSeek-R1': {'mode': True, 'id': "deepseek-reasoner", 'name': "DeepSeek-R1"},
        'Meta-Llama-3.3-70B-Instruct-Turbo': {'mode': True, 'id': "meta-llama/Llama-3.3-70B-Instruct-Turbo", 'name': "Meta-Llama-3.3-70B-Instruct-Turbo"},
        'Gemini-Flash-2.0': {'mode': True, 'id': "Gemini/Gemini-Flash-2.0", 'name': "Gemini-Flash-2.0"},
        'Mistral-Small-24B-Instruct-2501': {'mode': True, 'id': "mistralai/Mistral-Small-24B-Instruct-2501", 'name': "Mistral-Small-24B-Instruct-2501"},
        'DeepSeek-LLM-Chat-(67B)': {'mode': True, 'id': "deepseek-ai/deepseek-llm-67b-chat", 'name': "DeepSeek-LLM-Chat-(67B)"},
        'DBRX-Instruct': {'mode': True, 'id': "databricks/dbrx-instruct", 'name': "DBRX-Instruct"},
        'Qwen-QwQ-32B-Preview': {'mode': True, 'id': "Qwen/QwQ-32B-Preview", 'name': "Qwen-QwQ-32B-Preview"},
        'Nous-Hermes-2-Mixtral-8x7B-DPO': {'mode': True, 'id': "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO", 'name': "Nous-Hermes-2-Mixtral-8x7B-DPO"},
    }

    # Trending agent modes
    trendingAgentMode: Dict[str, Dict[str, Any]] = {
        'blackboxai-pro': {'mode': True, 'id': "BLACKBOXAI-PRO"},
        "Gemini Agent": {'mode': True, 'id': 'gemini'},
        "llama-3.1-405 Agent": {'mode': True, 'id': "llama-3.1-405"},
        'llama-3.1-70b Agent': {'mode': True, 'id': "llama-3.1-70b"},
        'llama-3.1-8b Agent': {'mode': True, 'id': "llama-3.1-8b"},
        'Python Agent': {'mode': True, 'id': "python"},
        'HTML Agent': {'mode': True, 'id': "html"},
        'Builder Agent': {'mode': True, 'id': "builder"},
        'Java Agent': {'mode': True, 'id': "java"},
        'JavaScript Agent': {'mode': True, 'id': "javascript"},
        'React Agent': {'mode': True, 'id': "react"},
        'Android Agent': {'mode': True, 'id': "android"},
        'Flutter Agent': {'mode': True, 'id': "flutter"},
        'Next.js Agent': {'mode': True, 'id': "next.js"},
        'AngularJS Agent': {'mode': True, 'id': "angularjs"},
        'Swift Agent': {'mode': True, 'id': "swift"},
        'MongoDB Agent': {'mode': True, 'id': "mongodb"},
        'PyTorch Agent': {'mode': True, 'id': "pytorch"},
        'Xcode Agent': {'mode': True, 'id': "xcode"},
        'Azure Agent': {'mode': True, 'id': "azure"},
        'Bitbucket Agent': {'mode': True, 'id': "bitbucket"},
        'DigitalOcean Agent': {'mode': True, 'id': "digitalocean"},
        'Docker Agent': {'mode': True, 'id': "docker"},
        'Electron Agent': {'mode': True, 'id': "electron"},
        'Erlang Agent': {'mode': True, 'id': "erlang"},
        'FastAPI Agent': {'mode': True, 'id': "fastapi"},
        'Firebase Agent': {'mode': True, 'id': "firebase"},
        'Flask Agent': {'mode': True, 'id': "flask"},
        'Git Agent': {'mode': True, 'id': "git"},
        'Gitlab Agent': {'mode': True, 'id': "gitlab"},
        'Go Agent': {'mode': True, 'id': "go"},
        'Godot Agent': {'mode': True, 'id': "godot"},
        'Google Cloud Agent': {'mode': True, 'id': "googlecloud"},
        'Heroku Agent': {'mode': True, 'id': "heroku"},
    }

    # Complete list of all models (for authorized users)
    _all_models: List[str] = list(dict.fromkeys([
        default_model,
        *userSelectedModel,
        *image_models,
        *list(agentMode.keys()),
        *list(trendingAgentMode.keys())
    ]))

    # Initialize models with fallback_models
    models: List[str] = fallback_models

    model_aliases: Dict[str, str] = {
        "gpt-4o": "GPT-4o",
        "claude-3.7-sonnet": "Claude-sonnet-3.7",
        "deepseek-v3": "DeepSeek-V3",
        "deepseek-r1": "DeepSeek-R1",
        "deepseek-chat": "DeepSeek-LLM-Chat-(67B)",
    }

    @classmethod
    def generate_session(cls, id_length: int = 21, days_ahead: int = 365) -> dict:
        """
        Генерирует динамическую сессию с правильным ID и форматом срока действия.

        Args:
            id_length (int): Длина числового ID (по умолчанию: 21).
            days_ahead (int): Количество дней до истечения срока действия (по умолчанию: 365).

        Returns:
            dict: Словарь сессии с информацией о пользователе и сроком действия.
        """
        # Generate numeric ID
        numeric_id: str = ''.join(random.choice('0123456789') for _ in range(id_length))

        # Generate future expiry date
        future_date: datetime = datetime.now() + timedelta(days=days_ahead)
        expiry: str = future_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        # Decode the encoded email
        encoded_email: str = "Z2lzZWxlQGJsYWNrYm94LmFp"  # Base64 encoded email
        email: str = base64.b64decode(encoded_email).decode('utf-8')

        # Generate random image ID for the new URL format
        chars: str = string.ascii_letters + string.digits + "-"
        random_img_id: str = ''.join(random.choice(chars) for _ in range(48))
        image_url: str = f"https://lh3.googleusercontent.com/a/ACg8oc{random_img_id}=s96-c"

        return {
            "user": {
                "name": "BLACKBOX AI",
                "email": email,
                "image": image_url,
                "id": numeric_id
            },
            "expires": expiry
        }

    @classmethod
    async def fetch_validated(cls, url: str = "https://www.blackbox.ai", force_refresh: bool = False) -> Optional[str]:
        """
        Извлекает валидированное значение из кэша или с веб-страницы.

        Args:
            url (str): URL для извлечения (по умолчанию: "https://www.blackbox.ai").
            force_refresh (bool): Принудительное обновление кэша (по умолчанию: False).

        Returns:
            Optional[str]: Валидированное значение или None в случае ошибки.
        """
        cache_file: Path = Path(get_cookies_dir()) / 'blackbox.json'

        if not force_refresh and cache_file.exists():
            try:
                with open(cache_file, 'r') as f:
                    data: dict = json.load(f)
                    if data.get('validated_value'):
                        return data['validated_value']
            except Exception as ex:
                logger.error(f"Blackbox: Error reading cache: {ex}", exc_info=True)
                debug.log(f"Blackbox: Error reading cache: {ex}")

        js_file_pattern: str = r'static/chunks/\\d{4}-[a-fA-F0-9]+\\.js'
        uuid_pattern: str = r'["\\\']([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})["\\\']'

        def is_valid_context(text: str) -> bool:
            """
            Проверяет, является ли контекст валидным.

            Args:
                text (str): Текст для проверки.

            Returns:
                bool: True, если контекст валиден, иначе False.
            """
            return any(char + '=' in text for char in 'abcdefghijklmnopqrstuvwxyz')

        async with ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        return None

                    page_content: str = await response.text()
                    js_files: List[str] = re.findall(js_file_pattern, page_content)

                for js_file in js_files:
                    js_url: str = f"{url}/_next/{js_file}"
                    async with session.get(js_url) as js_response:
                        if js_response.status == 200:
                            js_content: str = await js_response.text()
                            for match in re.finditer(uuid_pattern, js_content):
                                start: int = max(0, match.start() - 10)
                                end: int = min(len(js_content), match.end() + 10)
                                context: str = js_content[start:end]

                                if is_valid_context(context):
                                    validated_value: str = match.group(1)

                                    cache_file.parent.mkdir(exist_ok=True)
                                    try:
                                        with open(cache_file, 'w') as f:
                                            json.dump({'validated_value': validated_value}, f)
                                    except Exception as ex:
                                        logger.error(f"Blackbox: Error writing cache: {ex}", exc_info=True)
                                        debug.log(f"Blackbox: Error writing cache: {ex}")

                                    return validated_value

            except Exception as ex:
                logger.error(f"Blackbox: Error retrieving validated_value: {ex}", exc_info=True)
                debug.log(f"Blackbox: Error retrieving validated_value: {ex}")

        return None

    @classmethod
    def generate_id(cls, length: int = 7) -> str:
        """
        Генерирует случайный ID заданной длины.

        Args:
            length (int): Длина ID (по умолчанию: 7).

        Returns:
            str: Случайный ID.
        """
        chars: str = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    @classmethod
    def get_models(cls) -> list:
        """
        Возвращает список доступных моделей в зависимости от статуса авторизации.

        Авторизованные пользователи получают полный список моделей.
        Неавторизованные пользователи получают только fallback_models.
        """
        # Check if there are valid session data in HAR files
        has_premium_access: bool = cls._check_premium_access()

        if has_premium_access:
            # For authorized users - all models
            debug.log(f"Blackbox: Returning full model list with {len(cls._all_models)} models")
            return cls._all_models
        else:
            # For demo accounts - only free models
            debug.log(f"Blackbox: Returning free model list with {len(cls.fallback_models)} models")
            return cls.fallback_models

    @classmethod
    def _check_premium_access(cls) -> bool:
        """
        Проверяет наличие авторизованной сессии в HAR файлах.
        Возвращает True, если найдена действительная сессия, отличающаяся от демонстрационной.
        """
        try:
            har_dir: str = get_cookies_dir()
            if not os.access(har_dir, os.R_OK):
                return False

            for root, _, files in os.walk(har_dir):
                for file in files:
                    if file.endswith(".har"):
                        try:
                            with open(os.path.join(root, file), 'rb') as f:
                                har_data: dict = json.load(f)

                            for entry in har_data['log']['entries']:
                                # Only check requests to blackbox API
                                if 'blackbox.ai/api' in entry['request']['url']:
                                    if 'response' in entry and 'content' in entry['response']:
                                        content: dict = entry['response']['content']
                                        if ('text' in content and
                                            isinstance(content['text'], str) and
                                            '"user"' in content['text'] and
                                            '"email"' in content['text']):

                                            try:
                                                # Process request text
                                                text: str = content['text'].strip()
                                                if text.startswith('{') and text.endswith('}'):
                                                    text = text.replace('\\\\"', '"')
                                                    session_data: dict = json.loads(text)

                                                    # Check if this is a valid session
                                                    if (isinstance(session_data, dict) and
                                                        'user' in session_data and
                                                        'email' in session_data['user']):

                                                        # Check if this is not a demo session
                                                        demo_session: dict = cls.generate_session()
                                                        if (session_data['user'].get('email') !=
                                                            demo_session['user'].get('email')):
                                                            # This is not a demo session, so user has premium access
                                                            return True
                                            except json.JSONDecodeError as ex:
                                                # Only print error for entries that truly look like session data
                                                if ('"user"' in content['text'] and
                                                    '"email"' in content['text']):
                                                    logger.error(f"Blackbox: Error parsing likely session data: {ex}", exc_info=True)
                                                    debug.log(f"Blackbox: Error parsing likely session data: {ex}")

                        except Exception as ex:
                            logger.error(f"Blackbox: Error reading HAR file: {ex}", exc_info=True)
                            debug.log(f"Blackbox: Error reading HAR file: {ex}")

            return False
        except Exception as ex:
            logger.error(f"Blackbox: Error checking premium access: {ex}", exc_info=True)
            debug.log(f"Blackbox: Error checking premium access: {ex}")
            return False

    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        prompt: Optional[str] = None,
        proxy: Optional[str] = None,
        media: Optional[MediaListType] = None,
        top_p: Optional[float] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        conversation: Optional[Conversation] = None,
        return_conversation: bool = False,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для взаимодействия с Blackbox AI.

        Args:
            model (str): Модель для использования.
            messages (Messages): Список сообщений для отправки.
            prompt (Optional[str]): Дополнительный промпт (по умолчанию: None).
            proxy (Optional[str]): Прокси-сервер (по умолчанию: None).
            media (Optional[MediaListType]): Список медиа-файлов (по умолчанию: None).
            top_p (Optional[float]): Значение top_p (по умолчанию: None).
            temperature (Optional[float]): Температура (по умолчанию: None).
            max_tokens (Optional[int]): Максимальное количество токенов (по умолчанию: None).
            conversation (Optional[Conversation]): Объект Conversation (по умолчанию: None).
            return_conversation (bool): Возвращать ли объект Conversation (по умолчанию: False).
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор.
        """
        model = cls.get_model(model)
        headers: Dict[str, str] = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.blackbox.ai',
            'referer': 'https://www.blackbox.ai/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        }

        async with ClientSession(headers=headers) as session:
            if conversation is None or not hasattr(conversation, "chat_id"):
                conversation = Conversation(model)
                conversation.validated_value = await cls.fetch_validated()
                conversation.chat_id = cls.generate_id()
                conversation.message_history = []

            current_messages: List[Dict[str, Any]] = []
            for i, msg in enumerate(messages):
                msg_id: str = conversation.chat_id if i == 0 and msg["role"] == "user" else cls.generate_id()
                current_msg: Dict[str, Any] = {
                    "id": msg_id,
                    "content": msg["content"],
                    "role": msg["role"]
                }
                current_messages.append(current_msg)

            if media is not None:
                current_messages[-1]['data'] = {
                    "imagesData": [
                        {
                            "filePath": f"/{image_name}",
                            "contents": to_data_uri(image)
                        }
                        for image, image_name in merge_media(media, messages)
                    ],
                    "fileText": "",
                    "title": ""
                }

            # Try to get session data from HAR files
            session_data: Optional[Dict[str, Any]] = cls.generate_session()  # Default fallback
            session_found: bool = False

            # Look for HAR session data
            har_dir: str = get_cookies_dir()
            if os.access(har_dir, os.R_OK):
                for root, _, files in os.walk(har_dir):
                    for file in files:
                        if file.endswith(".har"):
                            try:
                                with open(os.path.join(root, file), 'rb') as f:
                                    har_data: dict = json.load(f)

                                for entry in har_data['log']['entries']:
                                    # Only look at blackbox API responses
                                    if 'blackbox.ai/api' in entry['request']['url']:
                                        # Look for a response that has the right structure
                                        if 'response' in entry and 'content' in entry['response']:
                                            content: dict = entry['response']['content']
                                            # Look for both regular and Google auth session formats
                                            if ('text' in content and
                                                isinstance(content['text'], str) and
                                                '"user"' in content['text'] and
                                                '"email"' in content['text'] and
                                                '"expires"' in content['text']):

                                                try:
                                                    # Remove any HTML or other non-JSON content
                                                    text: str = content['text'].strip()
                                                    if text.startswith('{') and text.endswith('}'):
                                                        # Replace escaped quotes
                                                        text = text.replace('\\\\"', '"')
                                                        har_session: dict = json.loads(text)

                                                        # Check if this is a valid session object (supports both regular and Google auth)
                                                        if (isinstance(har_session, dict) and
                                                            'user' in har_session and
                                                            'email' in har_session['user'] and
                                                            'expires' in har_session):

                                                            file_path: str = os.path.join(root, file)
                                                            debug.log(f"Blackbox: Found session in HAR file")

                                                            session_data = har_session
                                                            session_found = True
                                                            break
                                                except json.JSONDecodeError as ex:
                                                    # Only print error for entries that truly look like session data
                                                    if ('"user"' in content['text'] and
                                                        '"email"' in content['text']):
                                                        logger.error(f"Blackbox: Error parsing likely session data: {ex}", exc_info=True)
                                                        debug.log(f"Blackbox: Error parsing likely session data: {ex}")

                                    if session_found:
                                        break

                            except Exception as ex:
                                logger.error(f"Blackbox: Error reading HAR file: {ex}", exc_info=True)
                                debug.log(f"Blackbox: Error reading HAR file: {ex}")

                            if session_found:
                                break

                    if session_found:
                        break

            data: Dict[str, Any] = {
                "messages": current_messages,
                "agentMode": cls.agentMode.get(model, {}) if model in cls.agentMode else {},
                "id": conversation.chat_id,
                "previewToken": None,
                "userId": None,
                "codeModelMode": True,
                "trendingAgentMode": cls.trendingAgentMode.get(model, {}) if model in cls.trendingAgentMode else {},
                "isMicMode": False,
                "userSystemPrompt": None,
                "maxTokens": max_tokens,
                "playgroundTopP": top_p,
                "playgroundTemperature": temperature,
                "isChromeExt": False,
                "githubToken": "",
                "clickedAnswer2": False,
                "clickedAnswer3": False,
                "clickedForceWebSearch": False,
                "visitFromDelta": False,
                "isMemoryEnabled": False,
                "mobileClient": False,
                "userSelectedModel": model if model in cls.userSelectedModel else None,
                "validated": conversation.validated_value,
                "imageGenerationMode": model == cls.default_image_model,
                "webSearchModePrompt": False,
                "deepSearchMode": False,
                "domains": None,
                "vscodeClient": False,
                "codeInterpreterMode": False,
                "customProfile": {
                    "name": "",
                    "occupation": "",
                    "traits": [],
                    "additionalInfo": "",
                    "enableNewChats": False
                },
                "session": session_data if session_data else cls.generate_session(),
                "isPremium": True,
                "subscriptionCache": None,
                "beastMode": False,
                "webSearchMode": False
            }

            # Add debugging before making the API call
            if isinstance(session_data, dict) and 'user' in session_data:
                # Генеруємо демо-сесію для порівняння
                demo_session: dict = cls.generate_session()
                is_demo: bool = False

                if demo_session and isinstance(demo_session, dict) and 'user' in demo_session:
                    if session_data['user'].get('email') == demo_session['user'].get('email'):
                        is_demo = True

                if is_demo:
                    debug.log(f"Blackbox: Making API request with built-in Developer Premium Account")
                else:
                    user_email: str = session_data['user'].get('email', 'unknown')
                    debug.log(f"Blackbox: Making API request with HAR session email: {user_email}")

            # Continue with the API request and async generator behavior
            async with session.post(cls.api_endpoint, json=data, proxy=proxy) as response:
                await raise_for_status(response)

                # Collect the full response
                full_response: List[str] = []
                async for chunk in response.content.iter_any():
                    if chunk:
                        chunk_text: str = chunk.decode()
                        full_response.append(chunk_text)