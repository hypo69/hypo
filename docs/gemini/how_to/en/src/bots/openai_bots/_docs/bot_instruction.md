# Usage Guide for the OpenAI Bot

This guide describes how to use the OpenAI bot.

**Available Commands:**

* **`!hi`**: Greets the user.

   * **Example:** `!hi`

* **`!train <data> <data_dir> <positive> <attachment>`**: Trains the model with the provided data.  Specify either `data` for a file, `data_dir` for a directory, or `attachment` for a file attachment.

   * **Example (using a file):** `!train my_data.txt data_dir my_dir positive my_data.csv`
   * **Example (using a directory):** `!train data_dir my_directory positive my_data_labels.json`
      * **Important:**  When using `data_dir`, make sure to include the path to the directory.  Also provide the positive data, which might be a CSV file, JSON file, or other format expected by the training process.
   * **Example (using a file attachment):**  `!train attachment data_file positive data_labels.json`
      * **Note:**  Using file attachments may vary depending on the specific bot implementation and platform.

* **`!test <test_data>`**: Tests the model with provided JSON test data.

   * **Example:** `!test test_data.json`
   * **Important:**  The `test_data.json` file should contain valid JSON representing the test data format expected by the model.  The bot will typically provide output indicating the model's performance.


* **`!archive <directory>`**: Archives files in the specified directory.

   * **Example:** `!archive my_old_data`
   * **Important:**  This command archives files within the specified directory.  The archived files often remain accessible within the system's archive.  The location and method of access may depend on the bot's configuration.


* **`!select_dataset <path_to_dir_positive> <positive>`**: Selects a dataset for training from the specified directory.

   * **Example:** `!select_dataset /path/to/my/datasets my_dataset`
   * **Important:** The `positive` parameter is a label or identifier (not necessarily the full path) to specify the data set you want to select, often determined by a naming convention in the directory.

* **`!instruction`**: Displays this instruction message.

   * **Example:** `!instruction`


**General Notes:**

* **Data Formats:** The specific data formats (`data`, `data_dir`, `test_data`, and `positive`) required by the model for training and testing depend on the model's architecture and training setup.  The instructions for the particular model will detail the expected data structures.  If the bot doesn't provide these details, refer to the model documentation or contact the bot's administrator for clarification.
* **Error Handling:**  The bot may return error messages if commands are not correctly formatted or if issues arise during execution. Please review these messages carefully.
* **Input validation:** Input checking is critical. Always double-check that the provided parameters (`data`, `data_dir`, `test_data`, etc.) are valid and meet the expectations of the model's training/testing process.

This document provides a basic usage guide. Refer to the specific documentation for the model and bot for more advanced features and options.