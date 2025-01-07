# Импортируем библиотеку для выполнения HTTP-запросов
import requests


# Функция для скачивания файла по указанному URL и сохранения его на диск.
def download_file(url, destination):

    # Отправляем GET-запрос на сервер с указанным URL и передаем флаг stream=True для постепенной загрузки файла
    response = requests.get(url, stream=True)

    # Проверяем, успешен ли запрос (код ответа 200 означает успех)
    if response.status_code == 200:
        # Открываем файл для записи в бинарном режиме (wb)
        with open(destination, 'wb') as file:
            # Скачиваем файл по частям (по 1024 байта), чтобы избежать проблем с памятью при больших файлах
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)  # Записываем каждую часть в файл
        print("Файл успешно загружен!")  # Сообщаем об успешной загрузке
    else:
        # Если код ответа не 200, выводим сообщение об ошибке
        print("Ошибка загрузки файла!")


# Пример использования функции: скачивание файла по URL
file_url = 'https://example.com/path/to/file.txt'  # URL файла для скачивания
save_as = 'downloaded_file.txt'  # Имя файла, под которым он будет сохранен на диске
download_file(file_url, save_as)  # Вызов функции скачивания файла
