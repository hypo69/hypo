# Модуль исполнения сценария создания мехирона для Сергея Казаринова

## Обзор

Модуль предназначен для извлечения, разбора и обработки данных о товарах от поставщиков с целью их последующей публикации в Prestashop. Он включает в себя функциональность для подготовки данных, обработки с использованием AI и интеграции с Prestashop.

## Подробней

Этот модуль является частью проекта `hypotez` и выполняет важную роль в автоматизации процесса добавления товаров в интернет-магазин Prestashop. Он позволяет извлекать информацию о товарах из различных источников, включая веб-сайты поставщиков и JSON-файлы, обрабатывать эту информацию с помощью AI для улучшения качества данных и, наконец, публиковать товары в Prestashop.

## Классы

### `SupplierToPrestashopProvider`

**Описание**: Класс `SupplierToPrestashopProvider` предназначен для обработки данных о товарах, полученных от поставщиков, их разбора и сохранения. Данные могут быть получены как с веб-сайтов, так и из JSON файлов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `SupplierToPrestashopProvider`.
- `initialise_ai_model`: Инициализирует модель Gemini для обработки данных.
- `run_scenario`: Запускает основной сценарий: парсит товары, обрабатывает их с помощью AI и сохраняет данные.
- `save_product_data`: Сохраняет данные об отдельном товаре в файл.
- `process_ai`: Обрабатывает список товаров с использованием AI модели.
- `read_data_from_json`: Загружает JSON файлы и фотографии, полученные через телеграм.
- `save_in_prestashop`: Сохраняет товары в Prestashop.
- `post_facebook`: Исполняет сценарий рекламного модуля `facebook`.
- `create_report`: Отправляет задачу на создание отчета о мехироне в форматах `html` и `pdf`.

**Параметры**:
- `driver` (Driver): Экземпляр Selenium WebDriver.
- `export_path` (Path): Путь для экспорта данных.
- `mexiron_name` (str): Название мехирона.
- `price` (float): Цена товара.
- `timestamp` (str): Временная метка.
- `products_list` (list): Список обработанных данных о товарах.
- `model` (GoogleGenerativeAI): Экземпляр AI модели.
- `config` (SimpleNamespace): Конфигурация.
- `local_images_path` (Path): Путь к локальным изображениям товаров.
- `lang` (str): Язык.
- `gemini_api` (str): API ключ Gemini.
- `presta_api` (str): API ключ Prestashop.
- `presta_url` (str): URL Prestashop.

**Примеры**:

```python
from src.endpoints.emil.scenarios.from_supplier_to_prestashop import SupplierToPrestashopProvider
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox

# Инициализация класса
driver = Driver(Firefox)
provider = SupplierToPrestashopProvider(lang='ru', gemini_api='gemini_api_key', presta_api='presta_api_key', presta_url='https://your-prestashop.com', driver=driver)

# Запуск сценария
async def run():
    await provider.run_scenario(urls=['https://example.com/product1', 'https://example.com/product2'], price='100', mexiron_name='Мехирон 1')

import asyncio
asyncio.run(run())
```

## Функции

### `main`

```python
async def main(suppier_to_presta):
    """На данный момент функция читает JSON со списком фотографий , которые были получены от Эмиля"""
    ...
```

**Описание**: Функция `main` читает JSON файл со списком фотографий, полученных от Эмиля, и сохраняет товары в Prestashop.

**Параметры**:
- `suppier_to_presta` (SupplierToPrestashopProvider): Экземпляр класса `SupplierToPrestashopProvider`.

**Примеры**:

```python
import asyncio
from src.endpoints.emil.scenarios.from_supplier_to_prestashop import SupplierToPrestashopProvider

async def main():
    lang = 'he'
    # Здесь должна быть инициализация suppier_to_presta, но она отсутствует в предоставленном коде
    suppier_to_presta = SupplierToPrestashopProvider(lang=lang, gemini_api='gemini_api_key', presta_api='presta_api_key', presta_url='https://your-prestashop.com')
    # await suppier_to_presta.save_in_prestashop(products_list) # products_list отсутствует в данном контексте

if __name__ == '__main__':
    asyncio.run(main())
```