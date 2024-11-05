# Hypotez Project

## Project Description 
The `hypotez` project involves developing a personal AI assistant capable of performing various tasks, such as those of an insurance agent, real estate agent, sales specialist, HR representative, postal secretary, and more. Each assistant requires specific training for its designated role, and models will be offered for different business types. The goal is to create an adaptive assistant that can handle complex tasks independently.

In addition, the `hypotez` project includes tools for hypothesis analysis and data interpretation. It provides libraries for statistical analysis and data visualization, allowing users to conduct efficient analysis and make informed decisions based on collected insights.

Furthermore, a parser and scraper are built into the project for data gathering and processing from various sources. These tools automate the extraction of relevant information from websites and documents, enabling efficient data collection for analysis and decision-making. The integrated assistant aims to enhance productivity across domains by streamlining workflows with timely and accurate data.

**In a Nutshell**:

<br>
<img src="images/now_feature.png" alt="Feature Image" width="270" height="320" />
<br>

---

### Key Features

1. **Lead Management**:
   - **Capture Leads**: Automatically gather and store lead information from various sources.
   - **Track Interactions**: Log all interactions with leads, including emails, calls, and meetings.
   - **Lead Scoring**: Evaluate and rank leads based on potential value and engagement.

2. **Sales Pipeline Management**:
   - **Track Deals**: Monitor deals through different stages of the pipeline.
   - **Forecasting**: Predict future sales performance based on trends.
   - **Task Management**: Assign and track tasks related to each lead.

3. **Reporting and Analytics**:
   - **Performance Metrics**: Generate reports on sales performance and lead conversion.
   - **Custom Reports**: Create custom reports to analyze specific sales aspects.

4. **Communication Tools**:
   - **Email Integration**: Manage and track communications through email integration.
   - **Scheduling**: Schedule meetings and follow-ups.

5. **Customer Relationship Management (CRM)**:
   - **Contact Management**: Maintain a contact database.
   - **Interaction History**: Keep a record of all customer interactions.

6. **Automation**:
   - **Email Campaigns**: Automate follow-up emails and marketing campaigns.
   - **Data Entry**: Reduce manual entry through automated data capture.

7. **Team Collaboration**:
   - **Shared Dashboards**: Provide real-time dashboards for updates and collaboration.
   - **Notes and Comments**: Enable team members to leave notes on leads and deals.

8. **Integration with Other Tools**:
   - **Accounting Software**: Sync with accounting software for financial tracking.
   - **Project Management**: Integrate with project management tools.

### Example Workflow

1. **Lead Capture**: Automatically import lead information.
2. **Lead Scoring**: Assign scores to leads based on criteria.
3. **Pipeline Management**: Move leads through pipeline stages.
4. **Follow-Up**: Automate follow-up emails and schedule meetings.
5. **Reporting**: Generate weekly reports on lead status.
6. **Collaboration**: Share updates with the sales team.

### Potential Tools

- **CRM Systems**: Salesforce, HubSpot, Zoho CRM.
- **Automation Platforms**: Zapier, Microsoft Power Automate.
- **Reporting Tools**: Google Data Studio, Tableau.

---

## Setup Instructions

### Required Software (Pre-installed on your computer)
Here’s the list of required, pre-installed software for the project:

1. **Web Browsers**: One or more of the following:
   - **Firefox**
   - **Chrome**
   - **Edge**
   These are used in conjunction with browser drivers (in the `bin` folder) for testing and automation purposes.

2. **PowerShell**: A task automation and configuration management framework from Microsoft, essential for executing scripts and managing workflows, especially in Windows environments.

3. **Python 3.12**: This specific version of Python is required for the project, likely due to compatibility with certain libraries or dependencies.

4. **`npm`**: Node Package Manager for managing JavaScript project dependencies, allowing installation, updating, and managing of libraries and development tools.

# Software tools and library located in the `bin` folder:
Here's a brief overview of each software tool or library located in the bin folder:

1. **`ffmpeg.exe`**: A comprehensive tool for handling multimedia files. It's commonly used for video and audio encoding, decoding, transcoding, and streaming. It supports many formats and can convert media files, apply filters, and modify encoding settings.

2. **`chrome drivers`**: Web drivers for controlling the Google Chrome browser, mainly used for automated browser testing. These are often integrated into testing frameworks like Selenium for simulating browser interactions.

3. **`chrome for developers`**: This is a version of Google Chrome specifically for developers, often including beta or experimental features. It's useful for web development testing and debugging in real-world browser environments.

4. **`geckodriver`**: A driver for Mozilla Firefox, used to control Firefox in automated testing scenarios. It enables interaction with the Firefox browser through automation tools, allowing for cross-browser testing in conjunction with other drivers.

5. **`edge drivers`**: Drivers for Microsoft Edge browser control, useful in automated testing environments, similar to Chrome and Firefox drivers. It's part of Microsoft's WebDriver toolset and allows testing web applications in the Edge browser.

6. **`gtk`**: The GIMP Toolkit, a library for developing graphical user interfaces. Widely used in Linux applications, it provides a collection of controls and widgets for creating windows, buttons, and other interface elements.


### Installation Steps

1. **Clone the repository**:
   ```powershell
   # Set the current path
   $currentPath = (Get-Location).Path
   
   # Clone the repository
   git clone https://github.com/hypo69/hypo.git
   ```
   - Navigate to the `hypotez` directory.


2. **Download the `bin` directory**:
   [Download bin directory](https://mega.nz/file/VahExTTQ#igYq3AM8W_xUDvONX3VOKM5Nx-m9pLgno-YpqCzWNPo)
   - Unzip the downloaded compressed file into the `hypotez` folder .
	- Here’s the translation and adjustment for clarity:

Make sure to **unzip directly into the project folder**, similar to selecting "Extract Here" in a context menu. The archive already contains a `bin` folder with all necessary binaries, so unzipping it in the project root will place everything in the correct directory structure automatically.
   - Your directory structure should look like this:
   ```
   hypotez
   └─ bin
      ├─ wkhtmltopdf
      ├─ ffmpeg
      ├─ graphviz
      ├─ gtk
      ├─ keepass-2.55
      └─ webdrivers
   ``` 

Let me know if you'd like further adjustments!
	- - Easy Way to continue installation: 								
	Execute the install script `.\INSTALL.PS1`.

    The script will guide you through the steps to set up hypotez efficiently. After completion, continue to the Configuration section below to add your credentials and any other specific settings.

3. Continue to manual install:

4. **Set execution policy**:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

5. **Create a virtual environment**:
   ```powershell
   python -m venv venv
   ```

6. **Activate the virtual environment**:
   ```powershell
   venv\Scripts\Activate.ps1
   ```

7. **Upgrade `pip`**:
   ```powershell
   pip install --upgrade pip setuptools wheel
   ```

8. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt --ignore-installed
   ```

9. **Install npm and web-ext**:
	```powershell
	npm install -g npm
	npm install -g web-ext
	```

10. **Install Jupyter Lab extensions**:
	```powershell
	jupyter labextension install @jupyter-widgets/jupyterlab-manager
	```

11. **Install Playwright**:
	```powershell
	playwright install
	```

## Configuration

### Setting Up Credentials

Before starting, create a folder named `secrets` in the project root. Copy `credentials.kdbx.example` and `password.txt` from the service folder into `secrets`, and remove the `.example` suffix.

Here is the structure for credentials:

1. **Suppliers > Aliexpress > API**
   - `api_key`: Aliexpress API key.
   - `secret`: Secret key.
   - `tracking_id`: Tracking ID.
   - `email`: Aliexpress account email.
   - `password`: Aliexpress account password.

2. **OpenAI**
   - `api_key`: API key for OpenAI.

3. **Telegram**, **Discord**, **Prestashop**, **SMTP**, **Facebook**, **Google API**, etc.

Ensure these details are correctly entered to allow the assistant to function effectively.

#### PowerShell Commands

```powershell
# Define current path
$currentPath = (Get-Location).Path

# Create the 'secrets' folder
New-Item -ItemType Directory -Path "$currentPath\secrets"

# Copy example files to 'secrets' folder
Copy-Item -Path "$currentPath\credentials.kdbx.example" -Destination "$currentPath\secrets\credentials.kdbx"
Copy-Item -Path "$currentPath\password.txt" -Destination "$currentPath\secrets\password.txt"
```

For more details, please check out the [codebase in the `src/readme.md`](src/readme.md). 
Instructions for setting up passwords and secrets are documented in the [SECURITY.md](SECURITY.md) file.
