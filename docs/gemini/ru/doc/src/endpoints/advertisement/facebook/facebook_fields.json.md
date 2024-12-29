# Документация для `facebook_fields.json`

## Обзор

Файл `facebook_fields.json` содержит JSON-структуру, определяющую поля для создания рекламных объявлений в Facebook. Включает поля для постов и событий, а также параметры таймаута.

## Оглавление

- [Структура JSON](#структура-json)
- [Поле `post`](#поле-post)
- [Поле `timeout`](#поле-timeout)
- [Поле `timeout_for_event`](#поле-timeout_for_event)
- [Поле `event`](#поле-event)

## Структура JSON

JSON-структура состоит из полей `post`, `timeout`, `timeout_for_event` и `event`.

```json
{
	"post": {
		"title": "",
		"description": "",
		"language": "",
		"currency": "",
		"price": "",
		"category": "",
		"products" : []
	},
	"timeout":0,
  "timeout_for_event":"presence_of_element_located",
	"event": {
		"title": "",
		"description": "",
		"language": "",
		"currency": "",
		"price": "",
		"start_date": "",
		"start_time": "",
		"end_date": ""
	}
}
```

## Поле `post`

### Описание
Поле `post` содержит информацию, необходимую для создания рекламного поста.

### Структура
- `title` (string): Заголовок поста.
- `description` (string): Описание поста.
- `language` (string): Язык поста.
- `currency` (string): Валюта для цены.
- `price` (string): Цена.
- `category` (string): Категория поста.
- `products` (array): Массив продуктов.

## Поле `timeout`

### Описание

Поле `timeout` определяет таймаут для операций.

### Структура
- `timeout` (number): Значение таймаута, выраженное в секундах.

## Поле `timeout_for_event`

### Описание
Поле `timeout_for_event` определяет, какой таймаут использовать для события.

### Структура
- `timeout_for_event` (string): строка представляющая стратегию таймаута, например "presence_of_element_located".

## Поле `event`

### Описание

Поле `event` содержит информацию, необходимую для создания рекламного события.

### Структура
- `title` (string): Заголовок события.
- `description` (string): Описание события.
- `language` (string): Язык события.
- `currency` (string): Валюта для цены.
- `price` (string): Цена события.
- `start_date` (string): Дата начала события.
- `start_time` (string): Время начала события.
- `end_date` (string): Дата окончания события.