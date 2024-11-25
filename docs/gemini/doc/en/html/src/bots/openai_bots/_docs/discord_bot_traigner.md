html
<h1>Discord Bot Trainer Documentation</h1>

<h2>Overview</h2>
<p>This document details how to train and interact with a language model through a Discord bot. It outlines the steps for preparing training data, initiating training, monitoring progress, testing the model, and using additional commands.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#step-by-step-guide">Step-by-Step Guide</a></li>
  <li><a href="#guide-to-adding-a-q-a-command">Guide to Adding a Q&A Command</a></li>
  <li><a href="#summary">Summary</a></li>
</ul>


<h2>Step-by-Step Guide</h2>

<h3>Step 1: Ensure Bot is Running</h3>
<p>Make sure your bot is running. You should see a message in your console indicating the bot is logged in.</p>
<pre><code>
Logged in as YourBotName#1234
</code></pre>

<h3>Step 2: Invite the Bot to Your Server</h3>
<p>Ensure the bot is invited to your server with the necessary permissions to read messages and send messages.</p>


<h3>Step 3: Prepare Your Training Data</h3>
<p>You can train the model using text data or files containing the training data.</p>
<ol>
    <li>
        <strong>Training with Text Data</strong>:
        <p>Prepare a string of text data that you want to use for training.</p>
    </li>
    <li>
        <strong>Training with a File</strong>:
        <p>Prepare a file containing the training data. Ensure the file is accessible on your local machine.</p>
    </li>
</ol>


<h3>Step 4: Use the Training Command</h3>

<h4>Method 1: Using Text Data Directly</h4>
<ol>
    <li>
        In a Discord channel where the bot has access, type the following command:
        <pre><code>
!train "Your training data here" positive=True
        </code></pre>
        <p>Example:</p>
        <pre><code>
!train "Sample training data" positive=True
        </code></pre>
    </li>
</ol>

<h4>Method 2: Uploading a File</h4>
<ol>
    <li>
        Attach the file containing the training data in a message.
    </li>
    <li>
        In the same message, type the following command and send:
        <pre><code>
!train positive=True
        </code></pre>
        <p>Example:</p>
        <pre><code>
!train positive=True
        </code></pre>
    </li>
</ol>

<p>The bot will save the file and start training the model with the provided data.</p>


<h3>Step 5: Monitor Training</h3>
<p>After you send the training command, the bot should respond with a message indicating the status of the training job:</p>
<pre><code>
Model training started. Job ID: <job_id>
</code></pre>


<h3>Step 6: Verify Training Status</h3>
<p>You can add additional commands to your bot to check the status of the training job if needed. This would typically involve querying the model object for job status.</p>


<h3>Step 7: Testing the Model</h3>
<ol>
    <li>Prepare a JSON string of test data.</li>
    <li>In a Discord channel where the bot has access, type the following command:
        <pre><code>
!test {"test_key": "test_value"}
        </code></pre>
        <p>Example:</p>
        <pre><code>
!test {"input": "Test input data"}
        </code></pre>
    </li>
</ol>
<p>The bot will respond with the model's predictions.</p>


<h3>Step 8: Using Additional Commands</h3>
<p>Your bot also supports other commands such as archiving files and selecting datasets. Use these commands similarly to manage your data and model.</p>

<h4>Archiving Files</h4>
<pre><code>
!archive <directory_path>
</code></pre>
<p>Example:</p>
<pre><code>
!archive /path/to/directory
</code></pre>

<h4>Selecting Dataset</h4>
<pre><code>
!select_dataset <path_to_dir_positive> positive=True
</code></pre>
<p>Example:</p>
<pre><code>
!select_dataset /path/to/positive_data positive=True
</code></pre>

<h2>Guide to Adding a Q&A Command</h2>

<h3>Step 1: Start the Bot</h3>
<p>Make sure your bot is running.</p>

<h3>Step 2: Ask a Question</h3>
<p>In a Discord channel where the bot has access, type the following command:</p>
<pre><code>
!ask What is the capital of France?
</code></pre>

<h3>Step 3: Receive the Response</h3>
<p>The bot should respond with the model's answer:</p>
<pre><code>
Model response: The capital of France is Paris.
</code></pre>



<h2>Summary</h2>

<p>This guide details how to use the Discord bot trainer for various tasks, from data preparation to testing and managing your model.</p>