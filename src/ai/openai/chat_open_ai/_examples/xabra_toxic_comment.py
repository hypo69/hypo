# https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221-sltpLDS5IBaM7nitu6wqwh3QDGI4-s2%22%5D,%22action%22:%22open%22,%22userId%22:%22110086287199111465514%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing

from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()
import header
from src import gs
from src.logger.logger import logger

##############################################################

ENDPOINT = 'openai'
USE_ENV:bool = False # <- Определает откуда брать ключи. Если False - то из базы данных с паролями, иначе из .env
MODE:str = 'PRODUCTION' # <- Определяет режим прода. 
MODE:str = 'DEV' # <- Определяет режим разработчика. 
#############################################################

async def habra_toxic_commenter(author_username: str, model_name: str = "gpt-4o-mini", api_key:str = None):
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
        llm = ChatOpenAI(model = model_name,
                         api_key = api_key if api_key else gs.credentials.openai.hypotez.api_key,
                         )
        task = f"""Открой Хабр (habr.com), найди какую-нибудь статью от юзера {author_username},
        открой её полную версию, и предложи вариант токсичного комментария на русском,
        связанного с этой статьей, после опубликуй этот комментарий к статье."""
        agent = Agent(
            task=task,
            llm=llm,
            
        )
        logger.info(f"Агент начал работу по поиску статьи автора {author_username}")
        result = await agent.run()
        logger.info(f"Агент завершил работу.")
        return result
    except Exception as ex:
        logger.error(f"Произошла ошибка: ",ex)
        return None


async def main():
    """
    Пример использования функции habra_toxic_commenter.
    """
    api_key:str = gs.credentials.openai.hypotez.api_key
    model_name:str  = 'gpt-4o-mini'
    author = "ElKornacio"  # Замените на имя пользователя, статьи которого хотите найти
    result = await habra_toxic_commenter(author_username = author, model_name = model_name, api_key = api_key)

    if result:
        print("Результат работы агента:")
        print(result)
    else:
        print("Не удалось получить результат.")


if __name__ == "__main__":
    asyncio.run(main())