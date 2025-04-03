# Модуль для получения ссылок на чаты в ChatGPT

## Обзор

Модуль предназначен для автоматического извлечения ссылок на отдельные чаты из веб-интерфейса ChatGPT. В настоящее время модуль не работает с драйверами Chrome и Firefox.

## Подробнее

Этот модуль предназначен для автоматизации процесса сбора ссылок на чаты в ChatGPT. Он использует веб-драйвер для открытия страницы ChatGPT и извлечения необходимых ссылок.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `get_links`

```python
def get_links(d: Driver) -> list:
    """Ссылки на отдельные чаты """
    ...
    links = d.execute_locator(locator.link)
    return links
```

**Назначение**: Извлечение ссылок на отдельные чаты со страницы ChatGPT.

**Параметры**:
- `d` (Driver): Объект драйвера, используемый для управления браузером.

**Возвращает**:
- `list`: Список веб-элементов, представляющих ссылки на чаты.

**Как работает функция**:

1.  Функция `get_links` принимает объект драйвера `d` в качестве аргумента.
2.  Использует метод `execute_locator` объекта драйвера `d` для поиска элементов, соответствующих локатору `locator.link`.
3.  Возвращает список найденных элементов.

```ascii
    A
    |
    B
    |
    C
```

Где:

*   `A`: Получение объекта драйвера.
*   `B`: Поиск элементов по локатору `locator.link`.
*   `C`: Возврат списка найденных элементов.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.utils.jjson import j_loads_ns
from src import gs

locator = j_loads_ns(gs.path.src / 'suppliers' / 'chat_gpt' / 'locators' / 'chats_list.json')
d = Driver(Firefox)
d.get_url('https://chatgpt.com/')
links = get_links(d)
if links:
    print(f'Найдено {len(links)} ссылок на чаты')
else:
    print('Ссылки на чаты не найдены')
```

## Главный блок `if __name__ == '__main__'`

```python
if __name__ == '__main__':
    d = Driver(Firefox)
    d.get_url('https://chatgpt.com/')
    links = get_links(d)
    ...
```

**Назначение**: Обеспечивает запуск кода только при непосредственном выполнении скрипта, а не при импорте его как модуля.

**Как работает**:

1.  Создается экземпляр драйвера Firefox.
2.  Выполняется переход по URL-адресу `https://chatgpt.com/`.
3.  Вызывается функция `get_links` для получения ссылок на чаты.

**Примеры**:

```python
if __name__ == '__main__':
    d = Driver(Firefox)
    d.get_url('https://chatgpt.com/')
    links = get_links(d)
    if links:
        print(f'Найдено {len(links)} ссылок на чаты')
    else:
        print('Ссылки на чаты не найдены')