rst
How to use the profiling functions
========================================================================================

Description
-------------------------
These functions, `plot_age_distribution` and `plot_interest_distribution`, are designed to create visualizations of agent populations' characteristics.  They extract age and interest data from a list of `TinyPerson` agents and generate histograms and pie charts, respectively, to illuStarte the distribution of these attributes.  Crucially, each function returns a Pandas DataFrame containing the raw data used for plotting, allowing for further analysis or customization.

Execution steps
-------------------------
1. **Import necessary libraries:** The code begins by importing `pandas` for data manipulation, `matplotlib.pyplot` for plotting, `typing` for type hinting, and `TinyPerson` from the `tinytroupe.agent` module.

2. **Define `plot_age_distribution`:** This function takes a list of `TinyPerson` agents (`agents`), an optional title for the plot (`title`), and a boolean flag (`show`) to control whether the plot is displayed. It extracts the age values from the agents.

3. **Create a Pandas DataFrame:** A DataFrame named `df` is created from the extracted ages. The DataFrame is critical because it stores the raw data.

4. **Generate the age histogram:** The `plot.hist()` method of the `df['Age']` column is used to create a histogram.  The `bins=20` parameter controls the number of histogram bins. The plot title is set using the provided `title`.

5. **Display the plot (optional):** If `show` is `True`, the plot is displayed using `plt.show()`.

6. **Return the DataFrame:** The function returns the `df` containing the age data.

7. **Define `plot_interest_distribution`:** This function is analogous to `plot_age_distribution` but focuses on interest data. It extracts interests from the agents.

8. **Create a DataFrame (Interest Data):** A Pandas DataFrame is created from the extracted interest data, using `df["Interests"]`.

9. **Generate the interest pie chart:** A pie chart is generated using `value_counts().plot.pie()`.  This effectively counts the occurrences of each interest.

10. **Display the plot (optional):** If `show` is `True`, the plot is displayed.

11. **Return the DataFrame:** The function returns the `df` DataFrame containing the interest data.


Usage example
-------------------------
.. code-block:: python

    from tinytroupe.agent import TinyPerson  # Assuming this is defined elsewhere
    from tinytroupe.profiling import plot_age_distribution, plot_interest_distribution
    import pandas as pd
    
    # Sample data (replace with your actual agent data)
    agents = [
        TinyPerson({"age": 25, "interests": "coding"}),
        TinyPerson({"age": 30, "interests": "reading"}),
        TinyPerson({"age": 25, "interests": "coding"}),
        TinyPerson({"age": 40, "interests": "hiking"}),
    ]
    
    # Plot age distribution
    age_df = plot_age_distribution(agents, title="Age Distribution of Agents", show=True)
    print(age_df)
    
    # Plot interest distribution
    interest_df = plot_interest_distribution(agents, title="Interest Distribution", show=True)
    print(interest_df)