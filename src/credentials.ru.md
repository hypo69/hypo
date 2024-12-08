### Инициализация и Настройка

При запуске проект инициализирует и настраивает различные конфигурации и учетные данные. Этот документ объясняет, как эти значения устанавливаются и управляются.

#### Определение Корневой Директории Проекта

Проект автоматически определяет свою корневую директорию, ища вверх от текущей директории файла для определенных маркерных файлов (`pyproject.toml`, `requirements.txt`, `.git`). Это гарантирует, что проект может найти свои ресурсы независимо от текущей рабочей директории.

```python
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с текущей директории файла,
    ища вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.
    
    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корневой директории проекта.
    
    Returns:
        Path: Путь к корневой директории, если найдена, иначе директория, где находится скрипт.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

#### Загрузка Конфигурации

Проект загружает свои настройки по умолчанию из файла `config.json`, расположенного в директории `src`. Этот JSON-файл содержит различные параметры конфигурации, такие как:

- **Информация об Авторе**: Детали об авторе.
- **Доступные Режимы**: Поддерживаемые режимы (`dev`, `debug`, `test`, `prod`).
- **Пути**: Директории для логов, временных файлов, внешнего хранилища и Google Drive.
- **Детали Проекта**: Название, версия и информация о релизе проекта.

```python
self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
if not self.config:
    logger.error('Ошибка при загрузке настроек')
    ...
    return

self.config.project_name = self.base_dir.name
```

#### Управление Учетными Данными с Использованием KeePass

**Что такое KeePass?**

KeePass — это бесплатный и открытый менеджер паролей, который безопасно хранит ваши пароли и другую чувствительную информацию в зашифрованной базе данных. База данных защищена мастер-паролем, который является единственным паролем, который вам нужно запомнить. KeePass использует сильные алгоритмы шифрования (такие как AES и Twofish), чтобы гарантировать безопасность ваших данных.

**Почему Использовать KeePass?**

- **Безопасность**: KeePass использует отраслевые стандарты шифрования для защиты ваших данных, делая их высокозащищенными от несанкционированного доступа.
- **Переносимость**: Вы можете хранить свою базу данных KeePass на USB-накопителе или в облачном хранилище и получать к ней доступ с нескольких устройств.
- **Настройка**: KeePass позволяет организовывать ваши пароли в группы и подгруппы, что упрощает управление большим количеством учетных данных.
- **Открытый Исходный Код**: Будучи проектом с открытым исходным кодом, KeePass прозрачен и может быть проверен сообществом на предмет его безопасности.

**Как KeePass Работает в Этом Проекте**

Учетные данные безопасно управляются с использованием базы данных KeePass (`credentials.kdbx`). Мастер-пароль для этой базы данных обрабатывается по-разному в зависимости от среды:

- **Режим Разработки**: Пароль считывается из файла с именем `password.txt`, расположенного в директории `secrets`.
- **Режим Продакшн**: Пароль вводится через консоль.

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Открывает базу данных KeePass
    Args:
        retry (int): Количество попыток
    """
    while retry > 0:
        try:
            password:str = Path( self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
            kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                           password = password or getpass.getpass(print('Введите мастер-пароль KeePass: ').lower()))
            return kp
        except Exception as ex:
            print(f"Не удалось открыть базу данных KeePass. Исключение: {ex}, осталось попыток: {retry-1}.")
            ...
            retry -= 1
            if retry < 1:
                logger.critical('Не удалось открыть базу данных KeePass после нескольких попыток', exc_info=True)
                ...
                sys.exit()
```

#### Одиночка (Singleton)

Класс `ProgramSettings` следует шаблону проектирования Singleton, гарантируя, что будет создан только один экземпляр этого класса. Этот экземпляр хранит все настройки и учетные данные проекта, обеспечивая согласованную конфигурацию во всем приложении.

```python
@singleton
class ProgramSettings(BaseModel):
    """ 
    `ProgramSettings` - класс настроек программы.
    
    Синглтон, хранящий основные параметры и настройки проекта.
    """
    
    class Config:
        arbitrary_types_allowed = True

    host_name:str = socket.gethostname()
    print(f'host_name: {host_name}')

    base_dir: Path = Field(default_factory=lambda: set_project_root())
    config: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace())
    credentials: SimpleNamespace = field(default_factory=lambda: SimpleNamespace(
        aliexpress=SimpleNamespace(
            api_key=None,
            secret=None,
            tracking_id=None,
            username=None,
            email=None,
            password=None
        ),
        presta=SimpleNamespace(
            translations=SimpleNamespace(
                server=None,
                port=None,
                database=None,
                user=None,
                password=None,
            ),
            client=[SimpleNamespace(
                server=None,
                port=None,
                database=None,
                user=None,
                password=None,
            )]
        ),
        openai=SimpleNamespace(
            api_key=None, 
            assistant_id=SimpleNamespace(), 
            project_api=None
        ),
        gemini=SimpleNamespace(api_key=None),
        rev_com=SimpleNamespace(client_api=None,
                                user_api=None),
        shutter_stock=SimpleNamespace(token=None),
        discord=SimpleNamespace(
            application_id=None, 
            public_key=None, 
            bot_token=None
        ),
        telegram=SimpleNamespace(
            bot=SimpleNamespace()
        ),
        smtp=[],
        facebook=[],
        gapi={}
    ))
    MODE: str = Field(default='dev')
    path: SimpleNamespace = Field(default_factory=lambda: SimpleNamespace(
        root = None,
        src = None,
        bin = None,
        log = None,
        tmp = None,
        data = None,
        secrets = None,
        google_drive = None,
        external_storage = None,
        tools = None,
        dev_null ='nul' if sys.platform == 'win32' else '/dev/null'
    ))
```

#### Настройка Путей

Проект настраивает различные пути для бинарных файлов, исходного кода, логов, временных файлов и директорий данных. Эти пути выводятся из корневой директории проекта и могут быть переопределены значениями, указанными в файле `config.json`.

```python
self.path = SimpleNamespace(
    root = Path(self.base_dir),
    bin = Path(self.base_dir / 'bin'), # <- тут бинарники (chrome, firefox, ffmpeg, ...)
    src = Path(self.base_dir) / 'src', # <- тут весь код
    endpoints = Path(self.base_dir) / 'src' / 'endpoints', # <- тут все клиенты
    secrets = Path(self.base_dir / 'secrets'),  # <- это папка с паролями и базой данных ! Ей нельзя попадать в гит!!!
    toolbox = Path(self.base_dir / 'toolbox'), # <- служебные утилиты

    log = Path(getattr(self.config.path, 'log', self.base_dir / 'log')), 
    tmp = Path(getattr(self.config.path, 'tmp', self.base_dir / 'tmp')),
    data = Path(getattr(self.config.path, 'data', self.base_dir / 'data')), # <- данные от endpoints (hypo69, kazarinov, prestashop, etc ...)
    google_drive = Path(getattr(self.config.path, 'google_drive', self.base_dir / 'google_drive')), # <- GOOGLE DRIVE ЧЕРЕЗ ЛОКАЛЬНЫЙ ДИСК (NOT API) 
    external_storage = Path(getattr(self.config.path, 'external_storage',  self.base_dir / 'external_storage') ),
)
```

#### Загрузка Учетных Данных

Проект загружает учетные данные для различных сервисов (например, Aliexpress, OpenAI, Discord, Telegram) из базы данных KeePass. Каждый сервис имеет свой собственный метод для извлечения и хранения этих учетных данных в экземпляре `ProgramSettings`.

```python
def _load_credentials(self) -> None:
    """ Загружает учетные данные из настроек."""

    kp = self._open_kp(3)
    if not kp:
        print("Ошибка :( ")
        ...
        sys.exit(1)

    if not self._load_aliexpress_credentials(kp):
        print('Не удалось загрузить учетные данные Aliexpress')

    if not self._load_openai_credentials(kp):
        print('Не удалось загрузить учетные данные OpenAI')

    if not self._load_gemini_credentials(kp):
        print('Не удалось загрузить учетные данные GoogleAI')

    if not self._load_discord_credentials(kp):
        print('Не удалось загрузить учетные данные Discord')

    if not self._load_telegram_credentials(kp):
        print('Не удалось загрузить учетные данные Telegram')

    if not self._load_PrestaShop_credentials(kp):
        print('Не удалось загрузить учетные данные PrestaShop')

    if not self._load_smtp_credentials(kp):
        print('Не удалось загрузить учетные данные SMTP')

    if not self._load_facebook_credentials(kp):
        print('Не удалось загрузить учетные данные Facebook')

    if not self._load_presta_translations_credentials(kp):
        print('Не удалось загрузить учетные данные Translations')

    if not self._load_gapi_credentials(kp):
        print('Не удалось загрузить учетные данные GAPI')
```

#### Глобальный Экземпляр

Создается глобальный экземпляр `ProgramSettings`, чтобы гарантировать, что все части приложения используют одни и те же настройки и учетные данные.

```python
# Глобальный экземпляр ProgramSettings
gs: ProgramSettings = ProgramSettings()
```

Эта настройка гарантирует, что проект инициализируется с правильными путями, конфигурациями и учетными данными, обеспечивая надежную и безопасную среду для разработки и производства.