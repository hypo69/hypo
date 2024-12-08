rst
How to use the TinyTool class
========================================================================================

Description
-------------------------
This code defines the `TinyTool` class, a base class for specialized tools that agents can use.  It handles basic functionalities like checking for real-world side effects, enforcing ownership, and processing actions.  Subclasses must implement `_process_action`, `actions_definitions_prompt`, and `actions_constraints_prompt` to define their specific behavior.  The code also includes example subclasses `TinyCalendar` and `TinyWordProcessor`.

Execution steps
-------------------------
1. **Initialization:** Create a `TinyTool` object, specifying the tool's name, description, owner (optional), whether it has real-world side effects, and associated exporters and enrichers (optional).  
2. **Processing actions:**  Call the `process_action` method to execute an action.  This method internally checks for real-world side effects, enforces ownership (if specified), and then calls the `_process_action` method to perform the tool's specific actions.
3. **Subclasses define specific actions:** Subclasses implement the `_process_action` method to handle specific tasks.  For example, `TinyCalendar` handles adding events, and `TinyWordProcessor` handles writing documents.
4. **Defining tool capabilities:** Subclasses define prompts for actions using `actions_definitions_prompt` and `actions_constraints_prompt` to describe what actions they can perform and any constraints for those actions.


Usage example
-------------------------
.. code-block:: python

    import logging
    import json
    
    import tinytroupe.utils as utils
    from tinytroupe.extraction import ArtifactExporter
    from tinytroupe.enrichment import TinyEnricher
    from tinytroupe.tools import TinyTool, TinyWordProcessor

    # Example usage for TinyWordProcessor
    # Create an exporter (replace with your actual exporter)
    class DummyExporter(ArtifactExporter):
        def export(self, artifact_name, artifact_data, content_type, content_format, target_format):
            print(f"Exported {artifact_name} ({content_type}) to {target_format}")
            # Perform actual export logic here

    exporter = DummyExporter()
    
    # Create a TinyWordProcessor instance.  (assuming necessary imports)
    wordprocessor = TinyWordProcessor(exporter=exporter)

    # Prepare an action (a JSON-formatted dictionary) to process.
    action = {
        'type': 'WRITE_DOCUMENT',
        'content': json.dumps({
            'title': 'My Important Document',
            'content': 'This is a document written using TinyWordProcessor',
            'author': 'AgentBob'
        })
    }

    # Execute the action.
    result = wordprocessor.process_action(agent=None, action=action)  # agent parameter is place-holder

    # Check the result.
    if result:
        print("Document successfully written.")
    else:
        print("Document writing failed.")