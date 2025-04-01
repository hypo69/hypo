# Модуль `PollinationsImage`

## Обзор

Модуль `PollinationsImage` предназначен для работы с сервисом Pollinations AI для генерации изображений. Он расширяет возможности класса `PollinationsAI`, добавляя специфические параметры и логику для создания изображений. Модуль предоставляет асинхронный генератор для получения изображений на основе заданных параметров и промптов.

## Подробней

Этот модуль является частью проекта `hypotez` и служит для интеграции с API Pollinations AI, позволяя пользователям генерировать изображения, используя различные модели и параметры, такие как соотношение сторон, размеры, seed и другие. Он обеспечивает удобный интерфейс для взаимодействия с сервисом генерации изображений, а также кэширование и безопасную генерацию.

## Классы

### `PollinationsImage`

**Описание**: Класс `PollinationsImage` предназначен для генерации изображений с использованием API Pollinations AI. Он наследуется от класса `PollinationsAI` и добавляет специфические параметры и логику для создания изображений.

**Наследует**:
- `PollinationsAI`: Расширяет возможности базового класса `PollinationsAI` для работы с изображениями.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера изображений ("PollinationsImage").
- `default_model` (str): Модель, используемая по умолчанию для генерации изображений ("flux").
- `default_vision_model` (None): Модель компьютерного зрения по умолчанию (в данном случае `None`).
- `default_image_model` (str): Модель изображений по умолчанию (значение берется из `default_model` - "flux").
- `image_models` (list): Список поддерживаемых моделей изображений, содержащий `default_image_model`.
- `_models_loaded` (bool): Флаг, указывающий, были ли загружены модели (изначально `False`).

**Методы**:
- `get_models(**kwargs)`: Получает список доступных моделей, объединяя модели из родительского класса и дополнительные модели.
- `create_async_generator(...)`: Создает асинхронный генератор для генерации изображений на основе заданных параметров и промпта.

### `get_models`

```python
    @classmethod
    def get_models(cls, **kwargs):
        """Получает список доступных моделей, объединяя модели из родительского класса и дополнительные модели.

        Args:
            **kwargs: Дополнительные аргументы для получения моделей.

        Returns:
            list: Список доступных моделей изображений.
        """
```

**Назначение**: Метод `get_models` предназначен для получения и обновления списка доступных моделей для генерации изображений.

**Как работает функция**:

1. **Проверка загрузки моделей**: Проверяется, были ли уже загружены модели (`cls._models_loaded`).
2. **Загрузка моделей**: Если модели еще не были загружены (`cls._models_loaded` is `False`):
   - Вызывается метод `get_models` родительского класса (`super().get_models()`) для загрузки моделей из `PollinationsAI`.
   - Объединяются модели из `cls.image_models`, `PollinationsAI.image_models` и `cls.extra_image_models`, удаляя дубликаты с использованием `dict.fromkeys()`.
   - Обновляется `cls.image_models` объединенным списком моделей.
   - Устанавливается флаг `cls._models_loaded` в `True`, чтобы указать, что модели были загружены.
3. **Возврат моделей**: Возвращается список доступных моделей изображений (`cls.image_models`).

**ASCII flowchart**:

```
Проверка загрузки моделей (cls._models_loaded)
│
└─── False:
│    │
│    Вызов get_models родительского класса (super().get_models())
│    │
│    Объединение и дедупликация моделей
│    │
│    Обновление cls.image_models
│    │
│    Установка cls._models_loaded в True
│    │
└─── True:
│
Возврат cls.image_models
```

**Примеры**:

```python
# Пример вызова метода get_models
models = PollinationsImage.get_models()
print(models)  # Вывод: ['flux', 'модель_из_PollinationsAI', 'дополнительная_модель']
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
        """Создает асинхронный генератор для генерации изображений на основе заданных параметров и промпта.

        Args:
            model (str): Модель для генерации изображений.
            messages (Messages): Сообщения, используемые для формирования промпта.
            proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
            prompt (str, optional): Дополнительный промпт. По умолчанию `None`.
            aspect_ratio (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
            width (int, optional): Ширина изображения. По умолчанию `None`.
            height (int, optional): Высота изображения. По умолчанию `None`.
            seed (Optional[int], optional): Seed для генерации. По умолчанию `None`.
            cache (bool, optional): Использовать кэш. По умолчанию `False`.
            nologo (bool, optional): Удалять логотип. По умолчанию `True`.
            private (bool, optional): Приватная генерация. По умолчанию `False`.
            enhance (bool, optional): Улучшать изображение. По умолчанию `False`.
            safe (bool, optional): Безопасная генерация. По умолчанию `False`.
            n (int, optional): Количество генерируемых изображений. По умолчанию 4.
            **kwargs: Дополнительные аргументы.

        Yields:
            chunk: Часть сгенерированного изображения.
        """
```

**Назначение**: Метод `create_async_generator` создает асинхронный генератор для генерации изображений на основе заданных параметров и промпта.

**Параметры**:
- `model` (str): Модель для генерации изображений.
- `messages` (Messages): Сообщения, используемые для формирования промпта.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `prompt` (str, optional): Дополнительный промпт. По умолчанию `None`.
- `aspect_ratio` (str, optional): Соотношение сторон изображения. По умолчанию "1:1".
- `width` (int, optional): Ширина изображения. По умолчанию `None`.
- `height` (int, optional): Высота изображения. По умолчанию `None`.
- `seed` (Optional[int], optional): Seed для генерации. По умолчанию `None`.
- `cache` (bool, optional): Использовать кэш. По умолчанию `False`.
- `nologo` (bool, optional): Удалять логотип. По умолчанию `True`.
- `private` (bool, optional): Приватная генерация. По умолчанию `False`.
- `enhance` (bool, optional): Улучшать изображение. По умолчанию `False`.
- `safe` (bool, optional): Безопасная генерация. По умолчанию `False`.
- `n` (int, optional): Количество генерируемых изображений. По умолчанию 4.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий части сгенерированного изображения.

**Как работает функция**:

1. **Обновление моделей**: Вызывается метод `get_models()` для обновления списка доступных моделей.
2. **Асинхронная генерация изображений**:
   - Вызывается метод `_generate_image` для асинхронной генерации изображений с переданными параметрами.
   - Формируется промпт с использованием `format_image_prompt`.
3. **Генерация чанков**: Асинхронно перебираются чанки, генерируемые методом `_generate_image`, и каждый чанк возвращается через `yield`.

**ASCII flowchart**:

```
Обновление моделей (cls.get_models())
│
└───
│
Вызов _generate_image с параметрами
│
└───
│
Формирование промпта (format_image_prompt)
│
└───
│
Асинхронный перебор чанков
│
└───
│
Yield chunk
```

**Примеры**:

```python
# Пример использования async generator
async def main():
    async for chunk in PollinationsImage.create_async_generator(model='flux', messages='Example'):
        print(chunk)

import asyncio
asyncio.run(main())