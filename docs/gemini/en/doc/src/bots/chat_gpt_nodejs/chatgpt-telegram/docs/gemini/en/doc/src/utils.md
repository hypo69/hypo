# utils.js

## Overview

This module provides an asynchronous function for removing a file.


## Functions

### `removeFile`

**Description**:  This function asynchronously removes a file at the specified path.  Handles potential errors during the unlink operation.

**Parameters**:

- `path` (string): The path to the file to be removed.


**Returns**:

- `void`: The function does not return a value.


**Raises**:

- `Error`:  An error occurs during the file removal process, such as if the file does not exist or if the user lacks permissions to delete it.  Error information is logged to the console.


```javascript
import { unlink } from 'fs/promises'
export async function removeFile(path) {
    try {
        await unlink(path)
    } catch (e) {
        console.log('Error while removing file', e.message)
    }
}
```