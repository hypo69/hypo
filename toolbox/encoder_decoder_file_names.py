import hashlib
import sqlite3
from pathlib import Path
from typing import Optional



class PathEncoderDecoder:
    """
    Класс для кодирования и декодирования путей с использованием хэширования 
    и хранения данных в SQLite базе данных.
    """

    def __init__(self, db_path: str = 'path_mapping.db'):
        """
        Инициализация класса.

        Args:
            db_path (str): Путь к SQLite базе данных для хранения таблицы соответствий.
        """
        self.db_path = Path(db_path)
        self._initialize_database()

    def _initialize_database(self):
        """
        Инициализация базы данных, создание таблицы, если она отсутствует.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS path_mapping (
                    id TEXT PRIMARY KEY,
                    file_path TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def _save_to_database(self, short_id: str, file_path: str):
        """
        Сохраняет хэш и путь в базу данных.

        Args:
            short_id (str): Уникальный идентификатор пути.
            file_path (str): Полный путь к файлу.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO path_mapping (id, file_path) VALUES (?, ?)",
                (short_id, file_path)
            )
            conn.commit()

    def _fetch_from_database(self, short_id: str) -> Optional[str]:
        """
        Извлекает путь из базы данных по короткому идентификатору.

        Args:
            short_id (str): Уникальный идентификатор пути.

        Returns:
            Optional[str]: Полный путь файла или `None`, если идентификатор не найден.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT file_path FROM path_mapping WHERE id = ?", (short_id,))
            result = cursor.fetchone()
            return result[0] if result else None

    def encode(self, file_path: str) -> str:
        """
        Кодирует путь в короткий идентификатор.

        Args:
            file_path (str): Полный путь файла.

        Returns:
            str: Короткий идентификатор.
        """
        # Генерация хэша пути
        path_hash = hashlib.md5(file_path.encode('utf-8')).hexdigest()[:8]  # 8 символов
        short_id = f'id-{path_hash}'

        # Сохранение в базу данных
        self._save_to_database(short_id, file_path)
        return short_id

    def decode(self, short_id: str) -> Optional[str]:
        """
        Декодирует короткий идентификатор обратно в путь.

        Args:
            short_id (str): Короткий идентификатор.

        Returns:
            Optional[str]: Полный путь файла или `None`, если идентификатор не найден.
        """
        return self._fetch_from_database(short_id)

    def clear_mapping(self):
        """
        Очищает таблицу соответствий.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM path_mapping")
            conn.commit()

# Пример использования
if __name__ == '__main__':
    encoder_decoder = PathEncoderDecoder()

    # Кодирование пути
    original_path = 'src/same_folder/same_sub_folder/same-file.ext'
    encoded = encoder_decoder.encode(original_path)
    print(f'Кодированный путь: {encoded}')

    # Декодирование пути
    decoded = encoder_decoder.decode(encoded)
    print(f'Декодированный путь: {decoded}')

    # Очистка таблицы соответствий
    # encoder_decoder.clear_mapping()
