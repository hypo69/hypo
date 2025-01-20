## \file /src/fast_api/external_client.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.fast_api.external_client
    :platform: Windows, Unix
    :synopsis: Example XML-RPC client for managing the Fast API server from external code.

"""

import sys
from xmlrpc.client import ServerProxy
import time

def main():
    """Основная функция для управления сервером через RPC из внешнего кода."""
    rpc_client = ServerProxy("http://localhost:9000", allow_none=True)
    
    try:
        # Пример: Запуск сервера на порту 8001
        print("Starting server on port 8001...")
        rpc_client.start_server(8001, "127.0.0.1")
        time.sleep(1)
        
        # Пример: Добавление нового маршрута /test_route
        print("Adding new route /test_route...")
        rpc_client.add_new_route("/test_route", 'lambda: {"message": "Hello from test_route"}', ["GET"])
        time.sleep(1)

        # Пример: Получение статуса серверов
        print("Getting server status...")
        rpc_client.status_servers()
        time.sleep(1)

       # Пример: Остановка сервера на порту 8001
        print("Stopping server on port 8001...")
        rpc_client.stop_server(8001)
        time.sleep(1)
        
        # Пример: Получение статуса серверов
        print("Getting server status...")
        rpc_client.status_servers()
        time.sleep(1)

    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        print("Shutting down RPC server")
        rpc_client.shutdown()


if __name__ == "__main__":
    main()