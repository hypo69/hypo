Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код импортирует необходимые библиотеки для синтеза речи с использованием Google Text-to-Speech (TTS). Он определяет класс `TTS`, который инициализирует синтезатор речи и предоставляет методы для его использования.  Код также устанавливает глобальную переменную `MODE`, имеющую значение 'dev'.

Шаги выполнения
-------------------------
1. Импортируются необходимые библиотеки: `header`, `attr`, `pyttsx3`, и `gtts`.
2. Определяется глобальная константа `MODE` со значением 'dev'.
3. Определяется класс `TTS`, который инициализирует синтезатор речи `pyttsx3.init()`.
4.  Класс `TTS` получает список доступных голосов (`voices`) из синтезатора речи и выводит их в консоль.
5. Создается экземпляр класса `TTS` и сохраняется в переменной `_tts`.
6. Дальнейшие методы класса `TTS` (представленные как `...`) предполагаются, но не определены в данном фрагменте кода.

Пример использования
-------------------------
.. code-block:: python

    from hypotez.src.goog.text_to_speech import TTS

    # Инициализируем синтезатор речи
    tts_instance = TTS()

    # (Здесь вы могли бы добавить код, который вызывал бы методы класса TTS для выполнения синтеза речи,
    # например, для конвертации текста в звук.)