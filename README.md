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

|Tiny Commands|Scope|Description|
|:---:|:---:|---|
|`create_new_file`|View::File|Create new file(s) having the same parent directory with current view from input or selections|
|`create_test_function`|View::File or Selections (func_name)|Create test function(s) template based on selected function name(s)|
|`open_new_terminal_tab`|View::FIle|Open a new terminal tab having the same parent directory with current view|
|`open_new_terminal_window`|View::File|Open a new terminal window having the same parent directory with current view|
|`camelcase_to_snakecase`|View::Selections (func_name)|Convert function/variable name(s) from camelCase to snake_case|
|`snakecase_to_camelcase`|View::Selections (func_name)|Convert function/variable name(s) from snake_case to camelCase|
|`generate_underline_with_hyphens`|View::Selections (Doc-string)|Generate heading underline(s) with hyphens|
|`generate_underline_with_equals`|View::Selections (Doc-string)|Generate heading underline(s) with equals|
|`generate_underline_with_right_angle_brackets`|View::Selections (Doc-string)|Generate heading underline(s) with right angle brackets|
|`run_pytest`|View::File or Selections (func_name)|Run all tests or selected test_function(s) in the current view from terminal|
|`run_file`|View::File|Run current view of Python file from terminal|
|`split_into_lines_cursor_at_head`|View::Selections|Split selected regions into separated lines and place the cursor at the beginning of each line|
