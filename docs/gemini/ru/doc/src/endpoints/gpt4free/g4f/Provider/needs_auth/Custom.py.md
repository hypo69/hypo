# Модуль Custom

## Обзор

Модуль определяет классы `Custom` и `Feature`, которые наследуют класс `OpenaiTemplate`. Эти классы используются для настройки и работы с пользовательскими провайдерами, совместимыми с API OpenAI, в рамках проекта `hypotez`.

## Подробнее

Модуль `Custom` предоставляет базовую конфигурацию для пользовательских провайдеров, позволяя указывать адрес API, необходимость аутентификации и другие параметры. Класс `Feature` наследует `Custom` и предназначен для указания нерабочих провайдеров.

## Классы

### `Custom`

**Описание**:
Класс `Custom` наследует `OpenaiTemplate` и представляет собой базовую конфигурацию для пользовательского провайдера.

**Принцип работы**:
Класс задает основные атрибуты, необходимые для работы с пользовательским провайдером, таким как адрес API, флаг необходимости аутентификации и другие параметры.

**Наследует**:
- `OpenaiTemplate`: Класс, предоставляющий шаблон для провайдеров OpenAI.

**Атрибуты**:
- `label` (str): Метка провайдера ("Custom Provider").
- `working` (bool): Указывает, работает ли провайдер (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация (False).
- `api_base` (str): Базовый адрес API провайдера ("http://localhost:8080/v1").
- `sort_models` (bool): Указывает, нужно ли сортировать модели (False).

### `Feature`

**Описание**:
Класс `Feature` наследует класс `Custom` и используется для представления нерабочего провайдера.

**Принцип работы**:
Класс переопределяет атрибут `working` класса `Custom` на `False`, указывая, что данный провайдер не работает.

**Наследует**:
- `Custom`: Базовый класс для пользовательских провайдеров.

**Атрибуты**:
- `label` (str): Метка провайдера ("Feature Provider").
- `working` (bool): Указывает, работает ли провайдер (False).

```python
from __future__ import annotations

from ..template import OpenaiTemplate

class Custom(OpenaiTemplate):
    label = "Custom Provider"
    working = True
    needs_auth = False
    api_base = "http://localhost:8080/v1"
    sort_models = False

class Feature(Custom):
    label = "Feature Provider"
    working = False