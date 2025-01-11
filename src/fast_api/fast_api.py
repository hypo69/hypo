from fastapi import FastAPI, APIRouter
import uvicorn
from typing import List, Callable, Dict, Any
import functools
import threading
import asyncio


class FastApiServer(FastAPI):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
            cls._instance.server_tasks = {}  # Словарь для хранения задач (port: task)
            cls._instance.servers = {}  # Словарь для хранения серверов (port: server)
        return cls._instance

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        if self._initialized:
            return
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self._initialized = True


    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет маршрут к FastAPI приложению."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)


    def register_router(self):
        """Регистрирует роутер"""
        self.include_router(self.router)


    async def _start_server(self, port: int):
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        self.servers[port] = server
        await server.serve()

    def start(self, port: int):
        """Запускает FastAPI сервер на указанном порту."""
        if port in self.server_tasks and not self.server_tasks[port].done():
            print(f"Server already running on port {port}")
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task


    async def stop(self, port: int):
        if port in self.servers and self.servers[port].started:
            await self.servers[port].stop()

    async def stop_all(self):
        for port in list(self.servers.keys()):
             await self.stop(port)

    def get_app(self):
      """Возвращает FastAPI приложение"""
      return self



def test_function():
   return "It is working!!!"

def test_post(data: Dict[str, str]):
   return {"result": "post ok", "data": data}


async def main():
    api = FastApi(title="My API", host="0.0.0.0")
    api.add_route("/hello", test_function)
    api.add_route("/post", test_post, methods=["POST"])
    api.register_router()

    # Запускаем на порту 8080
    print('start api on port 8080')
    api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
    print('start api on port 8081')
    api.start(port=8081)

    await asyncio.sleep(2)
    # stop port 8080
    print('stop api on port 8080')
    await api.stop(port=8080)

    await asyncio.sleep(2)
    print('stop all servers')
    await api.stop_all()


if __name__ == "__main__":
    asyncio.run(main())