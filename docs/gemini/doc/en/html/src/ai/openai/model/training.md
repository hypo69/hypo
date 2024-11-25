html
<h1>hypotez/src/ai/openai/model/training.py</h1>

<h2>Overview</h2>
<p>This module defines the <code>OpenAIModel</code> class for interacting with the OpenAI API, managing model training, and handling communication with the model.</p>

<h2>Classes</h2>

<h3><code>OpenAIModel</code></h3>

<p><strong>Description</strong>: This class provides methods for interacting with the OpenAI API, managing assistants, fetching models, handling dialogues, and training the model.</p>

<p><strong>Attributes</strong>:</p>
<ul>
  <li><code>model</code> (str): The OpenAI model ID to use. Defaults to "gpt-4o-mini".</li>
  <li><code>client</code> (OpenAI): An OpenAI client object for interacting with the API.</li>
  <li><code>current_job_id</code> (str): The ID of the current training job.</li>
  <li><code>assistant_id</code> (str): The ID of the assistant to use.</li>
  <li><code>assistant</code> (SimpleNamespace): The assistant object.</li>
  <li><code>thread</code> (object): The OpenAI thread object for managing conversations.</li>
  <li><code>system_instruction</code> (str): A system instruction to provide to the model.</li>
  <li><code>dialogue_log_path</code> (str | Path): Path to the file for saving the dialogue log.</li>
  <li><code>dialogue</code> (List[Dict[str, str]]): List to store the dialogue history.</li>
  <li><code>assistants</code> (List[SimpleNamespace]): A list of available assistants.</li>
  <li><code>models_list</code> (List[str]): A list of available model IDs.</li>
</ul>

<p><strong>Methods</strong>:</p>
<ul>
  <li><code>__init__</code>(system_instruction: str = None, model_name:str = 'gpt-4o-mini', assistant_id: str = None):
    <p><strong>Description</strong>: Initializes the <code>OpenAIModel</code> object with an OpenAI API key, assistant ID, and optional system instruction.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>system_instruction</code> (str, optional): An optional system instruction for the model.</li>
      <li><code>model_name</code> (str): The OpenAI model ID to use.</li>
      <li><code>assistant_id</code> (str, optional): An optional assistant ID. Defaults to a pre-defined assistant ID.
      </li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Errors related to API key or assistant retrieval.</li>
    </ul>
  </li>
  <li><code>list_models</code>() -> List[str]:
    <p><strong>Description</strong>: Fetches and returns a list of available OpenAI models.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>List[str]: A list of model IDs.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Exception: If an error occurs while fetching models.</li>
    </ul>
  </li>
  <li><code>list_assistants</code>() -> List[str]:
    <p><strong>Description</strong>: Loads and returns a list of available assistant names.</p>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>List[str]: A list of assistant names.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Exception: If an error occurs while loading assistants.</li>
    </ul>
  </li>
  <li><code>set_assistant</code>(assistant_id: str):
    <p><strong>Description</strong>: Sets the assistant using the provided assistant ID.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>assistant_id</code> (str): The ID of the assistant to set.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Exception: If an error occurs while setting the assistant.</li>
    </ul>
  </li>
  <li><code>_save_dialogue</code>():
    <p><strong>Description</strong>: Saves the entire dialogue to the specified JSON file.</p>
  </li>
  <li><code>determine_sentiment</code>(message: str) -> str:
    <p><strong>Description</strong>: Determines the sentiment of a given message.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>message</code> (str): The message to analyze.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>str: The sentiment (\'positive\', \'negative\', or \'neutral\').</li>
    </ul>
  </li>  
  <li><code>ask</code>(message: str, system_instruction: str = None, attempts: int = 3) -> str:
      <!-- ... (Method details) ... -->
  </li>
    <li><code>describe_image</code>(image_path: str | Path, prompt: Optional[str] = None, system_instruction: Optional[str] = None) -> str:
        <!-- ... (Method details) ... -->
    </li>
    <li><code>describe_image_by_requests</code>(image_path: str | Path, prompt: str = None) -> str:
      <!-- ... (Method details) ... -->
  </li>  
  <li><code>dynamic_train</code>():
      <!-- ... (Method details) ... -->
  </li>
  <li><code>train</code>(data: str = None, data_dir: Path | str = None, data_file: Path | str = None, positive: bool = True) -> str | None:
    <p><strong>Description</strong>: Trains the model on the specified data or directory.</p>
    <p><strong>Parameters</strong>:</p>
    <ul>
      <li><code>data</code> (str, optional): Path to a CSV file or CSV-formatted string with data.</li>
      <li><code>data_dir</code> (Path | str, optional): Directory containing CSV files for training.</li>
      <li><code>data_file</code> (Path | str, optional): Path to a single CSV file with training data.</li>
      <li><code>positive</code> (bool, optional): Whether the data is positive or negative. Defaults to True.</li>
    </ul>
    <p><strong>Returns</strong>:</p>
    <ul>
      <li>str | None: The job ID of the training job or None if an error occurred.</li>
    </ul>
    <p><strong>Raises</strong>:</p>
    <ul>
      <li>Exception: If an error occurs during training.</li>
    </ul>
  </li>
  <li><code>save_job_id</code>(job_id: str, description: str, filename: str = "job_ids.json"):
      <!-- ... (Method details) ... -->
  </li>
</ul>

<h2>Functions</h2>

<h3><code>main</code>()</h3>

<p><strong>Description</strong>: This function initializes the <code>OpenAIModel</code>, demonstrates usage of its methods (fetching models, assistants, asking questions, training), and performing dynamic training. Also includes an example of saving the training job ID.</p>

<p><strong>Raises</strong>:</p>
<ul>
  <li>Any exceptions raised by the methods it calls.</li>
</ul>

<p><strong>Example Usage</strong> (within the <code>main</code> function):</p>
<ul>
<li>Initialization: <code>model = OpenAIModel(...)</code></li>
<li>Fetching models/assistants: <code>model.list_models</code>, <code>model.list_assistants</code></li>
<li>Sending a message: <code>response = model.ask(user_input)</code></li>
<li>Dynamic training: <code>model.dynamic_train()</code></li>
<li>Training: <code>training_result = model.train(...)</code></li>
<li>Saving job ID: <code>model.save_job_id(...)</code></li>
<li>Image description: <code>description = model.describe_image(...)</code></li>


</ul>