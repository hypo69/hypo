# `test_upload.py`

## Обзор

Данный файл содержит пример использования API для загрузки файла через IOP (Internet Open Platform). Он демонстрирует, как создать запрос на загрузку файла с использованием библиотеки `iop`.

## Оглавление

- [Обзор](#обзор)
- [Пример использования](#пример-использования)

## Пример использования

### Описание

В этом разделе представлен пример кода, демонстрирующий процесс создания и выполнения запроса на загрузку файла с использованием IOP. 

В коде устанавливается клиент IOP с указанием URL, ключа приложения и секрета приложения. Затем создается запрос для загрузки файла по определенному пути API. К запросу добавляются простые параметры типа `String`, такие как имя файла, и параметры типа `file`, которые содержат содержимое файла. После выполнения запроса, результат выводится в консоль, включая тип ответа, код, сообщение, ID запроса и полное тело ответа.

```python
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api._examples.iop """
# # -*- coding: utf-8 -*-
#
# import iop
#
# # params 1 : gateway url
# # params 2 : appkey
# # params 3 : appSecret
# client = iop.IopClient('https://api.taobao.tw/rest', '${appKey}', '${appSecret}')
#
# # create a api request
# request = iop.IopRequest('/xiaoxuan/mockfileupload')
#
# # simple type params ,Number ,String
# request.add_api_param('file_name','pom.xml')
#
# # file params, value should be file content
# request.add_file_param('file_bytes',open('/Users/xt/Documents/work/tasp/tasp/pom.xml').read())
#
# response = client.execute(request)
# #response = client.execute(request,access_token)
#
#
# # response type nil,ISP,ISV,SYSTEM
# # nil ：no error
# # ISP : API Service Provider Error
# # ISV : API Request Client Error
# # SYSTEM : Iop platform Error
# print(response.type)
#
# # response code, 0 is no error
# print(response.code)
#
# # response error message
# print(response.message)
#
# # response unique id
# print(response.request_id)
#
# # full response
# print(response.body)
```