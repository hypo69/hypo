# Анализ кода модуля `src.ai.helicone.README.MD`

**Качество кода**
8
-  Плюсы
    - Документ хорошо структурирован, предоставляет ясное описание класса `HeliconeAI` и его методов.
    - Приведены примеры использования, которые помогают понять, как применять класс.
    - Имеется информация об установке и зависимостях.
-  Минусы
    - Документация не в формате reStructuredText (RST), что требуется согласно инструкции.
    - Отсутствует подробное описание каждого метода в формате RST.
    - Не используется `logger` для обработки ошибок и логирования, что также необходимо.

**Рекомендации по улучшению**
1. Перевести всю документацию в формат RST.
2. Добавить более подробные docstring к каждому методу, включая описание параметров и возвращаемых значений.
3. Добавить блок с описанием модуля в формате RST в начале файла.
4. Использовать `logger` для логирования ошибок и отладки.
5. Проверить и добавить отсутствующие импорты, если таковые требуются.

**Оптимизированный код**
```markdown
.. module:: src.ai.helicone
   :synopsis: Модуль для интеграции с Helicone.ai и OpenAI.

=========================================================================================

Этот модуль предоставляет класс :class:`HeliconeAI`, который используется для взаимодействия с моделями Helicone.ai и OpenAI.

.. code-block:: python

    from src.ai.helicone.helicone_ai import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print(poem)
    
[Русский](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/readme.ru.md)
[About `helicone.ai`](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/about.ru.md)

# HeliconeAI: Integration with Helicone.ai and OpenAI

## Overview

The `HeliconeAI` class is designed to facilitate interaction with Helicone.ai and OpenAI's models. This class provides methods for generating poems, analyzing sentiment, summarizing text, and translating text. It also includes logging of completions using Helicone.ai.

## Key Features

1.  **Poem Generation**:
    - Generates a poem based on a given prompt using the `gpt-3.5-turbo` model.

2.  **Sentiment Analysis**:
    - Analyzes the sentiment of a given text using the `text-davinci-003` model.

3.  **Text Summarization**:
    - Summarizes a given text using the `text-davinci-003` model.

4.  **Text Translation**:
    - Translates a given text to a specified target language using the `text-davinci-003` model.

5.  **Completion Logging**:
    - Logs all completions using Helicone.ai for monitoring and analysis.

## Installation

To use the `HeliconeAI` class, ensure you have the necessary dependencies installed. You can install them using pip:

```bash
pip install openai helicone
```

## Usage

### Initialization

Initialize the `HeliconeAI` class:

```python
from helicone import Helicone
from openai import OpenAI
# Добавлен импорт logger из src.logger.logger
from src.logger.logger import logger 

class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    :ivar helicone: Экземпляр класса Helicone для логирования.
    :ivar client: Экземпляр класса OpenAI для работы с моделями.
    """
    def __init__(self):
        """Инициализирует Helicone и OpenAI клиенты."""
        self.helicone = Helicone()
        self.client = OpenAI()
```

### Methods

#### Generate Poem

Generate a poem based on a given prompt:

```python
    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        :param prompt: Текст промпта для генерации стихотворения.
        :return: Сгенерированное стихотворение.
        """
        try:
            # Код отправляет запрос в OpenAI для генерации стиха
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            # Код логирует результат через Helicone
            self.helicone.log_completion(response)
            # Код возвращает сгенерированное стих из ответа
            return response.choices[0].message.content
        except Exception as ex:
             # Код логирует ошибку
            logger.error(f'Ошибка при генерации стихотворения: {ex}')
            return ''
```

#### Analyze Sentiment

Analyze the sentiment of a given text:

```python
    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа тональности.
        :return: Тональность текста.
        """
        try:
            # Код отправляет запрос в OpenAI для анализа тональности
            response = self.client.completions.create(
                model="text-davinci-003",
                prompt=f"Analyze the sentiment of the following text: {text}",
                max_tokens=50
            )
            # Код логирует результат через Helicone
            self.helicone.log_completion(response)
            # Код возвращает результат анализа тональности
            return response.choices[0].text.strip()
        except Exception as ex:
             # Код логирует ошибку
            logger.error(f'Ошибка при анализе тональности: {ex}')
            return ''
```

#### Summarize Text

Summarize a given text:

```python
    def summarize_text(self, text: str) -> str:
        """
        Суммирует заданный текст.

        :param text: Текст для суммирования.
        :return: Суммированный текст.
        """
        try:
            # Код отправляет запрос в OpenAI для суммирования текста
            response = self.client.completions.create(
                model="text-davinci-003",
                prompt=f"Summarize the following text: {text}",
                max_tokens=100
            )
            # Код логирует результат через Helicone
            self.helicone.log_completion(response)
            # Код возвращает суммированный текст
            return response.choices[0].text.strip()
        except Exception as ex:
             # Код логирует ошибку
            logger.error(f'Ошибка при суммировании текста: {ex}')
            return ''
```

#### Translate Text

Translate a given text to a specified target language:

```python
    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный язык.

        :param text: Текст для перевода.
        :param target_language: Язык, на который нужно перевести текст.
        :return: Переведенный текст.
        """
        try:
            # Код отправляет запрос в OpenAI для перевода текста
            response = self.client.completions.create(
                model="text-davinci-003",
                prompt=f"Translate the following text to {target_language}: {text}",
                max_tokens=200
            )
            # Код логирует результат через Helicone
            self.helicone.log_completion(response)
            # Код возвращает переведенный текст
            return response.choices[0].text.strip()
        except Exception as ex:
             # Код логирует ошибку
            logger.error(f'Ошибка при переводе текста: {ex}')
            return ''
```

### Example Usage

Here is an example of how to use the `HeliconeAI` class:

```python
def main():
    """Пример использования класса HeliconeAI."""
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\\n", translation)

if __name__ == "__main__":
    main()
```

## Dependencies

- `helicone`
- `openai`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more detailed information, refer to the source code and comments within the `HeliconeAI` class.
```