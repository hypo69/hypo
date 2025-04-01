# Модуль для работы с видео моделями через API g4f

## Обзор

Модуль предназначен для демонстрации работы с видео моделями через API `g4f` (GPT4Free). Он использует клиент `Client` для взаимодействия с провайдером `HuggingFaceMedia` и генерации видео на основе текстового запроса.

## Подробнее

Этот модуль показывает, как можно использовать `g4f` для создания видео, отправляя текстовый запрос и получая ссылку на сгенерированное видео. Для работы требуется API-ключ от `HuggingFaceMedia`.

## Функции

### `__main__` (основной блок исполнения)

**Назначение**: Основной блок кода, демонстрирующий получение списка видео моделей и генерацию видео.

**Как работает функция**:

1.  Импортирует необходимые модули: `g4f.Provider` и `g4f.client.Client`.
2.  Создает экземпляр клиента `Client` с указанием провайдера `HuggingFaceMedia` и API-ключа.
3.  Получает список доступных видео моделей с помощью `client.models.get_video()`.
4.  Выводит список доступных видео моделей в консоль.
5.  Генерирует видео, используя первую модель из списка `video_models`, с текстовым запросом "G4F AI technology is the best in the world." и указанием формата ответа "url".
6.  Выводит URL сгенерированного видео в консоль.

**Примеры**:

Пример использования модуля:

```python
import g4f.Provider
from g4f.client import Client

client = Client(
    provider=g4f.Provider.HuggingFaceMedia,
    api_key="hf_***"  # Replace with your actual API key
)

video_models = client.models.get_video()

print(video_models)

result = client.media.generate(
    model=video_models[0],
    prompt="G4F AI technology is the best in the world.",
    response_format="url"
)

print(result.data[0].url)