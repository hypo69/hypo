# Set execution policy for the current user
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Define the base path as the parent directory of the current location
$basePath = Split-Path -Path (Get-Location) -Parent

# Set path to the Python interpreter relative to the base path, if needed
$pythonPath = Join-Path -Path $basePath -ChildPath "venv\scripts\python.exe"

# Set path to the Python script relative to the base path
$scriptPath = Join-Path -Path $basePath -ChildPath "dev_utils\update_files_headers.py"

# Define directories to process relative to the base path
$devUtilsDir = Join-Path -Path $basePath -ChildPath "dev_utils"
$srcDir = Join-Path -Path $basePath -ChildPath "src"
$docsDir = Join-Path -Path $basePath -ChildPath "docs"

# Run the script with specified directories as parameters
& $pythonPath $scriptPath $devUtilsDir $srcDir $docsDir
