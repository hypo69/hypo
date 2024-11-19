```diff
--- a/hypotez/src/endpoints/hypo69/code_assistant/assistant.py
+++ b/hypotez/src/endpoints/hypo69/code_assistant/assistant.py
@@ -1,12 +1,12 @@
 # -*- coding: utf-8 -*-
 #! venv/Scripts/python.exe
 #! venv/bin/python
-""" module: src.endpoints.hypo69.code_assistant """
+"""Ассистент для обучения моделей на основе кода."""
 MODE = 'development'
 import re
 import sys
 import time
-import signal
+import signal  # Для обработки CTRL+C
 import json
 import argparse
 from pathlib import Path
@@ -23,7 +23,7 @@
 from src.utils.printer import pprint
 from src.logger import logger
 
-class CodeAssistant(BaseModel):
+class CodeAssistant(BaseModel):  # Класс ассистента
     """Класс обучения ассистента программиста."""
 
     role: str = Field(default="doc_creator", description="Роль для выполнения задачи")
@@ -54,7 +54,7 @@
 
     def signal_handler(self, sig, frame):
         """Обработчик сигнала завершения работы программы через CTRL+C."""
-        logger.info("\nПрограмма завершена пользователем.")
+        logger.info('Программа завершена пользователем.')
         sys.exit(0)
 
 
@@ -62,11 +62,14 @@
         """Выполняет инициализацию после создания объекта."""
         super().__init__()
         pprint('CodeAssistant инициализирован',text_color='gray',bg_color='white')
-        self._payload()
-
-
-    def _payload(self) -> bool:
+        self._load_settings_and_models()
+
+
+    def _load_settings_and_models(self) -> bool:
         """Загружает настройки и инициализирует модели."""
+        """
+        Загружает настройки из settings.json,
+        инициализирует модели Gemini и OpenAI.
+        """
         try:
             # Загружаем настройки из файла `settings.json`
             settings_path = Path('settings.json')
@@ -75,8 +78,7 @@
             # Получаем аргументы командной строки
             cli_args = self.parse_args()
 
-            # Устанавливаем параметры: сначала значения из файла, затем перезаписываем аргументами из командной строки
-            self.role = cli_args['role'] if cli_args.get('role') else settings.get('role', 'code_checker')
+            # Приоритет аргументов командной строки выше значений из файла
             self.lang = cli_args['lang'] if cli_args.get('lang') else settings.get('lang', 'ru')
             self.model = cli_args['model'] if cli_args.get('model') else settings.get('model', ['gemini'])
             self.start_dirs = cli_args['start_dirs'] if cli_args.get('start_dirs') else \
@@ -93,8 +95,13 @@
             self.base_path = Path(settings.get('base_path', str(self.base_path)))
 
         except Exception as ex:
-            logger.error('Ошибка инициализации', ex)
+            logger.error('Ошибка загрузки настроек или инициализации моделей:', exc_info=True)
             return False
+
+        # Проверяем, что модель выбрана
+        if not self.model:
+            logger.error("Ошибка: не выбрана ни одна модель.")
+            return False
 
         return self.initialize_models()
 
@@ -105,7 +112,7 @@
         try:
             system_instruction_file = Path(gs.path.src / 'ai' / 'prompts' / 'developer' / f'{self.role}_{self.lang}.md')
             system_instruction = read_text_file(system_instruction_file)
-            return system_instruction
+            return system_instruction if system_instruction else False
         except Exception as ex:
             logger.error(f"Error reading instruction file:\n{system_instruction_file=}")
             return False    
@@ -115,7 +122,7 @@
         try:
             code_instruction_file = Path(self.base_path / 'instructions' / f'instruction_{self.role}_{self.lang}.md')
             code_instruction = read_text_file( code_instruction_file)
-            return code_instruction
+            return code_instruction if code_instruction else False
         except Exception as ex:
             logger.error(f"Error reading instruction file:\n{code_instruction_file=}")
             return False
@@ -157,7 +164,7 @@
         """Создание запроса с учетом роли и языка."""
         roles_translations: SimpleNamespace = getattr(translations.roles, self.role)
         role_description: str = getattr(roles_translations, self.lang)
-        code_instruction = self.code_instruction
+        code_instruction = self.code_instruction or ''  # Обработка пустых инструкций
         content_request = f"""Твоя специализация: `{role_description}`.\nИнструкция  для кода: ```{code_instruction}```\n Код:\n\n```{content}```\n"""
         return content_request
 
@@ -212,12 +219,11 @@
         pprint(f'Processed file number: {i + 1}', text_color='yellow')
         time.sleep(120)  # Пауза между запросами для избежания перегрузки
 
-    def yield_files_content(
+    def _yield_files_content(
         self,
         start_dirs: List[Path] = [gs.path.src],
         patterns: List[str] = ['*.py', 'README.MD', 'INTRO.MD', 'README.RU.MD', 'INTRO.RU.MD', 'README.EN.MD', 'INTRO.EN.MD']
     ) -> Iterator[tuple[Path, str]]:
-        """Генерирует пути файлов и их содержимое по указанным шаблонам.
 
         Args:
             start_dirs (List[Path]): Список начальных директорий для поиска файлов.
@@ -238,6 +244,7 @@
                         continue
                     # Проверка на наличие файла в списке исключаемых файлов
                     if str(file_path) in self.exclude_files:
+                        
                         pprint(f'Пропускаю исключенный файл: {file_path}', text_color='cyan')
                         continue
                     try:
@@ -247,10 +254,10 @@
                     except Exception as ex:
                         pprint(f'Ошибка при чтении файла: {ex}', text_color='red', bg_color='light_grey' )
                         yield None, None
-
-    def save_response(self, file_path: Path, response: str, model_name: str):
+    
+    def _save_response(self, file_path: Path, response: str, model_name: str):
         """Сохранение ответа модели в файл."""
-        output_directory: str = getattr(self.settings.output_directory, self.role)  
+        output_directory = getattr(self.settings, 'output_directory', {}).get(self.role) or 'default'  
         print(f'{file_path=}')
         target_dir = 'docs/' + output_directory.replace("<model>", model_name).replace("<lang>", self.lang)
         print(f'{target_dir=}')
@@ -269,7 +276,7 @@
     def parse_args(self):
         """Обработка аргументов командной строки."""
         parser = argparse.ArgumentParser(description='Code Assistant: обучение модели на основе кода.')
-        parser.add_argument('--role', type=str, help='Роль для выполнения задачи')
+        parser.add_argument('--role', type=str, help='Роль для выполнения задачи (Например: code_checker)')
         parser.add_argument('--lang', type=str, help='Язык выполнения')
         parser.add_argument('--models', type=str, nargs='+', help='Список моделей для инициализации')
         parser.add_argument('--start_dirs', type=Path, nargs='+', help='Список стартовых директорий')
@@ -283,9 +290,9 @@
             'model': args.models,
             'start_dirs': args.start_dirs
         }
-        pprint(f'{cli_args=}')
+        # pprint(f'{cli_args=}')  # Для отладки
         return cli_args
-
+    
     def run(self):
         """Запуск ассистента для обработки файлов."""
         signal.signal(signal.SIGINT, self.signal_handler)
@@ -293,7 +300,7 @@
         # Выполняем _payload после парсинга аргументов
         if not self._load_settings_and_models():
             logger.error('Ошибка при инициализации _payload()')
-            return
+            return  # Прекращение работы
     
         # Запускаем обработку файлов
         self.process_files()

```