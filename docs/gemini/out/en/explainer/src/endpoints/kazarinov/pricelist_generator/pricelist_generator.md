# Code Explanation for pricelist_generator.py

## <input code>

```python
## \file hypotez/src/endpoints/kazarinov/react/pricelist_generator.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov.react 
	:platform: Windows, Unix
	:synopsis: Генератор HTML и PDF для мехиронов Казаринова

Описание работы:
- Конструктор `__init__`: Принимает шаблон, базовый путь, метку времени и язык.
- Метод `load_data`: Загружает данные из JSON-файла.
- Метод `generate_html`: Генерирует HTML с использованием Jinja2.
- Метод `save_html`: Сохраняет HTML в файл.
- Метод `generate_pdf`: Преобразует HTML в PDF.
- Метод `create_report`: Запускает полный цикл генерации отчёта.

"""
MODE = 'dev'

#https://dev.to/kboskin/building-web-applications-with-react-and-python-2d8c


import header
from dataclasses import dataclass, field
from src import gs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import pdfkit
from src.utils.jjson import j_loads
from src.utils.file import read_text_file, save_text_file    
from src.utils.pdf import PDFUtils
from src.utils.convertors.html import html2pdf
from src.utils.printer import pprint
from src.logger import logger

# config = pdfkit.configuration(wkhtmltopdf= str( gs.path.bin / 'wkhtmltopdf' / 'files' / 'bin' / 'wkhtmltopdf.exe' ) )


@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """

    template_path: str  = field(default_factory=lambda: str(gs.path.endpoints / 'kazarinov' / 'react' / 'templates' / 'template.html'))

    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))

    def generate_html(self, data:dict ) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.

        Args:
            lang (str): Язык отчёта.

        Returns:
            str: HTML-контент.
        """
        #template = self.env.get_template(self.template_path)
        template_string = Path(self.template_path).read_text(encoding = 'UTF-8')
        template = self.env.from_string(template_string)
        return template.render(**data)


    def create_report(self, data: dict, html_file:str| Path, pdf_file:str |Path) -> None:
        """
        Полный цикл генерации отчёта.

        Args:
            lang (str): Язык отчёта.
        """
        html_content = self.generate_html(data)
        save_text_file(html_content, html_file)
        pdf = PDFUtils()

        if not pdf.save_pdf_pdfkit(html_content,pdf_file):
            logger.error(f"Не скопмилировался PDF")
            ...
        ...


def main(mexiron:str,lang:str) ->bool:
    base_path:Path =  gs.path.external_storage / 'kazarinov' / 'mexironim' / mexiron
    data:dict = j_loads(base_path / 'ru.json')
    html_file:Path =  base_path / f'{mexiron}_{lang}.html'
    pdf_file:Path = base_path / f'{mexiron}_{lang}.pdf'
    r = ReportGenerator()
    r.create_report(data, html_file, pdf_file)

if __name__ == "__main__":
    mexiron:str = '24_12_01_03_18_24_269'
    lang:str = 'ru'
    main(mexiron,lang)

```

## <algorithm>

**Step 1:**
*   **Input:**  `mexiron` (string) and `lang` (string).
*   **Action:**  Constructs paths for data, html and pdf files using `gs.path`.
*   **Example:**  `mexiron` = "24_12_01_03_18_24_269", `lang` = "ru".  Base path might be `/external_storage/kazarinov/mexironim/24_12_01_03_18_24_269`.

**Step 2:**
*   **Input:** Path to the `ru.json` file.
*   **Action:** Loads data from the JSON file using `j_loads`.
*   **Example:** Reads data from `/external_storage/kazarinov/mexironim/24_12_01_03_18_24_269/ru.json` into the `data` dictionary.

**Step 3:**
*   **Input:**  `data` (dictionary), `html_file` (Path), `pdf_file` (Path).
*   **Action:**  Creates an instance of `ReportGenerator`. Calls `create_report` method on the instance.
*   **Example:** Calls `r.create_report(data, html_file, pdf_file)` .

**Step 4:**
*   **Input:** `data` (dictionary).
*   **Action:** Calls `generate_html` to create HTML content.
*   **Example:** Using the data from `ru.json`, generates the HTML code.

**Step 5:**
*   **Input:** HTML content, `html_file` (Path).
*   **Action:** Saves the HTML content to the `html_file`.
*   **Example:** Saves generated HTML to `/external_storage/kazarinov/mexironim/24_12_01_03_18_24_269/24_12_01_03_18_24_269_ru.html`.

**Step 6:**
*   **Input:** HTML content, `pdf_file` (Path).
*   **Action:**  Converts HTML to PDF using `save_pdf_pdfkit` from `PDFUtils`.
*   **Example:** Converts the generated HTML to a PDF and saves it to `/external_storage/kazarinov/mexironim/24_12_01_03_18_24_269/24_12_01_03_18_24_269_ru.pdf`.

## <mermaid>

```mermaid
graph LR
    A[main(mexiron, lang)] --> B{Get data path};
    B --> C[Load data (ru.json)];
    C --> D[ReportGenerator()];
    D --> E{Create report(data, html_file, pdf_file)};
    E --> F[generate_html(data)];
    F --> G[Save to html_file];
    E --> H[save_pdf_pdfkit(html_content,pdf_file)];
    H --> I[Check PDF Conversion];
    I -- Success --> J[End];
    I -- Failure --> K[Error Logging];
```

**Dependencies Analysis:**

*   `header`: Likely a custom module or a specific configuration file.  It's not directly used but possibly influences paths or other setup aspects.
*   `gs`: Appears to be a custom package or module used for accessing global settings.  It's essential for building file paths.
*   `json`, `pathlib`: Standard Python modules for JSON handling and file path management.
*   `jinja2`, `pdfkit`: `jinja2` is for templating HTML and `pdfkit` for converting HTML to PDF.
*   `src.utils.jjson`, `src.utils.file`, `src.utils.pdf`, `src.utils.convertors.html`, `src.utils.printer`, `src.logger`: These modules are from the `src` project; they likely contain utilities for various tasks.  Importantly, `src.logger` is for logging and error handling.



## <explanation>

**Imports:**

*   `header`:  The purpose is unclear without more context; it probably handles initialization or configuration.
*   `gs`: This likely represents a "global settings" package for managing paths, configurations, or other project-wide data.
*   `json`, `pathlib`, `jinja2`, `pdfkit`: Standard Python libraries for handling JSON data, paths, templating with Jinja2, and generating PDFs.
*   `src.*`: Modules in the `src` directory:
    *   `src.utils.jjson`: For loading JSON files.
    *   `src.utils.file`: For file reading and saving.
    *   `src.utils.pdf`: For PDF creation.
    *   `src.utils.convertors.html`: Likely for HTML to PDF conversion utilities.
    *   `src.utils.printer`: For pretty printing output.
    *   `src.logger`: For logging errors or informational messages during PDF creation.



**Classes:**

*   `ReportGenerator`: This class encapsulates the logic for generating reports.
    *   `template_path`: Stores the path to the HTML template.
    *   `env`: A Jinja2 environment, configured for loading templates.
    *   `generate_html`: Renders the HTML template with given data.
    *   `create_report`: The core function that orcheStartes the generation of HTML and PDF reports. This method handles file saving and error checking.

**Functions:**

*   `main`: This function orcheStartes the entire process:
    *   Gets the paths for input files.
    *   Loads the JSON data.
    *   Generates and saves the HTML and PDF reports using `ReportGenerator`.


**Variables:**

*   `MODE`: A global string representing the current mode (e.g., "dev", "prod").
*   `mexiron`, `lang`:  Input parameters determining the specific report and its language.
*   `base_path`, `html_file`, `pdf_file`: Paths to files used in the report generation process.


**Potential Errors/Improvements:**

*   The code lacks error handling for cases where the JSON file is invalid or doesn't exist. `j_loads` should have a `try...except` block to handle potential `json.JSONDecodeError`.
*   The `if not pdf.save_pdf_pdfkit(...)` block only logs an error, but does not prevent further execution.  A more robust solution should also propagate the error upstream and potentially halt the process or retry.
*   The `...` placeholders could be improved to provide more explicit error handling or appropriate actions in case of failure.
*   The `@dataclass` usage in `ReportGenerator` could be improved. The default value for `template_path` using a lambda function within `field` isn't strictly needed in many cases, there are other ways to initialize data members.

**Relationships with Other Parts of the Project:**

The code relies heavily on other modules in the `src` package for various functionalities, including file handling, template rendering, PDF creation, and logging.  The `gs` module is crucial for providing project-wide settings and paths.   This demonStartes a modular design structure that facilitates code organization and reusability.