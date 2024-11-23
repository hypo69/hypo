```markdown
# Модуль web-streams-polyfill

## Обзор

Данный модуль содержит полифилл для спецификации `Web Streams API`.  Он предоставляет реализацию ключевых классов и интерфейсов, таких как `ReadableStream`, `WritableStream`, `ReadableStreamDefaultReader`, `ReadableStreamBYOBReader`, `ReadableStreamBYOBRequest`, `ReadableByteStreamController`, `ReadableStreamDefaultController`, `TransformStream`, и другие, необходимые для работы с потоками данных в браузерах, не поддерживающих эту спецификацию.

## Классы

### `SimpleQueue`

**Описание**:  Структура простого очереди, использующая связанный список массивов для хранения элементов.  Это позволяет избежать проблем масштабируемости, возникающих при использовании одного массива большой длины.

**Методы**:

- `push(element)`: Добавляет элемент в конец очереди.
- `shift()`: Удаляет и возвращает элемент из начала очереди. Возвращает `undefined`, если очередь пуста.
- `forEach(callback)`: Применяет переданную функцию `callback` к каждому элементу очереди.
- `peek()`: Возвращает значение элемента в начале очереди, без удаления его. Возвращает `undefined`, если очередь пуста.
- `get length()`: Возвращает текущую длину очереди.


### `ReadableStreamReaderGeneric`

**Описание**: Базовый класс для чтения потоков данных.


### `ReadableStreamDefaultReader`

**Описание**: Представляет собой стандартный читатель для `ReadableStream`.  Он позволяет асинхронно получать данные из потока.


### `ReadableStreamBYOBReader`

**Описание**: Представляет собой читатель для `ReadableStream` использующий подход BYOB (Byte-Order-Byte).


### `ReadableByteStreamController`

**Описание**: Контроллер для управления `ReadableStream` типа байтов.


### `ReadableStreamDefaultController`

**Описание**: Контроллер для управления стандартным `ReadableStream`.


### `ReadableStream`

**Описание**: Класс, представляющий поток данных.  Используется для чтения данных из источника.


### `ReadableStreamAsyncIteratorImpl`

**Описание**: Реализация `AsyncIterable` для `ReadableStream`.


### `WritableStream`

**Описание**: Класс, представляющий поток данных для записи. Используется для записи данных в приемник.


### `WritableStreamDefaultController`

**Описание**: Контроллер для управления стандартным `WritableStream`.


### `WritableStreamDefaultWriter`

**Описание**: Представляет собой стандартный писатель для `WritableStream`.  Позволяет асинхронно записывать данные в поток.


### `TransformStream`

**Описание**:  Преобразует данные от `ReadableStream` к `WritableStream`.


### `TransformStreamDefaultController`

**Описание**: Контроллер для управления потоками преобразования.



## Функции

### `noop`

**Описание**: Пустая функция, которая не делает ничего.


### `typeIsObject`

**Описание**: Проверяет, является ли переданное значение объектом или функцией.


### `rethrowAssertionErrorRejection`

**Описание**:  Функция, которая перебрасывает исключения `AssertionError`


### `setFunctionName`

**Описание**: Устанавливает имя функции.


### `newPromise`

**Описание**: Создает новый объект `Promise`.


### `promiseResolvedWith`

**Описание**: Создает `Promise`, который решен с заданным значением.


### `promiseRejectedWith`

**Описание**: Создает `Promise`, который отклонен с заданным значением.


### `PerformPromiseThen`

**Описание**: Выполняет метод `then` для `Promise`.


### `uponPromise`

**Описание**: Выполняет функцию `onFulfilled` или `onRejected` в зависимости от того, был ли выполнен или отклонен объект Promise.


### `uponFulfillment`

**Описание**: Выполняет функцию `onFulfilled` в случае выполнения Promise.


### `uponRejection`

**Описание**: Выполняет функцию `onRejected` в случае отклонения Promise.


### `transformPromiseWith`

**Описание**: Преобразует `Promise` с помощью заданных функций.


### `setPromiseIsHandledToTrue`

**Описание**: Устанавливает флаг `isHandled` для `Promise` в значение `true`.


### `CreateArrayFromList`

**Описание**: Создает новый массив из входного списка.


### `CopyDataBlockBytes`

**Описание**: Копирует данные из одного блока в другой.


### `IsDetachedBuffer`

**Описание**: Проверяет, отсоединено ли буферное хранилище.


### `ArrayBufferSlice`

**Описание**: Создает новую копию ArrayBuffer, начиная с begin и заканчивая end.


### `GetMethod`

**Описание**: Возвращает метод по имени из объекта `receiver`.


### `GetIterator`

**Описание**:  Возвращает объект итератора для объекта.


### `IteratorNext`

**Описание**: Получает следующий результат от итератора.


### `IteratorComplete`

**Описание**: Проверяет, завершена ли итерация.


### `IteratorValue`

**Описание**: Возвращает значение текущего шага итератора.


### `IsNonNegativeNumber`

**Описание**:  Проверка, является ли значение конечным, не NaN и неотрицательным числом.


### `CloneAsUint8Array`

**Описание**:  Создает глубокую копию Uint8Array.


### `assertDictionary`

**Описание**: Проверяет, что переданный объект является словарем.


### `assertFunction`

**Описание**: Проверяет, что переданная переменная является функцией.


### `assertObject`

**Описание**: Проверяет, что переданная переменная является объектом.


### `assertRequiredArgument`

**Описание**: Проверяет, что переданный аргумент не является undefined.


### `assertRequiredField`

**Описание**: Проверяет, что поле в объекте не undefined.


### `convertUnrestrictedDouble`

**Описание**:  Преобразует значение в число с плавающей запятой.


### `censorNegativeZero`

**Описание**: Заменяет отрицательный ноль на обычный ноль.


### `convertUnsignedLongLongWithEnforceRange`

**Описание**: Преобразует значение в беззнаковое 64-битное целое число с проверкой диапазона.


### `assertReadableStream`

**Описание**: Проверка типа на совместимость с ReadableStream.


### `ReadableStreamPipeTo`

**Описание**:  Метод для соединения `ReadableStream` и `WritableStream`.


### `defaultReaderBrandCheckException`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `streamAsyncIteratorBrandCheckException`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `isDataViewConstructor`

**Описание**: Проверяет, является ли переданный конструктор конструктором `DataView`.


### `isDataView`

**Описание**: Проверяет, является ли переданный объект объектом `DataView`.


### `arrayBufferViewElementSize`

**Описание**: Возвращает размер элемента буферного представления.


### `byobRequestBrandCheckException`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `byteStreamControllerBrandCheckException`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `convertReaderOptions`

**Описание**: Функция для преобразования опций читателя.


### `convertReadableStreamReaderMode`

**Описание**:  Функция для преобразования режима читателя.


### `convertByobReadOptions`

**Описание**: Функция для преобразования опций чтения BYOB.


### `convertUnderlyingDefaultOrByteSource`

**Описание**: Преобразует исходный поток в поток типа bytes или default.


### `convertUnderlyingSourceCancelCallback`

**Описание**: Функция для преобразования функции отмены исходного источника.


### `convertUnderlyingSourcePullCallback`

**Описание**: Функция для преобразования функции pull исходного источника.


### `convertUnderlyingSourceStartCallback`

**Описание**: Функция для преобразования функции start исходного источника.


### `convertReadableStreamType`

**Описание**:  Преобразует тип ReadableStream.


### `convertIteratorOptions`

**Описание**: Преобразует опции итератора.


### `convertPipeOptions`

**Описание**: Преобразует опции `pipe`.


### `assertAbortSignal`

**Описание**: Проверяет, что переданный объект является объектом `AbortSignal`.


### `convertReadableWritablePair`

**Описание**: Проверка и преобразование пары `readable/writable`.


### `streamBrandCheckException$1`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `streamBrandCheckException$2`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `defaultControllerBrandCheckException$1`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `defaultControllerBrandCheckException$2`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `defaultWriterBrandCheckException`

**Описание**: Функция для генерации исключения, если метод используется не с корректным объектом.


### `defaultWriterLockException`

**Описание**:  Функция для создания исключения, если писатель не заблокирован.


### `convertQueuingStrategyInit`

**Описание**:  Преобразует опции стратегии очереди.


### `byteLengthSizeFunction`

**Описание**: Возвращает длину в байтах объекта.


### `ByteLengthQueuingStrategy`

**Описание**: Стратегия очереди, которая подсчитывает количество байтов в каждом фрагменте.


### `countSizeFunction`

**Описание**: Функция, которая всегда возвращает 1.


### `CountQueuingStrategy`

**Описание**: Стратегия очереди, которая подсчитывает количество фрагментов.


### `convertTransformer`

**Описание**: Функция для преобразования опций преобразователя.


### `convertTransformerFlushCallback`

**Описание**: Преобразует функцию `flush`.


### `convertTransformerStartCallback`

**Описание**: Преобразует функцию `start`.


### `convertTransformerTransformCallback`

**Описание**: Преобразует функцию `transform`.


### `convertTransformerCancelCallback`

**Описание**: Преобразует функцию `cancel`.


### `streamBrandCheckException`

**Описание**:  Функция для генерации исключения, если метод используется не с корректным объектом.

```