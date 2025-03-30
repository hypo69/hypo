# Модуль warehouse

## Обзор

Модуль `warehouse` предназначен для работы с функциональностью управления складом в PrestaShop. Он расширяет возможности базового класса `PrestaShop` и предоставляет инструменты для взаимодействия с API PrestaShop, специфичными для управления складами.

## Подробней

Этот модуль является частью подсистемы `endpoints` проекта `hypotez` и предназначен для интеграции с платформой PrestaShop. Он обеспечивает взаимодействие с API PrestaShop для управления складскими операциями. Расположение файла в структуре проекта указывает на его роль как одной из конечных точек (endpoints) взаимодействия с PrestaShop.

## Классы

### `PrestaWarehouse`

**Описание**: Класс `PrestaWarehouse` наследуется от класса `PrestaShop` и предоставляет методы для работы с API PrestaShop, относящиеся к управлению складами.

**Методы**:
- (Описание методов будет добавлено после предоставления кода методов)

**Параметры**:
- (Описание параметров будет добавлено после предоставления кода параметров)

**Примеры**
```python
# Пример создания экземпляра класса PrestaWarehouse
# (Более подробные примеры будут добавлены после предоставления полного кода класса)
```
```python
from src.endpoints.prestashop.api import PrestaShop
from src.logger.logger import logger

class PrestaWarehouse(PrestaShop): 
    def __init__(self, url: str, api_key: str, debug: bool = False) -> None:
        """
        Инициализирует экземпляр класса PrestaWarehouse.

        Args:
            url (str): URL адрес магазина PrestaShop.
            api_key (str): Ключ API для доступа к PrestaShop.
            debug (bool, optional): Флаг для включения режима отладки. По умолчанию False.
        """
        super().__init__(url, api_key, debug)

    def get_warehouses(self) -> dict | None:
        """
        Получает список складов из PrestaShop.

        Returns:
            dict | None: Словарь с информацией о складах или None в случае ошибки.
        
        Raises:
            Exception: В случае ошибки при запросе к API.
        """
        try:
            return self.get('warehouses')
        except Exception as ex:
            logger.error(f'Ошибка при получении списка складов: {ex}', exc_info=True)
            return None

    def get_warehouse(self, warehouse_id: int) -> dict | None:
        """
        Получает информацию о конкретном складе по его ID.

        Args:
            warehouse_id (int): ID склада.

        Returns:
            dict | None: Словарь с информацией о складе или None в случае ошибки.

        Raises:
            Exception: В случае ошибки при запросе к API.
        """
        try:
            return self.get(f'warehouses/{warehouse_id}')
        except Exception as ex:
            logger.error(f'Ошибка при получении информации о складе с ID {warehouse_id}: {ex}', exc_info=True)
            return None

    def create_warehouse(self, data: dict) -> dict | None:
        """
        Создает новый склад в PrestaShop.

        Args:
            data (dict): Данные для создания склада.

        Returns:
            dict | None: Словарь с информацией о созданном складе или None в случае ошибки.

        Raises:
            Exception: В случае ошибки при запросе к API.
        """
        try:
            return self.add('warehouses', data)
        except Exception as ex:
            logger.error(f'Ошибка при создании склада: {ex}', exc_info=True)
            return None

    def update_warehouse(self, warehouse_id: int, data: dict) -> dict | None:
        """
        Обновляет информацию о складе в PrestaShop.

        Args:
            warehouse_id (int): ID склада для обновления.
            data (dict): Данные для обновления склада.

        Returns:
            dict | None: Словарь с информацией об обновленном складе или None в случае ошибки.

        Raises:
            Exception: В случае ошибки при запросе к API.
        """
        try:
            return self.update(f'warehouses/{warehouse_id}', data)
        except Exception as ex:
            logger.error(f'Ошибка при обновлении склада с ID {warehouse_id}: {ex}', exc_info=True)
            return None

    def delete_warehouse(self, warehouse_id: int) -> bool:
        """
        Удаляет склад из PrestaShop.

        Args:
            warehouse_id (int): ID склада для удаления.

        Returns:
            bool: True в случае успешного удаления, False в случае ошибки.

        Raises:
            Exception: В случае ошибки при запросе к API.
        """
        try:
            return self.delete(f'warehouses/{warehouse_id}')
        except Exception as ex:
            logger.error(f'Ошибка при удалении склада с ID {warehouse_id}: {ex}', exc_info=True)
            return False
```
```python
#Примеры работы с классом
from src.endpoints.prestashop.warehouse import PrestaWarehouse

#Замените на актуальные данные
url = 'https://your-prestashop-url.com'
api_key = 'your_api_key'

warehouse_api = PrestaWarehouse(url, api_key, debug=True)

# Пример получения списка складов
warehouses = warehouse_api.get_warehouses()
if warehouses:
    print("Список складов:", warehouses)

# Пример получения информации о складе по ID
warehouse_id = 1  # Замените на актуальный ID склада
warehouse = warehouse_api.get_warehouse(warehouse_id)
if warehouse:
    print(f"Информация о складе с ID {warehouse_id}:", warehouse)

# Пример создания нового склада
new_warehouse_data = {
    'name': 'My New Warehouse',
    'address1': '123 Main St',
    'city': 'New York',
    'id_country': 17,  # ID страны (например, США)
    'postcode': '10001'
}
created_warehouse = warehouse_api.create_warehouse(new_warehouse_data)
if created_warehouse:
    print("Склад успешно создан:", created_warehouse)

# Пример обновления информации о складе
updated_warehouse_data = {
    'name': 'Updated Warehouse Name'
}
warehouse_id_to_update = 2  # Замените на актуальный ID склада
updated_warehouse = warehouse_api.update_warehouse(warehouse_id_to_update, updated_warehouse_data)
if updated_warehouse:
    print(f"Склад с ID {warehouse_id_to_update} успешно обновлен:", updated_warehouse)

# Пример удаления склада
warehouse_id_to_delete = 3  # Замените на актуальный ID склада
deleted = warehouse_api.delete_warehouse(warehouse_id_to_delete)
if deleted:
    print(f"Склад с ID {warehouse_id_to_delete} успешно удален.")
else:
    print(f"Не удалось удалить склад с ID {warehouse_id_to_delete}.")
```
```python

```
```python

```
```python

```
```python

```
```python