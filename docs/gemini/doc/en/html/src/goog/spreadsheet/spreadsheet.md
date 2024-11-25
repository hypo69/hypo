html
<h1>Module: hypotez/src/goog/spreadsheet/spreadsheet.py</h1>

<h2>Overview</h2>
<p>Minimal library for working with Google Sheets.</p>

<h2>Classes</h2>

<h3><code>SpreadSheet</code></h3>

<p><strong>Description</strong>: Class for working with Google Sheets. Provides methods for accessing, creating, and managing spreadsheets, and uploading data from a CSV file.</p>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>:
    <p><strong>Description</strong>: Initialize GoogleSheetHandler with specified credentials and data file.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>spreadsheet_id</code> (str): ID of the Google Sheets spreadsheet. Specify <code>None</code> to create a new Spreadsheet.</li>
      <li><code>spreadsheet_name</code> (str, optional): Name of the new Spreadsheet if <code>spreadsheet_id</code> is not specified.</li>
      <li><code>sheet_name</code> (str, optional): Name of the sheet in Google Sheets.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>gspread.exceptions.SpreadsheetNotFound</code>: If the spreadsheet with the given ID does not exist.</li>
        <li><code>Exception</code>: Any other exception during initialization.</li>

    </ul>
  </li>
  <li><code>_create_credentials</code>:
    <p><strong>Description</strong>: Create credentials from a JSON file.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>ServiceAccountCredentials</code>: Credentials for accessing Google Sheets.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
      <li><code>Exception</code>: Any error while creating credentials.</li>
  </li>
  <li><code>_authorize_client</code>:
    <p><strong>Description</strong>: Authorize client to access the Google Sheets API.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>gspread.Client</code>: Authorized client for working with Google Sheets.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
      <li><code>Exception</code>: Any error while authorizing the client.</li>
  </li>
  <li><code>get_worksheet</code>:
    <p><strong>Description</strong>: Get the worksheet by name.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>worksheet_name</code> (str): Name of the sheet in Google Sheets.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li><code>Worksheet</code>: Worksheet for working with data.</li>
        <li><code>None</code>: If the worksheet is not found and cannot be created.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
        <li><code>gspread.exceptions.WorksheetNotFound</code>: If the sheet does not exist and cannot be created.</li>
        <li><code>Exception</code>: Any other exception during the process.</li>
  </li>
  <li><code>create_worksheet</code>:
        <p><strong>Description</strong>: Creates a new worksheet.</p>
        <p><strong>Parameters</strong>:</p>
        <ul>
          <li><code>title</code> (str): The title of the new worksheet.</li>
          <li><code>dim</code> (dict, optional): Dimensions of the worksheet. Defaults to 100 rows and 10 columns.</li>
        </ul>
        <p><strong>Returns</strong>:</p>
        <ul>
            <li><code>Worksheet</code>: The created worksheet.</li>
        </ul>
        <p><strong>Raises</strong>:</p>
        <li><code>Exception</code>: If any error occurs during the creation process.</li>


  </li>
  <li><code>copy_worksheet</code>:
    <p><strong>Description</strong>: Copy worksheet by name.</p>
      <p><strong>Parameters</strong>:</p>
      <ul>
          <li><code>from_worksheet</code> (str): Name of the worksheet to copy from.</li>
          <li><code>to_worksheet</code> (str): Name of the new worksheet to be created.</li>
      </ul>
      <p><strong>Returns</strong>:</p>
      <ul>
          <li><code>Worksheet</code>: The copied worksheet.</li>
      </ul>
      <p><strong>Raises</strong>:</p>
      <ul>
        <li><code>Exception</code>: Any error during worksheet copying.</li>
      </ul>
  </li>
  <li><code>upload_data_to_sheet</code>:
    <p><strong>Description</strong>: Upload data from a CSV file to Google Sheets.</p>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li><code>ValueError</code>: If the data file path is not set or the file does not exist.</li>
      <li><code>Exception</code>: Any other exception during the upload process.</li>

    </ul>
  </li>
</ul>

<h2>Functions</h2>

<!-- No functions found in the provided code -->