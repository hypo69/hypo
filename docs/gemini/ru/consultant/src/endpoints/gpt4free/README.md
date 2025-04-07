### **Анализ кода модуля `README.md`**

2. **Качество кода**:
   - **Соответствие стандартам**: 7/10
   - **Плюсы**:
     - Хорошая структурированность и организация контента.
     - Наличие оглавления для удобной навигации.
     - Подробные инструкции по установке и использованию.
     - Указание на проекты, использующие `gpt4free`.
     - Информация о лицензии и авторских правах.
     - Список контрибьюторов с ссылками на их GitHub профили.
   - **Минусы**:
     - Не все разделы хорошо проработаны с точки зрения ясности и краткости.
     - Некоторые ссылки могут быть неактуальными или вести на внешние ресурсы, что требует проверки.
     - Отсутствует единообразие в оформлении (например, в таблице "Powered by gpt4free").
     - Местами избыточное использование изображений и значков.

3. **Рекомендации по улучшению**:
   - **Актуализация ссылок**:
     - Необходимо проверить все ссылки на актуальность и исправить неработающие.
   - **Улучшение структуры и ясности**:
     - Пересмотреть структуру документа, возможно, объединить некоторые разделы или переформулировать заголовки для большей логичности.
     - Сделать инструкции более краткими и понятными, избегая избыточной информации.
   - **Единообразие в оформлении**:
     - Привести к единообразию оформление таблицы "Powered by gpt4free", возможно, упростить её.
     - Оптимизировать использование изображений и значков, чтобы не перегружать документ.
   - **Добавление информации о вкладе**:
     - Расширить раздел "Contribute", добавив больше информации о том, как можно внести вклад в проект (например, описание процесса code review).
   - **Локализация**:
     - Рассмотреть возможность перевода документа на другие языки для расширения аудитории.

4. **Оптимизированный код**:

```markdown
### **Проект gpt4free**

[![xtekky%2Fgpt4free | Trendshift](https://trendshift.io/api/badge/repositories/1692)](https://trendshift.io/repositories/1692)

---

<p align="center">
  <span style="background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    <strong>Автор: <a href="https://github.com/xtekky">@xtekky</a></strong>
  </span>
</p>

#### **Важное уведомление**
> [!IMPORTANT]
> Используя этот репозиторий или любой связанный с ним код, вы соглашаетесь с [юридическим уведомлением](LEGAL_NOTICE.md). Автор не несет ответственности за использование этого репозитория и не поддерживает его. Автор также не несет ответственности за любые копии, форки, повторные загрузки, сделанные другими пользователями, или что-либо еще, связанное с GPT4Free. Это единственный аккаунт и репозиторий автора. Для предотвращения выдачи себя за другое лицо или безответственных действий, пожалуйста, соблюдайте лицензию GNU GPL, которую использует этот репозиторий.

#### **Предупреждение**
> [!WARNING]
> _"gpt4free"_ служит **PoC** (доказательством концепции), демонстрирующим разработку API-пакета с многопровайдерскими запросами, с такими функциями, как тайм-ауты, балансировка нагрузки и управление потоком.

#### **Примечание**
> [!NOTE]
> <sup><strong>Последняя версия:</strong></sup><br> [![PyPI version](https://img.shields.io/pypi/v/g4f?color=blue)](https://pypi.org/project/g4f) [![Docker version](https://img.shields.io/docker/v/hlohaus789/g4f?label=docker&color=blue)](https://hub.docker.com/r/hlohaus789/g4f)  
> <sup><strong>Статистика:</strong></sup><br> [![Downloads](https://static.pepy.tech/badge/g4f)](https://pepy.tech/project/g4f) [![Downloads](https://static.pepy.tech/badge/g4f/month)](https://pepy.tech/project/g4f)

Установка через pip:
```sh
pip install -U g4f[all]
```

Установка через Docker:
```sh
docker pull hlohaus789/g4f
```

#### **Что нового**

![1000032415](https://github.com/user-attachments/assets/4caab977-eb05-48ed-b750-3ad082bcfcae)

- **Изучите последние функции и обновления**  
  Подробности на нашей [странице релизов](https://github.com/xtekky/gpt4free/releases).
  
- **Будьте в курсе с нашим Telegram-каналом** 📨  
  Присоединяйтесь к нам: [telegram.me/g4f_channel](https://telegram.me/g4f_channel).
  
- **Подпишитесь на наш Discord-канал новостей** 💬🆕️  
  Будьте в курсе обновлений через наш [канал новостей: discord.gg/5E39JUWUFa](https://discord.gg/5E39JUWUFa).
  
- **Получите поддержку в нашем Discord-сообществе** 🤝💻  
  Обратитесь за помощью в нашу [группу поддержки: discord.gg/qXA4Wf4Fsm](https://discord.gg/qXA4Wf4Fsm).

#### **Удаление сайта**

Если ваш сайт находится в этом репозитории и вы хотите его удалить, отправьте электронное письмо на takedown@g4f.ai с подтверждением того, что он принадлежит вам, и он будет удален как можно быстрее. Чтобы предотвратить воспроизведение, пожалуйста, защитите свой API. 😉

#### **GPT4Free на HuggingFace**
[![HuggingSpace](https://github.com/user-attachments/assets/1d859e8a-d6fa-416f-a213-ccc26aa11e90)](https://huggingface.co/spaces/roxky/g4f-new)
**Это proof-of-concept API-пакет для многопровайдерских AI-запросов. Он демонстрирует такие функции, как:**

- Балансировка нагрузки и контроль потока запросов.
- Бесшовная интеграция с несколькими AI-провайдерами.
- Поддержка генерации текста и изображений.

> Изучите [GPT4Free на HuggingFace Space](https://huggingface.co/spaces/roxky/g4f-new) для размещенной версии или [Duplicate GPT4Free Space](https://huggingface.co/spaces/roxky/g4f-new?duplicate=true) для личного использования.

---

#### **Содержание**
- [Что нового](#-whats-new)
- [Содержание](#-table-of-contents)
- [Начало работы](#-getting-started)
  - [Установка](#-installation)
    - [Использование Docker](#-using-docker)
    - [Windows Guide (.exe)](#-windows-guide-exe)
    - [Python Installation](#-python-installation)
- [Использование](#-usage)
  - [Генерация текста](#-text-generation)
  - [Генерация изображений](#-image-generation)
  - [Веб-интерфейс](#-web-interface)
  - [Локальный вывод](docs/local.md)
  - [Interference API](#-interference-api)
  - [Конфигурация](docs/configuration.md)
  - [Запуск на смартфоне](#-run-on-smartphone)
  - [Полная документация для Python API](#-full-documentation-for-python-api)
- [Провайдеры и модели](docs/providers-and-models.md)
- [Powered by gpt4free](#-powered-by-gpt4free)
- [Вклад](#-contribute)
  - [Как создать нового провайдера?](#guide-how-do-i-create-a-new-provider)
  - [Как AI может помочь мне с написанием кода?](#guide-how-can-ai-help-me-with-writing-code)
- [Авторы](#-contributors)
- [Авторские права](#-copyright)
- [История звезд](#-star-history)
- [Лицензия](#-license)

---

#### **Начало работы**

#### **Установка**

##### **Использование Docker**
1. **Установите Docker:** [Скачайте и установите Docker](https://docs.docker.com/get-docker/).
2. **Настройте директории:** Перед запуском контейнера убедитесь, что необходимые директории данных существуют или могут быть созданы. Например, вы можете создать и установить права собственности на эти директории, выполнив:
```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_images
sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_images
```
3. **Запустите Docker-контейнер:** Используйте следующие команды, чтобы получить последнее изображение и запустить контейнер (только x64):
```bash
docker pull hlohaus789/g4f
docker run -p 8080:8080 -p 7900:7900 \
  --shm-size="2g" \
  -v ${PWD}/har_and_cookies:/app/har_and_cookies \
  -v ${PWD}/generated_images:/app/generated_images \
  hlohaus789/g4f:latest
```

4. **Запуск Slim Docker Image:** Используйте следующие команды для запуска Slim Docker Image. Эта команда также обновляет пакет `g4f` при запуске и устанавливает любые дополнительные зависимости: (x64 и arm64)
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
 
5. **Доступ к клиентскому интерфейсу:**
   - **Чтобы использовать включенный клиент, перейдите по адресу:** [http://localhost:8080/chat/](http://localhost:8080/chat/)
   - **Или установите API base для вашего клиента на:** [http://localhost:8080/v1](http://localhost:8080/v1)

6. **(Optional) Provider Login:**
   При необходимости вы можете получить доступ к рабочему столу контейнера здесь: http://localhost:7900/?autoconnect=1&resize=scale&password=secret для целей входа в систему провайдера.

---

##### **Windows Guide (.exe)**
Чтобы обеспечить бесперебойную работу нашего приложения, пожалуйста, следуйте инструкциям ниже. Эти шаги предназначены для руководства вами в процессе установки в операционных системах Windows.

**Инструкция по установке:**
1. **Скачайте приложение**: Посетите нашу [страницу релизов](https://github.com/xtekky/gpt4free/releases/tag/0.4.2.0) и скачайте последнюю версию приложения, названную `g4f.exe.zip`.
2. **Разместите файл**: После скачивания найдите `.zip` файл в вашей папке "Downloads". Распакуйте его в выбранный вами каталог в вашей системе, затем запустите файл `g4f.exe`, чтобы запустить приложение.
3. **Откройте GUI**: Приложение запускает веб-сервер с графическим интерфейсом. Откройте ваш любимый браузер и перейдите по адресу [http://localhost:8080/chat/](http://localhost:8080/chat/), чтобы получить доступ к интерфейсу приложения.
4. **Настройка брандмауэра (Hotfix)**: После установки может потребоваться настроить параметры брандмауэра Windows, чтобы разрешить приложению работать правильно. Для этого получите доступ к настройкам брандмауэра Windows и разрешите работу приложения.

Выполнив эти шаги, вы сможете успешно установить и запустить приложение в вашей системе Windows. Если вы столкнетесь с какими-либо проблемами в процессе установки, пожалуйста, обратитесь к нашему Issue Tracker или попробуйте связаться через Discord для получения помощи.

---

##### **Python Installation**

#### Prerequisites:
1. Установите Python 3.10+ с [python.org](https://www.python.org/downloads/).
2. Установите Google Chrome для определенных провайдеров.

#### Install with PyPI:
```bash
pip install -U g4f[all]
```

> Как установить только части или отключить части? **Используйте частичные требования:** [/docs/requirements](docs/requirements.md)

#### Install from Source:
```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
```

> Как загрузить проект с помощью git и установить требования проекта? **Прочитайте этот учебник и выполните его шаг за шагом:** [/docs/git](docs/git.md)

---

#### **Использование**

##### **Генерация текста**
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

##### **Генерация изображений**
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

##### **Веб-интерфейс**
**Запустите GUI с помощью Python:**
```python
from g4f.gui import run_gui

run_gui()
```
**Запустите через CLI (чтобы запустить Flask Server):**
```bash
python -m g4f.cli gui --port 8080 --debug
```
**Или запустите FastAPI Server:**
```bash
python -m g4f --port 8080 --debug
```

> **Узнайте больше о GUI:** Подробные инструкции о том, как настроить, сконфигурировать и использовать GPT4Free GUI, см. в [GUI Documentation](docs/gui.md). Это руководство содержит пошаговые инструкции по выбору провайдера, управлению беседами, использованию расширенных функций, таких как распознавание речи, и многое другое.

---

#### **Interference API**

**Interference API** обеспечивает бесшовную интеграцию со службами OpenAI через G4F, позволяя вам развертывать эффективные AI-решения.

- **Документация**: [Interference API Docs](docs/interference-api.md)
- **Endpoint**: `http://localhost:1337/v1`
- **Swagger UI**: Изучите документацию OpenAPI через Swagger UI по адресу `http://localhost:1337/docs`
- **Provider Selection**: [Как указать провайдера?](docs/selecting_a_provider.md)

Этот API разработан для простой реализации и улучшенной совместимости с другими интеграциями OpenAI.

---

#### **Запуск на смартфоне**
Запустите веб-интерфейс на своем смартфоне для легкого доступа в пути. Ознакомьтесь со специальным руководством, чтобы узнать, как настроить и использовать GUI на своем мобильном устройстве: [Run on Smartphone Guide](docs/guides/phone.md)

---

#### **Полная документация для Python API**
- **Client API от G4F:** [/docs/client](docs/client.md)
- **AsyncClient API от G4F:** [/docs/async_client](docs/async_client.md)
- **Requests API от G4F:** [/docs/requests](docs/requests.md)
- **File API от G4F:** [/docs/file](docs/file.md)
- **PydanticAI и LangChain Integration для G4F:** [/docs/pydantic_ai](docs/pydantic_ai.md)
- **Legacy API с python-модулями:** [/docs/legacy](docs/legacy.md)
- **G4F - Медиа-документация** [/docs/media](/docs/media.md) *(New)*

---

#### **Powered by gpt4free**

<table>
  <thead>
    <tr>
      <th>Проект</th>
      <th>Звезды</th>
      <th>Форки</th>
      <th>Проблемы</th>
      <th>Pull requests</th>
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
    <tr>
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
          <b>Free AI API\'s & Potential Providers List</b>
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
          <b>ChatGpt Discord Bot</b>
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
    </tr>
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
    </tr>
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
          <b>ChatGpt Telegram Bot</b>
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
          <b>ChatGpt Line Bot