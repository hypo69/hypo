# Hypotez Project - Install Script
# This script sets up the Hypotez Project by cloning the repository, setting up the virtual environment, and configuring required files and folders.

# Define current path
$currentPath = (Get-Location).Path



# Navigate to the hypotez directory
Set-Location -Path "$currentPath"

# Set execution policy for the current user
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
& "$currentPath\venv\Scripts\Activate.ps1"

# Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# Install project dependencies
pip install -r requirements.txt --ignore-installed

# Install npm and web-ext
npm install -g npm
npm install -g web-ext

# Install Jupyter Lab extensions
jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Install Playwright features
playwright install

# Configuration - Setting up the 'secrets' folder and files
# Create the 'secrets' folder in the root of the project
New-Item -ItemType Directory -Path "$currentPath\secrets"

# Copy example files to 'secrets' folder
Copy-Item -Path "$currentPath\hypotez\credentials.kdbx.example" -Destination "$currentPath\secrets\credentials.kdbx"
Copy-Item -Path "$currentPath\hypotez\password.txt.exmple" -Destination "$currentPath\hypotez\password.txt"

# Confirm setup completion
Write-Output "Hypotez Project setup is complete. Ensure the downloaded 'bin' folder and 'secrets' folder are correctly populated. For further configurations, please refer to SECURITY.md."
