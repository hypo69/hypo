import functools
import json
import os, sys
from types import SimpleNamespace
from typing import List, Callable, Dict, Any
import threading

import uvicorn
from fastapi import FastAPI, APIRouter

import header
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint as print
from src.logger import logger
from pathlib import Path


api_instance = None  # Глобальная переменная для хранения экземпляра FastApiServer

try:
    config:SimpleNamespace = j_loads_ns (gs.path.src / 'fast_api' / 'fast_api.json')
    config.ports:list = config.ports if isinstance(config.ports, list) else [config.ports]

except Exception as ex:
    logger.critical(f"Config file nort found!")
    sys.exit()


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
        self.host = host or config.host
        self.server_tasks = {}  # Словарь для хранения задач (port: task)
        self.servers = {}  # Словарь для хранения серверов (port: server)

    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет маршрут к FastAPI приложению."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)

    def register_router(self):
        """Регистрирует роутер"""
        if self.router.routes:
            print(self.router)
            self.include_router(self.router)

    def _start_server(self, port: int):
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        server.run()

    def start(self, port: int):
        """Запускает FastAPI сервер на указанном порту."""
        if port in self.server_tasks and not self.server_tasks[port].done():
            print(f"Server already running on port {port}")
            return
        task = threading.Thread(target=self._start_server, args=(port,))
        self.server_tasks[port] = task
        task.start()


    def stop(self, port: int):
         if port in self.servers and self.servers[port].started:
            try:
                self.servers[port].stop()
                #j_dumps(self.server_tasks, 'servers.json') #Убрано сохранение
            except Exception as e:
                logger.error(f"Error stopping server on port {port}: {e}")
         else:
             print(f"Server on port {port} is not running or already stopped.")

    def stop_all(self):
        for port in list(self.servers.keys()):
             self.stop(port)

    def get_app(self):
        """Возвращает FastAPI приложение"""
        return self

    def get_servers_status(self):
        """Возвращает статус всех серверов"""
        if self.servers:
          return self.servers
        else:
           return {}


def test_function():
    return "It is working!!!"


def test_post(data: Dict[str, str]):
    return {"result": "post ok", "data": data}


def start(port: int, host: str):
    """Starts the FastAPI server on the specified port."""
    global api_instance
    if api_instance is None:
      try:
        api_instance = FastApiServer(title="My API", host=host)
        api_instance.add_route("/hello", test_function)
        api_instance.add_route("/post", test_post, methods=["POST"])
        # api_instance.register_router()
        api_instance.start(port=port)
      except Exception as e:
        logger.error(f"Error starting server on port {port}: {e}")
    else:
      if port not in api_instance.servers: #Если нет сервера с таким портом -  добавить
        try:
          api_instance.start(port=port)
        except Exception as e:
          logger.error(f"Error starting server on port {port}: {e}")
      else:
        print("Server already initialized. Use other commands to manage it.")


def stop(port: int):
    """Stops the FastAPI server on the specified port."""
    global api_instance
    if api_instance:
        try:
           api_instance.stop(port=port)
        except Exception as e:
            logger.error(f"Error stopping server on port {port}: {e}")
    else:
         print("Server not initialized. Use start command first.")


def stop_all():
    """Stops all running FastAPI servers."""
    global api_instance
    if api_instance:
        try:
           api_instance.stop_all()
        except Exception as e:
           logger.error(f"Error stopping all servers: {e}")
    else:
        print("Server not initialized. Use start command first.")


def status():
    """Show server status"""
    global api_instance
    if api_instance:
      
       servers = api_instance.get_servers_status()
       if servers:
         print(f"Server initialized on host {api_instance.host}")
         for port, server in servers.items():
            print(f"  - Port {port}: {'Running' if server.started else 'Stopped'}")
       else:
        print("No servers running")
    else:
       print("Server not initialized. Use start command first.")

def parse_port_range(range_str):
    """Разбирает строку с диапазоном портов."""
    if '-' in range_str:
        start, end = map(int, range_str.split('-'))
        return list(range(start, end + 1))
    else:
        return [int(range_str)]

def get_ports_from_config(config):
    """Извлекает список портов из конфигурации."""
    ports = []
    for range_str in config.ports:
        ports.extend(parse_port_range(range_str))
    return ports

def main():
    """Основная функция запуска."""
    host = config.host
    ports = get_ports_from_config(config)

    if not ports:
        print("No ports specified in config file.")
        return

    for port in ports:
        start(port=port, host=host)

    while True:
        command = input("Enter command (status, start <port>, stop <port>, stop_all, exit): ").strip().lower()

        if command == "status":
           status()
        elif command.startswith("start "):
            try:
                port_to_start = int(command.split(" ")[1])
                start(port=port_to_start, host=host)
            except (IndexError, ValueError):
                print("Invalid start command. Use 'start <port>'")
        elif command.startswith("stop "):
             try:
                port_to_stop = int(command.split(" ")[1])
                stop(port=port_to_stop)
             except (IndexError, ValueError):
                 print("Invalid stop command. Use 'stop <port>'")
        elif command == "stop_all":
            stop_all()
        elif command == "exit":
           break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()