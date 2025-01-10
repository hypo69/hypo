# Анализ кода модуля revai

**Качество кода**
1

-  Плюсы
    -  Присутствует описание модуля.
-  Минусы
    -  Код не соответствует ни одному из требований к оформлению кода.
    -  Отсутствуют импорты.
    -  Нет примеров использования, документации.
    -  Нет кода, только ссылки на документацию и описание.
    -  Отсутствует описание функций.
    -  Не проводится анализ структуры.

**Рекомендации по улучшению**

1.  Добавить импорты необходимых библиотек, если таковые требуются для работы с rev.com API.
2.  Создать структуру модуля, включая классы и функции для взаимодействия с API rev.com.
3.  Добавить документацию в формате RST для модуля, классов и функций.
4.  Использовать `from src.logger.logger import logger` для логирования.
5.  Учесть обработку ошибок с помощью `logger.error`.
6.  Добавить примеры использования.
7.  Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для работы с API Rev.ai (rev.com)
=========================================================================================

Этот модуль предоставляет инструменты для взаимодействия с API Rev.ai,
который используется для работы со звуковыми файлами переговоров, совещаний, звонков и т.п.

Модуль позволяет отправлять файлы для транскрибирования, получать результаты
и управлять процессами транскрипции.

Пример использования
--------------------

Пример создания экземпляра класса и отправки файла на транскрибирование:

.. code-block:: python

    from src.ai.revai import RevAiClient

    # инициализация клиента с токеном API
    revai_client = RevAiClient(api_token='your_api_token')

    # путь к аудиофайлу
    audio_file_path = 'path/to/your/audiofile.mp3'

    # отправка файла на транскрибирование
    job_id = await revai_client.submit_job(audio_file_path)
    print(f"Job ID: {job_id}")

"""

from pathlib import Path
from typing import Any, Dict, List
import json
import aiohttp
from src.logger.logger import logger

class RevAiClient:
    """
    Клиент для взаимодействия с API Rev.ai.

    Args:
        api_token (str): API токен для доступа к Rev.ai.
        base_url (str): Базовый URL API.

    Attributes:
        base_url (str): Базовый URL API.
        headers (dict): Заголовки для HTTP-запросов, включая авторизацию.

    """
    def __init__(self, api_token: str, base_url: str = "https://api.rev.ai/speechtotext/v1"):
        """Инициализирует клиента с токеном API."""
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
        }

    async def submit_job(self, audio_file_path: str | Path, options: Dict = None) -> str | None:
        """
        Отправляет аудиофайл на транскрибирование.

        Args:
            audio_file_path (str | Path): Путь к аудиофайлу.
            options (Dict, optional): Дополнительные опции для запроса.

        Returns:
            str | None: ID задания транскрибирования, если запрос успешен, иначе None.
        
        Example:
           >>> revai_client = RevAiClient(api_token='your_api_token')
           >>> audio_file_path = 'path/to/audio.mp3'
           >>> job_id = await revai_client.submit_job(audio_file_path)
           >>> print(job_id)
           "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        """
        url = f"{self.base_url}/jobs"
        try:
            async with aiohttp.ClientSession() as session:
                with open(audio_file_path, "rb") as audio_file:
                   files = {"media": audio_file}
                   async with session.post(url, headers=self.headers, data = files, params=options) as response:
                        response.raise_for_status()
                        data = await response.json()
                        logger.info(f"Задание успешно отправлено, ID: {data.get('id')}")
                        return data.get("id")
        except aiohttp.ClientError as e:
           logger.error(f"Ошибка при отправке задания: {e}")
           return None
        except Exception as ex:
            logger.error(f"Произошла непредвиденная ошибка {ex}")
            return None
    
    async def get_job_details(self, job_id: str) -> Dict | None:
        """
        Получает детали задания транскрибирования.

        Args:
            job_id (str): ID задания транскрибирования.

        Returns:
            Dict | None: Детали задания, если запрос успешен, иначе None.
        Example:
           >>> revai_client = RevAiClient(api_token='your_api_token')
           >>> job_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
           >>> details = await revai_client.get_job_details(job_id)
           >>> print(details)
           {'id': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'created_on': '...', 'status': 'transcribed', ...}
        """
        url = f"{self.base_url}/jobs/{job_id}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    logger.info(f"Детали задания {job_id} получены.")
                    return data
        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при получении деталей задания: {e}")
            return None
        except Exception as ex:
            logger.error(f"Произошла непредвиденная ошибка {ex}")
            return None

    async def get_transcript(self, job_id: str) -> str | None:
        """
        Получает текст транскрипции.

        Args:
            job_id (str): ID задания транскрибирования.

        Returns:
            str | None: Текст транскрипции, если запрос успешен, иначе None.

        Example:
           >>> revai_client = RevAiClient(api_token='your_api_token')
           >>> job_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
           >>> transcript = await revai_client.get_transcript(job_id)
           >>> print(transcript)
           "Пример текста транскрипции."
        """
        url = f"{self.base_url}/jobs/{job_id}/transcript"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    response.raise_for_status()
                    transcript = await response.text()
                    logger.info(f"Транскрипция для задания {job_id} получена.")
                    return transcript
        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при получении транскрипции: {e}")
            return None
        except Exception as ex:
            logger.error(f"Произошла непредвиденная ошибка {ex}")
            return None
    
    async def delete_job(self, job_id: str) -> bool:
        """
        Удаляет задание транскрибирования.

        Args:
            job_id (str): ID задания транскрибирования.

        Returns:
            bool: True, если задание успешно удалено, иначе False.
         Example:
           >>> revai_client = RevAiClient(api_token='your_api_token')
           >>> job_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
           >>> result = await revai_client.delete_job(job_id)
           >>> print(result)
           True
        """
        url = f"{self.base_url}/jobs/{job_id}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.delete(url, headers=self.headers) as response:
                    response.raise_for_status()
                    logger.info(f"Задание {job_id} удалено.")
                    return True
        except aiohttp.ClientError as e:
            logger.error(f"Ошибка при удалении задания: {e}")
            return False
        except Exception as ex:
            logger.error(f"Произошла непредвиденная ошибка {ex}")
            return False
```