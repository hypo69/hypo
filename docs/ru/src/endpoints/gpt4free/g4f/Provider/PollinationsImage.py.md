# Модуль PollinationsImage

## Обзор

Модуль `PollinationsImage` является частью проекта `hypotez` и предназначен для работы с изображениями, генерируемыми через API Pollinations AI. Он расширяет функциональность базового класса `PollinationsAI`, добавляя специфические параметры и логику для генерации изображений. Модуль предоставляет возможность асинхронной генерации изображений с использованием различных моделей и параметров.

## Подробней

Этот модуль предоставляет класс `PollinationsImage`, который позволяет пользователям генерировать изображения, используя API Pollinations AI. Он наследуется от класса `PollinationsAI` и добавляет специфические параметры для генерации изображений, такие как соотношение сторон, ширина, высота и другие. Модуль также обеспечивает асинхронную генерацию изображений, что позволяет эффективно использовать ресурсы и получать результаты в реальном времени.

## Классы

### `PollinationsImage`

**Описание**: Класс `PollinationsImage` предназначен для генерации изображений с использованием API Pollinations AI. Он наследуется от класса `PollinationsAI` и добавляет специфические параметры и логику для работы с изображениями.

**Наследует**:
- `PollinationsAI`: Базовый класс для взаимодействия с API Pollinations AI.

**Аттрибуты**:
- `label` (str): Метка класса, используется для идентификации провайдера. Значение: `"PollinationsImage"`.
- `default_model` (str): Модель, используемая по умолчанию для генерации изображений. Значение: `"flux"`.
- `default_vision_model` (None): Модель для обработки изображений, по умолчанию `None`.
- `default_image_model` (str): Псевдоним для `default_model`, модель для генерации изображений по умолчанию.
- `image_models` (list): Список поддерживаемых моделей для генерации изображений.
- `_models_loaded` (bool): Флаг, указывающий, были ли загружены модели.

**Методы**:
- `get_models(**kwargs)`: Возвращает список доступных моделей для генерации изображений.
- `create_async_generator(model: str, messages: Messages, proxy: str = None, prompt: str = None, aspect_ratio: str = "1:1", width: int = None, height: int = None, seed: Optional[int] = None, cache: bool = False, nologo: bool = True, private: bool = False, enhance: bool = False, safe: bool = False, n: int = 4, **kwargs) -> AsyncResult`: Асинхронно генерирует изображения на основе заданных параметров.

### `PollinationsImage.get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Получает список доступных моделей для генерации изображений.

        Args:
            **kwargs: Дополнительные аргументы (не используются).

        Returns:
            list: Список доступных моделей для генерации изображений.
        """
        ...
```

**Назначение**:
Метод `get_models` возвращает список доступных моделей для генерации изображений. Если модели еще не были загружены, он вызывает метод `get_models` родительского класса `PollinationsAI`, объединяет модели из родительского класса и дополнительные модели, а затем устанавливает флаг `_models_loaded` в `True`.

**Как работает функция**:

1. **Проверка загрузки моделей**: Проверяется, были ли загружены модели (`cls._models_loaded`).
2. **Загрузка моделей (если необходимо)**: Если модели не были загружены, выполняются следующие действия:
   - Вызывается метод `get_models` родительского класса (`super().get_models()`) для загрузки моделей, специфичных для родительского класса.
   - Объединяются модели из `cls.image_models`, `PollinationsAI.image_models` и `cls.extra_image_models` с использованием `dict.fromkeys` для удаления дубликатов и сохранения порядка.
   - Список объединенных моделей присваивается `cls.image_models`.
   - Устанавливается флаг `cls._models_loaded` в `True`.
3. **Возврат списка моделей**: Возвращается список доступных моделей для генерации изображений (`cls.image_models`).

**Примеры**:
```python
models = PollinationsImage.get_models()
print(models)
# Output: ['flux']
```

### `PollinationsImage.create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        prompt: str = None,
        aspect_ratio: str = "1:1",
        width: int = None,
        height: int = None,
        seed: Optional[int] = None,
        cache: bool = False,
        nologo: bool = True,
        private: bool = False,
        enhance: bool = False,
        safe: bool = False,
        n: int = 4,
        **kwargs
    ) -> AsyncResult:
        """Асинхронно генерирует изображения на основе заданных параметров.

        Args:
            model (str): Модель для генерации изображения.
            messages (Messages): Список сообщений для генерации изображения.
            proxy (str, optional): Прокси-сервер для подключения к API. По умолчанию `None`.
            prompt (str, optional): Дополнительный текст запроса. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию `"1:1"`.
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            seed (Optional[int], optional): Зерно для генерации случайных чисел. По умолчанию `None`.
            cache (bool, optional): Использовать кэш. По умолчанию `False`.
            nologo (bool, optional): Не добавлять логотип. По умолчанию `True`.
            private (bool, optional): Сделать изображение приватным. По умолчанию `False`.
            enhance (bool, optional): Улучшить качество изображения. По умолчанию `False`.
            safe (bool, optional): Включить безопасный режим. По умолчанию `False`.
            n (int, optional): Количество генерируемых изображений. По умолчанию `4`.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий чанки изображения.
        """
        ...
```

**Назначение**:
Метод `create_async_generator` асинхронно генерирует изображения на основе заданных параметров, используя API Pollinations AI. Он принимает различные параметры, такие как модель, сообщения, прокси, соотношение сторон и другие, и возвращает асинхронный генератор, который выдает чанки изображения.

**Как работает функция**:

1. **Обновление списка моделей**: Вызывается метод `cls.get_models()` для обновления списка доступных моделей.
2. **Асинхронная генерация изображений**: Вызывается метод `cls._generate_image()` с передачей всех необходимых параметров, включая форматированный запрос (`format_image_prompt`).
3. **Генерация чанков**: Метод `cls._generate_image()` возвращает асинхронный генератор, который выдает чанки изображения.
4. **Возврат асинхронного генератора**: Метод `create_async_generator` возвращает асинхронный генератор, который можно использовать для получения чанков изображения.

**Примеры**:
```python
async for chunk in PollinationsImage.create_async_generator(model="flux", messages=["cat"]):
    print(chunk)
# Output: <async_generator object PollinationsImage.create_async_generator at 0x...>
```

## Функции

В данном модуле функции отсутствуют.