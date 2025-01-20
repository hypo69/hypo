## \file /src/fast_api/main_rpc.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.fast_api.main_rpc
    :platform: Windows, Unix
    :synopsis: XML-RPC client for managing the Fast API server

"""

import sys
import header  # <-- Обязательный импорт
import argparse
from xmlrpc.client import ServerProxy
from src.fast_api.fast_api_rpc import CommandHandler, logger



def display_menu():
    """Выводит меню с доступными командами."""
    print("\nAvailable commands:")
    print("  start <port>        - Start server on the specified port")
    print("  status              - Show all served ports status")
    print("  stop <port>         - Stop server on the specified port")
    print("  stop_all            - Stop all servers")
    print("  add_route <path>    - Add a new route to the server")
    print("  shutdown            - Stop all servers and exit")
    print("  help                - Show this help menu")
    print("  exit                - Exit the program")


def main():
    """Основная функция управления сервером."""
    command_handler = CommandHandler()
    rpc_client = ServerProxy("http://localhost:9000", allow_none=True)
    while True:
        display_menu()
        try:
            command_line = input("Enter command: ").strip().lower()
            if not command_line:
                continue

            parts = command_line.split()
            command = parts[0]

            if command == "start":
                if len(parts) != 2:
                    print("Usage: start <port>")
                    continue
                try:
                    port = int(parts[1])
                    host = input("Enter host address (default: 127.0.0.1): ").strip() or "127.0.0.1"
                    rpc_client.start_server(port, host)
                except ValueError:
                    print("Invalid port number.")
                except Exception as ex:
                  logger.error(f"An error occurred:", ex, exc_info=True)

            elif command == "status":
                rpc_client.status_servers()
            
            elif command == "stop":
               if len(parts) != 2:
                   print("Usage: stop <port>")
                   continue
               try:
                    port = int(parts[1])
                    rpc_client.stop_server(port)
               except ValueError:
                   print("Invalid port number.")
               except Exception as ex:
                  logger.error(f"An error occurred:", ex, exc_info=True)
            
            elif command == "stop_all":
               rpc_client.stop_all_servers()
            
            elif command == "add_route":
                if len(parts) != 2:
                    print("Usage: add_route <path>")
                    continue
                path = parts[1]
                methods = input("Enter HTTP methods (comma-separated, default: GET): ").strip().upper() or "GET"
                methods = [method.strip() for method in methods.split(",")]
                rpc_client.add_new_route(path, "lambda: {\"message\": \"Hello from the new route\"}", methods)
            
            elif command == "get_url":
                url = rpc_client.get_ngrok_url()
                print(f"Ngrok URL: {url}")

            elif command == "shutdown":
                rpc_client.shutdown()
                print("Shutting down the client")
                sys.exit(0)

            elif command == "help":
                display_menu()

            elif command == "exit":
                print("Exiting the client.")
                sys.exit(0)
            
            else:
                print("Unknown command. Type 'help' to see the list of available commands")

        except Exception as ex:
            logger.error(f"An error occurred:", ex, exc_info=True)


if __name__ == "__main__":
    main()