# Анализ кода модуля `mega.py`

**Качество кода: 7/10**
-  Плюсы
    - Код выполняет основные функции для работы с API Mega, включая аутентификацию, загрузку и скачивание файлов.
    - Используются криптографические функции для шифрования и дешифрования данных.
    - Присутствуют обработки исключений для запросов к API и неверных паролей.
-  Минусы
    -  Не хватает документации для функций и класса.
    -  Используется стандартный `json.load` для обработки `json`, хотя в требованиях указано использование `j_loads`.
    -  Присутствуют избыточные `try-except` блоки.
    -  Не все переменные и функции соответствуют стандартам именования.
    -  Отсутствует импорт `logger` из `src.logger.logger`

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring к классу `Mega` и всем его методам, используя формат RST.
2.  **Использование `j_loads`:** Заменить использование `json.loads` на `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование:** Заменить `print` на `logger.error` для обработки ошибок и импортировать `logger` из `src.logger.logger`.
4.  **Обработка исключений:** Упростить обработку исключений, используя `logger.error` вместо `try-except`.
5.  **Согласованность именования:** Привести имена переменных и функций к общему стилю, используя snake_case.
6.  **Улучшение читаемости:** Добавить комментарии для лучшего понимания логики кода, особенно в криптографических операциях.
7.  **Использовать одинарные кавычки:** Заменить двойные кавычки на одинарные в коде, согласно инструкции, за исключением операций вывода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Mega API
=========================================================================================

Этот модуль содержит класс :class:`Mega`, который предоставляет интерфейс
для взаимодействия с API Mega, включая аутентификацию, загрузку, скачивание и управление файлами.

Пример использования
--------------------

Пример использования класса `Mega`:

.. code-block:: python

    mega = Mega.from_credentials(email='user@example.com', password='password')
    files = mega.get_files()
"""
import os
import random
import binascii

import requests
from urlobject import URLObject
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util import Counter

from mega.crypto import prepare_key, stringhash, encrypt_key, decrypt_key, \
    enc_attr, dec_attr, aes_cbc_encrypt_a32
from mega.utils import a32_to_str, str_to_a32, a32_to_base64, base64_to_a32, \
    mpi2int, base64urlencode, base64urldecode, get_chunks
from mega.exceptions import MegaRequestException, MegaIncorrectPasswordExcetion
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


class Mega(object):
    """
    Класс для взаимодействия с API Mega.

    Предоставляет методы для аутентификации, загрузки, скачивания файлов и других операций.
    """

    def __init__(self):
        """
        Инициализация объекта Mega.

        Устанавливает начальный номер последовательности запросов и идентификатор сессии.
        """
        self.seqno = random.randint(0, 0xFFFFFFFF)
        self.sid = None

    @classmethod
    def from_credentials(cls, email, password):
        """
        Создает экземпляр класса Mega, выполняя вход пользователя с указанными учетными данными.

        Args:
            email (str): Адрес электронной почты пользователя.
            password (str): Пароль пользователя.

        Returns:
            Mega: Экземпляр класса Mega.
        """
        inst = cls()
        inst.login_user(email, password)
        return inst

    @classmethod
    def from_ephemeral(cls):
        """
        Создает экземпляр класса Mega, выполняя анонимный (временный) вход.

        Returns:
            Mega: Экземпляр класса Mega.
        """
        inst = cls()
        inst.login_ephemeral()
        return inst

    def api_req(self, data):
        """
        Выполняет запрос к API Mega.

        Args:
            data (dict): Данные для отправки в запросе.

        Returns:
            dict: Ответ от API в формате JSON.

        Raises:
            MegaRequestException: Если API возвращает ошибку.
        """
        params = {'id': self.seqno}
        self.seqno += 1
        if self.sid:
            params.update({'sid': self.sid})
        data = j_loads_ns([data]) #  кодирует данные для отправки в формате JSON.
        req = requests.post(
            'https://g.api.mega.co.nz/cs', params=params, data=data)
        json_data = req.json()
        if isinstance(json_data, int):
            raise MegaRequestException(json_data)
        return json_data[0]

    def login_user(self, email, password):
        """
        Выполняет вход пользователя с указанными учетными данными.

        Args:
            email (str): Адрес электронной почты пользователя.
            password (str): Пароль пользователя.
        """
        password_aes = prepare_key(str_to_a32(password)) #  подготавливает ключ шифрования на основе пароля.
        uh = stringhash(email, password_aes) # создает хеш email и ключа
        res = self.api_req({'a': 'us', 'user': email, 'uh': uh}) # отправляет запрос на авторизацию
        self._login_common(res, password_aes) # вызывает метод для обработки ответа

    def login_ephemeral(self):
        """
        Выполняет анонимный (временный) вход.
        """
        random_master_key = [random.randint(0, 0xFFFFFFFF)] * 4 # генерирует случайный мастер ключ
        random_password_key = [random.randint(0, 0xFFFFFFFF)] * 4 # генерирует случайный ключ пароля
        random_session_self_challenge = [random.randint(0, 0xFFFFFFFF)] * 4 # генерирует случайный challenge
        user_handle = self.api_req({
            'a': 'up',
            'k': a32_to_base64(encrypt_key(random_master_key,
                                           random_password_key)),
            'ts': base64urlencode(a32_to_str(random_session_self_challenge) +
                                  a32_to_str(encrypt_key(
                                      random_session_self_challenge,
                                      random_master_key)))
        }) # отправляет запрос на создание временной сессии
        res = self.api_req({'a': 'us', 'user': user_handle}) #  запрос для получения данных пользователя
        self._login_common(res, random_password_key) # обрабатывает ответ

    def _login_common(self, res, password):
        """
        Общий метод для обработки ответа после входа в систему.

        Args:
            res (dict): Ответ от API.
            password (list): Ключ пароля.

        Raises:
            MegaIncorrectPasswordExcetion: Если пароль или email неверны.
        """
        if res in (-2, -9):
            raise MegaIncorrectPasswordExcetion("Incorrect e-mail and/or password.") # проверка ошибки
        
        enc_master_key = base64_to_a32(res['k']) #  получает зашифрованный мастер-ключ
        self.master_key = decrypt_key(enc_master_key, password) #  дешифрует мастер-ключ
        if 'tsid' in res:
            tsid = base64urldecode(res['tsid']) # получает tsid
            key_encrypted = a32_to_str(
                encrypt_key(str_to_a32(tsid[:16]), self.master_key)) # шифрует tsid
            if key_encrypted == tsid[-16:]: # сравнивает зашифрованный tsid
                self.sid = res['tsid'] #  устанавливает идентификатор сессии
        elif 'csid' in res:
            enc_rsa_priv_key = base64_to_a32(res['privk']) #  получает зашифрованный RSA приватный ключ
            rsa_priv_key = decrypt_key(enc_rsa_priv_key, self.master_key) # дешифрует приватный ключ

            privk = a32_to_str(rsa_priv_key)
            self.rsa_priv_key = [0, 0, 0, 0]

            for i in range(4): # извлекает значения RSA
                l = ((privk[0] * 256 + privk[1] + 7) // 8) + 2
                self.rsa_priv_key[i] = mpi2int(privk[:l])
                privk = privk[l:]

            enc_sid = mpi2int(base64urldecode(res['csid'])) #  получает зашифрованный идентификатор сессии
            decrypter = RSA.construct( # создаёт RSA объект
                (self.rsa_priv_key[0] * self.rsa_priv_key[1],
                 0,
                 self.rsa_priv_key[2],
                 self.rsa_priv_key[0],
                 self.rsa_priv_key[1]))
            sid = '%x' % decrypter.key._decrypt(enc_sid) #  дешифрует идентификатор сессии
            sid = binascii.unhexlify('0' + sid if len(sid) % 2 else sid)
            self.sid = base64urlencode(sid[:43]) #  устанавливает идентификатор сессии

    def get_files(self):
        """
        Получает список файлов и папок пользователя.

        Returns:
            dict: Данные о файлах и папках пользователя.
        """
        files_data = self.api_req({'a': 'f', 'c': 1}) # отправляет запрос на получение списка файлов
        for file in files_data['f']:
            if file['t'] in (0, 1):
                key = file['k'].split(':')[1] # получает ключ файла
                key = decrypt_key(base64_to_a32(key), self.master_key) # дешифрует ключ
                # file
                if file['t'] == 0:
                    k = (key[0] ^ key[4],
                         key[1] ^ key[5],
                         key[2] ^ key[6],
                         key[3] ^ key[7])
                # directory
                else:
                    k = key
                attributes = base64urldecode(file['a']) # получает атрибуты файла
                attributes = dec_attr(attributes, k)  # дешифрует атрибуты
                file['a'] = attributes #  сохраняет атрибуты
                file['k'] = key  #  сохраняет ключ
            # Root ("Cloud Drive")
            elif file['t'] == 2:
                self.root_id = file['h'] #  устанавливает идентификатор корневой папки
            # Inbox
            elif file['t'] == 3:
                self.inbox_id = file['h'] #  устанавливает идентификатор папки входящих
            # Trash Bin
            elif file['t'] == 4:
                self.trashbin_id = file['h'] #  устанавливает идентификатор корзины
        return files_data

    def download_from_url(self, url):
        """
        Скачивает файл по публичной ссылке.

        Args:
            url (str): Публичная ссылка на файл Mega.

        Returns:
            str: Имя файла.
        """
        url_object = URLObject(url) #  создает объект URL
        file_id, file_key = url_object.fragment[1:].split('!') # извлекает ID и ключ
        
        #return the filename
        return self.download_file(file_id, file_key, public=True) #  скачивает файл

    def download_file(self, file_id, file_key, public=False, store_path=None):
        """
        Скачивает файл по ID и ключу.

        Args:
            file_id (str): ID файла.
            file_key (str|list): Ключ файла.
            public (bool, optional): Флаг публичного доступа. Defaults to False.
            store_path (str, optional): Путь для сохранения файла. Defaults to None.

        Returns:
            str: Имя файла.

        Raises:
            ValueError: Если MAC не совпадает.
        """
        if public:
            file_key = base64_to_a32(file_key) # если файл публичный, декодирует ключ
            file_data = self.api_req({'a': 'g', 'g': 1, 'p': file_id}) # запрос на скачивание публичного файла
        else:
            file_data = self.api_req({'a': 'g', 'g': 1, 'n': file_id}) #  запрос на скачивание файла

        k = (file_key[0] ^ file_key[4], #  вычисляет ключ
             file_key[1] ^ file_key[5],
             file_key[2] ^ file_key[6],
             file_key[3] ^ file_key[7])
        iv = file_key[4:6] + (0, 0) #  получает вектор инициализации
        meta_mac = file_key[6:8]  #  получает мета MAC

        file_url = file_data['g']  #  получает URL файла
        file_size = file_data['s'] #  получает размер файла
        attributes = base64urldecode(file_data['at']) #  получает атрибуты
        attributes = dec_attr(attributes, k) #  дешифрует атрибуты
        file_name = attributes['n'] #  получает имя файла

        infile = requests.get(file_url, stream=True).raw #  скачивает файл
        if store_path:
            file_name = os.path.join(store_path, file_name) #  формирует путь сохранения
        outfile = open(file_name, 'wb') #  открывает файл для записи

        counter = Counter.new( # создает счетчик для AES
            128, initial_value=((iv[0] << 32) + iv[1]) << 64)
        decryptor = AES.new(a32_to_str(k), AES.MODE_CTR, counter=counter) #  создает объект дешифрования AES

        file_mac = (0, 0, 0, 0)  #  инициализирует MAC
        for chunk_start, chunk_size in sorted(get_chunks(file_size).items()):
            chunk = infile.read(chunk_size) #  читает чанк
            chunk = decryptor.decrypt(chunk) #  дешифрует чанк
            outfile.write(chunk) #  записывает чанк в файл

            chunk_mac = [iv[0], iv[1], iv[0], iv[1]] #  инициализирует MAC чанка
            for i in range(0, len(chunk), 16):
                block = chunk[i:i+16]
                if len(block) % 16:
                    block += b'\0' * (16 - (len(block) % 16))
                block = str_to_a32(block)
                chunk_mac = [
                    chunk_mac[0] ^ block[0],
                    chunk_mac[1] ^ block[1],
                    chunk_mac[2] ^ block[2],
                    chunk_mac[3] ^ block[3]]
                chunk_mac = aes_cbc_encrypt_a32(chunk_mac, k)

            file_mac = [
                file_mac[0] ^ chunk_mac[0],
                file_mac[1] ^ chunk_mac[1],
                file_mac[2] ^ chunk_mac[2],
                file_mac[3] ^ chunk_mac[3]]
            file_mac = aes_cbc_encrypt_a32(file_mac, k)

        outfile.close()

        # Integrity check
        if (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3]) != meta_mac:
            raise ValueError('MAC mismatch') #  проверка целостности
        
        return file_name #  возвращает имя файла
    
    def get_public_url(self, file_id, file_key):
        """
        Получает публичную ссылку на файл.

        Args:
            file_id (str): ID файла.
            file_key (list): Ключ файла.

        Returns:
             str: Публичная ссылка на файл.
        """
        public_handle = self.api_req({'a': 'l', 'n': file_id}) #  запрашивает публичный дескриптор
        decrypted_key = a32_to_base64(file_key) #  преобразует ключ
        return 'http://mega.co.nz/#!%s!%s' % (public_handle, decrypted_key) #  возвращает публичную ссылку

    def uploadfile(self, filename, dst=None):
        """
        Загружает файл на Mega.

        Args:
            filename (str): Путь к файлу для загрузки.
            dst (str, optional): ID папки назначения. Defaults to None.

        Returns:
            dict: Ответ API.
        """
        if not dst:
            root_id = getattr(self, 'root_id', None)
            if root_id == None:
                self.get_files()
            dst = self.root_id #  устанавливает ID папки назначения
        infile = open(filename, 'rb') # открывает файл для чтения
        size = os.path.getsize(filename) #  получает размер файла
        ul_url = self.api_req({'a': 'u', 's': size})['p'] #  запрашивает URL загрузки

        ul_key = [random.randint(0, 0xFFFFFFFF) for _ in range(6)] #  генерирует ключ загрузки
        counter = Counter.new( #  создает счетчик
            128, initial_value=((ul_key[4] << 32) + ul_key[5]) << 64)
        encryptor = AES.new( #  создает объект шифрования AES
            a32_to_str(ul_key[:4]),
            AES.MODE_CTR,
            counter=counter)

        file_mac = [0, 0, 0, 0] #  инициализирует MAC
        for chunk_start, chunk_size in sorted(get_chunks(size).items()):
            chunk = infile.read(chunk_size) #  читает чанк

            chunk_mac = [ul_key[4], ul_key[5], ul_key[4], ul_key[5]] #  инициализирует MAC чанка
            for i in range(0, len(chunk), 16):
                block = chunk[i:i+16]
                if len(block) % 16:
                    block += b'\0' * (16 - len(block) % 16)
                block = str_to_a32(block)
                chunk_mac = [chunk_mac[0] ^ block[0],
                             chunk_mac[1] ^ block[1],
                             chunk_mac[2] ^ block[2],
                             chunk_mac[3] ^ block[3]]
                chunk_mac = aes_cbc_encrypt_a32(chunk_mac, ul_key[:4])

            file_mac = [file_mac[0] ^ chunk_mac[0],
                        file_mac[1] ^ chunk_mac[1],
                        file_mac[2] ^ chunk_mac[2],
                        file_mac[3] ^ chunk_mac[3]]
            file_mac = aes_cbc_encrypt_a32(file_mac, ul_key[:4]) #  вычисляет MAC

            chunk = encryptor.encrypt(chunk) #  шифрует чанк
            url = '%s/%s' % (ul_url, str(chunk_start)) #  формирует URL для загрузки
            outfile = requests.post(url, data=chunk, stream=True).raw #  отправляет чанк

            # assume utf-8 encoding. Maybe this entire section can be simplified
            # by not looking at the raw output
            # (http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow)

            completion_handle = outfile.read().decode('utf-8') # получает идентификатор завершения
        infile.close()

        meta_mac = (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3]) # вычисляет meta MAC

        attributes = {'n': os.path.basename(filename)} #  создает словарь атрибутов
        enc_attributes = base64urlencode(enc_attr(attributes, ul_key[:4])) # шифрует атрибуты
        key = [ul_key[0] ^ ul_key[4],
               ul_key[1] ^ ul_key[5],
               ul_key[2] ^ meta_mac[0],
               ul_key[3] ^ meta_mac[1],
               ul_key[4], ul_key[5],
               meta_mac[0], meta_mac[1]] #  формирует ключ
        encrypted_key = a32_to_base64(encrypt_key(key, self.master_key)) #  шифрует ключ
        data = self.api_req({'a': 'p', 't': dst, 'n': [
            {'h': completion_handle,
             't': 0,
             'a': enc_attributes,
             'k': encrypted_key}]}) #  отправляет запрос на завершение загрузки
        return data