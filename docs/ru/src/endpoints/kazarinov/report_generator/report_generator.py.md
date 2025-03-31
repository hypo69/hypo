# Модуль `report_generator.py`

## Обзор

Модуль `report_generator.py` предназначен для генерации отчетов в форматах HTML и PDF на основе данных JSON для мехиронов Казаринова. Он включает в себя класс `ReportGenerator`, который выполняет загрузку данных, генерацию HTML с использованием Jinja2, преобразование HTML в PDF и сохранение отчетов в файлы.

## Подробнее

Этот модуль является частью системы отчетности и предоставляет функциональность для автоматического создания отчетов на основе данных, хранящихся в формате JSON. Он использует шаблоны Jinja2 для генерации HTML и библиотеку `pdfkit` для преобразования HTML в PDF.

## Классы

### `ReportGenerator`

**Описание**:
Класс `ReportGenerator` предназначен для генерации отчетов в форматах HTML и PDF на основе данных JSON.

**Как работает класс**:
1.  **Инициализация**: При инициализации класса определяются основные параметры, такие как необходимость генерации PDF и DOCX отчетов.
2.  **Создание отчетов**: С помощью метода `create_reports_async` происходит создание HTML, PDF и DOCX отчетов.
3.  **Генерация HTML**: Метод `create_html_report_async` генерирует HTML-контент на основе шаблона Jinja2 и данных.
4.  **Генерация PDF**: Метод `create_pdf_report_async` преобразует сгенерированный HTML в PDF формат.
5.  **Генерация DOCX**: Метод `create_docx_report_async` преобразует сгенерированный HTML в DOCX формат.

**Переменные класса**:
-   `if_need_html` (bool): Флаг, указывающий на необходимость генерации HTML-отчета.
-   `if_need_pdf` (bool): Флаг, указывающий на необходимость генерации PDF-отчета.
-   `if_need_docx` (bool): Флаг, указывающий на необходимость генерации DOCX-отчета.
-   `storage_path` (Path): Путь к директории, где хранятся сгенерированные отчеты. По умолчанию `gs.path.external_storage / ENDPOINT`.
-   `html_path` (Path | str): Путь к HTML-файлу.
-   `pdf_path` (Path | str): Путь к PDF-файлу.
-   `docs_path` (Path | str): Путь к DOCX-файлу.
-   `html_content` (str): Содержимое HTML-отчета.
-   `data` (dict): Данные для генерации отчета.
-   `lang` (str): Язык отчета.
-   `mexiron_name` (str): Имя мехирона.
-   `env` (Environment): Объект окружения Jinja2 для работы с шаблонами.

**Методы**:

#### `__init__`

```python
    def __init__(self, 
                 if_need_pdf:Optional[bool] = True, 
                 if_need_docx:Optional[bool] = True, 
            ):
        """Определение, какие форматы данных требуется вернуть"""
```

**Назначение**:
Инициализирует экземпляр класса `ReportGenerator`.

**Как работает функция**:
1.  Устанавливает значения флагов `if_need_pdf` и `if_need_docx`, определяющих, какие форматы отчетов необходимо генерировать.
2.  По умолчанию, если не указано иное, оба флага устанавливаются в `True`.

**Параметры**:

*   `if_need_pdf` (Optional[bool], optional): Флаг, определяющий необходимость генерации PDF-отчета. По умолчанию `True`.
*   `if_need_docx` (Optional[bool], optional): Флаг, определяющий необходимость генерации DOCX-отчета. По умолчанию `True`.

#### `create_reports_async`

```python
    async def create_reports_async(self,\
                             bot: telebot.TeleBot,\
                             chat_id: int,\
                             data:dict,\
                             lang:str,\
                             mexiron_name:str,\
                             ) -> tuple:
        """Create ALL types: HTML, PDF, DOCX"""
```

**Назначение**:
Создает отчеты во всех поддерживаемых форматах: HTML, PDF и DOCX.

**Как работает функция**:
1.  Устанавливает имя мехирона (`mexiron_name`) из переданных данных.
2.  Формирует пути для сохранения HTML, PDF и DOCX файлов в директории `storage_path / 'mexironim' / self.mexiron_name`.
3.  Создает HTML отчет, вызывая метод `create_html_report_async`. Если создание HTML отчета не удалось, возвращает `False`.
4.  Если требуется, создает PDF отчет, вызывая метод `create_pdf_report_async`.
5.  Если требуется, создает DOCX отчет, вызывая метод `create_docx_report_async`.

**Параметры**:

*   `bot` (telebot.TeleBot): Объект бота Telebot для отправки уведомлений и файлов.
*   `chat_id` (int): Идентификатор чата, куда отправлять отчеты.
*   `data` (dict): Данные для генерации отчета.
*   `lang` (str): Язык отчета.
*   `mexiron_name` (str): Имя мехирона.

**Возвращает**:

*   `tuple`: Возвращает кортеж с результатами создания отчетов в различных форматах.

#### `service_apendix`

```python
    def service_apendix(self, lang:str) -> dict:
        return  {
                "product_id":"00000",
                "product_name":"Сервис" if lang == \'ru\' else "שירות",
                "specification":Path(__root__ / \'src\' / \'endpoints\' / ENDPOINT / \'report_generator\' / \'templates\' / f\'service_as_product_{lang}.html\').read_text(encoding=\'UTF-8\').replace(\'/n\',\'<br>\'),
                "image_local_saved_path":random_image(self.storage_path / \'converted_images\' )
                }
```

**Назначение**:
Создает словарь с данными о сервисе для добавления в отчет.

**Как работает функция**:
1.  Определяет название продукта в зависимости от языка (`lang`). Если язык русский, название будет "Сервис", иначе "שירות".
2.  Считывает спецификацию продукта из HTML-файла, расположенного в директории шаблонов. Заменяет символы новой строки (`/n`) на теги `<br>`, чтобы корректно отображать спецификацию в HTML-отчете.
3.  Генерирует случайное изображение и сохраняет его путь.
4.  Возвращает словарь, содержащий идентификатор продукта, название продукта, спецификацию и путь к изображению.

**Параметры**:

*   `lang` (str): Язык отчета.

**Возвращает**:

*   `dict`: Словарь с данными о сервисе.

#### `create_html_report_async`

```python
    async def create_html_report_async(self, data:dict, lang:str, html_path:Optional[ str|Path] ) -> str | None:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
```

**Назначение**:
Генерирует HTML-контент на основе шаблона и данных.

**Как работает функция**:
1.  Устанавливает путь к HTML-файлу, используя переданный параметр `html_path`, если он указан, или значение по умолчанию `self.html_path`.
2.  Добавляет информацию о сервисе в данные (`data`), используя метод `self.service_apendix`.
3.  Выбирает шаблон в зависимости от языка (`lang`). Если язык иврит (`he`), используется шаблон `template_table_he.html`, иначе используется шаблон `template_table_ru.html`.
4.  Считывает содержимое шаблона из файла.
5.  Генерирует HTML-контент, используя шаблон Jinja2 и переданные данные.
6.  Сохраняет сгенерированный HTML-контент в файл.
7.  Логирует информацию об успешном сохранении файла.

**Параметры**:

*   `data` (dict): Данные для генерации отчета.
*   `lang` (str): Язык отчета.
*   `html_path` (Optional[str | Path], optional): Путь к HTML-файлу. По умолчанию `None`.

**Возвращает**:

*   `str | None`: HTML-контент или `None` в случае ошибки.

**Вызывает исключения**:

*   `Exception`: Если не удается сохранить файл или сгенерировать HTML-файл.

#### `create_pdf_report_async`

```python
    async def create_pdf_report_async(self, 
                                data: dict, 
                                lang:str, 
                                pdf_path:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
```

**Назначение**:
Генерирует PDF-отчет из HTML-контента.

**Как работает функция**:
1.  Устанавливает путь к PDF-файлу, используя переданный параметр `pdf_path`, если он указан, или значение по умолчанию `self.pdf_path`.
2.  Использует HTML-контент из параметра `data`, если он передан, или `self.html_content`.
3.  Использует утилиту `PDFUtils` для сохранения HTML-контента в PDF-файл.
4.  Если сохранение PDF-файла не удалось, логирует ошибку и отправляет сообщение об ошибке в чат, если объект бота (`self.bot`) доступен.
5.  Если объект бота доступен, пытается отправить PDF-файл в чат. В случае успеха возвращает `True`, иначе отправляет сообщение об ошибке в чат и возвращает `False`.

**Параметры**:

*   `data` (dict): Данные для генерации отчета.
*   `lang` (str): Язык отчета.
*   `pdf_path` (str | Path): Путь к PDF-файлу.

**Возвращает**:

*   `bool`: `True` в случае успешной генерации и отправки PDF-отчета, `False` в случае ошибки.

#### `create_docx_report_async`

```python
    async def create_docx_report_async(self, html_path:str|Path, docx_path:str|Path) -> bool :
        """Создаю docx файл """
```

**Назначение**:
Создает DOCX-файл из HTML-файла.

**Как работает функция**:
1.  Преобразует HTML-файл в DOCX-файл, используя функцию `html_to_docx`.
2.  Если преобразование не удалось, логирует ошибку и возвращает `False`.
3.  В случае успеха возвращает `True`.

**Параметры**:

*   `html_path` (str | Path): Путь к HTML-файлу.
*   `docx_path` (str | Path): Путь к DOCX-файлу.

**Возвращает**:

*   `bool`: `True` в случае успешного создания DOCX-файла, `False` в случае ошибки.

## Функции

### `main`

```python
def main(maxiron_name:str, lang:str) ->bool:
    
    external_storage: Path =  gs.path.external_storage / ENDPOINT / \'mexironim\' /  maxiron_name
    data: dict = j_loads(external_storage / f\'{maxiron_name}_{lang}.json\')
    html_path: Path =  external_storage / f\'{maxiron_name}_{lang}.html\' 
    pdf_path: Path = external_storage / f\'{maxiron_name}_{lang}.pdf\'
    docx_path: Path = external_storage / f\'{maxiron_name}_{lang}.docx\'
    if_need_html: bool = True
    if_need_pdf: bool = True
    if_need_docx: bool = True 
    r = ReportGenerator(if_need_html, if_need_pdf, if_need_docx, html_path, pdf_path, docx_path)

    asyncio.run( r.create_reports_async( data,\
                                    maxiron_name,\
                                    lang, \
                                    html_path, \
                                    pdf_path, \
                                    docx_path, )   
                )
```

**Назначение**:
Основная функция для запуска процесса генерации отчетов.

**Как работает функция**:

1.  Формирует путь к директории, где хранятся данные и сгенерированные файлы, на основе имени мехирона (`maxiron_name`).
2.  Загружает данные из JSON-файла.
3.  Формирует пути для HTML, PDF и DOCX файлов.
4.  Создает экземпляр класса `ReportGenerator`, передавая пути к файлам и флаги необходимости генерации отчетов в разных форматах.
5.  Запускает асинхронный процесс создания отчетов, вызывая метод `create_reports_async` класса `ReportGenerator`.

**Параметры**:

*   `maxiron_name` (str): Имя мехирона.
*   `lang` (str): Язык отчета.

**Возвращает**:

*   `bool`: Возвращает `True` в случае успешного завершения, `False` в случае ошибки.

```python
if __name__ == "__main__":
    maxiron_name = \'250127221657987\' # <- debug
    lang:str = \'ru\'
    
    main(maxiron_name, lang)
```

**Назначение**:
Запускает функцию `main` при выполнении скрипта как основной программы.

**Как работает функция**:
1.  Устанавливает имя мехирона и язык отчета.
2.  Вызывает функцию `main` с установленными параметрами.