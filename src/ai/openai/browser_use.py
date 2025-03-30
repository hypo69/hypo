#@ https://habr.com/ru/articles/875798/

from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

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


if __name__ == "__main__":
    asyncio.run(main())