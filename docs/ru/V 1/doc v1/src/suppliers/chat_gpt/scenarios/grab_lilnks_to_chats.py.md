# Модуль `grab_lilnks_to_chats`

## Обзор

Этот модуль предназначен для извлечения ссылок на отдельные чаты с веб-страницы, используя веб-драйвер. В текущей реализации (**ВАЖНО:**) не работает через драйверы Chrome и Firefox. Модуль использует файл локаторов для определения элементов на странице.

## Подробней

Модуль `grab_lilnks_to_chats` разработан для автоматизации процесса сбора ссылок на чаты с веб-сайта ChatGPT. Он использует веб-драйвер (в данном случае, Firefox) для навигации по сайту и извлечения необходимых данных. Файл `chats_list.json` содержит локаторы элементов, которые используются для поиска ссылок на странице.  Важно отметить, что, согласно комментариям в коде, текущая реализация не работает через драйверы Chrome и Firefox.  Дальнейшая работа с модулем потребует решения этой проблемы.

## Функции

### `get_links`

```python
def get_links(d:Driver):
    """Ссылки на отдельные чаты """
    ...
```

**Описание**: Извлекает ссылки на отдельные чаты с использованием драйвера.

**Параметры**:
- `d` (Driver): Экземпляр класса `Driver`, представляющий веб-драйвер.

**Возвращает**:
- `links`: Список найденных ссылок на чаты. Тип возвращаемого значения не указан явно в предоставленном коде, но, вероятно, это список строк.

**Вызывает исключения**:
- В предоставленном коде нет явной обработки исключений.

**Примеры**:

```python
from src.webdriver.firefox import Firefox
from src.webdriver.driver import Driver

d = Driver(Firefox)
d.get_url('https://chatgpt.com/')
links = get_links(d)
if links:
    print(f'Найдены ссылки: {links}')
else:
    print('Ссылки не найдены.')
```
```python
from src.webdriver.firefox import Firefox
from src.webdriver.driver import Driver
from unittest.mock import MagicMock

# Создаем мок-объект для класса Driver
mock_driver = MagicMock(spec=Driver)
mock_driver.execute_locator.return_value = ['link1', 'link2', 'link3']  # Задаем возвращаемое значение для execute_locator

# Вызываем функцию get_links с мок-объектом
links = get_links(mock_driver)

# Проверяем, что функция вернула ожидаемый результат
print(f'Найдены ссылки: {links}')
```
```python
from src.webdriver.firefox import Firefox
from src.webdriver.driver import Driver
from unittest.mock import MagicMock

# Создаем мок-объект для класса Driver
mock_driver = MagicMock(spec=Driver)
mock_driver.execute_locator.return_value = []  # Задаем пустой список как возвращаемое значение для execute_locator

# Вызываем функцию get_links с мок-объектом
links = get_links(mock_driver)

# Проверяем, что функция вернула ожидаемый результат
if not links:
    print('Ссылки не найдены.')
```