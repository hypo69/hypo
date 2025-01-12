import asyncio
import functools
import json
import os
from typing import List, Callable, Dict, Any

import typer
import uvicorn
from fastapi import FastAPI, APIRouter

from src.utils.jjson import j_dumps
from src.logger import logger

app = typer.Typer()
api_instance = None  # Глобальная переменная для хранения экземпляра FastApiServer


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
            try:
                await self.servers[port].stop()
                j_dumps(self.server_tasks, 'servers.json')
            except Exception as e:
                logger.error(f"Error stopping server on port {port}: {e}")
         else:
             print(f"Server on port {port} is not running or already stopped.")

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


@app.command()
def start(
        port: int = typer.Option(8000, help="Port to run the server on"),
        host: str = typer.Option("0.0.0.0", help="Host address for server"),
):
    """Starts the FastAPI server on the specified port."""
    global api_instance
    if api_instance is None:
      try:
        api_instance = FastApiServer(title="My API", host=host)
        api_instance.add_route("/hello", test_function)
        api_instance.add_route("/post", test_post, methods=["POST"])
        api_instance.register_router()
        asyncio.run(api_instance.start(port=port))
      except Exception as e:
        logger.error(f"Error starting server on port {port}: {e}")
    else:
      print("Server already initialized. Use other commands to manage it.")
@app.command()
def stop(
    port: int = typer.Option(8000, help="Port of the server to stop"),
):
    """Stops the FastAPI server on the specified port."""
    global api_instance
    if api_instance:
        try:
            asyncio.run(api_instance.stop(port=port))
        except Exception as e:
            logger.error(f"Error stopping server on port {port}: {e}")
    else:
         print("Server not initialized. Use start command first.")

@app.command()
def stop_all():
    """Stops all running FastAPI servers."""
    global api_instance
    if api_instance:
        try:
           asyncio.run(api_instance.stop_all())
        except Exception as e:
           logger.error(f"Error stopping all servers: {e}")
    else:
        print("Server not initialized. Use start command first.")

@app.command()
def status():
    """Show server status"""
    global api_instance
    if api_instance:
       print(f"Server initialized on host {api_instance.host}")
       for port, server in api_instance.servers.items():
           print(f"  - Port {port}: {'Running' if server.started else 'Stopped'}")
    else:
       print("Server not initialized. Use start command first.")

if __name__ == "__main__":
    app()