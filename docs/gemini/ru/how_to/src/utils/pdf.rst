Как использовать модуль преобразования HTML в PDF
==========================================================================================

Описание
-------------------------
Этот модуль предоставляет функции для преобразования HTML-контента или файлов в PDF-документы. Он использует библиотеки `pdfkit` и `fpdf`.  Модуль находит корневой каталог проекта, а затем ищет исполняемый файл wkhtmltopdf в подкаталоге 'bin/wkhtmltopdf/files/bin'.  Он также предоставляет альтернативный метод сохранения текста в PDF с использованием библиотеки `FPDF`.

Шаги выполнения
-------------------------
1. **Установка необходимых библиотек:**  Убедитесь, что в вашем окружении установлены библиотеки `pdfkit`, `reportlab`, `fpdf` и `requests` (если используется в `pdfkit`).  Можно установить их с помощью pip:
   ```bash
   pip install pdfkit reportlab fpdf requests
   ```
2. **Настройка пути к wkhtmltopdf:** Модуль ищет `wkhtmltopdf.exe` в подкаталоге `bin/wkhtmltopdf/files/bin`  корневого каталога проекта.  Если файл не найден, будет выброшено исключение `FileNotFoundError`.  Не забудьте установить `wkhtmltopdf` на вашем компьютере.
3. **Использование `save_pdf` для преобразования HTML-контента или файла:**
   - Для преобразования HTML-контента в строковом формате:
     ```python
     from hypotez.src.utils.pdf import PDFUtils
     html_content = "<html><body><h1>Мой заголовок</h1></body></html>"
     pdf_file = "output.pdf"
     success = PDFUtils.save_pdf(html_content, pdf_file)
     if success:
         print(f"PDF успешно сохранен в {pdf_file}")
     ```
   - Для преобразования HTML-файла:
     ```python
     from hypotez.src.utils.pdf import PDFUtils
     html_file = Path("input.html")
     pdf_file = "output.pdf"
     success = PDFUtils.save_pdf(html_file, pdf_file)
     if success:
         print(f"PDF успешно сохранен в {pdf_file}")
     ```
4. **Использование `save_pdf_v2` для сохранения текста в PDF:**
   -  Этот метод использует библиотеку `fpdf` для сохранения текста в PDF-файл.
     ```python
     from hypotez.src.utils.pdf import PDFUtils
     text_to_save = "Этот текст будет сохранен в PDF."
     pdf_file = "output_v2.pdf"
     success = PDFUtils.save_pdf_v2(text_to_save, pdf_file)
     if success:
         print(f"PDF отчет успешно сохранен в {pdf_file}")
     ```


Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.utils.pdf import PDFUtils
    from pathlib import Path
    
    # Пример использования для преобразования HTML-файла
    html_file = Path("input.html")
    pdf_file = "output.pdf"
    
    if PDFUtils.save_pdf(html_file, pdf_file):
        print("PDF успешно сохранен.")
    else:
        print("Ошибка при сохранении PDF.")


    # Пример использования для сохранения текста в PDF
    text_to_save = "Пример текста для сохранения в PDF формате v2."
    pdf_file_v2 = "output_v2.pdf"
    if PDFUtils.save_pdf_v2(text_to_save, pdf_file_v2):
        print("PDF отчет успешно сохранен.")
    else:
        print("Ошибка при сохранении PDF.")