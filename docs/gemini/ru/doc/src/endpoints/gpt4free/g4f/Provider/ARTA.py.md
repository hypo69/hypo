# Модуль для работы с ARTA API
=================================================

Модуль содержит класс `ARTA`, который используется для взаимодействия с API ARTA для генерации изображений на основе текстовых запросов.
Он предоставляет асинхронные методы для аутентификации, обновления токенов и создания изображений.

Пример использования
----------------------

```python
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA
import asyncio

async def main():
    model = "Flux"
    messages = [{"role": "user", "content": "cat"}]
    async for response in ARTA.create_async_generator(model=model, messages=messages):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

## Обзор

Этот модуль предназначен для асинхронного взаимодействия с API ARTA для генерации изображений.
Он включает в себя механизмы аутентификации, обновления токенов и обработки запросов на генерацию изображений.

## Подробнее

Модуль `ARTA` предоставляет функциональность для аутентификации, обновления токенов и генерации изображений с использованием API ARTA.
Он использует асинхронные запросы для эффективного взаимодействия с API и включает обработку ошибок для обеспечения стабильной работы.

## Классы

### `ARTA`

**Описание**: Класс `ARTA` является основным классом для взаимодействия с API ARTA. Он наследует `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию результатов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL API ARTA.
- `auth_url` (str): URL для аутентификации.
- `token_refresh_url` (str): URL для обновления токена.
- `image_generation_url` (str): URL для генерации изображений.
- `status_check_url` (str): URL для проверки статуса генерации изображений.
- `working` (bool): Указывает, работает ли провайдер.
- `default_model` (str): Модель по умолчанию.
- `default_image_model` (str): Модель изображений по умолчанию.
- `model_aliases` (dict): Словарь псевдонимов моделей.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей.

**Методы**:
- `get_auth_file()`: Возвращает путь к файлу аутентификации.
- `create_token(path: Path, proxy: Optional[str] = None)`: Создает токен аутентификации.
- `refresh_token(refresh_token: str, proxy: Optional[str] = None)`: Обновляет токен аутентификации.
- `read_and_refresh_token(proxy: Optional[str] = None)`: Читает и обновляет токен аутентификации.
- `create_async_generator(model: str, messages: Messages, proxy: Optional[str] = None, prompt: Optional[str] = None, negative_prompt: str = "blurry, deformed hands, ugly", n: int = 1, guidance_scale: int = 7, num_inference_steps: int = 30, aspect_ratio: str = "1:1", seed: Optional[int] = None, **kwargs)`: Создает асинхронный генератор для генерации изображений.

### `get_auth_file`

```python
    @classmethod
    def get_auth_file(cls) -> Path:
        """
        Возвращает путь к файлу, в котором хранится информация об аутентификации.

        Returns:
            Path: Объект Path, представляющий путь к файлу аутентификации.
        """
        ...
```
**Назначение**: Возвращает путь к файлу аутентификации.

**Как работает функция**:
1. Получает директорию для хранения cookies.
2. Создает директорию, если она не существует.
3. Формирует имя файла аутентификации на основе имени класса.
4. Возвращает объект `Path`, представляющий путь к файлу.

```
Получение директории для cookies
↓
Создание директории, если не существует
↓
Формирование имени файла аутентификации
↓
Возврат объекта Path
```

**Примеры**:

```python
from pathlib import Path
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA

# Получение пути к файлу аутентификации
auth_file_path = ARTA.get_auth_file()
print(f"Путь к файлу аутентификации: {auth_file_path}")
```
### `create_token`

```python
    @classmethod
    async def create_token(cls, path: Path, proxy: str | None = None) -> dict:
        """
        Создает токен аутентификации, используя API Google Identity Toolkit.

        Args:
            path (Path): Путь для сохранения данных аутентификации.
            proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

        Returns:
            dict: Данные аутентификации, содержащие токен.

        Raises:
            ResponseError: Если не удается получить токен аутентификации.
        """
        ...
```

**Назначение**: Создает токен аутентификации, используя API Google Identity Toolkit.

**Параметры**:
- `path` (Path): Путь для сохранения данных аутентификации.
- `proxy` (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `dict`: Данные аутентификации, содержащие токен.

**Вызывает исключения**:
- `ResponseError`: Если не удается получить токен аутентификации.

**Как работает функция**:
1. Создает асинхронную сессию клиента.
2. Формирует полезную нагрузку для запроса аутентификации.
3. Отправляет POST-запрос к API Google Identity Toolkit.
4. Извлекает токен аутентификации из ответа.
5. Сохраняет данные аутентификации в файл.
6. Возвращает данные аутентификации.

```
Создание асинхронной сессии
↓
Формирование полезной нагрузки
↓
Отправка POST-запроса
↓
Извлечение токена
↓
Сохранение данных в файл
↓
Возврат данных
```

**Примеры**:

```python
import asyncio
from pathlib import Path
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA

async def main():
    path = Path("auth.json")
    auth_data = await ARTA.create_token(path)
    print(f"Данные аутентификации: {auth_data}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `refresh_token`

```python
    @classmethod
    async def refresh_token(cls, refresh_token: str, proxy: str | None = None) -> tuple[str, str]:
        """
        Обновляет токен аутентификации, используя refresh token.

        Args:
            refresh_token (str): Refresh token для обновления.
            proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

        Returns:
            tuple[str, str]: Новый токен и refresh token.
        """
        ...
```

**Назначение**: Обновляет токен аутентификации, используя refresh token.

**Параметры**:
- `refresh_token` (str): Refresh token для обновления.
- `proxy` (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `tuple[str, str]`: Новый токен и refresh token.

**Как работает функция**:
1. Создает асинхронную сессию клиента.
2. Формирует полезную нагрузку для запроса обновления токена.
3. Отправляет POST-запрос к API обновления токена.
4. Извлекает новый токен и refresh token из ответа.
5. Возвращает новый токен и refresh token.

```
Создание асинхронной сессии
↓
Формирование полезной нагрузки
↓
Отправка POST-запроса
↓
Извлечение нового токена и refresh token
↓
Возврат нового токена и refresh token
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA

async def main():
    refresh_token = "some_refresh_token"  # <Замените на реальный refresh token>
    new_token, new_refresh_token = await ARTA.refresh_token(refresh_token)
    print(f"Новый токен: {new_token}, Новый refresh token: {new_refresh_token}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `read_and_refresh_token`

```python
    @classmethod
    async def read_and_refresh_token(cls, proxy: str | None = None) -> dict:
        """
        Читает токен из файла и обновляет его, если он устарел.

        Args:
            proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

        Returns:
            dict: Данные аутентификации, содержащие токен.
        """
        ...
```

**Назначение**: Читает токен из файла и обновляет его, если он устарел.

**Параметры**:
- `proxy` (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.

**Возвращает**:
- `dict`: Данные аутентификации, содержащие токен.

**Как работает функция**:
1. Получает путь к файлу аутентификации.
2. Проверяет, существует ли файл.
3. Если файл существует, загружает данные аутентификации из файла.
4. Проверяет, устарел ли токен.
5. Если токен устарел, обновляет его.
6. Возвращает данные аутентификации.
7. Если файл не существует или произошла ошибка, создает новый токен.

```
Получение пути к файлу аутентификации
↓
Проверка существования файла
↓
Загрузка данных из файла (если существует)
↓
Проверка устаревания токена
↓
Обновление токена (если устарел)
↓
Возврат данных аутентификации
↓
Создание нового токена (если файл не существует или произошла ошибка)
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA

async def main():
    auth_data = await ARTA.read_and_refresh_token()
    print(f"Данные аутентификации: {auth_data}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        prompt: str = None,
        negative_prompt: str = "blurry, deformed hands, ugly",
        n: int = 1,
        guidance_scale: int = 7,
        num_inference_steps: int = 30,
        aspect_ratio: str = "1:1",
        seed: int = None,
        **kwargs
    ) -> AsyncResult:
        """
        Создает асинхронный генератор для генерации изображений на основе текстового запроса.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Список сообщений, содержащих текстовый запрос.
            proxy (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.
            prompt (Optional[str], optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            negative_prompt (Optional[str], optional): Негативный запрос для генерации изображения. По умолчанию "blurry, deformed hands, ugly".
            n (int, optional): Количество изображений для генерации. По умолчанию 1.
            guidance_scale (int, optional): Масштаб соответствия запросу. По умолчанию 7.
            num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 30.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            seed (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            **kwargs: Дополнительные аргументы.

        Yields:
            AsyncResult: Результаты генерации изображения.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для генерации изображений на основе текстового запроса.

**Параметры**:
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Список сообщений, содержащих текстовый запрос.
- `proxy` (Optional[str], optional): Прокси-сервер для использования. По умолчанию `None`.
- `prompt` (Optional[str], optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `negative_prompt` (Optional[str], optional): Негативный запрос для генерации изображения. По умолчанию "blurry, deformed hands, ugly".
- `n` (int, optional): Количество изображений для генерации. По умолчанию 1.
- `guidance_scale` (int, optional): Масштаб соответствия запросу. По умолчанию 7.
- `num_inference_steps` (int, optional): Количество шагов для генерации изображения. По умолчанию 30.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
- `seed` (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий результаты генерации изображения.

**Как работает функция**:
1. Получает модель для генерации изображений.
2. Форматирует текстовый запрос.
3. Генерирует случайное зерно, если оно не предоставлено.
4. Получает токен аутентификации.
5. Создает асинхронную сессию клиента.
6. Формирует полезную нагрузку для запроса генерации изображения.
7. Отправляет POST-запрос к API генерации изображения.
8. Извлекает ID записи из ответа.
9. Проверяет статус генерации изображения.
10. Возвращает URL-адреса сгенерированных изображений.

```
Получение модели
↓
Форматирование запроса
↓
Генерация зерна (если не предоставлено)
↓
Получение токена аутентификации
↓
Создание асинхронной сессии
↓
Формирование полезной нагрузки
↓
Отправка POST-запроса
↓
Извлечение ID записи
↓
Проверка статуса генерации
↓
Возврат URL-адресов изображений
```

**Примеры**:

```python
import asyncio
from src.endpoints.gpt4free.g4f.Provider.ARTA import ARTA

async def main():
    model = "Flux"
    messages = [{"role": "user", "content": "cat"}]
    async for response in ARTA.create_async_generator(model=model, messages=messages):
        print(response)

if __name__ == "__main__":
    asyncio.run(main())
```
## Функции

В данном модуле нет отдельных функций, не относящихся к классам.