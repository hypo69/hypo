```markdown
# OpenAI Assistants API Quickstart

## Обзор

Этот проект предназначен в качестве шаблона для использования API Assistants в Next.js с потоковой передачей данных, использованием инструментов (интерпретатора кода и поиска по файлам) и вызовами функций.  В проекте представлены несколько страниц, демонстрирующих эти возможности, но они все используют один и тот же помощник со всеми включенными возможностями.

Основная логика чата находится в компоненте `Chat` в `app/components/chat.tsx`, а обработчики начинаются с `api/assistants/threads` (в `api/assistants/threads/...`). Не стесняйтесь начинать свой собственный проект и копировать часть этой логики! Компонент `Chat` сам по себе можно скопировать и использовать напрямую, при условии, что вы также скопируете стили из `app/components/chat.module.css`.

## Страницы

- **Пример базового чата**: [http://localhost:3000/examples/basic-chat](http://localhost:3000/examples/basic-chat)
- **Пример вызова функций**: [http://localhost:3000/examples/function-calling](http://localhost:3000/examples/function-calling)
- **Пример поиска по файлам**: [http://localhost:3000/examples/file-search](http://localhost:3000/examples/file-search)
- **Пример со всеми функциями**: [http://localhost:3000/examples/all](http://localhost:3000/examples/all)


## Основные компоненты

### `app/components/chat.tsx`

**Описание**: Обрабатывает отображение чата, потоковую передачу данных и перенаправление вызовов функций.

### `app/components/file-viewer.tsx`

**Описание**: Обрабатывает загрузку, извлечение и удаление файлов для поиска по файлам.


## Конечные точки

### `api/assistants` (POST)

**Описание**: Создает помощника (используется только при запуске).

### `api/assistants/threads` (POST)

**Описание**: Создает новую ветку.

### `api/assistants/threads/[threadId]/messages` (POST)

**Описание**: Отправляет сообщение помощнику.

### `api/assistants/threads/[threadId]/actions` (POST)

**Описание**: Сообщает помощнику о результате вызова функции.

### `api/assistants/files` (GET/POST/DELETE)

**Описание**: Получает, загружает и удаляет файлы помощника для поиска по файлам.


## Настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/openai/openai-assistants-quickstart.git
cd openai-assistants-quickstart
```

### 2. Установка ключа API OpenAI

```bash
export OPENAI_API_KEY="sk_..."
```

(или в файле `.env.example` и переименовать его в `.env`).

### 3. Установка зависимостей

```bash
npm install
```

### 4. Запуск

```bash
npm run dev
```

### 5. Переход по адресу [http://localhost:3000](http://localhost:3000).


## Развертывание

Вы можете развернуть этот проект на Vercel или любой другой платформе, поддерживающей Next.js.

[![Развертывание с Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fopenai%2Fopenai-assistants-quickstart&env=OPENAI_API_KEY,OPENAI_ASSISTANT_ID&envDescription=API%20Keys%20and%20Instructions&envLink=https%3A%2F%2Fgithub.com%2Fopenai%2Fopenai-assistants-quickstart%2Fblob%2Fmain%2F.env.example)


## Обратная связь

Дайте нам знать о ваших идеях, вопросах или отзывах в [форме](https://docs.google.com/forms/d/e/1FAIpQLScn_RSBryMXCZjCyWV4_ebctksVvQYWkrq90iN21l1HLv3kPg/viewform?usp=sf_link)!
```
