**Prompt:**

Generate documentation in `rst` format for each input Python file, following these requirements:

- Use `reStructuredText (rst)` with appropriate headers.
- Include a brief description and `.. toctree::` for each file.
- Document all classes and functions using `autoclass`, `autofunction` directives.
- Use the comment format for functions and methods:
  ```python
  def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
      """
      Args:
          param (str): Description of the `param` parameter.
          param1 (Optional[str | dict | str], optional): Description of `param1`, default is `None`.
  
      Returns:
          dict | None: Description of return value.
  
      Raises:
          SomeError: Description of the exception.
      """
  ```
- Use `ex` in exception handling blocks.
- Provide only! the `rst` code, no explanations or additional text!!!