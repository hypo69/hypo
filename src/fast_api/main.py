import asyncio
import os
import argparse
import sys

import typer

import header  # Import header to set project root
from src.fast_api.fast_api import app as fast_api_app  # Import Typer app from fast_api.py
from src.fast_api.fast_api import api_instance

def parse_args():
        """Разбор аргументов командной строки."""
        parser = argparse.ArgumentParser(description="FastAPI Server Manager")
        parser.add_argument(
            "--command",
            type=str,
            default="start",
            help="Command to execute: start, stop, stop_all, status",
        )
        parser.add_argument(
            "--port",
            type=int,
            default=8000,
            help="Port for the server to run on",
        )
        parser.add_argument(
            "--host",
            type=str,
            default="0.0.0.0",
            help="Host address for the server",
        )
        return vars(parser.parse_args())

def main():
    """Основная функция для запуска."""
    args = parse_args()
    command = args["command"]
    port = args["port"]
    host = args["host"]
    
    if command == "start":
       asyncio.run(fast_api_app(args=["start", "--port", str(port), "--host", host]))
    elif command == "stop":
        asyncio.run(fast_api_app(args=["stop", "--port", str(port)]))
    elif command == "stop_all":
        asyncio.run(fast_api_app(args=["stop-all"]))
    elif command == "status":
        asyncio.run(fast_api_app(args=["status"]))
    else:
        print("Invalid command. Please use start, stop, stop_all, or status.")

if __name__ == "__main__":
    main()