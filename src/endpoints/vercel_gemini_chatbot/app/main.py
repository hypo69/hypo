from __future__ import annotations
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import google.generativeai as genai
from pathlib import Path

from header  import __root__

app = FastAPI()
# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Разрешенные домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешенные методы (GET, POST, etc.)
    allow_headers=["*"],  # Разрешенные заголовки
)
# Модель для запроса
class ChatRequest(BaseModel):
    message: str

# Инициализация Gemini AI
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    #raise ValueError("GEMINI_API_KEY не найден в .env файле")
    ...

genai.configure(api_key="AIzaSyCprZ9Tr-rB_xFau5zgWsKPM_6W-FmUntk")

model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Маршрут для корневого пути
@app.get("/", response_class=HTMLResponse)
async def root():
    # Чтение HTML-файла
    html_content = Path(__root__ / 'app'/ 'templates'/'index.html').read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)

# Маршрут для чата
@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        # Отправка сообщения в Gemini AI
        response = model.generate_content(request.message)

        # Возврат ответа
        return {"response": response.text}
    except Exception as e:
        # Обработка ошибок
        raise HTTPException(status_code=500, detail=str(e))


# Запуск сервера (для локальной разработки)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)