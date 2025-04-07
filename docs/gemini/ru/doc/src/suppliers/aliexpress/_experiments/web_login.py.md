# Модуль web_login.py

## Обзор

Модуль `web_login.py` предназначен для экспериментов с автоматическим входом на сайт AliExpress, получения и сохранения cookies.
Он использует библиотеку `requests` для отправки HTTP-запросов и модуль `pickle` для сохранения cookies.

## Подробней

Модуль выполняет следующие шаги:
1.  Импортирует необходимые библиотеки и модули, включая `header`, `Path`, `pickle`, `requests`, `gs`, `Supplier`, `pprint`.
2.  Создает экземпляр класса `Supplier` для AliExpress.
3.  Получает драйвер из экземпляра `Supplier`.
4.  Переходит по URL `https://aliexpress.com` с помощью драйвера.

## Классы

В предоставленном коде нет определения классов.

## Функции

В предоставленном коде нет определения функций.

## Пример

```python
import header
from pathlib import Path
import pickle
import requests

from src import gs
from src.suppliers import Supplier
from src.utils.printer import pprint

a = Supplier('aliexpress')

d = a.driver
d.get_url('https://aliexpress.com')
```