Вот обновленная версия README.md с TOC и улучшенной логикой установки. Я также убрал лишние элементы, сохранив только ключевые шаги.

```markdown
# Hypotez Project

## Table of Contents
- [Project Description](#project-description)
- [Key Features](#key-features)
- [Setup Instructions](#setup-instructions)
  - [Required Software](#required-software)
  - [Installation Steps](#installation-steps)
  - [Configuration](#configuration)
- [Licenses](#licenses)

## Project Description

**In a Nutshell**:
<br>
<img src="images/now_feature.png" alt="Feature Image" width="270" height="320" />
<br>

The `hypotez` project is your personal AI assistant designed to help with a wide range of tasks. Whether you need a virtual insurance agent, a real estate assistant, a sales specialist, an HR representative, or even an email secretary, `hypotez` has you covered. Our goal is to create a versatile assistant that can adapt to different roles and handle complex tasks as if you have a personal helper for every situation.

Additionally, `hypotez` is a powerful data analysis tool. It comes with various libraries for statistics and visualization, helping you quickly make sense of your data and make informed decisions.

On top of that, the project features a handy parser and scraper that automatically gather data from websites and documents. This means you can skip the tedious data collection and get the insights you need for analysis and decision-making right away. In short, `hypotez` is your go-to assistant that speeds up your work and helps you make smart, well-informed choices.

---

## Key Features

1. **Lead Management**:
   - Capture and store lead information.
   - Track interactions (emails, calls, meetings).
   - Rank leads based on potential value and engagement.

2. **Sales Pipeline Management**:
   - Monitor deals through different pipeline stages.
   - Predict future sales performance.
   - Assign and track tasks for each lead.

3. **Reporting and Analytics**:
   - Generate sales performance and lead conversion reports.
   - Create custom reports for specific sales aspects.

4. **Communication Tools**:
   - Email integration and communication tracking.
   - Schedule meetings and follow-ups.

5. **Automation**:
   - Automate email campaigns and marketing.
   - Reduce manual entry with automated data capture.

6. **Team Collaboration**:
   - Share real-time dashboards.
   - Enable team collaboration with shared notes and comments.

---

## Setup Instructions

### Required Software

Ensure the following software is installed on your system:

1. **Web Browsers**:
   - Firefox
   - Chrome
   - Edge

2. **PowerShell**: For task automation and script execution.

3. **Python 3.12**: Specific version required for compatibility with dependencies.

4. **npm**: For managing JavaScript project dependencies.

---

### Installation Steps

1. **Clone the repository**:
   ```powershell
   # Clone the repository
   git clone https://github.com/hypo69/hypo.git
   ```
   Navigate to the `hypotez` directory.

2. **Download the `bin` directory**:
   [Download bin directory](https://mega.nz/file/VahExTTQ#igYq3AM8W_xUDvONX3VOKM5Nx-m9pLgno-YpqCzWNPo)
   - Unzip the downloaded file into the `hypotez` folder.

   Ensure the `bin` folder is unzipped directly into the project folder (select "Extract Here").

3. **Set Execution Policy** (Windows):
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Install Python 3.12**:
   - Verify Python version:
     ```bash
     python --version
     ```
   - If Python 3.12 is not installed, follow the instructions below:

     - **Linux**:
       ```bash
       sudo apt update
       sudo apt install python3.12
       ```

     - **Windows**:
       Download from [python.org](https://www.python.org/downloads/release/python-3120/) and install.

     - **macOS**:
       ```bash
       brew install python@3.12
       ```

5. **Create Virtual Environment**:
   After installing Python 3.12, create a virtual environment:
   ```bash
   python3.12 -m venv venv
   ```

6. **Activate Virtual Environment**:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

7. **Upgrade `pip`**:
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

8. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

9. **Install npm and Web Extensions**:
   ```bash
   npm install -g npm
   npm install -g web-ext
   ```

10. **Install Playwright**:
    ```bash
    playwright install
    ```

---

### Configuration

1. **Create `secrets` folder**:
   ```powershell
   $currentPath = (Get-Location).Path
   New-Item -ItemType Directory -Path "$currentPath\secrets"
   ```

2. **Copy Credentials**:
   Copy `credentials.kdbx.example` and `password.txt` from the `service` folder into `secrets` and remove `.example` suffix.

   ```powershell
   Copy-Item -Path "$currentPath\credentials.kdbx.example" -Destination "$currentPath\secrets\credentials.kdbx"
   Copy-Item -Path "$currentPath\password.txt" -Destination "$currentPath\secrets\password.txt"
   ```

3. **Set API Keys and Credentials**:
   Ensure correct API keys and credentials are configured for services like Aliexpress, OpenAI, Telegram, and others.

---

## Licenses

Check the [LICENSE](LICENSE) file for the project’s licensing details.
