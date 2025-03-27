# Модуль: `from_supplier_to_prestashop.py`

## Обзор

Модуль предназначен для автоматизации процесса извлечения, обработки и публикации данных о товарах от поставщиков на платформе Prestashop. Он включает в себя функциональность для сбора данных с веб-сайтов поставщиков, их преобразования, использования AI для обработки контента и, наконец, добавления товаров в Prestashop.

## Подробней

Этот модуль является частью проекта `hypotez` и выполняет сценарий создания "мехирона" (специального предложения или товара) для конкретного пользователя (Сергея Казаринова). Он автоматизирует шаги, необходимые для получения информации о товаре от поставщика, обработки этой информации (включая использование AI для улучшения контента) и публикации товара на платформе электронной коммерции Prestashop. Расположение файла `/src/endpoints/emil/scenarios/from_supplier_to_prestashop.py` указывает, что этот модуль является частью endpoint'а `emil` и отвечает за выполнение определенных сценариев, связанных с поставщиками и интеграцией с Prestashop.

## Классы

### `SupplierToPrestashopProvider`

**Описание**: Класс предназначен для обработки данных о продуктах, получаемых от поставщиков, их преобразования и сохранения в Prestashop.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `SupplierToPrestashopProvider`.
- `initialise_ai_model`: Инициализирует AI модель Gemini для обработки данных о продуктах.
- `run_scenario`: Запускает основной сценарий, включающий парсинг данных о продуктах, их обработку с помощью AI и сохранение данных.
- `save_product_data`: Сохраняет данные об отдельном продукте в файл.
- `process_ai`: Обрабатывает список продуктов с использованием AI модели.
- `read_data_from_json`: Загружает JSON файлы с данными и изображениями продуктов.
- `save_in_prestashop`: Сохраняет товары в Prestashop.
- `post_facebook`: Исполняет сценарий рекламного модуля `facebook`.
- `create_report`: Создает отчет о мехироне в форматах `html` и `pdf`.

**Параметры**:
- `lang` (str): Язык, на котором предоставляется информация о продуктах.
- `gemini_api` (str): Ключ API для доступа к модели Gemini.
- `presta_api` (str): Ключ API для доступа к Prestashop.
- `presta_url` (str): URL адрес Prestashop.
- `driver` (Optional[Driver], optional): Экземпляр Selenium WebDriver. По умолчанию `None`.

**Примеры**:
```python
# Пример инициализации класса SupplierToPrestashopProvider
suppier_to_presta = SupplierToPrestashopProvider(
    lang='he',
    gemini_api='your_gemini_api_key',
    presta_api='your_presta_api_key',
    presta_url='https://your-prestashop-domain.com'
)
```

## Функции

### `main`

```python
async def main(suppier_to_presta):
    """На данный момент функция читает JSON со списком фотографий , которые были получены от Эмиля"""    
    lang = 'he'
    products_ns = j_loads_ns(gs.path.external_storage / ENDPOINT / 'out_250108230345305_he.json')

    suppier_to_presta = SupplierToPrestashopProvider(lang)
    products_list:list = [f for f in products_ns]
    await suppier_to_presta.save_in_prestashop(products_list)
```

**Описание**: Функция `main` выполняет основную логику чтения данных о продуктах из JSON, инициализации `SupplierToPrestashopProvider` и сохранения продуктов в Prestashop.

**Параметры**:
- `suppier_to_presta`: Параметр не используется, но ожидается экземпляр класса `SupplierToPrestashopProvider`.

**Примеры**:
```python
# Пример вызова функции main
asyncio.run(main())