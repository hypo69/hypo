# Документация для разработчика: gpt4free

## Обзор

Этот документ предоставляет обзор проекта gpt4free, включая информацию об установке, использовании, архитектуре и возможностях. Проект представляет собой proof-of-concept API для мультипровайдерных AI запросов, демонстрирующий балансировку нагрузки, контроль потока запросов и интеграцию с различными AI провайдерами.

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
  - [Локальный вывод](#-local-inference)
  - [API взаимодействия](#-interference-api)
  - [Конфигурация](#-configuration)
  - [Запуск на смартфоне](#-run-on-smartphone)
  - [Полная документация для Python API](#-full-documentation-for-python-api)
- [Провайдеры и модели](#-providers-and-models)
- [Проекты, использующие gpt4free](#-powered-by-gpt4free)
- [Вклад в проект](#-contribute)
  - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
  - [Как AI может помочь с написанием кода?](#guide-how-can-ai-help-me-with-writing-code)
- [Авторы](#-contributors)
- [Авторские права](#-copyright)
- [История звезд](#-star-history)
- [Лицензия](#-license)

## Подробнее

Проект gpt4free предназначен для облегчения интеграции с различными AI-провайдерами, предоставляя единый API для выполнения текстовых и графических запросов. Он включает в себя веб-интерфейс, API для взаимодействия и инструменты конфигурации, что позволяет разработчикам легко развертывать AI-решения. Проект активно поддерживается сообществом и предлагает возможности для внесения вклада.

## Установка

### Использование Docker

1.  **Установите Docker**: Скачайте и установите [Docker](https://docs.docker.com/get-docker/).
2.  **Настройте директории**: Перед запуском контейнера убедитесь, что необходимые директории данных существуют или могут быть созданы.
    ```bash
    mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
    sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
    ```
3.  **Запустите Docker контейнер**: Используйте следующие команды для получения последнего образа и запуска контейнера (только x64):
    ```bash
    docker pull hlohaus789/g4f
    docker run -p 8080:8080 -p 7900:7900 \
    --shm-size="2g" \
    -v ${PWD}/har_and_cookies:/app/har_and_cookies \
    -v ${PWD}/generated_images:/app/generated_images \
    hlohaus789/g4f:latest
    ```
4.  **Запуск Slim Docker Image**: Используйте следующие команды для запуска Slim Docker image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости: (x64 и arm64)
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
5.  **Доступ к клиентскому интерфейсу**:
    *   Для использования включенного клиента перейдите по адресу: [http://localhost:8080/chat/](http://localhost:8080/chat/)
    *   Или установите API base для своего клиента на: [http://localhost:8080/v1](http://localhost:8080/v1)
6.  **(Опционально) Вход в систему провайдера**:
    При необходимости вы можете получить доступ к рабочему столу контейнера здесь: http://localhost:7900/?autoconnect=1&resize=scale&password=secret для целей входа в систему провайдера.

### Windows Guide (.exe)

1.  **Скачайте приложение**: Посетите нашу [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и скачайте последнюю версию приложения, названную `g4f.exe.zip`.
2.  **Размещение файлов**: После скачивания найдите `.zip` файл в папке загрузок. Распакуйте его в выбранный каталог в вашей системе, затем выполните файл `g4f.exe` для запуска приложения.
3.  **Откройте GUI**: Приложение запускает веб-сервер с графическим интерфейсом. Откройте свой любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/) для доступа к интерфейсу приложения.
4.  **Конфигурация брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить приложению работать правильно. Для этого получите доступ к параметрам брандмауэра Windows и разрешите приложение.

### Python Installation

#### Prerequisites:

1.  Install Python 3.10+ from [python.org](https://www.python.org/downloads/).
2.  Install Google Chrome for certain providers.

#### Install with PyPI:

```bash
pip install -U g4f[all]
```

#### Install from Source:

```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

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

Результат:

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

**Запуск GUI с использованием Python:**

```python
from g4f.gui import run_gui

run_gui()
```

**Запуск через CLI (Для запуска Flask Server):**

```bash
python -m g4f.cli gui --port 8080 --debug
```

**Или, запуск FastAPI Server:**

```bash
python -m g4f --port 8080 --debug
```

### API взаимодействия

**Interference API** обеспечивает бесшовную интеграцию со службами OpenAI через G4F, что позволяет развертывать эффективные AI-решения.

*   **Документация**: [Interference API Docs](docs/interference-api.md)
*   **Endpoint**: `http://localhost:1337/v1`
*   **Swagger UI**: Explore the OpenAPI documentation via Swagger UI at `http://localhost:1337/docs`
*   **Provider Selection**: [How to Specify a Provider?](docs/selecting_a_provider.md)

### Запуск на смартфоне

Запустите веб-интерфейс на своем смартфоне для легкого доступа в дороге. Ознакомьтесь со специальным руководством, чтобы узнать, как настроить и использовать графический интерфейс на своем мобильном устройстве: [Run on Smartphone Guide](docs/guides/phone.md)

### Полная документация для Python API

*   **Client API from G4F:** [/docs/client](docs/client.md)
*   **AsyncClient API from G4F:** [/docs/async_client](docs/async_client.md)
*   **Requests API from G4F:** [/docs/requests](docs/requests.md)
*   **File API from G4F:** [/docs/file](docs/file.md)
*   **PydanticAI and LangChain Integration for G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
*   **Legacy API with python modules:** [/docs/legacy](docs/legacy.md)

## Проекты, использующие gpt4free

Список проектов, использующих gpt4free, доступен в таблице.

## Вклад в проект

Приветствуются вклады от сообщества. Создание pull request - все, что требуется - наш сопроцессор обработает процесс проверки кода.

## Авторы

Список всех авторов доступен [здесь](https://github.com/xtekky/gpt4free/graphs/contributors).

## Авторские права

Эта программа лицензируется в соответствии с [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```
xtekky/gpt4free: Copyright (C) 2023 xtekky

Эта программа является свободным программным обеспечением: вы можете перераспространять ее и/или модифицировать
в соответствии с условиями GNU General Public License, опубликованной
Free Software Foundation, либо версии 3 Лицензии, либо
(по вашему выбору) любой более поздней версии.

Эта программа распространяется в надежде, что она будет полезной,
но БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ; даже без подразумеваемой гарантии
ПРИГОДНОСТИ ДЛЯ ПРОДАЖИ или ПРИГОДНОСТИ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ. См.
GNU General Public License для получения более подробной информации.

Вы должны были получить копию GNU General Public License
вместе с этой программой. Если нет, см. <https://www.gnu.org/licenses/>.
```

## Star History

График истории звезд доступен по ссылке.

## Лицензия

Этот проект лицензирован в соответствии с [GNU_GPL_v3.0](https://github.com/xtekky/gpt4free/blob/main/LICENSE).