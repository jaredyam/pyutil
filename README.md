📦 pyutil.sublime - plugins
===========================

*Tiny commands, easy life.* A collection of tiny commands could let me code with ST3 more comfortably.

**Note:**

- All commands that invoke the terminal will open the `Terminal` application by default, thereby restricted to run on macOS only
- `create_new_file` supposes that the shell command `subl` for invoking ST3 from command line is available

## Installation

- **Git**: clone the repository in your Sublime Text "Packages" directory:

    ```bash
    git clone https://github.com/jaredyam/pyutil.git
    ```

    The "Packages" directory on macOS is located at:

    ```bash
    ~/Library/Application Support/Sublime Text 3/Packages/
    ```


## Tiny commands

|TINY COMMANDS|DESCRIPTION|
|:---:|---|
|`create_new_file`|Create a new file having the same parent directory with current view|
|`create_test_function`|Create a test function template based on the selected function name|
|`open_new_terminal_tab`|Open a new terminal tab having the same parent directory with current view|
|`open_new_terminal_window`|Open a new terminal window having the same parent directory with current view|
|`camelcase_to_snakecase`|Convert function/variable name from camelCase to snake_case|
|`snakecase_to_camelcase`|Convert function/variabel name from snake_case to camelCase|
|`generate_underline_with_hyphens`|Generate a heading underline with hyphens|
|`generate_underline_with_equals`|Generate a heading underline with equals|
|`pytest`|Run all tests or selected test_function(s) in current file|
