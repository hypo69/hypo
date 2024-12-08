rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code interacts with the Google Apps Script API.  It authenticates the application, creates a new Apps Script project, uploads two files (a JavaScript function and a manifest file) to the project, and prints a link to the created script.  This allows for deploying basic Apps Script functionality.

Execution steps
-------------------------
1. **Authentication:** The code first checks for an existing `token.json` file.  If found, it uses the credentials stored in that file. If not, it prompts the user to authorize the application to access their Google Apps Script account. It obtains credentials and stores them in `token.json` for future use.

2. **API Building:** The code builds an API client object (`service`) using the retrieved credentials.  This client object is essential for interacting with the Apps Script API.

3. **Project Creation:** The code creates a new Apps Script project using the `projects().create()` method. It provides a title for the project.

4. **File Upload:** It uploads two files to the newly created project.  These are a JavaScript function ("hello") and a manifest file ("appsscript"). The manifest file configures the script settings, and the JavaScript function provides the script's code.

5. **Update and Print Link:** The code then updates the project's content by uploading these files. Finally, it retrieves the script ID and prints a URL to the project in Google Apps Script.

6. **Error Handling:** The `try...except` block handles potential `HttpError` exceptions that might occur during API calls. It prints the error content if any issues arise.

7. **Initialization:** The `if __name__ == '__main__':` block ensures that the `main()` function is called only when the script is executed directly, not when imported as a module.


Usage example
-------------------------
.. code-block:: python

    # ... (Import necessary modules, e.g., from pathlib import Path, etc.)
    # ... (Define relevant variables like SCOPES, SAMPLE_CODE, SAMPLE_MANIFEST)
    # ... (Define the 'gs' module and its 'path' attribute, if needed.)


    def main():
        """Calls the Apps Script API."""
        # ... (Your authentication and service build code remains the same)

        try:
            service = build('script', 'v1', credentials=creds)

            # ... (Your project creation and file upload code remains the same)
            print('https://script.google.com/d/' + response['scriptId'] + '/edit')
        except errors.HttpError as error:
            print(error.content)


    if __name__ == '__main__':
        main()