html
<h1>Module bully</h1>

<h2>Overview</h2>
<p>This module provides a function to generate hate speech examples from the perspective of a bully using the OpenAI API. It utilizes a system prompt to instruct the model to write like a bully, focusing on intimidation tactics and structured JSON output.</p>

<h2>Variables</h2>

<h3><code>MODE</code></h3>

<p><strong>Description</strong>: A variable to control the mode (currently set to 'dev').</p>


<h2>Functions</h2>

<h3><code>bully</code></h3>

<p><strong>Description</strong>: Generates a hate speech example from the perspective of a bully using the OpenAI API.</p>

<p><strong>Parameters</strong>:</p>
<ul>
  <li><code>user_message</code> (str): The user's initial message (default is "Hello!").  Used to prompt the model.</li>
  <li><code>messages</code> (list, optional):  A list of messages for the chat completion context (default is a list containing the system prompt).  Typically, you'd initialize this with the system prompt.  Providing additional messages here may further shape the response.</li>
</ul>

<p><strong>Returns</strong>:</p>
<ul>
  <li><code>messages</code> (list): A list of messages including the generated hate speech example.</li>
</ul>

<p><strong>Raises</strong>:</p>
<ul>
  <li><code>Exception</code>:  Any exceptions that may be raised by the <code>openai.ChatCompletion.create()</code> method.  This needs to be more specific.  What kinds of exceptions are possible?</li>
</ul>


<p><strong>Code Example</strong>:</p>

<pre><code class="language-python">
import os
import openai

# ... (initialize openai API key, etc.) ...

system_prompt = """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""

user_message = "Describe how a bully might intimidate someone."

messages = [{"system": "user", "content": system_prompt}]  # Initialize the message list

response = bully(user_message=user_message, messages=messages)

print(response)
</code></pre>


<p><strong>Important Considerations</strong>:</p>
<ul>
<li><strong>Error Handling</strong>:  The provided code lacks robust error handling.  It's crucial to include <code>try...except</code> blocks to catch potential errors (e.g., API errors, invalid inputs) and handle them gracefully, rather than just letting exceptions propagate.</li>
<li><strong>Security</strong>:  Be extremely cautious about how you use this code, as it has the potential to generate harmful content.  Use it responsibly.</li>
<li><strong>OpenAI API Key</strong>: The placeholder <code>"YOUR_API_KEYS_OPENAI"</code> needs to be replaced with your actual OpenAI API key.  Store this securely and avoid hardcoding it into the code for production environments.</li>
<li><strong>Input Validation</strong>: Consider validating the input <code>user_message</code> to ensure it's appropriate and doesn't lead to unwanted outputs.</li>
</ul>