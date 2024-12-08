# tinytroupe/profiling.py

## Overview

This module provides functions for profiling agent populations, such as plotting age and interest distributions.  It includes functions to visualize and return data for plotting the age and interest distributions of agents.

## Table of Contents

* [plot_age_distribution](#plot_age_distribution)
* [plot_interest_distribution](#plot_interest_distribution)

## Functions

### `plot_age_distribution`

**Description**: Plots the age distribution of a list of `TinyPerson` agents.

**Parameters**:
- `agents` (List[TinyPerson]): A list of `TinyPerson` agents.
- `title` (str, optional): The title of the plot. Defaults to "Age Distribution".
- `show` (bool, optional): Whether to display the plot. Defaults to True.

**Returns**:
- `pd.DataFrame`: A Pandas DataFrame containing the age data used for plotting.

**Raises**:
- `TypeError`: If input `agents` is not a list.
- `TypeError`: If any element in the `agents` list is not a `TinyPerson` object.


### `plot_interest_distribution`

**Description**: Plots the interest distribution of a list of `TinyPerson` agents.

**Parameters**:
- `agents` (List[TinyPerson]): A list of `TinyPerson` agents.
- `title` (str, optional): The title of the plot. Defaults to "Interest Distribution".
- `show` (bool, optional): Whether to display the plot. Defaults to True.

**Returns**:
- `pd.DataFrame`: A Pandas DataFrame containing the interest data used for plotting.

**Raises**:
- `TypeError`: If input `agents` is not a list.
- `TypeError`: If any element in the `agents` list is not a `TinyPerson` object.