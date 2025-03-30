## АНАЛИЗ КОДА: `FastApi` - Синглтон для FastAPI с Динамическим Управлением Портами

### 1. <алгоритм>

**Блок-схема работы класса `FastApi`:**

```mermaid
graph LR
    A[Начало: Создание экземпляра FastApi] --> B{_instance is None?};
    B -- Да --> C[Создание нового экземпляра super().__new__];
    C --> D[Инициализация атрибутов: _initialized=False, server_tasks={}, servers={}];
    B -- Нет --> E[Возврат существующего экземпляра];
    D --> F[Вызов __init__];
    E --> F;
    F --> G{_initialized?};
    G -- Да --> H[Конец __init__];
    G -- Нет --> I[Инициализация: super().__init__, self.router, self.host, self._initialized=True];
    I --> H;
    H --> J[Возврат экземпляра];

    J --> K[Вызов add_route(path, func, methods)];
    K --> L[Создание wrapper];
    L --> M[Добавление маршрута self.router.add_api_route(path, wrapper, methods)];
     M --> N[Вызов register_router()];
    N --> O[Регистрация роутера self.include_router(self.router)];
    O --> P[Вызов start(port)];
    P --> Q{port in server_tasks and not done()};
    Q -- Да --> R[Сообщение "Server already running"];
    Q -- Нет --> S[Создание задачи asyncio.create_task(_start_server(port))];
     S --> T[Сохранение задачи в self.server_tasks];

     T --> U[Вызов _start_server(port)];
     U --> V[Создание uvicorn.Config, uvicorn.Server];
     V --> W[Сохранение сервера в self.servers];
    W --> X[Запуск сервера await server.serve()];
    X --> Y[Вызов stop(port)];
    Y --> Z{port in self.servers and server.started};
    Z -- Да --> AA[Остановка сервера await self.servers[port].stop()];
     Z -- Нет --> AB[Конец stop(port)];

    AA --> AB;

     AB --> AC[Вызов stop_all()];
     AC --> AD[Для каждого порта в self.servers вызвать stop(port)]
     AD --> AE[Конец stop_all()]
```

**Примеры:**
* **Создание экземпляра `FastApi`:** Вызов `api = FastApi(title="My API", host="0.0.0.0")`. Если это первый вызов, создается новый экземпляр, иначе возвращается существующий.
* **`add_route`:** Вызов `api.add_route("/hello", test_function)`. Функция `test_function` обертывается в `wrapper` и добавляется по маршруту `/hello`.
* **`start`:** Вызов `api.start(port=8080)`. Если сервер на этом порту не запущен, запускается асинхронная задача для его запуска.
* **`stop`:** Вызов `await api.stop(port=8080)`. Останавливает сервер, работающий на порту `8080`, если такой существует и запущен.

### 2. <mermaid>

```mermaid
flowchart TD
    subgraph FastApi Class
        A[FastApi Instance Creation] --> B{_instance is None?};
        B -- Yes --> C[Create New Instance];
        C --> D[Initialize Attributes: _initialized=False, server_tasks={}, servers={}];
        B -- No --> E[Return Existing Instance];
        D --> F[Call __init__];
        E --> F;
        F --> G{_initialized?};
        G -- Yes --> H[End __init__];
        G -- No --> I[Initialize: super().__init__, self.router, self.host, self._initialized=True];
        I --> H;
        H --> J[Return Instance];

         J --> K[Call add_route(path, func, methods)];
        K --> L[Create Wrapper];
        L --> M[Add route to self.router.add_api_route(path, wrapper, methods)];
         M --> N[Call register_router()];
        N --> O[Register router self.include_router(self.router)];
        O --> P[Call start(port)];
        P --> Q{port in server_tasks and not done()};
        Q -- Yes --> R[Message "Server already running"];
         Q -- No --> S[Create task asyncio.create_task(_start_server(port))];
        S --> T[Save task to self.server_tasks];

         T --> U[Call _start_server(port)];
        U --> V[Create uvicorn.Config, uvicorn.Server];
       V --> W[Save server to self.servers];
        W --> X[Start server await server.serve()];

         X --> Y[Call stop(port)];
          Y --> Z{port in self.servers and server.started};
        Z -- Yes --> AA[Stop server await self.servers[port].stop()];
        Z -- No --> AB[End stop(port)];
        AA --> AB
        AB --> AC[Call stop_all()];
        AC --> AD[For each port in self.servers call stop(port)]
        AD --> AE[End stop_all()]
    end
    subgraph uvicorn
    BB[uvicorn.Config] --> CC[uvicorn.Server]
    CC --> DD[server.serve]
    end
     subgraph asyncio
      EE[asyncio.create_task]
      EE --> FF[asyncio.sleep]
    end

    subgraph fastapi
     GG[FastAPI as Fapi]
     GG --> HH[APIRouter]
      end
      J --> HH
      EE --> U
      V --> DD
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#f9f,stroke:#333,stroke-width:2px
    style P fill:#ccf,stroke:#333,stroke-width:2px
    style X fill:#ccf,stroke:#333,stroke-width:2px
    style Y fill:#ccf,stroke:#333,stroke-width:2px
    style AC fill:#ccf,stroke:#333,stroke-width:2px
```

**Описание зависимостей:**

*   `FastApi`: Основной класс, реализующий синглтон для FastAPI. Использует `uvicorn` для запуска сервера, `asyncio` для асинхронных операций и `fastapi` для маршрутизации.
*   `uvicorn`: Используется для создания и запуска HTTP-сервера. Класс `uvicorn.Config` используется для настройки сервера, а класс `uvicorn.Server` для его запуска и остановки.
*   `asyncio`: Используется для асинхронного запуска сервера (`create_task`) и задержек (`sleep`).
*   `fastapi`: Используется для создания веб-приложения (`FastAPI as Fapi`) и маршрутизации запросов (`APIRouter`).

### 3. <объяснение>

**Импорты:**

*   `from fastapi import FastAPI as Fapi, APIRouter`: Импортирует класс `FastAPI` (переименованный в `Fapi`) для создания веб-приложения и `APIRouter` для управления маршрутами.
*   `import uvicorn`: Импортирует библиотеку `uvicorn` для запуска асинхронного HTTP-сервера.
*   `from typing import List, Callable, Dict, Any`: Импортирует типы для аннотаций: `List`, `Callable`, `Dict`, `Any`.
*   `import functools`: Импортирует `functools` для работы с функциями, в частности, для использования декоратора `@functools.wraps`.
*   `import threading`: Импортирует модуль `threading`.
*   `import asyncio`: Импортирует модуль `asyncio` для работы с асинхронным кодом.

**Класс `FastApi`:**

*   **`_instance`**: Приватный атрибут класса, хранящий единственный экземпляр класса.
*   **`__new__(cls, *args, **kwargs)`**: Метод для реализации синглтона. Если экземпляр не существует, он создает его, иначе возвращает существующий.
*   **`__init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs)`**: Конструктор класса. Инициализирует приложение FastAPI, роутер и хост. Проверяет, инициализирован ли объект, для предотвращения повторной инициализации.
*   **`add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs)`**: Метод для добавления маршрута к приложению. Использует декоратор `functools.wraps`, чтобы сохранить метаданные исходной функции.
*   **`register_router(self)`**: Метод для регистрации роутера в приложении FastAPI.
*   **`_start_server(self, port: int)`**: Приватный асинхронный метод для запуска Uvicorn-сервера на заданном порту.
*   **`start(self, port: int)`**: Метод для запуска сервера на определенном порту. Проверяет, запущен ли уже сервер, и если нет, создает новую задачу asyncio.
*   **`stop(self, port: int)`**: Асинхронный метод для остановки сервера на заданном порту.
*   **`stop_all(self)`**: Асинхронный метод для остановки всех запущенных серверов.
*   **`get_app(self)`**: Метод для возврата текущего приложения FastAPI.
*   **`server_tasks`**: Словарь для хранения задач запущенных серверов (`port: task`).
*   **`servers`**: Словарь для хранения запущенных серверов (`port: server`).
*    **`router`**: Объект `APIRouter` для управления маршрутами.

**Функции:**

*   `test_function()`: Асинхронная тестовая функция, возвращает строку "It is working!!!".
*   `test_post(data: Dict[str, str])`: Функция для обработки POST-запроса, возвращает словарь с результатом и переданными данными.
*   `main()`: Асинхронная функция, содержащая пример использования класса `FastApi`. Создает экземпляр, добавляет маршруты, запускает и останавливает серверы на разных портах.

**Переменные:**

*   `api`: Экземпляр класса `FastApi`, используемый в примере.
*   `port`: Целочисленная переменная, представляющая номер порта, на котором запускается сервер.
*   `task`: Объект асинхронной задачи, возвращенный `asyncio.create_task`.
*   `config`: Объект `uvicorn.Config`, содержащий настройки сервера.
*  `server`: Объект `uvicorn.Server`, представляющий HTTP-сервер.
*   `data`: Словарь, представляющий данные, переданные в POST-запросе.
*   `path`: Строка, представляющая путь маршрута.
*    `func`: Функция, которая будет вызвана при запросе по указанному маршруту.
*   `methods`: Список строк, представляющих HTTP-методы (например, `GET`, `POST`).
*  `wrapper`: Обертка для функции `func`.

**Потенциальные ошибки и области для улучшения:**

*   Не обрабатываются исключения при запуске и остановке сервера, что может привести к непредсказуемому поведению.
*   Нет механизма для проверки, доступен ли порт перед его использованием.
*   Отсутствует возможность настройки логирования uvicorn.
*   Класс `FastApi` не предоставляет возможности для добавления middleware.
*   Использование `print` для логирования не является лучшей практикой. Рекомендуется использовать стандартный модуль `logging`.
*   Следует использовать более надежные механизмы управления многопоточностью.

**Цепочка взаимосвязей:**
`FastApi` является ядром данного примера. Он инкапсулирует логику для работы с `FastAPI`, `uvicorn`, и `asyncio`.

1. **Инициализация**: При создании экземпляра `FastApi` через синглтон, вызывается `__init__`, где создается экземпляр `FastAPI` и `APIRouter`.
2. **Маршрутизация**: Метод `add_route` используется для добавления новых маршрутов, которые регистрируются через `register_router`.
3. **Запуск сервера**: При вызове метода `start` создается асинхронная задача `_start_server`, использующая `uvicorn` для запуска HTTP сервера на заданном порту.
4. **Остановка сервера**: Методы `stop` и `stop_all` останавливают запущенные серверы.
5. **Асинхронность**: Все операции, связанные с запуском и остановкой сервера, выполняются асинхронно с помощью `asyncio`.

**Взаимосвязь с другими частями проекта (если применимо):**
В предоставленном коде не указаны другие части проекта, но можно предположить, что `FastApi` может быть использован как основной класс для создания API-сервисов, где каждый сервис использует свой экземпляр `FastApi` для управления своими API-точками и портами.

В целом, код предоставляет функциональность для динамического управления портами FastAPI-приложения с использованием синглтона, асинхронности и библиотеки `uvicorn`.