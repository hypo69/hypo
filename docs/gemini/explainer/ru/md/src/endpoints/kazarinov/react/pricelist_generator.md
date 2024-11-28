# pricelist_generator.py - Генератор отчетов в HTML и PDF

```markdown
## Файл `hypotez/src/endpoints/kazarinov/react/pricelist_generator.py`

Этот файл содержит класс `ReportGenerator`, предназначенный для генерации HTML и PDF отчетов на основе данных из JSON-файла. Отчеты генерируются на основе шаблона, заданного в `template_path`.

### Класс `ReportGenerator`

```python
@dataclass
class ReportGenerator:
    """
    Класс для генерации HTML- и PDF-отчётов на основе данных из JSON.
    """
    template_path: str = field(default_factory=lambda: str(gs.path.src / 'suppliers' / 'kazarinov' / 'react' / 'templates' / 'template.html'))
    env: Environment = field(default_factory=lambda: Environment(loader=FileSystemLoader('.')))
```

*   **`template_path`:** Путь к шаблону HTML-отчета. По умолчанию берется из `gs.path.src/suppliers/kazarinov/react/templates/template.html`.
*   **`env`:** Объект `Environment` из библиотеки Jinja2, используемый для обработки шаблона.

### Метод `generate_html`

```python
    def generate_html(self, data: dict) -> str:
        """
        Генерирует HTML-контент на основе шаблона и данных.
        
        Args:
            data (dict): Данные для заполнения шаблона.

        Returns:
            str: HTML-контент.
        """
        template_string = read_text_file(self.template_path)
        template = self.env.from_string(template_string)
        return template.render(**data)
```

Этот метод принимает данные (`data`) и использует Jinja2 для рендеринга шаблона `template_path`, подставляя значения из `data`.  **Важно:**  Используется `read_text_file` для чтения шаблона, что предпочтительнее, чем `get_template`, так как позволяет использовать шаблоны в строковом формате, а не из файла.

### Метод `create_report`

```python
    def create_report(self, data: dict, html_file: str | Path, pdf_file: str | Path) -> None:
        """
        Полный цикл генерации отчёта.

        Args:
            data (dict): Данные для отчета.
            html_file (str | Path): Путь к файлу для сохранения HTML.
            pdf_file (str | Path): Путь к файлу для сохранения PDF.
        """
        html_content = self.generate_html(data)
        save_text_file(html_content, html_file)
        html2pdf(html_content, pdf_file)
```

Этот метод вызывает `generate_html`, сохраняет результат в `html_file` и конвертирует его в PDF, сохраняя в `pdf_file`.  В текущей реализации используется функция `html2pdf`. Важно, что отсутствует обработка ошибок.


### Основной блок (`if __name__ == "__main__":`)

```python
if __name__ == "__main__":
    base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326'
    data: dict = j_loads(base_path / '202410262326_ru.json')
    html_file: Path = base_path / '202410262326_ru.html'
    pdf_file: Path = base_path / '202410262326_ru.pdf'
    r = ReportGenerator()
    r.create_report(data, html_file, pdf_file)
```

Этот блок кода демонстрирует использование класса `ReportGenerator` для создания отчета. Загружает данные из JSON, генерирует HTML и PDF отчеты в указанные файлы.


**Выводы:**

Код хорошо структурирован, но для улучшения необходимо добавить обработку ошибок (например, исключения при чтении файлов, отсутствии библиотек).  Также стоит более подробно документировать используемые библиотеки и функции. Добавьте логирование ошибок.
```