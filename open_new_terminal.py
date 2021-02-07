import sublime_plugin

import os
from .osx_utils import call_terminal, open_terminal_with_new_window


class OpenNewTerminalTabCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.file_name():
            filepath = os.path.dirname(
                self.view.file_name()).replace(' ', '\\\ ')
            call_terminal(run_command='cd {}'.format(filepath),
                          new_tab=True)
        else:
            call_terminal(new_tab=True)


class OpenNewTerminalWindowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.file_name():
            filepath = os.path.dirname(self.view.file_name()).replace(' ',
                                                                      '\\ ')
            open_terminal_with_new_window(filepath)
        else:
            open_terminal_with_new_window()
