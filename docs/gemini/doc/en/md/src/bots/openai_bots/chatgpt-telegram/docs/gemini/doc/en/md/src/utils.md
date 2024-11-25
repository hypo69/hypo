# utils.js

## Overview

This module provides a function for removing files asynchronously.

## Table of Contents

* [removeFile](#removefile)


## Functions

### `removeFile`

**Description**: Removes a file asynchronously.

**Parameters**:
- `path` (string): The path to the file to be removed.


**Returns**:
- `void`:  The function does not return a value.

**Raises**:
- `Error`: An error is raised if there's a problem removing the file.  The error message will be logged to the console.

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