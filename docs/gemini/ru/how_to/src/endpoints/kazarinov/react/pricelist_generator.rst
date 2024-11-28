Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код реализует класс `ReportGenerator` для генерации отчетов в HTML и PDF форматах.  Класс принимает данные в формате JSON, шаблон HTML-документа и пути к файлам для сохранения HTML и PDF.  Он использует Jinja2 для рендеринга шаблона с данными, а `pdfkit` для преобразования HTML в PDF.  Код также содержит методы для загрузки данных, генерации HTML, сохранения HTML-файла и генерации PDF-файла.  Важная часть - корректная настройка пути к `wkhtmltopdf` для успешного преобразования.

Шаги выполнения
-------------------------
1. **Инициализация класса `ReportGenerator`**: Создается экземпляр класса `ReportGenerator`, который принимает путь к шаблону HTML.
2. **Загрузка данных**:  Метод `create_report` принимает данные в формате словаря (dict) и пути к файлам для сохранения HTML и PDF.
3. **Генерация HTML**: Метод `generate_html` рендерит HTML-шаблон с использованием данных, переданных в `create_report`.  Он использует Jinja2 для подстановки данных в шаблон.
4. **Сохранение HTML**: Метод `create_report` сохраняет сгенерированный HTML-код в указанный файл.
5. **Генерация PDF**: Метод `create_report` преобразует HTML-код в PDF-файл используя `html2pdf`.
6. **Сохранение PDF**:  Метод `create_report` сохраняет сгенерированный PDF-файл в указанный файл.


Пример использования
-------------------------
.. code-block:: python

    import json
    from pathlib import Path
    from hypotez.src.endpoints.kazarinov.react.pricelist_generator import ReportGenerator  # Импорт класса

    # Пути к файлам
    base_path = Path("./data/kazarinov/mexironim/202410262326")
    data_file = base_path / "202410262326_ru.json"
    html_file = base_path / "202410262326_ru.html"
    pdf_file = base_path / "202410262326_ru.pdf"

    try:
        # Загрузка данных
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Создание экземпляра класса ReportGenerator
        generator = ReportGenerator()

        # Генерация отчета
        generator.create_report(data, html_file, pdf_file)

        print(f"Отчет успешно сгенерирован в {html_file} и {pdf_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {data_file} не найден.")
    except json.JSONDecodeError:
        print(f"Ошибка: Некорректный формат данных в файле {data_file}.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")