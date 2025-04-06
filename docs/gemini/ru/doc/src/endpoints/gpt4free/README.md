# Документация для разработчика: gpt4free

## Обзор

Этот документ предоставляет подробное описание проекта `gpt4free`, включая инструкции по установке, использованию, внесению вклада и лицензированию. Проект представляет собой API-пакет для работы с различными AI-провайдерами, предоставляя возможности для балансировки нагрузки, управления потоком запросов, генерации текста и изображений.

## Подробнее

`gpt4free` разработан как Proof of Concept (PoC) для демонстрации создания API-пакета, который может взаимодействовать с несколькими AI-провайдерами. Основные цели проекта:

- Предоставление простого интерфейса для работы с разными AI-моделями.
- Обеспечение балансировки нагрузки и контроля потока запросов.
- Поддержка генерации текста и изображений.

Проект включает в себя различные способы установки и использования, такие как Docker, Windows (.exe) и Python. Также предоставляются примеры кода для генерации текста и изображений.

## Содержание

- [Что нового](#-whats-new)
- [Установка](#-getting-started)
    - [Использование Docker](#-using-docker)
    - [Windows Guide (.exe)](#-windows-guide-exe)
    - [Python Installation](#-python-installation)
- [Использование](#-usage)
    - [Генерация текста](#-text-generation)
    - [Генерация изображений](#-image-generation)
    - [Веб-интерфейс](#-web-interface)
    - [Локальный вывод](#docslocalmd)
    - [API](#-interference-api)
    - [Конфигурация](#docsconfigurationmd)
    - [Запуск на смартфоне](#-run-on-smartphone)
    - [Полная документация Python API](#-full-documentation-for-python-api)
- [Провайдеры и модели](#docsproviders-and-modelsmd)
- [Проекты на базе gpt4free](#-powered-by-gpt4free)
- [Вклад](#-contribute)
    - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
    - [Как AI может помочь мне писать код?](#guide-how-can-ai-help-me-with-writing-code)
- [Авторы](#-contributors)
- [Авторские права](#-copyright)
- [История звезд](#-star-history)
- [Лицензия](#-license)

## Установка

### Использование Docker

1.  **Установите Docker:** [Скачать и установить Docker](https://docs.docker.com/get-docker/).
2.  **Настройте директории:** Перед запуском контейнера убедитесь, что необходимые каталоги данных существуют или могут быть созданы. Например, можно создать и установить право собственности на эти каталоги, выполнив:

    ```bash
    mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
    sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
    ```
3.  **Запустите Docker Container:** Используйте следующие команды для извлечения последнего образа и запуска контейнера (только x64):

    ```bash
    docker pull hlohaus789/g4f
    docker run -p 8080:8080 -p 7900:7900 \
      --shm-size="2g" \
      -v ${PWD}/har_and_cookies:/app/har_and_cookies \
      -v ${PWD}/generated_images:/app/generated_images \
      hlohaus789/g4f:latest
    ```
4.  **Запуск Slim Docker Image:** И используйте следующие команды для запуска Slim Docker Image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости: (x64 и arm64)

    ```bash
    mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
    chown -R 1000:1000 ${PWD}/har_and_cookies ${PWD}/generated_images
    docker run \
      -p 1337:1337 \
      -v ${PWD}/har_and_cookies:/app/har_and_cookies \
      -v ${PWD}/generated_images:/app/generated_images \
      hlohaus789/g4f:latest-slim \
      rm -r -f /app/g4f/ \
      && pip install -U g4f[slim] \
      && python -m g4f --debug
    ```
5.  **Доступ к клиентскому интерфейсу:**

    *   **Чтобы использовать прилагаемый клиент, перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
    *   **Или установите базу API для своего клиента по адресу:** [http://localhost:8080/v1](http://localhost:8080/v1)
6.  **(Необязательно) Вход в провайдер:**

    *   При необходимости вы можете получить доступ к рабочему столу контейнера здесь: [http://localhost:7900/?autoconnect=1&resize=scale&password=secret](http://localhost:7900/?autoconnect=1&resize=scale&password=secret) для целей входа в провайдер.

### Windows Guide (.exe)

1.  **Скачайте приложение**: Посетите [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и скачайте последнюю версию приложения, названную `g4f.exe.zip`.
2.  **Размещение файлов**: После скачивания найдите `.zip` файл в папке загрузок. Распакуйте его в выбранный вами каталог в вашей системе, затем выполните файл `g4f.exe`, чтобы запустить приложение.
3.  **Открыть GUI**: Приложение запускает веб-сервер с GUI. Откройте свой любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4.  **Конфигурация брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы приложение работало правильно. Для этого зайдите в настройки брандмауэра Windows и разрешите работу приложения.

### Python Installation

#### Prerequisites:

1.  Install Python 3.10+ from [python.org](https://www.python.org/downloads/).
2.  Install Google Chrome for certain providers.

#### Install with PyPI:

```bash
pip install -U g4f[all]
```

> How do I install only parts or do disable parts? **Use partial requirements:** [/docs/requirements](docs/requirements.md)

#### Install from Source:

```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

> How do I load the project using git and installing the project requirements? **Read this tutorial and follow it step by step:** [/docs/git](docs/git.md)

## Использование

### Генерация текста

```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello"}],
    web_search=False
)
print(response.choices[0].message.content)
```

### Генерация изображений

```python
from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux",
    prompt="a white siamese cat",
    response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")
```

### Веб-интерфейс

**Запуск GUI с использованием Python:**

```python
from g4f.gui import run_gui

run_gui()
```

**Запуск через CLI (для запуска Flask Server):**

```bash
python -m g4f.cli gui --port 8080 --debug
```

**Или запустите FastAPI Server:**

```bash
python -m g4f --port 8080 --debug
```

## API

### Interference API

The **Interference API** enables seamless integration with OpenAI's services through G4F, allowing you to deploy efficient AI solutions.

- **Documentation**: [Interference API Docs](docs/interference-api.md)
- **Endpoint**: `http://localhost:1337/v1`
- **Swagger UI**: Explore the OpenAPI documentation via Swagger UI at `http://localhost:1337/docs`
- **Provider Selection**: [How to Specify a Provider?](docs/selecting_a_provider.md)

This API is designed for straightforward implementation and enhanced compatibility with other OpenAI integrations.

## Ссылки

#### **📘 Полная документация Python API**

*   **Client API from G4F:** [/docs/client](docs/client.md)
*   **AsyncClient API from G4F:** [/docs/async_client](docs/async_client.md)
*   **Requests API from G4F:** [/docs/requests](docs/requests.md)
*   **File API from G4F:** [/docs/file](docs/file.md)
*   **PydanticAI and LangChain Integration for G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
*   **Legacy API with python modules:** [/docs/legacy](docs/legacy.md)
*   **G4F - Media Documentation** [/docs/media](/docs/media.md) *(New)*

## Проекты на базе gpt4free

В таблице ниже перечислены проекты, использующие `gpt4free`:

| **Проекты**                                                                          | **Звезды**                                                                                                                     | **Форки**                                                                                                                      | **Проблемы**                                                                                                                    | **Пулл реквесты**                                                                                                             |
| :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| [gpt4free](https://github.com/xtekky/gpt4free)                                     | [![Stars](https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&labelColor=343b41)](https://github.com/xtekky/gpt4free/stargazers)    | [![Forks](https://img.shields.io/github/forks/xtekky/gpt4free?style=flat-square&labelColor=343b41)](https://github.com/xtekky/gpt4free/network/members)    | [![Issues](https://img.shields.io/github/issues/xtekky/gpt4free?style=flat-square&labelColor=343b41)](https://github.com/xtekky/gpt4free/issues)   | [![Pull Requests](https://img.shields.io/github/issues-pr/xtekky/gpt4free?style=flat-square&labelColor=343b41)](https://github.com/xtekky/gpt4free/pulls) |
| [gpt4free-ts](https://github.com/xiangsx/gpt4free-ts)                               | [![Stars](https://img.shields.io/github/stars/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41)](https://github.com/xiangsx/gpt4free-ts/stargazers) | [![Forks](https://img.shields.io/github/forks/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41)](https://github.com/xiangsx/gpt4free-ts/network/members) | [![Issues](https://img.shields.io/github/issues/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41)](https://github.com/xiangsx/gpt4free-ts/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41)](https://github.com/xiangsx/gpt4free-ts/pulls) |
| [Free AI API's & Potential Providers List](https://github.com/zukixa/cool-ai-stuff/) | [![Stars](https://img.shields.io/github/stars/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41)](https://github.com/zukixa/cool-ai-stuff/stargazers)      | [![Forks](https://img.shields.io/github/forks/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41)](https://github.com/zukixa/cool-ai-stuff/network/members)      | [![Issues](https://img.shields.io/github/issues/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41)](https://github.com/zukixa/cool-ai-stuff/issues)     | [![Pull Requests](https://img.shields.io/github/issues-pr/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41)](https://github.com/zukixa/cool-ai-stuff/pulls)   |
| [ChatGPT-Clone](https://github.com/xtekky/chatgpt-clone)                               | [![Stars](https://img.shields.io/github/stars/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41)](https://github.com/xtekky/chatgpt-clone/stargazers)      | [![Forks](https://img.shields.io/github/forks/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41)](https://github.com/xtekky/chatgpt-clone/network/members)      | [![Issues](https://img.shields.io/github/issues/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41)](https://github.com/xtekky/chatgpt-clone/issues)     | [![Pull Requests](https://img.shields.io/github/issues-pr/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41)](https://github.com/xtekky/chatgpt-clone/pulls)   |
| [Ai agent](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free)                   | [![Stars](https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/Josh-XT/AGiXT/stargazers) | [![Forks](https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/Josh-XT/AGiXT/network/members) | [![Issues](https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/Josh-XT/AGiXT/issues)  | [![Pull Requests](https://img.shields.io/github/issues-pr/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/Josh-XT/AGiXT/pulls) |
| [ChatGpt Discord Bot](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free)       | [![Stars](https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/stargazers) | [![Forks](https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/network/members) | [![Issues](https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/mishalhossin/Coding-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/mishalhossin/Coding-Chatbot-Gpt4Free/pulls) |
| [chatGPT-discord-bot](https://github.com/Zero6992/chatGPT-discord-bot)             | [![Stars](https://img.shields.io/github/stars/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41)](https://github.com/Zero6992/chatGPT-discord-bot/stargazers) | [![Forks](https://img.shields.io/github/forks/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41)](https://github.com/Zero6992/chatGPT-discord-bot/network/members) | [![Issues](https://img.shields.io/github/issues/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41)](https://github.com/Zero6992/chatGPT-discord-bot/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41)](https://github.com/Zero6992/chatGPT-discord-bot/pulls) |
| [Nyx-Bot (Discord)](https://github.com/SamirXR/Nyx-Bot)                               | [![Stars](https://img.shields.io/github/stars/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41)](https://github.com/SamirXR/Nyx-Bot/stargazers)             | [![Forks](https://img.shields.io/github/forks/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41)](https://github.com/SamirXR/Nyx-Bot/network/members)             | [![Issues](https://img.shields.io/github/issues/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41)](https://github.com/SamirXR/Nyx-Bot/issues)            | [![Pull Requests](https://img.shields.io/github/issues-pr/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41)](https://github.com/SamirXR/Nyx-Bot/pulls)          |
| [LangChain gpt4free](https://github.com/MIDORIBIN/langchain-gpt4free)                 | [![Stars](https://img.shields.io/github/stars/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41)](https://github.com/MIDORIBIN/langchain-gpt4free/stargazers) | [![Forks](https://img.shields.io/github/forks/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41)](https://github.com/MIDORIBIN/langchain-gpt4free/network/members) | [![Issues](https://img.shields.io/github/issues/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41)](https://github.com/MIDORIBIN/langchain-gpt4free/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41)](https://github.com/MIDORIBIN/langchain-gpt4free/pulls) |
| [ChatGpt Telegram Bot](https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free)         | [![Stars](https://img.shields.io/github/stars/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/stargazers) | [![Forks](https://img.shields.io/github/forks/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/network/members) | [![Issues](https://img.shields.io/github/issues/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41)](https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/pulls) |
| [ChatGpt Line Bot](https://github.com/Lin-jun-xiang/chatgpt-line-bot)               | [![Stars](https://img.shields.io/github/stars/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/chatgpt-line-bot/stargazers)   | [![Forks](https://img.shields.io/github/forks/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/chatgpt-line-bot/network/members)   | [![Issues](https://img.shields.io/github/issues/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues)  | [![Pull Requests](https://img.shields.io/github/issues-pr/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/chatgpt-line-bot/pulls) |
| [Action Translate Readme](https://github.com/Lin-jun-xiang/action-translate-readme)   | [![Stars](https://img.shields.io/github/stars/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/action-translate-readme/stargazers)  | [![Forks](https://img.shields.io/github/forks/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/action-translate-readme/network/members)  | [![Issues](https://img.shields.io/github/issues/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/action-translate-readme/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/action-translate-readme/pulls)  |
| [Langchain Document GPT](https://github.com/Lin-jun-xiang/docGPT-streamlit)          | [![Stars](https://img.shields.io/github/stars/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/docGPT-streamlit/stargazers) | [![Forks](https://img.shields.io/github/forks/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/docGPT-streamlit/network/members) | [![Issues](https://img.shields.io/github/issues/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/docGPT-streamlit/issues) | [![Pull Requests](https://img.shields.io/github/issues-pr/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41)](https://github.com/Lin-jun-xiang/docGPT-streamlit/pulls) |
| [python-tgpt](https://github.com/Simatwa/python-tgpt)                               | [![Stars](https://img.shields.io/github/stars/Simatwa/python-tgpt?style=flat-square&labelColor=343b41)](https://github.com/Simatwa/python-tgpt/stargazers)          | [![Forks](https://img.shields.io/github/forks/Simatwa/python-tgpt?style=flat-square&labelColor=343b41)](https://github.com/Simatwa/python-tgpt/network/members)          | [![Issues](https://img.shields.io/github/issues/Simatwa/python-tgpt?style=flat-square&labelColor=343b41)](https://github.com/Simatwa/python-tgpt/issues)         | [![Pull Requests](https://img.shields.io/github/issues-pr/Simatwa/python-tgpt?style=flat-square&labelColor=343b41)](https://github.com/Simatwa/python-tgpt/pulls)       |
| [GPT4js](https://github.com/zachey01/gpt4free.js)                                  | [![Stars](https://img.shields.io/github/stars/zachey01/gpt4free.js?style=flat-square&labelColor=343b41)](https://github.com/zachey01/gpt4free.js/stargazers)    | [![Forks](https://img.shields.io/github/forks/zachey01/gpt4free.js?style=flat-square&labelColor=343b41)](https://github.com/zachey01/gpt4free.js/network/members)    | [![Issues](https://img.shields.io/github/issues/zachey01/gpt4free.js?style=flat-square&labelColor=343b41)](https://github.com/zachey01/gpt4free.js/issues)   | [![Pull Requests](https://img.shields.io/github/issues-pr/zachey01/gpt4free.js?style=flat-square&labelColor=343b41)](https://github.com/zachey01/gpt4free.js/pulls) |
| [VividNode (pyqt-openai)](https://github.com/yjg30737/pyqt-openai)                   | [![Stars](https://img.shields.io/github/stars/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41)](https://github.com/yjg30737/pyqt-openai/stargazers)    | [![Forks](https://img.shields.io/github/forks/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41)](https://github.com/yjg30737/pyqt-openai/network/members)    | [![Issues](https://img.shields.io/github/issues/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41)](https://github.com/yjg30737/pyqt-openai/issues)   | [![Pull Requests](https://img.shields.io/github/issues-pr/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41)](https://github.com/yjg30737/pyqt-openai/pulls) |

## Вклад

Приветствуются вклады от сообщества. Будь то добавление новых провайдеров или функций, или просто исправление опечаток и внесение небольших улучшений, ваш вклад ценен. Создание запроса на вытягивание - это все, что нужно - наш сопроцессор будет обрабатывать процесс проверки кода. После того, как все изменения были устранены, мы объединим запрос на вытягивание в основную ветку и выпустим обновления позже.

###### Руководство: Как создать нового провайдера?

*   **Читать:** [Create Provider Guide](docs/guides/create_provider.md)

###### Руководство: Как AI может помочь мне писать код?

*   **Читать:** [AI Assistance Guide](docs/guides/help_me.md)

## Авторы

Список всех участников доступен [здесь](https://github.com/xtekky/gpt4free/graphs/contributors)

## Авторские права

Эта программа лицензируется в соответствии с [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```
xtekky/gpt4free: Copyright (C) 2023 xtekky

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## История звезд

## Лицензия

Этот проект лицензирован в соответствии с [GNU GPL v3.0](https://github.com/xtekky/gpt4free/blob/main/LICENSE).