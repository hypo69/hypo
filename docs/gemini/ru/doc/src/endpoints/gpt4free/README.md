# Документация для разработчика: gpt4free

## Обзор

Этот документ содержит информацию о проекте `gpt4free`, который представляет собой proof-of-concept API для мультипровайдерных AI-запросов. Он демонстрирует такие функции, как балансировка нагрузки, управление потоком запросов, интеграция с несколькими AI-провайдерами и поддержку генерации текста и изображений.

## Подробнее

Проект `gpt4free` предоставляет API-пакет с мультипровайдерными запросами, что позволяет разработчикам легко интегрировать различные AI-сервисы в свои приложения. Он также включает функции, такие как таймауты, балансировка нагрузки и управление потоком, что делает его надежным и эффективным решением для AI-запросов.

## Содержание

- [🆕 Что нового](#-whats-new)
- [📚 Оглавление](#-table-of-contents)
- [⚡ Начало работы](#-getting-started)
    - [🛠 Установка](#-installation)
        - [🐳 Использование Docker](#-using-docker)
        - [🪟 Руководство для Windows (.exe)](#-windows-guide-exe)
        - [🐍 Установка Python](#-python-installation)
- [💡 Использование](#-usage)
    - [📝 Генерация текста](#-text-generation)
    - [🎨 Генерация изображений](#-image-generation)
    - [🌐 Веб-интерфейс](#-web-interface)
    - [🖥️ Локальный вывод](docs/local.md)
    - [🤖 API вывода](#-interference-api)
    - [🛠️ Конфигурация](docs/configuration.md)
    - [📱 Запуск на смартфоне](#-run-on-smartphone)
    - [📘 Полная документация для Python API](#-full-documentation-for-python-api)
- [🚀 Провайдеры и модели](docs/providers-and-models.md)
- [🔗 Powered by gpt4free](#-powered-by-gpt4free)
- [🤝 Вклад](#-contribute)
    - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
    - [Как AI может помочь мне с написанием кода?](#guide-how-can-ai-help-me-with-writing-code)
- [🙌 Участники](#-contributors)
- [©️ Авторское право](#-copyright)
- [⭐ История звезд](#-star-history)
- [📄 Лицензия](#-license)

## ⚡️ Начало работы

### 🛠 Установка

#### 🐳 Использование Docker

1.  **Установите Docker:** [Скачайте и установите Docker](https://docs.docker.com/get-docker/).
2.  **Настройте каталоги:** Перед запуском контейнера убедитесь, что необходимые каталоги данных существуют или могут быть созданы. Например, вы можете создать и установить права собственности на эти каталоги, выполнив:

```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
```

3.  **Запустите Docker-контейнер:** Используйте следующие команды для получения последнего образа и запуска контейнера (только x64):

```bash
docker pull hlohaus789/g4f
docker run -p 8080:8080 -p 7900:7900 \
  --shm-size="2g" \
  -v ${PWD}/har_and_cookies:/app/har_and_cookies \
  -v ${PWD}/generated_images:/app/generated_images \
  hlohaus789/g4f:latest
```

4.  **Запуск Slim Docker Image:** Используйте следующие команды для запуска Slim Docker Image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости: (x64 и arm64)

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

    *   **Для использования включенного клиента перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
    *   **Или установите базовый API для вашего клиента на:** [http://localhost:8080/v1](http://localhost:8080/v1)

6.  **(Необязательно) Вход в систему провайдера:**

    *   При необходимости вы можете получить доступ к рабочему столу контейнера здесь: [http://localhost:7900/?autoconnect=1&resize=scale&password=secret](http://localhost:7900/?autoconnect=1&resize=scale&password=secret) для целей входа в систему провайдера.

#### 🪟 Руководство для Windows (.exe)

Чтобы обеспечить бесперебойную работу нашего приложения, следуйте приведенным ниже инструкциям. Эти шаги предназначены для того, чтобы помочь вам в процессе установки в операционных системах Windows.

**Этапы установки:**

1.  **Загрузите приложение**: Посетите нашу [страницу выпусков](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и загрузите последнюю версию приложения, которая называется `g4f.exe.zip`.
2.  **Размещение файла**: После загрузки найдите `.zip` файл в папке загрузок. Распакуйте его в каталог по вашему выбору в вашей системе, затем выполните файл `g4f.exe`, чтобы запустить приложение.
3.  **Открыть GUI**: Приложение запускает веб-сервер с GUI. Откройте свой любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4.  **Конфигурация брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить правильную работу приложения. Для этого откройте параметры брандмауэра Windows и разрешите работу приложения.

Выполнив эти шаги, вы сможете успешно установить и запустить приложение в своей системе Windows. Если во время установки возникнут какие-либо проблемы, обратитесь к нашему трекеру проблем или попробуйте связаться с нами через Discord для получения помощи.

#### 🐍 Установка Python

##### Предварительные требования:

1.  Установите Python 3.10+ с [python.org](https://www.python.org/downloads/).
2.  Установите Google Chrome для определенных провайдеров.

##### Установка с помощью PyPI:

```bash
pip install -U g4f[all]
```

> Как установить только части или отключить части? **Используйте частичные требования:** [/docs/requirements](docs/requirements.md)

##### Установка из источника:

```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

> Как загрузить проект с помощью git и установить требования проекта? **Прочитайте этот учебник и выполните его шаг за шагом:** [/docs/git](docs/git.md)

## 💡 Использование

### 📝 Генерация текста

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

```
Hello! How can I assist you today?
```

### 🎨 Генерация изображений

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

[![Image with cat](/docs/images/cat.jpeg)](docs/client.md)

### 🌐 Веб-интерфейс

**Запустите GUI с помощью Python:**

```python
from g4f.gui import run_gui

run_gui()
```

**Запустите через CLI (Для запуска Flask Server):**

```bash
python -m g4f.cli gui --port 8080 --debug
```

**Или запустите FastAPI Server:**

```bash
python -m g4f --port 8080 --debug
```

> **Подробнее о GUI:** Для получения подробных инструкций о том, как настроить, сконфигурировать и использовать GPT4Free GUI, обратитесь к [GUI Documentation](docs/gui.md). Это руководство включает пошаговые сведения о выборе провайдера, управлении беседами, использовании расширенных функций, таких как распознавание речи, и многое другое.

### 🤖 API вывода

**API вывода** обеспечивает плавную интеграцию со службами OpenAI через G4F, что позволяет развертывать эффективные решения AI.

- **Документация**: [Interference API Docs](docs/interference-api.md)
- **Конечная точка**: `http://localhost:1337/v1`
- **Swagger UI**: Изучите документацию OpenAPI через Swagger UI по адресу `http://localhost:1337/docs`
- **Выбор поставщика**: [Как указать поставщика?](docs/selecting_a_provider.md)

Этот API разработан для простой реализации и улучшенной совместимости с другими интеграциями OpenAI.

### 📱 Запуск на смартфоне

Запустите веб-интерфейс на своем смартфоне для удобного доступа в пути. Ознакомьтесь со специальным руководством, чтобы узнать, как настроить и использовать графический интерфейс на своем мобильном устройстве: [Запуск на смартфоне](docs/guides/phone.md)

#### **📘 Полная документация для Python API**

*   **Client API from G4F:** [/docs/client](docs/client.md)
*   **AsyncClient API from G4F:** [/docs/async_client](docs/async_client.md)
*   **Requests API from G4F:** [/docs/requests](docs/requests.md)
*   **File API from G4F:** [/docs/file](docs/file.md)
*   **PydanticAI and LangChain Integration for G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
*   **Legacy API with python modules:** [/docs/legacy](docs/legacy.md)
*   **G4F - Media Documentation** [/docs/media](/docs/media.md) *(New)*

## 🔗 Powered by gpt4free

<table>
  <thead align="center">
    <tr border: none;>
      <td>
        <b>🎁 Проекты</b>
      </td>
      <td>
        <b>⭐ Звезды</b>
      </td>
      <td>
        <b>📚 Форки</b>
      </td>
      <td>
        <b>🛎 Проблемы</b>
      </td>
      <td>
        <b>📬 Pull requests</b>
      </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="https://github.com/xtekky/gpt4free">
          <b>gpt4free</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/gpt4free/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/gpt4free/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/xtekky/gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/gpt4free/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/xtekky/gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/gpt4free/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <td>
      <a href="https://github.com/xiangsx/gpt4free-ts">
        <b>gpt4free-ts</b>
      </a>
    </td>
    <td>
      <a href="https://github.com/xiangsx/gpt4free-ts/stargazers">
        <img alt="Stars" src="https://img.shields.io/github/stars/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" />
      </a>
    </td>
    <td>
      <a href="https://github.com/xiangsx/gpt4free-ts/network/members">
        <img alt="Forks" src="https://img.shields.io/github/forks/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" />
      </a>
    </td>
    <td>
      <a href="https://github.com/xiangsx/gpt4free-ts/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" />
      </a>
    </td>
    <td>
      <a href="https://github.com/xiangsx/gpt4free-ts/pulls">
        <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" />
      </a>
    </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/zukixa/cool-ai-stuff/">
          <b>Список бесплатных AI API и потенциальных провайдеров</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/zukixa/cool-ai-stuff/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/zukixa/cool-ai-stuff/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/zukixa/cool-ai-stuff/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/zukixa/cool-ai-stuff/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
    <tr>
      <td>
        <a href="https://github.com/xtekky/chatgpt-clone">
          <b>ChatGPT-Clone</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/chatgpt-clone/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/chatgpt-clone/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/chatgpt-clone/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/xtekky/chatgpt-clone/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free">
          <b>Ai agent</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Josh-XT/AGiXT/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Josh-XT/AGiXT/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Josh-XT/AGiXT/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Josh-XT/AGiXT/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free">
          <b>Чат-бот ChatGpt для Discord</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/mishalhossin/Coding-Chatbot-Gpt4Free/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    <tr>
    <tr>
      <td>
        <a href="https://github.com/Zero6992/chatGPT-discord-bot">
          <b>chatGPT-discord-bot</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Zero6992/chatGPT-discord-bot/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Zero6992/chatGPT-discord-bot/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Zero6992/chatGPT-discord-bot/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Zero6992/chatGPT-discord-bot/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    <tr>
      <td>
        <a href="https://github.com/SamirXR/Nyx-Bot">
          <b>Nyx-Bot (Discord)</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/SamirXR/Nyx-Bot/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/SamirXR/Nyx-Bot/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/SamirXR/Nyx-Bot/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/SamirXR/Nyx-Bot/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/MIDORIBIN/langchain-gpt4free">
          <b>LangChain gpt4free</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/MIDORIBIN/langchain-gpt4free/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/MIDORIBIN/langchain-gpt4free/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/MIDORIBIN/langchain-gpt4free/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/MIDORIBIN/langchain-gpt4free/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free">
          <b>Чат-бот ChatGpt для Telegram</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot">
          <b>Чат-бот ChatGpt для Line</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/Lin-jun-xiang/action-translate-readme">
          <b>Action Translate Readme</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/action-translate-readme/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/action-translate-readme/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/action-translate-readme/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/action-translate-readme/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/Lin-jun-xiang/docGPT-streamlit">
          <b>Langchain Document GPT</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/issues">
          <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/pulls">
          <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/Simatwa/python-tgpt">
          <b>python-tgpt</b>
        </a>
      </td>
      <td>
        <a href="https://github.com/Simatwa/python-tgpt/stargazers">
          <img alt="Stars" src="https://img.shields.io/github/stars/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Simatwa/python-tgpt/network/members">
          <img alt="Forks" src="https://img.shields.io/github/forks/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />
        </a>
      </td>
      <td>
        <a href="https://github.com/Simatwa/python-tgpt/issues">
          <