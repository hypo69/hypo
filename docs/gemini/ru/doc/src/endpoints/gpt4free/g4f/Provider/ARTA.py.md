# Модуль ARTA

## Обзор

Модуль `ARTA` предоставляет класс `ARTA`, который является асинхронным провайдером для генерации изображений с использованием AI-сервиса ARTA. Он поддерживает создание токенов аутентификации, их обновление и генерацию изображений на основе текстовых запросов.

## Подробней

Этот модуль предназначен для интеграции с AI-сервисом ARTA для генерации изображений. Он включает в себя механизмы аутентификации, запросы на генерацию изображений и проверку статуса генерации. Модуль использует асинхронные запросы для неблокирующей работы.

## Классы

### `ARTA`

**Описание**: Класс `ARTA` является асинхронным провайдером для генерации изображений с использованием AI-сервиса ARTA. Он наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`.

**Принцип работы**:
Класс реализует методы для аутентификации, обновления токенов и генерации изображений. Он использует асинхронные запросы к API ARTA для выполнения этих операций. Класс также предоставляет возможность выбора различных моделей для генерации изображений.

**Методы**:

- `get_auth_file`: Возвращает путь к файлу, в котором хранится информация об аутентификации.
- `create_token`: Создает новый токен аутентификации.
- `refresh_token`: Обновляет существующий токен аутентификации.
- `read_and_refresh_token`: Читает существующий токен аутентификации и, если необходимо, обновляет его.
- `create_async_generator`: Создает асинхронный генератор для генерации изображений на основе текстового запроса.

### `get_auth_file`

```python
    @classmethod
    def get_auth_file(cls):
        """ Возвращает путь к файлу, в котором хранится информация об аутентификации.

        Args:
            cls: Ссылка на класс.

        Returns:
            Path: Путь к файлу аутентификации.

        Как работает функция:
        1. Определяет путь к директории для хранения cookies.
        2. Создает директорию, если она не существует.
        3. Формирует имя файла аутентификации на основе имени класса.
        4. Возвращает объект `Path`, представляющий путь к файлу аутентификации.
        """
```

**Примеры**:
```python
# Пример использования метода get_auth_file
file_path = ARTA.get_auth_file()
print(file_path)
```

### `create_token`

```python
    @classmethod
    async def create_token(cls, path: Path, proxy: str | None = None):
        """ Создает новый токен аутентификации.

        Args:
            cls: Ссылка на класс.
            path (Path): Путь для сохранения данных аутентификации.
            proxy (str | None, optional): Прокси-сервер для использования. По умолчанию None.

        Returns:
            dict: Данные аутентификации.

        Raises:
            ResponseError: Если не удается получить токен аутентификации.

        Как работает функция:
        1. Отправляет POST-запрос на URL аутентификации для генерации токена.
        2. Извлекает токен из ответа.
        3. Сохраняет данные аутентификации в файл.
        4. Возвращает данные аутентификации.
        """
```

**Примеры**:
```python
# Пример использования метода create_token
import asyncio
from pathlib import Path

async def main():
    path = Path("auth_arta.json")
    token_data = await ARTA.create_token(path)
    print(token_data)

if __name__ == "__main__":
    asyncio.run(main())
```

### `refresh_token`

```python
    @classmethod
    async def refresh_token(cls, refresh_token: str, proxy: str = None) -> tuple[str, str]:
        """ Обновляет существующий токен аутентификации.

        Args:
            cls: Ссылка на класс.
            refresh_token (str): Токен обновления.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию None.

        Returns:
            tuple[str, str]: Новый токен и токен обновления.

        Как работает функция:
        1. Отправляет POST-запрос на URL обновления токена с токеном обновления.
        2. Извлекает новый токен и токен обновления из ответа.
        3. Возвращает новый токен и токен обновления.
        """
```

**Примеры**:
```python
# Пример использования метода refresh_token
import asyncio

async def main():
    refresh_token = "old_refresh_token"  # Замените на актуальный токен обновления
    new_token, new_refresh_token = await ARTA.refresh_token(refresh_token)
    print(f"New token: {new_token}, New refresh token: {new_refresh_token}")

if __name__ == "__main__":
    asyncio.run(main())
```

### `read_and_refresh_token`

```python
    @classmethod
    async def read_and_refresh_token(cls, proxy: str | None = None) -> str:
        """ Читает существующий токен аутентификации и, если необходимо, обновляет его.

        Args:
            cls: Ссылка на класс.
            proxy (str | None, optional): Прокси-сервер для использования. По умолчанию None.

        Returns:
            dict: Данные аутентификации.

        Как работает функция:
        1. Проверяет наличие файла аутентификации.
        2. Если файл существует, загружает данные аутентификации из файла.
        3. Проверяет, не истек ли срок действия токена.
        4. Если срок действия токена истек или подходит к концу, обновляет токен.
        5. Возвращает данные аутентификации.
        """
```

**Примеры**:
```python
# Пример использования метода read_and_refresh_token
import asyncio

async def main():
    auth_data = await ARTA.read_and_refresh_token()
    print(auth_data)

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
        """ Создает асинхронный генератор для генерации изображений на основе текстового запроса.

        Args:
            cls: Ссылка на класс.
            model (str): Модель для генерации изображений.
            messages (Messages): Сообщения для формирования запроса.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию None.
            prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию None.
            negative_prompt (str, optional): Негативный запрос для генерации изображения. По умолчанию "blurry, deformed hands, ugly".
            n (int, optional): Количество изображений для генерации. По умолчанию 1.
            guidance_scale (int, optional): Масштаб соответствия запросу. По умолчанию 7.
            num_inference_steps (int, optional): Количество шагов для генерации изображения. По умолчанию 30.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            seed (int, optional): Зерно для генерации случайных чисел. По умолчанию None.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор для получения результатов генерации изображений.

        Raises:
            ResponseError: Если не удается инициировать генерацию изображения или если генерация завершается с ошибкой.

        Как работает функция:
        1. Выбирает модель для генерации изображений.
        2. Формирует текстовый запрос на основе сообщений.
        3. Генерирует случайное зерно, если оно не предоставлено.
        4. Получает токен аутентификации.
        5. Отправляет POST-запрос на URL генерации изображений с параметрами запроса.
        6. Проверяет статус генерации изображения.
        7. Возвращает URL-адреса сгенерированных изображений.
        """
```

**Примеры**:
```python
# Пример использования метода create_async_generator
import asyncio

async def main():
    messages = [{"role": "user", "content": "A cat wearing a hat"}]
    async for result in ARTA.create_async_generator(model="Flux", messages=messages):
        print(result)

if __name__ == "__main__":
    asyncio.run(main())