# Training and Using Your Discord Bot's Trained Model

This guide details how to train your model, test its performance, and interact with it through your Discord bot.

## Training Your Model

### Step-by-Step Guide

#### Step 1: Ensure Bot is Running

Verify that your bot is running.  Look for a console message confirming the bot's login, like this:

```plaintext
Logged in as YourBotName#1234
```

#### Step 2: Invite the Bot to Your Server

Add the bot to the Discord server you want to use. Ensure it has the necessary permissions, specifically to read and send messages.

#### Step 3: Prepare Your Training Data

Prepare your training data.  This can be text or a file.

1. **Training with Text Data:**  Prepare a string containing the text you want to use for training.

2. **Training with a File:**  Prepare a file containing your training data.  Make sure the file is accessible on your local machine.

#### Step 4: Use the Training Command

**Method 1: Using Text Data Directly**

1. In a Discord channel, type the following command, replacing `"Your training data here"` with your actual text:

   ```plaintext
   !train "Your training data here" positive=True
   ```

   Example:

   ```plaintext
   !train "Sample training data" positive=True
   ```


**Method 2: Uploading a File**

1. Attach the training data file to your message.
2. In the same message, type the following command:

   ```plaintext
   !train positive=True
   ```

   Example:

   ```plaintext
   !train positive=True
   ```

The bot will save the file and begin training.

#### Step 5: Monitor Training

After sending the training command, the bot will respond with a message like this, indicating the training job's progress:

```plaintext
Model training started. Job ID: <job_id>
```

#### Step 6: Verify Training Status (Optional)

If needed, add commands to check the status of the training job.  This typically involves querying the model object for its status.


#### Step 7: Testing the Model

Once training is complete, test the model with the `!test` command.

1. Prepare a JSON string containing your test data.

2. In a Discord channel, type the following command, replacing `{"test_key": "test_value"}` with your actual test data:

   ```plaintext
   !test {"test_key": "test_value"}
   ```

   Example:

   ```plaintext
   !test {"input": "Test input data"}
   ```

The bot will respond with the model's predictions.


#### Step 8: Managing Data (Optional)

Use the `!archive` and `!select_dataset` commands for managing your data and model as needed.


```plaintext
!archive <directory_path>
```

Example:

```plaintext
!archive /path/to/directory
```


```plaintext
!select_dataset <path_to_dir_positive> positive=True
```

Example:

```plaintext
!select_dataset /path/to/positive_data positive=True
```


### Summary

1.  **Start Bot:** Ensure your bot is running.
2.  **Invite Bot:** Add the bot to your Discord server.
3.  **Prepare Data:** Have your training data ready.
4.  **Train Model:** Use the `!train` command with your data.
5.  **Monitor Training:** Watch for the bot's training status message.
6.  **Test Model:** Use `!test` with sample data.
7.  **Manage Data:** Use `!archive` and `!select_dataset` as needed.


## Interacting with Your Trained Model (Q&A)

### Adding a Q&A Command

1.  **Start the Bot:** Make sure your bot is running.

2.  **Ask a Question:** In a Discord channel, type the `!ask` command followed by your question.

    ```plaintext
    !ask What is the capital of France?
    ```

3.  **Receive the Response:** The bot will respond with the model's answer:

    ```plaintext
    Model response: The capital of France is Paris.
    ```

### Summary

1.  **Add `ask` Command:** Modify your bot script to include the `ask` command and implement the `ask` method in your `Model` class to query the model and return a response.
2.  **Run the Bot:** Start your bot.
3.  **Ask Questions:** Use the `!ask` command to interact with your trained model.


This comprehensive guide provides clear instructions for training, testing, and interacting with your Discord bot's trained model. Remember to adapt the commands and file paths to your specific setup.