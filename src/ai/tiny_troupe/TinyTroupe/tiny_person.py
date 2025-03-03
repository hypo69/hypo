import os
from dotenv import load_dotenv
# Если ключ хранится в файле .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from tinytroupe.agent import TinyPerson

# Create a TinyPerson instance
john = TinyPerson(name="John")

# Define some characteristics
john.define("age", 35)
john.define("occupation", "Software Engineer")
john.define("nationality", "American")
john.define("skills", [{"skill": "Coding in python"}])

# Interact with the agent
john.listen("Hello, John! How are you today?")
john.act()
john.pp_current_interactions()