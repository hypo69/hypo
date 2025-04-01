# Документация для разработчика: gpt4free

## Обзор

Этот файл `README.md` предоставляет информацию о проекте `gpt4free`, который является PoC (proof of concept) API-пакетом для мультипровайдерных AI-запросов. Он демонстрирует такие функции, как балансировка нагрузки, управление потоком запросов и интеграция с различными AI-провайдерами.

## Подробней

Этот проект предоставляет API для работы с различными AI-провайдерами, позволяя пользователям отправлять текстовые и графические запросы. Он включает в себя документацию по установке, настройке и использованию API, а также информацию о поддерживаемых провайдерах и моделях. Проект также предоставляет Dockerfile для развертывания в контейнере.

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
  - [API взаимодействия](#-interference-api)
  - [Конфигурация](#-configuration)
  - [Запуск на смартфоне](#-run-on-smartphone)
  - [Полная документация для Python API](#-full-documentation-for-python-api)
- [Провайдеры и модели](#-providers-and-models)
- [На базе gpt4free](#-powered-by-gpt4free)
- [Вклад](#-contribute)
  - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
  - [Как AI может помочь мне в написании кода?](#guide-how-can-ai-help-me-with-writing-code)
- [Участники](#-contributors)
- [Авторское право](#-copyright)
- [История звезд](#-star-history)
- [Лицензия](#-license)

## Установка

### Использование Docker

1.  **Установка Docker:** [Скачать и установить Docker](https://docs.docker.com/get-docker/).
2.  **Настройка каталогов:** Перед запуском контейнера убедитесь, что необходимые каталоги данных существуют или могут быть созданы. Например, вы можете создать и установить права владения на эти каталоги, выполнив:

```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
```

3.  **Запуск Docker-контейнера:** Используйте следующие команды для загрузки последнего образа и запуска контейнера (только x64):

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

    *   **Чтобы использовать включенный клиент, перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
    *   **Или установите API base для вашего клиента на:** [http://localhost:8080/v1](http://localhost:8080/v1)
6.  **(Optional) Provider Login:**

    *   Если требуется, вы можете получить доступ к рабочему столу контейнера здесь: [http://localhost:7900/?autoconnect=1&resize=scale&password=secret](http://localhost:7900/?autoconnect=1&resize=scale&password=secret) для целей входа в систему провайдера.

### Руководство по Windows (.exe)

1.  **Скачать приложение**: Посетите нашу [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и скачайте последнюю версию приложения, названную `g4f.exe.zip`.
2.  **Размещение файлов**: После скачивания найдите `.zip` файл в вашей папке Downloads. Распакуйте его в каталог по вашему выбору в вашей системе, затем выполните файл `g4f.exe`, чтобы запустить приложение.
3.  **Открыть GUI**: Приложение запускает веб-сервер с GUI. Откройте ваш любимый браузер и перейдите к [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4.  **Конфигурация брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить правильную работу приложения. Для этого откройте параметры брандмауэра Windows и разрешите приложению.

### Установка Python

1.  **Предварительные требования:**
    *   Установите Python 3.10+ с [python.org](https://www.python.org/downloads/).
    *   Установите Google Chrome для определенных провайдеров.
2.  **Установка с помощью PyPI:**

```bash
pip install -U g4f[all]
```

**Установка из исходного кода:**

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

**Или, запустите FastAPI Server:**

```bash
python -m g4f --port 8080 --debug
```

### API взаимодействия

**Interference API** обеспечивает простую интеграцию со службами OpenAI через G4F, позволяя развертывать эффективные решения AI.

*   **Документация**: [Interference API Docs](docs/interference-api.md)
*   **Конечная точка**: `http://localhost:1337/v1`
*   **Swagger UI**: Изучите документацию OpenAPI через Swagger UI по адресу `http://localhost:1337/docs`
*   **Выбор провайдера**: [Как указать провайдера?](docs/selecting_a_provider.md)

### Запуск на смартфоне

Запустите веб-интерфейс на своем смартфоне для легкого доступа в пути. Ознакомьтесь со специальным руководством, чтобы узнать, как настроить и использовать GUI на своем мобильном устройстве: [Run on Smartphone Guide](docs/guides/phone.md)

## Ссылки на документацию

*   **Client API from G4F:** [/docs/client](docs/client.md)
*   **AsyncClient API from G4F:** [/docs/async_client](docs/async_client.md)
*   **Requests API from G4F:** [/docs/requests](docs/requests.md)
*   **File API from G4F:** [/docs/file](docs/file.md)
*   **PydanticAI and LangChain Integration for G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
*   **Legacy API with python modules:** [/docs/legacy](docs/legacy.md)
*   **G4F - Media Documentation** [/docs/media](/docs/media.md) *(New)*

## Вклад

Мы приветствуем вклад сообщества. Независимо от того, добавляете ли вы новых провайдеров или функции, или просто исправляете опечатки и вносите небольшие улучшения, ваш вклад ценится. Создание запроса на включение — это все, что нужно — наш сопроводитель обработает процесс проверки кода. Как только все изменения будут учтены, мы объединим запрос на включение в основную ветвь и выпустим обновления позже.

###### Руководство: Как создать нового провайдера?

*   **Прочитайте:** [Create Provider Guide](docs/guides/create_provider.md)

###### Руководство: Как AI может помочь мне в написании кода?

*   **Прочитайте:** [AI Assistance Guide](docs/guides/help_me.md)

## Авторское право

Эта программа лицензирована в соответствии с [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

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

## Лицензия

Этот проект лицензирован в соответствии с [GNU_GPL_v3.0](https://github.com/xtekky/gpt4free/blob/main/LICENSE).