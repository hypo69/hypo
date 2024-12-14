# Анализ кода модуля `readme.ru.md`

**Качество кода: 7/10**

- **Плюсы:**
    - Документ содержит подробное описание класса `HeliconeAI` и его методов.
    - Приведены примеры использования, которые помогают понять, как применять этот класс.
    - Документ содержит информацию об установке, зависимостях и лицензии.
    - Использованы Markdown-заголовки, что делает структуру документа понятной.
- **Минусы:**
    - Документ представляет собой README, а не код, и поэтому не подлежит проверке как код Python.
    - Нет документации в формате reStructuredText (RST) внутри кода Python.
    - Примеры кода не соответствуют требованиям по форматированию docstring.
    - Отсутствует использование `logger` для обработки ошибок.
    - Не хватает информации о том, как настроить API-ключи для Helicone и OpenAI.
    - Код в примере не содержит обработки возможных ошибок при вызове API.
    - Не указан путь до файла `about.ru.md` относительно данного файла.
    - Не указан путь до файла LICENSE относительно данного файла.

**Рекомендации по улучшению**

1.  **Формат документации:** Необходимо переписать документацию к классу и методам в формате reStructuredText (RST) и разместить ее непосредственно в коде.
2.  **Обработка ошибок:** Добавить обработку ошибок с использованием `logger.error` вместо общих `try-except`.
3.  **Логирование:** Обеспечить логирование важных событий, таких как успешное выполнение запросов и возникновение ошибок.
4.  **Конфигурация:** Добавить информацию о том, как настроить API-ключи для Helicone и OpenAI, и как их передать в класс.
5.  **Примеры кода:** Привести примеры кода в соответствие с требованиями к оформлению docstring.
6.  **Зависимости:** Уточнить версии пакетов `helicone` и `openai`.

**Оптимизированный код**

```markdown
# Анализ кода модуля `readme.ru.md`

**Качество кода: 7/10**

- **Плюсы:**
    - Документ содержит подробное описание класса `HeliconeAI` и его методов.
    - Приведены примеры использования, которые помогают понять, как применять этот класс.
    - Документ содержит информацию об установке, зависимостях и лицензии.
    - Использованы Markdown-заголовки, что делает структуру документа понятной.
- **Минусы:**
    - Документ представляет собой README, а не код, и поэтому не подлежит проверке как код Python.
    - Нет документации в формате reStructuredText (RST) внутри кода Python.
    - Примеры кода не соответствуют требованиям по форматированию docstring.
    - Отсутствует использование `logger` для обработки ошибок.
    - Не хватает информации о том, как настроить API-ключи для Helicone и OpenAI.
    - Код в примере не содержит обработки возможных ошибок при вызове API.
    - Не указан путь до файла `about.ru.md` относительно данного файла.
    - Не указан путь до файла LICENSE относительно данного файла.

**Рекомендации по улучшению**

1.  **Формат документации:** Необходимо переписать документацию к классу и методам в формате reStructuredText (RST) и разместить ее непосредственно в коде.
2.  **Обработка ошибок:** Добавить обработку ошибок с использованием `logger.error` вместо общих `try-except`.
3.  **Логирование:** Обеспечить логирование важных событий, таких как успешное выполнение запросов и возникновение ошибок.
4.  **Конфигурация:** Добавить информацию о том, как настроить API-ключи для Helicone и OpenAI, и как их передать в класс.
5.  **Примеры кода:** Привести примеры кода в соответствие с требованиями к оформлению docstring.
6.  **Зависимости:** Уточнить версии пакетов `helicone` и `openai`.

**Оптимизированный код**

```python
"""
Модуль для интеграции с Helicone.ai и OpenAI
=========================================================================================

Этот модуль предоставляет класс :class:`HeliconeAI`, который упрощает взаимодействие с Helicone.ai
и моделями OpenAI. Класс включает методы для генерации стихов, анализа тональности,
создания краткого изложения и перевода текста.

Пример использования
--------------------

Пример использования класса `HeliconeAI`:

.. code-block:: python

    from src.ai.helicone import HeliconeAI

    helicone_ai = HeliconeAI()
    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print(poem)
"""

from helicone import Helicone
from openai import OpenAI
from typing import Any
from src.logger.logger import logger  # Импорт logger

class HeliconeAI:
    """
    Класс для взаимодействия с Helicone.ai и OpenAI.

    :param helicone_api_key: API ключ для Helicone.ai.
    :param openai_api_key: API ключ для OpenAI.
    """
    def __init__(self, helicone_api_key: str = None, openai_api_key: str = None):
        """
        Инициализирует экземпляр класса HeliconeAI.

        :param helicone_api_key: API ключ для Helicone.ai.
        :param openai_api_key: API ключ для OpenAI.
        """
        self.helicone = Helicone(api_key=helicone_api_key)  # Инициализация Helicone с API ключом
        self.client = OpenAI(api_key=openai_api_key)  # Инициализация OpenAI с API ключом

    def generate_poem(self, prompt: str) -> str:
        """
        Генерирует стихотворение на основе заданного промпта.

        :param prompt: Текст промпта для генерации стихотворения.
        :return: Сгенерированное стихотворение.
        """
        try: #  Обработка ошибок при вызове API
            response = self.client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'user', 'content': prompt}
                ]
            )
            self.helicone.log_completion(response) # Логирование завершения через Helicone
            return response.choices[0].message.content
        except Exception as ex:
            logger.error('Ошибка при генерации стихотворения', ex)  # Логирование ошибки
            return '' # Возвращаем пустую строку, чтобы не прерывать выполнение

    def analyze_sentiment(self, text: str) -> str:
        """
        Анализирует тональность заданного текста.

        :param text: Текст для анализа тональности.
        :return: Результат анализа тональности.
        """
        try: #  Обработка ошибок при вызове API
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Analyze the sentiment of the following text: {text}',
                max_tokens=50
            )
            self.helicone.log_completion(response) # Логирование завершения через Helicone
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка при анализе тональности', ex) # Логирование ошибки
            return ''  # Возвращаем пустую строку, чтобы не прерывать выполнение

    def summarize_text(self, text: str) -> str:
        """
        Создает краткое изложение заданного текста.

        :param text: Текст для краткого изложения.
        :return: Краткое изложение текста.
        """
        try: #  Обработка ошибок при вызове API
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Summarize the following text: {text}',
                max_tokens=100
            )
            self.helicone.log_completion(response) # Логирование завершения через Helicone
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка при создании краткого изложения', ex)  # Логирование ошибки
            return '' # Возвращаем пустую строку, чтобы не прерывать выполнение

    def translate_text(self, text: str, target_language: str) -> str:
        """
        Переводит заданный текст на указанный целевой язык.

        :param text: Текст для перевода.
        :param target_language: Целевой язык для перевода.
        :return: Переведенный текст.
        """
        try:  # Обработка ошибок при вызове API
            response = self.client.completions.create(
                model='text-davinci-003',
                prompt=f'Translate the following text to {target_language}: {text}',
                max_tokens=200
            )
            self.helicone.log_completion(response)  # Логирование завершения через Helicone
            return response.choices[0].text.strip()
        except Exception as ex:
            logger.error('Ошибка при переводе текста', ex)  # Логирование ошибки
            return ''  # Возвращаем пустую строку, чтобы не прерывать выполнение


def main():
    """
    Пример использования класса HeliconeAI.
    """
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem('Напиши мне стихотворение про кота.')
    print('Generated Poem:\\n', poem)

    sentiment = helicone_ai.analyze_sentiment('Сегодня был отличный день!')
    print('Sentiment Analysis:\\n', sentiment)

    summary = helicone_ai.summarize_text('Длинный текст для изложения...')
    print('Summary:\\n', summary)

    translation = helicone_ai.translate_text('Hello, how are you?', 'русский')
    print('Translation:\\n', translation)

if __name__ == '__main__':
    main()
```

```markdown
[English](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/README.MD)
[что такое `helicone.ai`](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/about.ru.md)
# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для упрощения взаимодействия с Helicone.ai и моделями OpenAI. Этот класс предоставляет методы для генерации стихов, анализа тональности текста, создания краткого изложения текста и перевода текста. Он также включает логирование завершений с использованием Helicone.ai.

## Основные особенности

1.  **Генерация стихотворения**:
    - Генерирует стихотворение на основе заданного промпта с использованием модели `gpt-3.5-turbo`.

2.  **Анализ тональности**:
    - Анализирует тональность заданного текста с использованием модели `text-davinci-003`.

3.  **Краткое изложение текста**:
    - Создает краткое изложение заданного текста с использованием модели `text-davinci-003`.

4.  **Перевод текста**:
    - Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.

5.  **Логирование завершений**:
    - Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.

## Установка

Для использования класса `HeliconeAI` убедитесь, что у вас установлены необходимые зависимости. Вы можете установить их с помощью pip:

```bash
pip install openai helicone
```

## Использование

### Инициализация

Инициализируйте класс `HeliconeAI`:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self, helicone_api_key: str = None, openai_api_key: str = None):
        self.helicone = Helicone(api_key=helicone_api_key)
        self.client = OpenAI(api_key=openai_api_key)
```

### Методы

#### Генерация стихотворения

Сгенерируйте стихотворение на основе заданного промпта:

```python
def generate_poem(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

#### Анализ тональности

Проанализируйте тональность заданного текста:

```python
def analyze_sentiment(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Краткое изложение текста

Создайте краткое изложение заданного текста:

```python
def summarize_text(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Перевод текста

Переведите заданный текст на указанный целевой язык:

```python
def translate_text(self, text: str, target_language: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

### Пример использования

Вот пример того, как использовать класс `HeliconeAI`:

```python
def main():
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

## Зависимости

- `helicone`
- `openai`

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле [LICENSE](LICENSE).

---

Для получения более подробной информации обратитесь к исходному коду и комментариям внутри класса `HeliconeAI`.
```