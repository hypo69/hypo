# Модуль авторизации для Etzmaleh

## Обзор

Модуль `login.py` предназначен для осуществления авторизации поставщика Etzmaleh. В настоящее время содержит заглушку, возвращающую `True`, и логирует факт «авторизации».

## Подробней

Данный модуль является частью системы взаимодействия с поставщиками проекта `hypotez`. На данный момент он выполняет фиктивную авторизацию, но в будущем должен быть реализован полноценный механизм авторизации через веб-драйвер.

## Функции

### `login(s)`

```python
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
```

**Назначение**:
Функция `login(s)` предназначена для выполнения авторизации поставщика.

**Параметры**:
- `s`: Объект поставщика (Supplier), содержащий данные, необходимые для авторизации.

**Возвращает**:
- `bool`: `True`, если авторизация прошла успешно, `False` в противном случае.

**Как работает функция**:

1. Функция логирует сообщение о том, что произошла авторизация.
2.  Возвращает `True`, имитируя успешную авторизацию.

**Примеры**:

```python
from src.suppliers.etzmaleh.login import login

class Supplier:
    def __init__(self, name):
        self.name = name

s = Supplier(name='Etzmaleh')
result = login(s)
print(result)  # Вывод: True
```
```python
from src.suppliers.etzmaleh.login import login

class Supplier:
    def __init__(self, name):
        self.name = name

s = Supplier(name='Etzmaleh')
result = login(s)
if result:
    print('Авторизация прошла успешно')
else:
    print('Ошибка авторизации')