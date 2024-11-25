# AliExpress Campaign Management Module

## Overview

This module provides functionality for managing AliExpress campaigns, including editing, promotional campaigns, and data handling through Google Sheets.  It utilizes various components for data preparation, organization, and interaction with external services.

## Table of Contents

- [AliExpress Campaign Management Module](#aliexpress-campaign-management-module)
- [Overview](#overview)
- [Classes](#classes)
- [Functions](#functions)
- [Dependencies](#dependencies)


## Classes

### `AliCampaignGoogleSheet`

**Description**:  A class for interacting with Google Sheets for campaign data. This class handles the specific functions for retrieving, manipulating, and storing campaign data within Google Sheets.


## Functions

### `create_campaign`

**Description**: Creates a new AliExpress campaign.

**Parameters**:
- `campaign_data` (dict):  A dictionary containing the necessary campaign details.
- `spreadsheet_id` (str):  The ID of the Google Spreadsheet to which the campaign data should be written.
- `sheet_name` (str): The name of the sheet within the Google spreadsheet.

**Returns**:
- `dict`: The campaign information with the creation details.

**Raises**:
- `GoogleSheetError`: If there are issues interacting with the Google Sheet.


### `update_campaign`

**Description**: Updates an existing AliExpress campaign.

**Parameters**:
- `campaign_id` (str): The ID of the campaign to be updated.
- `updated_data` (dict): A dictionary containing the updated details of the campaign.
- `spreadsheet_id` (str): The ID of the Google Spreadsheet to which the campaign data should be written.
- `sheet_name` (str): The name of the sheet within the Google spreadsheet.

**Returns**:
- `dict`: The campaign information with the update details, or `None` if the campaign doesn't exist.


**Raises**:
- `GoogleSheetError`: If there are issues interacting with the Google Sheet.
- `ValueError`: If the `campaign_id` is invalid.


## Dependencies

This module relies on the following external libraries and modules:

- `gspread`: For interacting with Google Sheets.
- `pandas`: For data manipulation and analysis.
- `src.settings.gs`: For configuration settings related to Google Sheets.