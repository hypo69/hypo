rst
How to use the check_release function
========================================================================================

Description
-------------------------
This Python function, `check_latest_release`, retrieves the latest release tag of a GitHub repository.  It uses the GitHub API to fetch release information.

Execution steps
-------------------------
1. The function takes two string arguments: `owner` (the GitHub username or organization) and `repo` (the repository name).
2. It constructs a URL to the GitHub API endpoint for the latest release of the specified repository.
3. It sends a GET request to the constructed URL using the `requests` library.
4. If the request is successful (status code 200), it parses the JSON response.
5. It extracts the 'tag_name' from the parsed JSON, which represents the release version.
6. It returns the extracted tag name.
7. If the request is not successful (non-200 status code), it returns `None`.  Note that currently, no error handling is performed beyond returning `None`.


Usage example
-------------------------
.. code-block:: python

    import requests
    from hypotez.src.check_release import check_latest_release
    from hypotez.src.logger import logger

    def main():
      owner = "owner_name"  # Replace with the owner of the repo
      repo = "repo_name"    # Replace with the name of the repo

      latest_release = check_latest_release(owner, repo)

      if latest_release:
          print(f"Latest release version: {latest_release}")
      else:
          logger.error(f"Could not retrieve latest release for {owner}/{repo}")


    if __name__ == "__main__":
        main()