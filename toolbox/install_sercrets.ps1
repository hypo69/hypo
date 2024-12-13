
# Create the 'secrets' folder in the root of the project
New-Item -ItemType Directory -Path ".\secrets"

# Copy the example files to the 'secrets' folder
Copy-Item -Path ".\templates\credentials.kdbx.example" -Destination ".\secrets\credentials.kdbx"


