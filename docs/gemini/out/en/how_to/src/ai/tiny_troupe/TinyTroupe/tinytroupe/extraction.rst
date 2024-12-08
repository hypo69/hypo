rst
How to use the ResultsExtractor class
========================================================================================

Description
-------------------------
This code defines a `ResultsExtractor` class for extracting data from TinyTroupe elements (agents and worlds).  It utilizes OpenAI's API to generate structured results based on a prompt template and the interaction history of agents or a world.  The class caches extraction results for efficiency and provides a method to save these results in JSON format.  It also includes a `ResultsReducer` class that allows defining custom rules to reduce the extracted data.


Execution steps
-------------------------
1. **Initialization:** Create a `ResultsExtractor` object.  This object will handle the extraction process.

2. **Extract results from an agent:**
   - Call the `extract_results_from_agent` method, providing the `tinyperson` object, the desired `extraction_objective`, `situation`, and potentially a `fields` list or `fields_hints` dictionary to specify the desired output structure.   Set `verbose` to `True` for debug messages.

3. **Extract results from a world:**
   - Call the `extract_results_from_world` method with the `tinyworld` object and the desired `extraction_objective`, `situation`, `fields` (optional), and `fields_hints` (optional).   Set `verbose` to `True` for debug messages.

4. **Save results:** Call the `save_as_json` method to save the extracted results (from agents and world) to a JSON file.


Usage example
-------------------------
.. code-block:: python

    import logging
    from tinytroupe.agent import TinyPerson
    from tinytroupe.environment import TinyWorld
    from tinytroupe.extraction import ResultsExtractor, Normalizer

    # Configure logging (optional)
    logging.basicConfig(level=logging.INFO)

    # Assume you have a TinyPerson object named 'my_agent' and a TinyWorld object named 'my_world'
    extractor = ResultsExtractor()
    agent_results = extractor.extract_results_from_agent(
        tinyperson=my_agent, extraction_objective="Summary of interactions", situation="Normal conversation", verbose=True
    )
    world_results = extractor.extract_results_from_world(
        tinyworld=my_world, extraction_objective="Overall world summary", verbose=True
    )

    if agent_results and world_results:
        extractor.save_as_json("extraction_results.json", verbose=True)
        print("Extraction results saved to extraction_results.json")

    # Example of Normalizer usage (assuming you have some elements to normalize):
    normalizer = Normalizer(elements=["element1", "element2"], n=2) # Use specific n
    normalized_elements = normalizer.normalize(["element1", "element2"])
    print("Normalized elements:", normalized_elements)