## \file /src/fast_api/fast_api_rpc.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
FastAPI сервер с XML-RPC интерфейсом для удалённого управления
====================================================

.. module:: src.fast_api.fast_api_rpc
    :platform: Windows, Unix
    :synopsis: FastAPI сервер с интерфейсом XML-RPC для удалённого управления

"""
import asyncio
import functools
import json
import os
import sys
import threading
from types import SimpleNamespace
from typing import List, Callable, Dict
from pathlib import Path
from contextlib import asynccontextmanager
from xmlrpc.server import SimpleXMLRPCServer
from dotenv import load_dotenv

import uvicorn
from fastapi import FastAPI, APIRouter

import header  # <-- Обязательный импорт
from header import __root__
from src import gs
from src.utils.jjson import j_loads, j_loads_ns
#from src.endpoints.bots.telegram.webhooks import telegram_webhook
from src.utils.printer import pprint as print
from src.logger import logger

import re

load_dotenv()


try:
    config: SimpleNamespace = j_loads_ns(__root__ / 'src' / 'fast_api' / 'fast_api.json')
    config.ports: list = config.ports if isinstance(config.ports, list) else [config.ports]
except Exception as ex:
    logger.critical(f"Config file not found!")
    sys.exit()

_api_server_instance = None


class FastApiServer:
    """FastAPI сервер с реализацией Singleton."""

    _instance = None
    app: FastAPI = FastAPI()
    host: str = config.host
    port: int = 8000
    router: APIRouter = APIRouter()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host: str = "127.0.0.1", title: str = "FastAPI RPC Server", **kwargs):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
        self.add_route("/hello", test_function)
        self.add_route("/post", test_post, methods=["POST"])
        self.add_route("/telegram_webhook", telegram_webhook, methods=["POST"])

        self.app = FastAPI()
        self.host = host or config.host
        self.server_tasks = {}
        self.servers = {}
        self.app.include_router(self.router)

    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет маршрут к FastAPI приложению."""
        self.router.add_api_route(path, func, methods=methods, **kwargs)

    def add_new_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет новый маршрут к уже работающему приложению."""
        self.add_route(path, func, methods, **kwargs)

    async def _start_server(self, port: int):
        """Запускает uvicorn сервер асинхронно."""
        config = uvicorn.Config(self.app, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        try:
            await server.serve()
            logger.success(f"Server started on: {self.host}:{port}")
        except Exception as e:
            logger.error(f"Error running server on port {port}: {e}")
        finally:
            self.servers.pop(port, None)

    def start(self, port: int, as_thread:bool = True):
        """Запускает FastAPI сервер на указанном порту."""
        if port in self.servers:
            print(f"Server already running on port {port}")
            return

        task = threading.Thread(target=asyncio.run, args=(self._start_server(port),), daemon=True)
        self.server_tasks[port] = task
        self.servers[port] = task
        task.start()

    def stop(self, port: int):
        """Останавливает FastAPI сервер на указанном порту."""
        if port in self.servers:
            try:
                self.servers[port]._thread.join(1)
                self.servers.pop(port)
                print(f"Server on port {port} stopped.")
            except Exception as e:
                logger.error(f"Error stopping server on port {port}: {e}")
        else:
            print(f"Server on port {port} is not running or already stopped.")

    def stop_all(self):
        """Останавливает все запущенные сервера."""
        for port in list(self.servers):
            self.stop(port)

    def get_servers_status(self):
        """Возвращает статус всех серверов."""
        return {port: "Running" if task.is_alive() else "Stopped" for port, task in self.servers.items()}

    def get_app(self):
        """Возвращает FastAPI приложение."""
        return self.app


def telegram_webhook():
    """"""
    return 'Hello, World!'


def test_function():
    return "It is working!!!"


def test_post(data: Dict[str, str]):
    return {"result": "post ok", "data": data}


def start_server(port: int, host: str):
    """Запускает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance is None:
        _api_server_instance = FastApiServer(host=host)
    _api_server_instance.start(port=port)


def stop_server(port: int):
    """Останавливает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance:
        _api_server_instance.stop(port=port)


def stop_all_servers():
    """Останавливает все запущенные FastAPI серверы."""
    global _api_server_instance
    if _api_server_instance:
        _api_server_instance.stop_all()


def status_servers():
    """Показывает статус серверов."""
    global _api_server_instance
    if _api_server_instance:
        servers = _api_server_instance.get_servers_status()
        if servers:
            print(f"Server initialized on host {_api_server_instance.host}")
            for port, status in servers.items():
                print(f"  - Port {port}: {status}")
        else:
            print("No servers running")
    else:
        print("Server not initialized.")


def add_new_route(path: str, func: Callable, methods: List[str] = ["GET"]):
    """Добавляет новый роут к серверу."""
    global _api_server_instance
    if _api_server_instance:
        _api_server_instance.add_new_route(path=path, func=func, methods=methods)
        print(f"Route added: {path}, {methods=}")
    else:
        print("Server not initialized. Start server first")


def parse_port_range(range_str):
    """Разбирает строку с диапазоном портов."""
    if not re.match(r'^[\d-]+$', range_str):
        print(f"Invalid port range: {range_str}")
        return []
    if '-' in range_str:
        try:
            start, end = map(int, range_str.split('-'))
            if start > end:
                raise ValueError("Invalid port range")
            return list(range(start, end + 1))
        except ValueError:
            print(f"Invalid port range: {range_str}")
            return []
    else:
        try:
            return [int(range_str)]
        except ValueError:
            print(f"Invalid port: {range_str}")
            return []


class CommandHandler:
    """Обработчик команд для FastAPI сервера через XML-RPC."""

    def __init__(self, rpc_port=9000):
        self.rpc_port = rpc_port
        self.rpc_server = SimpleXMLRPCServer(("localhost", self.rpc_port), allow_none=True)
        self.rpc_server.register_instance(self)
        threading.Thread(target=self.rpc_server.serve_forever, daemon=True).start()
        print(f"RPC server started on port: {self.rpc_port}")

    def start_server(self, port: int, host: str):
        start_server(port=port, host=host)

    def stop_server(self, port: int):
        stop_server(port=port)

    def stop_all_servers(self):
        stop_all_servers()

    def status_servers(self):
        status_servers()

    def add_new_route(self, path: str, func: str, methods: List[str] = ["GET"]):
        # Передаем ссылку на функцию вместо eval.
        func_ref = globals().get(func)
        if func_ref:
            add_new_route(path=path, func=func_ref, methods=methods)
        else:
            print(f"Function {func} not found.")

    def shutdown(self):
        self.stop_all_servers()
        self.rpc_server.shutdown()
        print("RPC server shutdown")
        sys.exit(0)
