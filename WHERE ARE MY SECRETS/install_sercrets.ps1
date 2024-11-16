## \file hypotez/WHERE ARE MY SECRETS/install_sercrets.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: WHERE ARE MY SECRETS """
MODE = 'debug'
# Create the 'secrets' folder in the root of the project
New-Item -ItemType Directory -Path "..\..\secrets"

# Copy the example files to the 'secrets' folder
Copy-Item -Path "credentials.kdbx.example" -Destination "..\..\secrets\credentials.kdbx"
Copy-Item -Path "password.txt" -Destination "..\..\secrets\password.txt"

# Remove the .example suffix from the credentials file
Rename-Item -Path ".\secrets\credentials.kdbx.example" -NewName ".\secrets\credentials.kdbx"
Rename-Item -Path ".\secrets\credentials.kdbx.example" -NewName ".\secrets\credentials.kdbx"
