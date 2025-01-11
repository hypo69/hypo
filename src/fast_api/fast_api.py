from fastapi import FastAPI, APIRouter
import uvicorn
from typing import List, Callable, Dict, Any
import functools
import asyncio
import header
from src.utils.jjson import j_dumps


class Singleton(type):
    """Metaclass for implementing the singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FastApiServer(FastAPI, metaclass=Singleton):
    """FastAPI server with singleton implementation."""

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self.server_tasks = {}  # Словарь для хранения задач (port: task)
        self.servers = {}  # Словарь для хранения серверов (port: server)


    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет маршрут к FastAPI приложению."""
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)


    def register_router(self):
        """Регистрирует роутер"""
        self.include_router(self.router)


    async def _start_server(self, port: int):
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        self.servers[port] = server
        await server.serve()

    async def start(self, port: int):
        """Запускает FastAPI сервер на указанном порту."""
        if port in self.server_tasks and not self.server_tasks[port].done():
            print(f"Server already running on port {port}")
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task
        j_dumps(self.server_tasks, 'servers.json')


    async def stop(self, port: int):
        if port in self.servers and self.servers[port].started:
            await self.servers[port].stop()
            j_dumps(self.server_tasks, 'servers.json')

    async def stop_all(self):
        for port in list(self.servers.keys()):
             await self.stop(port)

    def get_app(self):
      """Возвращает FastAPI приложение"""
      return self



async def test_function():
   return "It is working!!!"

async def test_post(data: Dict[str, str]):
   return {"result": "post ok", "data": data}


async def main():
    api = FastApiServer(title="My API", host="0.0.0.0")
    api.add_route("/hello", test_function)
    api.add_route("/post", test_post, methods=["POST"])
    api.register_router()

    # Запускаем на порту 8080
    print('start api on port 8080')
    await api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
    print('start api on port 8081')
    await api.start(port=8081)

    await asyncio.sleep(2)
    # stop port 8080
    print('stop api on port 8080')
    await api.stop(port=8080)

    await asyncio.sleep(2)
    print('stop all servers')
    await api.stop_all()


if __name__ == "__main__":
    asyncio.run(main())