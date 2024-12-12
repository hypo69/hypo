## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    -   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    -   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    -   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    -   **Переменные**: Их типы и использование.
    -   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

### <алгоритм>
1.  **Инициализация и настройка окружения:**
    *   Код начинается с определения глобальных объектов и функций, которые будут использоваться на протяжении всего скрипта.
    *   Происходит определение совместимости с ES6 символами.
    *   Создается объект `ea`, который будет использоваться для хранения глобальных переменных.
    *   Определяются вспомогательные функции для работы с массивами, строками, объектами и т.д.
        *   Например, `ia` для безопасного задания свойств объектов, `xa` для удаления пробелов, `ya` для сравнения версий, и т.д.
    *   Настраиваются параметры для сбора информации об окружении (браузер, ОС).
    
2.  **Работа с флагами и настройками:**
    *   Функции `ja` и `ka` используются для получения значений флагов, которые могут влиять на поведение кода.
    *   Определяются различные константы и переменные на основе полученных флагов.
    *   Например, `Aa`, `Ba`, `Ca`, `Da`, `Ea` – флаги, определяющие поведение кода в разных условиях.
        
3.  **Обработка строк и кодирование:**
    *   Определяются функции для сравнения строк (`ya`, `za`), поиска подстрок (`Qa`), фильтрации массивов (`Ra`), маппинга (`Sa`), проверки наличия элемента в массиве (`Ta`), поиска последнего индекса (`Ua`), проверки вхождения подстроки (`Va`).
    *   Функция `ab` и `bb` используются для декодирования base64 строк.
    *   Инициализируется алфавит для декодирования base64 через функцию `cb`.
    
4.  **Работа с числами и битами:**
    *   Функции `fb` и `hb` служат для преобразования целых чисел в 64-битные представления.
    *   Функция `jb` преобразует 64-битное представление в строку.
    *   Функция `Sb` для округления чисел до целого, а `Tb` преобразует число в строку безопасно.
    
5.  **Работа с объектами и типами данных:**
    *   Определяется ряд функций для работы с объектами:
        *   `ub`, `vb` – проверки на тип объекта.
        *   `wb` - проверка массива
        *   `pb`, `qb`, `rb` – для управления флагами объектов.
    *   `zb` проверяет флаги объекта
    *   Определены константы `Ab`, `Bb`, `Cb`
    *   Функции для вызова ошибок `Fb`, `Gb`
    *   `Cb` задает контекст ошибки, `Hb` бросает ошибку, `Ib` бросает предупреждение.
    *   Определяются функции для валидации типов `Jb`, `Lb`, `w`, `Mb`, `Nb`, `Ob`, `Pb`, `Qb`, `Rb` , `Vb`, `Wb`, `Xb` .
    *    Функции `Sb` и `Ub` служат для безопасного преобразования чисел в строку
    
6.  **Работа со структурированными данными:**
    *  Определяются функции для работы с массивами, объектами, Uint8Array:
        * `Yb`, `$b` - создание объектов
        * `bc` - создает новый объект с заданной структурой
        * `cc`, `dc` - преобразования в различные форматы
        * `ec` - применяет функцию к каждому элементу массива
        * `fc`, `gc` - рекурсивное преобразование
        * `hc`, `ic` - методы для JSON, бинарных данных.
        * `jc` - клонирование объекта
        * `kc`, `lc`, `mc` - работа с флагами объектов.
    *   Определяется механизм для создания прокси-объектов `nc`, `pc`, `qc`.
    *   Функции `sc`, `tc` и `uc` служат для работы со значениями по смещению.
    *   Функции `y` и `z` служат для изменения значений у объектов по ключу и добавляют флаги.
    *   Функции `wc` и `A` служат для извлечения значений.
    *   Функции `yc`, `zc`, `Bc`, `Cc`, `Ec`, `B`, `Fc`, `Gc`, `Jc`, `Kc`, `Hc`, `Ic`, `Lc`, `xc`, `Mc`, `D`, `E`, `Oc`, `Pc`, `Qc`, `Ac`, `Dc`, `Rc`, `Sc`, `Uc`, `Vc`, `F`, `G`, `H`, `Wc`, `Xc`, `Yc`, `I`, `J`, `Zc`, `$c`, `ad`, `K`, `bd`, `cd` - функции для работы с объектами.
    
7.  **Классы для работы со структурированными данными:**
    *   Определяется класс `M`, базовый класс для работы с данными
    *   Функции `ed`, `fd` служат для работы с экземплярами класса `M`.
    *   Функции `gd` служит для проверки валидации.
    
8.  **Работа с функциями и событиями:**
    *   Определяются функции для управления событиями `qd`, `rd`, `sd`, `td`, `ud`, `vd`, `pd`, `od`.
    *   Функции `ra`, `sa` и `ta` служат для привязки контекста.
    
9.  **Работа с URL:**
    *   Определяется класс `xd` для работы с URL.
    *   Функции `yd`, `Ad`, `Bd`, `Cd` служат для безопасной работы с URL.
    *   Функция `Ed` используется для создания URL.
    
10. **Работа с размерами и стилями:**
    *   Определяется класс `Fd` для работы с размерами.
    *   Функции `Hd`, `Id` и `Jd` служат для работы с DOM.
    *   Функции `Kd` и `Ld` для определения типа устройства.
    *   Функции `Od` для работы с параметрами URL.
    *   Функции `Rd` служат для вставки скриптов в DOM.
    *    Функции `Td` для получения стилей элементов, `Ud` для генерации случайных чисел, `Vd` для работы с объектами.
    *   Функция `Wd` для вычисления hash строк, `Xd`, `Yd`, `Zd` и `$d` служат для работы с CSS.
    *   Функция `ae` проверяет тип устройства, `be` - скрывает элемент, `de` для работы с очередью задач.
    *  Функция `ee` вставляет origin-trial metatag
    *  Функции `he` и `ie` для работы с уникальными id
    *  Функция `ke` и `le` для асинхронной загрузки картинок.
    *  Функция `ne` выполняет GET запрос.
    
11. **Работа с куки и хранилищем:**
    *   Определяется класс `qe` для работы с куками.
    *   Функции `re`, `se` служат для работы с localStorage.
    
12. **Работа с логами:**
     *   Функция `ue` используется для отправки логов.
     *  Функция `ve` и `we` для получения контекста страницы
     *   Функции `xe` и `ye` генерирует id.
     *   Функция `ze` определяет standalone
     *   Функция `Ae` нормализует название клиента.
     *   Класс `Be` служит для управления ошибками.
     *    Класс `Ee` и `Fe` служат для работы с URL, `Ge` и `He` для работы с hash
    *  Функции `Ie` и `Je` служат для получения текущего времени
    *   Класс `Ke` - данные о тайминге.
    *   Класс `Qe` - механизм сбора таймингов.
    *   Функции `Oe` и `Pe` очищают тайминги.
    *   Функции `Re`, `Se`, `Te` для работы с параметрами URL.
    *   Функция `Ue` и `Ve` для создания URL.
    *   Класс `We` для работы с параметрами URL.
    *   Функция `Xe` форматирует стек ошибок.
    *  Класс `Ze` для обработки ошибок, `ck` для отправки данных на сервер.

13. **Различные классы для обработки данных:**
    *  Классы `$e`, `af`, `bf`, `df`, `ef`, `ff`, `gf` и `hf` - для структур данных.
    *  Функции `jf` и `kf` используются для обработки данных в разных форматах.
    *   Функция `lf` - для управления логикой.
    *  Классы `Nc`, `mf`, `nf`, `of`, `pf`, `qf`, `tf`, `uf`, `vf`, `wf`, `xf`, `yf`, `Af`, `Bf`, `Cf`, `Df`, `Ef`, `Ff`, `Gf`, `If`, `Jf`, `Kf`, `Lf`, `Mf`, `Tf`, `Uf`, `Yf`, `$f`, `ag`, `bg`, `cg`, `eg`.

14. **Механизм отправки данных:**
     *  Класс `jg`, `kg` и `gg` служат для отправки данных на сервер.
     *  Класс `ng` и `og` - для управления запросами.
     *  Функция `lg` служит для отправки логов на сервер.

15.  **Сбор данных и логика обработки:**
     *  Классы `tg` и `N`, `ug`, `Ag` - для управлении состояниями, хранение настроек.
     *  Функции `wg`, `xg`, `yg`, `zg`, `Cg`, `Dg`, `Gg`, `Hg`, `Ig`, `Jg`, `Bg`, `Kg`, `Lg`, `Mg`, `Ng`, `Og`, `P`, `Pg`, `Qg`, `Rg`, `Sg`, `Tg`, `Ug`, `Ye`, `Vg`, `Wg`, `Xg`, `Yg` и `Zg` служат для работы с конфигурацией и определения условий.

16.  **Работа с Promise:**
    *   Определяется класс `eh` и `ch` для управления Promise.
    *   Функция `dh` для управления состоянием Promise
    *   Определяется класс `fh` - для работы с массивами.
    *   Функция `gh` для перебора массива.

17. **Работа с Map:**
    *   Определяется класс `ih` и `rh` - для управления Map.
    *   Функция `hh` - для работы с ключами Map.
    
18.  **Работа с значениями:**
    *    Функции `jh`, `lh`, `mh`, `nh`, `oh` и `ph` служат для работы с значениями.
    *    Определяется класс `kh` - контейнер для значений
    
19.  **Работа с наборами:**
     *   Определяется класс `qh` для работы с наборами.
    
20. **Сбор и обработка ошибок:**
    *   Определяется класс `Q` и `sh` для работы с ошибками.
    *   Функции `uh`, `th`, `vh`, `Ah`, `xh`, `zh`, `Ah`, `yh` служат для работы с ошибками.
    *   Определяются классы `Ch`, `Dh`, `Eh`, `Fh`, `Gh`, `Hh`, `R`, `Jh`, `Kh`, `$h`, `fe`, `Fi`  –  для работы с данными и для параметров логирования.
    *   Функция `S`, `T`, `Gi` – для получения конфигураций
   
21. **Работа с DOM:**
    *   Функции `Hi`, `Ii`, `Ji`, `Ki` служат для работы с DOM.
    *   Классы `Li` и `Mi` - для работы с разными типами объявлений.
    *  Функции `Ni`, `U`, `Oi`, `Pi`, `Qi`, `Ri`, `Si`, `Ti`, `Ui`, `Vi`, `Wi`, `Xi`, `Yi`.
    
22. **Обработка размеров и позиционирования:**
    *  Классы `Zi`, `Y`, `Y`, `lo`, `qo` и `so` - для управления размерами и позиционированием элементов
    * Функции `bj`, `ej`, `fj`, `cj`, `gj`, `dj`, `eo`, `go`, `ho` служат для работы с размерами элементов.
    * Функции `mo`, `po`, `no`, `oo`, `to`, `uo`, `vo` для определения размеров, логики позиционирования.
     * Функция `no` проверяет ширину элемента.
     * Функция `oo` устанавливает значение атрибутов.
    
23. **Настройки для объявлений:**
    *   Определяются различные константы и переменные для работы с настройками объявлений, включая `hj`, `ij`, `jj`.
    *   Классы `kj`, `lj`, `mj`, `nj`, `oj`, `pj`, `qj`, `rj`, `sj`, `tj`, `vj`, `wj`, `xj`, `yj` - для описания структуры данных объявлений.
    *   Функции `zj`, `Aj`, `Bj`, `Cj`, `Dj` и класс `Ej` для работы с текстовым контентом.

24. **Работа с обработкой ошибок (Fj):**
    *   Класс `Fj` используется для обработки ошибок в JavaScript.
    *   Функции `T`, `ha`, `sa` и `da` используются для обработки ошибок и отправки сообщений об ошибках.
    
25. **Работа с отчетами:**
   *  Функция `Gj` для сбора отчетов.
   *  Функции `Hj` и `Ij` для обертки функций.
   *  Функция `Jj` для вызова функций
   *  Функция `Kj` и классы `Q`, `sh` для работы с ID элемента
   * Функции `Lj` и `Nj` для преобразования ID.
   *  Функция `Oj` для управления состоянием.
   *  Функция `Pj` для управление параметрами.
   *  Функция `Qj` для получения идентификаторов.
    *   Функция `Rj` для перемещения по DOM дереву, `Sj`, `Uj`, `Vj`, `Tj` и `Xj` служат для сбора информации о позициях элементов.
    *   Класс `Wj` - обертка для позиций элементов
    
26. **Основная логика:**
    *   Определяются константы `Yj` и `W`.
    *    Функции `ak` для управления таймингами
    *   Класс `V` служит для обработки ошибок, `bk` и `ck` для записи логов.
    *  Функции `dk` и `ek` служат для обработки ошибок.
    
27. **Классы и функции для работы с пользовательским интерфейсом:**
    *    Класс `fk`, `lk`, `xk`, `tk`, `uk`, `yk`, `Ak`, `Ck`, `Dk`, `Gk`, `Hk`, `Ik`, `Jk`, `Kk`, `Lk`, `Mk`, `Nk`, `Ok`, `Pk`, `Qk`, `Rk`, `Sk`, `Xk`, `Tk`, `Yk`, `Uk`, `Zk`, `$k`, `al`, `Vk`, `Wk` - работа с локальным хранилищем, CMP, GDPR.
    *    Классы `bl`, `cl`, `dl`, `el`, `gl`, `hl` для управления состояниями.
    *  Функция `fl` для обработки ошибок.
    *  Функции `il`, `jl`, `kl`, `ll`, `ml` для преобразования строк.
    *   Классы `xl`, `rl`, `Cn`, `Dl`, `El`, `Fl`, `Gl`, `Hl`, `Il`, `Ll`, `Ol`, `Pl`, `Ql`, `Rl`, `Vl`.
    *   Функции `zl`, `yl`, `Al`, `Sl`
    *   Функции `Jl` и `Kl` - для работы с postMessage API
    *   Функции `Ml` и `Nl` - для работы с USP API
   
28. **Основные параметры и функции:**
    *   Определяются переменные `nl`, `ol`, `pl`
    *   Функции `ql`, `sl`, `tl`, `ul`, `vl`, `wl` для работы со строками
    *   Функция `zl` служит для декодирования данных.
    *   Классы `Vl` и `Ol` для работы с API.
    *   Функции `Al`, `Bl`, `Cl`, `Dl`, `El`, `Fl`, `Gl`, `Hl`, `Il`, `Jl` для работы с различными типами данных.
    *   Функции `Sl` для декодирования строк, `Tl` для создания iframe, `Ul`, `Wl`, `Xl` для работы с CMP.
    *   Функция `Yl` для получения данных.
    *   Функции `$l`, `Zl` и класс `Vl` служат для работы с данными.
    *  Функции `am`, `bm`, `cm`, `dm`, `em`, `fm`, `gm`, `hm` и классы `im` и `jm` служат для работы с доменом, URL.
    *   Классы `km`, `mm`, `nm`, `om`, `pm`, `rm` служат для описания структур данных.
    *   Функция `tm`, `X`, `um`, `vm`, `wm`, `xm`, `ym` и `zm` служат для управления состоянием.
    *   Функции `Am`, `Bm`, `Cm`, `Dm`, `Em`, `Fm`, `Gm`, `Hm`, `Im`, `Jm`, `Km`, `Lm`, `Mm`, `Nm`, `Om`, `Pm`, `Rm`, `Sm`, `Tm`, `Vm`, `Wm`, `Xm`, `Um` и класс `Qm` - для управления логикой.
    *  Функция `$`m для инициализации объявлений
    *  Функция `Ym` и `Zm` для логирования
    * Функции `an` и `cn` для работы с url.
    *  Классы `dn`, `en`, `fn`, `gn` служат для асинхронной работы, promise
    *   Функция `hn` - сбора параметров URL.
    *   Классы `jn` и `kn` служат для загрузки частей кода
    *   Класс `mn` и `nn` для управления состоянием глобального объекта.
    *   Функция `on` создает объект для PLA, `pn` для управления запуском механизма, `qn` - для обработки логики PLA, `rn` - обертка для инициализации.
    *   Функция `sn` и `tn` - для создания div, `un` - для получения имени лоадера, `vn` - список параметров для copy
    *   Функция `wn` и `xn` - для парсинга параметров из script тега.
    *   Функция `yn` - для работы с параметрами.
    *  Функция `zn` - для получения client id.
    *   Классы `An` и `Bn` - для определения размера
    *   Класс `Cn` для работы с версиями, `Dn`, `En`, `Fn`, `Gn`, `Hn`, `In`, `Jn`, `Kn`, `Ln`, `Mn`, `Nn`, `On`, `Pn`, `Qn` для сбора информации о браузере.
    *  Функции `Rn`, `Sn`, `Tn`, `Vn`, `Un`, `Wn`, `Xn`, `Yn`, `Zn` служат для работы с DOM и iframe.
    *   Класс `$n`, `Y` служат для управления размером, `ao`, `bo`, `co` служат для параметров объявлений.
    *   Функции `eo`, `fo`, `go`, `ho` служат для работы с параметрами объявлений.
    *   Класс `jo` - для объявления, `ko`, `lo` - для контейнера.
     *  Классы `mo`, `po`, `no`, `oo`, `qo`, `ro`, `so` - для работы с разными типами объявлений.
    *   Функция `to` для вычисления размера контейнера, `uo` для проверки условий, `vo` - для фильтрации.
     * Переменные `Z` и `wo` служат для хранения предустановленных размеров.
     * Функции `xo`, `zo`, `yo`, `Ao`, `Bo`, `Co`, `Eo`, `Do`, `Fo` для определения размера и типа объявления
    *  Функция `Jo` для создания контейнера объявлений, `Io`, `Go`, `Ko` - для управления форматом объявления.
    *   Функция `Lo` - вычисление ширины, `Mo` - нормализация типов данных.
    *   Функции `No`, `Oo`, `Po` для нормализации параметров, `Qo` - уровень вложенности.
    *    Функции `mg`, `So`, `To`, `Ro`, `Uo` - для управления таймаутами и видимостью.
    *   Класс `Vo` - для управления таймаутами.
    *    Функция `Wo` для асинхронного ожидания.
    *    Функции `Xo`, `Yo`, `Zo` для работы с ID, `$`o для проверки готовности.
    *  Функции `ap`, `cp`, `dp`, `ep`, `fp`, `gp`, `bp` для работы с логикой отчетов.
    *   Функции `hp`, `ip`, `jp`, `kp`, `lp`, `mp`, `np`, `op`, `pp`, `qp`, `rp`, `sp`, `tp` для настройки логики работы.
    *  Класс `Ap` и функции `zp`, `Bp`, `Cp`, `Dp`, `Ep`, `Fp`, `Gp` служат для управления конфигурацией
    *   Функции `Hp`, `Ip`, `Jp`, `Kp`, `Lp`, `Mp` служат для работы с ID и типами объявлений
    *    Функции `Np`, `Op` служат для получения размера экрана и работы с postMessage.
    *   Функции `Pp`, `Qp`, `Rp`, `Sp`, `Tp`, `Up`, `Xp`, `Vp`, `Yp`, `Wp`, `Zp`, `cq`, `gq`, `eq`, `fq`, `jq`, `hq`, `iq`, `kq` и класс `dq` - для сбора и обработки аналитики о загрузке объявлений.
    *  Переменные `$p`, `aq`, `bq` служат для работы с аналитикой.
    *  Функции `lq`, `mq`, `nq` для управления очередью, `pq` - проверка объявления
    *  Функции `qq`, `rq` и `sq` - управление отображением объявлений.
    *  Функции `tq`, `uq`, `wq`, `xq`, `zq` и `vq` служат для обработки данных в DOM дереве
    *   Функции `Bq`, `Cq`, `Dq`, `Fq`, `Aq` - для работы с тегами в head и body.
    *    Функции `Gq`, `yq`, `Iq`, `Mq`, `Jq`, `Kq`, `Lq`, `Oq`, `Pq`, `Qq`, `Rq`, `Eq` и `Sq` для управление объявлением, обработкой callback, загрузкой js.
    *   Функция `Hq` создает timeout.
    *  Анонимная функция в конце кода является точкой входа и инициализирует весь скрипт.

### <mermaid>

```mermaid
flowchart TD
    subgraph Initial Setup
        Start[Начало]
        InitializeGlobalObjects[Инициализация глобальных объектов и функций]
        SetCompatibility[Определение совместимости с ES6]
        CreateGlobalObject[Создание объекта ea для хранения глобальных переменных]
        DefineHelperFunctions[Определение вспомогательных функций]
        InitializeEnvironment[Настройка параметров окружения]
    end

    Start --> InitializeGlobalObjects
    InitializeGlobalObjects --> SetCompatibility
    SetCompatibility --> CreateGlobalObject
    CreateGlobalObject --> DefineHelperFunctions
    DefineHelperFunctions --> InitializeEnvironment

    subgraph Feature Flags and Config
        GetFlagValues[Получение значений флагов]
        ApplySettings[Применение настроек на основе флагов]
    end
    InitializeEnvironment --> GetFlagValues
    GetFlagValues --> ApplySettings


    subgraph String and Encoding
        StringProcessing[Обработка строк]
        Base64Decoding[Декодирование base64 строк]
        Base64EncodingSetup[Настройка алфавита base64]
    end
     ApplySettings --> StringProcessing
    StringProcessing --> Base64Decoding
    Base64Decoding --> Base64EncodingSetup

    subgraph Numerical and Bit Operations
         NumberConversion[Преобразование чисел в 64-битное представление]
        NumberToStringConversion[Преобразование чисел в строку]
        SafeIntegerConversion[Безопасное преобразование в строку и целое число]
    end
    Base64EncodingSetup --> NumberConversion
    NumberConversion --> NumberToStringConversion
    NumberToStringConversion --> SafeIntegerConversion

    subgraph Data Types and Objects
        ObjectValidation[Проверки типов объектов]
        ObjectManipulation[Управление флагами объектов]
        ErrorHandling[Обработка ошибок]
        TypeValidation[Проверка типов данных]
         ObjectCreation[Создание объектов]
    end
    SafeIntegerConversion --> ObjectValidation
    ObjectValidation --> ObjectManipulation
    ObjectManipulation --> ErrorHandling
     ErrorHandling --> TypeValidation
     TypeValidation --> ObjectCreation


    subgraph Structured Data Handling
        ArrayObjectManipulation[Работа с массивами и объектами]
        ObjectCloning[Клонирование объектов]
        FlagManagement[Управление флагами объектов]
        ProxySetup[Настройка прокси-объектов]
        OffsetValueAccess[Доступ к значениям по смещению]
        DataModification[Изменение значений объектов по ключу]
        ValueExtraction[Извлечение значений]
    end
    ObjectCreation --> ArrayObjectManipulation
    ArrayObjectManipulation --> ObjectCloning
    ObjectCloning --> FlagManagement
    FlagManagement --> ProxySetup
    ProxySetup --> OffsetValueAccess
    OffsetValueAccess --> DataModification
    DataModification --> ValueExtraction


     subgraph Core Data Classes
        DataClassDefinition[Определение класса M для работы с данными]
        InstanceHandling[Работа с экземплярами класса M]
        DataValidationClass[Работа с валидацией]
    end
    ValueExtraction --> DataClassDefinition
    DataClassDefinition --> InstanceHandling
    InstanceHandling --> DataValidationClass
    

     subgraph Event and Function Handling
        EventManagement[Управление событиями]
        ContextBinding[Привязка контекста]
    end
    DataValidationClass --> EventManagement
    EventManagement --> ContextBinding


    subgraph URL Management
        URLClassDefinition[Определение класса xd для работы с URL]
        SecureURLHandling[Безопасная работа с URL]
        URLCreation[Создание URL]
    end
    ContextBinding --> URLClassDefinition
    URLClassDefinition --> SecureURLHandling
    SecureURLHandling --> URLCreation


    subgraph Styling and DOM
       DimensionsClassDefinition[Определение класса Fd для работы с размерами]
        DOMManipulation[Работа с DOM]
        DeviceTypeDetection[Определение типа устройства]
        URLParameterHandling[Работа с параметрами URL]
        ScriptInsertion[Вставка скриптов в DOM]
        StyleExtraction[Получение стилей элементов]
        RandomNumberGeneration[Генерация случайных чисел]
        ObjectIteration[Работа с объектами]
        StringHash[Вычисление hash строк]
        CSSHandling[Работа с CSS]
        DeviceDetection[Определение типа устройства]
        QueueManagement[Управление очередью]
         OriginTrial[Вставка origin-trial metatag]
       UniqueId[Генерация уникальных ID]
       AsyncImgRequest[Асинхронный запрос]
       GETRequest[Отправка GET запроса]
    end
    URLCreation --> DimensionsClassDefinition
    DimensionsClassDefinition --> DOMManipulation
    DOMManipulation --> DeviceTypeDetection
    DeviceTypeDetection --> URLParameterHandling
    URLParameterHandling --> ScriptInsertion
    ScriptInsertion --> StyleExtraction
     StyleExtraction --> RandomNumberGeneration
     RandomNumberGeneration --> ObjectIteration
     ObjectIteration --> StringHash
     StringHash --> CSSHandling
     CSSHandling --> DeviceDetection
     DeviceDetection --> QueueManagement
     QueueManagement --> OriginTrial
     OriginTrial --> UniqueId
      UniqueId --> AsyncImgRequest
     AsyncImgRequest --> GETRequest

    subgraph Storage and Cookies
        CookieManagement[Работа с куками]
        LocalStorageHandling[Работа с localStorage]
     end
    GETRequest --> CookieManagement
    CookieManagement --> LocalStorageHandling

     subgraph Log Management
        LogSending[Отправка логов]
        ContextExtraction[Получение контекста страницы]
        IdGeneration[Генерация ID]
        StandaloneDetection[Определение standalone]
        ClientNormalization[Нормализация названия клиента]
        ErrorClassDefinition[Определение класса Be для работы с ошибками]
        URLDataExtraction[Работа с URL]
        TimeTracking[Отслеживание времени]
        TimingData[Сбор таймингов]
        ReportHandling[Сбор и отправка данных]
        StackTraceFormatting[Форматирование стека ошибок]
        ErrorProcessing[Обработка ошибок]
    end
    LocalStorageHandling --> LogSending
    LogSending --> ContextExtraction
     ContextExtraction --> IdGeneration
      IdGeneration --> StandaloneDetection
      StandaloneDetection --> ClientNormalization
     ClientNormalization --> ErrorClassDefinition
     ErrorClassDefinition --> URLDataExtraction
      URLDataExtraction --> TimeTracking
       TimeTracking --> TimingData
       TimingData --> ReportHandling
        ReportHandling --> StackTraceFormatting
        StackTraceFormatting --> ErrorProcessing

     subgraph Data Structure Classes
        DataStructureClassDefinition[Определение классов для структур данных]
        DataProcessingLogic[Реализация логики для работы со структурами данных]
    end
    ErrorProcessing --> DataStructureClassDefinition
    DataStructureClassDefinition --> DataProcessingLogic

     subgraph Data Sending Mechanism
       LogSendingClass[Определение класса для отправки данных]
       DataPreparation[Подготовка данных]
       DataSendMechanism[Механизм отправки]
    end
    DataProcessingLogic --> LogSendingClass
    LogSendingClass --> DataPreparation
    DataPreparation --> DataSendMechanism

    subgraph Configuration and Logic
        ConfigurationManagement[Управление состоянием и хранение настроек]
        ParameterNormalization[Нормализация параметров]
        LogicInitialization[Инициализация логики]
    end
     DataSendMechanism --> ConfigurationManagement
    ConfigurationManagement --> ParameterNormalization
    ParameterNormalization --> LogicInitialization

    subgraph Promises and Async
       PromiseManagement[Создание и управление Promise]
       AsyncOperations[Выполнение асинхронных операций]
    end
    LogicInitialization --> PromiseManagement
    PromiseManagement --> AsyncOperations

     subgraph Map Handling
        MapManagement[Управление Map]
         KeyHandling[Обработка ключей Map]
    end
   AsyncOperations --> MapManagement
   MapManagement --> KeyHandling

    subgraph Values Management
       ValueDefinition[Определение контейнера значений]
        ValueManipulation[Работа со значениями]
    end
    KeyHandling --> ValueDefinition
     ValueDefinition --> ValueManipulation
     
    subgraph Set Handling
         SetManagement[Работа с наборами]
    end
     ValueManipulation --> SetManagement

      subgraph Error Handling
        ErrorDefinition[Определение класса Q для работы с ошибками]
       ErrorDataProcessing[Работа с данными ошибок]
    end
    SetManagement --> ErrorDefinition
    ErrorDefinition --> ErrorDataProcessing
    
   subgraph Dimension Classes
       DimensionClassDefinition[Определение класса Fd для работы с размерами]
    end
     ErrorDataProcessing --> DimensionClassDefinition
     
    subgraph Core Settings
      SettingsDataDefinition[Определение классов настроек]
        ConfigAccess[Получение конфигураций]
    end
     DimensionClassDefinition --> SettingsDataDefinition
      SettingsDataDefinition --> ConfigAccess
      
     subgraph DOM Element Check
       HTMLElementCheck[Проверка element]
    end
    ConfigAccess --> HTMLElementCheck

    subgraph CSS Dimension and Style Handling
        StyleHandling[Определение стилей]
        DimensionCalculation[Вычисление размеров]
    end
     HTMLElementCheck --> StyleHandling
    StyleHandling --> DimensionCalculation