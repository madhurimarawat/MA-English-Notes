"""
Project Directory Tree Generator
=================================

Author: Madhurima Rawat

Description
-----------
This script recursively displays the complete directory structure of a
project or repository in a tree-like format.

It uses Python's built-in `os` module to:

- Read files and folders from a specified directory.
- Sort directory contents alphabetically.
- Display files and folders using tree-style connectors.
- Recursively enter subdirectories and display their contents.
- Use indentation and vertical lines to visually represent the
  parent-child relationship between folders and files.

Example output
--------------
📂 Project Structure:

├── README.md
├── Directory_Structure.md
├── Final_Year
│   ├── Notes
│   │   ├── 1_British_Literature
│   │   └── 2_Indian_Writings_in_English
│   │       └── Syllabus.txt
└── Previous_Year
    └── Notes

How to use
----------
1. Place this script inside your project/repository, or run it from
   another location.
2. Set `folder_path` to the directory whose structure you want to display.
3. Run the script.
4. The complete directory tree will be printed in the terminal.

For the current directory, use:

    folder_path = "."

For a specific folder, use:

    folder_path = "path/to/your/folder"

Notes
-----
- `.` represents the current working directory.
- The script does not modify, create, or delete any files.
- It only reads directory names and file names and prints their structure.
- Hidden files and folders are included if they are returned by
  `os.listdir()`.
"""

import os


def print_tree(start_path, prefix=""):
    """
    Recursively print the directory structure in a tree-like format.

    Parameters
    ----------
    start_path : str
        The path of the directory whose contents should be displayed.

    prefix : str, optional
        The indentation/prefix used to visually represent the current
        level of the directory tree. It is automatically updated during
        recursive calls.

    How it works
    ------------
    1. Gets all files and folders inside `start_path`.
    2. Sorts them alphabetically for consistent output.
    3. Loops through every item.
    4. Determines whether the item is the last item in the directory.
    5. Selects the appropriate tree connector:
       - `├──` for an item that is not last.
       - `└──` for the last item.
    6. Prints the item name.
    7. If the item is a directory, the function calls itself recursively
       to display everything inside that directory.
    """

    # Get all files and directories inside the current directory
    # and sort them alphabetically.
    files = sorted(os.listdir(start_path))

    # Process each item in the directory.
    for index, name in enumerate(files):

        # Create the complete path of the current item.
        path = os.path.join(start_path, name)

        # Check whether this is the final item in the current directory.
        is_last = index == len(files) - 1

        # Choose the appropriate tree connector.
        #
        # ├── means there are more items after this one.
        # └── means this is the final item at this level.
        connector = "└── " if is_last else "├── "

        # Print the current item with its indentation and connector.
        print(prefix + connector + name)

        # If the current item is a directory, recursively print
        # everything inside it.
        if os.path.isdir(path):

            # Keep the tree aligned correctly for the next level.
            #
            # If this is the last item, no vertical line is required.
            # Otherwise, │ keeps the visual connection with the
            # remaining items at the current level.
            extension = "    " if is_last else "│   "

            # Recursively process the directory.
            print_tree(path, prefix + extension)


if __name__ == "__main__":
    """
    Main program entry point.

    The code inside this block runs only when this Python file is
    executed directly. It will not run automatically if the file is
    imported as a module into another Python program.
    """

    # "." represents the current working directory.
    #
    # Change this value if you want to generate a tree for a
    # different project/repository folder.
    folder_path = "."

    # Print a heading before displaying the directory tree.
    print("📂 Project Structure:\n")

    # Start generating and printing the directory tree.
    print_tree(folder_path)
