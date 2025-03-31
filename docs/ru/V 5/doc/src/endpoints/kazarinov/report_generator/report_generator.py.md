# Модуль `report_generator.py`

## Обзор

Модуль предназначен для генерации отчетов в формате HTML, PDF и DOCX на основе данных, полученных в формате JSON. Он использует шаблонизатор Jinja2 для создания HTML-страниц, а также библиотеки `pdfkit` и `python-docx` для преобразования HTML в PDF и DOCX соответственно.

## Подробней

Данный модуль является частью проекта `hypotez` и расположен в поддиректории `src/endpoints/kazarinov/report_generator`. Он используется для автоматического создания отчетов, предположительно, для мехиронов Казаринова. Модуль предоставляет класс `ReportGenerator`, который инкапсулирует логику генерации отчетов различных форматов на основе предоставленных данных и шаблонов.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Как работает класс**:
Класс `ReportGenerator` предназначен для создания отчетов в различных форматах (HTML, PDF, DOCX) на основе данных, полученных в формате JSON. Он инициализируется с параметрами, определяющими необходимость генерации PDF и DOCX. Основная логика работы класса заключается в загрузке данных, применении шаблонов Jinja2 для создания HTML-контента и последующем преобразовании HTML в PDF и DOCX с использованием соответствующих библиотек. Класс также включает методы для сохранения сгенерированных отчетов в файлы и отправки PDF-файлов через Telegram-бота.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `ReportGenerator` и определяет, какие форматы отчетов необходимо генерировать.
- `create_reports_async`: Асинхронно создает отчеты во всех требуемых форматах (HTML, PDF, DOCX).
- `service_apendix`: Создает словарь с данными для сервисного приложения.
- `create_html_report_async`: Асинхронно генерирует HTML-контент на основе шаблона и данных.
- `create_pdf_report_async`: Асинхронно генерирует PDF-отчет на основе HTML-контента.
- `create_docx_report_async`: Асинхронно генерирует DOCX-отчет на основе HTML-контента.

**Параметры**:

- `if_need_pdf` (Optional[bool], optional): Флаг, определяющий необходимость генерации PDF-отчета. По умолчанию `True`.
- `if_need_docx` (Optional[bool], optional): Флаг, определяющий необходимость генерации DOCX-отчета. По умолчанию `True`.
- `if_need_html` (bool): Указывает, требуется ли генерация HTML-отчета.
- `storage_path` (Path): Путь к директории хранения отчетов. По умолчанию `Path(gs.path.external_storage, ENDPOINT)`.
- `html_path` (Path | str): Путь к HTML-файлу.
- `pdf_path` (Path | str): Путь к PDF-файлу.
- `docs_path` (Path | str): Путь к DOCX-файлу.
- `html_content` (str): HTML-контент отчета.
- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчета.
- `mexiron_name` (str): Имя мехирона.
- `env` (Environment): Окружение Jinja2 для шаблонизации.

**Примеры**:

```python
report_generator = ReportGenerator(if_need_pdf=True, if_need_docx=False)
```

## Функции

### `create_reports_async`

```python
async def create_reports_async(bot: telebot.TeleBot, chat_id: int, data: dict, lang: str, mexiron_name: str) -> tuple:
    """Create ALL types: HTML, PDF, DOCX"""
    ...
    self.mexiron_name = mexiron_name
    export_path = self.storage_path / 'mexironim' / self.mexiron_name

    self.html_path = export_path / f"{self.mexiron_name}_{lang}.html"
    self.pdf_path = export_path / f"{self.mexiron_name}_{lang}.pdf"
    self.docx_path = export_path / f"{self.mexiron_name}_{lang}.docx"
    self.bot = bot
    self.chat_id = chat_id

    self.html_content = await self.create_html_report_async(data, lang, self.html_path)

    if not self.html_content:
        return False

    if self.if_need_pdf:
        await self.create_pdf_report_async(self.html_content, lang, self.pdf_path)

    if self.if_need_docx:
        await self.create_pdf_report_async(self.html_content, lang, self.pdf_path)
```

**Описание**: Асинхронно создает отчеты во всех требуемых форматах (HTML, PDF, DOCX).

**Как работает функция**:
Функция `create_reports_async` является асинхронной и отвечает за создание отчетов во всех необходимых форматах: HTML, PDF и DOCX. Она принимает Telegram-бота, идентификатор чата, данные для отчета, язык и имя мехирона в качестве параметров. Функция формирует пути для сохранения отчетов, создает HTML-отчет с помощью метода `create_html_report_async`, а затем, если необходимо, создает PDF и DOCX отчеты на основе сгенерированного HTML-контента.

**Параметры**:

- `bot` (telebot.TeleBot): Экземпляр Telegram-бота для отправки отчетов.
- `chat_id` (int): Идентификатор чата, в который нужно отправить отчет.
- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчета.
- `mexiron_name` (str): Имя мехирона.

**Возвращает**:

- `tuple`: Не указано.

**Примеры**:

```python
await report_generator.create_reports_async(bot, chat_id, data, lang, mexiron_name)
```

### `service_apendix`

```python
def service_apendix(self, lang: str) -> dict:
    return {
        "product_id": "00000",
        "product_name": "Сервис" if lang == 'ru' else "שירות",
        "specification": Path(__root__ / 'src' / 'endpoints' / ENDPOINT / 'report_generator' / 'templates' / f'service_as_product_{lang}.html').read_text(encoding='UTF-8').replace('/n', '<br>'),
        "image_local_saved_path": random_image(self.storage_path / 'converted_images')
    }

    ...
```

**Описание**: Создает словарь с данными для сервисного приложения.

**Как работает функция**:
Функция `service_apendix` создает и возвращает словарь, содержащий данные для сервисного приложения. Этот словарь включает идентификатор продукта, его название (на русском или иврите в зависимости от языка отчета), спецификацию, прочитанную из HTML-шаблона, и путь к случайному изображению. Функция использует условный оператор для определения названия продукта в зависимости от языка и считывает содержимое HTML-файла, заменяя символы новой строки на теги `<br>`.

**Параметры**:

- `lang` (str): Язык отчета.

**Возвращает**:

- `dict`: Словарь с данными для сервисного приложения.

**Примеры**:

```python
service_data = report_generator.service_apendix(lang='ru')
```

### `create_html_report_async`

```python
async def create_html_report_async(self, data: dict, lang: str, html_path: Optional[str | Path]) -> str | None:
    """
    Генерирует HTML-контент на основе шаблона и данных.

    Args:
        lang (str): Язык отчёта.

    Returns:
        str: HTML-контент.
    """
    self.html_path = html_path if html_path and isinstance(html_path, str) else Path(html_path) or self.html_path

    try:
        service_apendix = self.service_apendix(lang)
        data['products'].append(service_apendix)
        template: str = 'template_table_he.html' if lang == 'he' else 'template_table_ru.html'
        template_path: str = str(gs.path.endpoints / ENDPOINT / 'report_generator' / 'templates' / template)
        # template = self.env.get_template(self.template_path)
        template_string = Path(template_path).read_text(encoding='UTF-8')
        template = self.env.from_string(template_string)
        self.html_content: str = template.render(**data)

        try:
            Path(self.html_path).write_text(data=self.html_content, encoding='UTF-8')
        except Exception as ex:
            logger.error(f"Не удалось сохранить файл")
            return self.html_content

        logger.info(f"Файл HTML удачно сохранен в {html_path}")
        return self.html_content

    except Exception as ex:
        logger.error(f"Не удалось сгенерирпвать HTML файл {html_path}", ex)
        return
```

**Описание**: Генерирует HTML-контент на основе шаблона и данных.

**Как работает функция**:
Функция `create_html_report_async` является асинхронной и отвечает за генерацию HTML-контента на основе предоставленных данных и шаблона Jinja2. Она принимает данные, язык отчета и путь для сохранения HTML-файла в качестве параметров. Функция определяет, какой шаблон использовать в зависимости от языка отчета, загружает шаблон из файла, добавляет сервисные данные в данные отчета, применяет шаблон к данным и сохраняет полученный HTML-контент в файл. В случае возникновения ошибок, функция логирует их и возвращает `None`.

**Параметры**:

- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчета.
- `html_path` (Optional[str  |  Path]): Путь для сохранения HTML-файла.

**Возвращает**:

- `str  |  None`: HTML-контент или `None` в случае ошибки.

**Вызывает исключения**:

- `Exception`: Если не удается сгенерировать HTML-файл.

**Примеры**:

```python
html_content = await report_generator.create_html_report_async(data, lang='ru', html_path='report.html')
```

### `create_pdf_report_async`

```python
async def create_pdf_report_async(self, data: dict, lang: str, pdf_path: str | Path) -> bool:
    """
    Полный цикл генерации отчёта.

    Args:
        lang (str): Язык отчёта.
    """
    pdf_path = pdf_path if pdf_path and isinstance(pdf_path, (str, Path)) else self.pdf_path

    self.html_content = data if data else self.html_content

    from src.utils.pdf import PDFUtils
    pdf = PDFUtils()

    if not pdf.save_pdf_pdfkit(self.html_content, pdf_path):
        logger.error(f"Не удалось сохранить PDF файл {pdf_path}")
        if self.bot:
            self.bot.send_message(self.chat_id, f"Не удалось сохранить файл {pdf_path}")
        ...
        return False

    if self.bot:
        try:
            with open(pdf_path, 'rb') as f:
                self.bot.send_document(self.chat_id, f)
                return True
        except Exception as ex:
            self.bot.send_message(self.chat_id, f"Не удалось отправить файл {pdf_path} по причине: {ex}")
            return False
```

**Описание**: Асинхронно генерирует PDF-отчет на основе HTML-контента.

**Как работает функция**:
Функция `create_pdf_report_async` является асинхронной и отвечает за генерацию PDF-отчета на основе предоставленного HTML-контента. Она принимает HTML-контент, язык отчета и путь для сохранения PDF-файла в качестве параметров. Функция использует класс `PDFUtils` для преобразования HTML в PDF и сохранения его в файл. Если указан Telegram-бот, функция пытается отправить PDF-файл в заданный чат. В случае возникновения ошибок, функция логирует их и отправляет сообщение об ошибке в чат (если бот указан).

**Параметры**:

- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчета.
- `pdf_path` (str  |  Path): Путь для сохранения PDF-файла.

**Возвращает**:

- `bool`: `True`, если PDF-файл успешно сгенерирован и отправлен (если бот указан), `False` в случае ошибки.

**Вызывает исключения**:

- `Exception`: Если не удается отправить файл через Telegram-бота.

**Примеры**:

```python
success = await report_generator.create_pdf_report_async(html_content, lang='ru', pdf_path='report.pdf')
```

### `create_docx_report_async`

```python
async def create_docx_report_async(self, html_path: str | Path, docx_path: str | Path) -> bool:
    """Создаю docx файл """

    if not html_to_docx(self.html_path, docx_path):
        logger.error(f"Не скопмилировался DOCX.")
        return False
    return True
```

**Описание**: Создает docx файл

**Как работает функция**:
Функция `create_docx_report_async` создает DOCX-файл на основе предоставленного HTML-контента. Она принимает пути к HTML-файлу и DOCX-файлу в качестве параметров. Функция использует функцию `html_to_docx` для преобразования HTML в DOCX. В случае ошибки преобразования, функция логирует ее и возвращает `False`.

**Параметры**:

- `html_path` (str | Path): Путь к HTML-файлу.
- `docx_path` (str | Path): Путь к DOCX-файлу.

**Возвращает**:

- `bool`: `True`, если DOCX-файл успешно сгенерирован, `False` в случае ошибки.

**Примеры**:

```python
success = await report_generator.create_docx_report_async(html_path='report.html', docx_path='report.docx')
```

### `main`

```python
def main(maxiron_name: str, lang: str) -> bool:
    external_storage: Path = gs.path.external_storage / ENDPOINT / 'mexironim' / maxiron_name
    data: dict = j_loads(external_storage / f'{maxiron_name}_{lang}.json')
    html_path: Path = external_storage / f'{maxiron_name}_{lang}.html'
    pdf_path: Path = external_storage / f'{maxiron_name}_{lang}.pdf'
    docx_path: Path = external_storage / f'{maxiron_name}_{lang}.docx'
    if_need_html: bool = True
    if_need_pdf: bool = True
    if_need_docx: bool = True
    r = ReportGenerator(if_need_html, if_need_pdf, if_need_docx, html_path, pdf_path, docx_path)

    asyncio.run(r.create_reports_async(data,
                                        maxiron_name,
                                        lang,
                                        html_path,
                                        pdf_path,
                                        docx_path,))
```

**Описание**: Главная функция для запуска генерации отчетов.

**Как работает функция**:
Функция `main` является точкой входа для запуска процесса генерации отчетов. Она принимает имя мехирона и язык в качестве параметров. Функция формирует пути к данным, HTML, PDF и DOCX файлам, создает экземпляр класса `ReportGenerator` и запускает асинхронный процесс создания отчетов с использованием `asyncio.run`.

**Параметры**:

- `maxiron_name` (str): Имя мехирона.
- `lang` (str): Язык отчета.

**Возвращает**:

- `bool`: Успешно или нет

**Примеры**:

```python
main(maxiron_name='250127221657987', lang='ru')