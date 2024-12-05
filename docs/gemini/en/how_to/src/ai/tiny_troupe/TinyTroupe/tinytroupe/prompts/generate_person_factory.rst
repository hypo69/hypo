rst
How to use this code block for generating person contexts
=========================================================================================

Description
-------------------------
This code block describes a process for generating a list of person contexts.  It takes a broad description of desired characteristics (e.g., demographics, physical characteristics, behaviors, beliefs) and creates a series of more specific contexts derived from that base. Each context is designed to be fed into a system that generates a detailed person description.

Execution steps
-------------------------
1. **Input the broad context**: The user provides a description of the desired characteristics for the people to be generated (e.g., location, age range, socioeconomic status, religious views, marital status, children, profession, employment).


2. **Process the input**: The system analyzes the broad context and identifies key elements (e.g., location, age, occupation).


3. **Generate variations**: The system generates different contexts, each focusing on a specific combination of details from the broad context.  For example, if the broad context mentioned "Latin American" and "professional," the system might generate specific contexts like "Mexican lawyer" or "Colombian doctor."  These contexts are more detailed than the broad description.


4. **Output the contexts as JSON array**: The system returns an array of strings, where each string is a context suitable for generating a person's description.

Usage example
-------------------------
.. code-block:: python

    # Example of how to use the function
    def generate_person_contexts(broad_context):
        """
        Generates a list of contexts for creating person descriptions.

        Args:
            broad_context (str):  A description of the desired characteristics.

        Returns:
            list: A list of strings, each representing a context.  Returns an empty list if input is invalid or empty.
        """
        
        #  (This section needs to be replaced with the actual code logic)
        #  Example of basic filtering and formatting to illustrate the concept.
        
        if not isinstance(broad_context, str) or not broad_context:
            return []
        
        contexts = []
        if "Latin American" in broad_context and "professional" in broad_context:
            contexts.append("Mexican person that has formed as lawyer but now works in other are, is single, like sports and movies")
            contexts.append("Colombian person that is a lawyer, like to read and drink coffee and is married with 2 children.")
        elif "Brazilian" in broad_context and "doctor" in broad_context:
            contexts.append("Create a Brazilian person that is a doctor, like pets and the nature and love heavy metal.")


        return contexts

    broad_context = "Latin American, age between 20 and 40 years old, economic status can vary between poor and rich, it can be religious or not, it can be married or not, it have children or not, it can be a professional or not, it can be a worker or not"
    person_contexts = generate_person_contexts(broad_context)

    #Print to verify
    import json
    print(json.dumps(person_contexts, indent=2))