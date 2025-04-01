# Модуль `report_generator`

## Обзор

Модуль `report_generator` предназначен для генерации отчётов в формате HTML, PDF и DOCX на основе данных, полученных в формате JSON. Он использует шаблоны Jinja2 для создания HTML-контента, который затем может быть преобразован в PDF и DOCX. Модуль предназначен для использования в проекте `hypotez` и интегрирован с системой логирования и утилитами для работы с файлами и изображениями. Расположен в директории `src/endpoints/kazarinov/report_generator`.

## Подробней

Основная задача модуля - автоматизировать процесс создания отчётов для мехиронов Казаринова. Он предоставляет класс `ReportGenerator`, который инкапсулирует всю логику генерации отчётов. Модуль использует шаблоны Jinja2 для создания HTML-контента, который затем конвертируется в PDF и DOCX. Это позволяет генерировать отчёты с динамическим содержимым на основе данных из JSON.

Взаимодействие с модулем происходит через класс `ReportGenerator`, который принимает параметры, определяющие необходимость генерации отчётов в различных форматах. Метод `create_reports_async` является точкой входа для запуска процесса генерации отчётов.

## Классы

### `ReportGenerator`

**Описание**: Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `ReportGenerator`.
- `create_reports_async`: Создаёт отчёты во всех требуемых форматах: HTML, PDF, DOCX.
- `service_apendix`: Формирует словарь с информацией о сервисе.
- `create_html_report_async`: Генерирует HTML-контент на основе шаблона и данных.
- `create_pdf_report_async`: Генерирует PDF-отчёт на основе HTML-контента.
- `create_docx_report_async`: Создаёт DOCX-файл на основе HTML-контента.

**Параметры**:
- `if_need_html` (bool): Флаг, указывающий на необходимость генерации HTML-отчёта.
- `if_need_pdf` (bool): Флаг, указывающий на необходимость генерации PDF-отчёта.
- `if_need_docx` (bool): Флаг, указывающий на необходимость генерации DOCX-отчёта.
- `storage_path` (Path): Путь к директории для сохранения отчётов.
- `html_path` (Path | str): Путь к HTML-файлу.
- `pdf_path` (Path | str): Путь к PDF-файлу.
- `docs_path` (Path | str): Путь к DOCX-файлу.
- `html_content` (str): HTML-контент отчёта.
- `data` (dict): Данные для генерации отчёта.
- `lang` (str): Язык отчёта.
- `mexiron_name` (str): Имя мехирона.
- `env` (Environment): Окружение Jinja2 для работы с шаблонами.

**Примеры**:

```python
    r = ReportGenerator(if_need_html=True, if_need_pdf=True, if_need_docx=True)
```

## Функции

### `main`

```python
def main(maxiron_name: str, lang: str) -> bool:
    """
    Args:
        maxiron_name (str): Имя мехирона.
        lang (str): Язык отчёта.

    Returns:
        bool: Возвращает `True` в случае успешного завершения, `False` в противном случае.
    """
```

**Описание**: Функция `main` является точкой входа для запуска процесса генерации отчётов.

**Параметры**:
- `maxiron_name` (str): Имя мехирона.
- `lang` (str): Язык отчёта.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного завершения, `False` в противном случае.

**Примеры**:

```python
    maxiron_name = '250127221657987' # <- debug
    lang: str = 'ru'
    main(maxiron_name, lang)
```
```python
    async def create_reports_async(self,
                             bot: telebot.TeleBot,
                             chat_id: int,
                             data:dict,
                             lang:str,
                             mexiron_name:str,
                             ) -> tuple:
        """Create ALL types: HTML, PDF, DOCX"""
```
```python
    async def create_html_report_async(self, data:dict, lang:str, html_path:Optional[ str|Path] ) -> str | None:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            data (dict): Данные для отчета.
            lang (str): Язык отчёта.
            html_path (Optional[str|Path]): Путь для сохранения HTML файла.

        Returns:
            str: HTML-контент.
        """
```
```python
    async def create_pdf_report_async(self, 
                                data: dict, 
                                lang:str, 
                                pdf_path:str |Path) -> bool:
        """
        Полный цикл генерации отчёта.

        Args:
            data (dict): Данные для отчета.
            lang (str): Язык отчёта.
            pdf_path (str | Path): Путь для сохранения PDF файла.
        Returns:
            bool: True в случае успешного создания, иначе False
        """
```
```python
    async def create_docx_report_async(self, html_path:str|Path, docx_path:str|Path) -> bool :
        """Создаю docx файл """
        """
        Создает docx файл из html.

        Args:
            html_path (str|Path): Путь к HTML файлу.
            docx_path (str|Path): Путь для сохранения DOCX файла.
        Returns:
            bool: True в случае успешного создания, иначе False
        """
```
```python
    def service_apendix(self, lang:str) -> dict:
        """
        Args:
            lang (str): Язык отчёта.

        Returns:
            dict: словарь с информацией о сервисе.
        """
```
```python
    def __init__(self, 
                 if_need_pdf:Optional[bool] = True, 
                 if_need_docx:Optional[bool] = True, 
            ):
        """Определение, какие форматы данных требуется вернуть"""
        """
        Определение, какие форматы данных требуется вернуть.

        Args:
            if_need_pdf (Optional[bool], optional): Флаг, указывающий на необходимость генерации PDF-отчёта. По умолчанию True.
            if_need_docx (Optional[bool], optional): Флаг, указывающий на необходимость генерации DOCX-отчёта. По умолчанию True.
        """
```
```python
class ReportGenerator():
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """