# HeliconeAI: Интеграция с Helicone.ai и OpenAI

## Обзор

Класс `HeliconeAI` предназначен для взаимодействия с сервисом Helicone.ai и моделями OpenAI. Он предоставляет методы для генерации стихотворений, анализа настроения, резюмирования текста и перевода текста. Также класс включает в себя логирование завершений с использованием Helicone.ai.

## Оглавление

* [Обзор](#обзор)
* [Ключевые особенности](#ключевые-особенности)
* [Установка](#установка)
* [Использование](#использование)
* [Методы](#методы)
    * [Генерация стихотворения](#генерация-стихотворения)
    * [Анализ настроения](#анализ-настроения)
    * [Резюмирование текста](#резюмирование-текста)
    * [Перевод текста](#перевод-текста)
* [Пример использования](#пример-использования)
* [Зависимости](#зависимости)
* [Лицензия](#лицензия)


## Ключевые особенности

1. **Генерация стихотворения**: Генерирует стихотворение на основе заданного запроса с использованием модели `gpt-3.5-turbo`.
2. **Анализ настроения**: Анализирует настроение заданного текста с использованием модели `text-davinci-003`.
3. **Резюмирование текста**: Резюмирует заданный текст с использованием модели `text-davinci-003`.
4. **Перевод текста**: Переводит заданный текст на указанный целевой язык с использованием модели `text-davinci-003`.
5. **Логирование завершений**: Логирует все завершения с использованием Helicone.ai для мониторинга и анализа.


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
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```


### Методы

#### Генерация стихотворения

Генерирует стихотворение на основе заданного запроса:

```python
def generate_poem(self, prompt: str) -> str:
    """
    Args:
        prompt (str): Запрос для генерации стихотворения.

    Returns:
        str: Сгенерированное стихотворение.

    Raises:
        Exception: Любые ошибки, возникающие при взаимодействии с OpenAI или Helicone.ai.
    """
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

#### Анализ настроения

Анализирует настроение заданного текста:

```python
def analyze_sentiment(self, text: str) -> str:
    """
    Args:
        text (str): Текст для анализа настроения.

    Returns:
        str: Анализ настроения (например, "положительный", "отрицательный").

    Raises:
        Exception: Любые ошибки, возникающие при взаимодействии с OpenAI или Helicone.ai.
    """
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

(Аналогично реализованы методы `summarize_text` и `translate_text`)


#### Резюмирование текста
#### Перевод текста


### Пример использования

Вот пример того, как использовать класс `HeliconeAI`:

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Сгенерированное стихотворение:\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Анализ настроения:\n", sentiment)

    # ... (примеры использования других методов)

if __name__ == "__main__":
    main()
```


## Зависимости

- `helicone`
- `openai`


## Лицензия

Этот проект лицензирован по лицензии MIT.  См. файл [LICENSE](LICENSE) для подробностей.