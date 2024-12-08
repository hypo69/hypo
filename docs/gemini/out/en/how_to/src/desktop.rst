rst
How to use this code block
=========================================================================================

Description
-------------------------
This code block defines the properties of a Windows desktop file entry.  Specifically, it's a `.desktop` file (used for creating shortcuts on Windows).  It's usually part of a file named `desktop.ini` in a folder. The code snippet specifies an icon and sets the folder type to "Generic".

Execution steps
-------------------------
1. **`[ShellClassInfo]` section**: Defines properties related to the file's appearance and behavior (e.g., icon).
2. **`IconResource=C:\\WINDOWS\\System32\\SHELL32.dll,300`**: This line specifies that the file uses the icon resource from the SHELL32.dll file. The number `300` refers to the index of the icon within that resource file.
3. **`[ViewState]` section**: Contains information related to the file's view state, such as how it's displayed.
4. **`Mode=\nVid=\nFolderType=Generic`**: This part of the `ViewState` section sets properties for how the folder is displayed. Notably, `FolderType=Generic` indicates the folder's type.


Usage example
-------------------------
.. code-block:: ini

    [.ShellClassInfo]
    IconResource=C:\\WINDOWS\\System32\\SHELL32.dll,300
    [ViewState]
    Mode=
    Vid=
    FolderType=Generic