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

1. **Web Browsers**: `Firefox`, `Chrome`, and/or `Edge`.
2. **PowerShell**: Command-line shell for task automation (for `Windows`).
3. **Python 3.12**: Required version of Python.

### Software Used in the Project (No Installation Required, Located in the `bin` Folder)

- **`ffmpeg.exe`**: Tool for multimedia file processing.
- **`chrome drivers`**: Drivers for Google Chrome.
- **`chrome for developers`**: Developer version of Chrome.
- **`geckodriver`**: Driver for Firefox.
- **`edge drivers`**: Drivers for Microsoft Edge.
- **`gtk`**: Toolkit for GUI development.

### Installation Steps

1. **Clone the repository**:
   ```powershell
   # Set the current path
   $currentPath = (Get-Location).Path
   
   # Clone the repository
   git clone https://github.com/hypo69/hypo.git
   ```
   - Navigate to the `hypotez` directory.

2. **Download and set up the `bin` directory**:
   [Download bin directory](https://mega.nz/file/VahExTTQ#igYq3AM8W_xUDvONX3VOKM5Nx-m9pLgno-YpqCzWNPo)
   - Unzip into the `hypotez` folder (`hypotez/bin`).

3. **Set execution policy**:
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Create a virtual environment**:
   ```powershell
   python -m venv venv
   ```

5. **Activate the virtual environment**:
   ```powershell
   venv\Scripts\Activate.ps1
   ```

6. **Upgrade `pip`**:
   ```powershell
   pip install --upgrade pip setuptools wheel
   ```

7. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt --ignore-installed
   ```

8. **Install npm and web-ext**:
	```powershell
	npm install -g npm
	npm install -g web-ext
	```

9. **Install Jupyter Lab extensions**:
	```powershell
	jupyter labextension install @jupyter-widgets/jupyterlab-manager
	```

10. **Install Playwright**:
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
