# Модуль для проверки генерации прайслиста

## Обзор

Модуль предназначен для проверки функциональности генерации прайс-листа. Он использует класс `ReportGenerator` для создания отчетов на разных языках (в данном случае, иврит и русский) и сохранения их в форматах HTML и PDF.

## Подробнее

Данный модуль выполняет проверку генерации прайс-листа с использованием класса `ReportGenerator`. Он создает отчеты на двух языках: иврите (`he`) и русском (`ru`), сохраняя их в форматах HTML и PDF. Для создания отчетов используются данные, полученные из словарей `response_he_dict` и `response_ru_dict`, которые предположительно содержат информацию, необходимую для формирования отчетов на соответствующих языках. Пути к файлам для сохранения отчетов определены с использованием библиотеки `pathlib`.

## Переменные

### `report_generator`

- **Описание**: Экземпляр класса `ReportGenerator`, используемый для генерации отчетов.
- **Тип**: `ReportGenerator`

### `html_file_he`

- **Описание**: Объект `Path`, представляющий путь к HTML-файлу для отчета на иврите.
- **Тип**: `Path`

### `pdf_file_he`

- **Описание**: Объект `Path`, представляющий путь к PDF-файлу для отчета на иврите.
- **Тип**: `Path`

### `html_file_ru`

- **Описание**: Объект `Path`, представляющий путь к HTML-файлу для отчета на русском языке.
- **Тип**: `Path`

### `pdf_file_ru`

- **Описание**: Объект `Path`, представляющий путь к PDF-файлу для отчета на русском языке.
- **Тип**: `Path`

## Функции

### `create_report`

```python
def create_report(data: dict, lang: str, html_file: Path, pdf_file: Path) -> None:
    """
    Создает отчет на указанном языке и сохраняет его в форматах HTML и PDF.

    Args:
        data (dict): Данные для формирования отчета.
        lang (str): Язык отчета ('he' для иврита, 'ru' для русского).
        html_file (Path): Путь для сохранения HTML-файла.
        pdf_file (Path): Путь для сохранения PDF-файла.

    Returns:
        None

    Raises:
        Exception: Если возникает ошибка при создании отчета.
    """
    ...
```

**Назначение**: Создает отчет на указанном языке и сохраняет его в форматах HTML и PDF.

**Параметры**:

- `data` (dict): Данные для формирования отчета.
- `lang` (str): Язык отчета ('he' для иврита, 'ru' для русского).
- `html_file` (Path): Путь для сохранения HTML-файла.
- `pdf_file` (Path): Путь для сохранения PDF-файла.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `Exception`: Если возникает ошибка при создании отчета.

**Как работает функция**:

1. Функция `create_report` вызывается дважды: один раз для иврита и один раз для русского языка.
2. Для каждого языка передаются соответствующие данные из словарей `response_he_dict` и `response_ru_dict`, а также пути для сохранения HTML и PDF файлов.
3.  Внутри  `create_report` происходит вся магия формирования отчета на нужном языке, с использованием переданных данных, и последующее сохранение в двух форматах: HTML и PDF.

```
      Начало
         ↓
      Передача данных, языка и путей к файлам
         ↓
      Формирование отчета на заданном языке (he или ru) с использованием данных
         ↓
      Сохранение отчета в формате HTML по указанному пути
         ↓
      Сохранение отчета в формате PDF по указанному пути
         ↓
      Конец
```

**Примеры**:

```python
report_generator.create_report(response_he_dict['he'], 'he', html_file_he, pdf_file_he)
report_generator.create_report(response_ru_dict['ru'], 'ru', html_file_ru, pdf_file_ru)