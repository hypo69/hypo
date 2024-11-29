[Русский](README.ru.md)
# Project Hypotez

## Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Required Tools and Software](#required-tools-and-software)
- [Installation Instructions](#installation-instructions)
  - [Checking Python Version](#checking-python-version)
  - [Installing Python 3.12](#installing-python-312)
  - [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Installing npm and web-ext](#installing-npm-and-web-ext)
  - [Installing Jupyter Lab Extensions](#installing-jupyter-lab-extensions)
  - [Installing Playwright](#installing-playwright)
- [Configuration](#configuration)
  - [Setting Up Credentials](#setting-up-credentials)
- [Additional Information](#additional-information)
- [Developer Documentation](https://github.com/hypo69/hypo/tree/master/docs/gemini/consultant/en) (**Not Ready* 😕)
- [User Documentation](https://github.com/hypo69/hypo/blob/master/docs/scenarios/README.MD) (**Not Ready* 😕)
- [Tests](https://github.com/hypo69/hypo/tree/master/pytest)

## Project Overview

I am working on the `hypotez` project, aimed at creating a versatile AI assistant. This assistant is designed to handle a wide range of tasks — from managing emails to analyzing market data.

### Goals and Objectives:
- **Automating routine processes** to save time and boost efficiency.  
- **Accurate and fast data analysis** to simplify decision-making.  
- **Seamless interaction with technology**, tailored to user needs.

---

## Key Directions

1. **Smart Assistant**: Designed for sales, HR, insurance, and task management.  
2. **Analysis Tools**: Data visualization and decision support.  
3. **Automated Information Gathering**: Extracting data from documents, emails, and web pages.

---

## Key Features

### 1. Workflow Automation Assistant  
- Generate meeting summaries with key points and sentiment analysis.  
- Automate message handling and integrate with email services and messengers.

### 2. Price Lists and Procurement  
- Keep price lists up to date for internal and external processes.  
- Automatically match product items from various sources.

### 3. Market Data Analysis  
- Monitor market trends relevant to business, with automated report generation.  
- Identify new opportunities based on analytical data.

### 4. Data Processing and Analysis  
- Integrate sales and procurement data for pattern analysis.  
- Prepare performance metric reports.

### 5. Parsing and Web Scraping  
- Extract structured data from web pages, documents, and emails.  
- Automate data collection with subsequent processing and filtering.  
- Integrate data with internal systems for enhanced analytics.

### 6. Task Automation  
- Reduce manual effort by automating data entry and report management.  
- Integrate with CRM systems for automated workflows.

### 7. Client and Communication Management  
- Consolidate data from emails and messengers.  
- Log client interactions and set reminders for tasks.

### 8. Platform Integration  
- Synchronize data with PrestaShop and other systems.  
- Analyze customer behavior to improve user experience.

### 9. Sales Funnel Management  
- Monitor deal stages and forecast sales.  
- Generate reports on departmental performance.

### 10. Communication and Planning Tools  
- Integrate with email services to manage communications.  
- Automatically schedule meetings and task reminders.

### 11. Analytics and Reporting  
- Dynamic business process reports with custom metric support.  
- Tailored data analysis for specific tasks.

### 12. Advanced Automation  
- Collect data through APIs and complex integrations.  
- Configure scenarios for automatic document creation.

---

## Required Tools and Software

- **Python** (version 3.12)  
- **Chrome/Edge/Firefox** web browsers  

---

## Installation Instructions

### Checking Python Version

*The project is optimized for version 3.12.*

Run the following command to check your installed Python version:

```bash
python --version
```

or

```bash
python3 --version
```

If you have multiple Python versions installed, verify with:

```bash
python3.12 --version
python3.13 --version
```

### Installing Python 3.12

#### For Linux

Install Python 3.12 on Ubuntu:

```bash
sudo apt update
sudo apt install python3.12
```

#### For Windows

Download the installer from the [official Python website](https://www.python.org/downloads/release/python-3120/) and run it. (✎ Ensure the **Add Python to PATH** option is selected).

#### For macOS

Install Python via Homebrew:

```bash
brew install python@3.12
```

---

### Setting Up a Virtual Environment

1. **DEPRECATED** Install `virtualenv` using the following command:
   ```bash
   pip install virtualenv
   ```
2. Create a virtual environment:
   ```bash
   python3.12 -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

1. Install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Installing npm and web-ext

1. Install npm:
   ```bash
   npm install -g npm
   ```

2. Install `web-ext`:
   ```bash
   npm install -g web-ext
   ```

### Installing Jupyter Lab Extensions

```bash
jupyter labextension install @jupyterlab/toc
```

### Installing Playwright

1. Install Playwright:
   ```bash
   pip install playwright
   ```

2. Install browsers:
   ```bash
   playwright install
   ```

---

## Configuration

### Setting Up Credentials

Before starting, create a folder named `secrets` in the project root. Copy `credentials.kdbx.example` from the service folder into `secrets`, and remove the `.example` suffix.

Credential structure:

1. **Suppliers > Aliexpress > API**
   - `api_key`: Aliexpress API key.
   - `secret`: Secret key.
   - `tracking_id`: Tracking ID.
   - `email`: Aliexpress account email.
   - `password`: Aliexpress account password.

2. **OpenAI**
   - `api_key`: API key for OpenAI.

3. **Telegram**, **Discord**, **Prestashop**, **SMTP**, **Facebook**, **Google API**, etc.

Ensure all details are entered correctly for optimal assistant performance.

```powershell
# Define current path
$currentPath = (Get-Location).Path

# Create the 'secrets' folder
New-Item -ItemType Directory -Path "$currentPath\secrets"

# Copy example files to 'secrets' folder
Copy-Item -Path "$currentPath\credentials.kdbx.example" -Destination "$currentPath\secrets\credentials.kdbx"
Copy-Item -Path "$currentPath\password.txt" -Destination "$currentPath\secrets\password.txt"
```

---

## Next Steps

1. [Developer Documentation](https://github.com/hypo69/hypo/tree/master/docs/gemini/consultant/en) (**Not Ready* 😕)  
2. [User Documentation](https://github.com/hypo69/hypo/blob/master/docs/scenarios/README.MD) (**Not Ready* 😕)  
3. [Tests](https://github.com/hypo69/hypo/tree/master/pytest)

## Additional Information

[https://davidka.net](https://davidka.net).  