# Быстрый старт с API помощников OpenAI

Шаблон быстрого старта, использующий API помощников OpenAI [https://platform.openai.com/docs/assistants/overview](https://platform.openai.com/docs/assistants/overview) с [Next.js](https://nextjs.org/docs).
<br/>
<br/>
![Быстрый старт с API помощников OpenAI](https://github.com/openai/openai-assistants-quickstart/assets/27232/755e85e9-3ea4-421f-b202-3b0c435ea270)

## Настройка быстрого старта

### 1. Клонирование репозитория

```bash
git clone https://github.com/openai/openai-assistants-quickstart.git
cd openai-assistants-quickstart
```

### 2. Установка вашего [ключа API OpenAI](https://platform.openai.com/api-keys)

```bash
export OPENAI_API_KEY="sk_..."
```

(или в `.env.example` и переименуйте его в `.env`).

### 3. Установка зависимостей

```bash
npm install
```

### 4. Запуск

```bash
npm run dev
```

### 5. Переход по ссылке [http://localhost:3000](http://localhost:3000).

## Развертывание

Вы можете развернуть этот проект на Vercel или любой другой платформе, поддерживающей Next.js.

[![Развернуть с Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fopenai%2Fopenai-assistants-quickstart&env=OPENAI_API_KEY,OPENAI_ASSISTANT_ID&envDescription=Ключи%20API%20и%20инструкции&envLink=https%3A%2F%2Fgithub.com%2Fopenai%2Fopenai-assistants-quickstart%2Fblob%2Fmain%2F.env.example)

## Обзор

Этот проект предназначен в качестве шаблона для использования API помощников в Next.js с [потоковым выводом](https://platform.openai.com/docs/assistants/overview/step-4-create-a-run), использованием инструментов ([интерпретатор кода](https://platform.openai.com/docs/assistants/tools/code-interpreter) и [поиск по файлам](https://platform.openai.com/docs/assistants/tools/file-search)), и [вызовом функций](https://platform.openai.com/docs/assistants/tools/function-calling). Хотя есть несколько страниц для демонстрации каждой из этих возможностей, все они используют одного и того же помощника со всеми включенными возможностями.

Основная логика чата находится в компоненте `Chat` в `app/components/chat.tsx` и обработчиках, начинающихся с `api/assistants/threads` (находятся в `api/assistants/threads/...`). Не стесняйтесь начать свой собственный проект и скопировать часть этой логики! Компонент `Chat` сам по себе может быть скопирован и использован непосредственно, при условии, что вы также скопируете стили из `app/components/chat.module.css`.

### Страницы

- Пример базового чата: [http://localhost:3000/examples/basic-chat](http://localhost:3000/examples/basic-chat)
- Пример вызова функций: [http://localhost:3000/examples/function-calling](http://localhost:3000/examples/function-calling)
- Пример поиска по файлам: [http://localhost:3000/examples/file-search](http://localhost:3000/examples/file-search)
- Пример с полным функционалом: [http://localhost:3000/examples/all](http://localhost:3000/examples/all)

### Основные компоненты

- `app/components/chat.tsx` — обрабатывает отображение чата, [потоковый вывод](https://platform.openai.com/docs/assistants/overview?context=with-streaming), и перенаправление [вызова функций](https://platform.openai.com/docs/assistants/tools/function-calling/quickstart?context=streaming&lang=node.js)
- `app/components/file-viewer.tsx` — обрабатывает загрузку, извлечение и удаление файлов для [поиска по файлам](https://platform.openai.com/docs/assistants/tools/file-search)

### Конечные точки

- `api/assistants` — `POST`: создание помощника (используется только при запуске)
- `api/assistants/threads` — `POST`: создание нового потока
- `api/assistants/threads/[threadId]/messages` — `POST`: отправка сообщения помощнику
- `api/assistants/threads/[threadId]/actions` — `POST`: информирование помощника о результате вызова функции
- `api/assistants/files` — `GET`/`POST`/`DELETE`: извлечение, загрузка и удаление файлов помощника для поиска по файлам

## Обратная связь

Поделитесь своими мыслями, вопросами или обратной связью в [этой форме](https://docs.google.com/forms/d/e/1FAIpQLScn_RSBryMXCZjCyWV4_ebctksVvQYWkrq90iN21l1HLv3kPg/viewform?usp=sf_link)!


**Изменения:**

*  Перевод всех текстов на русский язык.
*  Использование более точных и понятных терминов.
*  Сохранение исходной структуры и функциональности.
*  Использование правильного синтаксиса Markdown для гиперссылок и заголовков.
*  Добавление более подходящих изображений в случае отсутствия.