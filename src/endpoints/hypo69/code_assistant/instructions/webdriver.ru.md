
Этот документ предоставляет обзор всех вебдрайверов, доступных в проекте, их настроек и опций. Каждый вебдрайвер имеет свои параметры, которые можно настроить в соответствующих файлах JSON.

# Вебдрайверы и их настройки

&nbsp;&nbsp;&nbsp;&nbsp;Этот документ содержит описание всех вебдрайверов, доступных в проекте, их настроек и опций. Каждый вебдрайвер предоставляет возможности для автоматизации браузеров и сбора данных.

---

## Оглавление

1. [Firefox WebDriver](#1-firefox-webdriver)
2. [Chrome WebDriver](#2-chrome-webdriver)
3. [Edge WebDriver](#3-edge-webdriver)
4. [Playwright Crawler](#4-playwright-crawler)
5. [BeautifulSoup и XPath Parser](#5-beautifulsoup-и-xpath-parser)
6. [Заключение](#заключение)

---

## 1. Firefox WebDriver

### Описание
&nbsp;&nbsp;&nbsp;&nbsp;Firefox WebDriver предоставляет функциональность для работы с браузером Firefox. Он поддерживает настройку пользовательских профилей, прокси, user-agent и других параметров.

### Настройки
- **profile_name**: Имя пользовательского профиля Firefox.
- **geckodriver_version**: Версия geckodriver.
- **firefox_version**: Версия Firefox.
- **user_agent**: Пользовательский агент.
- **proxy_file_path**: Путь к файлу с прокси.
- **options**: Список опций для Firefox (например, `["--kiosk", "--headless"]`).

### Пример конфигурации (`firefox.json`)
```json
{
  "options": ["--kiosk", "--headless"],
  "profile_directory": {
    "os": "%LOCALAPPDATA%\\Mozilla\\Firefox\\Profiles\\default",
    "internal": "webdriver\\firefox\\profiles\\default"
  },
  "executable_path": {
    "firefox_binary": "bin\\webdrivers\\firefox\\ff\\core-127.0.2\\firefox.exe",
    "geckodriver": "bin\\webdrivers\\firefox\\gecko\\33\\geckodriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  },
  "proxy_enabled": false
}
```

---

## 2. Chrome WebDriver

### Описание
Chrome WebDriver предоставляет функциональность для работы с браузером Google Chrome. Он поддерживает настройку профилей, user-agent, прокси и других параметров.

### Настройки
- **profile_name**: Имя пользовательского профиля Chrome.
- **chromedriver_version**: Версия chromedriver.
- **chrome_version**: Версия Chrome.
- **user_agent**: Пользовательский агент.
- **proxy_file_path**: Путь к файлу с прокси.
- **options**: Список опций для Chrome (например, `["--headless", "--disable-gpu"]`).

### Пример конфигурации (`chrome.json`)
```json
{
  "options": ["--headless", "--disable-gpu"],
  "profile_directory": {
    "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data\\Default",
    "internal": "webdriver\\chrome\\profiles\\default"
  },
  "executable_path": {
    "chrome_binary": "bin\\webdrivers\\chrome\\125.0.6422.14\\chrome.exe",
    "chromedriver": "bin\\webdrivers\\chrome\\125.0.6422.14\\chromedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  },
  "proxy_enabled": false
}
```

---

## 3. Edge WebDriver

### Описание
Edge WebDriver предоставляет функциональность для работы с браузером Microsoft Edge. Он поддерживает настройку профилей, user-agent, прокси и других параметров.

### Настройки
- **profile_name**: Имя пользовательского профиля Edge.
- **edgedriver_version**: Версия edgedriver.
- **edge_version**: Версия Edge.
- **user_agent**: Пользовательский агент.
- **proxy_file_path**: Путь к файлу с прокси.
- **options**: Список опций для Edge (например, `["--headless", "--disable-gpu"]`).

### Пример конфигурации (`edge.json`)
```json
{
  "options": ["--headless", "--disable-gpu"],
  "profiles": {
    "os": "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default",
    "internal": "webdriver\\edge\\profiles\\default"
  },
  "executable_path": {
    "edge_binary": "bin\\webdrivers\\edge\\123.0.2420.97\\edge.exe",
    "edgedriver": "bin\\webdrivers\\edge\\123.0.2420.97\\msedgedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  },
  "proxy_enabled": false
}
```

---

## 4. Playwright Crawler

### Описание
Playwright Crawler предоставляет функциональность для автоматизации браузеров с использованием библиотеки Playwright. Он поддерживает настройку прокси, user-agent, размера окна и других параметров.

### Настройки
- **max_requests**: Максимальное количество запросов.
- **headless**: Режим безголового запуска браузера.
- **browser_type**: Тип браузера (`chromium`, `firefox`, `webkit`).
- **user_agent**: Пользовательский агент.
- **proxy**: Настройки прокси-сервера.
- **viewport**: Размер окна браузера.
- **timeout**: Тайм-аут для запросов.
- **ignore_https_errors**: Игнорирование ошибок HTTPS.

### Пример конфигурации (`playwrid.json`)
```json
{
  "max_requests": 10,
  "headless": true,
  "browser_type": "chromium",
  "options": ["--disable-dev-shm-usage", "--no-sandbox"],
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "proxy": {
    "enabled": false,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "timeout": 30000,
  "ignore_https_errors": false
}
```

---

## 5. BeautifulSoup и XPath Parser

### Описание
Модуль для парсинга HTML-контента с использованием BeautifulSoup и XPath. Он позволяет извлекать данные из локальных файлов или веб-страниц.

### Настройки
- **default_url**: URL по умолчанию для загрузки HTML.
- **default_file_path**: Путь к файлу по умолчанию.
- **default_locator**: Локатор по умолчанию для извлечения элементов.
- **logging**: Настройки логирования.
- **proxy**: Настройки прокси-сервера.
- **timeout**: Тайм-аут для запросов.
- **encoding**: Кодировка для чтения файлов или запросов.

### Пример конфигурации (`bs.json`)
```json
{
  "default_url": "https://example.com",
  "default_file_path": "file://path/to/your/file.html",
  "default_locator": {
    "by": "ID",
    "attribute": "element_id",
    "selector": "//*[@id='element_id']"
  },
  "logging": {
    "level": "INFO",
    "file": "logs/bs.log"
  },
  "proxy": {
    "enabled": false,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "timeout": 10,
  "encoding": "utf-8"
}
```

---
