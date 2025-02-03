import platform
import psutil

def get_system_info():
    info = {
        "Операционная система": platform.system(),
        "Версия ОС": platform.version(),
        "Имя компьютера": platform.node(),
        "Архитектура": platform.architecture(),
        "Процессор": platform.processor(),
        "Количество ядер": psutil.cpu_count(logical=True),
        "Объем оперативной памяти": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Объем свободной памяти": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Диск": psutil.disk_usage('/').total / (1024 ** 3)
    }
    return info


if __name__ == "__main__":
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")