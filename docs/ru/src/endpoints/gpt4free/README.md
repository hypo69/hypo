# Документация для разработчика: gpt4free

## Обзор

Этот документ предоставляет подробное описание проекта `gpt4free`, включая информацию об установке, использовании, структуре и возможностях. Проект представляет собой Proof-of-Concept (PoC) API-пакет для мультипровайдерных AI-запросов, демонстрирующий такие функции, как балансировка нагрузки, контроль потока запросов и интеграция с различными AI-провайдерами для генерации текста и изображений.

## Подробней

Проект `gpt4free` предоставляет API для работы с различными AI-провайдерами, позволяя генерировать текст и изображения. Он включает в себя инструменты для установки и настройки, примеры использования и информацию о поддерживаемых провайдерах и моделях. Проект также предоставляет веб-интерфейс для удобного взаимодействия с API.

## Содержание

- [🆕 Что нового](#-whats-new)
- [📚 Оглавление](#-table-of-contents)
- [⚡️ Начало работы](#-getting-started)
  - [🛠 Установка](#-installation)
    - [🐳 Использование Docker](#-using-docker)
    - [🪟 Руководство по Windows (.exe)](#-windows-guide-exe)
    - [🐍 Установка Python](#-python-installation)
- [💡 Использование](#-usage)
  - [📝 Генерация текста](#-text-generation)
  - [🎨 Генерация изображений](#-image-generation)
  - [🌐 Веб-интерфейс](#-web-interface)
  - [🖥️ Локальный вывод](docs/local.md)
  - [🤖 API интерфейса](#-interference-api)
  - [🛠️ Конфигурация](docs/configuration.md)
  - [📱 Запуск на смартфоне](#-run-on-smartphone)
  - [📘 Полная документация для Python API](#-full-documentation-for-python-api)
- [🚀 Провайдеры и модели](docs/providers-and-models.md)
- [🔗 На базе gpt4free](#-powered-by-gpt4free)
- [🤝 Вклад](#-contribute)
  - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
  - [Как AI может помочь мне в написании кода?](#guide-how-can-ai-help-me-with-writing-code)
- [🙌 Авторы](#-contributors)
- [©️ Авторские права](#-copyright)
- [⭐ История звезд](#-star-history)
- [📄 Лицензия](#-license)

## ⚡️ Начало работы

Этот раздел описывает, как начать работу с проектом `gpt4free`.

### 🛠 Установка

#### 🐳 Использование Docker

1.  **Установите Docker:** [Загрузите и установите Docker](https://docs.docker.com/get-docker/).
2.  **Настройте каталоги:** Перед запуском контейнера убедитесь, что необходимые каталоги данных существуют или могут быть созданы. Например:

    ```bash
    mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
    sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
    ```

3.  **Запустите Docker-контейнер:** Используйте следующие команды для извлечения последнего образа и запуска контейнера (только x64):

    ```bash
    docker pull hlohaus789/g4f
    docker run -p 8080:8080 -p 7900:7900 \
      --shm-size="2g" \
      -v ${PWD}/har_and_cookies:/app/har_and_cookies \
      -v ${PWD}/generated_images:/app/generated_images \
      hlohaus789/g4f:latest
    ```

4.  **Запустите Slim Docker Image:** Используйте следующие команды для запуска Slim Docker Image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости (x64 и arm64):

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
    - **Для использования прилагаемого клиента перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
    - **Или установите базовый API для вашего клиента на:** [http://localhost:8080/v1](http://localhost:8080/v1)

6.  **(Необязательно) Вход в провайдер:**
    При необходимости вы можете получить доступ к рабочему столу контейнера здесь: [http://localhost:7900/?autoconnect=1&resize=scale&password=secret](http://localhost:7900/?autoconnect=1&resize=scale&password=secret) для целей входа в провайдер.

#### 🪟 Руководство по Windows (.exe)

1.  **Загрузите приложение:** Посетите нашу [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и загрузите последнюю версию приложения, названную `g4f.exe.zip`.
2.  **Разместите файл:** После загрузки найдите файл `.zip` в папке "Загрузки". Распакуйте его в выбранный вами каталог в вашей системе, затем запустите файл `g4f.exe`, чтобы запустить приложение.
3.  **Откройте GUI:** Приложение запускает веб-сервер с графическим интерфейсом. Откройте свой любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4.  **Настройка брандмауэра (Hotfix):** После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить правильную работу приложения. Для этого зайдите в настройки брандмауэра Windows и разрешите приложение.

#### 🐍 Установка Python

##### Необходимые условия:

1.  Установите Python 3.10+ с сайта [python.org](https://www.python.org/downloads/).
2.  Установите Google Chrome для определенных провайдеров.

##### Установка с помощью PyPI:

```bash
pip install -U g4f[all]
```

##### Установка из исходного кода:

```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

## 💡 Использование

Этот раздел содержит примеры использования `gpt4free` для различных задач.

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

Результат:

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

### 🌐 Веб-интерфейс

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

### 🤖 API интерфейса

**Interference API** обеспечивает плавную интеграцию со службами OpenAI через G4F, что позволяет развертывать эффективные решения AI.

- **Документация**: [Interference API Docs](docs/interference-api.md)
- **Endpoint**: `http://localhost:1337/v1`
- **Swagger UI**: Изучите документацию OpenAPI через Swagger UI по адресу `http://localhost:1337/docs`

### 📱 Запуск на смартфоне

Запустите веб-интерфейс на своем смартфоне для легкого доступа в дороге. [Руководство по запуску на смартфоне](docs/guides/phone.md)

#### **📘 Полная документация для Python API**

- **Client API from G4F:** [/docs/client](docs/client.md)
- **AsyncClient API from G4F:** [/docs/async_client](docs/async_client.md)
- **Requests API from G4F:** [/docs/requests](docs/requests.md)
- **File API from G4F:** [/docs/file](docs/file.md)
- **PydanticAI and LangChain Integration for G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
- **Legacy API with python modules:** [/docs/legacy](docs/legacy.md)
- **G4F - Media Documentation** [/docs/media](/docs/media.md) *(New)*

## 🔗 На базе gpt4free

В этом разделе перечислены проекты, использующие `gpt4free`.

## 🤝 Вклад

Приглашаем к участию в сообществе. Независимо от того, добавляете ли вы новых провайдеров или функции, или просто исправляете опечатки и вносите небольшие улучшения, ваш вклад ценен.

###### Руководство: Как создать нового провайдера?

- **Читать:** [Руководство по созданию провайдера](docs/guides/create_provider.md)

###### Руководство: Как AI может помочь мне в написании кода?

- **Читать:** [Руководство по помощи AI](docs/guides/help_me.md)

## 🙌 Авторы

Список всех авторов доступен [здесь](https://github.com/xtekky/gpt4free/graphs/contributors)

## ©️ Авторские права

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

## ⭐ История звезд

График истории звезд репозитория.

## 📄 Лицензия

Проект лицензирован под GNU GPL v3.0.