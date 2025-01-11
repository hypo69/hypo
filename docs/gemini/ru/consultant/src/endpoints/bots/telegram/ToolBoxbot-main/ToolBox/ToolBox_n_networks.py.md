# Анализ кода модуля `ToolBox_n_networks.py`

**Качество кода**
8
- Плюсы
    - Код структурирован в класс `neural_networks`, что обеспечивает его организованность.
    - Используются `requests` для выполнения HTTP запросов к API.
    - Присутствует обработка HTTP статусов ответов.
    - Есть использование переменных окружения для токенов доступа.
    - Использование `io.BytesIO` для обработки бинарных данных изображений.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не хватает docstring для класса и методов.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Использованы двойные кавычки в Python коде.
    - Нет обработки ошибок с помощью `logger.error`.
    - Избыточное использование циклов для перебора токенов.
    - Не приведены в соответствие имена переменных с ранее обработанными файлами.

**Рекомендации по улучшению**

1.  **Документирование**: Добавить docstring для класса `neural_networks` и его методов.
2.  **Импорты**: Добавить импорт `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
3.  **Форматирование**: Использовать одинарные кавычки для строк в Python коде и двойные только в операциях вывода.
4.  **Обработка ошибок**: Заменить `try-except` блоки на использование `logger.error` для обработки ошибок.
5.  **Оптимизация циклов**: Упростить циклы перебора токенов.
6.  **Использование j_loads**: Заменить `json.loads` на `j_loads`.
7.  **Соответствие именований**: Привести в соответствие имена переменных с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для работы с нейронными сетями.
=========================================================================================

Этот модуль содержит класс :class:`neural_networks`, который используется для взаимодействия с различными API
нейронных сетей, таких как Hugging Face, Mistral и Inference AI.

Пример использования
--------------------

Пример использования класса `neural_networks`:

.. code-block:: python

    networks = neural_networks()
    image = networks._FLUX_schnell(prompt='a cat', size=[512, 512], seed=42, num_inference_steps=20)
    text_data = networks._free_gpt_4o_mini(prompt=[{'role':'user', 'content':'hello'}])

"""
import requests
import os
import io
from random import randint
from PIL import Image
from src.utils.jjson import j_loads
from src.logger.logger import logger


class neural_networks:
    """
    Класс для взаимодействия с различными API нейронных сетей.

    Этот класс предоставляет методы для генерации изображений и текста с использованием
    моделей, размещенных на Hugging Face, Mistral и Inference AI.
    """

    def _FLUX_schnell(self, prompt: str, size: list[int, int], seed: int, num_inference_steps: int) -> Image.Image | None:
        """
        Генерирует изображение с использованием модели FLUX.1-schnell.

        Args:
            prompt (str): Текстовый запрос для генерации изображения.
            size (list[int, int]): Размеры изображения (ширина, высота).
            seed (int): Зерно для воспроизводимости результата.
            num_inference_steps (int): Количество шагов для генерации изображения.

        Returns:
            Image.Image | None: Объект изображения PIL или None, если произошла ошибка.
        """
        payload = {
            'inputs': prompt,
            'parameters': {
                'guidance_scale': 1.5,
                'num_inference_steps': num_inference_steps,
                'width': size[0],
                'height': size[1],
                'seed': seed
            }
        }
        for i in range(1, 7):
            try:
                response = requests.post(
                    'https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell',
                    headers={
                        'Authorization': 'Bearer ' + os.environ[f'HF_TOKEN{i}'],
                        'Content-Type': 'application/json'
                    },
                    json=payload
                )
                response.raise_for_status()  # Проверка статуса ответа
                image = Image.open(io.BytesIO(response.content))
                return image
            except requests.exceptions.RequestException as ex:
                logger.error(f'Ошибка при запросе к FLUX.1-schnell с токеном {i}: {ex}')
            except Exception as ex:
               logger.error(f'Ошибка при обработке ответа от FLUX.1-schnell: {ex}')
        return None

    def __mistral_large_2407(self, prompt: list[dict[str, str]]) -> tuple[str, int, int] | str:
        """
        Генерирует текст с использованием модели Mistral Large 2407.

        Args:
            prompt (list[dict[str, str]]): Список сообщений для модели.

        Returns:
            tuple[str, int, int] | str: Ответ модели, количество токенов в запросе и ответе,
            или сообщение об ошибке в виде строки.
        """
        data = {
            'messages': prompt,
            'temperature': 1.0,
            'top_p': 1.0,
            'max_tokens': 1024,
            'model': 'pixtral-12b-2409'
        }
        try:
            response = requests.post(
                'https://api.mistral.ai/v1/chat/completions',
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + os.environ['MISTRAL_TOKEN']
                },
                json=data
            )
            response.raise_for_status() # Проверка статуса ответа
            response_data = j_loads(response.text) # Используем j_loads вместо json.loads
            message = response_data['choices'][0]['message']
            prompt_tokens = response_data['usage']['prompt_tokens']
            completion_tokens = response_data['usage']['completion_tokens']
            return message, prompt_tokens, completion_tokens
        except requests.exceptions.RequestException as ex:
            logger.error(f'Ошибка при запросе к Mistral Large: {ex}')
            return f'Ошибка при запросе к Mistral Large: {ex}'
        except Exception as ex:
           logger.error(f'Ошибка при обработке ответа от Mistral Large: {ex}')
           return f'Ошибка при обработке ответа от Mistral Large: {ex}'
    def _free_gpt_4o_mini(self, prompt: list[dict[str, str]]) -> tuple[str, int, int] | str:
        """
        Генерирует текст с использованием модели gpt-4o-mini или fallback Mistral Large 2407.

        Args:
            prompt (list[dict[str, str]]): Список сообщений для модели.

        Returns:
            tuple[str, int, int] | str: Ответ модели, количество токенов в запросе и ответе,
            или сообщение об ошибке в виде строки.
        """
        data = {
            'messages': prompt,
            'temperature': 1.0,
            'top_p': 1.0,
            'max_tokens': 1024,
            'model': 'gpt-4o-mini'
        }
        for i in range(1, 7):
            try:
                response = requests.post(
                    'https://models.inference.ai.azure.com/chat/completions',
                    headers={
                        'Authorization': os.environ[f'GIT_TOKEN{i}'],
                        'Content-Type': 'application/json'
                    },
                    json=data
                )
                response.raise_for_status() # Проверка статуса ответа
                response_data = j_loads(response.text) # Используем j_loads вместо json.loads
                message = response_data['choices'][0]['message']
                prompt_tokens = response_data['usage']['prompt_tokens']
                completion_tokens = response_data['usage']['completion_tokens']
                return message, prompt_tokens, completion_tokens
            except requests.exceptions.RequestException as ex:
                logger.error(f'Ошибка при запросе к gpt-4o-mini с токеном {i}: {ex}')
            except Exception as ex:
                logger.error(f'Ошибка при обработке ответа от gpt-4o-mini: {ex}')

        return self.__mistral_large_2407(prompt)
```