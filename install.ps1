### Hypotez
# The name of the project folder is important.

# Setting the execution policy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Cloning the `hypotez` repository
#git clone https://github.com/DavidkaBenAvraham/hypotez

# Navigating to the hypotez directory
#cd hypotez

# Creating a virtual environment `venv`. The name of the environment is specified in the code.
# It is advisable not to change it
python -m venv venv
Write-Output " ######################### Virtual Environment Created ######################"

# Setting the path to the directory with the code
# Getting the path to the directory containing activate.ps1
$venvDir = Get-Item -LiteralPath (Split-Path $MyInvocation.MyCommand.Path)

# Full path to activate.ps1
$activatePath = Join-Path -Path $venvDir -ChildPath "Scripts\Activate.ps1"

# Line we want to add
$lineToAdd = '$env:PYTHONPATH += ";$PSScriptRoot\src"'

# Adding the line to the end of the file
Add-Content -Path $activatePath -Value $lineToAdd

# Navigating to the hypotez directory
Set-Location hypotez



# Activating the virtual environment
venv\scripts\activate.ps1

# Updating `pip`
pip install --upgrade pip setuptools wheel

# Installing dependencies from requirements.txt. The `--ignore-installed` flag allows other dependencies to be installed,
# even if one of them causes an error.
pip install -r requirements.txt --ignore-installed

# Installing Jupyter Notebook version 7
pip install jupyter==7.*

jupyter labextension install @jupyter-widgets/jupyterlab-manager

# Installing Jupyter Kernel
python -m ipykernel install --user --name=venv --display-name "Python (hypotez)"

# Creating project folders
New-Item -ItemType Directory -Path .\docs
New-Item -ItemType Directory -Path .\export
New-Item -ItemType Directory -Path .\log
New-Item -ItemType Directory -Path .\tmp
New-Item -ItemType Directory -Path .\bin
New-Item -ItemType Directory -Path .\sandbox

# Cloning the `docs` repository inside the hypotez directory
git clone https://github.com/DavidkaBenAvraham/docs

# Running doxyrun (from `hypotez`) for cerating local project documentashion in doxygen format 
# Good for reach helping
./doxyrun

# Installing web-ext using npm
try {
    npm install --global web-ext
} catch {
    # If an error occurs, display the error message
    Write-Host "An error occurred: $_"
}

# Configuring Jupyter appearance
mkdir $env:USERPROFILE\.jupyter\custom
Copy-Item -Path "src\install\jupyter\style.css" -Destination "$env:USERPROFILE\.jupyter\custom\custom.css"

