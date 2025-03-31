# Модуль для генерации токсичных комментариев на Habr с использованием OpenAI

## Обзор

Этот модуль содержит функции для поиска статьи на Хабре по указанному автору, открытия её и генерации токсичного комментария с использованием языковой модели OpenAI.

## Подробней

Модуль предназначен для автоматической генерации токсичных комментариев на платформе Habr. Он использует библиотеку `langchain_openai` для взаимодействия с OpenAI API и модуль `browser_use` для автоматизации действий в браузере.

## Функции

### `habra_toxic_commenter`

```python
async def habra_toxic_commenter(author_username: str, model_name: str = "gpt-4o"):
    """
    Ищет статью на Хабре по указанному автору, открывает её и генерирует токсичный комментарий.

    Args:
        author_username: Имя пользователя на Хабре.
        model_name: Название языковой модели OpenAI для использования.  По умолчанию gpt-4o.

    Returns:
        Строку с результатом работы агента, содержащую название статьи и сгенерированный комментарий.
        Возвращает None, если произошла ошибка.
    """
    try:
        llm = ChatOpenAI(model=model_name)
        task = f"""Открой Хабр (habr.com), найди какую-нибудь статью от юзера {author_username},
        открой её полную версию, и предложи вариант токсичного комментария на русском,
        связанного с этой статьей, после опубликуй этот комментарий к статье."""
        agent = Agent(
            task=task,
            llm=llm,
        )
        logging.info(f"Агент начал работу по поиску статьи автора {author_username}")
        result = await agent.run()
        logging.info(f"Агент завершил работу.")
        return result
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return None
```

**Назначение**: Ищет статью на Хабре по указанному автору, открывает её и генерирует токсичный комментарий.

**Как работает функция**:
1. Инициализируется языковая модель OpenAI (`ChatOpenAI`) с указанным именем (`model_name`). По умолчанию используется модель "gpt-4o".
2. Формируется задача (`task`) для агента, которая включает в себя поиск статьи на Хабре по указанному имени пользователя (`author_username`), открытие полной версии статьи и предложение варианта токсичного комментария на русском языке, связанного с этой статьей, а также публикацию этого комментария к статье.
3. Создается экземпляр класса `Agent` с переданной задачей и языковой моделью.
4. В лог записывается информация о начале работы агента с указанием имени автора.
5. Запускается агент для выполнения задачи с помощью `await agent.run()`.
6. После завершения работы агента в лог записывается соответствующая информация.
7. Возвращается результат работы агента.
8. В случае возникновения ошибки, информация об ошибке записывается в лог и возвращается `None`.

**Параметры**:
- `author_username` (str): Имя пользователя на Хабре.
- `model_name` (str, optional): Название языковой модели OpenAI для использования. По умолчанию "gpt-4o".

**Возвращает**:
- `str | None`: Строка с результатом работы агента, содержащая название статьи и сгенерированный комментарий. Возвращает `None`, если произошла ошибка.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки в процессе выполнения функции.

### `main`

```python
async def main():
    """
    Пример использования функции habra_toxic_commenter.
    """
    author = "ElKornacio"  # Замените на имя пользователя, статьи которого хотите найти
    result = await habra_toxic_commenter(author_username=author)

    if result:
        print("Результат работы агента:")
        print(result)
    else:
        print("Не удалось получить результат.")
```

**Назначение**: Пример использования функции `habra_toxic_commenter`.

**Как работает функция**:
1. Определяется имя пользователя (`author`), статьи которого необходимо найти. В данном примере это "ElKornacio".
2. Вызывается функция `habra_toxic_commenter` с указанным именем пользователя.
3. Если результат работы функции не равен `None`, то выводится сообщение "Результат работы агента:" и сам результат.
4. В противном случае выводится сообщение "Не удалось получить результат."

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Примеры**:
```python
async def main():
    """
    Пример использования функции habra_toxic_commenter.
    """
    author = "ElKornacio"  # Замените на имя пользователя, статьи которого хотите найти
    result = await habra_toxic_commenter(author_username=author)

    if result:
        print("Результат работы агента:")
        print(result)
    else:
        print("Не удалось получить результат.")
```
```python
if __name__ == "__main__":
    asyncio.run(main())
```
```python
author = "ElKornacio"  # Замените на имя пользователя, статьи которого хотите найти
result = await habra_toxic_commenter(author_username=author)
```
```python
result = await habra_toxic_commenter(author_username=author)
```
```python
llm = ChatOpenAI(model=model_name)
```
```python
task = f"""Открой Хабр (habr.com), найди какую-нибудь статью от юзера {author_username},
        открой её полную версию, и предложи вариант токсичного комментария на русском,
        связанного с этой статьей, после опубликуй этот комментарий к статье."""
```
```python
asyncio.run(main())
```
```python
agent = Agent(
            task=task,
            llm=llm,
        )
```

```python
logging.info(f"Агент начал работу по поиску статьи автора {author_username}")
```
```python
logging.info(f"Агент завершил работу.")
```
```python
logging.error(f"Произошла ошибка: {e}")
```
```python
return result
```
```python
except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return None
```
```python
if result:
        print("Результат работы агента:")
        print(result)
    else:
        print("Не удалось получить результат.")
```
```python
load_dotenv()
```
```python
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import logging
```
```python
return None