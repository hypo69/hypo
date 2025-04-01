# Документация для разработчика gpt4free

## Обзор

Этот документ предоставляет обзор проекта `gpt4free`, включая информацию об установке, использовании, структуре, а также сведения о лицензировании и вкладе в проект. `gpt4free` - это proof-of-concept API для выполнения запросов к различным AI-провайдерам, реализующий такие функции, как балансировка нагрузки, контроль потока запросов и интеграция с несколькими AI-провайдерами.

## Подробнее

Проект `gpt4free` предоставляет API для бесплатного использования различных AI-моделей. Он включает в себя клиентскую библиотеку, примеры использования, документацию и информацию о том, как внести свой вклад в проект. Проект поддерживает генерацию текста и изображений, а также имеет веб-интерфейс.

## Содержание

- [Что нового](#-whats-new)
- [Таблица содержания](#-table-of-contents)
- [Начало работы](#-getting-started)
  - [Установка](#-installation)
    - [Использование Docker](#-using-docker)
    - [Руководство по Windows (.exe)](#-windows-guide-exe)
    - [Установка Python](#-python-installation)
- [Использование](#-usage)
  - [Генерация текста](#-text-generation)
  - [Генерация изображений](#-image-generation)
  - [Веб-интерфейс](#-web-interface)
  - [Локальный вывод](#-local-inference)
  - [API помех](#-interference-api)
  - [Конфигурация](#-configuration)
  - [Запуск на смартфоне](#-run-on-smartphone)
  - [Полная документация для Python API](#-full-documentation-for-python-api)
- [Провайдеры и модели](#-providers-and-models)
- [На базе gpt4free](#-powered-by-gpt4free)
- [Вклад](#-contribute)
  - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
  - [Как ИИ может помочь мне в написании кода?](#guide-how-can-ai-help-me-with-writing-code)
- [Участники](#-contributors)
- [Авторские права](#-copyright)
- [История звезд](#-star-history)
- [Лицензия](#-license)

## Установка

### Использование Docker

1.  **Установите Docker:** [Скачайте и установите Docker](https://docs.docker.com/get-docker/).
2.  **Настройте каталоги:** Перед запуском контейнера убедитесь, что необходимые каталоги данных существуют или могут быть созданы. Например, вы можете создать и установить права собственности на эти каталоги, выполнив:

```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
```

3.  **Запустите Docker контейнер:** Используйте следующие команды, чтобы загрузить последнее изображение и запустить контейнер (только x64):

```bash
docker pull hlohaus789/g4f
docker run -p 8080:8080 -p 7900:7900 \
  --shm-size="2g" \
  -v ${PWD}/har_and_cookies:/app/har_and_cookies \
  -v ${PWD}/generated_images:/app/generated_images \
  hlohaus789/g4f:latest
```

4.  **Запуск Slim Docker Image:** Используйте следующие команды, чтобы запустить Slim Docker Image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости: (x64 и arm64)

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

*   **Чтобы использовать включенный клиент, перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
*   **Или установите базу API для своего клиента на:** [http://localhost:8080/v1](http://localhost:8080/v1)

6.  **(Необязательно) Вход в систему провайдера:**

Если требуется, вы можете получить доступ к рабочему столу контейнера здесь: http://localhost:7900/?autoconnect=1&resize=scale&password=secret для целей входа в систему провайдера.

### Руководство по Windows (.exe)

Для обеспечения бесперебойной работы нашего приложения, пожалуйста, следуйте инструкциям ниже. Эти шаги предназначены для того, чтобы помочь вам в процессе установки в операционных системах Windows.

**Этапы установки:**

1.  **Загрузите приложение**: Посетите нашу [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и скачайте самую последнюю версию приложения, названную `g4f.exe.zip`.
2.  **Размещение файлов**: После загрузки найдите `.zip` файл в папке Downloads. Распакуйте его в выбранный вами каталог в вашей системе, затем запустите файл `g4f.exe`, чтобы запустить приложение.
3.  **Откройте GUI**: Приложение запускает веб-сервер с GUI. Откройте ваш любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4.  **Конфигурация брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить приложению работать правильно. Для этого получите доступ к настройкам брандмауэра Windows и разрешите приложению.

Выполнив эти шаги, вы сможете успешно установить и запустить приложение в вашей системе Windows. Если во время процесса установки возникнут какие-либо проблемы, обратитесь к нашему Issue Tracker или попробуйте связаться через Discord для получения помощи.

### Установка Python

#### Предварительные требования:

1.  Установите Python 3.10+ из [python.org](https://www.python.org/downloads/).
2.  Установите Google Chrome для определенных провайдеров.

#### Установка с помощью PyPI:

```bash
pip install -U g4f[all]
```

> Как установить только части или отключить части? **Используйте частичные требования:** [/docs/requirements](docs/requirements.md)

#### Установка из исходного кода:

```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

> Как загрузить проект с использованием git и установить требования проекта? **Прочитайте этот учебник и выполните его шаг за шагом:** [/docs/git](docs/git.md)

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

```
Hello! How can I assist you today?
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

**Запустите GUI с помощью Python:**

```python
from g4f.gui import run_gui

run_gui()
```

**Запуск через CLI (Для запуска Flask Server):**

```bash
python -m g4f.cli gui --port 8080 --debug
```

**Или запустите FastAPI Server:**

```bash
python -m g4f --port 8080 --debug
```

> **Узнайте больше о GUI:** Подробные инструкции о том, как настроить, сконфигурировать и использовать GPT4Free GUI, см. в [Документации GUI](docs/gui.md). Это руководство содержит пошаговые сведения о выборе провайдера, управлении беседами, использовании расширенных функций, таких как распознавание речи, и многое другое.

### API помех

**Interference API** обеспечивает бесшовную интеграцию со службами OpenAI через G4F, позволяя развертывать эффективные решения AI.

*   **Документация**: [Interference API Docs](docs/interference-api.md)
*   **Endpoint**: `http://localhost:1337/v1`
*   **Swagger UI**: Исследуйте документацию OpenAPI через Swagger UI по адресу `http://localhost:1337/docs`
*   **Выбор провайдера**: [Как указать провайдера?](docs/selecting_a_provider.md)

Этот API разработан для простой реализации и улучшенной совместимости с другими интеграциями OpenAI.

### Запуск на смартфоне

Запустите веб-интерфейс на своем смартфоне для легкого доступа в дороге. Ознакомьтесь со специальным руководством, чтобы узнать, как настроить и использовать графический интерфейс на своем мобильном устройстве: [Руководство по запуску на смартфоне](docs/guides/phone.md)

#### **Полная документация для Python API**

*   **Client API из G4F:** [/docs/client](docs/client.md)
*   **AsyncClient API из G4F:** [/docs/async_client](docs/async_client.md)
*   **Requests API из G4F:** [/docs/requests](docs/requests.md)
*   **File API из G4F:** [/docs/file](docs/file.md)
*   **PydanticAI и LangChain Integration для G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
*   **Legacy API с python модулями:** [/docs/legacy](docs/legacy.md)
*   **G4F - Медиа Документация** [/docs/media](/docs/media.md) *(New)*

## На базе gpt4free

|                                           🎁 Projects                                            |                                     ⭐ Stars                                      |                                   📚 Forks                                    |                                  🛎 Issues                                  |                              📬 Pull requests                              |
| :----------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
|                                      **gpt4free**                                      |  <img alt="Stars" src="https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&labelColor=343b41" />  | <img alt="Forks" src="https://img.shields.io/github/forks/xtekky/gpt4free?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/xtekky/gpt4free?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/gpt4free?style=flat-square&labelColor=343b41" /> |
|                                    **gpt4free-ts**                                     | <img alt="Stars" src="https://img.shields.io/github/stars/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41" /> |
|                      **Free AI API's & Potential Providers List**                       |  <img alt="Stars" src="https://img.shields.io/github/stars/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41" /> |
|                                    **ChatGPT-Clone**                                     | <img alt="Stars" src="https://img.shields.io/github/stars/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41" /> |
|                                         **Ai agent**                                         | <img alt="Stars" src="https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> |
|                                  **ChatGpt Discord Bot**                                  | <img alt="Stars" src="https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/mishalhossin/Coding-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> |
|                                  **chatGPT-discord-bot**                                  | <img alt="Stars" src="https://img.shields.io/github/stars/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41" /> |
|                                   **Nyx-Bot (Discord)**                                   |   <img alt="Stars" src="https://img.shields.io/github/stars/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />   |  <img alt="Forks" src="https://img.shields.io/github/forks/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />  |  <img alt="Issues" src="https://img.shields.io/github/issues/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />  |  <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41" />  |
|                                   **LangChain gpt4free**                                   | <img alt="Stars" src="https://img.shields.io/github/stars/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41" /> |
|                                **ChatGpt Telegram Bot**                                 | <img alt="Stars" src="https://img.shields.io/github/stars/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41" /> |
|                                  **ChatGpt Line Bot**                                  | <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41" /> |
|                                 **Action Translate Readme**                                 | <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41" /> |
|                                 **Langchain Document GPT**                                  | <img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41" /> |
|                                      **python-tgpt**                                      |   <img alt="Stars" src="https://img.shields.io/github/stars/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />   |  <img alt="Forks" src="https://img.shields.io/github/forks/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />  |  <img alt="Issues" src="https://img.shields.io/github/issues/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />  |  <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Simatwa/python-tgpt?style=flat-square&labelColor=343b41" />  |
|                                       **GPT4js**                                       |   <img alt="Stars" src="https://img.shields.io/github/stars/zachey01/gpt4free.js?style=flat-square&labelColor=343b41" />   |  <img alt="Forks" src="https://img.shields.io/github/forks/zachey01/gpt4free.js?style=flat-square&labelColor=343b41" />  |  <img alt="Issues" src="https://img.shields.io/github/issues/zachey01/gpt4free.js?style=flat-square&labelColor=343b41" />  |  <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/zachey01/gpt4free.js?style=flat-square&labelColor=343b41" />  |
|                                **VividNode (pyqt-openai)**                                 |  <img alt="Stars" src="https://img.shields.io/github/stars/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41" /> | <img alt="Forks" src="https://img.shields.io/github/forks/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41" /> | <img alt="Issues" src="https://img.shields.io/github/issues/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41" /> | <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/yjg30737/pyqt-openai?style=flat-square&labelColor=343b41" /> |

## Вклад

Мы приветствуем вклад сообщества. Независимо от того, добавляете ли вы новых провайдеров или функции, или просто исправляете опечатки и вносите небольшие улучшения, ваш вклад ценится. Создание запроса на вытягивание — это все, что нужно — наш второй пилот обработает процесс проверки кода. Как только все изменения будут устранены, мы объединим запрос на вытягивание в основную ветку и выпустим обновления позднее.

###### Руководство: Как создать нового провайдера?

*   **Прочитайте:** [Руководство по созданию провайдера](docs/guides/create_provider.md)

###### Руководство: Как ИИ может помочь мне в написании кода?

*   **Прочитайте:** [Руководство по помощи ИИ](docs/guides/help_me.md)

## Участники

Список всех участников доступен [здесь](https://github.com/xtekky/gpt4free/graphs/contributors)

## Авторские права

Эта программа лицензируется в соответствии с [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```
xtekky/gpt4free: Copyright (C) 2023 xtekky

Эта программа является свободным программным обеспечением: вы можете распространять ее и/или изменять
в соответствии с условиями GNU General Public License, опубликованными
Free Software Foundation, либо версии 3 лицензии, либо
(по вашему выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной,
но БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемой гарантии
КОММЕРЧЕСКОЙ ПРИГОДНОСТИ ИЛИ ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ.  См.
GNU General Public License для получения более подробной информации.

Вы должны были получить копию GNU General Public License
вместе с этой программой.  Если нет, см. <https://www.gnu.org/licenses/>.
```

## История звезд

## Лицензия

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                              |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/1200px-GPLv3_Logo.svg.png" width="80%"></img> | <img src="https://img.shields.io/badge/License-GNU_GPL_v3.0-red.svg"/> <br> Этот проект лицензируется в соответствии с [GNU_GPL_v3.0](https://github.com/xtekky/gpt4free/blob/main/LICENSE). |