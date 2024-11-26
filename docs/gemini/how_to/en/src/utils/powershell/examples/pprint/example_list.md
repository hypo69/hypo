How to use the `pprint` module in PowerShell to pretty-print a list.

The input is a list: `["a","b","c"]`.

**Method 1: Using `-InputObject` and `Format-List`**

This method is simple and directly uses the `-InputObject` parameter for the list.


```powershell
$list = '["a","b","c"]'  # Your input string
$list = [System.Collections.ArrayList]::new()
$list += 'a'
$list += 'b'
$list += 'c'


$list | Format-List
```

This will output the list in a formatted way, with each element on a separate line:

```
a
b
c
```


**Method 2: Using `ConvertFrom-StringData` and `Format-List`**


This method is slightly more involved, but useful when your input is a string representation of a list that needs to be parsed.

```powershell
$listString = '["a","b","c"]'
$list = ConvertFrom-StringData $listString
$list | Format-List
```

This will output the list in a formatted way.


**Explanation:**

* `ConvertFrom-StringData` parses the string representation of the list into a PowerShell object.
* `Format-List` is a PowerShell cmdlet to format the data in a human-readable way.


**Note:**

The first method is generally more suitable when you directly have the list as a PowerShell variable, while the second method is better if the list is parsed from a string. The first method is more efficient as it doesn't need to parse the string. The output is similar in both methods.


**Further Enhancements (if needed):**


* If you need a specific output format (e.g., a JSON output), use the `ConvertTo-Json` cmdlet:

```powershell
$list | ConvertTo-Json
```


* If you want a more customizable output, the `Write-Host` cmdlet (or the `-Format` parameter) along with some string formatting (`-f` operator) can provide that:


```powershell
$list | ForEach-Object {Write-Host "Item: $($_.ToString())"}
```


Choose the method that best suits your specific input and desired output format. Remember to replace `"a"`, `"b"`, and `"c"` with your actual list elements.