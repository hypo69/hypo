import google.generativeai as genai

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Инициализация модели GoogleGenerativeAI.

        Аргументы:
            api_key (str): Ключ API для доступа к генеративной модели.
            model_name (str, optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        Аргументы:
            q (str): Вопрос, который будет отправлен модели.

        Возвращает:
            str: Ответ от модели.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY:str = input("API ключ от `gemini`")
model = GoogleGenerativeAI(api_key = API_KEY)

q = input("Вопрос: ")
response = model.ask(q)
print(response)