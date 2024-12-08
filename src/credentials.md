### Initialization and Setup

Upon startup, the project initializes and sets up various configurations and credentials. This document explains how these values are established and managed.

#### Project Root Detection

The project automatically detects its root directory by searching upwards from the current file's directory for specific marker files (`pyproject.toml`, `requirements.txt`, `.git`). This ensures that the project can locate its resources regardless of the current working directory.

```python
def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.
    
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
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

#### Configuration Loading

The project loads its default settings from the `config.json` file located in the `src` directory. This JSON file contains various configuration parameters such as:

- **Author Information**: Details about the author.
- **Available Modes**: Supported modes (`dev`, `debug`, `test`, `prod`).
- **Paths**: Directories for logs, temporary files, external storage, and Google Drive.
- **Project Details**: Name, version, and release information.

```python
self.config = j_loads_ns(self.base_dir / 'src' / 'config.json')
if not self.config:
    logger.error('Ошибка при загрузке настроек')
    ...
    return

self.config.project_name = self.base_dir.name
```

#### Credential Management with KeePass

**What is KeePass?**

KeePass is a free and open-source password manager that securely stores your passwords and other sensitive information in an encrypted database. The database is protected by a master password, which is the only password you need to remember. KeePass uses strong encryption algorithms (such as AES and Twofish) to ensure that your data is secure.

**Why Use KeePass?**

- **Security**: KeePass uses industry-standard encryption to protect your data, making it highly secure against unauthorized access.
- **Portability**: You can store your KeePass database on a USB drive or cloud storage and access it from multiple devices.
- **Customization**: KeePass allows you to organize your passwords into groups and subgroups, making it easy to manage large numbers of credentials.
- **Open Source**: Being open-source, KeePass is transparent and can be audited by the community to ensure its security.

**How KeePass Works in This Project**

Credentials are securely managed using a KeePass database (`credentials.kdbx`). The master password for this database is handled differently based on the environment:

- **Development Mode**: The password is read from a file named `password.txt` located in the `secrets` directory.
- **Production Mode**: The password is entered via the console.

```python
def _open_kp(self, retry: int = 3) -> PyKeePass | None:
    """ Open KeePass database
    Args:
        retry (int): Number of retries
    """
    while retry > 0:
        try:
            password:str = Path( self.path.secrets / 'password.txt').read_text(encoding="utf-8") or None
            kp = PyKeePass(str(self.path.secrets / 'credentials.kdbx'), 
                           password = password or getpass.getpass(print('Enter KeePass master password: ').lower()))
            return kp
        except Exception as ex:
            print(f"Failed to open KeePass database Exception: {ex}, {retry-1} retries left.")
            ...
            retry -= 1
            if retry < 1:
                logger.critical('Failed to open KeePass database after multiple attempts', exc_info=True)
                ...
                sys.exit()
```

#### Singleton Design Pattern

The `ProgramSettings` class follows the Singleton design pattern, ensuring that only one instance of this class is created. This instance holds all the project's settings and credentials, providing a consistent configuration across the application.

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

#### Path Setup

The project sets up various paths for binaries, source code, logs, temporary files, and data directories. These paths are derived from the project root and can be overridden by values specified in the `config.json` file.

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

#### Credential Loading

The project loads credentials for various services (e.g., Aliexpress, OpenAI, Discord, Telegram) from the KeePass database. Each service has its own method for extracting and storing these credentials in the `ProgramSettings` instance.

```python
def _load_credentials(self) -> None:
    """ Загружает учетные данные из настроек."""

    kp = self._open_kp(3)
    if not kp:
        print("Error :( ")
        ...
        sys.exit(1)

    if not self._load_aliexpress_credentials(kp):
        print('Failed to load Aliexpress credentials')

    if not self._load_openai_credentials(kp):
        print('Failed to load OpenAI credentials')

    if not self._load_gemini_credentials(kp):
        print('Failed to load GoogleAI credentials')

    if not self._load_discord_credentials(kp):
        print('Failed to load Discord credentials')

    if not self._load_telegram_credentials(kp):
        print('Failed to load Telegram credentials')

    if not self._load_PrestaShop_credentials(kp):
        print('Failed to load PrestaShop credentials')

    if not self._load_smtp_credentials(kp):
        print('Failed to load SMTP credentials')

    if not self._load_facebook_credentials(kp):
        print('Failed to load Facebook credentials')

    if not self._load_presta_translations_credentials(kp):
        print('Failed to load Translations credentials')

    if not self._load_gapi_credentials(kp):
        print('Failed to load GAPI credentials')
```

#### Global Instance

A global instance of `ProgramSettings` is created to ensure that all parts of the application use the same settings and credentials.

```python
# Global instance of ProgamSettings
gs: ProgramSettings = ProgramSettings()
```

This setup ensures that the project is initialized with the correct paths, configurations, and credentials, providing a robust and secure environment for development and production.