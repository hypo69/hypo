## <алгоритм>

**Блок-схема работы конвертера HTML в Markdown:**

1.  **Инициализация:**
    *   Устанавливаются глобальные настройки, такие как ширина строки `BODY_WIDTH`, отступы для списков `GOOGLE_LIST_INDENT`, и флаги для обработки ссылок и изображений.
    *   Создается экземпляр класса `_html2text`, который наследуется от `HTMLParser.HTMLParser`.
    *   В конструкторе устанавливаются начальные значения переменных, которые используются для отслеживания состояния обработки HTML, таких как уровень вложенности списков (`self.list`), кавычек (`self.blockquote`), и кода (`self.code`, `self.pre`).
    *   Инициализируется `self.outtextlist` – список для хранения обработанных фрагментов текста, и `self.outtext` как строка.
    *   При необходимости (если `options.google_doc` равен `True`) удаляется символ неразрывного пробела `&nbsp;` из словаря `unifiable_n` и заменяется на плейсхолдер.

2.  **Разбор HTML:**
    *   Метод `feed(data)` класса `_html2text` вызывается для обработки HTML-кода.
    *   Метод `feed` заменяет закрывающие теги `</script>` на `</ignore>`, чтобы предотвратить их интерпретацию как теги.
    *   HTML-код передается в базовый класс `HTMLParser.HTMLParser` для разбора.

3.  **Обработка HTML-тегов:**
    *   Методы `handle_starttag(tag, attrs)` и `handle_endtag(tag)` вызываются парсером при нахождении открывающих и закрывающих тегов соответственно.
    *   Метод `handle_tag` обрабатывает оба типа тегов (начальные и конечные).
    *   В `handle_tag`:
        *   Для google doc: вычисляется стиль текущего элемента, используя родительские стили и стили, заданные в атрибутах (`class`, `style`).
        *   Для заголовков (`h1`-`h9`): добавляются символы `#` в начале строки.
        *   Для `<p>` и `<div>`: добавляются пустые строки.
        *   Для `<br>`: добавляется два пробела и символ новой строки.
        *   Для `<hr>`: добавляется строка `* * *`.
        *   Для `head`, `style`, `script`: включается/выключается тихий режим, чтобы игнорировать содержимое этих тегов.
        *   Для `blockquote`: добавляется символ `>` в начале строки.
        *   Для `em`, `i`, `u`: добавляется символ `_`.
        *   Для `strong`, `b`: добавляется `**`.
        *   Для `del`, `strike`: добавляется `<del>` и `</del>`.
        *   Для `code`: добавляется символ `` ` ``.
        *   Для `abbr`: сохраняется определение аббревиатуры.
        *   Для `a`: обрабатываются ссылки, добавляются `[]` для текста ссылки и `()` или `[]` для URL.
        *   Для `img`: обрабатываются изображения, добавляются `![]` для отображения изображения.
        *   Для `dl`, `dt`, `dd`: добавляется разметка для списков определений.
        *   Для `ol`, `ul`: обрабатываются списки.
        *   Для `li`: добавляется маркер списка (`*` или `-` для `ul`, или номер для `ol`).
        *   Для `table`, `tr`, `td`: добавляются пустые строки для табличной разметки.
        *   Для `pre`: включается/выключается режим сохранения пробелов и переносов.

4.  **Обработка текста:**
    *   Метод `handle_data(data)` вызывается парсером для обработки текстового содержимого HTML.
    *   `handle_data` вызывает `self.o(data, 1)`, который добавляет текст в список `self.outtextlist` с применением необходимого форматирования.
    *   Если идет разбор `style`, то разбирается css.

5.  **Форматирование вывода:**
    *   Метод `o(data, puredata=0, force=0)` добавляет данные в список `self.outtextlist`, применяя форматирование в зависимости от контекста.
        *   В начале может добавлять отступы для цитат (`>`) и кода (`    `).
        *   Обрабатывает начальные пробелы в зависимости от настроек google doc.
        *   Обрабатывает переносы строк в зависимости от контекста.
        *   Добавляет ссылки в конце каждого параграфа или в конце документа.
        *   Добавляет определения для аббревиатур в конце документа.
    *   Метод `p()` добавляет две пустые строки, `pbr()` добавляет одну пустую строку, `soft_br` добавляет одну строку и устанавливает переключатель для мягкого переноса.

6.  **Завершение:**
    *   После завершения разбора, метод `close()` вызывается.
    *   В `close()`: вызывается `pbr()` для добавления пустой строки в конце, `o` с `force="end"` для добавления финальных переносов строк, и ссылок с аббревиатурами.
    *   Содержимое списка `self.outtextlist` объединяется в строку `self.outtext`.
    *   `&nbsp_place_holder;` заменяется на пробел, если `options.google_doc` равен `True`.
    *   Возвращается отформатированный текст.

7.  **Финальная обработка:**
    *   Функция `optwrap(text)` оборачивает текст в соответствии с заданной шириной строки `BODY_WIDTH`.

8.  **Вывод:**
    *   Функция `html2text` преобразует HTML в текст и применяет форматирование, возвращая результирующий markdown.
    *   Функция `html2text_file` аналогична, но не вызывает `optwrap`.
    *   Функция `wrapwrite` выводит текст в `sys.stdout`, обрабатывая ошибки кодировки.

**Примеры:**

*   **Инициализация**: `_html2text(out=None, baseurl='http://example.com')` создаёт объект для конвертации,  `baseurl` используется для преобразования относительных URL в абсолютные.
*   **Разбор HTML**: `h.feed("<p>Hello <b>world</b>!</p>")` передаёт HTML для разбора.
*   **Обработка тегов**: `handle_tag("p", {}, 1)` обрабатывает начало параграфа, `handle_tag("b", {}, 1)` обрабатывает начало выделения, `handle_tag("b", {}, 0)` обрабатывает конец выделения.
*   **Обработка текста**: `handle_data("Hello ")` добавляет текст `Hello ` в буфер.
*   **Форматирование вывода**: `o("world", 1)` добавляет текст `world` в буфер,  `o("\n", force=1)` добавляет принудительный перенос строки.
*   **Завершение**: `h.close()` возвращает строку markdown.
*   **Финальная обработка**: `optwrap(text)` оборачивает текст по ширине.

## <mermaid>

```mermaid
graph LR
    A[Начало] --> B(Инициализация);
    B --> C{Разбор HTML};
    C -->|Начальный тег| D[handle_starttag];
    C -->|Конечный тег| E[handle_endtag];
    C -->|Текст| F[handle_data];
    D --> G[handle_tag];
    E --> G;
    G --> H{Тег};
    H -- "h1-h9" --> I[Обработка заголовка];
    H -- "p, div" --> J[Обработка параграфа];
    H -- "br" --> K[Обработка разрыва];
    H -- "hr" --> L[Обработка разделителя];
    H -- "head, style, script" --> M[Управление тихим режимом];
    H -- "blockquote" --> N[Обработка цитаты];
     H -- "em, i, u, strong, b, del, strike, code" --> O[Обработка форматирования текста];
    H -- "abbr" --> P[Обработка аббревиатуры];
    H -- "a" --> Q[Обработка ссылки];
    H -- "img" --> R[Обработка изображения];
   H -- "dl, dt, dd" --> S[Обработка списков определений];
   H -- "ol, ul" --> T[Обработка списков];
    H -- "li" --> U[Обработка элемента списка];
    H -- "table, tr, td" --> V[Обработка таблицы];
    H -- "pre" --> W[Обработка форматированного текста];
    I --> X(o);
    J --> X;
    K --> X;
    L --> X;
     M --> X;
    N --> X;
     O --> X;
    P --> X;
   Q --> X;
    R --> X;
    S --> X;
   T --> X;
    U --> X;
    V --> X;
   W --> X;
   F --> Y[o];
    X --> C;
    Y --> C;
    C --> Z{Конец разбора};
    Z --> AA[close()];
    AA --> BB[optwrap()];
    BB --> CC(Вывод);
    
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#ccf,stroke:#333,stroke-width:2px
    style H fill:#ccf,stroke:#333,stroke-width:2px
    style X fill:#ccf,stroke:#333,stroke-width:2px
    style Y fill:#ccf,stroke:#333,stroke-width:2px
```

**Анализ зависимостей:**

*   **Инициализация (`B`)**: Устанавливает начальное состояние конвертера, включая параметры форматирования и переменные состояния.
*   **Разбор HTML (`C`)**:  Зависит от методов `handle_starttag`, `handle_endtag`, и `handle_data`, которые обрабатывают различные части HTML-документа.
*   **Обработка тегов (`D`, `E`, `G`):**  Зависит от типа тега и атрибутов, и вызывает функции обработки для соответствующих тегов.
*   **Обработка текста (`F`):** Зависит от текстового содержимого HTML, вызывает функцию `o`, которая добавляет форматирование.
*   **Форматированный вывод (`X`):** Зависит от всех обработчиков тегов, управляет выводом текста и формирует markdown.
*  **Функции `o`, `p`, `pbr`(`X`, `Y`):** Зависят от состояния конвертера, управляют добавлением текста, переносов строк, отступов.
*   **Завершение разбора (`Z`)**:  Зависит от завершения обработки всех HTML-тегов и текста, формирует итоговый markdown.
*  **Завершение (`AA`):**  Зависит от разбора html, формирует финальный текст, вызывает `optwrap` для обертки строк.
*  **Оборачивание текста (`BB`):**  Зависит от финального текста, обертывает текст в соответствии с заданной шириной.
*   **Вывод (`CC`):**  Зависит от обернутого текста, выводит текст в stdout.

## <объяснение>

**Импорты:**

*   `html.entities as htmlentitydefs`: Предоставляет определения HTML-сущностей (например, `&amp;`, `&nbsp;`). Используется для преобразования HTML-сущностей в соответствующие символы. Внутри пакета `src` не используется.
*   `urllib.parse as urlparse`: Используется для парсинга и объединения URL. Внутри пакета `src` не используется.
*   `html.parser as HTMLParser`: Предоставляет базовый класс `HTMLParser` для разбора HTML. Внутри пакета `src` не используется.
*   `urllib.request as urllib`: Используется для загрузки данных по URL. Внутри пакета `src` не используется.
*   `optparse`:  Используется для парсинга аргументов командной строки. Внутри пакета `src` не используется.
*   `re`: Используется для работы с регулярными выражениями, в основном для замены HTML сущностей и удаления лишних пробелов. Внутри пакета `src` не используется.
*   `sys`: Предоставляет доступ к системным переменным и функциям, используется для чтения из stdin и записи в stdout. Внутри пакета `src` не используется.
*   `codecs`: Используется для кодирования и декодирования текста, в частности для обработки HTML-сущностей. Внутри пакета `src` не используется.
*   `types`: Не используется в данном коде, возможно, остался от предыдущих версий.
*   `textwrap.wrap`: Используется для переноса длинных строк. Внутри пакета `src` не используется.
*   `chardet.detect`: Используется для определения кодировки HTML-страницы. Внутри пакета `src` не используется.
*   `feedparser._getCharacterEncoding`: Используется для определения кодировки HTML-страницы, полученной по http. Внутри пакета `src` не используется.

**Классы:**

*   `_html2text(HTMLParser.HTMLParser)`: Основной класс конвертера, наследуется от `HTMLParser.HTMLParser`.
    *   `__init__(self, out=None, baseurl='')`:
        *   Инициализирует состояние парсера. `out` - функция для вывода, по умолчанию используется `self.outtextf`, `baseurl` - базовый URL для обработки ссылок.
        *   `self.outtextlist`: Список для хранения выводимых символов, которые будут объединены в строку.
        *   `self.outtext`: Итоговая строка markdown.
        *   `self.quiet`: Счетчик для игнорирования содержимого тегов.
        *   `self.p_p`: Счетчик для добавления пустых строк.
        *   `self.outcount`: Счетчик для вывода ссылок.
        *   `self.start`: Флаг для обработки начала документа.
        *   `self.space`: Флаг для добавления пробела.
        *   `self.a`: Список ссылок.
        *   `self.astack`: Стек ссылок.
        *   `self.acount`: Счетчик ссылок.
        *   `self.list`: Стек списков.
        *   `self.blockquote`: Уровень вложенности цитат.
        *   `self.pre`: Флаг для тега `<pre>`.
        *   `self.startpre`: Флаг для начала тега `<pre>`.
        *   `self.code`: Флаг для тега `<code>`.
        *   `self.br_toggle`:  Флаг для управления переносом строк.
        *   `self.lastWasNL`:  Флаг для проверки последнего символа на перенос строки.
        *   `self.lastWasList`: Флаг для проверки последнего элемента на список.
        *   `self.style`: Счетчик для определения нахождения внутри тега style.
        *   `self.style_def`: Словарь для хранения стилей css.
        *   `self.tag_stack`: Стек тегов для google docs.
        *   `self.emphasis`: Счетчик для жирного и курсивного текста.
        *   `self.drop_white_space`: Флаг для отбрасывания лишних пробелов в тексте.
        *   `self.inheader`: Флаг для проверки нахождения внутри тега заголовка.
        *   `self.abbr_title`: Заголовок текущей аббревиатуры.
        *   `self.abbr_data`: Данные текущей аббревиатуры.
        *   `self.abbr_list`: Список аббревиатур.
        *   `self.baseurl`: Базовый URL.

    *   `feed(self, data)`: Обрабатывает HTML-код.
    *   `outtextf(self, s)`: Добавляет текст в `self.outtextlist`.
    *   `close(self)`: Завершает разбор и возвращает отформатированный текст.
    *   `handle_charref(self, c)`: Обрабатывает числовые HTML-сущности.
    *   `handle_entityref(self, c)`: Обрабатывает именованные HTML-сущности.
    *   `handle_starttag(self, tag, attrs)`: Обрабатывает открывающие теги.
    *   `handle_endtag(self, tag)`: Обрабатывает закрывающие теги.
    *   `previousIndex(self, attrs)`: Возвращает индекс ссылки в списке `self.a`.
    *   `drop_last(self, nLetters)`: Удаляет последние n символов из вывода.
    *    `handle_emphasis(self, start, tag_style, parent_style)`: Обрабатывает форматирование текста.
    *   `handle_tag(self, tag, attrs, start)`: Основная функция для обработки HTML-тегов.
    *   `pbr(self)`: Добавляет одну пустую строку.
    *   `p(self)`: Добавляет две пустые строки.
    *   `soft_br(self)`: Добавляет мягкий перенос строки.
    *   `o(self, data, puredata=0, force=0)`: Добавляет текст в вывод, применяет форматирование.
    *   `handle_data(self, data)`: Обрабатывает текстовое содержимое HTML.
    *   `unknown_decl(self, data)`: Пустая функция для обработки неизвестных деклараций.

*   `Storage`: Пустой класс для хранения настроек.

**Функции:**

*   `has_key(x, y)`: Проверяет наличие ключа в словаре или атрибута у объекта.
*   `name2cp(k)`: Преобразует имя HTML-сущности в код символа.
*   `charref(name)`: Преобразует числовую HTML-сущность в символ.
*   `entityref(c)`: Преобразует именованную HTML-сущность в символ.
*   `replaceEntities(s)`: Функция для замены HTML-сущности на символ.
*   `unescape(s)`:  Заменяет все HTML-сущности в строке.
*   `onlywhite(line)`: Проверяет, состоит ли строка только из пробельных символов.
*   `optwrap(text)`: Оборачивает текст по ширине.
*  `hn(tag)`: Возвращает уровень заголовка из тега.
*   `dumb_property_dict(style)`: Разбирает строку CSS-стилей в словарь.
*   `dumb_css_parser(data)`: Разбирает CSS-код в словарь селекторов и их стилей.
*   `element_style(attrs, style_def, parent_style)`: Вычисляет финальные стили элемента, учитывая стили родителя.
*   `google_list_style(style)`: Определяет тип списка (ul или ol) на основе стилей Google Docs.
*   `google_nest_count(style)`: Определяет уровень вложенности списка на основе стилей Google Docs.
*    `google_has_height(style)`: Проверяет наличие высоты в стилях.
*    `google_text_emphasis(style)`: Возвращает список стилей для форматирования текста.
*  `google_fixed_width_font(style)`: Проверяет, использует ли элемент шрифт фиксированной ширины.
*   `list_numbering_start(attrs)`: Извлекает номер начала списка из атрибутов.
*   `wrapwrite(text)`: Выводит текст в stdout.
*   `html2text_file(html, out=wrapwrite, baseurl='')`: Преобразует HTML в текст, не применяя обертывание.
*   `html2text(html, baseurl='')`: Преобразует HTML в текст и применяет обертывание.

**Переменные:**

*   `MODE`: Указывает режим работы (в коде не используется).
*   `__version__`, `__author__`, `__copyright__`, `__contributors__`: Метаданные.
*   `UNICODE_SNOB`: Флаг для использования Unicode-символов.
*   `LINKS_EACH_PARAGRAPH`: Флаг для размещения ссылок после каждого параграфа.
*   `BODY_WIDTH`: Ширина строки для обертывания текста.
*   `SKIP_INTERNAL_LINKS`: Флаг для пропуска внутренних ссылок.
*   `INLINE_LINKS`: Флаг для использования инлайн-ссылок.
*   `GOOGLE_LIST_INDENT`: Отступ для списков Google Docs.
*   `IGNORE_ANCHORS`: Флаг для игнорирования ссылок.
*   `IGNORE_IMAGES`: Флаг для игнорирования изображений.
*   `unifiable`: Словарь HTML-сущностей для замены.
*   `unifiable_n`: Словарь HTML-сущностей с числовыми кодами для замены.
*    `r_unescape`: Регулярное выражение для поиска HTML-сущностей.
*   `options`: Объект `Storage`, содержащий настройки программы.

**Потенциальные ошибки и улучшения:**

*   Обработка таблиц минимальна.
*   Поддержка CSS ограничена.
*   Не обрабатывает все HTML-сущности.
*   Код может быть сложным для понимания из-за большого количества переменных состояния.
*   Не хватает модульного тестирования.

**Цепочка взаимосвязей с другими частями проекта:**

*   Этот модуль является утилитой, и, вероятно, используется другими модулями для преобразования HTML в Markdown. Он может быть частью модуля, который генерирует документацию или преобразует контент. Он может быть вызван из любого места в коде, где необходимо преобразовать HTML в текст.

**Дополнительно:**

*   Код использует глобальные переменные для настроек, что может затруднить рефакторинг.
*   Класс `_html2text` имеет много атрибутов, что может сделать его сложным в понимании.
*   Много специфических проверок на "google doc", которые, возможно, стоит вынести в отдельную функцию.
*   Стоит добавить тесты для более полной проверки функциональности.